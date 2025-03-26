import re
from typing import Iterable


def tokenize(s: str) -> Iterable[str | None]:
    if s.startswith("_") or s.startswith("__"):  # Ignore hidden/private names
        return None
    elif "_" in s:
        # snake_case
        return s.split("_")
    elif "-" in s:
        # kebab-case
        return s.split("-")
    elif s:
        # camelCase or PascalCase, including acronyms
        return re.findall(r"[A-Z]+(?=[A-Z][a-z])|[A-Z]?[a-z]+|[A-Z]+", s)
    else:
        return [s]
