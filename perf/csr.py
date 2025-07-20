#!/usr/bin/env python3
"""
Benchmark comparing CSR vs list of lists for sparse row operations.
Tests direct access, view creation, iteration patterns, and modification.
"""

import random
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from cp_library.perf.benchmark import Benchmark, BenchmarkConfig
from cp_library.ds.view.csr_cls import CSR

# Configure benchmark
config = BenchmarkConfig(
    name="csr",
    sizes=[1000000, 100000, 10000, 1000, 100],  # Reverse order to warm up JIT
    operations=['copy_construction', 'direct_access', 'random_access', 'indexed_iter', 'foreach_iter', 'modification', 'bucketize', 'col1_indexed_iter', 'col1_foreach_iter'],
    iterations=10,
    warmup=3,
    output_dir="./output/benchmark_results/csr"
)

# Create benchmark instance
benchmark = Benchmark(config)

# Data generator
@benchmark.data_generator("default")
def generate_csr_data(size: int, operation: str):
    """Generate test data for CSR operations"""
    # Create rows with variable sizes (using CSR2's better approach)
    row_sizes = []
    total = 0
    
    while total < size:
        row_size = random.randint(50, 150)
        if total + row_size > size:
            row_size = size - total
        row_sizes.append(row_size)
        total += row_size
    
    # Generate offset array
    O = [0]
    for row_size in row_sizes:
        O.append(O[-1] + row_size)
    
    # Generate data array
    A = [random.randint(1, 1000000) for _ in range(size)]
    
    # Create list of lists equivalent
    list_of_lists = []
    for i in range(len(row_sizes)):
        start, end = O[i], O[i + 1]
        list_of_lists.append(A[start:end].copy())
    
    # Create CSR
    csr = CSR(A.copy(), O.copy())
    
    # For bucketize operation
    actual_num_rows = len(row_sizes)
    keys = [random.randint(0, max(0, actual_num_rows - 1)) for _ in range(size)]
    values = [random.randint(0, 1000000) for _ in range(size)]
    
    return {
        'csr': csr,
        'list_of_lists': list_of_lists,
        'A': A,
        'O': O,
        'num_rows': len(row_sizes),
        'keys': keys,
        'values': values,
        'size': size,
        'operation': operation
    }

# Specialized data generator for single-element rows
@benchmark.data_generator("col1_indexed_iter")
def generate_col1_indexed_data(size: int, operation: str):
    """Generate test data where every row has exactly 1 column - tests indexed iteration"""
    return _generate_col1_data(size, operation)

@benchmark.data_generator("col1_foreach_iter")
def generate_col1_foreach_data(size: int, operation: str):
    """Generate test data where every row has exactly 1 column - tests foreach iteration"""
    return _generate_col1_data(size, operation)

def _generate_col1_data(size: int, operation: str):
    """Helper to generate single-element row data"""
    # Each row has exactly 1 element
    num_rows = size
    
    # Generate offset array for single-element rows
    O = list(range(size + 1))  # [0, 1, 2, 3, ..., size]
    
    # Generate data array
    A = [random.randint(1, 1000000) for _ in range(size)]
    
    # Create list of lists equivalent (each row has 1 element)
    list_of_lists = [[A[i]] for i in range(size)]
    
    # Create CSR
    csr = CSR(A.copy(), O.copy())
    
    # For bucketize operation - distribute across fewer buckets to avoid empty ones
    bucket_count = max(1, size // 10)  # 10 elements per bucket on average
    keys = [random.randint(0, bucket_count - 1) for _ in range(size)]
    values = [random.randint(0, 1000000) for _ in range(size)]
    
    return {
        'csr': csr,
        'list_of_lists': list_of_lists,
        'A': A,
        'O': O,
        'num_rows': num_rows,
        'keys': keys,
        'values': values,
        'size': size,
        'operation': operation,
        'bucket_count': bucket_count
    }

# Setup functions for operations that modify data
@benchmark.setup("csr", ["modification"])
def setup_csr_modify(data):
    """Setup function that copies CSR data before modification"""
    new_data = data.copy()
    A_copy = data['A'].copy()
    O_copy = data['O'].copy()
    new_data['csr'] = CSR(A_copy, O_copy)
    return new_data

@benchmark.setup("list_of_lists", ["modification"])
def setup_list_modify(data):
    """Setup function that copies list data before modification"""
    new_data = data.copy()
    new_data['list_of_lists'] = [row.copy() for row in data['list_of_lists']]
    return new_data

# Direct element access operation
@benchmark.implementation("csr", "direct_access")
def direct_access_csr(data):
    """Access elements using csr(i,j)"""
    csr = data['csr']
    checksum = 0
    for i in range(len(csr)):
        for j in range(len(csr[i])):
            checksum ^= csr(i, j)
    return checksum

@benchmark.implementation("list_of_lists", "direct_access")
def direct_access_list_of_lists(data):
    """Access elements using list[i][j]"""
    list_of_lists = data['list_of_lists']
    checksum = 0
    for i in range(len(list_of_lists)):
        for j in range(len(list_of_lists[i])):
            checksum ^= list_of_lists[i][j]
    return checksum


# Indexed iteration using [i] access
@benchmark.implementation("csr", "indexed_iter")
def indexed_iter_csr(data):
    """Iterate using csr[i] access"""
    csr = data['csr']
    checksum = 0
    for i in range(len(csr)):
        row_view = csr[i]
        for j in range(len(row_view)):
            checksum ^= row_view[j]
    return checksum

@benchmark.implementation("list_of_lists", "indexed_iter")
def indexed_iter_list_of_lists(data):
    """Iterate using list[i] access"""
    list_of_lists = data['list_of_lists']
    checksum = 0
    for i in range(len(list_of_lists)):
        row = list_of_lists[i]
        for j in range(len(row)):
            checksum ^= row[j]
    return checksum

# Foreach iteration using for-in pattern
@benchmark.implementation("csr", "foreach_iter")
def foreach_iter_csr(data):
    """Iterate using for row in csr"""
    csr = data['csr']
    checksum = 0
    for row_view in csr:
        for element in row_view:
            checksum ^= element
    return checksum

@benchmark.implementation("list_of_lists", "foreach_iter")
def foreach_iter_list_of_lists(data):
    """Iterate using for row in list"""
    list_of_lists = data['list_of_lists']
    checksum = 0
    for row in list_of_lists:
        for element in row:
            checksum ^= element
    return checksum

# In-place modification operation
@benchmark.implementation("csr", "modification")
def modification_csr(data):
    """Modify elements through CSR view"""
    csr = data['csr']
    checksum = 0
    for i in range(len(csr)):
        row_view = csr[i]
        for j in range(len(row_view)):
            row_view[j] = (row_view[j] * 2) & 0xFFFFFFFF
            checksum ^= row_view[j]
    return checksum

@benchmark.implementation("list_of_lists", "modification")
def modification_list_of_lists(data):
    """Modify elements in list directly"""
    list_of_lists = data['list_of_lists']
    checksum = 0
    for i in range(len(list_of_lists)):
        row = list_of_lists[i]
        for j in range(len(row)):
            row[j] = (row[j] * 2) & 0xFFFFFFFF
            checksum ^= row[j]
    return checksum

# Copy construction operation
@benchmark.implementation("csr", "copy_construction")
def copy_construction_csr(data):
    """Construct CSR from copied arrays for fair comparison"""
    A_copy = data['A'].copy()
    O_copy = data['O'].copy()
    csr = CSR(A_copy, O_copy)
    return len(csr)

@benchmark.implementation("list_of_lists", "copy_construction")
def copy_construction_list_of_lists(data):
    """Copy pre-initialized list of lists"""
    list_structure = [row.copy() for row in data['list_of_lists']]
    return len(list_structure)

# Random access operation
@benchmark.implementation("csr", "random_access")
def random_access_csr(data):
    """Random access using csr(i,j)"""
    csr = data['csr']
    checksum = 0
    num_accesses = min(1000, data['size'] // 10)
    
    rng = random.Random(42)
    for _ in range(num_accesses):
        i = rng.randint(0, data['num_rows'] - 1)
        row_size = len(csr[i])
        if row_size > 0:
            j = rng.randint(0, row_size - 1)
            checksum ^= csr(i, j)
    return checksum & 0xFFFFFFFF

@benchmark.implementation("list_of_lists", "random_access")
def random_access_list_of_lists(data):
    """Random access through list of lists"""
    list_of_lists = data['list_of_lists']
    checksum = 0
    num_accesses = min(1000, data['size'] // 10)
    
    rng = random.Random(42)
    for _ in range(num_accesses):
        i = rng.randint(0, data['num_rows'] - 1)
        if len(list_of_lists[i]) > 0:
            j = rng.randint(0, len(list_of_lists[i]) - 1)
            checksum ^= list_of_lists[i][j]
    return checksum & 0xFFFFFFFF

# Bucketize operation
@benchmark.implementation("csr", "bucketize")
def bucketize_csr(data):
    """Use CSR.bucketize method"""
    csr = CSR.bucketize(data['num_rows'], data['keys'], data['values'])
    checksum = 0
    for i in range(len(csr)):
        row_view = csr[i]
        for j in range(len(row_view)):
            checksum ^= row_view[j]
    return checksum & 0xFFFFFFFF

@benchmark.implementation("list_of_lists", "bucketize")
def bucketize_list_of_lists(data):
    """Manual bucketization into lists"""
    keys = data['keys']
    values = data['values']
    num_rows = data['num_rows']
    
    buckets = [[] for _ in range(num_rows)]
    
    for i in range(len(keys)):
        k = keys[i]
        if 0 <= k < num_rows:
            buckets[k].append(values[i])
    
    checksum = 0
    for i in range(num_rows):
        for j in range(len(buckets[i])):
            checksum ^= buckets[i][j]
    return checksum & 0xFFFFFFFF

# Column-1 iteration - indexed access
@benchmark.implementation("csr", "col1_indexed_iter")
def col1_indexed_csr(data):
    """Iterate through CSR where every row has exactly 1 element using indexed access"""
    csr = data['csr']
    
    checksum = 0
    # Iterate through many single-element rows using indexing
    for i in range(len(csr)):
        view = csr[i]  # Each view has exactly 1 element
        checksum ^= view[0]  # Access the single element
    
    return checksum & 0xFFFFFFFF

@benchmark.implementation("list_of_lists", "col1_indexed_iter")
def col1_indexed_lists(data):
    """Iterate through list of single-element lists using indexed access"""
    list_of_lists = data['list_of_lists']
    
    checksum = 0
    # Iterate through many single-element lists using indexing
    for i in range(len(list_of_lists)):
        checksum ^= list_of_lists[i][0]  # Each row has exactly 1 element
    
    return checksum & 0xFFFFFFFF

@benchmark.implementation("direct_array", "col1_indexed_iter")
def col1_indexed_direct(data):
    """Direct indexed access through array (baseline for single elements)"""
    A = data['A']
    
    checksum = 0
    # Direct indexed iteration - each element is its own "row"
    for i in range(len(A)):
        checksum ^= A[i]
    
    return checksum & 0xFFFFFFFF

@benchmark.implementation("csr", "col1_foreach_iter")
def col1_foreach_csr(data):
    """Iterate through CSR using foreach loop where every row has exactly 1 element"""
    csr = data['csr']
    
    checksum = 0
    # Use foreach iteration pattern (Python will use __getitem__)
    for view in csr:  # Each view has exactly 1 element
        checksum ^= view[0]  # Access the single element
    
    return checksum & 0xFFFFFFFF

@benchmark.implementation("list_of_lists", "col1_foreach_iter")
def col1_foreach_lists(data):
    """Iterate through list of single-element lists using foreach"""
    list_of_lists = data['list_of_lists']
    
    checksum = 0
    # Use foreach iteration pattern
    for row in list_of_lists:
        checksum ^= row[0]  # Each row has exactly 1 element
    
    return checksum & 0xFFFFFFFF

@benchmark.implementation("direct_array", "col1_foreach_iter")
def col1_foreach_direct(data):
    """Direct foreach iteration through array (baseline for single elements)"""
    A = data['A']
    
    checksum = 0
    # Direct foreach iteration - each element is its own "row"
    for val in A:
        checksum ^= val
    
    return checksum & 0xFFFFFFFF

if __name__ == "__main__":
    # Parse command line args and run appropriate mode
    runner = benchmark.parse_args()
    runner.run()