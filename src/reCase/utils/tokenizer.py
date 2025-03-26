import re


def tokenize(s: str) -> list[str]:
    if "_" in s:
        # snake_case
        return s.split("_")
    elif "-" in s:
        # kebab-case
        return s.split("-")
    elif s:
        # camelCase or PascalCase, including acronyms
        return re.findall(r'[A-Z]+(?=[A-Z][a-z])|[A-Z]?[a-z]+|[A-Z]+', s)
    else:
        return [s]