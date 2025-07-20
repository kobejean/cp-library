#!/usr/bin/env python3
"""
Benchmark comparing list2 (dual-array list) vs regular tuple list.
Tests construction, access, modification, sorting, append/pop operations.
"""

import random
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from cp_library.perf.benchmark import Benchmark, BenchmarkConfig
from cp_library.ds.list.list2_cls import list2

# Configure benchmark
config = BenchmarkConfig(
    name="list2",
    sizes=[1000000, 100000, 10000, 1000, 100],  # Reverse order to warm up JIT
    operations=['construction', 'tuple_access', 'iteration', 'modification', 'sorting', 'append_pop', 'add_operation'],
    iterations=10,
    warmup=3,
    output_dir="./output/benchmark_results/list2"
)

# Create benchmark instance
benchmark = Benchmark(config)

# Data generator
@benchmark.data_generator("default")
def generate_list2_data(size: int, operation: str):
    """Generate test data for list2 operations"""
    # Generate parallel arrays
    A1 = [random.randint(1, 1000000) for _ in range(size)]
    A2 = [random.randint(1, 1000000) for _ in range(size)]
    
    # Create list2 instance
    l2 = list2(A1.copy(), A2.copy())
    
    # Create equivalent data structures
    tuple_list = [(A1[i], A2[i]) for i in range(size)]
    list_of_lists = [[A1[i], A2[i]] for i in range(size)]
    
    return {
        'list2': l2,
        'tuple_list': tuple_list,
        'list_of_lists': list_of_lists,
        'A1': A1.copy(),
        'A2': A2.copy(),
        'size': size
    }

# Setup functions for operations that modify data
@benchmark.setup("list2", ["modification", "sorting", "append_pop", "add_operation"])
def setup_list2_modify(data):
    """Setup function that copies list2 data before modification"""
    new_data = data.copy()
    A1_copy = data['A1'].copy()
    A2_copy = data['A2'].copy()
    new_data['list2'] = list2(A1_copy, A2_copy)
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
@benchmark.implementation("list2", "construction")
def construction_list2(data):
    """Construct list2 from arrays"""
    A1_copy = data['A1'].copy()
    A2_copy = data['A2'].copy()
    l2 = list2(A1_copy, A2_copy)
    return len(l2)

@benchmark.implementation("tuple_list", "construction")
def construction_tuple_list(data):
    """Construct tuple list from arrays"""
    A1, A2 = data['A1'], data['A2']
    tuple_list = [(A1[i], A2[i]) for i in range(len(A1))]
    return len(tuple_list)

@benchmark.implementation("list_of_lists", "construction")
def construction_list_of_lists(data):
    """Construct list of lists from arrays"""
    A1, A2 = data['A1'], data['A2']
    list_of_lists = [[A1[i], A2[i]] for i in range(len(A1))]
    return len(list_of_lists)

# Tuple access operation
@benchmark.implementation("list2", "tuple_access")
def tuple_access_list2(data):
    """Access tuples using list2[i]"""
    l2 = data['list2']
    checksum = 0
    for i in range(len(l2)):
        a1, a2 = l2[i]
        checksum ^= a1 ^ a2
    return checksum

@benchmark.implementation("tuple_list", "tuple_access")
def tuple_access_tuple_list(data):
    """Access tuples using list[i]"""
    tuple_list = data['tuple_list']
    checksum = 0
    for i in range(len(tuple_list)):
        a1, a2 = tuple_list[i]
        checksum ^= a1 ^ a2
    return checksum

@benchmark.implementation("list_of_lists", "tuple_access")
def tuple_access_list_of_lists(data):
    """Access elements using list[i]"""
    list_of_lists = data['list_of_lists']
    checksum = 0
    for i in range(len(list_of_lists)):
        a1, a2 = list_of_lists[i][0], list_of_lists[i][1]
        checksum ^= a1 ^ a2
    return checksum

# Iteration operation
@benchmark.implementation("list2", "iteration")
def iteration_list2(data):
    """Iterate through list2 using for-in"""
    l2 = data['list2']
    checksum = 0
    for a1, a2 in l2:
        checksum ^= a1 ^ a2
    return checksum

@benchmark.implementation("tuple_list", "iteration")
def iteration_tuple_list(data):
    """Iterate through tuple list using for-in"""
    tuple_list = data['tuple_list']
    checksum = 0
    for a1, a2 in tuple_list:
        checksum ^= a1 ^ a2
    return checksum

@benchmark.implementation("list_of_lists", "iteration")
def iteration_list_of_lists(data):
    """Iterate through list of lists"""
    list_of_lists = data['list_of_lists']
    checksum = 0
    for row in list_of_lists:
        a1, a2 = row[0], row[1]
        checksum ^= a1 ^ a2
    return checksum

# Modification operation
@benchmark.implementation("list2", "modification")
def modification_list2(data):
    """Modify list2 elements using __setitem__"""
    l2 = data['list2']
    checksum = 0
    for i in range(len(l2)):
        a1, a2 = l2[i]
        new_a1 = (a1 * 2) & 0xFFFFFFFF
        new_a2 = (a2 * 3) & 0xFFFFFFFF
        l2[i] = (new_a1, new_a2)
        checksum ^= new_a1 ^ new_a2
    return checksum

@benchmark.implementation("tuple_list", "modification")
def modification_tuple_list(data):
    """Modify tuple list elements"""
    tuple_list = data['tuple_list']
    checksum = 0
    for i in range(len(tuple_list)):
        a1, a2 = tuple_list[i]
        new_a1 = (a1 * 2) & 0xFFFFFFFF
        new_a2 = (a2 * 3) & 0xFFFFFFFF
        tuple_list[i] = (new_a1, new_a2)
        checksum ^= new_a1 ^ new_a2
    return checksum

@benchmark.implementation("list_of_lists", "modification")
def modification_list_of_lists(data):
    """Modify list of lists elements"""
    list_of_lists = data['list_of_lists']
    checksum = 0
    for i in range(len(list_of_lists)):
        a1, a2 = list_of_lists[i][0], list_of_lists[i][1]
        new_a1 = (a1 * 2) & 0xFFFFFFFF
        new_a2 = (a2 * 3) & 0xFFFFFFFF
        list_of_lists[i][0] = new_a1
        list_of_lists[i][1] = new_a2
        checksum ^= new_a1 ^ new_a2
    return checksum

# Sorting operation
@benchmark.implementation("list2", "sorting")
def sorting_list2(data):
    """Sort list2 using isort_parallel"""
    l2 = data['list2']
    l2.sort()  # Uses isort_parallel on both arrays
    
    checksum = 0
    for i in range(min(100, len(l2))):
        a1, a2 = l2[i]
        checksum ^= a1 ^ a2
    return checksum

@benchmark.implementation("tuple_list", "sorting")
def sorting_tuple_list(data):
    """Sort tuple list by first element"""
    tuple_list = data['tuple_list']
    tuple_list.sort(key=lambda x: x[0])
    
    checksum = 0
    for i in range(min(100, len(tuple_list))):
        a1, a2 = tuple_list[i]
        checksum ^= a1 ^ a2
    return checksum

@benchmark.implementation("list_of_lists", "sorting")
def sorting_list_of_lists(data):
    """Sort list of lists by first element"""
    list_of_lists = data['list_of_lists']
    list_of_lists.sort(key=lambda x: x[0])
    
    checksum = 0
    for i in range(min(100, len(list_of_lists))):
        a1, a2 = list_of_lists[i][0], list_of_lists[i][1]
        checksum ^= a1 ^ a2
    return checksum

# Append/pop operation
@benchmark.implementation("list2", "append_pop")
def append_pop_list2(data):
    """Test list2 append/pop operations"""
    l2 = data['list2']
    checksum = 0
    operations = min(1000, len(l2) // 10)
    
    # Pop from end and append back
    for _ in range(operations):
        a1, a2 = l2.pop()
        checksum ^= a1 ^ a2
    for i in range(operations):
        l2.append((i + 1000, i + 2000))
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
        a1, a2 = tuple_list.pop()
        checksum ^= a1 ^ a2
    for i in range(operations):
        tuple_list.append((i + 1000, i + 2000))
        checksum ^= (i + 1000) ^ (i + 2000)
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
        a1, a2 = row[0], row[1]
        checksum ^= a1 ^ a2
    for i in range(operations):
        list_of_lists.append([i + 1000, i + 2000])
        checksum ^= (i + 1000) ^ (i + 2000)
    return checksum

# Add operation (specific to list2)
@benchmark.implementation("list2", "add_operation")
def add_operation_list2(data):
    """Test list2 add operation"""
    l2 = data['list2']
    checksum = 0
    for i in range(len(l2)):
        add_val = (i % 100, (i % 100) * 2)
        l2.add(i, add_val)
        a1, a2 = l2[i]
        checksum ^= a1 ^ a2
    return checksum

if __name__ == "__main__":
    # Parse command line args and run appropriate mode
    runner = benchmark.parse_args()
    runner.run()