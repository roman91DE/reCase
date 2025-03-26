import ast
from functools import partial
from typing import Generator, Type


def extract_node_names(node_type: Type[ast.AST], source_code: str) -> Generator[str]:
    return (
        node.name for node in ast.walk(ast.parse(source_code))
        if isinstance(node, node_type) and hasattr(node, 'name')
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

def extract_names(source_code: str) -> dict[str, list[str]]:
    return {
        "classes": extract_class_names(source_code),
        "functions": extract_function_names(source_code),
        "variables": extract_variable_names(source_code),
    }