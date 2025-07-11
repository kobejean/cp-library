#!/usr/bin/env python3
"""
Benchmark comparing view2 (dual-array view) vs tuple list.
Tests tuple access, iteration, sorting, modification, and append/pop operations.
"""

import random
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from cp_library.perf.benchmark import Benchmark, BenchmarkConfig
from cp_library.ds.view.view2_cls import view2

# Configure benchmark
config = BenchmarkConfig(
    name="view2",
    sizes=[1000000, 100000, 10000, 1000, 100],  # Reverse order to warm up JIT
    operations=['tuple_access', 'iteration', 'sorting', 'modification', 'append_pop'],
    iterations=10,
    warmup=3,
    output_dir="./output/benchmark_results/view2"
)

# Create benchmark instance
benchmark = Benchmark(config)

# Data generator
@benchmark.data_generator("default")
def generate_view2_data(size: int, operation: str):
    """Generate test data for view2 operations"""
    # Generate parallel arrays
    A = [random.randint(1, 1000000) for _ in range(size)]
    B = [random.randint(1, 1000000) for _ in range(size)]
    
    # Create view2 covering full range
    view2 = view2(A.copy(), B.copy(), 0, size)
    
    # Create equivalent data structures
    tuple_list = [(A[i], B[i]) for i in range(size)]
    
    return {
        'view2': view2,
        'tuple_list': tuple_list,
        'A': A.copy(),
        'B': B.copy(),
        'size': size
    }

# Setup functions for operations that modify data
@benchmark.setup("view2", ["modification", "sorting", "append_pop"])
def setup_view2_modify(data):
    """Setup function that copies view2 data before modification"""
    new_data = data.copy()
    A_copy = data['A'].copy()
    B_copy = data['B'].copy()
    new_data['view2'] = view2(A_copy, B_copy, 0, data['size'])
    return new_data

@benchmark.setup("tuple_list", ["modification", "sorting", "append_pop"])
def setup_tuple_list_modify(data):
    """Setup function that copies tuple list before modification"""
    new_data = data.copy()
    new_data['tuple_list'] = data['tuple_list'].copy()
    return new_data

# Tuple access operation
@benchmark.implementation("view2", "tuple_access")
def tuple_access_view2(data):
    """Access tuples using view2[i]"""
    view2 = data['view2']
    checksum = 0
    for i in range(len(view2)):
        a, b = view2[i]
        checksum ^= a ^ b
    return checksum

@benchmark.implementation("tuple_list", "tuple_access")
def tuple_access_tuple_list(data):
    """Access tuples using list[i]"""
    tuple_list = data['tuple_list']
    checksum = 0
    for i in range(len(tuple_list)):
        a, b = tuple_list[i]
        checksum ^= a ^ b
    return checksum

# Iteration operation
@benchmark.implementation("view2", "iteration")
def iteration_view2(data):
    """Iterate through view2 using for-in (no __iter__)"""
    view2 = data['view2']
    checksum = 0
    for a, b in view2:  # Uses __getitem__ with IndexError
        checksum ^= a ^ b
    return checksum

@benchmark.implementation("tuple_list", "iteration")
def iteration_tuple_list(data):
    """Iterate through tuple list using for-in"""
    tuple_list = data['tuple_list']
    checksum = 0
    for a, b in tuple_list:
        checksum ^= a ^ b
    return checksum

# Sorting operation
@benchmark.implementation("view2", "sorting")
def sorting_view2(data):
    """Sort view2 using isort_ranged"""
    view2 = data['view2']
    view2.sort()  # Uses isort_ranged on view range
    
    checksum = 0
    for i in range(min(100, len(view2))):
        a, b = view2[i]
        checksum ^= a ^ b
    return checksum

@benchmark.implementation("tuple_list", "sorting")
def sorting_tuple_list(data):
    """Sort tuple list by first element"""
    tuple_list = data['tuple_list']
    tuple_list.sort(key=lambda x: x[0])
    
    checksum = 0
    for i in range(min(100, len(tuple_list))):
        a, b = tuple_list[i]
        checksum ^= a ^ b
    return checksum

# Modification operation
@benchmark.implementation("view2", "modification")
def modification_view2(data):
    """Modify view2 elements using __setitem__"""
    view2 = data['view2']
    checksum = 0
    for i in range(len(view2)):
        a, b = view2[i]
        new_a = (a * 2) & 0xFFFFFFFF
        new_b = (b * 3) & 0xFFFFFFFF
        view2[i] = (new_a, new_b)
        checksum ^= new_a ^ new_b
    return checksum

@benchmark.implementation("tuple_list", "modification")
def modification_tuple_list(data):
    """Modify tuple list elements"""
    tuple_list = data['tuple_list']
    checksum = 0
    for i in range(len(tuple_list)):
        a, b = tuple_list[i]
        new_a = (a * 2) & 0xFFFFFFFF
        new_b = (b * 3) & 0xFFFFFFFF
        tuple_list[i] = (new_a, new_b)
        checksum ^= new_a ^ new_b
    return checksum

# Append/pop operation
@benchmark.implementation("view2", "append_pop")
def append_pop_view2(data):
    """Test view2 append/pop operations"""
    view2 = data['view2']
    checksum = 0
    operations = min(1000, len(view2) // 10)
    
    # Pop from end and append back
    for _ in range(operations):
        a, b = view2.pop()
        checksum ^= a ^ b
    for i in range(operations):
        view2.append((i + 1000, i + 2000))
        checksum ^= (i + 1000) ^ (i + 2000)
    return checksum

@benchmark.implementation("tuple_list", "append_pop")
def append_pop_tuple_list(data):
    """Test tuple list append/pop operations"""
    tuple_list = data['tuple_list']
    checksum = 0
    operations = min(1000, len(tuple_list) // 10)
    
    # Pop from end and append back
    for _ in range(operations):
        a, b = tuple_list.pop()
        checksum ^= a ^ b
    for i in range(operations):
        tuple_list.append((i + 1000, i + 2000))
        checksum ^= (i + 1000) ^ (i + 2000)
    return checksum

if __name__ == "__main__":
    # Parse command line args and run appropriate mode
    runner = benchmark.parse_args()
    runner.run()