def _capitalize_first(s: str) -> str:
    return s[0].upper() + s[1:]

def to_camel_case(tokens: list[str]) -> str:
    return tokens[0] + "".join(list(map(_capitalize_first, tokens[1:])))

def to_pascal_case(tokens: list[str]) -> str:
    return "".join(list(map(_capitalize_first, tokens)))

def to_snake_case(tokens: list[str]) -> str:
    return "_".join(
        token if token.isupper() else token.lower()
        for token in tokens
    )
