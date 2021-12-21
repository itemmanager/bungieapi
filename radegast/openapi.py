import abc
import dataclasses as dt
import typing as t
from collections import defaultdict
from enum import Enum

from svarog.tools import camel_to_snake
from svarog.types import Forge
from .svarog import svarog
from .tools import to_camel_case

Method: t.TypeAlias = t.Literal["get", "post"]


class ParameterSource(Enum):
    PATH = "path"
    QUERY = "query"


@dt.dataclass(frozen=True)
class Reference:
    ref: str
    required: bool = False

    @property
    def class_name(self) -> str:
        assert self.ref.startswith("#/definitions")
        return f"'{self.ref.split('/')[-1].replace('.', '')}'"

    @staticmethod
    def filter(
        t: t.Type["IntegerType"], data: t.Mapping, forge: Forge
    ) -> t.Mapping[str, t.Any]:
        return fix(data, {"$ref": "ref"})


class ApiType(Enum):
    INTEGER = "integer"
    STRING = "string"
    BOOLEAN = "boolean"
    ARRAY = "array"
    OBJECT = "object"


@dt.dataclass(frozen=True)
class Schema(abc.ABC):
    types: t.ClassVar[t.Mapping[ApiType, "Schema"]] = {}
    type: t.ClassVar[ApiType]
    required: bool = False

    def __init_subclass__(cls, type: ApiType, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.types[type] = cls
        cls.type = type

    @staticmethod
    def forge(t: t.Type["Schema"], data: t.Mapping, forge: Forge) -> "Schema":

        cls = Schema.types[ApiType(data["type"])]
        return forge(cls, data)




@dt.dataclass(frozen=True)
class Boolean(Schema, type=ApiType.BOOLEAN):
    ...

class StringFormat(Enum):
    DATE_TIME = "date-time"


@dt.dataclass(frozen=True)
class String(Schema, type=ApiType.STRING):
    format: t.Optional[StringFormat] = None


class IntegerFormat(Enum):
    INT32 = "int32"
    INT64 = "int64"
    UINT32 = "uint32"
    UINT64 = "uint64"
    BYTE = "byte"


def fix(
    data: t.Mapping[str, t.Any], replacements: t.Mapping[str, str]
) -> t.Mapping[str, t.Any]:
    return {replacements.get(k, k): v for k, v in data.items()}


@dt.dataclass(frozen=True)
class Integer(Schema, type=ApiType.INTEGER):
    format: t.Optional[IntegerFormat] = None
    enum_reference: t.Optional[Reference] = None

    @staticmethod
    def filter(
        t: t.Type["Integer"], data: t.Mapping, forge: Forge
    ) -> t.Mapping[str, t.Any]:
        return fix(data, {"x-enum-reference": "enum_reference"})


@dt.dataclass(frozen=True)
class Object(Schema, type=ApiType.OBJECT):
    properties: t.Optional[t.Mapping[str, t.Union[Reference, Schema]]] = None
    additional_properties: t.Union[Reference, Schema, None] = None


def forge_regerence_or_schema(
    t: t.Union[Reference, Schema], data: t.Mapping[str, t.Any], forge: Forge
) -> t.Union[Reference, Schema]:
    if "$ref" in data:
        return forge(Reference, data)
    return forge(Schema, data)


svarog.register_forge(t.Union[Reference, Schema], forge_regerence_or_schema)
svarog.register_forge(t.Union[Reference, Schema, None], forge_regerence_or_schema)


@dt.dataclass(frozen=True)
class Array(Schema, type=ApiType.ARRAY):
    items: t.Union[Reference, Schema] = dt.field(default_factory=list)


@dt.dataclass(frozen=True)
class Parameter:
    name: str
    in_: ParameterSource
    description: str
    type: Schema

    @staticmethod
    def forge(t: t.Type["Parameter"], data: t.Mapping, forge: Forge) -> "Parameter":
        return t(
            name=data["name"],
            in_=data["in"],
            description=data.get("description", ""),
            type=forge(Schema, data),
        )

    @property
    def python_name(self) -> str:
        return camel_to_snake(self.name)

@dt.dataclass(frozen=True)
class Response:
    description: str
    schema: Schema




@dt.dataclass(frozen=True)
class Operation:
    operation_id: str
    parameters: t.Sequence[Parameter]
    responses: t.Mapping[str, Response]
    deprecated: bool = False
    description: t.Optional[str] = None



class Scheme(Enum):
    HTTP = "http"
    HTTPS = "https"


@dt.dataclass(frozen=True)
class Info:
    title: t.Optional[str] = None
    description: t.Optional[str] = None
    terms_of_service: t.Optional[str] = None
    version: t.Optional[str] = None


@dt.dataclass(frozen=True)
class BindOperation(Operation):
    path: str = ""
    method: Method = "get"

    @classmethod
    def bind(cls, path: str, method: Method, operation: Operation) -> "BindOperation":
        return BindOperation(path=path, method=method, **operation.__dict__)

    @property
    def name(self):
        return to_camel_case(self.python_name)

    @property
    def python_name(self):
        return camel_to_snake(self.operation_id.split(".")[-1])


@dt.dataclass(frozen=True)
class OperationTree:
    name: str
    children: t.Sequence[t.Union[BindOperation, "OperationTree"]]

    @classmethod
    def from_mapping(
        cls, name: str, by_id: t.Mapping[str, t.Union[BindOperation, "OperationTree"]]
    ):
        children = defaultdict(dict)
        my = []
        for operation_id, operation in by_id.items():
            if "." not in operation_id:
                my.append(operation)
            else:
                group, rest = operation_id.split(".", 2)
                children[group][rest] = operation
        return OperationTree(
            name=name,
            children=[
                *my,
                *(
                    OperationTree.from_mapping(name, by_id)
                    for name, by_id in children.items()
                ),
            ],
        )


@dt.dataclass(frozen=True)
class OpenApi:
    swagger: str
    info: Info
    host: str
    base_path: str
    schemes: t.Sequence[Scheme]
    paths: t.Mapping[str, t.Mapping[Method, Operation]]

    def operations_tree(self) -> OperationTree:
        def fix_operation_id(operation_id) -> str:
            if operation_id.startswith("."):
                return operation_id[1:]
            return operation_id

        by_id = {
            fix_operation_id(operation.operation_id): BindOperation.bind(
                path, method, operation
            )
            for path, operation_map in self.paths.items()
            for method, operation in operation_map.items()
            if not operation.deprecated
        }
        return OperationTree.from_mapping("Root", by_id)
