import typing as t
from functools import singledispatch

from update.generator.imports import generate_imports
from update.generator.literals import literal
from update.generator.schema import generate_schema
from update.generator.tools import camel_to_snake
from update.openapi import BindOperation, OperationTree

from .. import openapi as api


def client(operation_tree: OperationTree) -> t.Iterator[str]:
    yield "from .. import clients"
    yield "import dataclasses as dt"
    yield "import typing as t"
    yield "from ...base import BaseClient"

    for operation in operation_tree.child_operations():
        yield from generate_imports(operation, [])

    for operation in operation_tree.child_operations():
        assert operation.response.schema.type == api.ApiType.OBJECT
        assert isinstance(operation.response.schema, api.Object)
        yield from generate_schema(
            operation.response.schema, response_type_name(operation), []
        )

    yield f"class Client(BaseClient):"
    if not operation_tree.children:
        yield "..."

    for child in operation_tree.children:
        yield from client_method(child)


def response_type_name(operation: BindOperation) -> str:
    return f"{operation.name}ClientResponse"


@singledispatch
def client_method(node: t.Union[OperationTree, BindOperation]) -> t.Iterator[str]:
    raise RuntimeError(f"Not defined for type {type(node)}")


@client_method.register
def generate_client_method_operation(operation: BindOperation) -> t.Iterator[str]:
    yield f"    async def {operation.python_name}(self,"
    for parameter in sorted(
        operation.parameters, key=lambda param: not param.type.required
    ):
        yield f"{parameter.python_name}: {literal(parameter.type, []) }{ ' = None' if not parameter.type.required  else ''},"
    yield f") -> {response_type_name(operation)}:"
    if operation.description:
        yield f'        """{operation.description}"""'
    yield f"        ..."


@client_method.register
def generate_client_method_node(operation_tree: OperationTree) -> t.Iterator[str]:
    klass = f"clients.{camel_to_snake(operation_tree.name)}.Client"
    yield "    @property"
    yield f"    def {camel_to_snake(operation_tree.name)}(self) -> {klass}: "
    yield f"        return {klass}(self._session, self._path)"


def generate_clients_init(root: OperationTree) -> t.Iterator[str]:
    submodules = [
        camel_to_snake(operation_tree.name) for operation_tree in root.child_clients()
    ]
    for submodule in submodules:
        yield f"from . import {submodule}"
    all = [f'"{submodule}"' for submodule in submodules]
    yield f"__all__ = [{', '.join(all)}]"
