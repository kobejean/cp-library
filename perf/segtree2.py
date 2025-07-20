#!/usr/bin/env python3
"""
Benchmark comparing SegTree2 (dual-channel segment tree) vs regular segment tree with tuples.
Tests construction, point updates, range queries, and search operations.
"""

import random
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from cp_library.perf.benchmark import Benchmark, BenchmarkConfig
from cp_library.ds.tree.seg.segtree2_cls import SegTree2
from cp_library.ds.tree.seg.segtree_cls import SegTree

# Configure benchmark
config = BenchmarkConfig(
    name="segtree2",
    sizes=[1000000, 100000, 10000, 1000, 100],  # Reverse order to warm up JIT
    operations=['construction', 'point_updates', 'range_queries', 'mixed_ops', 'max_right_search', 'all_prod'],
    iterations=10,
    warmup=3,
    output_dir="./output/benchmark_results/segtree2"
)

# Create benchmark instance
benchmark = Benchmark(config)

# Define operations for segment trees
def tuple_add(a, b):
    """Addition operation for tuples"""
    return (a[0] + b[0], a[1] + b[1])

def dual_max(a, b):
    """Max operation for dual values"""
    return (max(a[0], b[0]), max(a[1], b[1]))

def sum_threshold_check(x, threshold):
    """Check if sum of tuple components is less than or equal to threshold"""
    return x[0] + x[1] <= threshold

# Data generator
@benchmark.data_generator("default")
def generate_segtree2_data(size: int, operation: str):
    """Generate test data for SegTree2 operations"""
    # Generate random initial values
    values_a = [random.randint(1, 1000) for _ in range(size)]
    values_b = [random.randint(1, 1000) for _ in range(size)]
    
    # Create tuple values for regular SegTree
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
    
    return {
        'values_a': values_a,
        'values_b': values_b,
        'tuple_values': tuple_values,
        'update_indices': update_indices,
        'update_values_a': update_values_a,
        'update_values_b': update_values_b,
        'update_tuple_values': update_tuple_values,
        'query_ranges': query_ranges,
        'size': size,
        'threshold': size * 100
    }

# Setup functions to prepare data and reduce overhead during timing
@benchmark.setup("segtree2_sum", ["construction", "range_queries", "mixed_ops", "max_right_search", "all_prod"])
def setup_segtree2_sum(data):
    """Prepare data for SegTree2 sum operations"""
    prepared = data.copy()
    # Pre-create tuple pairs for construction
    prepared['segtree2_init_data'] = [(data['values_a'][i], data['values_b'][i]) for i in range(data['size'])]
    # Pre-create update pairs
    prepared['segtree2_updates'] = [(data['update_values_a'][i], data['update_values_b'][i]) for i in range(len(data['update_indices']))]
    return prepared

@benchmark.setup("segtree2_max", ["construction", "point_updates", "range_queries", "all_prod"])
def setup_segtree2_max(data):
    """Prepare data for SegTree2 max operations"""
    prepared = data.copy()
    # Pre-create tuple pairs for construction
    prepared['segtree2_init_data'] = [(data['values_a'][i], data['values_b'][i]) for i in range(data['size'])]
    # Pre-create update pairs
    prepared['segtree2_updates'] = [(data['update_values_a'][i], data['update_values_b'][i]) for i in range(len(data['update_indices']))]
    return prepared

@benchmark.setup("segtree_tuple_sum", ["mixed_ops"])
def setup_segtree_tuple_sum(data):
    """Prepare data for regular SegTree tuple operations"""
    prepared = data.copy()
    return prepared

@benchmark.setup("segtree_tuple_max", ["point_updates"])
def setup_segtree_tuple_max(data):
    """Prepare data for regular SegTree tuple max operations"""
    prepared = data.copy()
    return prepared

# Construction operation
@benchmark.implementation("segtree2_sum", "construction")
def construction_segtree2_sum(data):
    """Construct SegTree2 with sum operation"""
    seg = SegTree2(tuple_add, (0, 0), data['segtree2_init_data'])
    return seg.n

@benchmark.implementation("segtree_tuple_sum", "construction")
def construction_segtree_tuple_sum(data):
    """Construct regular SegTree with tuple sum operation"""
    seg = SegTree(tuple_add, (0, 0), data['tuple_values'])
    return seg.n

@benchmark.implementation("segtree2_max", "construction")
def construction_segtree2_max(data):
    """Construct SegTree2 with max operation"""
    seg = SegTree2(dual_max, (0, 0), data['segtree2_init_data'])
    return seg.n

@benchmark.implementation("segtree_tuple_max", "construction")
def construction_segtree_tuple_max(data):
    """Construct regular SegTree with tuple max operation"""
    seg = SegTree(dual_max, (0, 0), data['tuple_values'])
    return seg.n

# Point updates operation
@benchmark.implementation("segtree2_sum", "point_updates")
def point_updates_segtree2_sum(data):
    """Point updates on SegTree2 with sum"""
    seg = SegTree2(tuple_add, (0, 0), data['size'])
    checksum = 0
    indices = data['update_indices']
    updates = data['segtree2_updates']
    for j in range(len(indices)):
        i = indices[j]
        val = updates[j]
        seg.set(i, val)
        result = seg.get(i)
        checksum ^= result[0] ^ result[1]
    return checksum

@benchmark.implementation("segtree_tuple_sum", "point_updates")
def point_updates_segtree_tuple_sum(data):
    """Point updates on regular SegTree with tuples"""
    seg = SegTree(tuple_add, (0, 0), data['size'])
    checksum = 0
    indices = data['update_indices']
    updates = data['update_tuple_values']
    for j in range(len(indices)):
        i = indices[j]
        val = updates[j]
        seg.set(i, val)
        result = seg.get(i)
        checksum ^= result[0] ^ result[1]
    return checksum

@benchmark.implementation("segtree2_max", "point_updates")
def point_updates_segtree2_max(data):
    """Point updates on SegTree2 with max"""
    seg = SegTree2(dual_max, (0, 0), data['size'])
    checksum = 0
    indices = data['update_indices']
    updates = data['segtree2_updates']
    for j in range(len(indices)):
        i = indices[j]
        val = updates[j]
        seg.set(i, val)
        result = seg.get(i)
        checksum ^= result[0] ^ result[1]
    return checksum

@benchmark.implementation("segtree_tuple_max", "point_updates")
def point_updates_segtree_tuple_max(data):
    """Point updates on regular SegTree with tuple max"""
    seg = SegTree(dual_max, (0, 0), data['size'])
    checksum = 0
    indices = data['update_indices']
    updates = data['update_tuple_values']
    for j in range(len(indices)):
        i = indices[j]
        val = updates[j]
        seg.set(i, val)
        result = seg.get(i)
        checksum ^= result[0] ^ result[1]
    return checksum

# Range queries operation
@benchmark.implementation("segtree2_sum", "range_queries")
def range_queries_segtree2_sum(data):
    """Range queries on SegTree2 with sum"""
    seg = SegTree2(tuple_add, (0, 0), data['segtree2_init_data'])
    checksum = 0
    for l, r in data['query_ranges']:
        result = seg.prod(l, r)
        checksum ^= result[0] ^ result[1]
    return checksum

@benchmark.implementation("segtree_tuple_sum", "range_queries")
def range_queries_segtree_tuple_sum(data):
    """Range queries on regular SegTree with tuples"""
    seg = SegTree(tuple_add, (0, 0), data['tuple_values'])
    checksum = 0
    for l, r in data['query_ranges']:
        result = seg.prod(l, r)
        checksum ^= result[0] ^ result[1]
    return checksum

@benchmark.implementation("segtree2_max", "range_queries")
def range_queries_segtree2_max(data):
    """Range queries on SegTree2 with max"""
    seg = SegTree2(dual_max, (0, 0), data['segtree2_init_data'])
    checksum = 0
    for l, r in data['query_ranges']:
        result = seg.prod(l, r)
        checksum ^= result[0] ^ result[1]
    return checksum

@benchmark.implementation("segtree_tuple_max", "range_queries")
def range_queries_segtree_tuple_max(data):
    """Range queries on regular SegTree with tuple max"""
    seg = SegTree(dual_max, (0, 0), data['tuple_values'])
    checksum = 0
    for l, r in data['query_ranges']:
        result = seg.prod(l, r)
        checksum ^= result[0] ^ result[1]
    return checksum

# Mixed operations (updates + queries)
@benchmark.implementation("segtree2_sum", "mixed_ops")
def mixed_ops_segtree2_sum(data):
    """Mixed updates and queries on SegTree2"""
    seg = SegTree2(tuple_add, (0, 0), data['segtree2_init_data'])
    checksum = 0
    
    # Interleave updates and queries
    query_ranges = data['query_ranges']
    update_indices = data['update_indices']
    segtree2_updates = data['segtree2_updates']
    min_len = min(len(query_ranges), len(update_indices), len(segtree2_updates))
    
    for i in range(min_len):
        if i % 2 == 0:
            # Query
            l, r = query_ranges[i]
            result = seg.prod(l, r)
            checksum ^= result[0] ^ result[1]
        else:
            # Update
            idx = update_indices[i]
            val = segtree2_updates[i]
            seg.set(idx, val)
            result = seg.get(idx)
            checksum ^= result[0] ^ result[1]
    return checksum

@benchmark.implementation("segtree_tuple_sum", "mixed_ops")
def mixed_ops_segtree_tuple_sum(data):
    """Mixed updates and queries on regular SegTree"""
    seg = SegTree(tuple_add, (0, 0), data['tuple_values'])
    checksum = 0
    
    # Interleave updates and queries
    query_ranges = data['query_ranges']
    update_indices = data['update_indices']
    update_tuple_values = data['update_tuple_values']
    min_len = min(len(query_ranges), len(update_indices), len(update_tuple_values))
    
    for i in range(min_len):
        if i % 2 == 0:
            # Query
            l, r = query_ranges[i]
            result = seg.prod(l, r)
            checksum ^= result[0] ^ result[1]
        else:
            # Update
            idx = update_indices[i]
            val = update_tuple_values[i]
            seg.set(idx, val)
            result = seg.get(idx)
            checksum ^= result[0] ^ result[1]
    return checksum

# Max right search operation
@benchmark.implementation("segtree2_sum", "max_right_search")
def max_right_search_segtree2_sum(data):
    """Binary search using max_right on SegTree2"""
    seg = SegTree2(tuple_add, (0, 0), data['segtree2_init_data'])
    checksum = 0
    
    # Search for positions where sum is less than threshold
    threshold = data['threshold']
    def check_predicate(x):
        return sum_threshold_check(x, threshold)
    
    for i in range(0, data['size'], max(1, data['size'] // 100)):
        pos = seg.max_right(i, check_predicate)
        checksum ^= pos
    return checksum

@benchmark.implementation("segtree_tuple_sum", "max_right_search")
def max_right_search_segtree_tuple_sum(data):
    """Binary search using max_right on regular SegTree"""
    seg = SegTree(tuple_add, (0, 0), data['tuple_values'])
    checksum = 0
    
    # Search for positions where sum is less than threshold
    threshold = data['threshold']
    def check_predicate(x):
        return sum_threshold_check(x, threshold)
    
    for i in range(0, data['size'], max(1, data['size'] // 100)):
        pos = seg.max_right(i, check_predicate)
        checksum ^= pos
    return checksum

# All product operation
@benchmark.implementation("segtree2_sum", "all_prod")
def all_prod_segtree2_sum(data):
    """Get total sum using all_prod on SegTree2"""
    seg = SegTree2(tuple_add, (0, 0), data['segtree2_init_data'])
    result = seg.all_prod()
    return result[0] ^ result[1]

@benchmark.implementation("segtree_tuple_sum", "all_prod")
def all_prod_segtree_tuple_sum(data):
    """Get total sum using all_prod on regular SegTree"""
    seg = SegTree(tuple_add, (0, 0), data['tuple_values'])
    result = seg.all_prod()
    return result[0] ^ result[1]

@benchmark.implementation("segtree2_max", "all_prod")
def all_prod_segtree2_max(data):
    """Get global max using all_prod on SegTree2"""
    seg = SegTree2(dual_max, (0, 0), data['segtree2_init_data'])
    result = seg.all_prod()
    return result[0] ^ result[1]

@benchmark.implementation("segtree_tuple_max", "all_prod")
def all_prod_segtree_tuple_max(data):
    """Get global max using all_prod on regular SegTree"""
    seg = SegTree(dual_max, (0, 0), data['tuple_values'])
    result = seg.all_prod()
    return result[0] ^ result[1]

if __name__ == "__main__":
    # Parse command line args and run appropriate mode
    runner = benchmark.parse_args()
    runner.run()