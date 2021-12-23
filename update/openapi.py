import dataclasses as dt
import typing as t
from collections import defaultdict
from enum import Enum

from svarog.tools import camel_to_snake
from svarog.types import Forge

from .svarog import svarog
from .tools import to_camel_case

Method = t.Literal["get", "post"]


class ParameterSource(Enum):
    PATH = "path"
    QUERY = "query"


@dt.dataclass(frozen=True)
class Reference:
    ref: str
    required: bool = False

    @property
    def class_name(self) -> str:
        assert self.ref.startswith("#/")
        *modules, name = self.ref.split("/")[-1].split(".")
        return ".".join(
            ("types", *(camel_to_snake(module) for module in modules), name)
        )

    @staticmethod
    def filter(
        t: t.Type["Integer"], data: t.Mapping, forge: Forge
    ) -> t.Mapping[str, t.Any]:
        return fix(data, {"$ref": "ref"})

    def local(self, module: t.Sequence[str]) -> bool:
        *ref_module, class_name = self.class_name.split(".")
        return module == ref_module

    @property
    def name(self) -> str:
        return self.class_name.split(".")[-1]


class ApiType(Enum):
    INTEGER = "integer"
    STRING = "string"
    BOOLEAN = "boolean"
    ARRAY = "array"
    OBJECT = "object"
    NUMBER = "number"


@dt.dataclass(frozen=True)
class Schema:
    types: t.ClassVar[t.Dict[ApiType, t.Type["Schema"]]] = {}
    type: t.ClassVar[ApiType]
    description: t.Optional[str] = None
    required: bool = False

    def __init_subclass__(cls, type: ApiType, **kwargs: t.Any) -> None:
        super().__init_subclass__(**kwargs)
        cls.types[type] = cls
        cls.type = type

    @staticmethod
    def forge(t: t.Type["Schema"], data: t.Mapping, forge: Forge) -> "Schema":

        cls = Schema.types[ApiType(data["type"])]
        return forge(cls, data)


@dt.dataclass(frozen=True)
class BindSchema:
    name: str
    schema: Schema

    @classmethod
    def bind(cls, name: str, schema: Schema) -> "BindSchema":
        return BindSchema(name, schema)

    @property
    def schema_name(self):
        return self.name.split(".")[-1].replace("[]", "Array")


@dt.dataclass(frozen=True)
class Boolean(Schema, type=ApiType.BOOLEAN):
    ...


class StringFormat(Enum):
    DATE_TIME = "date-time"
    BYTE = "byte"


@dt.dataclass(frozen=True)
class String(Schema, type=ApiType.STRING):
    format: t.Optional[StringFormat] = None


class IntegerFormat(Enum):
    INT16 = "int16"
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
class EnumValue:
    numeric_value: int
    identifier: str
    description: t.Optional[str] = None


@dt.dataclass(frozen=True)
class Integer(Schema, type=ApiType.INTEGER):
    format: t.Optional[IntegerFormat] = None
    enum_reference: t.Optional[Reference] = None
    enum: t.Optional[t.Sequence[int]] = None
    enum_values: t.Optional[t.Sequence[EnumValue]] = None

    @staticmethod
    def filter(
        t: t.Type["Integer"], data: t.Mapping, forge: Forge
    ) -> t.Mapping[str, t.Any]:
        return fix(
            data, {"x-enum-reference": "enum_reference", "x-enum-values": "enum_values"}
        )


class NumberFormat(Enum):
    FLOAT = "float"
    DOUBLE = "double"


@dt.dataclass(frozen=True)
class Number(Schema, type=ApiType.NUMBER):
    format: t.Optional[NumberFormat] = None


@dt.dataclass(frozen=True)
class Object(Schema, type=ApiType.OBJECT):
    properties: t.Optional[t.Mapping[str, t.Union[Reference, Schema]]] = None
    additional_properties: t.Union[Reference, Schema, None] = None
    all_of: t.Optional[t.Sequence[Reference]] = None


def forge_regerence_or_schema(
    t: t.Union[Reference, Schema], data: t.Mapping[str, t.Any], forge: Forge
) -> t.Union[Reference, Schema]:
    if "$ref" in data:
        return forge(Reference, data)
    return forge(Schema, data)


svarog.register_forge(t.Union[Reference, Schema], forge_regerence_or_schema)  # type: ignore
svarog.register_forge(t.Union[Reference, Schema, None], forge_regerence_or_schema)  # type: ignore


def not_allowed():
    raise RuntimeError("non null is not allowed")


@dt.dataclass(frozen=True)
class Array(Schema, type=ApiType.ARRAY):
    items: t.Union[Reference, Schema] = dt.field(default_factory=not_allowed)


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
            in_=forge(ParameterSource, data["in"]),
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

    @property
    def response(self) -> Response:
        assert len(self.responses.values()) == 1
        return next(self.responses.values().__iter__())


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
class TypeTree:
    name: str
    children: t.Sequence[t.Union[BindSchema, "TypeTree"]]

    def child_types(self) -> t.Iterator["TypeTree"]:
        yield from (child for child in self.children if isinstance(child, TypeTree))

    def child_schema(self) -> t.Iterator[BindSchema]:
        yield from (child for child in self.children if isinstance(child, BindSchema))

    @classmethod
    def from_mapping(cls, name: str, by_name: t.Mapping[str, BindSchema]) -> "TypeTree":
        children: t.Mapping[str, t.Any] = defaultdict(dict)
        my = []
        for schema_name, schema in by_name.items():
            if "." not in schema_name:
                my.append(schema)
            else:
                group, rest = schema_name.split(".", 1)
                children[camel_to_snake(group)][rest] = schema
        return TypeTree(
            name=name,
            children=[
                *my,
                *(
                    TypeTree.from_mapping(name, by_name)
                    for name, by_name in children.items()
                ),
            ],
        )


@dt.dataclass(frozen=True)
class OperationTree:
    name: str
    children: t.Sequence[t.Union[BindOperation, "OperationTree"]]

    def child_clients(self) -> t.Iterator["OperationTree"]:
        yield from (
            child for child in self.children if isinstance(child, OperationTree)
        )

    def child_operations(self) -> t.Iterator[BindOperation]:
        yield from (
            child for child in self.children if isinstance(child, BindOperation)
        )

    @classmethod
    def from_mapping(
        cls, name: str, by_id: t.Mapping[str, t.Union[BindOperation, "OperationTree"]]
    ) -> "OperationTree":
        children: t.Dict[str, t.Any] = defaultdict(dict)
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
    definitions: t.Mapping[str, Schema]

    def operations_tree(self) -> OperationTree:
        def fix_operation_id(operation_id: str) -> str:
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

    def types_tree(self) -> TypeTree:
        by_name = {
            name: BindSchema(name, schema) for name, schema in self.definitions.items()
        }
        return TypeTree.from_mapping("types", by_name)
