import pytest

from reCase.utils.transformer import to_camel_case, to_pascal_case, to_snake_case


@pytest.mark.parametrize(
    "tokens, expected",
    [
        (["snake", "case"], "snake_case"),
        (["HTTP", "Response"], "HTTP_response"),  # all-caps preserved
        (["Upper", "CASE", "Mixed"], "upper_CASE_mixed"),
    ],
)
def test_to_snake_case(tokens, expected):
    assert to_snake_case(tokens) == expected


@pytest.mark.parametrize(
    "tokens, expected",
    [
        (["camel", "case"], "camelCase"),
        (["http", "response"], "httpResponse"),
    ],
)
def test_to_camel_case(tokens, expected):
    assert to_camel_case(tokens) == expected


@pytest.mark.parametrize(
    "tokens, expected",
    [
        (["pascal", "case"], "PascalCase"),
        (["http", "response"], "HttpResponse"),
    ],
)
def test_to_pascal_case(tokens, expected):
    assert to_pascal_case(tokens) == expected
