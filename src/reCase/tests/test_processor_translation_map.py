from pathlib import Path

from reCase.utils.processor import build_translation_map, parse_file


def test_translation_map_from_script_1():
    test_file = Path("src/reCase/tests/res/test_script_1.py")
    code = parse_file(test_file)
    assert code is not None, "Failed to parse test script."

    translation_map = build_translation_map(code)

    # Classes should be PascalCase
    assert (
        translation_map.get("HttpResponseHandler") == "HttpResponseHandler"
    )  # already Pascal
    assert "HttpResponseHandler" in translation_map

    # Functions and variables should be snake_case
    assert translation_map.get("addToLog") == "add_to_log"
    assert translation_map.get("GetStatusMessage") == "get_status_message"
    assert translation_map.get("processHTTPRequest") == "process_HTTP_request"
    assert translation_map.get("MAIN_HANDLER") == "MAIN_HANDLER"
    assert translation_map.get("LogEntry") == "log_entry"
    assert translation_map.get("Response_code") == "response_code"
    assert translation_map.get("errorFlag") == "error_flag"
    # assert translation_map.get("internal_log_buffer") == "internal_log_buffer"  # already snake
    assert translation_map.get("Output_Result") == "output_result"
    assert translation_map.get("weirdArgumentName") == "weird_argument_name"
