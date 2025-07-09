#!/usr/bin/env python3
"""
Simple ranking benchmark using the new declarative framework.
Compares irank vs irank_multi performance across different data patterns.
"""

import random
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from cp_library.perf.benchmark import Benchmark, BenchmarkConfig
from cp_library.alg.iter.rank.irank_fn import irank
from cp_library.alg.iter.rank.irank_multi_fn import irank as irank_multi

# Configure benchmark
config = BenchmarkConfig(
    name="rank",
    sizes=[1000000, 100000, 10000, 1000, 100, 10, 1],  # Reverse order to warm up JIT
    operations=['construction', 'random', 'sorted', 'duplicates', 'reverse'],
    iterations=5,
    warmup=3,
    output_dir="./output/benchmark_results/rank"
)

# Create benchmark instance
benchmark = Benchmark(config)

# Data generator
@benchmark.data_generator("default")
def generate_rank_data(size: int, operation: str):
    """Generate ranking data in different patterns"""
    if operation == 'random':
        data = [random.randint(1, size) for _ in range(size)]
    elif operation == 'sorted':
        data = list(range(size))
    elif operation == 'duplicates':
        # Many duplicates (10% unique values)
        unique_count = max(1, size // 10)
        data = [random.randint(1, unique_count) for _ in range(size)]
    elif operation == 'reverse':
        data = list(range(size, 0, -1))
    else:
        raise ValueError(f"Unknown operation: {operation}")
    
    # Pre-initialize data for fair timing (exclude copy overhead)
    preinitialized = {
        'data_copy1': list(data),
        'data_copy2': list(data),
        'distinct': False
    }
    
    return {
        'data': data,
        'distinct': False,
        'size': size,
        'operation': operation,
        'preinitialized': preinitialized
    }

# Construction operation
@benchmark.implementation("irank", "construction")
def construction_irank(data):
    """Construct data copy for irank"""
    data_copy = list(data['data'])
    checksum = 0
    for x in data_copy:
        checksum ^= x
    return checksum

@benchmark.implementation("irank_multi", "construction")
def construction_irank_multi(data):
    """Construct data copy for irank_multi"""
    data_copy = list(data['data'])
    checksum = 0
    for x in data_copy:
        checksum ^= x
    return checksum

# Random operation
@benchmark.implementation("irank", "random")
def random_irank(data):
    """Standard irank implementation for random data"""
    pre = data['preinitialized']
    result = irank(pre['data_copy1'], distinct=pre['distinct'])
    checksum = 0
    for x in result:
        checksum ^= x
    return checksum

@benchmark.implementation("irank_multi", "random")
def random_irank_multi(data):
    """Multi-pass irank implementation for random data"""
    pre = data['preinitialized']
    result = irank_multi(pre['data_copy2'], distinct=pre['distinct'])
    checksum = 0
    for x in result:
        checksum ^= x
    return checksum

# Sorted operation
@benchmark.implementation("irank", "sorted")
def sorted_irank(data):
    """Standard irank implementation for sorted data"""
    pre = data['preinitialized']
    result = irank(pre['data_copy1'], distinct=pre['distinct'])
    checksum = 0
    for x in result:
        checksum ^= x
    return checksum

@benchmark.implementation("irank_multi", "sorted")
def sorted_irank_multi(data):
    """Multi-pass irank implementation for sorted data"""
    pre = data['preinitialized']
    result = irank_multi(pre['data_copy2'], distinct=pre['distinct'])
    checksum = 0
    for x in result:
        checksum ^= x
    return checksum

# Duplicates operation
@benchmark.implementation("irank", "duplicates")
def duplicates_irank(data):
    """Standard irank implementation for data with duplicates"""
    pre = data['preinitialized']
    result = irank(pre['data_copy1'], distinct=pre['distinct'])
    checksum = 0
    for x in result:
        checksum ^= x
    return checksum

@benchmark.implementation("irank_multi", "duplicates")
def duplicates_irank_multi(data):
    """Multi-pass irank implementation for data with duplicates"""
    pre = data['preinitialized']
    result = irank_multi(pre['data_copy2'], distinct=pre['distinct'])
    checksum = 0
    for x in result:
        checksum ^= x
    return checksum

# Reverse operation
@benchmark.implementation("irank", "reverse")
def reverse_irank(data):
    """Standard irank implementation for reverse data"""
    pre = data['preinitialized']
    result = irank(pre['data_copy1'], distinct=pre['distinct'])
    checksum = 0
    for x in result:
        checksum ^= x
    return checksum

@benchmark.implementation("irank_multi", "reverse")
def reverse_irank_multi(data):
    """Multi-pass irank implementation for reverse data"""
    pre = data['preinitialized']
    result = irank_multi(pre['data_copy2'], distinct=pre['distinct'])
    checksum = 0
    for x in result:
        checksum ^= x
    return checksum

# Additional benchmark with distinct=True
@benchmark.data_generator("distinct")
def generate_rank_data_distinct(size: int, operation: str):
    """Generate ranking data with distinct=True"""
    base_data = generate_rank_data(size, operation)
    base_data['distinct'] = True
    base_data['preinitialized']['distinct'] = True
    return base_data

def irank_distinct_implementation(data):
    """irank with distinct=True"""
    pre = data['preinitialized']
    result = irank(pre['data_copy1'], distinct=True)
    checksum = 0
    for x in result:
        checksum ^= x
    return checksum

def irank_multi_distinct_implementation(data):
    """irank_multi with distinct=True"""
    pre = data['preinitialized']
    result = irank_multi(pre['data_copy2'], distinct=True)
    checksum = 0
    for x in result:
        checksum ^= x
    return checksum

# Custom validator for rank results (now using XOR checksums)
@benchmark.validator("default")
def validate_rank_result(expected, actual):
    """Validate ranking results using XOR checksums"""
    try:
        # Compare XOR checksums directly
        return int(expected) == int(actual)
    except Exception:
        return False

if __name__ == "__main__":
    # Run with default data generator
    print("Running rank benchmark with distinct=False...")
    benchmark.run()
    
    # Create a separate benchmark for distinct=True
    print("\nRunning rank benchmark with distinct=True...")
    config_distinct = BenchmarkConfig(
        name="rank_distinct",
        sizes=[1000000, 100000, 10000, 1000, 100, 10, 1],  # Reverse order to warm up JIT
        operations=['construction', 'random', 'sorted', 'duplicates', 'reverse'],
        iterations=5,
        warmup=3,
        output_dir="./output/benchmark_results/rank_distinct"
    )
    benchmark_distinct = Benchmark(config_distinct)
    benchmark_distinct.data_generators = {"default": generate_rank_data_distinct}
    
    # Register implementations properly for each operation
    for operation in config_distinct.operations:
        if operation == "construction":
            benchmark_distinct.implementations[operation] = {
                "irank_distinct": lambda data: construction_irank(data),
                "irank_multi_distinct": lambda data: construction_irank_multi(data)
            }
        else:
            benchmark_distinct.implementations[operation] = {
                "irank_distinct": irank_distinct_implementation,
                "irank_multi_distinct": irank_multi_distinct_implementation
            }
    
    benchmark_distinct.validators = {"default": validate_rank_result}
    benchmark_distinct.run()