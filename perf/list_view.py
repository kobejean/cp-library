#!/usr/bin/env python3
"""
Benchmark comparing operations on list slices vs view objects.
Tests various operations to measure the overhead of slice copying vs view indirection.
"""

import random
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from cp_library.perf.benchmark import Benchmark, BenchmarkConfig
from cp_library.ds.view.view_cls import view

# Configure benchmark
config = BenchmarkConfig(
    name="list_view",
    sizes=[1000000, 100000, 10000, 1000, 100],  # Reverse order to warm up JIT
    operations=['construction', 'sum', 'modify', 'index', 'reverse', 'sort', 'nested_sum', 'pop', 'append'],
    iterations=10,
    warmup=3,
    output_dir="./output/benchmark_results/list_view"
)

# Create benchmark instance
benchmark = Benchmark(config)

# Data generator
@benchmark.data_generator("default")
def generate_view_data(size: int, operation: str):
    """Generate test data for slice/view operations"""
    # Generate random list
    data = [random.randint(0, 1000000) for _ in range(size)]
    
    # Generate random slice boundaries (10-50% of list)
    slice_size = random.randint(size // 10, size // 2)
    start = random.randint(0, size - slice_size)
    end = start + slice_size
    
    return {
        'data': data,
        'start': start,
        'end': end,
        'slice_size': slice_size,
        'search_value': random.randint(0, 1000000),
        'size': size,
        'operation': operation
    }

# Construction operation
@benchmark.implementation("slice", "construction")
def construction_slice(data):
    """Create a slice copy of the list"""
    lst = data['data']
    start, end = data['start'], data['end']
    
    # Create slice (copies data)
    slice_copy = lst[start:end]
    
    # Return checksum to ensure it's not optimized away
    checksum = 0
    for x in slice_copy:
        checksum ^= x
    return checksum

@benchmark.implementation("view", "construction")
def construction_view(data):
    """Create a view of the list"""
    lst = data['data']
    start, end = data['start'], data['end']
    
    # Create view (no copy)
    list_view = view(lst, start, end)
    
    # Return checksum to ensure it's not optimized away
    checksum = 0
    for i in range(len(list_view)):
        checksum ^= list_view[i]
    return checksum

# Sum operation
@benchmark.implementation("slice", "sum")
def sum_slice(data):
    """Sum elements in a slice"""
    lst = data['data']
    start, end = data['start'], data['end']
    
    # Create slice and sum
    slice_copy = lst[start:end]
    return sum(slice_copy) & 0xFFFFFFFF  # Keep as 32-bit for checksum

@benchmark.implementation("view", "sum")
def sum_view(data):
    """Sum elements in a view"""
    lst = data['data']
    start, end = data['start'], data['end']
    
    # Create view and sum through it
    list_view = view(lst, start, end)
    total = 0
    for i in range(len(list_view)):
        total += list_view[i]
    return total & 0xFFFFFFFF  # Keep as 32-bit for checksum

@benchmark.implementation("view_direct", "sum")
def sum_view_direct(data):
    """Sum elements using direct indexing"""
    lst = data['data']
    start, end = data['start'], data['end']
    
    # Sum directly without creating slice or view
    total = 0
    for i in range(start, end):
        total += lst[i]
    return total & 0xFFFFFFFF  # Keep as 32-bit for checksum

# Setup functions for operations that need copying
@benchmark.setup("slice", ["modify", "reverse", "sort", "pop", "append"])
def setup_slice_modify(data):
    """Setup function that copies data before modification"""
    new_data = data.copy()
    new_data['data'] = data['data'].copy()
    return new_data

@benchmark.setup("view", ["modify", "reverse", "sort", "pop", "append"])
def setup_view_modify(data):
    """Setup function that copies data before modification"""
    new_data = data.copy()
    new_data['data'] = data['data'].copy()
    return new_data

@benchmark.setup("view_direct", ["modify", "reverse", "sort", "pop", "append"])
def setup_view_direct_modify(data):
    """Setup function that copies data before modification"""
    new_data = data.copy()
    new_data['data'] = data['data'].copy()
    return new_data

# Modify operation
@benchmark.implementation("slice", "modify")
def modify_slice(data):
    """Modify elements in a slice"""
    lst = data['data']
    start, end = data['start'], data['end']
    
    # Create slice and modify
    slice_copy = lst[start:end]
    for i in range(len(slice_copy)):
        slice_copy[i] = (slice_copy[i] * 2) & 0xFFFFFFFF
    
    # Copy back to original positions manually
    for i, val in enumerate(slice_copy):
        lst[start + i] = val
    
    # Return checksum
    checksum = 0
    for i in range(start, end):
        checksum ^= lst[i]
    return checksum

@benchmark.implementation("view", "modify")
def modify_view(data):
    """Modify elements through a view"""
    lst = data['data']
    start, end = data['start'], data['end']
    
    # Create view and modify through it
    list_view = view(lst, start, end)
    for i in range(len(list_view)):
        list_view[i] = (list_view[i] * 2) & 0xFFFFFFFF
    
    # Return checksum
    checksum = 0
    for i in range(start, end):
        checksum ^= lst[i]
    return checksum

@benchmark.implementation("view_direct", "modify")
def modify_view_direct(data):
    """Modify elements using direct indexing"""
    lst = data['data']
    start, end = data['start'], data['end']
    
    # Modify directly
    for i in range(start, end):
        lst[i] = (lst[i] * 2) & 0xFFFFFFFF
    
    # Return checksum
    checksum = 0
    for i in range(start, end):
        checksum ^= lst[i]
    return checksum

# Index operation
@benchmark.implementation("slice", "index")
def index_slice(data):
    """Find index of element in a slice"""
    lst = data['data']
    start, end = data['start'], data['end']
    search_value = data['search_value']
    
    # Create slice and search
    slice_copy = lst[start:end]
    try:
        idx = slice_copy.index(search_value)
        return start + idx  # Return global index
    except ValueError:
        return -1

@benchmark.implementation("view", "index")
def index_view(data):
    """Find index of element in a view"""
    lst = data['data']
    start, end = data['start'], data['end']
    search_value = data['search_value']
    
    # Create view and search in it
    list_view = view(lst, start, end)
    try:
        idx = list_view.index(search_value)
        return start + idx  # Return global index
    except ValueError:
        return -1

@benchmark.implementation("view_direct", "index")
def index_view_direct(data):
    """Find index of element using direct search"""
    lst = data['data']
    start, end = data['start'], data['end']
    search_value = data['search_value']
    
    # Search directly
    for i in range(start, end):
        if lst[i] == search_value:
            return i
    return -1

# Reverse operation
@benchmark.implementation("slice", "reverse")
def reverse_slice(data):
    """Reverse a slice"""
    lst = data['data']
    start, end = data['start'], data['end']
    
    # Create slice, reverse, and copy back manually
    slice_copy = lst[start:end]
    slice_copy.reverse()
    for i, val in enumerate(slice_copy):
        lst[start + i] = val
    
    # Return checksum
    checksum = 0
    for i in range(start, min(start + 100, end)):  # First 100 elements
        checksum ^= lst[i]
    return checksum

@benchmark.implementation("view", "reverse")
def reverse_view(data):
    """Reverse through a view"""
    lst = data['data']
    start, end = data['start'], data['end']
    
    # Create view and reverse through it
    list_view = view(lst, start, end)
    list_view.reverse()
    
    # Return checksum
    checksum = 0
    for i in range(start, min(start + 100, end)):  # First 100 elements
        checksum ^= lst[i]
    return checksum

@benchmark.implementation("view_direct", "reverse")
def reverse_view_direct(data):
    """Reverse using direct manipulation"""
    lst = data['data']
    start, end = data['start'], data['end']
    
    # Reverse directly
    left, right = start, end - 1
    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1
    
    # Return checksum
    checksum = 0
    for i in range(start, min(start + 100, end)):  # First 100 elements
        checksum ^= lst[i]
    return checksum

# Sort operation
@benchmark.implementation("slice", "sort")
def sort_slice(data):
    """Sort a slice"""
    lst = data['data']
    start, end = data['start'], data['end']
    
    # Create slice, sort, and copy back manually
    slice_copy = lst[start:end]
    slice_copy.sort()
    for i, val in enumerate(slice_copy):
        lst[start + i] = val
    
    # Return checksum of first elements
    checksum = 0
    for i in range(start, min(start + 100, end)):
        checksum ^= lst[i]
    return checksum

@benchmark.implementation("view", "sort")
def sort_view(data):
    """Sort through a view"""
    lst = data['data']
    start, end = data['start'], data['end']
    
    # Create view and sort through it
    list_view = view(lst, start, end)
    list_view.sort()
    
    # Return checksum of first elements
    checksum = 0
    for i in range(start, min(start + 100, end)):
        checksum ^= lst[i]
    return checksum

# Nested sum operation (multiple slices)
@benchmark.implementation("slice", "nested_sum")
def nested_sum_slice(data):
    """Sum multiple overlapping slices"""
    lst = data['data']
    start, end = data['start'], data['end']
    slice_size = (end - start) // 4
    
    total = 0
    # Create 4 overlapping slices
    for offset in range(4):
        s = start + offset * slice_size // 2
        e = min(s + slice_size, end)
        slice_copy = lst[s:e]
        total += sum(slice_copy)
    
    return total & 0xFFFFFFFF

@benchmark.implementation("view", "nested_sum")
def nested_sum_view(data):
    """Sum multiple overlapping views"""
    lst = data['data']
    start, end = data['start'], data['end']
    slice_size = (end - start) // 4
    
    total = 0
    # Create 4 overlapping views
    for offset in range(4):
        s = start + offset * slice_size // 2
        e = min(s + slice_size, end)
        list_view = view(lst, s, e)
        for i in range(len(list_view)):
            total += list_view[i]
    
    return total & 0xFFFFFFFF

@benchmark.implementation("view_direct", "nested_sum")
def nested_sum_view_direct(data):
    """Sum multiple overlapping ranges directly"""
    lst = data['data']
    start, end = data['start'], data['end']
    slice_size = (end - start) // 4
    
    total = 0
    # Sum 4 overlapping ranges
    for offset in range(4):
        s = start + offset * slice_size // 2
        e = min(s + slice_size, end)
        for i in range(s, e):
            total += lst[i]
    
    return total & 0xFFFFFFFF

# Pop operation
@benchmark.implementation("slice", "pop")
def pop_slice(data):
    """Pop from end of slice"""
    lst = data['data']
    start, end = data['start'], data['end']
    
    # Create slice and pop from it
    slice_copy = lst[start:end]
    checksum = 0
    for _ in range(min(100, len(slice_copy))):  # Pop up to 100 elements
        if slice_copy:
            val = slice_copy.pop()
            checksum ^= val
    
    # Copy back to original (shortened)
    for i, val in enumerate(slice_copy):
        lst[start + i] = val
    
    return checksum

@benchmark.implementation("view", "pop")
def pop_view(data):
    """Pop from end of view"""
    lst = data['data']
    start, end = data['start'], data['end']
    
    # Create view and pop from it
    list_view = view(lst, start, end)
    checksum = 0
    for _ in range(min(100, len(list_view))):  # Pop up to 100 elements
        if len(list_view) > 0:
            val = list_view.pop()
            checksum ^= val
    
    return checksum

@benchmark.implementation("view_direct", "pop")
def pop_view_direct(data):
    """Pop using direct list manipulation"""
    lst = data['data']
    start, end = data['start'], data['end']
    
    checksum = 0
    current_end = end
    for _ in range(min(100, end - start)):  # Pop up to 100 elements
        if current_end > start:
            current_end -= 1
            val = lst[current_end]
            checksum ^= val
    
    return checksum

# Append operation
@benchmark.implementation("slice", "append")
def append_slice(data):
    """Append to slice"""
    lst = data['data']
    start, end = data['start'], data['end']
    
    # Create slice and append to it
    slice_copy = lst[start:end]
    checksum = 0
    for i in range(100):  # Append 100 elements
        val = (i * 17) & 0xFFFFFFFF
        slice_copy.append(val)
        checksum ^= val
    
    # Note: Can't copy back easily since slice grew, so just return checksum
    return checksum

@benchmark.implementation("view", "append")
def append_view(data):
    """Append to view"""
    lst = data['data']
    start, end = data['start'], data['end']
    
    # Create view and append to it
    list_view = view(lst, start, end)
    checksum = 0
    for i in range(min(100, len(lst) - end)):  # Append up to 100 elements or space available
        val = (i * 17) & 0xFFFFFFFF
        list_view.append(val)
        checksum ^= val
    
    return checksum

@benchmark.implementation("view_direct", "append")
def append_view_direct(data):
    """Append using direct list manipulation"""
    lst = data['data']
    start, end = data['start'], data['end']
    
    checksum = 0
    current_end = end
    for i in range(min(100, len(lst) - end)):  # Append up to 100 elements or space available
        val = (i * 17) & 0xFFFFFFFF
        if current_end < len(lst):
            lst[current_end] = val
            current_end += 1
            checksum ^= val
    
    return checksum

if __name__ == "__main__":
    # Parse command line args and run appropriate mode
    runner = benchmark.parse_args()
    runner.run()