import ast
from functools import partial
from typing import Generator, Iterable, Type


def extract_node_names(node_type: Type[ast.AST], source_code: str) -> Iterable[str]:
    return (
        node.name
        for node in ast.walk(ast.parse(source_code))
        if isinstance(node, node_type) and hasattr(node, "name")
    )


extract_function_names = partial(extract_node_names, ast.FunctionDef)
extract_class_names = partial(extract_node_names, ast.ClassDef)


def extract_variable_names(source_code: str) -> Generator[str, None, None]:
    def extract_from_target(target: ast.expr) -> Generator[str, None, None]:
        if isinstance(target, ast.Name):
            yield target.id
        elif isinstance(target, (ast.Tuple, ast.List)):
            for elt in target.elts:
                yield from extract_from_target(elt)

    for node in ast.walk(ast.parse(source_code)):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                yield from extract_from_target(target)


def extract_parameter_names(source_code: str) -> Iterable[str]:
    param_names = []
    tree = ast.parse(source_code)

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            for arg in node.args.args:
                param_names.append(arg.arg)

            # Handle positional-only and keyword-only arguments
            for arg in getattr(node.args, "posonlyargs", []):
                param_names.append(arg.arg)
            for arg in node.args.kwonlyargs:
                param_names.append(arg.arg)

            # Handle *args and **kwargs
            if node.args.vararg:
                param_names.append(node.args.vararg.arg)
            if node.args.kwarg:
                param_names.append(node.args.kwarg.arg)

    return param_names


def extract_names(source_code: str) -> dict[str, list[str]]:
    return {
        "classes": extract_class_names(source_code),
        "functions": extract_function_names(source_code),
        "variables": extract_variable_names(source_code),
        "parameters": extract_parameter_names(source_code),
    }
