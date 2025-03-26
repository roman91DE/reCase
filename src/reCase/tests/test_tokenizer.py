import pytest

from reCase.utils.tokenizer import tokenize


@pytest.mark.parametrize(
    "input_str,expected",
    [
        ("snake_case_example", ["snake", "case", "example"]),
        ("kebab-case-example", ["kebab", "case", "example"]),
        ("camelCaseExample", ["camel", "Case", "Example"]),
        ("PascalCaseExample", ["Pascal", "Case", "Example"]),
        ("getHTTPResponseCode", ["get", "HTTP", "Response", "Code"]),
        ("HTTPRequest", ["HTTP", "Request"]),
        ("CONSTANT_CASE", ["CONSTANT", "CASE"]),
        ("", [""]),
        ("simple", ["simple"]),
    ],
)
def test_tokenize(input_str, expected):
    assert tokenize(input_str) == expected
