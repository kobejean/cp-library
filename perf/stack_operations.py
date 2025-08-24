#!/usr/bin/env python3
"""
Benchmark comparing stack operations: stack_fn vs elist_fn vs normal list.
Tests push-only, mixed push/pop, and peek-heavy workloads.
"""

import random
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from cp_library.perf.benchmark import Benchmark, BenchmarkConfig
from cp_library.ds.stack.stack_fn import stack
from cp_library.ds.list.elist_fn import elist

# Configure benchmark
config = BenchmarkConfig(
    name="stack_operations",
    sizes=[1000000, 100000, 10000, 1000],  # Reverse order to warm up JIT
    operations=['construction', 'push_only', 'pop_only', 'push_pop_mixed', 'peek_heavy', 'construction_with_data'],
    iterations=10,
    warmup=3,
    output_dir="./output/benchmark_results/stack"
)

# Create benchmark instance
benchmark = Benchmark(config)

# Data generator
@benchmark.data_generator("default")
def generate_stack_data(size: int, operation: str):
    """Generate test data for stack operations"""
    # Generate values to push
    push_values = [random.randint(0, 1000000) for _ in range(size)]
    
    # For mixed operations, generate operation sequence
    num_ops = min(size, 100000)  # Limit operations for large sizes
    
    return {
        'size': size,
        'push_values': push_values,
        'num_ops': num_ops,
        'operation': operation
    }

# Setup functions for operations that need preinitialized stacks
@benchmark.setup("stack", ["pop_only"])
def setup_stack_pop(data):
    """Setup stack with data for pop operations"""
    new_data = data.copy()
    size = data['size']
    values = data['push_values']
    
    st = stack(size)
    for val in values:
        st.push(val)
    
    new_data['stack'] = st
    return new_data

@benchmark.setup("elist", ["pop_only"])
def setup_elist_pop(data):
    """Setup elist with data for pop operations"""
    new_data = data.copy()
    size = data['size']
    values = data['push_values']
    
    lst = elist(size)
    for val in values:
        lst.append(val)
    
    new_data['elist'] = lst
    return new_data

@benchmark.setup("list", ["pop_only"])
def setup_list_pop(data):
    """Setup list with data for pop operations"""
    new_data = data.copy()
    values = data['push_values']
    
    new_data['list'] = values.copy()
    return new_data

# Push-only operation
@benchmark.implementation("stack", "push_only")
def push_only_stack(data):
    """Push n elements using stack class"""
    size = data['size']
    values = data['push_values']
    
    st = stack(size)
    for val in values:
        st.push(val)
    
    # Return something to verify correctness
    return len(st)

@benchmark.implementation("elist", "push_only")
def push_only_elist(data):
    """Push n elements using elist with hint"""
    size = data['size']
    values = data['push_values']
    
    lst = elist(size)
    for val in values:
        lst.append(val)
    
    return len(lst)

@benchmark.implementation("list", "push_only")
def push_only_list(data):
    """Push n elements using normal list"""
    values = data['push_values']
    
    lst = []
    for val in values:
        lst.append(val)
    
    return len(lst)

# Mixed push/pop operations
@benchmark.implementation("stack", "push_pop_mixed")
def push_pop_mixed_stack(data):
    """Mixed push and pop operations using stack class"""
    size = data['size']
    num_ops = data['num_ops']
    
    st = stack(size)
    
    # Initial push
    for i in range(size // 2):
        st.push(i)
    
    # Mixed operations
    checksum = 0
    for i in range(num_ops):
        if i % 3 == 0 and len(st) > 0:
            checksum ^= st.pop()
        else:
            st.push(i)
            if len(st) > size * 0.9:  # Prevent overflow
                st.pop()
    
    return checksum

@benchmark.implementation("elist", "push_pop_mixed")
def push_pop_mixed_elist(data):
    """Mixed push and pop operations using elist"""
    size = data['size']
    num_ops = data['num_ops']
    
    lst = elist(size)
    
    # Initial push
    for i in range(size // 2):
        lst.append(i)
    
    # Mixed operations
    checksum = 0
    for i in range(num_ops):
        if i % 3 == 0 and len(lst) > 0:
            checksum ^= lst.pop()
        else:
            lst.append(i)
            if len(lst) > size * 0.9:
                lst.pop()
    
    return checksum

@benchmark.implementation("list", "push_pop_mixed")
def push_pop_mixed_list(data):
    """Mixed push and pop operations using normal list"""
    size = data['size']
    num_ops = data['num_ops']
    
    lst = []
    
    # Initial push
    for i in range(size // 2):
        lst.append(i)
    
    # Mixed operations
    checksum = 0
    for i in range(num_ops):
        if i % 3 == 0 and len(lst) > 0:
            checksum ^= lst.pop()
        else:
            lst.append(i)
            if len(lst) > size * 0.9:
                lst.pop()
    
    return checksum

# Peek-heavy operations
@benchmark.implementation("stack", "peek_heavy")
def peek_heavy_stack(data):
    """Peek-heavy operations using stack class"""
    size = min(data['size'], 10000)  # Limit for peek operations
    
    st = stack(size)
    for i in range(size):
        st.push(i)
    
    checksum = 0
    # Many peek operations
    for _ in range(size * 10):
        if len(st) > 0:
            checksum ^= st.peek()
    
    return checksum

@benchmark.implementation("elist", "peek_heavy")
def peek_heavy_elist(data):
    """Peek-heavy operations using elist"""
    size = min(data['size'], 10000)
    
    lst = elist(size)
    for i in range(size):
        lst.append(i)
    
    checksum = 0
    for _ in range(size * 10):
        if len(lst) > 0:
            checksum ^= lst[-1]
    
    return checksum

@benchmark.implementation("list", "peek_heavy")
def peek_heavy_list(data):
    """Peek-heavy operations using normal list"""
    size = min(data['size'], 10000)
    
    lst = []
    for i in range(size):
        lst.append(i)
    
    checksum = 0
    for _ in range(size * 10):
        if len(lst) > 0:
            checksum ^= lst[-1]
    
    return checksum

# Construction benchmarks
@benchmark.implementation("stack", "construction")
def construction_stack(data):
    """Construct empty stack with capacity"""
    size = data['size']
    st = stack(size)
    return len(st)  # Should be 0

@benchmark.implementation("elist", "construction")
def construction_elist(data):
    """Construct empty elist with hint"""
    size = data['size']
    lst = elist(size)
    return len(lst)  # Should be 0

@benchmark.implementation("list", "construction")
def construction_list(data):
    """Construct empty list"""
    lst = []
    return len(lst)  # Should be 0

# Construction with initial data
@benchmark.implementation("stack", "construction_with_data")
def construction_with_data_stack(data):
    """Construct and fill stack"""
    size = data['size']
    values = data['push_values']
    
    st = stack(size)
    for val in values:
        st.push(val)
    return len(st)

@benchmark.implementation("elist", "construction_with_data")
def construction_with_data_elist(data):
    """Construct and fill elist"""
    size = data['size']
    values = data['push_values']
    
    lst = elist(size)
    for val in values:
        lst.append(val)
    return len(lst)

@benchmark.implementation("list", "construction_with_data")
def construction_with_data_list(data):
    """Construct and fill list using comprehension"""
    values = data['push_values']
    lst = [val for val in values]
    return len(lst)

# Pop-only operations (with preinitialized data)
@benchmark.implementation("stack", "pop_only")
def pop_only_stack(data):
    """Pop all elements from preinitialized stack"""
    st = data['stack']
    checksum = 0
    
    while len(st) > 0:
        checksum ^= st.pop()
    
    return checksum

@benchmark.implementation("elist", "pop_only")
def pop_only_elist(data):
    """Pop all elements from preinitialized elist"""
    lst = data['elist']
    checksum = 0
    
    while len(lst) > 0:
        checksum ^= lst.pop()
    
    return checksum

@benchmark.implementation("list", "pop_only")
def pop_only_list(data):
    """Pop all elements from preinitialized list"""
    lst = data['list']
    checksum = 0
    
    while len(lst) > 0:
        checksum ^= lst.pop()
    
    return checksum

if __name__ == "__main__":
    # Parse command line args and run appropriate mode
    runner = benchmark.parse_args()
    runner.run()