#!/bin/bash

# Check if a file path is provided as an argument
if [ $# -eq 0 ]; then
    echo "Please provide the path to a test file as an argument."
    exit 1
fi

CXXFLAGS="-Wl,-stack_size,0x10000000 -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk -ftree-vectorize -fPIC -fstack-protector-strong -O2 -pipe -fvisibility-inlines-hidden -fmessage-length=0"

# export CXX=/usr/bin/clang++
# export CXXFLAGS="-Wl,-stack_size,0x10000000 -std=c++17 -O2"
# export CPPFLAGS=""
# export PATH="/usr/bin:/bin:/usr/sbin:/sbin:$PATH"

# Get the test file path from the argument
test_file="$1"

# Ensure the file exists
if [ ! -f "$test_file" ]; then
    echo "The file $test_file does not exist."
    exit 1
fi

# Ensure the cache directory exists
mkdir -p .verify-helper/cache

# Extract just the filename without the path
filename=$(basename "$test_file")

# Run oj-bundle and redirect output to cache
oj-bundle "$test_file" > ".verify-helper/cache/$test_file"

# Run oj-verify on the cached file
oj-verify run ".verify-helper/cache/$test_file"