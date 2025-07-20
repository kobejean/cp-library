#!/usr/bin/env python3
"""
Benchmark comparing BIT2 (dual-channel BIT) vs regular BIT with tuples.
Tests construction, point updates, prefix sums, range sums, and mixed operations.
"""

import random
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from cp_library.perf.benchmark import Benchmark, BenchmarkConfig
from cp_library.ds.tree.bit.bit2_cls import BIT2
from cp_library.ds.tree.bit.bit_monoid_cls import BITMonoid

# Configure benchmark
config = BenchmarkConfig(
    name="bit2",
    sizes=[1000000, 100000, 10000, 1000, 100],  # Reverse order to warm up JIT
    operations=['construction', 'point_updates', 'prefix_sums', 'range_sums', 'mixed_ops'],
    iterations=10,
    warmup=3,
    output_dir="./output/benchmark_results/bit2"
)

# Create benchmark instance
benchmark = Benchmark(config)

# Define operations for BIT with tuples
def tuple_add(a, b):
    """Addition operation for tuples"""
    return (a[0] + b[0], a[1] + b[1])

def tuple_sub(a, b):
    """Subtraction operation for tuples"""
    return (a[0] - b[0], a[1] - b[1])

# Data generator
@benchmark.data_generator("default")
def generate_bit2_data(size: int, operation: str):
    """Generate test data for BIT2 operations"""
    # Generate random initial values
    values_a = [random.randint(1, 1000) for _ in range(size)]
    values_b = [random.randint(1, 1000) for _ in range(size)]
    
    # Create tuple values for regular BIT
    tuple_values = [(values_a[i], values_b[i]) for i in range(size)]
    
    # Generate update operations
    num_updates = min(1000, size // 10)
    update_indices = [random.randint(0, size - 1) for _ in range(num_updates)]
    update_values_a = [random.randint(1, 1000) for _ in range(num_updates)]
    update_values_b = [random.randint(1, 1000) for _ in range(num_updates)]
    update_tuple_values = [(update_values_a[i], update_values_b[i]) for i in range(num_updates)]
    
    # Generate query ranges
    num_queries = min(1000, size // 10)
    query_ranges = []
    for _ in range(num_queries):
        l = random.randint(0, size - 1)
        r = random.randint(l + 1, size)
        query_ranges.append((l, r))
    
    # Generate prefix indices
    prefix_indices = [random.randint(1, size) for _ in range(num_queries)]
    
    return {
        'values_a': values_a,
        'values_b': values_b,
        'tuple_values': tuple_values,
        'update_indices': update_indices,
        'update_values_a': update_values_a,
        'update_values_b': update_values_b,
        'update_tuple_values': update_tuple_values,
        'query_ranges': query_ranges,
        'prefix_indices': prefix_indices,
        'size': size
    }

# Setup functions to prepare data and reduce overhead during timing
@benchmark.setup("default")
def setup(data):
    prepared = data.copy()
    return prepared

# Construction operation
@benchmark.implementation("bit2_sum", "construction")
def construction_bit2_sum(data):
    """Construct BIT2 with sum operation"""
    bit = BIT2(data['tuple_values'])
    return len(bit)

@benchmark.implementation("tuple_bit_sum", "construction")
def construction_tuple_bit_sum(data):
    """Construct BITMonoid with tuple sum operation"""
    bit = BITMonoid(tuple_add, (0, 0), data['tuple_values'])
    return len(bit)

# Point updates operation
@benchmark.implementation("bit2_sum", "point_updates")
def point_updates_bit2_sum(data):
    """Point updates on BIT2 with sum"""
    bit = BIT2(data['size'])
    checksum = 0
    indices = data['update_indices']
    updates = data['update_tuple_values']
    for j in range(len(indices)):
        i = indices[j]
        val = updates[j]
        bit.set(i, val)
        result = bit.get(i)
        checksum ^= result[0] ^ result[1]
    return checksum

@benchmark.implementation("tuple_bit_sum", "point_updates")
def point_updates_tuple_bit_sum(data):
    """Point updates on BITMonoid with tuples"""
    bit = BITMonoid(tuple_add, (0, 0), data['size'])
    checksum = 0
    indices = data['update_indices']
    updates = data['update_tuple_values']
    for j in range(len(indices)):
        i = indices[j]
        val = updates[j]
        # Set element: add difference between target and current
        current = tuple_sub(bit.sum(i + 1), bit.sum(i))
        bit.add(i, tuple_sub(val, current))
        # Get element: reconstruct from prefix sums
        result = tuple_sub(bit.sum(i + 1), bit.sum(i))
        checksum ^= result[0] ^ result[1]
    return checksum

# Prefix sums operation
@benchmark.implementation("bit2_sum", "prefix_sums")
def prefix_sums_bit2_sum(data):
    """Prefix sums on BIT2 with sum"""
    bit = BIT2(data['tuple_values'])
    checksum = 0
    for n in data['prefix_indices']:
        result = bit.sum(n)
        checksum ^= result[0] ^ result[1]
    return checksum

@benchmark.implementation("tuple_bit_sum", "prefix_sums")
def prefix_sums_tuple_bit_sum(data):
    """Prefix sums on BITMonoid with tuples"""
    bit = BITMonoid(tuple_add, (0, 0), data['tuple_values'])
    checksum = 0
    for n in data['prefix_indices']:
        result = bit.sum(n)
        checksum ^= result[0] ^ result[1]
    return checksum

# Range sums operation
@benchmark.implementation("bit2_sum", "range_sums")
def range_sums_bit2_sum(data):
    """Range sums on BIT2 with sum"""
    bit = BIT2(data['tuple_values'])
    checksum = 0
    for l, r in data['query_ranges']:
        result = bit.sum_range(l, r)
        checksum ^= result[0] ^ result[1]
    return checksum

@benchmark.implementation("tuple_bit_sum", "range_sums")
def range_sums_tuple_bit_sum(data):
    """Range sums on BITMonoid with tuples"""
    bit = BITMonoid(tuple_add, (0, 0), data['tuple_values'])
    checksum = 0
    for l, r in data['query_ranges']:
        # Range sum: sum(r) - sum(l)
        result = tuple_sub(bit.sum(r), bit.sum(l))
        checksum ^= result[0] ^ result[1]
    return checksum

# Mixed operations (updates + queries)
@benchmark.implementation("bit2_sum", "mixed_ops")
def mixed_ops_bit2_sum(data):
    """Mixed updates and queries on BIT2"""
    bit = BIT2(data['tuple_values'])
    checksum = 0
    
    # Interleave updates and queries
    query_ranges = data['query_ranges']
    update_indices = data['update_indices']
    update_tuple_values = data['update_tuple_values']
    min_len = min(len(query_ranges), len(update_indices))
    
    for i in range(min_len):
        if i % 2 == 0:
            # Range query
            l, r = query_ranges[i]
            result = bit.sum_range(l, r)
            checksum ^= result[0] ^ result[1]
        else:
            # Update
            idx = update_indices[i]
            val = update_tuple_values[i]
            bit.add(idx, val)
            result = bit.get(idx)
            checksum ^= result[0] ^ result[1]
    return checksum

@benchmark.implementation("tuple_bit_sum", "mixed_ops")
def mixed_ops_tuple_bit_sum(data):
    """Mixed updates and queries on BITMonoid"""
    bit = BITMonoid(tuple_add, (0, 0), data['tuple_values'])
    checksum = 0
    
    # Interleave updates and queries
    query_ranges = data['query_ranges']
    update_indices = data['update_indices']
    update_tuple_values = data['update_tuple_values']
    min_len = min(len(query_ranges), len(update_indices))
    
    for i in range(min_len):
        if i % 2 == 0:
            # Range query
            l, r = query_ranges[i]
            result = tuple_sub(bit.sum(r), bit.sum(l))
            checksum ^= result[0] ^ result[1]
        else:
            # Update
            idx = update_indices[i]
            val = update_tuple_values[i]
            bit.add(idx, val)
            result = tuple_sub(bit.sum(idx + 1), bit.sum(idx))
            checksum ^= result[0] ^ result[1]
    return checksum

if __name__ == "__main__":
    # Parse command line args and run appropriate mode
    runner = benchmark.parse_args()
    runner.run()