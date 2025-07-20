#!/usr/bin/env python3
"""
Benchmark comparing Que vs FIFO queue alternatives.
Tests FIFO queue operations: push/append, pop/popleft, construction.
"""

import random
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from cp_library.perf.benchmark import Benchmark, BenchmarkConfig
from cp_library.ds.que.que_cls import Que
from cp_library.ds.que.deque_cls import Deque
from collections import deque as builtin_deque
import queue

# Configure benchmark
config = BenchmarkConfig(
    name="que",
    sizes=[1000000, 100000, 10000, 1000, 100],  # Reverse order to warm up JIT
    operations=['construction', 'access', 'iteration', 'modification', 'fifo_push_pop', 'bulk_operations', 'mixed_fifo'],
    iterations=10,
    warmup=3,
    output_dir="./output/benchmark_results/que"
)

# Create benchmark instance
benchmark = Benchmark(config)

# Data generator
@benchmark.data_generator("default")
def generate_que_data(size: int, operation: str):
    """Generate test data for FIFO queue operations"""
    # Generate initial data
    initial_data = [random.randint(1, 1000) for _ in range(size)]
    
    # Generate operation data
    num_ops = size
    push_values = [random.randint(1, 1000) for _ in range(num_ops)]
    
    return {
        'initial_data': initial_data,
        'push_values': push_values,
        'size': size,
        'num_ops': num_ops
    }

# Setup functions
@benchmark.setup("default")
def setup(data):
    prepared = data.copy()
    return prepared

# Construction operation
@benchmark.implementation("que", "construction")
def construction_que(data):
    """Construct Que"""
    que = Que(data['initial_data'])
    return len(que)

@benchmark.implementation("deque_fifo", "construction")
def construction_deque_fifo(data):
    """Construct Deque for FIFO usage"""
    deque = Deque(data['initial_data'], maxlen=len(data['initial_data']) * 2)
    return len(deque)

@benchmark.implementation("builtin_deque_fifo", "construction")
def construction_builtin_deque_fifo(data):
    """Construct builtin deque for FIFO usage"""
    deque = builtin_deque(data['initial_data'], maxlen=len(data['initial_data']) * 2)
    return len(deque)

# Access operations
@benchmark.implementation("que", "access")
def access_que(data):
    """Random access on Que using __getitem__"""
    que = Que(data['initial_data'])
    checksum = 0
    for i in range(len(que)):
        val = que[i]
        checksum ^= val
    return checksum

@benchmark.implementation("deque_fifo", "access")
def access_deque_fifo(data):
    """Random access on Deque using __getitem__"""
    deque = Deque(data['initial_data'], maxlen=len(data['initial_data']) * 2)
    checksum = 0
    for i in range(len(deque)):
        val = deque[i]
        checksum ^= val
    return checksum

@benchmark.implementation("builtin_deque_fifo", "access")
def access_builtin_deque_fifo(data):
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
@benchmark.implementation("que", "iteration")
def iteration_que(data):
    """Iterate through Que using for-in"""
    que = Que(data['initial_data'])
    checksum = 0
    for val in que:
        checksum ^= val
    return checksum

@benchmark.implementation("deque_fifo", "iteration")
def iteration_deque_fifo(data):
    """Iterate through Deque using for-in"""
    deque = Deque(data['initial_data'], maxlen=len(data['initial_data']) * 2)
    checksum = 0
    for val in deque:
        checksum ^= val
    return checksum

@benchmark.implementation("builtin_deque_fifo", "iteration")
def iteration_builtin_deque_fifo(data):
    """Iterate through builtin deque using for-in"""
    deque = builtin_deque(data['initial_data'])
    checksum = 0
    for val in deque:
        checksum ^= val
    return checksum

# Modification operations
@benchmark.implementation("que", "modification")
def modification_que(data):
    """Modify Que elements using __setitem__"""
    que = Que(data['initial_data'])
    checksum = 0
    for i in range(len(que)):
        old_val = que[i]
        new_val = (old_val * 2) & 0xFFFFFFFF
        que[i] = new_val
        checksum ^= new_val
    return checksum

@benchmark.implementation("deque_fifo", "modification")
def modification_deque_fifo(data):
    """Modify Deque elements using __setitem__"""
    deque = Deque(data['initial_data'], maxlen=len(data['initial_data']) * 2)
    checksum = 0
    for i in range(len(deque)):
        old_val = deque[i]
        new_val = (old_val * 2) & 0xFFFFFFFF
        deque[i] = new_val
        checksum ^= new_val
    return checksum

@benchmark.implementation("builtin_deque_fifo", "modification")
def modification_builtin_deque_fifo(data):
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

# FIFO push/pop operations
@benchmark.implementation("que", "fifo_push_pop")
def fifo_push_pop_que(data):
    """FIFO push/pop on Que"""
    que = Que()
    checksum = 0
    
    # Push all values
    for val in data['push_values']:
        que.push(val)
        checksum ^= len(que)
    
    # Pop all values (FIFO order)
    while len(que) > 0:
        val = que.pop()
        checksum ^= val
    
    return checksum

@benchmark.implementation("deque_fifo", "fifo_push_pop")
def fifo_push_pop_deque_fifo(data):
    """FIFO push/pop on Deque"""
    deque = Deque(maxlen=len(data['push_values']) * 2)
    checksum = 0
    
    # Push all values (append right)
    for val in data['push_values']:
        deque.append(val)
        checksum ^= len(deque)
    
    # Pop all values (pop left for FIFO)
    while len(deque) > 0:
        val = deque.popleft()
        checksum ^= val
    
    return checksum

@benchmark.implementation("builtin_deque_fifo", "fifo_push_pop")
def fifo_push_pop_builtin_deque_fifo(data):
    """FIFO push/pop on builtin deque"""
    deque = builtin_deque()
    checksum = 0
    
    # Push all values (append right)
    for val in data['push_values']:
        deque.append(val)
        checksum ^= len(deque)
    
    # Pop all values (pop left for FIFO)
    while len(deque) > 0:
        val = deque.popleft()
        checksum ^= val
    
    return checksum


# Bulk operations (construct with data, then pop all)
@benchmark.implementation("que", "bulk_operations")
def bulk_operations_que(data):
    """Bulk construct and pop all on Que"""
    que = Que(data['initial_data'])
    checksum = 0
    
    # Pop all values
    while len(que) > 0:
        val = que.pop()
        checksum ^= val
    
    return checksum

@benchmark.implementation("deque_fifo", "bulk_operations")
def bulk_operations_deque_fifo(data):
    """Bulk construct and pop all on Deque"""
    deque = Deque(data['initial_data'], maxlen=len(data['initial_data']) * 2)
    checksum = 0
    
    # Pop all values (FIFO)
    while len(deque) > 0:
        val = deque.popleft()
        checksum ^= val
    
    return checksum

@benchmark.implementation("builtin_deque_fifo", "bulk_operations")
def bulk_operations_builtin_deque_fifo(data):
    """Bulk construct and pop all on builtin deque"""
    deque = builtin_deque(data['initial_data'])
    checksum = 0
    
    # Pop all values (FIFO)
    while len(deque) > 0:
        val = deque.popleft()
        checksum ^= val
    
    return checksum


# Mixed FIFO operations
@benchmark.implementation("que", "mixed_fifo")
def mixed_fifo_que(data):
    """Mixed FIFO operations on Que"""
    que = Que()
    checksum = 0
    
    for i, val in enumerate(data['push_values']):
        if i % 3 == 0:
            # Push
            que.push(val)
            checksum ^= len(que)
        elif i % 3 == 1 and len(que) > 0:
            # Pop (FIFO)
            popped = que.pop()
            checksum ^= popped
        else:
            # Push again
            que.push(val)
            checksum ^= len(que)
    
    return checksum

@benchmark.implementation("deque_fifo", "mixed_fifo")
def mixed_fifo_deque_fifo(data):
    """Mixed FIFO operations on Deque"""
    deque = Deque(maxlen=len(data['push_values']) * 2)
    checksum = 0
    
    for i, val in enumerate(data['push_values']):
        if i % 3 == 0:
            # Push (append right)
            deque.append(val)
            checksum ^= len(deque)
        elif i % 3 == 1 and len(deque) > 0:
            # Pop (pop left for FIFO)
            popped = deque.popleft()
            checksum ^= popped
        else:
            # Push again
            deque.append(val)
            checksum ^= len(deque)
    
    return checksum

@benchmark.implementation("builtin_deque_fifo", "mixed_fifo")
def mixed_fifo_builtin_deque_fifo(data):
    """Mixed FIFO operations on builtin deque"""
    deque = builtin_deque()
    checksum = 0
    
    for i, val in enumerate(data['push_values']):
        if i % 3 == 0:
            # Push (append right)
            deque.append(val)
            checksum ^= len(deque)
        elif i % 3 == 1 and len(deque) > 0:
            # Pop (pop left for FIFO)
            popped = deque.popleft()
            checksum ^= popped
        else:
            # Push again
            deque.append(val)
            checksum ^= len(deque)
    
    return checksum

if __name__ == "__main__":
    # Parse command line args and run appropriate mode
    runner = benchmark.parse_args()
    runner.run()