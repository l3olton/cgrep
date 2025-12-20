import subprocess
from pathlib import Path

cwd = Path.cwd()

cgrep = cwd / ".." / "build" / "cgrep"
if not cgrep.exists():
    print("Executable not found.") # TODO: better message
    exit(1)

class SingleInputFile:
    __input_path = cwd / "test-data" / "single-file"
    if not __input_path.exists():
        print("Test data not found.") # TODO: better message
        exit(1)

    def searching_single_file_no_flags(self):
        print("Searching single file with no flags:")

        # Arrange
        search_term = "one"
        expected = cwd / "expected" / "single-file-no-flags"
        expected_return_code = 0

        # Act
        result = subprocess.run([cgrep, search_term, self.__input_path], capture_output=True, text=True, cwd=cwd.relative_to(cwd))

        print("CWD: ", cwd.relative_to(cwd))

        # Assert
        assert result.returncode == expected_return_code, f"\nExpected: {expected_return_code}\nReceived: {result.returncode}"
        assert expected.read_text() == result.stdout, f"\nExpected:\n{expected.read_text()}\nReceived:\n{result.stdout}"
        print("\u2714 Passed\n")

    def searching_single_file_json_flag(self):
        print("Searching single file with --json flag:")

        # Arrange
        search_term = "one"
        flag = "--json"
        expected = cwd / "expected" / "single-file-json-flag"
        expected_return_code = 0

        # Act
        result = subprocess.run([cgrep, search_term, self.__input_path, flag], capture_output=True, text=True, cwd=cwd.relative_to(cwd))

        # Assert
        assert result.returncode == expected_return_code, f"\nExpected: {expected_return_code}\nReceived: {result.returncode}"
        assert expected.read_text() == result.stdout, f"\nExpected:\n{expected.read_text()}\nReceived:\n{result.stdout}"
        print("\u2714 Passed")


test = SingleInputFile()
test.searching_single_file_no_flags()
test.searching_single_file_json_flag()
