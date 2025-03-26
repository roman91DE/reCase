from typing import Iterable


def _capitalize_first(s: str) -> str:
    return s[0].upper() + s[1:]


def _filter_tokens(tokens: Iterable[str]) -> Iterable[str]:
    return list(filter(lambda x: x is not None, tokens))


def to_camel_case(tokens: Iterable[str]) -> str:
    tokens = _filter_tokens(tokens)
    return tokens[0] + "".join((map(_capitalize_first, tokens[1:])))


def to_pascal_case(tokens: Iterable[str]) -> str:
    tokens = _filter_tokens(tokens)
    return "".join((map(_capitalize_first, tokens)))


def to_snake_case(tokens: Iterable[str]) -> str:
    tokens = _filter_tokens(tokens)
    return "_".join(token if token.isupper() else token.lower() for token in tokens)
