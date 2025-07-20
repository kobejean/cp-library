#!/usr/bin/env python3
"""
Benchmark comparing Que vs Deque vs collections.deque.
Tests append/appendleft, pop/popleft, and construction operations.
"""

import random
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from cp_library.perf.benchmark import Benchmark, BenchmarkConfig
from cp_library.ds.que.deque_cls import Deque
from collections import deque as builtin_deque

# Configure benchmark
config = BenchmarkConfig(
    name="deque",
    sizes=[10000000, 1000000, 100000, 10000, 1000, 100],  # Reverse order to warm up JIT
    operations=['construction', 'access', 'iteration', 'modification', 'append_ops', 'append_left_ops', 'pop_ops', 'pop_left_ops', 'mixed_ops'],
    iterations=10,
    warmup=3,
    output_dir="./output/benchmark_results/deque"
)

# Create benchmark instance
benchmark = Benchmark(config)

# Data generator
@benchmark.data_generator("default")
def generate_deque_data(size: int, operation: str):
    """Generate test data for deque operations"""
    # Generate initial data
    initial_data = [random.randint(1, 1_000_000_000) for _ in range(size)]
    
    # Generate operation data
    num_ops = size
    append_values = [random.randint(1, 1_000_000_000) for _ in range(num_ops)]
    
    return {
        'initial_data': initial_data,
        'append_values': append_values,
        'size': size,
        'num_ops': num_ops
    }

# Setup functions
@benchmark.setup("default")
def setup(data):
    prepared = data.copy()
    return prepared

# Construction operation
@benchmark.implementation("deque", "construction")
def construction_deque(data):
    """Construct Deque"""
    # Use maxlen to avoid capacity issues with unlimited deque
    deque = Deque(data['initial_data'], maxlen=len(data['initial_data']) * 2)
    return len(deque)

@benchmark.implementation("builtin_deque", "construction")
def construction_builtin_deque(data):
    """Construct builtin deque"""
    deque = builtin_deque(data['initial_data'])
    return len(deque)

# Access operations
@benchmark.implementation("deque", "access")
def access_deque(data):
    """Random access on Deque using __getitem__"""
    deque = Deque(data['initial_data'], maxlen=len(data['initial_data']) * 2)
    checksum = 0
    for i in range(len(deque)):
        val = deque[i]
        checksum ^= val
    return checksum

@benchmark.implementation("builtin_deque", "access")
def access_builtin_deque(data):
    """Random access on builtin deque using __getitem__ (O(n) operation)"""
    # Skip for large sizes due to O(n) complexity
    if data['size'] > 10000:
        return None
    
    deque = builtin_deque(data['initial_data'])
    checksum = 0
    for i in range(len(deque)):
        val = deque[i]
        checksum ^= val
    return checksum

# Iteration operations
@benchmark.implementation("deque", "iteration")
def iteration_deque(data):
    """Iterate through Deque using for-in"""
    deque = Deque(data['initial_data'], maxlen=len(data['initial_data']) * 2)
    checksum = 0
    for val in deque:
        checksum ^= val
    return checksum

@benchmark.implementation("builtin_deque", "iteration")
def iteration_builtin_deque(data):
    """Iterate through builtin deque using for-in"""
    deque = builtin_deque(data['initial_data'])
    checksum = 0
    for val in deque:
        checksum ^= val
    return checksum

# Modification operations
@benchmark.implementation("deque", "modification")
def modification_deque(data):
    """Modify Deque elements using __setitem__"""
    deque = Deque(data['initial_data'], maxlen=len(data['initial_data']) * 2)
    checksum = 0
    for i in range(len(deque)):
        old_val = deque[i]
        new_val = (old_val * 2) & 0xFFFFFFFF
        deque[i] = new_val
        checksum ^= new_val
    return checksum

@benchmark.implementation("builtin_deque", "modification")
def modification_builtin_deque(data):
    """Modify builtin deque elements using __setitem__ (O(n) operation)"""
    # Skip for large sizes due to O(n) complexity
    if data['size'] > 10000:
        return None
    
    deque = builtin_deque(data['initial_data'])
    checksum = 0
    for i in range(len(deque)):
        old_val = deque[i]
        new_val = (old_val * 2) & 0xFFFFFFFF
        deque[i] = new_val
        checksum ^= new_val
    return checksum

# Append operations (right side)
@benchmark.implementation("deque", "append_ops")
def append_ops_deque(data):
    """Append operations on Deque"""
    deque = Deque()
    checksum = 0
    for val in data['append_values']:
        deque.append(val)
        checksum ^= len(deque)
    return checksum

@benchmark.implementation("builtin_deque", "append_ops")
def append_ops_builtin_deque(data):
    """Append operations on builtin deque"""
    deque = builtin_deque()
    checksum = 0
    for val in data['append_values']:
        deque.append(val)
        checksum ^= len(deque)
    return checksum

# Append left operations (only Deque and builtin_deque support this)
@benchmark.implementation("deque", "append_left_ops")
def append_left_ops_deque(data):
    """Append left operations on Deque"""
    deque = Deque()
    checksum = 0
    for val in data['append_values']:
        deque.appendleft(val)
        checksum ^= len(deque)
    return checksum

@benchmark.implementation("builtin_deque", "append_left_ops")
def append_left_ops_builtin_deque(data):
    """Append left operations on builtin deque"""
    deque = builtin_deque()
    checksum = 0
    for val in data['append_values']:
        deque.appendleft(val)
        checksum ^= len(deque)
    return checksum

# Pop operations (right side)

@benchmark.implementation("deque", "pop_ops")
def pop_ops_deque(data):
    """Pop operations on Deque (right side)"""
    deque = Deque(data['initial_data'], maxlen=len(data['initial_data']) * 2)
    checksum = 0
    for _ in range(min(len(deque), len(data['append_values']))):
        if len(deque) > 0:
            val = deque.pop()
            checksum ^= val
    return checksum

@benchmark.implementation("builtin_deque", "pop_ops")
def pop_ops_builtin_deque(data):
    """Pop operations on builtin deque (right side)"""
    deque = builtin_deque(data['initial_data'])
    checksum = 0
    for _ in range(min(len(deque), len(data['append_values']))):
        if len(deque) > 0:
            val = deque.pop()
            checksum ^= val
    return checksum

# Pop left operations (only Deque and builtin_deque support this)
@benchmark.implementation("deque", "pop_left_ops")
def pop_left_ops_deque(data):
    """Pop left operations on Deque"""
    deque = Deque(data['initial_data'], maxlen=len(data['initial_data']) * 2)
    checksum = 0
    for _ in range(min(len(deque), len(data['append_values']))):
        if len(deque) > 0:
            val = deque.popleft()
            checksum ^= val
    return checksum

@benchmark.implementation("builtin_deque", "pop_left_ops")
def pop_left_ops_builtin_deque(data):
    """Pop left operations on builtin deque"""
    deque = builtin_deque(data['initial_data'])
    checksum = 0
    for _ in range(min(len(deque), len(data['append_values']))):
        if len(deque) > 0:
            val = deque.popleft()
            checksum ^= val
    return checksum

# Mixed operations
@benchmark.implementation("deque", "mixed_ops")
def mixed_ops_deque(data):
    """Mixed operations on Deque"""
    deque = Deque()
    checksum = 0
    
    for i, val in enumerate(data['append_values']):
        if i % 4 == 0:
            # Append right
            deque.append(val)
            checksum ^= len(deque)
        elif i % 4 == 1:
            # Append left
            deque.appendleft(val)
            checksum ^= len(deque)
        elif i % 4 == 2 and len(deque) > 0:
            # Pop right
            popped = deque.pop()
            checksum ^= popped
        elif i % 4 == 3 and len(deque) > 0:
            # Pop left
            popped = deque.popleft()
            checksum ^= popped
    
    return checksum

@benchmark.implementation("builtin_deque", "mixed_ops")
def mixed_ops_builtin_deque(data):
    """Mixed operations on builtin deque"""
    deque = builtin_deque()
    checksum = 0
    
    for i, val in enumerate(data['append_values']):
        if i % 4 == 0:
            # Append right
            deque.append(val)
            checksum ^= len(deque)
        elif i % 4 == 1:
            # Append left
            deque.appendleft(val)
            checksum ^= len(deque)
        elif i % 4 == 2 and len(deque) > 0:
            # Pop right
            popped = deque.pop()
            checksum ^= popped
        elif i % 4 == 3 and len(deque) > 0:
            # Pop left
            popped = deque.popleft()
            checksum ^= popped
    
    return checksum

if __name__ == "__main__":
    # Parse command line args and run appropriate mode
    runner = benchmark.parse_args()
    runner.run()