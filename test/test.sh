#!/bin/bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
CGREP="$SCRIPT_DIR/../build/cgrep"

if [ ! -x "$CGREP" ]; then
  echo "Executable not found"
  exit 1
fi

TESTDATA="$SCRIPT_DIR/./test-data"
EXPECTED="$SCRIPT_DIR/./expected"

PASSED=0
FAILED=0
TESTS=()

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

run_test() {
    local name="$1"
    local test_func="$2"

    if $test_func; then
        echo -e "${GREEN}✓${NC} $name"
        ((PASSED++))
    else
        echo -e "${RED}✗${NC} $name"
        ((FAILED++))
    fi
}

single_file_txt_stdout() {
  local search_term="one"
  local expected="$EXPECTED/single-file-no-flags"
  local expected_return_code=0

  local result=$($CGREP "$search_term" "$TESTDATA/single-file")
  local result_file=<(echo "$result")
  diff -q <(echo "$result") "$expected" >/dev/null
}

run_test "Search single file, output to stdout" single_file_txt_stdout

exit 0
