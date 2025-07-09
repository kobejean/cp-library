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
    sizes=[100, 1000, 10000, 50000],
    operations=['random', 'sorted', 'duplicates', 'reverse'],
    iterations=5,
    warmup=2,
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
    
    return {
        'data': data,
        'distinct': False,
        'size': size,
        'operation': operation
    }

# Implementation: irank
@benchmark.implementation("irank", ["random", "sorted", "duplicates", "reverse"])
def irank_implementation(data):
    """Standard irank implementation"""
    return irank(data['data'].copy(), distinct=data['distinct'])

# Implementation: irank_multi
@benchmark.implementation("irank_multi", ["random", "sorted", "duplicates", "reverse"])
def irank_multi_implementation(data):
    """Multi-pass irank implementation"""
    return irank_multi(data['data'].copy(), distinct=data['distinct'])

# Additional benchmark with distinct=True
@benchmark.data_generator("distinct")
def generate_rank_data_distinct(size: int, operation: str):
    """Generate ranking data with distinct=True"""
    base_data = generate_rank_data(size, operation)
    base_data['distinct'] = True
    return base_data

@benchmark.implementation("irank_distinct", ["random", "sorted", "duplicates", "reverse"])
def irank_distinct_implementation(data):
    """irank with distinct=True"""
    return irank(data['data'].copy(), distinct=True)

@benchmark.implementation("irank_multi_distinct", ["random", "sorted", "duplicates", "reverse"])
def irank_multi_distinct_implementation(data):
    """irank_multi with distinct=True"""
    return irank_multi(data['data'].copy(), distinct=True)

# Custom validator for rank results
@benchmark.validator("default")
def validate_rank_result(expected, actual):
    """Validate ranking results"""
    if isinstance(expected, list) and isinstance(actual, list):
        return len(expected) == len(actual) and all(
            0 <= e < len(expected) and 0 <= a < len(actual) 
            for e, a in zip(expected, actual)
        )
    return expected == actual

if __name__ == "__main__":
    # Run with default data generator
    print("Running rank benchmark with distinct=False...")
    benchmark.run()
    
    # Create a separate benchmark for distinct=True
    print("\nRunning rank benchmark with distinct=True...")
    config_distinct = BenchmarkConfig(
        name="rank_distinct",
        sizes=[100, 1000, 10000, 50000],
        operations=['random', 'sorted', 'duplicates', 'reverse'],
        iterations=5,
        warmup=2,
        output_dir="./output/benchmark_results/rank_distinct"
    )
    benchmark_distinct = Benchmark(config_distinct)
    benchmark_distinct.data_generators = {"default": generate_rank_data_distinct}
    benchmark_distinct.implementations = {
        "irank_distinct": irank_distinct_implementation,
        "irank_multi_distinct": irank_multi_distinct_implementation
    }
    benchmark_distinct.validators = {"default": validate_rank_result}
    benchmark_distinct.run()