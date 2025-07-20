#!/usr/bin/env python3
"""
Benchmark comparing CSR6 vs direct arrays for 6-array sparse data.
CSR6 provides view6 objects for efficient row access patterns.
"""

import random
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from cp_library.perf.benchmark import Benchmark, BenchmarkConfig
from cp_library.ds.view.csr6_cls import CSR6
from cp_library.ds.view.view6_cls import view6

# Configure benchmark
config = BenchmarkConfig(
    name="csr6",
    sizes=[1000000, 100000, 10000, 1000, 100],  # Reverse order to warm up JIT
    operations=['copy_construction', 'direct_access', 'random_access', 'indexed_iter', 'foreach_iter', 'modification', 'bucketize', 'col1_indexed_iter', 'col1_foreach_iter'],
    iterations=10,
    warmup=3,
    output_dir="./output/benchmark_results/csr6"
)

# Create benchmark instance
benchmark = Benchmark(config)

# Data generator
@benchmark.data_generator("default")
def generate_csr6_data(size: int, operation: str):
    """Generate test data for CSR6 operations"""
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
    array_a1 = [random.randint(0, 1000000) for _ in range(size)]
    array_a2 = [random.randint(0, 1000000) for _ in range(size)]
    array_a3 = [random.randint(0, 1000000) for _ in range(size)]
    array_a4 = [random.randint(0, 1000000) for _ in range(size)]
    array_a5 = [random.randint(0, 1000000) for _ in range(size)]
    array_a6 = [random.randint(0, 1000000) for _ in range(size)]
    
    # Create list of lists structure
    list_structure = []
    for i in range(len(row_sizes)):
        start = offsets[i]
        end = offsets[i + 1]
        row = [(array_a1[j], array_a2[j], array_a3[j], array_a4[j], array_a5[j], array_a6[j]) 
               for j in range(start, end)]
        list_structure.append(row)
    
    # For bucketize operation
    actual_num_rows = len(row_sizes)
    keys = [random.randint(0, max(0, actual_num_rows - 1)) for _ in range(size)]
    values_v1 = [random.randint(0, 1000000) for _ in range(size)]
    values_v2 = [random.randint(0, 1000000) for _ in range(size)]
    values_v3 = [random.randint(0, 1000000) for _ in range(size)]
    values_v4 = [random.randint(0, 1000000) for _ in range(size)]
    values_v5 = [random.randint(0, 1000000) for _ in range(size)]
    values_v6 = [random.randint(0, 1000000) for _ in range(size)]
    
    return {
        'array_a1': array_a1,
        'array_a2': array_a2,
        'array_a3': array_a3,
        'array_a4': array_a4,
        'array_a5': array_a5,
        'array_a6': array_a6,
        'offsets': offsets,
        'num_rows': len(row_sizes),
        'list_structure': list_structure,
        'keys': keys,
        'values_v1': values_v1,
        'values_v2': values_v2,
        'values_v3': values_v3,
        'values_v4': values_v4,
        'values_v5': values_v5,
        'values_v6': values_v6,
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
    array_a1 = [random.randint(0, 1000000) for _ in range(size)]
    array_a2 = [random.randint(0, 1000000) for _ in range(size)]
    array_a3 = [random.randint(0, 1000000) for _ in range(size)]
    array_a4 = [random.randint(0, 1000000) for _ in range(size)]
    array_a5 = [random.randint(0, 1000000) for _ in range(size)]
    array_a6 = [random.randint(0, 1000000) for _ in range(size)]
    
    # Create list of lists structure (each row has 1 element)
    list_structure = [[(array_a1[i], array_a2[i], array_a3[i], array_a4[i], array_a5[i], array_a6[i])] 
                      for i in range(size)]
    
    # For bucketize operation - distribute across fewer buckets to avoid empty ones
    bucket_count = max(1, size // 10)  # 10 elements per bucket on average
    keys = [random.randint(0, bucket_count - 1) for _ in range(size)]
    values_v1 = [random.randint(0, 1000000) for _ in range(size)]
    values_v2 = [random.randint(0, 1000000) for _ in range(size)]
    values_v3 = [random.randint(0, 1000000) for _ in range(size)]
    values_v4 = [random.randint(0, 1000000) for _ in range(size)]
    values_v5 = [random.randint(0, 1000000) for _ in range(size)]
    values_v6 = [random.randint(0, 1000000) for _ in range(size)]
    
    return {
        'array_a1': array_a1,
        'array_a2': array_a2,
        'array_a3': array_a3,
        'array_a4': array_a4,
        'array_a5': array_a5,
        'array_a6': array_a6,
        'offsets': offsets,
        'num_rows': num_rows,
        'list_structure': list_structure,
        'keys': keys,
        'values_v1': values_v1,
        'values_v2': values_v2,
        'values_v3': values_v3,
        'values_v4': values_v4,
        'values_v5': values_v5,
        'values_v6': values_v6,
        'size': size,
        'bucket_count': bucket_count
    }

# Copy construction operation
@benchmark.implementation("csr6", "copy_construction")
def copy_construction_csr6(data):
    """Construct CSR6 from copied arrays for fair comparison"""
    arrays_copy = [
        data['array_a1'].copy(),
        data['array_a2'].copy(),
        data['array_a3'].copy(),
        data['array_a4'].copy(),
        data['array_a5'].copy(),
        data['array_a6'].copy()
    ]
    offsets_copy = data['offsets'].copy()
    csr = CSR6(*arrays_copy, offsets_copy)
    return len(csr)

@benchmark.implementation("direct_arrays", "copy_construction")
def copy_construction_direct(data):
    """Copy arrays for fair comparison with CSR6"""
    arrays_copy = [
        data['array_a1'].copy(),
        data['array_a2'].copy(),
        data['array_a3'].copy(),
        data['array_a4'].copy(),
        data['array_a5'].copy(),
        data['array_a6'].copy()
    ]
    offsets_copy = data['offsets'].copy()
    return len(offsets_copy) - 1  # Return number of rows

@benchmark.implementation("list_of_lists", "copy_construction")
def copy_construction_list_of_lists(data):
    """Copy pre-initialized list of lists"""
    list_structure = [row.copy() for row in data['list_structure']]
    return len(list_structure)

# Direct access operation
@benchmark.implementation("csr6", "direct_access")
def direct_access_csr6(data):
    """Direct access through CSR6 views"""
    csr = CSR6(data['array_a1'], data['array_a2'], data['array_a3'], 
               data['array_a4'], data['array_a5'], data['array_a6'], data['offsets'])
    checksum = 0
    for i in range(len(csr)):
        view = csr[i]
        for j in range(len(view)):
            a1 = view.A1[view.l + j]
            a2 = view.A2[view.l + j]
            a3 = view.A3[view.l + j]
            a4 = view.A4[view.l + j]
            a5 = view.A5[view.l + j]
            a6 = view.A6[view.l + j]
            checksum ^= (a1 + a2 + a3 + a4 + a5 + a6)
    return checksum & 0xFFFFFFFF

@benchmark.implementation("direct_arrays", "direct_access")
def direct_access_direct(data):
    """Direct access using direct arrays"""
    arrays = [data['array_a1'], data['array_a2'], data['array_a3'], 
              data['array_a4'], data['array_a5'], data['array_a6']]
    offsets = data['offsets']
    checksum = 0
    for i in range(data['num_rows']):
        for j in range(offsets[i], offsets[i + 1]):
            sum_val = sum(arr[j] for arr in arrays)
            checksum ^= sum_val
    return checksum & 0xFFFFFFFF

@benchmark.implementation("list_of_lists", "direct_access")
def direct_access_list_of_lists(data):
    """Direct access through list of lists"""
    list_structure = data['list_structure']
    checksum = 0
    for row in list_structure:
        for a1, a2, a3, a4, a5, a6 in row:
            checksum ^= (a1 + a2 + a3 + a4 + a5 + a6)
    return checksum & 0xFFFFFFFF

# Random access operation
@benchmark.implementation("csr6", "random_access")
def random_access_csr6(data):
    """Random access using csr(i,j)"""
    csr = CSR6(data['array_a1'], data['array_a2'], data['array_a3'], 
               data['array_a4'], data['array_a5'], data['array_a6'], data['offsets'])
    checksum = 0
    num_accesses = min(1000, data['size'] // 10)
    
    rng = random.Random(42)
    for _ in range(num_accesses):
        i = rng.randint(0, data['num_rows'] - 1)
        row_size = data['offsets'][i + 1] - data['offsets'][i]
        if row_size > 0:
            j = rng.randint(0, row_size - 1)
            a1, a2, a3, a4, a5, a6 = csr(i, j)
            checksum ^= (a1 + a2 + a3 + a4 + a5 + a6)
    return checksum & 0xFFFFFFFF

@benchmark.implementation("direct_arrays", "random_access")
def random_access_direct(data):
    """Random access using direct indexing"""
    arrays = [data['array_a1'], data['array_a2'], data['array_a3'], 
              data['array_a4'], data['array_a5'], data['array_a6']]
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
            idx = start + j
            sum_val = sum(arr[idx] for arr in arrays)
            checksum ^= sum_val
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
            a1, a2, a3, a4, a5, a6 = list_structure[i][j]
            checksum ^= (a1 + a2 + a3 + a4 + a5 + a6)
    return checksum & 0xFFFFFFFF

# Setup for modify operations
@benchmark.setup("csr6", ["modification"])
def setup_csr6_modify(data):
    """Copy data before modification"""
    new_data = data.copy()
    new_data['array_a1'] = data['array_a1'].copy()
    new_data['array_a2'] = data['array_a2'].copy()
    new_data['array_a3'] = data['array_a3'].copy()
    new_data['array_a4'] = data['array_a4'].copy()
    new_data['array_a5'] = data['array_a5'].copy()
    new_data['array_a6'] = data['array_a6'].copy()
    return new_data

@benchmark.setup("direct_arrays", ["modification"])
def setup_direct_modify(data):
    """Copy data before modification"""
    new_data = data.copy()
    new_data['array_a1'] = data['array_a1'].copy()
    new_data['array_a2'] = data['array_a2'].copy()
    new_data['array_a3'] = data['array_a3'].copy()
    new_data['array_a4'] = data['array_a4'].copy()
    new_data['array_a5'] = data['array_a5'].copy()
    new_data['array_a6'] = data['array_a6'].copy()
    return new_data

@benchmark.setup("list_of_lists", ["modification"])
def setup_list_of_lists_modify(data):
    """Copy list structure before modification"""
    new_data = data.copy()
    new_data['list_structure'] = [row.copy() for row in data['list_structure']]
    return new_data

# Modification operation
@benchmark.implementation("csr6", "modification")
def modification_csr6(data):
    """Modify elements using csr.set(i,j,val)"""
    csr = CSR6(data['array_a1'], data['array_a2'], data['array_a3'], 
               data['array_a4'], data['array_a5'], data['array_a6'], data['offsets'])
    checksum = 0
    num_modifications = min(1000, data['size'] // 10)
    
    rng = random.Random(42)
    for _ in range(num_modifications):
        i = rng.randint(0, data['num_rows'] - 1)
        row_size = data['offsets'][i + 1] - data['offsets'][i]
        if row_size > 0:
            j = rng.randint(0, row_size - 1)
            new_vals = tuple(rng.randint(0, 1000000) for _ in range(6))
            csr.set(i, j, new_vals)
            checksum ^= sum(new_vals)
    return checksum & 0xFFFFFFFF

@benchmark.implementation("direct_arrays", "modification")
def modification_direct(data):
    """Modify elements using direct array access"""
    arrays = [data['array_a1'], data['array_a2'], data['array_a3'], 
              data['array_a4'], data['array_a5'], data['array_a6']]
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
            idx = start + j
            new_vals = [rng.randint(0, 1000000) for _ in range(6)]
            for k, arr in enumerate(arrays):
                arr[idx] = new_vals[k]
            checksum ^= sum(new_vals)
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
            new_val = tuple(rng.randint(0, 1000000) for _ in range(6))
            list_structure[i][j] = new_val
            checksum ^= sum(new_val)
    return checksum & 0xFFFFFFFF

# Indexed iteration using [i] access
@benchmark.implementation("csr6", "indexed_iter")
def indexed_iter_csr6(data):
    """Iterate using csr[i] access"""
    csr = CSR6(data['array_a1'], data['array_a2'], data['array_a3'], 
               data['array_a4'], data['array_a5'], data['array_a6'], data['offsets'])
    checksum = 0
    for i in range(len(csr)):
        row_view = csr[i]
        for j in range(len(row_view)):
            a1, a2, a3, a4, a5, a6 = row_view[j]
            checksum ^= (a1 + a2 + a3 + a4 + a5 + a6)
    return checksum & 0xFFFFFFFF

@benchmark.implementation("direct_arrays", "indexed_iter")
def indexed_iter_direct(data):
    """Iterate using direct array access"""
    arrays = [data['array_a1'], data['array_a2'], data['array_a3'], 
              data['array_a4'], data['array_a5'], data['array_a6']]
    offsets = data['offsets']
    checksum = 0
    for i in range(data['num_rows']):
        for j in range(offsets[i], offsets[i + 1]):
            sum_val = sum(arr[j] for arr in arrays)
            checksum ^= sum_val
    return checksum & 0xFFFFFFFF

@benchmark.implementation("list_of_lists", "indexed_iter")
def indexed_iter_list_of_lists(data):
    """Iterate using list[i] access"""
    list_structure = data['list_structure']
    checksum = 0
    for i in range(len(list_structure)):
        row = list_structure[i]
        for j in range(len(row)):
            a1, a2, a3, a4, a5, a6 = row[j]
            checksum ^= (a1 + a2 + a3 + a4 + a5 + a6)
    return checksum & 0xFFFFFFFF

# Foreach iteration using for-in pattern
@benchmark.implementation("csr6", "foreach_iter")
def foreach_iter_csr6(data):
    """Iterate using for row in csr"""
    csr = CSR6(data['array_a1'], data['array_a2'], data['array_a3'], 
               data['array_a4'], data['array_a5'], data['array_a6'], data['offsets'])
    checksum = 0
    for row_view in csr:
        for a1, a2, a3, a4, a5, a6 in row_view:
            checksum ^= (a1 + a2 + a3 + a4 + a5 + a6)
    return checksum & 0xFFFFFFFF

@benchmark.implementation("direct_arrays", "foreach_iter")
def foreach_iter_direct(data):
    """Iterate using direct arrays with manual chunking"""
    arrays = [data['array_a1'], data['array_a2'], data['array_a3'], 
              data['array_a4'], data['array_a5'], data['array_a6']]
    offsets = data['offsets']
    checksum = 0
    for i in range(data['num_rows']):
        for j in range(offsets[i], offsets[i + 1]):
            sum_val = sum(arr[j] for arr in arrays)
            checksum ^= sum_val
    return checksum & 0xFFFFFFFF

@benchmark.implementation("list_of_lists", "foreach_iter")
def foreach_iter_list_of_lists(data):
    """Iterate using for row in list"""
    list_structure = data['list_structure']
    checksum = 0
    for row in list_structure:
        for a1, a2, a3, a4, a5, a6 in row:
            checksum ^= (a1 + a2 + a3 + a4 + a5 + a6)
    return checksum & 0xFFFFFFFF

# Bucketize operation
@benchmark.implementation("csr6", "bucketize")
def bucketize_csr6(data):
    """Use CSR6.bucketize method"""
    csr = CSR6.bucketize(data['num_rows'], data['keys'], 
                         data['values_v1'], data['values_v2'], data['values_v3'],
                         data['values_v4'], data['values_v5'], data['values_v6'])
    checksum = 0
    for i in range(len(csr)):
        view = csr[i]
        for j in range(len(view)):
            vals = (view.A1[view.l + j], view.A2[view.l + j], view.A3[view.l + j],
                    view.A4[view.l + j], view.A5[view.l + j], view.A6[view.l + j])
            checksum ^= sum(vals)
    return checksum & 0xFFFFFFFF

@benchmark.implementation("manual_bucketize", "bucketize")
def bucketize_manual(data):
    """Manual bucketization into lists"""
    keys = data['keys']
    values = [data['values_v1'], data['values_v2'], data['values_v3'],
              data['values_v4'], data['values_v5'], data['values_v6']]
    num_rows = data['num_rows']
    
    buckets = [[[] for _ in range(6)] for _ in range(num_rows)]
    
    for i in range(len(keys)):
        k = keys[i]
        if 0 <= k < num_rows:
            for j in range(6):
                buckets[k][j].append(values[j][i])
    
    checksum = 0
    for i in range(num_rows):
        for j in range(len(buckets[i][0])):
            sum_val = sum(buckets[i][k][j] for k in range(6))
            checksum ^= sum_val
    return checksum & 0xFFFFFFFF

# Column-1 iteration - indexed access
@benchmark.implementation("csr6", "col1_indexed_iter")
def col1_indexed_csr6(data):
    """Iterate through CSR6 where every row has exactly 1 element using indexed access"""
    arrays = [data['array_a1'], data['array_a2'], data['array_a3'], 
              data['array_a4'], data['array_a5'], data['array_a6']]
    offsets = data['offsets']
    csr = CSR6(*arrays, offsets)
    
    checksum = 0
    # Iterate through many single-element rows using indexing
    for i in range(len(csr)):
        view = csr[i]  # Each view has exactly 1 element
        sum_val = sum(arr[view.l] for arr in [view.A1, view.A2, view.A3, view.A4, view.A5, view.A6])
        checksum ^= sum_val
    
    return checksum & 0xFFFFFFFF

@benchmark.implementation("list_of_lists", "col1_indexed_iter")
def col1_indexed_lists(data):
    """Iterate through list of single-element lists using indexed access"""
    list_structure = data['list_structure']
    
    checksum = 0
    # Iterate through many single-element lists using indexing
    for i in range(len(list_structure)):
        a1, a2, a3, a4, a5, a6 = list_structure[i][0]  # Each row has exactly 1 element
        checksum ^= (a1 + a2 + a3 + a4 + a5 + a6)
    
    return checksum & 0xFFFFFFFF

@benchmark.implementation("direct_arrays", "col1_indexed_iter")
def col1_indexed_direct(data):
    """Direct indexed access through arrays (baseline for single elements)"""
    arrays = [data['array_a1'], data['array_a2'], data['array_a3'], 
              data['array_a4'], data['array_a5'], data['array_a6']]
    
    checksum = 0
    # Direct indexed iteration - each element is its own "row"
    for i in range(len(arrays[0])):
        sum_val = sum(arr[i] for arr in arrays)
        checksum ^= sum_val
    
    return checksum & 0xFFFFFFFF

@benchmark.implementation("csr6", "col1_foreach_iter")
def col1_foreach_csr6(data):
    """Iterate through CSR6 using foreach loop where every row has exactly 1 element"""
    arrays = [data['array_a1'], data['array_a2'], data['array_a3'], 
              data['array_a4'], data['array_a5'], data['array_a6']]
    offsets = data['offsets']
    csr = CSR6(*arrays, offsets)
    
    checksum = 0
    # Use foreach iteration pattern
    for view in csr:  # Each view has exactly 1 element
        a1, a2, a3, a4, a5, a6 = view[0]  # Access the single element
        checksum ^= (a1 + a2 + a3 + a4 + a5 + a6)
    
    return checksum & 0xFFFFFFFF

@benchmark.implementation("list_of_lists", "col1_foreach_iter")
def col1_foreach_lists(data):
    """Iterate through list of single-element lists using foreach"""
    list_structure = data['list_structure']
    
    checksum = 0
    # Use foreach iteration pattern
    for row in list_structure:
        a1, a2, a3, a4, a5, a6 = row[0]  # Each row has exactly 1 element
        checksum ^= (a1 + a2 + a3 + a4 + a5 + a6)
    
    return checksum & 0xFFFFFFFF

@benchmark.implementation("direct_arrays", "col1_foreach_iter")
def col1_foreach_direct(data):
    """Direct foreach iteration through arrays (baseline for single elements)"""
    arrays = [data['array_a1'], data['array_a2'], data['array_a3'], 
              data['array_a4'], data['array_a5'], data['array_a6']]
    
    checksum = 0
    # Direct foreach iteration - each element is its own "row"
    for i in range(len(arrays[0])):
        sum_val = sum(arr[i] for arr in arrays)
        checksum ^= sum_val
    
    return checksum & 0xFFFFFFFF

if __name__ == "__main__":
    # Parse command line args and run appropriate mode
    runner = benchmark.parse_args()
    runner.run()