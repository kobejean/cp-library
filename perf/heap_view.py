#!/usr/bin/env python3
"""
Benchmark comparing heap operations on list slices vs view objects vs direct indexing.
Tests heapify, heappop, heapreplace, heappush, heappushpop operations.
"""

import random
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from cp_library.perf.benchmark import Benchmark, BenchmarkConfig
from cp_library.ds.view.view_cls import view
from cp_library.ds.heap.fast_heapq import heapify, heappop, heapreplace, heappush, heappushpop
import heapq  # Standard library for comparison

# Configure benchmark
config = BenchmarkConfig(
    name="heap_view",
    sizes=[100000, 10000, 1000, 100, 50],  # Reverse order to warm up JIT
    operations=['heapify', 'heappop', 'heapreplace', 'heappush', 'heappushpop'],
    iterations=10,
    warmup=3,
    output_dir="./output/benchmark_results/heap_view"
)

# Create benchmark instance
benchmark = Benchmark(config)

# Data generator
@benchmark.data_generator("default")
def generate_heap_data(size: int, operation: str):
    """Generate test data for heap operations"""
    # Generate random list for heap operations
    data = [random.randint(1, 1000000) for _ in range(size)]
    
    # Generate random slice boundaries (30-70% of list for reasonable heap size)
    slice_size = random.randint(size // 3, min(size * 2 // 3, size - 1))
    start = random.randint(0, size - slice_size)
    end = start + slice_size
    
    return {
        'data': data,
        'start': start,
        'end': end,
        'slice_size': slice_size,
        'new_value': random.randint(1, 1000000),
        'replace_value': random.randint(1, 1000000),
        'size': size,
        'operation': operation
    }

# Setup functions for operations that modify data
@benchmark.setup("slice", ["heappop", "heapreplace", "heappush", "heappushpop"])
def setup_slice_heap(data):
    """Setup function that copies data and heapifies before heap operations"""
    new_data = data.copy()
    new_data['data'] = data['data'].copy()
    
    # Pre-heapify the slice for operations that need it
    lst = new_data['data']
    start, end = new_data['start'], new_data['end']
    slice_copy = lst[start:end]
    heapify(slice_copy)
    for i, val in enumerate(slice_copy):
        lst[start + i] = val
    
    return new_data

@benchmark.setup("view", ["heappop", "heapreplace", "heappush", "heappushpop"])
def setup_view_heap(data):
    """Setup function that copies data and heapifies before heap operations"""
    new_data = data.copy()
    new_data['data'] = data['data'].copy()
    
    # Pre-heapify the view for operations that need it
    lst = new_data['data']
    start, end = new_data['start'], new_data['end']
    heap_view = view(lst, start, end)
    heapify(heap_view)
    
    return new_data

@benchmark.setup("direct", ["heappop", "heapreplace", "heappush", "heappushpop"])
def setup_direct_heap(data):
    """Setup function that copies data and heapifies before heap operations"""
    new_data = data.copy()
    new_data['data'] = data['data'].copy()
    
    # Pre-heapify the range for operations that need it
    lst = new_data['data']
    start, end = new_data['start'], new_data['end']
    temp_list = lst[start:end]
    heapify(temp_list)
    for i, val in enumerate(temp_list):
        lst[start + i] = val
    
    return new_data

@benchmark.setup("stdlib", ["heappop", "heapreplace", "heappush", "heappushpop"])
def setup_stdlib_heap(data):
    """Setup function that copies data and heapifies before heap operations"""
    new_data = data.copy()
    new_data['data'] = data['data'].copy()
    
    # Pre-heapify the slice for operations that need it
    lst = new_data['data']
    start, end = new_data['start'], new_data['end']
    slice_copy = lst[start:end]
    heapq.heapify(slice_copy)
    for i, val in enumerate(slice_copy):
        lst[start + i] = val
    
    return new_data

# For heapify operation, we need setup without pre-heapifying
@benchmark.setup("slice", ["heapify"])
def setup_slice_heapify(data):
    """Setup function that only copies data for heapify operation"""
    new_data = data.copy()
    new_data['data'] = data['data'].copy()
    return new_data

@benchmark.setup("view", ["heapify"])
def setup_view_heapify(data):
    """Setup function that only copies data for heapify operation"""
    new_data = data.copy()
    new_data['data'] = data['data'].copy()
    return new_data

@benchmark.setup("direct", ["heapify"])
def setup_direct_heapify(data):
    """Setup function that only copies data for heapify operation"""
    new_data = data.copy()
    new_data['data'] = data['data'].copy()
    return new_data

@benchmark.setup("stdlib", ["heapify"])
def setup_stdlib_heapify(data):
    """Setup function that only copies data for heapify operation"""
    new_data = data.copy()
    new_data['data'] = data['data'].copy()
    return new_data

# Heapify operation
@benchmark.implementation("slice", "heapify")
def heapify_slice(data):
    """Heapify a slice"""
    lst = data['data']
    start, end = data['start'], data['end']
    
    # Create slice and heapify
    slice_copy = lst[start:end]
    heapify(slice_copy)
    
    # Copy back manually
    for i, val in enumerate(slice_copy):
        lst[start + i] = val
    
    # Return checksum
    checksum = 0
    for i in range(start, min(start + 10, end)):  # First 10 elements
        checksum ^= lst[i]
    return checksum

@benchmark.implementation("view", "heapify")
def heapify_view(data):
    """Heapify through a view"""
    lst = data['data']
    start, end = data['start'], data['end']
    
    # Create view and heapify
    heap_view = view(lst, start, end)
    heapify(heap_view)
    
    # Return checksum
    checksum = 0
    for i in range(start, min(start + 10, end)):  # First 10 elements
        checksum ^= lst[i]
    return checksum

@benchmark.implementation("direct", "heapify")
def heapify_direct(data):
    """Heapify using direct list access"""
    lst = data['data']
    start, end = data['start'], data['end']
    
    # Heapify the range directly in the list
    temp_list = lst[start:end]
    heapify(temp_list)
    for i, val in enumerate(temp_list):
        lst[start + i] = val
    
    # Return checksum
    checksum = 0
    for i in range(start, min(start + 10, end)):  # First 10 elements
        checksum ^= lst[i]
    return checksum

@benchmark.implementation("stdlib", "heapify")
def heapify_stdlib(data):
    """Heapify using standard library"""
    lst = data['data']
    start, end = data['start'], data['end']
    
    # Create slice and heapify with stdlib
    slice_copy = lst[start:end]
    heapq.heapify(slice_copy)
    
    # Copy back manually
    for i, val in enumerate(slice_copy):
        lst[start + i] = val
    
    # Return checksum
    checksum = 0
    for i in range(start, min(start + 10, end)):  # First 10 elements
        checksum ^= lst[i]
    return checksum

# Heappop operation (heap is already heapified in setup)
@benchmark.implementation("slice", "heappop")
def heappop_slice(data):
    """Pop from heap slice"""
    lst = data['data']
    start, end = data['start'], data['end']
    
    # Create slice and pop (already heapified)
    slice_copy = lst[start:end]
    
    checksum = 0
    for _ in range(min(10, len(slice_copy))):  # Pop up to 10 elements
        if slice_copy:
            val = heappop(slice_copy)
            checksum ^= val
    
    # Copy back
    for i, val in enumerate(slice_copy):
        lst[start + i] = val
    
    return checksum

@benchmark.implementation("view", "heappop")
def heappop_view(data):
    """Pop from heap view"""
    lst = data['data']
    start, end = data['start'], data['end']
    
    # Create view and pop (already heapified)
    heap_view = view(lst, start, end)
    
    checksum = 0
    for _ in range(min(10, len(heap_view))):  # Pop up to 10 elements
        if len(heap_view) > 0:
            val = heappop(heap_view)
            checksum ^= val
    
    return checksum

@benchmark.implementation("direct", "heappop")
def heappop_direct(data):
    """Pop from heap using direct access"""
    lst = data['data']
    start, end = data['start'], data['end']
    
    # Pop from range (already heapified)
    temp_list = lst[start:end]
    
    checksum = 0
    for _ in range(min(10, len(temp_list))):  # Pop up to 10 elements
        if temp_list:
            val = heappop(temp_list)
            checksum ^= val
    
    # Copy back
    for i, val in enumerate(temp_list):
        lst[start + i] = val
    
    return checksum

@benchmark.implementation("stdlib", "heappop")
def heappop_stdlib(data):
    """Pop from heap using standard library"""
    lst = data['data']
    start, end = data['start'], data['end']
    
    # Create slice and pop with stdlib (already heapified)
    slice_copy = lst[start:end]
    
    checksum = 0
    for _ in range(min(10, len(slice_copy))):  # Pop up to 10 elements
        if slice_copy:
            val = heapq.heappop(slice_copy)
            checksum ^= val
    
    # Copy back
    for i, val in enumerate(slice_copy):
        lst[start + i] = val
    
    return checksum

# Heapreplace operation (heap is already heapified in setup)
@benchmark.implementation("slice", "heapreplace")
def heapreplace_slice(data):
    """Replace in heap slice"""
    lst = data['data']
    start, end = data['start'], data['end']
    new_value = data['new_value']
    
    # Create slice and replace (already heapified)
    slice_copy = lst[start:end]
    if slice_copy:
        checksum = 0
        for _ in range(min(5, len(slice_copy))):  # Replace up to 5 elements
            if slice_copy:
                val = heapreplace(slice_copy, new_value)
                checksum ^= val
                new_value = (new_value + 1) & 0xFFFFFFFF
        
        # Copy back
        for i, val in enumerate(slice_copy):
            lst[start + i] = val
        
        return checksum
    return 0

@benchmark.implementation("view", "heapreplace")
def heapreplace_view(data):
    """Replace in heap view"""
    lst = data['data']
    start, end = data['start'], data['end']
    new_value = data['new_value']
    
    # Create view and replace (already heapified)
    heap_view = view(lst, start, end)
    if len(heap_view) > 0:
        checksum = 0
        for _ in range(min(5, len(heap_view))):  # Replace up to 5 elements
            if len(heap_view) > 0:
                val = heapreplace(heap_view, new_value)
                checksum ^= val
                new_value = (new_value + 1) & 0xFFFFFFFF
        
        return checksum
    return 0

@benchmark.implementation("direct", "heapreplace")
def heapreplace_direct(data):
    """Replace in heap using direct access"""
    lst = data['data']
    start, end = data['start'], data['end']
    new_value = data['new_value']
    
    # Replace from range (already heapified)
    temp_list = lst[start:end]
    if temp_list:
        checksum = 0
        for _ in range(min(5, len(temp_list))):  # Replace up to 5 elements
            if temp_list:
                val = heapreplace(temp_list, new_value)
                checksum ^= val
                new_value = (new_value + 1) & 0xFFFFFFFF
        
        # Copy back
        for i, val in enumerate(temp_list):
            lst[start + i] = val
        
        return checksum
    return 0

@benchmark.implementation("stdlib", "heapreplace")
def heapreplace_stdlib(data):
    """Replace in heap using standard library"""
    lst = data['data']
    start, end = data['start'], data['end']
    new_value = data['new_value']
    
    # Create slice and replace with stdlib (already heapified)
    slice_copy = lst[start:end]
    if slice_copy:
        checksum = 0
        for _ in range(min(5, len(slice_copy))):  # Replace up to 5 elements
            if slice_copy:
                val = heapq.heapreplace(slice_copy, new_value)
                checksum ^= val
                new_value = (new_value + 1) & 0xFFFFFFFF
        
        # Copy back
        for i, val in enumerate(slice_copy):
            lst[start + i] = val
        
        return checksum
    return 0

# Heappush operation (heap is already heapified in setup)
@benchmark.implementation("slice", "heappush")
def heappush_slice(data):
    """Push to heap slice"""
    lst = data['data']
    start, end = data['start'], data['end']
    new_value = data['new_value']
    
    # Create slice and push (already heapified)
    slice_copy = lst[start:end]
    
    checksum = 0
    for i in range(5):  # Push 5 elements
        val = (new_value + i) & 0xFFFFFFFF
        heappush(slice_copy, val)
        checksum ^= val
    
    # Note: Can't copy back easily since slice grew, just return checksum
    return checksum

@benchmark.implementation("view", "heappush")
def heappush_view(data):
    """Push to heap view"""
    lst = data['data']
    start, end = data['start'], data['end']
    new_value = data['new_value']
    
    # Create view and push (already heapified)
    heap_view = view(lst, start, end)
    
    checksum = 0
    max_push = min(5, len(lst) - end)  # Limited by available space
    for i in range(max_push):
        val = (new_value + i) & 0xFFFFFFFF
        heappush(heap_view, val)
        checksum ^= val
    
    return checksum

@benchmark.implementation("direct", "heappush")
def heappush_direct(data):
    """Push to heap using direct access"""
    lst = data['data']
    start, end = data['start'], data['end']
    new_value = data['new_value']
    
    # Push to range (already heapified)
    temp_list = lst[start:end]
    
    checksum = 0
    for i in range(5):  # Push 5 elements
        val = (new_value + i) & 0xFFFFFFFF
        heappush(temp_list, val)
        checksum ^= val
    
    # Note: Can't copy back easily since temp_list grew, just return checksum
    return checksum

@benchmark.implementation("stdlib", "heappush")
def heappush_stdlib(data):
    """Push to heap using standard library"""
    lst = data['data']
    start, end = data['start'], data['end']
    new_value = data['new_value']
    
    # Create slice and push with stdlib (already heapified)
    slice_copy = lst[start:end]
    
    checksum = 0
    for i in range(5):  # Push 5 elements
        val = (new_value + i) & 0xFFFFFFFF
        heapq.heappush(slice_copy, val)
        checksum ^= val
    
    # Note: Can't copy back easily since slice grew, just return checksum
    return checksum

# Heappushpop operation (heap is already heapified in setup)
@benchmark.implementation("slice", "heappushpop")
def heappushpop_slice(data):
    """Push and pop from heap slice"""
    lst = data['data']
    start, end = data['start'], data['end']
    new_value = data['new_value']
    
    # Create slice and pushpop (already heapified)
    slice_copy = lst[start:end]
    if slice_copy:
        checksum = 0
        for i in range(min(5, len(slice_copy))):  # Pushpop up to 5 elements
            val = (new_value + i) & 0xFFFFFFFF
            popped = heappushpop(slice_copy, val)
            checksum ^= popped
        
        # Copy back
        for i, val in enumerate(slice_copy):
            lst[start + i] = val
        
        return checksum
    return 0

@benchmark.implementation("view", "heappushpop")
def heappushpop_view(data):
    """Push and pop from heap view"""
    lst = data['data']
    start, end = data['start'], data['end']
    new_value = data['new_value']
    
    # Create view and pushpop (already heapified)
    heap_view = view(lst, start, end)
    if len(heap_view) > 0:
        checksum = 0
        for i in range(min(5, len(heap_view))):  # Pushpop up to 5 elements
            val = (new_value + i) & 0xFFFFFFFF
            popped = heappushpop(heap_view, val)
            checksum ^= popped
        
        return checksum
    return 0

@benchmark.implementation("direct", "heappushpop")
def heappushpop_direct(data):
    """Push and pop from heap using direct access"""
    lst = data['data']
    start, end = data['start'], data['end']
    new_value = data['new_value']
    
    # Pushpop from range (already heapified)
    temp_list = lst[start:end]
    if temp_list:
        checksum = 0
        for i in range(min(5, len(temp_list))):  # Pushpop up to 5 elements
            val = (new_value + i) & 0xFFFFFFFF
            popped = heappushpop(temp_list, val)
            checksum ^= popped
        
        # Copy back
        for i, val in enumerate(temp_list):
            lst[start + i] = val
        
        return checksum
    return 0

@benchmark.implementation("stdlib", "heappushpop")
def heappushpop_stdlib(data):
    """Push and pop from heap using standard library"""
    lst = data['data']
    start, end = data['start'], data['end']
    new_value = data['new_value']
    
    # Create slice and pushpop with stdlib (already heapified)
    slice_copy = lst[start:end]
    if slice_copy:
        checksum = 0
        for i in range(min(5, len(slice_copy))):  # Pushpop up to 5 elements
            val = (new_value + i) & 0xFFFFFFFF
            popped = heapq.heappushpop(slice_copy, val)
            checksum ^= popped
        
        # Copy back
        for i, val in enumerate(slice_copy):
            lst[start + i] = val
        
        return checksum
    return 0

if __name__ == "__main__":
    # Parse command line args and run appropriate mode
    runner = benchmark.parse_args()
    runner.run()