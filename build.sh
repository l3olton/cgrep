#!/bin/bash

set -e

mkdir -p build

gcc -o build/cgrep \
  src/main.c \
  src/arg_parser.c \
  src/csv_utils.c \
  src/file_utils.c \
  src/json_utils.c \
  src/output_handler.c \
  src/search_result.c \
  src/searcher.c