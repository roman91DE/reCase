import argparse
import ast
from pathlib import Path

from reCase.utils.processor import build_translation_map, parse_file, rewrite_file


def main():
    parser = argparse.ArgumentParser(
        description="reCase - Normalize Python identifier casing."
    )
    parser.add_argument(
        "--input", "-i", type=Path, required=True, help="Path to the input Python file."
    )
    parser.add_argument(
        "--output", "-o", type=Path, help="Optional path to write transformed code."
    )

    args = parser.parse_args()

    code = parse_file(args.input)
    if code is None:
        print(f"Could not read file: {args.input}")
        return

    if args.output:
        rewrite_file(code, args.output)
        print(f"Rewritten file saved to: {args.output}")
    else:
        translation_map = build_translation_map(code)
        tree = ast.parse(code)
        from reCase.utils.processor import ASTRenamer

        renamer = ASTRenamer(translation_map)
        new_tree = renamer.visit(tree)
        ast.fix_missing_locations(new_tree)
        print(ast.unparse(new_tree))


if __name__ == "__main__":
    main()
