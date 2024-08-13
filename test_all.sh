#!/bin/bash

# Ensure the cache directory exists
mkdir -p .verify-helper/cache/test

CXXFLAGS="-isysroot /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk -ftree-vectorize -fPIC -fstack-protector-strong -O2 -pipe -fvisibility-inlines-hidden -fmessage-length=0"

for test_file in test/*.test.py; do
    filename=$(basename "$test_file")
    oj-bundle "$test_file" > ".verify-helper/cache/test/$filename"
done
cd .verify-helper/cache/test
oj-verify all
cp -r .verify-helper/* ../../
