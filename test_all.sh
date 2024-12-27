#!/bin/bash

# Ensure the cache directory exists
mkdir -p .verify-helper/cache

CXXFLAGS="-Wl,-stack_size,0x10000000 -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk -ftree-vectorize -fPIC -fstack-protector-strong -O2 -pipe -fvisibility-inlines-hidden -fmessage-length=0"

# Function to process files recursively
process_files() {
    for test_file in "$1"/*.test.py; do
        if [ -f "$test_file" ]; then
            relative_path=${test_file#./}
            mkdir -p "$(dirname ".verify-helper/cache/$relative_path")"
            cp "$test_file" ".verify-helper/cache/$relative_path"
            oj-bundle ".verify-helper/cache/$relative_path" > "$test_file"
        fi
    done

    # Recurse into subdirectories
    for dir in "$1"/*/ ; do
        if [ -d "$dir" ]; then
            process_files "$dir"
        fi
    done
}

# Process files starting from the test directory
process_files "./test"

# Run verification
oj-verify all

# Restore original files
restore_files() {
    for test_file in "$1"/*.test.py; do
        if [ -f "$test_file" ]; then
            relative_path=${test_file#./}
            cat ".verify-helper/cache/$relative_path" > "$test_file"
        fi
    done

    # Recurse into subdirectories
    for dir in "$1"/*/ ; do
        if [ -d "$dir" ]; then
            restore_files "$dir"
        fi
    done
}

# Restore files starting from the test directory
if [ -d "./test" ]; then
    restore_files "./test"
else
    echo "No test/ directory found."
fi