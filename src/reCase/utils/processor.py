import ast
from pathlib import Path

from reCase.utils.extract_names import extract_names
from reCase.utils.tokenizer import tokenize
from reCase.utils.transformer import to_pascal_case, to_snake_case


def parse_file(p: Path) -> str | None:
    if not p.exists():
        return None

    return p.open().read(-1)


def build_translation_map(code: str):
    symbols = extract_names(code)
    translation_map = {}

    for t, names in symbols.items():
        match t:
            case "classes":
                for identifier in names:
                    tokens = tokenize(identifier)
                    if tokens is not None:
                        translation_map[identifier] = to_pascal_case(tokens)

            case _:
                for identifier in names:
                    tokens = tokenize(identifier)
                    if tokens is not None:
                        translation_map[identifier] = to_snake_case(tokens)

    return translation_map


class ASTRenamer(ast.NodeTransformer):
    def __init__(self, translation_map: dict[str, str]):
        self.translation_map = translation_map

    def visit_Name(self, node: ast.Name) -> ast.AST:
        if node.id in self.translation_map:
            return ast.copy_location(
                ast.Name(id=self.translation_map[node.id], ctx=node.ctx), node
            )
        return node

    def visit_FunctionDef(self, node: ast.FunctionDef) -> ast.AST:
        if node.name in self.translation_map:
            node.name = self.translation_map[node.name]
        self.generic_visit(node)
        return node

    def visit_ClassDef(self, node: ast.ClassDef) -> ast.AST:
        if node.name in self.translation_map:
            node.name = self.translation_map[node.name]
        self.generic_visit(node)
        return node

    def visit_arg(self, node: ast.arg) -> ast.AST:
        if node.arg in self.translation_map:
            node.arg = self.translation_map[node.arg]
        return node


def rewrite_file(code: str, output_path: Path):
    translation_map = build_translation_map(code)
    tree = ast.parse(code)
    renamer = ASTRenamer(translation_map)
    new_tree = renamer.visit(tree)
    ast.fix_missing_locations(new_tree)
    new_code = ast.unparse(new_tree)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(new_code)
