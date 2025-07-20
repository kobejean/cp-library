#!/usr/bin/env python3
"""
Benchmark comparing list6 (6-array list) vs regular tuple list.
Tests construction, access, modification, sorting, append/pop operations.
"""

import random
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from cp_library.perf.benchmark import Benchmark, BenchmarkConfig
from cp_library.ds.list.list6_cls import list6

# Configure benchmark
config = BenchmarkConfig(
    name="list6",
    sizes=[1000000, 100000, 10000, 1000, 100],  # Reverse order to warm up JIT
    operations=['construction', 'tuple_access', 'iteration', 'modification', 'sorting', 'append_pop', 'add_operation'],
    iterations=10,
    warmup=3,
    output_dir="./output/benchmark_results/list6"
)

# Create benchmark instance
benchmark = Benchmark(config)

# Data generator
@benchmark.data_generator("default")
def generate_list6_data(size: int, operation: str):
    """Generate test data for list6 operations"""
    # Generate parallel arrays
    A1 = [random.randint(1, 1000000) for _ in range(size)]
    A2 = [random.randint(1, 1000000) for _ in range(size)]
    A3 = [random.randint(1, 1000000) for _ in range(size)]
    A4 = [random.randint(1, 1000000) for _ in range(size)]
    A5 = [random.randint(1, 1000000) for _ in range(size)]
    A6 = [random.randint(1, 1000000) for _ in range(size)]
    
    # Create list6 instance
    l6 = list6(A1.copy(), A2.copy(), A3.copy(), A4.copy(), A5.copy(), A6.copy())
    
    # Create equivalent data structures
    tuple_list = [(A1[i], A2[i], A3[i], A4[i], A5[i], A6[i]) for i in range(size)]
    list_of_lists = [[A1[i], A2[i], A3[i], A4[i], A5[i], A6[i]] for i in range(size)]
    
    return {
        'list6': l6,
        'tuple_list': tuple_list,
        'list_of_lists': list_of_lists,
        'A1': A1.copy(),
        'A2': A2.copy(),
        'A3': A3.copy(),
        'A4': A4.copy(),
        'A5': A5.copy(),
        'A6': A6.copy(),
        'size': size
    }

# Setup functions for operations that modify data
@benchmark.setup("list6", ["modification", "sorting", "append_pop", "add_operation"])
def setup_list6_modify(data):
    """Setup function that copies list6 data before modification"""
    new_data = data.copy()
    A1_copy = data['A1'].copy()
    A2_copy = data['A2'].copy()
    A3_copy = data['A3'].copy()
    A4_copy = data['A4'].copy()
    A5_copy = data['A5'].copy()
    A6_copy = data['A6'].copy()
    new_data['list6'] = list6(A1_copy, A2_copy, A3_copy, A4_copy, A5_copy, A6_copy)
    return new_data

@benchmark.setup("tuple_list", ["modification", "sorting", "append_pop"])
def setup_tuple_list_modify(data):
    """Setup function that copies tuple list before modification"""
    new_data = data.copy()
    new_data['tuple_list'] = data['tuple_list'].copy()
    return new_data

@benchmark.setup("list_of_lists", ["modification", "sorting", "append_pop"])
def setup_list_of_lists_modify(data):
    """Setup function that copies list of lists before modification"""
    new_data = data.copy()
    new_data['list_of_lists'] = [row.copy() for row in data['list_of_lists']]
    return new_data

# Construction operation
@benchmark.implementation("list6", "construction")
def construction_list6(data):
    """Construct list6 from arrays"""
    A1_copy = data['A1'].copy()
    A2_copy = data['A2'].copy()
    A3_copy = data['A3'].copy()
    A4_copy = data['A4'].copy()
    A5_copy = data['A5'].copy()
    A6_copy = data['A6'].copy()
    l6 = list6(A1_copy, A2_copy, A3_copy, A4_copy, A5_copy, A6_copy)
    return len(l6)

@benchmark.implementation("tuple_list", "construction")
def construction_tuple_list(data):
    """Construct tuple list from arrays"""
    A1, A2, A3, A4, A5, A6 = data['A1'], data['A2'], data['A3'], data['A4'], data['A5'], data['A6']
    tuple_list = [(A1[i], A2[i], A3[i], A4[i], A5[i], A6[i]) for i in range(len(A1))]
    return len(tuple_list)

@benchmark.implementation("list_of_lists", "construction")
def construction_list_of_lists(data):
    """Construct list of lists from arrays"""
    A1, A2, A3, A4, A5, A6 = data['A1'], data['A2'], data['A3'], data['A4'], data['A5'], data['A6']
    list_of_lists = [[A1[i], A2[i], A3[i], A4[i], A5[i], A6[i]] for i in range(len(A1))]
    return len(list_of_lists)

# Tuple access operation
@benchmark.implementation("list6", "tuple_access")
def tuple_access_list6(data):
    """Access tuples using list6[i]"""
    l6 = data['list6']
    checksum = 0
    for i in range(len(l6)):
        a1, a2, a3, a4, a5, a6 = l6[i]
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

@benchmark.implementation("list_of_lists", "tuple_access")
def tuple_access_list_of_lists(data):
    """Access elements using list[i]"""
    list_of_lists = data['list_of_lists']
    checksum = 0
    for i in range(len(list_of_lists)):
        row = list_of_lists[i]
        a1, a2, a3, a4, a5, a6 = row[0], row[1], row[2], row[3], row[4], row[5]
        checksum ^= a1 ^ a2 ^ a3 ^ a4 ^ a5 ^ a6
    return checksum

# Iteration operation
@benchmark.implementation("list6", "iteration")
def iteration_list6(data):
    """Iterate through list6 using for-in"""
    l6 = data['list6']
    checksum = 0
    for a1, a2, a3, a4, a5, a6 in l6:
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

@benchmark.implementation("list_of_lists", "iteration")
def iteration_list_of_lists(data):
    """Iterate through list of lists"""
    list_of_lists = data['list_of_lists']
    checksum = 0
    for row in list_of_lists:
        a1, a2, a3, a4, a5, a6 = row[0], row[1], row[2], row[3], row[4], row[5]
        checksum ^= a1 ^ a2 ^ a3 ^ a4 ^ a5 ^ a6
    return checksum

# Modification operation
@benchmark.implementation("list6", "modification")
def modification_list6(data):
    """Modify list6 elements using __setitem__"""
    l6 = data['list6']
    checksum = 0
    for i in range(len(l6)):
        a1, a2, a3, a4, a5, a6 = l6[i]
        new_a1 = (a1 * 2) & 0xFFFFFFFF
        new_a2 = (a2 * 3) & 0xFFFFFFFF
        new_a3 = (a3 * 4) & 0xFFFFFFFF
        new_a4 = (a4 * 5) & 0xFFFFFFFF
        new_a5 = (a5 * 6) & 0xFFFFFFFF
        new_a6 = (a6 * 7) & 0xFFFFFFFF
        l6[i] = (new_a1, new_a2, new_a3, new_a4, new_a5, new_a6)
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

@benchmark.implementation("list_of_lists", "modification")
def modification_list_of_lists(data):
    """Modify list of lists elements"""
    list_of_lists = data['list_of_lists']
    checksum = 0
    for i in range(len(list_of_lists)):
        row = list_of_lists[i]
        a1, a2, a3, a4, a5, a6 = row[0], row[1], row[2], row[3], row[4], row[5]
        new_a1 = (a1 * 2) & 0xFFFFFFFF
        new_a2 = (a2 * 3) & 0xFFFFFFFF
        new_a3 = (a3 * 4) & 0xFFFFFFFF
        new_a4 = (a4 * 5) & 0xFFFFFFFF
        new_a5 = (a5 * 6) & 0xFFFFFFFF
        new_a6 = (a6 * 7) & 0xFFFFFFFF
        row[0], row[1], row[2], row[3], row[4], row[5] = new_a1, new_a2, new_a3, new_a4, new_a5, new_a6
        checksum ^= new_a1 ^ new_a2 ^ new_a3 ^ new_a4 ^ new_a5 ^ new_a6
    return checksum

# Sorting operation
@benchmark.implementation("list6", "sorting")
def sorting_list6(data):
    """Sort list6 using isort_parallel"""
    l6 = data['list6']
    l6.sort()  # Uses isort_parallel on all 6 arrays
    
    checksum = 0
    for i in range(min(100, len(l6))):
        a1, a2, a3, a4, a5, a6 = l6[i]
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

@benchmark.implementation("list_of_lists", "sorting")
def sorting_list_of_lists(data):
    """Sort list of lists by first element"""
    list_of_lists = data['list_of_lists']
    list_of_lists.sort(key=lambda x: x[0])
    
    checksum = 0
    for i in range(min(100, len(list_of_lists))):
        row = list_of_lists[i]
        a1, a2, a3, a4, a5, a6 = row[0], row[1], row[2], row[3], row[4], row[5]
        checksum ^= a1 ^ a2 ^ a3 ^ a4 ^ a5 ^ a6
    return checksum

# Append/pop operation
@benchmark.implementation("list6", "append_pop")
def append_pop_list6(data):
    """Test list6 append/pop operations"""
    l6 = data['list6']
    checksum = 0
    operations = min(1000, len(l6) // 10)
    
    # Pop from end and append back
    for _ in range(operations):
        a1, a2, a3, a4, a5, a6 = l6.pop()
        checksum ^= a1 ^ a2 ^ a3 ^ a4 ^ a5 ^ a6
    for i in range(operations):
        vals = (i + 1000, i + 2000, i + 3000, i + 4000, i + 5000, i + 6000)
        l6.append(vals)
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

@benchmark.implementation("list_of_lists", "append_pop")
def append_pop_list_of_lists(data):
    """Test list of lists append/pop operations"""
    list_of_lists = data['list_of_lists']
    checksum = 0
    operations = min(1000, len(list_of_lists) // 10)
    
    # Pop from end and append back
    for _ in range(operations):
        row = list_of_lists.pop()
        a1, a2, a3, a4, a5, a6 = row[0], row[1], row[2], row[3], row[4], row[5]
        checksum ^= a1 ^ a2 ^ a3 ^ a4 ^ a5 ^ a6
    for i in range(operations):
        vals = [i + 1000, i + 2000, i + 3000, i + 4000, i + 5000, i + 6000]
        list_of_lists.append(vals)
        checksum ^= vals[0] ^ vals[1] ^ vals[2] ^ vals[3] ^ vals[4] ^ vals[5]
    return checksum

# Add operation (specific to list6)
@benchmark.implementation("list6", "add_operation")
def add_operation_list6(data):
    """Test list6 add operation"""
    l6 = data['list6']
    checksum = 0
    for i in range(len(l6)):
        base = i % 100
        add_val = (base, base * 2, base * 3, base * 4, base * 5, base * 6)
        l6.add(i, add_val)
        a1, a2, a3, a4, a5, a6 = l6[i]
        checksum ^= a1 ^ a2 ^ a3 ^ a4 ^ a5 ^ a6
    return checksum

if __name__ == "__main__":
    # Parse command line args and run appropriate mode
    runner = benchmark.parse_args()
    runner.run()