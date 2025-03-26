# 🐍 reCase

**reCase** is a CLI tool that normalizes variable, function, class, and parameter names in Python files into a consistent naming convention. It uses Python’s AST to safely refactor code without touching strings or comments.


## ✨ Features

- 🔁 Converts identifiers across various naming styles
- 🔍 Detects `snake_case`, `camelCase`, `PascalCase`, `kebab-case`, and `UPPER_CASE`
- ✅ Safely rewrites Python source using AST (no regex hacks!)
- 🔧 CLI with optional output path or `stdout` preview
- 🧪 Fully tested with `pytest`
- 🧹 Integrated with `ruff`, `isort`, `pytest`, and `uv` via pre-commit hooks

> ⚠️ **Current Limitation:**  
> The program currently **only supports**:
> - Renaming **functions**, **variables**, and **parameters** to **`snake_case`**
> - Renaming **class names** to **`PascalCase`**

Support for other casing styles is planned for future versions.

---

## 🚀 Installation


```bash
git clone https://github.com/roman91DE/reCase.git
cd reCase
uv pip install -e .
```

## Usage

Rewrite a Python file in place

```bash
recase -i path/to/script.py -o path/to/rewritten_script.py
```

Preview transformation (to stdout)

```bash
recase -i path/to/script.py
```



## Development

Set up your local dev environment:

```bash
uv pip install -e .
uv pip install pytest ruff isort pre-commit
pre-commit install
```

Run tests:

```bash
pytest
```



## Project Structure

src/reCase/
│
├── cli/              # CLI entry point
├── utils/
│   ├── extract_names.py   # Identifier extraction using AST
│   ├── tokenizer.py       # Splits identifiers into word tokens
│   ├── transformer.py     # Converts token lists to desired casing
│   └── processor.py       # Translates and rewrites Python files
├── tests/            # Pytest suite
└── ...




## ✅ Pre-commit Hooks

Pre-commit will automatically run:
	•	ruff format
	•	ruff check
	•	isort
	•	pytest
	•	uv pip install -e .

To trigger manually:

```bash
pre-commit run --all-files
```



## 🧠 Motivation

Python projects often accumulate mixed naming styles due to multiple contributors, legacy code, or poor linters. reCase helps normalize identifier casing without risk of breaking your code.


## 📜 License

MIT


## 🙌 Contributions

Issues and PRs welcome! Let’s clean up some code together.

## Example

### Before

```python
class HttpResponseHandler:
    """
    Handles HTTPResponseCodes and performs URLParse_operations.
    """

    def __init__(self, Response_code=200, errorFlag=False):
        self.Response_code = Response_code
        self.errorFlag = errorFlag
        self.internal_log_buffer = []

    def addToLog(self, LogEntry: str) -> None:
        """
        Adds a log_entry to internal-log-buffer.
        """
        self.internal_log_buffer.append(LogEntry)

    def GetStatusMessage(self):
        """
        Returns statusMessage based on RESPONSE_CODE.
        """
        if self.Response_code == 200:
            return "OK"
        elif self.Response_code == 404:
            return "NotFound"
        else:
            return "Error"


def processHTTPRequest(url_address, methodType):
    """
    Processes HTTP-request from URLAddress using method-type.
    """
    temp_var = "processing"
    print(temp_var)
    Output_Result = f"{methodType} request sent to {url_address}"
    return Output_Result


GLOBAL_CONSTANT = 42
anotherGlobalVariable = "HelloWorld"


def MAIN_HANDLER():
    """
    EntryPoint for the MainHandler class.
    """
    handlerInstance = HttpResponseHandler(Response_code=404)
    handlerInstance.addToLog("Initialization complete")
    status = handlerInstance.GetStatusMessage()
    print(f"Status: {status}")
    print(processHTTPRequest("http://example.com", "GET"))


def __hidden_function(weirdArgumentName):
    pass


def _another_hidden_function():
    pass

```

### After:

```python
class HttpResponseHandler:
    """
    Handles HTTPResponseCodes and performs URLParse_operations.
    """

    def __init__(self, response_code=200, error_flag=False):
        self.Response_code = response_code
        self.errorFlag = error_flag
        self.internal_log_buffer = []

    def add_to_log(self, log_entry: str) -> None:
        """
        Adds a log_entry to internal-log-buffer.
        """
        self.internal_log_buffer.append(log_entry)

    def get_status_message(self):
        """
        Returns statusMessage based on RESPONSE_CODE.
        """
        if self.Response_code == 200:
            return 'OK'
        elif self.Response_code == 404:
            return 'NotFound'
        else:
            return 'Error'

def process_HTTP_request(url_address, method_type):
    """
    Processes HTTP-request from URLAddress using method-type.
    """
    temp_var = 'processing'
    print(temp_var)
    output_result = f'{method_type} request sent to {url_address}'
    return output_result
GLOBAL_CONSTANT = 42
another_global_variable = 'HelloWorld'

def MAIN_HANDLER():
    """
    EntryPoint for the MainHandler class.
    """
    handler_instance = HttpResponseHandler(Response_code=404)
    handler_instance.addToLog('Initialization complete')
    status = handler_instance.GetStatusMessage()
    print(f'Status: {status}')
    print(process_HTTP_request('http://example.com', 'GET'))

def __hidden_function(weird_argument_name):
    pass

def _another_hidden_function():
    pass
```