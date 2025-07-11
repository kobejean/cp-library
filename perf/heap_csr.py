#!/usr/bin/env python3
"""
Benchmark comparing heap operations on CSR sparse rows vs list of lists/heaps.
Tests heapify, heappop, heapreplace, heappush, heappushpop operations.
"""

import random
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from cp_library.perf.benchmark import Benchmark, BenchmarkConfig
from cp_library.ds.view.csr_cls import CSR
from cp_library.ds.heap.fast_heapq import heapify, heappop, heapreplace, heappush, heappushpop

# Configure benchmark
config = BenchmarkConfig(
    name="heap_csr",
    sizes=[10000000, 1000000, 100000, 10000, 1000, 100, 10],  # Reverse order to warm up JIT
    operations=['initialization', 'initialization_bucketize', 'heapify', 'heappop', 'heapreplace', 'heappush', 'heappushpop'],
    iterations=10,
    warmup=3,
    output_dir="./output/benchmark_results/heap_csr"
)

# Create benchmark instance
benchmark = Benchmark(config)

# Data generator for initialization
@benchmark.data_generator("initialization")
def generate_initialization_data(size: int, operation: str):
    """Generate raw data for initialization benchmark"""
    # Generate multiple sparse rows (each row is a heap)
    num_rows = max(10, size // 100)  # 10-100 rows depending on size
    total_elements = size
    
    # Generate raw row data
    raw_rows = []
    elements_per_row = total_elements // num_rows
    remaining = total_elements % num_rows
    
    for i in range(num_rows):
        # Variable row sizes (some rows get extra elements)
        row_size = elements_per_row + (1 if i < remaining else 0)
        row_size = max(1, row_size)  # Ensure at least 1 element per row
        
        # Generate random heap data for this row
        row_data = [random.randint(1, 1000000) for _ in range(row_size)]
        raw_rows.append(row_data)
    
    return {
        'raw_rows': raw_rows,
        'num_rows': num_rows,
        'size': size,
        'operation': operation
    }

# Data generator for bucketize initialization
@benchmark.data_generator("initialization_bucketize")
def generate_bucketize_data(size: int, operation: str):
    """Generate (key, value) pairs for bucketize initialization benchmark"""
    # Generate multiple sparse rows (each row is a heap)
    num_rows = max(10, size // 100)  # 10-100 rows depending on size
    total_elements = size
    
    # Generate (key, value) pairs
    keys = []
    values = []
    
    elements_per_row = total_elements // num_rows
    remaining = total_elements % num_rows
    
    for i in range(num_rows):
        # Variable row sizes (some rows get extra elements)
        row_size = elements_per_row + (1 if i < remaining else 0)
        row_size = max(1, row_size)  # Ensure at least 1 element per row
        
        # Generate random heap data for this row
        for _ in range(row_size):
            keys.append(i)  # Row index as key
            values.append(random.randint(1, 1000000))  # Random value
    
    # Shuffle to simulate unsorted input
    combined = list(zip(keys, values))
    random.shuffle(combined)
    keys, values = zip(*combined)
    keys, values = list(keys), list(values)
    
    # Create equivalent raw rows for list_of_lists comparison
    raw_rows = [[] for _ in range(num_rows)]
    for key, value in zip(keys, values):
        raw_rows[key].append(value)
    
    return {
        'keys': keys,
        'values': values,
        'raw_rows': raw_rows,
        'num_rows': num_rows,
        'size': size,
        'operation': operation
    }

# Data generator for other operations
@benchmark.data_generator("default")
def generate_csr_heap_data(size: int, operation: str):
    """Generate test data for CSR heap operations"""
    # Generate multiple sparse rows (each row is a heap)
    num_rows = max(10, size // 100)  # 10-100 rows depending on size
    total_elements = size
    
    # Create sparse row data
    A = []  # All elements concatenated
    O = [0]  # Offsets for each row
    
    elements_per_row = total_elements // num_rows
    remaining = total_elements % num_rows
    
    for i in range(num_rows):
        # Variable row sizes (some rows get extra elements)
        row_size = elements_per_row + (1 if i < remaining else 0)
        row_size = max(1, row_size)  # Ensure at least 1 element per row
        
        # Generate random heap data for this row
        row_data = [random.randint(1, 1000000) for _ in range(row_size)]
        A.extend(row_data)
        O.append(len(A))
    
    # Create list of lists equivalent
    list_of_lists = []
    for i in range(num_rows):
        start, end = O[i], O[i + 1]
        list_of_lists.append(A[start:end].copy())
    
    return {
        'A': A,
        'O': O,
        'list_of_lists': list_of_lists,
        'num_rows': num_rows,
        'new_value': random.randint(1, 1000000),
        'target_row': random.randint(0, num_rows - 1),
        'size': size,
        'operation': operation
    }

# Setup functions for operations that modify data
@benchmark.setup("csr", ["heappop", "heapreplace", "heappush", "heappushpop"])
def setup_csr_heap(data):
    """Setup function that copies data and heapifies CSR rows"""
    new_data = data.copy()
    new_data['A'] = data['A'].copy()
    new_data['O'] = data['O'].copy()
    
    # Create CSR and pre-heapify all rows
    csr = CSR(new_data['A'], new_data['O'])
    for row_view in csr:
        heapify(row_view)
    
    new_data['csr'] = csr
    return new_data

@benchmark.setup("list_of_lists", ["heappop", "heapreplace", "heappush", "heappushpop"])
def setup_list_of_lists_heap(data):
    """Setup function that copies data and heapifies list of lists"""
    new_data = data.copy()
    # Deep copy list of lists
    new_data['list_of_lists'] = [row.copy() for row in data['list_of_lists']]
    
    # Pre-heapify all lists
    for row in new_data['list_of_lists']:
        heapify(row)
    
    return new_data

# For heapify operation, we need setup without pre-heapifying
@benchmark.setup("csr", ["heapify"])
def setup_csr_heapify(data):
    """Setup function that only copies data for heapify operation"""
    new_data = data.copy()
    new_data['A'] = data['A'].copy()
    new_data['O'] = data['O'].copy()
    new_data['csr'] = CSR(new_data['A'], new_data['O'])
    return new_data

@benchmark.setup("list_of_lists", ["heapify"])
def setup_list_of_lists_heapify(data):
    """Setup function that only copies data for heapify operation"""
    new_data = data.copy()
    new_data['list_of_lists'] = [row.copy() for row in data['list_of_lists']]
    return new_data

# Initialization operation
@benchmark.implementation("csr", "initialization")
def initialization_csr(data):
    """Initialize CSR from raw row data"""
    raw_rows = data['raw_rows']
    
    # Create CSR structure
    A = []  # All elements concatenated
    O = [0]  # Offsets for each row
    
    for row_data in raw_rows:
        A.extend(row_data)
        O.append(len(A))
    
    # Create CSR object
    csr = CSR(A, O)
    
    # Return checksum to ensure it's not optimized away
    checksum = 0
    for i in range(min(10, len(csr))):  # First 10 rows
        row_view = csr[i]
        for j in range(min(3, len(row_view))):  # First 3 elements per row
            checksum ^= row_view[j]
    
    return checksum

@benchmark.implementation("list_of_lists", "initialization")
def initialization_list_of_lists(data):
    """Initialize list of lists from raw row data"""
    raw_rows = data['raw_rows']
    
    # Create list of lists (deep copy)
    list_of_lists = [row.copy() for row in raw_rows]
    
    # Return checksum to ensure it's not optimized away
    checksum = 0
    for i in range(min(10, len(list_of_lists))):  # First 10 rows
        row = list_of_lists[i]
        for j in range(min(3, len(row))):  # First 3 elements per row
            checksum ^= row[j]
    
    return checksum

# Bucketize initialization operation
@benchmark.implementation("csr", "initialization_bucketize")
def initialization_bucketize_csr(data):
    """Initialize CSR using bucketize from (key, value) pairs"""
    keys = data['keys']
    values = data['values']
    num_rows = data['num_rows']
    
    # Create CSR using bucketize
    csr = CSR.bucketize(num_rows, keys, values)
    
    # Return checksum to ensure it's not optimized away
    checksum = 0
    for i in range(min(10, len(csr))):  # First 10 rows
        row_view = csr[i]
        for j in range(min(3, len(row_view))):  # First 3 elements per row
            checksum ^= row_view[j]
    
    return checksum

@benchmark.implementation("list_of_lists", "initialization_bucketize")
def initialization_bucketize_list_of_lists(data):
    """Initialize list of lists by grouping (key, value) pairs manually"""
    keys = data['keys']
    values = data['values']
    num_rows = data['num_rows']
    
    # Group by key manually (simulating what bucketize does)
    list_of_lists = [[] for _ in range(num_rows)]
    for e, k in enumerate(keys):
        list_of_lists[k].append(values[e])
    
    # Return checksum to ensure it's not optimized away
    checksum = 0
    for i in range(min(10, len(list_of_lists))):  # First 10 rows
        row = list_of_lists[i]
        for j in range(min(3, len(row))):  # First 3 elements per row
            checksum ^= row[j]
    
    return checksum

# Heapify operation
@benchmark.implementation("csr", "heapify")
def heapify_csr(data):
    """Heapify all CSR rows"""
    csr = data['csr']
    
    checksum = 0
    for row_view in csr:
        heapify(row_view)
        # Add first few elements to checksum
        for j in range(min(3, len(row_view))):
            checksum ^= row_view[j]
    
    return checksum

@benchmark.implementation("list_of_lists", "heapify")
def heapify_list_of_lists(data):
    """Heapify all lists in list of lists"""
    list_of_lists = data['list_of_lists']
    
    checksum = 0
    for row in list_of_lists:
        heapify(row)
        # Add first few elements to checksum
        for j in range(min(3, len(row))):
            checksum ^= row[j]
    
    return checksum

# Heappop operation (heaps are already heapified in setup)
@benchmark.implementation("csr", "heappop")
def heappop_csr(data):
    """Pop from CSR heaps"""
    csr = data['csr']
    
    checksum = 0
    # Pop from multiple rows
    for row_view in csr:
        pop_count = min(3, len(row_view))  # Pop up to 3 elements per row
        for _ in range(pop_count):
            if row_view:
                val = heappop(row_view)
                checksum ^= val
    
    return checksum

@benchmark.implementation("list_of_lists", "heappop")
def heappop_list_of_lists(data):
    """Pop from list of lists heaps"""
    list_of_lists = data['list_of_lists']
    
    checksum = 0
    # Pop from multiple rows
    for row in list_of_lists:
        pop_count = min(3, len(row))  # Pop up to 3 elements per row
        for _ in range(pop_count):
            if row:
                val = heappop(row)
                checksum ^= val
    
    return checksum

# Heapreplace operation (heaps are already heapified in setup)
@benchmark.implementation("csr", "heapreplace")
def heapreplace_csr(data):
    """Replace in CSR heaps"""
    csr = data['csr']
    new_value = data['new_value']
    
    checksum = 0
    # Replace in multiple rows
    for row_view in csr:
        if row_view:
            replace_count = min(2, len(row_view))  # Replace up to 2 elements per row
            for j in range(replace_count):
                if row_view:
                    val = heapreplace(row_view, new_value + j)
                    checksum ^= val
    
    return checksum

@benchmark.implementation("list_of_lists", "heapreplace")
def heapreplace_list_of_lists(data):
    """Replace in list of lists heaps"""
    list_of_lists = data['list_of_lists']
    new_value = data['new_value']
    
    checksum = 0
    # Replace in multiple rows
    for row in list_of_lists:
        if row:
            replace_count = min(2, len(row))  # Replace up to 2 elements per row
            for j in range(replace_count):
                if row:
                    val = heapreplace(row, new_value + j)
                    checksum ^= val
    
    return checksum

# Heappush operation (heaps are already heapified in setup)
@benchmark.implementation("csr", "heappush")
def heappush_csr(data):
    """Push to CSR heaps"""
    csr = data['csr']
    new_value = data['new_value']
    
    checksum = 0
    # Push to multiple rows
    for i in range(min(5, len(csr))):  # Push to first 5 rows
        row_view = csr[i]
        # Check if there's space to expand (view can grow within A bounds)
        if row_view.r < len(csr.A):
            push_count = min(2, len(csr.A) - row_view.r)  # Push up to 2 elements per row
            for j in range(push_count):
                val = new_value + i * 10 + j
                heappush(row_view, val)
                checksum ^= val
    
    return checksum

@benchmark.implementation("list_of_lists", "heappush")
def heappush_list_of_lists(data):
    """Push to list of lists heaps"""
    list_of_lists = data['list_of_lists']
    new_value = data['new_value']
    
    checksum = 0
    # Push to multiple rows
    for i in range(min(5, len(list_of_lists))):  # Push to first 5 rows
        row = list_of_lists[i]
        push_count = 2  # Push 2 elements per row
        for j in range(push_count):
            val = new_value + i * 10 + j
            heappush(row, val)
            checksum ^= val
    
    return checksum

# Heappushpop operation (heaps are already heapified in setup)
@benchmark.implementation("csr", "heappushpop")
def heappushpop_csr(data):
    """Push and pop from CSR heaps"""
    csr = data['csr']
    new_value = data['new_value']
    
    checksum = 0
    # Pushpop from multiple rows
    for i, row_view in enumerate(csr):
        if row_view:
            pushpop_count = min(2, len(row_view))  # Pushpop up to 2 elements per row
            for j in range(pushpop_count):
                val = new_value + i * 10 + j
                popped = heappushpop(row_view, val)
                checksum ^= popped
    
    return checksum

@benchmark.implementation("list_of_lists", "heappushpop")
def heappushpop_list_of_lists(data):
    """Push and pop from list of lists heaps"""
    list_of_lists = data['list_of_lists']
    new_value = data['new_value']
    
    checksum = 0
    # Pushpop from multiple rows
    for i, row in enumerate(list_of_lists):
        if row:
            pushpop_count = min(2, len(row))  # Pushpop up to 2 elements per row
            for j in range(pushpop_count):
                val = new_value + i * 10 + j
                popped = heappushpop(row, val)
                checksum ^= popped
    
    return checksum

if __name__ == "__main__":
    # Parse command line args and run appropriate mode
    runner = benchmark.parse_args()
    runner.run()