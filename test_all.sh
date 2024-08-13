#!/bin/bash

# Ensure the cache directory exists
mkdir -p .verify-helper/cache/test

CXXFLAGS="-isysroot /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk -ftree-vectorize -fPIC -fstack-protector-strong -O2 -pipe -fvisibility-inlines-hidden -fmessage-length=0"
for test_file in test/*.test.py; do
    cp "$test_file" ".verify-helper/cache/$test_file"
    oj-bundle ".verify-helper/cache/$test_file" > "$test_file"
done

oj-verify all

for test_file in test/*.test.py; do
    cat  ".verify-helper/cache/$test_file" > "$test_file"
done