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

### Poetry Package Management

This project uses Poetry for dependency management:

```bash
# Install dependencies
poetry install

# Add new dependency
poetry add package-name

# Run commands in poetry environment
poetry run pytest
```

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

- **perf/** - Performance benchmarking framework
  - Declarative benchmark system with decorator-based API
  - Timing utilities with warmup and validation
  - Plotting support (matplotlib + ASCII fallback)
  - Checksum utilities for result validation

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

4. **Multichannel Data Structures**:
   - Many data structures have multichannel versions (e.g., BIT2-6, SegTree2-6, List2-6)
   - Multichannel structures use inheritance with overridable operation methods
   - Base classes avoid conditional logic using `_op`, `_add`, `_sub` pattern
   - Multichannel classes have K class variable indicating number of channels

5. **Header Files**:
   - `__header__.py` files contain metadata for the verify-helper tool
   - These specify dependencies and other verification settings

## Best Practices

### Code Organization and Imports

1. **Use Absolute Imports**: Due to oj-verify bundling behavior, always use absolute imports to avoid import resolution issues:
   ```python
   # Good: Absolute imports
   from cp_library.ds.tree.segtree_cls import SegTree
   from cp_library.math.mod.mint_cls import mint
   
   # Bad: Relative imports (can break during bundling)
   from .segtree_cls import SegTree
   from ..mod.mint_cls import mint
   ```

2. **Keep __init__.py Files Empty**: The oj-verify bundler works better with empty `__init__.py` files. Avoid adding imports or initialization code to these files.

3. **Import Dependencies at Module Level**: Place all imports at the top of files rather than inside functions to ensure proper bundling:
   ```python
   # Good: Module-level imports
   import cp_library.ds.__header__
   from cp_library.math.mod.mint_cls import mint
   
   class MyClass:
       def method(self):
           return mint(42)
   
   # Bad: Function-level imports (can cause bundling issues)
   class MyClass:
       def method(self):
           from cp_library.math.mod.mint_cls import mint
           return mint(42)
   ```

### Benchmark Best Practices

When writing benchmarks in the `perf/` directory, follow these guidelines for fair and accurate performance comparisons:

#### 1. Reducing Timing Overhead
- **Make data structures hashable**: Add `__hash__` methods to custom data structures to avoid conversion overhead in timed sections
  ```python
  class MyDataStructure:
      def __hash__(self):
          return hash(tuple(self.data))  # Efficient hashable representation
  ```

- **Return objects directly**: Let the benchmark framework handle checksums after timing
  ```python
  # Good: Return data structure directly
  @benchmark.implementation("my_impl", "construction")
  def construct_my_impl(data):
      ds = MyDataStructure(data['initial_values'])
      return ds  # Framework will hash this after timing
  
  # Also good: Return non-hashable objects (lists, etc.)
  @benchmark.implementation("list_impl", "construction")
  def construct_list_impl(data):
      result = [x * 2 for x in data['initial_values']]
      return result  # Framework will convert to tuple(result) and hash
  
  # Framework automatically handles:
  # - Lists: converted to tuple(list) 
  # - Sets: converted to tuple(sorted(set)) for consistent ordering
  # - Dicts: converted to tuple(sorted(dict.items())) for consistent ordering
  # - Objects: converted to tuple(sorted(obj.__dict__.items()))
  
  # Bad: Calculate hash during timed section
  @benchmark.implementation("my_impl", "construction")
  def construct_my_impl(data):
      ds = MyDataStructure(data['initial_values'])
      return hash(tuple(ds.data))  # Overhead during timing
  ```

- **Move expensive computations outside timed sections**: Use setup functions for data preparation
  ```python
  @benchmark.setup("my_impl")
  def setup_my_impl(data):
      # Expensive preprocessing outside timing
      return {
          'preprocessed': expensive_preparation(data['raw_data']),
          'indices': data['indices']
      }
  ```

#### 2. Data Consistency
- **Use identical data sources**: All implementations being compared must use the exact same input data
- **Avoid prepared data inconsistencies**: Don't mix `data['prepared_values']` with `data['raw_values']` between implementations
- **Example**: Both `segtree2_sum` and `segtree_tuple_sum` should use `data['tuple_values']`

#### 3. Fair Overhead Patterns
- **Eliminate lambda functions**: Replace lambdas with predefined functions to ensure consistent overhead
  ```python
  # Bad: Mixed lambda and function usage
  seg1 = SegTree2(lambda a, b: (a[0] + b[0], a[1] + b[1]), ...)
  seg2 = SegTree(tuple_add, ...)
  
  # Good: Consistent function usage
  seg1 = SegTree2(tuple_add, ...)
  seg2 = SegTree(tuple_add, ...)
  ```

- **Avoid zip operations in timed code**: Use indexed loops instead of zip with unpacking
  ```python
  # Bad: Complex zip with unpacking in timed section
  for i, (va, vb) in zip(data['indices'], zip(data['values_a'], data['values_b'])):
      # timing-sensitive code
  
  # Good: Indexed loops with prepared data
  indices = data['indices']
  updates = data['prepared_updates']  # prepared in setup
  for j in range(len(indices)):
      i = indices[j]
      val = updates[j]
      # timing-sensitive code
  ```

### 3. Setup Functions
- **Move data preparation to setup**: Use `@benchmark.setup()` to prepare complex data structures outside timing loops
- **Keep setup functions simple**: When possible, use a single `@benchmark.setup("default")` function
- **Prepare data consistently**: Ensure all implementations have access to the same prepared data

### 4. Validation Requirements
- **Return consistent checksums**: All implementations must return comparable validation values
- **Use identical operations**: Ensure the same mathematical operations are performed in both implementations
- **Handle validation failures**: If implementations return different checksums, check data consistency first

### 5. Implementation Patterns
- **Focus on single operations**: Benchmark one operation type (e.g., only sum, not both sum and max)
- **Use consistent naming**: Follow the pattern `{structure}_{operation}` vs `{structure}_tuple_{operation}`
- **Simplify when possible**: Remove unnecessary complexity that doesn't contribute to the performance comparison

### 6. Common Pitfalls to Avoid
- **Data source mismatches**: Using different data keys between implementations
- **Inconsistent computational overhead**: Mixed use of lambdas, zip operations, or different loop patterns
- **Setup function gaps**: Missing setup functions for operations that need prepared data
- **Validation inconsistencies**: Different validation logic between implementations

### Example Structure
```python
# Good benchmark structure
@benchmark.setup("default")
def setup(data):
    prepared = data.copy()
    return prepared

@benchmark.implementation("struct_sum", "operation")
def implementation_struct_sum(data):
    struct = Struct(operation_func, identity, data['tuple_values'])
    # consistent timing logic
    return checksum

@benchmark.implementation("struct_tuple_sum", "operation") 
def implementation_struct_tuple_sum(data):
    struct = Struct(operation_func, identity, data['tuple_values'])  # same data!
    # identical timing logic
    return checksum
```

## Important Notes

- Always activate the conda environment (`conda activate atcoder`) before running tests
- The library uses PyPy for performance in competitive programming contexts
- Tests are computationally intensive and may take significant time to run
- The verify-helper tool caches results in `.verify-helper/cache/`
- When modifying algorithms, ensure corresponding tests still pass