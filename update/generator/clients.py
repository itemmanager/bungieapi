import re
import typing as t
from functools import singledispatch

from update.generator.imports import generate_imports
from update.generator.literals import literal
from update.openapi import BindOperation, Tree
from update.tools import camel_to_snake

from .. import openapi as api


CLIENT_REPLACEMENTS = {"app": "AppClient"}


def client(operation_tree: Tree[BindOperation]) -> t.Iterator[str]:
    yield "import dataclasses as dt"
    yield "import typing as t"
    yield "from bungieapi.generated import clients"
    yield f"from bungieapi.base import BaseClient, {','.join(CLIENT_REPLACEMENTS.values())}"
    yield "from bungieapi.forge import forge"
    yield "from bungieapi.json import to_json"

    for operation in operation_tree.child_leaf():
        yield from generate_imports(operation, [])

    yield f"class Client({CLIENT_REPLACEMENTS.get(operation_tree.name, 'BaseClient')}):"
    if not operation_tree.children:
        yield "..."

    for child in operation_tree.children:
        yield from client_method(child)


@singledispatch
def client_method(node: t.Union[Tree[BindOperation], BindOperation]) -> t.Iterator[str]:
    raise RuntimeError(f"Not defined for type {type(node)}")


PATH_QUERY_PARAM_RE = re.compile(r"\{(?P<name>[^\}]+)}")


def query_param_to_snake(match: re.Match) -> str:
    return f"{{{camel_to_snake(match.group('name'))}}}"


@client_method.register
def generate_client_method_operation(operation: BindOperation) -> t.Iterator[str]:
    yield f"    async def {operation.python_name}(self,"
    if operation.request_body:
        yield f"request: {literal(operation.request_body, [])},"
    for parameter in sorted(
        operation.parameters, key=lambda param: not param.schema.required
    ):
        yield f"{parameter.python_name}: {literal(parameter.schema, []) }{ ' = None' if not parameter.schema.required  else ''},"

    assert isinstance(operation.response, api.Reference)
    return_type = operation.response.name
    yield f") -> {return_type}:"
    yield f'        """{operation.description}'
    parameter_descriptions = [p for p in operation.parameters if p.description]
    if parameter_descriptions:
        yield "Parameters:"
        for p in parameter_descriptions:
            yield f"    {p.python_name}: {p.description}"

    yield '"""'
    path_parameters = [
        p for p in operation.parameters if p.in_ == api.ParameterSource.PATH
    ]
    query_parameters = [
        p for p in operation.parameters if p.in_ == api.ParameterSource.QUERY
    ]
    if path_parameters:
        path = PATH_QUERY_PARAM_RE.sub(query_param_to_snake, operation.path)
        path = f'f"{path}"'
    else:
        path = f'"{operation.path}"'
    if query_parameters:
        dict_inside = ", ".join(
            (f'"{p.name}": {p.python_name}' for p in query_parameters)
        )
        query_dict = f"{{{dict_inside}}}"
        yield f"        query = {query_dict}"
    else:
        yield "        query = None"
    request = "request=request" if operation.request_body else ""

    yield f"        result = await self.{operation.method}(path={path}, query=query,{request})"
    yield f"        return forge({return_type}, result)"


@client_method.register
def generate_client_method_node(operation_tree: Tree) -> t.Iterator[str]:
    klass = f"clients.{camel_to_snake(operation_tree.name)}.Client"
    yield "    @property"
    yield f"    def {camel_to_snake(operation_tree.name)}(self) -> {klass}: "
    yield f"        return {klass}(self._session, self._path)"


def generate_clients_init(root: Tree[BindOperation]) -> t.Iterator[str]:
    submodules = [
        camel_to_snake(operation_tree.name) for operation_tree in root.child_nodes()
    ]
    for submodule in submodules:
        yield f"from . import {submodule}"
    all = [f'"{submodule}"' for submodule in submodules]
    yield f"__all__ = [{', '.join(all)}]"
