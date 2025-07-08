# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is a competitive programming library in Python containing implementations of common algorithms and data structures used in competitive programming contests. The library is verified using the online-judge-verify-helper tool with tests from AtCoder, AOJ, Library Checker, and Yukicoder.

## Development Commands

### Running Tests

To run tests for this library, you must first activate the conda environment:

```bash
conda activate atcoder
```

To verify all tests:
```bash
oj-verify all
```

### C++ Compilation Setup

If you encounter C++ compilation errors with oj-verify (especially on macOS), use the system compiler instead of conda's:
```bash
export CC=/usr/bin/clang
export CXX=/usr/bin/clang++
export CXXFLAGS="-Wl,-stack_size,0x10000000 -std=c++17 -O2"
export CPPFLAGS=""
```

For convenience, create an alias:
```bash
alias oj-verify-cpp='CC=/usr/bin/clang CXX=/usr/bin/clang++ CXXFLAGS="-Wl,-stack_size,0x10000000 -std=c++17 -O2" CPPFLAGS="" oj-verify'
```

To run a specific test:
```bash
./test.sh test/path/to/test_file.test.py
```

To run unit tests:
```bash
pytest
```

### Linting and Type Checking

The repository uses standard Python tools. Check the pyproject.toml for specific configurations.

## Code Architecture

### Library Structure

The library is organized into modules under `cp_library/`:

- **alg/** - Algorithms
  - divcon/ - Divide and conquer algorithms (binary search, quickselect, etc.)
  - dp/ - Dynamic programming utilities
  - graph/ - Graph algorithms (BFS, DFS, shortest paths, flows, etc.)
  - iter/ - Iterator utilities and sorting algorithms
  - tree/ - Tree-specific algorithms (centroid decomposition, HLD, LCA, etc.)

- **bit/** - Bit manipulation utilities
  - pack/ - Bit packing/unpacking utilities
  - masks/ - Common bit masks

- **ds/** - Data structures
  - array/ - Typed array utilities
  - cnt/ - Counting structures
  - heap/ - Various heap implementations
  - list/ - List-based structures (deque, ordered lists, etc.)
  - tree/ - Tree data structures (segment trees, BSTs, Fenwick trees, etc.)
  - wavelet/ - Wavelet matrix implementations

- **io/** - Input/output utilities
  - Fast I/O implementations for competitive programming

- **math/** - Mathematical utilities
  - conv/ - Convolution algorithms (FFT, NTT, subset convolutions, etc.)
  - fps/ - Formal power series operations
  - mod/ - Modular arithmetic utilities
  - nt/ - Number theory algorithms
  - table/ - Precomputed tables (primes, combinations, etc.)

- **misc/** - Miscellaneous utilities
  - decorators/ - Python decorators
  - Type definitions and recursion limit settings

- **opt/** - Optimization utilities

- **vis/** - Visualization and debugging utilities

### Testing Structure

Tests are organized by online judge platform:
- test/aoj/ - AOJ (Aizu Online Judge) tests
- test/atcoder/ - AtCoder tests
- test/library-checker/ - Library Checker tests
- test/yukicoder/ - Yukicoder tests
- test/unittests/ - Unit tests using pytest

Each test file follows the pattern `*.test.py` and uses the verify-helper format with problem URLs specified in comments.

### Key Design Patterns

1. **Naming Conventions**:
   - Classes end with `_cls` (e.g., `graph_cls.py`)
   - Functions end with `_fn` (e.g., `dijkstra_fn.py`)
   - Constants end with `_cnst` (e.g., `inft_cnst.py`)
   - Protocols/interfaces end with `_proto` (e.g., `graph_proto.py`)

2. **Fast Implementations**:
   - Many algorithms have optimized versions in `fast/` subdirectories
   - These use more efficient data structures or algorithms

3. **Modular Arithmetic**:
   - Modules under `mod/` subdirectories contain modular arithmetic versions
   - The `mint_cls` provides a modular integer implementation

4. **Header Files**:
   - `__header__.py` files contain metadata for the verify-helper tool
   - These specify dependencies and other verification settings

## Important Notes

- Always activate the conda environment (`conda activate atcoder`) before running tests
- The library uses PyPy for performance in competitive programming contexts
- Tests are computationally intensive and may take significant time to run
- The verify-helper tool caches results in `.verify-helper/cache/`
- When modifying algorithms, ensure corresponding tests still pass