#!/usr/bin/env python3
"""
Benchmark comparing CSR2 vs direct arrays for dual-array sparse data.
CSR2 provides view2 objects for efficient row access patterns.
"""

import random
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from cp_library.perf.benchmark import Benchmark, BenchmarkConfig
from cp_library.ds.view.csr2_cls import CSR2
from cp_library.ds.view.view2_cls import view2

# Configure benchmark
config = BenchmarkConfig(
    name="csr2",
    sizes=[10000000, 1000000, 100000, 10000, 1000, 100],  # Reverse order to warm up JIT
    operations=['copy_construction', 'direct_access', 'random_access', 'indexed_iter', 'foreach_iter', 'modification', 'bucketize', 'col1_indexed_iter', 'col1_foreach_iter'],
    iterations=10,
    warmup=3,
    output_dir="./output/benchmark_results/csr2"
)

# Create benchmark instance
benchmark = Benchmark(config)

# Data generator
@benchmark.data_generator("default")
def generate_csr2_data(size: int, operation: str):
    """Generate test data for CSR2 operations"""
    # Create rows with variable sizes
    num_rows = max(1, size // 100)  # Average 100 elements per row
    row_sizes = []
    total = 0
    
    while total < size:
        row_size = random.randint(50, 150)
        if total + row_size > size:
            row_size = size - total
        row_sizes.append(row_size)
        total += row_size
    
    # Generate offset array
    offsets = [0]
    for row_size in row_sizes:
        offsets.append(offsets[-1] + row_size)
    
    # Generate data arrays
    array_a = [random.randint(0, 1000000) for _ in range(size)]
    array_b = [random.randint(0, 1000000) for _ in range(size)]
    
    # Create list of lists structure
    list_structure = []
    for i in range(len(row_sizes)):
        start = offsets[i]
        end = offsets[i + 1]
        row = [(array_a[j], array_b[j]) for j in range(start, end)]
        list_structure.append(row)
    
    # For bucketize operation
    actual_num_rows = len(row_sizes)
    keys = [random.randint(0, max(0, actual_num_rows - 1)) for _ in range(size)]
    values_v = [random.randint(0, 1000000) for _ in range(size)]
    values_w = [random.randint(0, 1000000) for _ in range(size)]
    
    return {
        'array_a': array_a,
        'array_b': array_b,
        'offsets': offsets,
        'num_rows': len(row_sizes),
        'list_structure': list_structure,
        'keys': keys,
        'values_v': values_v,
        'values_w': values_w,
        'size': size
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
    offsets = list(range(size + 1))  # [0, 1, 2, 3, ..., size]
    
    # Generate data arrays
    array_a = [random.randint(0, 1000000) for _ in range(size)]
    array_b = [random.randint(0, 1000000) for _ in range(size)]
    
    # Create list of lists structure (each row has 1 element)
    list_structure = [[(array_a[i], array_b[i])] for i in range(size)]
    
    # For bucketize operation - distribute across fewer buckets to avoid empty ones
    bucket_count = max(1, size // 10)  # 10 elements per bucket on average
    keys = [random.randint(0, bucket_count - 1) for _ in range(size)]
    values_v = [random.randint(0, 1000000) for _ in range(size)]
    values_w = [random.randint(0, 1000000) for _ in range(size)]
    
    return {
        'array_a': array_a,
        'array_b': array_b,
        'offsets': offsets,
        'num_rows': num_rows,
        'list_structure': list_structure,
        'keys': keys,
        'values_v': values_v,
        'values_w': values_w,
        'size': size,
        'bucket_count': bucket_count
    }

# Copy construction operation
@benchmark.implementation("csr2", "copy_construction")
def copy_construction_csr2(data):
    """Construct CSR2 from copied arrays for fair comparison"""
    array_a_copy = data['array_a'].copy()
    array_b_copy = data['array_b'].copy()
    offsets_copy = data['offsets'].copy()
    csr = CSR2(array_a_copy, array_b_copy, offsets_copy)
    return len(csr)

@benchmark.implementation("direct_arrays", "copy_construction")
def copy_construction_direct(data):
    """Copy arrays for fair comparison with CSR2"""
    array_a_copy = data['array_a'].copy()
    array_b_copy = data['array_b'].copy()
    offsets_copy = data['offsets'].copy()
    return len(offsets_copy) - 1  # Return number of rows

@benchmark.implementation("list_of_lists", "copy_construction")
def copy_construction_list_of_lists(data):
    """Copy pre-initialized list of lists"""
    list_structure = [row.copy() for row in data['list_structure']]
    return len(list_structure)

# Direct access operation
@benchmark.implementation("csr2", "direct_access")
def direct_access_csr2(data):
    """Direct access through CSR2 views"""
    csr = CSR2(data['array_a'], data['array_b'], data['offsets'])
    checksum = 0
    for i in range(len(csr)):
        view = csr[i]
        for j in range(len(view)):
            a_val = view.A[view.l + j]
            b_val = view.B[view.l + j]
            checksum ^= (a_val + b_val)
    return checksum & 0xFFFFFFFF

@benchmark.implementation("direct_arrays", "direct_access")
def direct_access_direct(data):
    """Direct access using direct arrays"""
    array_a = data['array_a']
    array_b = data['array_b']
    offsets = data['offsets']
    checksum = 0
    for i in range(data['num_rows']):
        for j in range(offsets[i], offsets[i + 1]):
            checksum ^= (array_a[j] + array_b[j])
    return checksum & 0xFFFFFFFF

@benchmark.implementation("list_of_lists", "direct_access")
def direct_access_list_of_lists(data):
    """Direct access through list of lists"""
    list_structure = data['list_structure']
    checksum = 0
    for row in list_structure:
        for a_val, b_val in row:
            checksum ^= (a_val + b_val)
    return checksum & 0xFFFFFFFF

# Random access operation
@benchmark.implementation("csr2", "random_access")
def random_access_csr2(data):
    """Random access using csr(i,j)"""
    csr = CSR2(data['array_a'], data['array_b'], data['offsets'])
    checksum = 0
    num_accesses = min(1000, data['size'] // 10)
    
    rng = random.Random(42)
    for _ in range(num_accesses):
        i = rng.randint(0, data['num_rows'] - 1)
        row_size = data['offsets'][i + 1] - data['offsets'][i]
        if row_size > 0:
            j = rng.randint(0, row_size - 1)
            a_val, b_val = csr(i, j)
            checksum ^= (a_val + b_val)
    return checksum & 0xFFFFFFFF

@benchmark.implementation("direct_arrays", "random_access")
def random_access_direct(data):
    """Random access using direct indexing"""
    array_a = data['array_a']
    array_b = data['array_b']
    offsets = data['offsets']
    checksum = 0
    num_accesses = min(1000, data['size'] // 10)
    
    rng = random.Random(42)
    for _ in range(num_accesses):
        i = rng.randint(0, data['num_rows'] - 1)
        start = offsets[i]
        end = offsets[i + 1]
        if end > start:
            j = rng.randint(0, end - start - 1)
            checksum ^= (array_a[start + j] + array_b[start + j])
    return checksum & 0xFFFFFFFF

@benchmark.implementation("list_of_lists", "random_access")
def random_access_list_of_lists(data):
    """Random access through list of lists"""
    list_structure = data['list_structure']
    checksum = 0
    num_accesses = min(1000, data['size'] // 10)
    
    rng = random.Random(42)
    for _ in range(num_accesses):
        i = rng.randint(0, data['num_rows'] - 1)
        if len(list_structure[i]) > 0:
            j = rng.randint(0, len(list_structure[i]) - 1)
            a_val, b_val = list_structure[i][j]
            checksum ^= (a_val + b_val)
    return checksum & 0xFFFFFFFF

# Setup for modify operations
@benchmark.setup("csr2", ["modification"])
def setup_csr2_modify(data):
    """Copy data before modification"""
    new_data = data.copy()
    new_data['array_a'] = data['array_a'].copy()
    new_data['array_b'] = data['array_b'].copy()
    return new_data

@benchmark.setup("direct_arrays", ["modification"])
def setup_direct_modify(data):
    """Copy data before modification"""
    new_data = data.copy()
    new_data['array_a'] = data['array_a'].copy()
    new_data['array_b'] = data['array_b'].copy()
    return new_data

@benchmark.setup("list_of_lists", ["modification"])
def setup_list_of_lists_modify(data):
    """Copy list structure before modification"""
    new_data = data.copy()
    new_data['list_structure'] = [row.copy() for row in data['list_structure']]
    return new_data

# Modification operation
@benchmark.implementation("csr2", "modification")
def modification_csr2(data):
    """Modify elements using csr.set(i,j,val)"""
    csr = CSR2(data['array_a'], data['array_b'], data['offsets'])
    checksum = 0
    num_modifications = min(1000, data['size'] // 10)
    
    rng = random.Random(42)
    for _ in range(num_modifications):
        i = rng.randint(0, data['num_rows'] - 1)
        row_size = data['offsets'][i + 1] - data['offsets'][i]
        if row_size > 0:
            j = rng.randint(0, row_size - 1)
            new_val = (rng.randint(0, 1000000), rng.randint(0, 1000000))
            csr.set(i, j, new_val)
            checksum ^= (new_val[0] + new_val[1])
    return checksum & 0xFFFFFFFF

@benchmark.implementation("direct_arrays", "modification")
def modification_direct(data):
    """Modify elements using direct array access"""
    array_a = data['array_a']
    array_b = data['array_b']
    offsets = data['offsets']
    checksum = 0
    num_modifications = min(1000, data['size'] // 10)
    
    rng = random.Random(42)
    for _ in range(num_modifications):
        i = rng.randint(0, data['num_rows'] - 1)
        start = offsets[i]
        end = offsets[i + 1]
        if end > start:
            j = rng.randint(0, end - start - 1)
            new_val_a = rng.randint(0, 1000000)
            new_val_b = rng.randint(0, 1000000)
            array_a[start + j] = new_val_a
            array_b[start + j] = new_val_b
            checksum ^= (new_val_a + new_val_b)
    return checksum & 0xFFFFFFFF

@benchmark.implementation("list_of_lists", "modification")
def modification_list_of_lists(data):
    """Modify elements in list of lists"""
    list_structure = data['list_structure']
    checksum = 0
    num_modifications = min(1000, data['size'] // 10)
    
    rng = random.Random(42)
    for _ in range(num_modifications):
        i = rng.randint(0, data['num_rows'] - 1)
        if len(list_structure[i]) > 0:
            j = rng.randint(0, len(list_structure[i]) - 1)
            new_val = (rng.randint(0, 1000000), rng.randint(0, 1000000))
            list_structure[i][j] = new_val
            checksum ^= (new_val[0] + new_val[1])
    return checksum & 0xFFFFFFFF

# Indexed iteration using [i] access
@benchmark.implementation("csr2", "indexed_iter")
def indexed_iter_csr2(data):
    """Iterate using csr[i] access"""
    csr = CSR2(data['array_a'], data['array_b'], data['offsets'])
    checksum = 0
    for i in range(len(csr)):
        row_view = csr[i]
        for j in range(len(row_view)):
            a_val, b_val = row_view[j]
            checksum ^= (a_val + b_val)
    return checksum & 0xFFFFFFFF

@benchmark.implementation("direct_arrays", "indexed_iter")
def indexed_iter_direct(data):
    """Iterate using direct array access"""
    array_a = data['array_a']
    array_b = data['array_b']
    offsets = data['offsets']
    checksum = 0
    for i in range(data['num_rows']):
        for j in range(offsets[i], offsets[i + 1]):
            checksum ^= (array_a[j] + array_b[j])
    return checksum & 0xFFFFFFFF

@benchmark.implementation("list_of_lists", "indexed_iter")
def indexed_iter_list_of_lists(data):
    """Iterate using list[i] access"""
    list_structure = data['list_structure']
    checksum = 0
    for i in range(len(list_structure)):
        row = list_structure[i]
        for j in range(len(row)):
            a_val, b_val = row[j]
            checksum ^= (a_val + b_val)
    return checksum & 0xFFFFFFFF

# Foreach iteration using for-in pattern
@benchmark.implementation("csr2", "foreach_iter")
def foreach_iter_csr2(data):
    """Iterate using for row in csr"""
    csr = CSR2(data['array_a'], data['array_b'], data['offsets'])
    checksum = 0
    for row_view in csr:
        for a_val, b_val in row_view:
            checksum ^= (a_val + b_val)
    return checksum & 0xFFFFFFFF

@benchmark.implementation("direct_arrays", "foreach_iter")
def foreach_iter_direct(data):
    """Iterate using direct arrays with manual chunking"""
    array_a = data['array_a']
    array_b = data['array_b']
    offsets = data['offsets']
    checksum = 0
    for i in range(data['num_rows']):
        for j in range(offsets[i], offsets[i + 1]):
            checksum ^= (array_a[j] + array_b[j])
    return checksum & 0xFFFFFFFF

@benchmark.implementation("list_of_lists", "foreach_iter")
def foreach_iter_list_of_lists(data):
    """Iterate using for row in list"""
    list_structure = data['list_structure']
    checksum = 0
    for row in list_structure:
        for a_val, b_val in row:
            checksum ^= (a_val + b_val)
    return checksum & 0xFFFFFFFF


# Bucketize operation
@benchmark.implementation("csr2", "bucketize")
def bucketize_csr2(data):
    """Use CSR2.bucketize method"""
    csr = CSR2.bucketize(data['num_rows'], data['keys'], data['values_v'], data['values_w'])
    checksum = 0
    for i in range(len(csr)):
        view = csr[i]
        for j in range(len(view)):
            checksum ^= (view.A[view.l + j] + view.B[view.l + j])
    return checksum & 0xFFFFFFFF

@benchmark.implementation("manual_bucketize", "bucketize")
def bucketize_manual(data):
    """Manual bucketization into lists"""
    keys = data['keys']
    values_v = data['values_v']
    values_w = data['values_w']
    num_rows = data['num_rows']
    
    buckets_a = [[] for _ in range(num_rows)]
    buckets_b = [[] for _ in range(num_rows)]
    
    for i in range(len(keys)):
        k = keys[i]
        if 0 <= k < num_rows:
            buckets_a[k].append(values_v[i])
            buckets_b[k].append(values_w[i])
    
    checksum = 0
    for i in range(num_rows):
        for j in range(len(buckets_a[i])):
            checksum ^= (buckets_a[i][j] + buckets_b[i][j])
    return checksum & 0xFFFFFFFF

# Column-1 iteration - indexed access
@benchmark.implementation("csr2", "col1_indexed_iter")
def col1_indexed_csr2(data):
    """Iterate through CSR2 where every row has exactly 1 element using indexed access"""
    array_a = data['array_a']
    array_b = data['array_b']
    offsets = data['offsets']
    csr = CSR2(array_a, array_b, offsets)
    
    checksum = 0
    # Iterate through many single-element rows using indexing
    for i in range(len(csr)):
        view = csr[i]  # Each view has exactly 1 element
        checksum ^= (view.A[view.l] + view.B[view.l])  # Direct access to single element
    
    return checksum & 0xFFFFFFFF

@benchmark.implementation("list_of_lists", "col1_indexed_iter")
def col1_indexed_lists(data):
    """Iterate through list of single-element lists using indexed access"""
    list_structure = data['list_structure']
    
    checksum = 0
    # Iterate through many single-element lists using indexing
    for i in range(len(list_structure)):
        a_val, b_val = list_structure[i][0]  # Each row has exactly 1 element
        checksum ^= (a_val + b_val)
    
    return checksum & 0xFFFFFFFF

@benchmark.implementation("direct_arrays", "col1_indexed_iter")
def col1_indexed_direct(data):
    """Direct indexed access through arrays (baseline for single elements)"""
    array_a = data['array_a']
    array_b = data['array_b']
    
    checksum = 0
    # Direct indexed iteration - each element is its own "row"
    for i in range(len(array_a)):
        checksum ^= (array_a[i] + array_b[i])
    
    return checksum & 0xFFFFFFFF

@benchmark.implementation("csr2", "col1_foreach_iter")
def col1_foreach_csr2(data):
    """Iterate through CSR2 using foreach loop where every row has exactly 1 element"""
    array_a = data['array_a']
    array_b = data['array_b']
    offsets = data['offsets']
    csr = CSR2(array_a, array_b, offsets)
    
    checksum = 0
    # Use foreach iteration pattern
    for view in csr:  # Each view has exactly 1 element
        a_val, b_val = view[0]  # Access the single element
        checksum ^= (a_val + b_val)
    
    return checksum & 0xFFFFFFFF

@benchmark.implementation("list_of_lists", "col1_foreach_iter")
def col1_foreach_lists(data):
    """Iterate through list of single-element lists using foreach"""
    list_structure = data['list_structure']
    
    checksum = 0
    # Use foreach iteration pattern
    for row in list_structure:
        a_val, b_val = row[0]  # Each row has exactly 1 element
        checksum ^= (a_val + b_val)
    
    return checksum & 0xFFFFFFFF

@benchmark.implementation("direct_arrays", "col1_foreach_iter")
def col1_foreach_direct(data):
    """Direct foreach iteration through arrays (baseline for single elements)"""
    array_a = data['array_a']
    array_b = data['array_b']
    
    checksum = 0
    # Direct foreach iteration - each element is its own "row"
    for i in range(len(array_a)):
        checksum ^= (array_a[i] + array_b[i])
    
    return checksum & 0xFFFFFFFF

if __name__ == "__main__":
    # Parse command line args and run appropriate mode
    runner = benchmark.parse_args()
    runner.run()