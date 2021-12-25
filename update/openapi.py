import dataclasses as dt
import typing as t
from collections import defaultdict
from enum import Enum

from svarog.tools import camel_to_snake
from svarog.types import Forge

from .generator.tools import response_schema_name
from .svarog import svarog
from .tools import to_camel_case


Method = t.Literal["get", "post"]


class ParameterSource(Enum):
    PATH = "path"
    QUERY = "query"


@dt.dataclass(frozen=True)
class Reference:
    ref: str
    required: bool = True

    @property
    def class_name(self) -> str:
        assert self.ref.startswith("#/")
        _, *path, dotted_name = self.ref.split("/")
        *modules, name = dotted_name.split(".")
        return ".".join(
            (
                *("bungieapi", "generated"),
                *map(camel_to_snake, path),
                *map(camel_to_snake, modules),
                name,
            )
        )

    @staticmethod
    def filter(t: t.Type["Integer"], data: t.Mapping) -> t.Mapping[str, t.Any]:
        return fix(data, {"$ref": "ref"})

    def local(self, module: t.Sequence[str]) -> bool:
        return module == self.module

    @property
    def name(self) -> str:
        class_name = self.class_name
        name = class_name.split(".")[-1]
        if class_name.startswith("bungieapi.generated.components.responses"):
            name = response_schema_name(name)
        return name

    @property
    def module(self) -> t.Sequence[str]:
        *module, _ = self.class_name.split(".")
        return module


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
    required: bool = True

    def __init_subclass__(cls, type: ApiType, **kwargs: t.Any) -> None:
        super().__init_subclass__(**kwargs)
        cls.types[type] = cls
        cls.type = type

    @staticmethod
    def forge(t: t.Type["Schema"], data: t.Mapping, forge: Forge) -> "Schema":
        cls = Schema.types[ApiType(data["type"])]
        return forge(cls, data)


class Binded:
    name: str

    @property
    def schema_name(self):
        return self.name.split(".")[-1].replace("[]", "Array")


@dt.dataclass(frozen=True)
class BindResponse(Binded):
    name: str
    response: "Response"


@dt.dataclass(frozen=True)
class BindSchema(Binded):
    name: str
    schema: Schema

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
    def filter(t: t.Type["Integer"], data: t.Mapping) -> t.Mapping[str, t.Any]:
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
    t: t.Union[Reference, Schema, None], data: t.Mapping[str, t.Any], forge: Forge
) -> t.Union[Reference, Schema, None]:
    if data is None:
        return None
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
    schema: Schema

    @staticmethod
    def filter(t: t.Type["Parameter"], data: t.Mapping) -> t.Mapping[str, t.Any]:
        return fix(data, {"in": "in_"})

    @property
    def python_name(self) -> str:
        return camel_to_snake(self.name)


@dt.dataclass(frozen=True)
class Response:
    description: str
    schema: Object

    @staticmethod
    def filter(t: t.Type["Response"], data: t.Mapping) -> t.Mapping[str, t.Any]:
        return {
            "description": data["description"],
            "schema": data["content"]["application/json"]["schema"],
        }

    def __post_init__(self):
        self.schema.properties["DetailedErrorTrace"] = dt.replace(  # type: ignore
            self.schema.properties["DetailedErrorTrace"],  # type: ignore
            required=False,
        )


@dt.dataclass(frozen=True)
class Operation:
    operation_id: str
    parameters: t.Sequence[Parameter]
    response: Reference
    deprecated: bool = False
    description: t.Optional[str] = None
    request_body: t.Union[Reference, Schema, None] = None

    @staticmethod
    def filter(t: t.Type["Operation"], data: t.Dict) -> t.Mapping:
        responses = data.pop("responses")
        if request_body := data.pop("request_body", None):
            request_body = request_body["content"]["application/json"]["schema"]

        return {**data, "response": responses["200"], "request_body": request_body}


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


T = t.TypeVar("T")


@dt.dataclass(frozen=True)
class Tree(t.Generic[T]):
    name: str
    children: t.Sequence[t.Union[T, "Tree"]]

    def child_nodes(self) -> t.Iterator["Tree"]:
        yield from (child for child in self.children if isinstance(child, Tree))

    def child_leaf(self) -> t.Iterator[T]:
        yield from (child for child in self.children if not isinstance(child, Tree))

    @classmethod
    def from_mapping(
        cls, name: str, by_id: t.Mapping[str, t.Union[T, "Tree"]]
    ) -> "Tree":
        children: t.Dict[str, t.Any] = defaultdict(dict)
        my = []
        for operation_id, operation in by_id.items():
            if "." not in operation_id:
                my.append(operation)
            else:
                group, *rest = operation_id.split(".")
                children[camel_to_snake(group)][".".join(rest)] = operation
        return Tree(
            name=name,
            children=[
                *my,
                *(Tree.from_mapping(name, by_id) for name, by_id in children.items()),
            ],
        )


@dt.dataclass(frozen=True)
class Operations:
    summary: str
    description: str
    get: t.Optional[Operation] = None
    post: t.Optional[Operation] = None

    def __post_init__(self):
        if self.get and self.post:
            raise RuntimeError("get and post cannot be set in the same moment")

    def items(self) -> t.Iterator[t.Tuple[Method, Operation]]:
        if self.get:
            yield "get", self.get
        if self.post:
            yield "post", self.post


@dt.dataclass(frozen=True)
class Components:
    schemas: t.Mapping[str, Schema]
    responses: t.Mapping[str, Response]


@dt.dataclass(frozen=True)
class OpenApi:
    openapi: str
    info: Info
    paths: t.Mapping[str, Operations]
    components: Components

    def operations_tree(self) -> Tree[BindOperation]:
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
        return Tree[BindOperation].from_mapping("Root", by_id)

    def schema_tree(self) -> Tree[BindSchema]:
        return Tree.from_mapping(
            "schemas",
            {
                name: BindSchema(name, schema)
                for name, schema in self.components.schemas.items()
            },
        )

    def response_tree(self) -> Tree[BindResponse]:
        return Tree.from_mapping(
            "responses",
            {
                name: BindResponse(name, schema)
                for name, schema in self.components.responses.items()
            },
        )
