#!/usr/bin/env python3
"""
Benchmark comparing view6 (6-array view) vs tuple list.
Tests tuple access, iteration, sorting, modification, and append/pop operations.
"""

import random
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from cp_library.perf.benchmark import Benchmark, BenchmarkConfig
from cp_library.ds.view.view6_cls import view6

# Configure benchmark
config = BenchmarkConfig(
    name="view6",
    sizes=[1000000, 100000, 10000, 1000, 100],  # Reverse order to warm up JIT
    operations=['tuple_access', 'iteration', 'sorting', 'modification', 'append_pop'],
    iterations=10,
    warmup=3,
    output_dir="./output/benchmark_results/view6"
)

# Create benchmark instance
benchmark = Benchmark(config)

# Data generator
@benchmark.data_generator("default")
def generate_view6_data(size: int, operation: str):
    """Generate test data for view6 operations"""
    # Generate parallel arrays
    A1 = [random.randint(1, 1000000) for _ in range(size)]
    A2 = [random.randint(1, 1000000) for _ in range(size)]
    A3 = [random.randint(1, 1000000) for _ in range(size)]
    A4 = [random.randint(1, 1000000) for _ in range(size)]
    A5 = [random.randint(1, 1000000) for _ in range(size)]
    A6 = [random.randint(1, 1000000) for _ in range(size)]
    
    # Create view6 covering full range
    v6 = view6(A1.copy(), A2.copy(), A3.copy(), A4.copy(), A5.copy(), A6.copy(), 0, size)
    
    # Create equivalent data structures
    tuple_list = [(A1[i], A2[i], A3[i], A4[i], A5[i], A6[i]) for i in range(size)]
    
    return {
        'view6': v6,
        'tuple_list': tuple_list,
        'A1': A1.copy(),
        'A2': A2.copy(),
        'A3': A3.copy(),
        'A4': A4.copy(),
        'A5': A5.copy(),
        'A6': A6.copy(),
        'size': size
    }

# Setup functions for operations that modify data
@benchmark.setup("view6", ["modification", "sorting", "append_pop"])
def setup_view6_modify(data):
    """Setup function that copies view6 data before modification"""
    new_data = data.copy()
    A1_copy = data['A1'].copy()
    A2_copy = data['A2'].copy()
    A3_copy = data['A3'].copy()
    A4_copy = data['A4'].copy()
    A5_copy = data['A5'].copy()
    A6_copy = data['A6'].copy()
    new_data['view6'] = view6(A1_copy, A2_copy, A3_copy, A4_copy, A5_copy, A6_copy, 0, data['size'])
    return new_data

@benchmark.setup("tuple_list", ["modification", "sorting", "append_pop"])
def setup_tuple_list_modify(data):
    """Setup function that copies tuple list before modification"""
    new_data = data.copy()
    new_data['tuple_list'] = data['tuple_list'].copy()
    return new_data

# Tuple access operation
@benchmark.implementation("view6", "tuple_access")
def tuple_access_view6(data):
    """Access tuples using view6[i]"""
    v6 = data['view6']
    checksum = 0
    for i in range(len(v6)):
        a1, a2, a3, a4, a5, a6 = v6[i]
        checksum ^= a1 ^ a2 ^ a3 ^ a4 ^ a5 ^ a6
    return checksum

@benchmark.implementation("tuple_list", "tuple_access")
def tuple_access_tuple_list(data):
    """Access tuples using list[i]"""
    tuple_list = data['tuple_list']
    checksum = 0
    for i in range(len(tuple_list)):
        a1, a2, a3, a4, a5, a6 = tuple_list[i]
        checksum ^= a1 ^ a2 ^ a3 ^ a4 ^ a5 ^ a6
    return checksum

# Iteration operation
@benchmark.implementation("view6", "iteration")
def iteration_view6(data):
    """Iterate through view6 using for-in (no __iter__)"""
    v6 = data['view6']
    checksum = 0
    for a1, a2, a3, a4, a5, a6 in v6:  # Uses __getitem__ with IndexError
        checksum ^= a1 ^ a2 ^ a3 ^ a4 ^ a5 ^ a6
    return checksum

@benchmark.implementation("tuple_list", "iteration")
def iteration_tuple_list(data):
    """Iterate through tuple list using for-in"""
    tuple_list = data['tuple_list']
    checksum = 0
    for a1, a2, a3, a4, a5, a6 in tuple_list:
        checksum ^= a1 ^ a2 ^ a3 ^ a4 ^ a5 ^ a6
    return checksum

# Sorting operation
@benchmark.implementation("view6", "sorting")
def sorting_view6(data):
    """Sort view6 using isort_ranged"""
    v6 = data['view6']
    v6.sort()  # Uses isort_ranged on view range
    
    checksum = 0
    for i in range(min(100, len(v6))):
        a1, a2, a3, a4, a5, a6 = v6[i]
        checksum ^= a1 ^ a2 ^ a3 ^ a4 ^ a5 ^ a6
    return checksum

@benchmark.implementation("tuple_list", "sorting")
def sorting_tuple_list(data):
    """Sort tuple list by first element"""
    tuple_list = data['tuple_list']
    tuple_list.sort(key=lambda x: x[0])
    
    checksum = 0
    for i in range(min(100, len(tuple_list))):
        a1, a2, a3, a4, a5, a6 = tuple_list[i]
        checksum ^= a1 ^ a2 ^ a3 ^ a4 ^ a5 ^ a6
    return checksum

# Modification operation
@benchmark.implementation("view6", "modification")
def modification_view6(data):
    """Modify view6 elements using __setitem__"""
    v6 = data['view6']
    checksum = 0
    for i in range(len(v6)):
        a1, a2, a3, a4, a5, a6 = v6[i]
        new_a1 = (a1 * 2) & 0xFFFFFFFF
        new_a2 = (a2 * 3) & 0xFFFFFFFF
        new_a3 = (a3 * 4) & 0xFFFFFFFF
        new_a4 = (a4 * 5) & 0xFFFFFFFF
        new_a5 = (a5 * 6) & 0xFFFFFFFF
        new_a6 = (a6 * 7) & 0xFFFFFFFF
        v6[i] = (new_a1, new_a2, new_a3, new_a4, new_a5, new_a6)
        checksum ^= new_a1 ^ new_a2 ^ new_a3 ^ new_a4 ^ new_a5 ^ new_a6
    return checksum

@benchmark.implementation("tuple_list", "modification")
def modification_tuple_list(data):
    """Modify tuple list elements"""
    tuple_list = data['tuple_list']
    checksum = 0
    for i in range(len(tuple_list)):
        a1, a2, a3, a4, a5, a6 = tuple_list[i]
        new_a1 = (a1 * 2) & 0xFFFFFFFF
        new_a2 = (a2 * 3) & 0xFFFFFFFF
        new_a3 = (a3 * 4) & 0xFFFFFFFF
        new_a4 = (a4 * 5) & 0xFFFFFFFF
        new_a5 = (a5 * 6) & 0xFFFFFFFF
        new_a6 = (a6 * 7) & 0xFFFFFFFF
        tuple_list[i] = (new_a1, new_a2, new_a3, new_a4, new_a5, new_a6)
        checksum ^= new_a1 ^ new_a2 ^ new_a3 ^ new_a4 ^ new_a5 ^ new_a6
    return checksum

# Append/pop operation
@benchmark.implementation("view6", "append_pop")
def append_pop_view6(data):
    """Test view6 append/pop operations"""
    v6 = data['view6']
    checksum = 0
    operations = min(1000, len(v6) // 10)
    
    # Pop from end and append back
    for _ in range(operations):
        a1, a2, a3, a4, a5, a6 = v6.pop()
        checksum ^= a1 ^ a2 ^ a3 ^ a4 ^ a5 ^ a6
    for i in range(operations):
        vals = (i + 1000, i + 2000, i + 3000, i + 4000, i + 5000, i + 6000)
        v6.append(vals)
        checksum ^= vals[0] ^ vals[1] ^ vals[2] ^ vals[3] ^ vals[4] ^ vals[5]
    return checksum

@benchmark.implementation("tuple_list", "append_pop")
def append_pop_tuple_list(data):
    """Test tuple list append/pop operations"""
    tuple_list = data['tuple_list']
    checksum = 0
    operations = min(1000, len(tuple_list) // 10)
    
    # Pop from end and append back
    for _ in range(operations):
        a1, a2, a3, a4, a5, a6 = tuple_list.pop()
        checksum ^= a1 ^ a2 ^ a3 ^ a4 ^ a5 ^ a6
    for i in range(operations):
        vals = (i + 1000, i + 2000, i + 3000, i + 4000, i + 5000, i + 6000)
        tuple_list.append(vals)
        checksum ^= vals[0] ^ vals[1] ^ vals[2] ^ vals[3] ^ vals[4] ^ vals[5]
    return checksum

if __name__ == "__main__":
    # Parse command line args and run appropriate mode
    runner = benchmark.parse_args()
    runner.run()