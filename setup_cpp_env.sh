#!/bin/bash
# Setup script for C++ compilation with oj-verify on macOS
# Usage: source setup_cpp_env.sh

export CC=/usr/bin/clang
export CXX=/usr/bin/clang++
export CXXFLAGS="-Wl,-stack_size,0x10000000 -std=c++17 -O2"
export CPPFLAGS=""

echo "C++ environment configured for oj-verify:"
echo "CC=$CC"
echo "CXX=$CXX"
echo "CXXFLAGS=$CXXFLAGS"
echo "CPPFLAGS=$CPPFLAGS"