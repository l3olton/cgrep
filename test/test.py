import subprocess
import sys
from pathlib import Path

cwd = Path.cwd()

cgrep = cwd / ".." / "build" / "cgrep"
if not cgrep.exists():
    print("Executable not found.")
    exit(1)

TESTS = {}

def test_case(func):
    TESTS[func.__name__] = func
    return func

@test_case
def search_single_file_txt_stdout():
    # Arrange
    search_term = "one"
    command = [cgrep, search_term, "test-data/single-file"]
    expected = cwd / "expected" / "single-file-text-stdout"
    expected_return_code = 0

    # Act
    result = subprocess.run(command, capture_output=True, text=True, cwd=cwd.relative_to(cwd))

    # Assert
    assert result.returncode == expected_return_code, f"\nExpected: {expected_return_code}\nReceived: {result.returncode}"
    assert expected.read_text() == result.stdout, f"\nExpected:\n{expected.read_text()}\nReceived:\n{result.stdout}"

@test_case
def search_single_file_json_stdout():
    # Arrange
    search_term = "one"
    command = [cgrep, search_term, "test-data/single-file", "--json"]
    expected = cwd / "expected" / "single-file-json-flag"
    expected_return_code = 0

    # Act
    result = subprocess.run(command, capture_output=True, text=True, cwd=cwd.relative_to(cwd))

    # Assert
    assert result.returncode == expected_return_code, f"\nExpected: {expected_return_code}\nReceived: {result.returncode}"
    assert expected.read_text() == result.stdout, f"\nExpected:\n{expected.read_text()}\nReceived:\n{result.stdout}"

if __name__ == "__main__":
    passed = 0
    failed = 0

    for name, test in TESTS.items():
        try:
            test()
            print(f"✅ {name} PASSED")
            passed += 1
        except Exception as e:
            print(f"❌ {name} FAILED: {e}")
            failed += 1

    print(f"\nSummary: {passed} passed, {failed} failed.")
    if failed > 0:
        sys.exit(1)