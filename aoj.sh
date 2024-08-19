#!/bin/bash
test_file="$1"
oj-bundle $test_file > output/bundled.py
# python -m atcoder output/bundled.py -o output/aoj.py
cat output/bundled.py | pbcopy