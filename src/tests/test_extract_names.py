from reCase.utils.extract_names import (
    extract_class_names,
    extract_function_names,
    extract_variable_names,
)

sample_code = '''
class MyClass:
    def method_one(self):
        pass

def standalone_function():
    x = 1

y = 2
a, b = 3, 4
z = w = 5
'''

def test_extract_function_names():
    functions = list(extract_function_names(sample_code))
    assert "method_one" in functions
    assert "standalone_function" in functions
    assert len(functions) == 2

def test_extract_class_names():
    classes = list(extract_class_names(sample_code))
    assert "MyClass" in classes
    assert len(classes) == 1

def test_extract_variable_names():
    variables = list(extract_variable_names(sample_code))
    for var in ["x", "y", "a", "b", "z", "w"]:
        assert var in variables
    assert len(variables) == 6

