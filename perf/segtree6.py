#!/usr/bin/env python3
"""
Benchmark comparing SegTree6 (6-channel segment tree) vs regular segment tree with tuples.
Tests construction, point updates, range queries, and search operations.
"""

import random
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from cp_library.perf.benchmark import Benchmark, BenchmarkConfig
from cp_library.ds.tree.seg.segtree6_cls import SegTree6
from cp_library.ds.tree.seg.segtree_cls import SegTree

# Configure benchmark
config = BenchmarkConfig(
    name="segtree6",
    sizes=[1000000, 100000, 10000, 1000, 100],  # Reverse order to warm up JIT
    operations=['construction', 'point_updates', 'range_queries', 'mixed_ops', 'max_right_search', 'all_prod'],
    iterations=10,
    warmup=3,
    output_dir="./output/benchmark_results/segtree6"
)

# Create benchmark instance
benchmark = Benchmark(config)

# Define operations for segment trees
def tuple6_add(a, b):
    """Addition operation for 6-tuples"""
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2], a[3] + b[3], a[4] + b[4], a[5] + b[5])

def hex_max(a, b):
    """Max operation for 6 values"""
    return (max(a[0], b[0]), max(a[1], b[1]), max(a[2], b[2]), 
            max(a[3], b[3]), max(a[4], b[4]), max(a[5], b[5]))

def sum6_threshold_check(x, threshold):
    """Check if sum of 6-tuple components is less than or equal to threshold"""
    return sum(x) <= threshold

# Data generator
@benchmark.data_generator("default")
def generate_segtree6_data(size: int, operation: str):
    """Generate test data for SegTree6 operations"""
    # Generate random initial values
    values_a1 = [random.randint(1, 1000) for _ in range(size)]
    values_a2 = [random.randint(1, 1000) for _ in range(size)]
    values_a3 = [random.randint(1, 1000) for _ in range(size)]
    values_a4 = [random.randint(1, 1000) for _ in range(size)]
    values_a5 = [random.randint(1, 1000) for _ in range(size)]
    values_a6 = [random.randint(1, 1000) for _ in range(size)]
    
    # Create tuple values for regular SegTree
    tuple_values = [(values_a1[i], values_a2[i], values_a3[i], values_a4[i], values_a5[i], values_a6[i]) 
                    for i in range(size)]
    
    # Generate update operations
    num_updates = min(1000, size // 10)
    update_indices = [random.randint(0, size - 1) for _ in range(num_updates)]
    update_values_a1 = [random.randint(1, 1000) for _ in range(num_updates)]
    update_values_a2 = [random.randint(1, 1000) for _ in range(num_updates)]
    update_values_a3 = [random.randint(1, 1000) for _ in range(num_updates)]
    update_values_a4 = [random.randint(1, 1000) for _ in range(num_updates)]
    update_values_a5 = [random.randint(1, 1000) for _ in range(num_updates)]
    update_values_a6 = [random.randint(1, 1000) for _ in range(num_updates)]
    update_tuple_values = [(update_values_a1[i], update_values_a2[i], update_values_a3[i],
                           update_values_a4[i], update_values_a5[i], update_values_a6[i]) 
                          for i in range(num_updates)]
    
    # Generate query ranges
    num_queries = min(1000, size // 10)
    query_ranges = []
    for _ in range(num_queries):
        l = random.randint(0, size - 1)
        r = random.randint(l + 1, size)
        query_ranges.append((l, r))
    
    return {
        'values_a1': values_a1,
        'values_a2': values_a2,
        'values_a3': values_a3,
        'values_a4': values_a4,
        'values_a5': values_a5,
        'values_a6': values_a6,
        'tuple_values': tuple_values,
        'update_indices': update_indices,
        'update_values_a1': update_values_a1,
        'update_values_a2': update_values_a2,
        'update_values_a3': update_values_a3,
        'update_values_a4': update_values_a4,
        'update_values_a5': update_values_a5,
        'update_values_a6': update_values_a6,
        'update_tuple_values': update_tuple_values,
        'query_ranges': query_ranges,
        'size': size,
        'threshold': size * 100
    }

# Setup functions to prepare data and reduce overhead during timing
@benchmark.setup("segtree6_sum", ["construction", "range_queries", "mixed_ops", "max_right_search", "all_prod"])
def setup_segtree6_sum(data):
    """Prepare data for SegTree6 sum operations"""
    prepared = data.copy()
    # Pre-create 6-tuple pairs for construction
    prepared['segtree6_init_data'] = [(data['values_a1'][i], data['values_a2'][i], data['values_a3'][i],
                                      data['values_a4'][i], data['values_a5'][i], data['values_a6'][i]) 
                                     for i in range(data['size'])]
    # Pre-create update 6-tuples
    prepared['segtree6_updates'] = [(data['update_values_a1'][i], data['update_values_a2'][i], data['update_values_a3'][i],
                                    data['update_values_a4'][i], data['update_values_a5'][i], data['update_values_a6'][i]) 
                                   for i in range(len(data['update_indices']))]
    return prepared

@benchmark.setup("segtree6_max", ["construction", "point_updates", "range_queries", "all_prod"])
def setup_segtree6_max(data):
    """Prepare data for SegTree6 max operations"""
    prepared = data.copy()
    # Pre-create 6-tuple pairs for construction
    prepared['segtree6_init_data'] = [(data['values_a1'][i], data['values_a2'][i], data['values_a3'][i],
                                      data['values_a4'][i], data['values_a5'][i], data['values_a6'][i]) 
                                     for i in range(data['size'])]
    # Pre-create update 6-tuples
    prepared['segtree6_updates'] = [(data['update_values_a1'][i], data['update_values_a2'][i], data['update_values_a3'][i],
                                    data['update_values_a4'][i], data['update_values_a5'][i], data['update_values_a6'][i]) 
                                   for i in range(len(data['update_indices']))]
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
@benchmark.implementation("segtree6_sum", "construction")
def construction_segtree6_sum(data):
    """Construct SegTree6 with sum operation"""
    seg = SegTree6(tuple6_add, (0, 0, 0, 0, 0, 0), data['segtree6_init_data'])
    return seg.n

@benchmark.implementation("segtree_tuple_sum", "construction")
def construction_segtree_tuple_sum(data):
    """Construct regular SegTree with 6-tuple sum operation"""
    seg = SegTree(tuple6_add, (0, 0, 0, 0, 0, 0), data['tuple_values'])
    return seg.n

@benchmark.implementation("segtree6_max", "construction")
def construction_segtree6_max(data):
    """Construct SegTree6 with max operation"""
    seg = SegTree6(hex_max, (0, 0, 0, 0, 0, 0), data['segtree6_init_data'])
    return seg.n

@benchmark.implementation("segtree_tuple_max", "construction")
def construction_segtree_tuple_max(data):
    """Construct regular SegTree with 6-tuple max operation"""
    seg = SegTree(hex_max, (0, 0, 0, 0, 0, 0), data['tuple_values'])
    return seg.n

# Point updates operation
@benchmark.implementation("segtree6_sum", "point_updates")
def point_updates_segtree6_sum(data):
    """Point updates on SegTree6 with sum"""
    seg = SegTree6(tuple6_add, (0, 0, 0, 0, 0, 0), data['size'])
    checksum = 0
    indices = data['update_indices']
    updates = data['segtree6_updates']
    for j in range(len(indices)):
        i = indices[j]
        val = updates[j]
        seg.set(i, val)
        result = seg.get(i)
        checksum ^= result[0] ^ result[1] ^ result[2] ^ result[3] ^ result[4] ^ result[5]
    return checksum

@benchmark.implementation("segtree_tuple_sum", "point_updates")
def point_updates_segtree_tuple_sum(data):
    """Point updates on regular SegTree with 6-tuples"""
    seg = SegTree(tuple6_add, (0, 0, 0, 0, 0, 0), data['size'])
    checksum = 0
    indices = data['update_indices']
    updates = data['update_tuple_values']
    for j in range(len(indices)):
        i = indices[j]
        val = updates[j]
        seg.set(i, val)
        result = seg.get(i)
        checksum ^= result[0] ^ result[1] ^ result[2] ^ result[3] ^ result[4] ^ result[5]
    return checksum

@benchmark.implementation("segtree6_max", "point_updates")
def point_updates_segtree6_max(data):
    """Point updates on SegTree6 with max"""
    seg = SegTree6(hex_max, (0, 0, 0, 0, 0, 0), data['size'])
    checksum = 0
    indices = data['update_indices']
    updates = data['segtree6_updates']
    for j in range(len(indices)):
        i = indices[j]
        val = updates[j]
        seg.set(i, val)
        result = seg.get(i)
        checksum ^= result[0] ^ result[1] ^ result[2] ^ result[3] ^ result[4] ^ result[5]
    return checksum

@benchmark.implementation("segtree_tuple_max", "point_updates")
def point_updates_segtree_tuple_max(data):
    """Point updates on regular SegTree with 6-tuple max"""
    seg = SegTree(hex_max, (0, 0, 0, 0, 0, 0), data['size'])
    checksum = 0
    indices = data['update_indices']
    updates = data['update_tuple_values']
    for j in range(len(indices)):
        i = indices[j]
        val = updates[j]
        seg.set(i, val)
        result = seg.get(i)
        checksum ^= result[0] ^ result[1] ^ result[2] ^ result[3] ^ result[4] ^ result[5]
    return checksum

# Range queries operation
@benchmark.implementation("segtree6_sum", "range_queries")
def range_queries_segtree6_sum(data):
    """Range queries on SegTree6 with sum"""
    seg = SegTree6(tuple6_add, (0, 0, 0, 0, 0, 0), data['segtree6_init_data'])
    checksum = 0
    for l, r in data['query_ranges']:
        result = seg.prod(l, r)
        checksum ^= result[0] ^ result[1] ^ result[2] ^ result[3] ^ result[4] ^ result[5]
    return checksum

@benchmark.implementation("segtree_tuple_sum", "range_queries")
def range_queries_segtree_tuple_sum(data):
    """Range queries on regular SegTree with 6-tuples"""
    seg = SegTree(tuple6_add, (0, 0, 0, 0, 0, 0), data['tuple_values'])
    checksum = 0
    for l, r in data['query_ranges']:
        result = seg.prod(l, r)
        checksum ^= result[0] ^ result[1] ^ result[2] ^ result[3] ^ result[4] ^ result[5]
    return checksum

@benchmark.implementation("segtree6_max", "range_queries")
def range_queries_segtree6_max(data):
    """Range queries on SegTree6 with max"""
    seg = SegTree6(hex_max, (0, 0, 0, 0, 0, 0), data['segtree6_init_data'])
    checksum = 0
    for l, r in data['query_ranges']:
        result = seg.prod(l, r)
        checksum ^= result[0] ^ result[1] ^ result[2] ^ result[3] ^ result[4] ^ result[5]
    return checksum

@benchmark.implementation("segtree_tuple_max", "range_queries")
def range_queries_segtree_tuple_max(data):
    """Range queries on regular SegTree with 6-tuple max"""
    seg = SegTree(hex_max, (0, 0, 0, 0, 0, 0), data['tuple_values'])
    checksum = 0
    for l, r in data['query_ranges']:
        result = seg.prod(l, r)
        checksum ^= result[0] ^ result[1] ^ result[2] ^ result[3] ^ result[4] ^ result[5]
    return checksum

# Mixed operations (updates + queries)
@benchmark.implementation("segtree6_sum", "mixed_ops")
def mixed_ops_segtree6_sum(data):
    """Mixed updates and queries on SegTree6"""
    seg = SegTree6(tuple6_add, (0, 0, 0, 0, 0, 0), data['segtree6_init_data'])
    checksum = 0
    
    # Interleave updates and queries
    query_ranges = data['query_ranges']
    update_indices = data['update_indices']
    segtree6_updates = data['segtree6_updates']
    min_len = min(len(query_ranges), len(update_indices), len(segtree6_updates))
    
    for i in range(min_len):
        if i % 2 == 0:
            # Query
            l, r = query_ranges[i]
            result = seg.prod(l, r)
            checksum ^= result[0] ^ result[1] ^ result[2] ^ result[3] ^ result[4] ^ result[5]
        else:
            # Update
            idx = update_indices[i]
            val = segtree6_updates[i]
            seg.set(idx, val)
            result = seg.get(idx)
            checksum ^= result[0] ^ result[1] ^ result[2] ^ result[3] ^ result[4] ^ result[5]
    return checksum

@benchmark.implementation("segtree_tuple_sum", "mixed_ops")
def mixed_ops_segtree_tuple_sum(data):
    """Mixed updates and queries on regular SegTree"""
    seg = SegTree(tuple6_add, (0, 0, 0, 0, 0, 0), data['tuple_values'])
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
            checksum ^= result[0] ^ result[1] ^ result[2] ^ result[3] ^ result[4] ^ result[5]
        else:
            # Update
            idx = update_indices[i]
            val = update_tuple_values[i]
            seg.set(idx, val)
            result = seg.get(idx)
            checksum ^= result[0] ^ result[1] ^ result[2] ^ result[3] ^ result[4] ^ result[5]
    return checksum

# Max right search operation
@benchmark.implementation("segtree6_sum", "max_right_search")
def max_right_search_segtree6_sum(data):
    """Binary search using max_right on SegTree6"""
    seg = SegTree6(tuple6_add, (0, 0, 0, 0, 0, 0), data['segtree6_init_data'])
    checksum = 0
    
    # Search for positions where sum is less than threshold
    threshold = data['threshold']
    def check_predicate(x):
        return sum6_threshold_check(x, threshold)
    
    for i in range(0, data['size'], max(1, data['size'] // 100)):
        pos = seg.max_right(i, check_predicate)
        checksum ^= pos
    return checksum

@benchmark.implementation("segtree_tuple_sum", "max_right_search")
def max_right_search_segtree_tuple_sum(data):
    """Binary search using max_right on regular SegTree"""
    seg = SegTree(tuple6_add, (0, 0, 0, 0, 0, 0), data['tuple_values'])
    checksum = 0
    
    # Search for positions where sum is less than threshold
    threshold = data['threshold']
    def check_predicate(x):
        return sum6_threshold_check(x, threshold)
    
    for i in range(0, data['size'], max(1, data['size'] // 100)):
        pos = seg.max_right(i, check_predicate)
        checksum ^= pos
    return checksum

# All product operation
@benchmark.implementation("segtree6_sum", "all_prod")
def all_prod_segtree6_sum(data):
    """Get total sum using all_prod on SegTree6"""
    seg = SegTree6(tuple6_add, (0, 0, 0, 0, 0, 0), data['segtree6_init_data'])
    result = seg.all_prod()
    return result[0] ^ result[1] ^ result[2] ^ result[3] ^ result[4] ^ result[5]

@benchmark.implementation("segtree_tuple_sum", "all_prod")
def all_prod_segtree_tuple_sum(data):
    """Get total sum using all_prod on regular SegTree"""
    seg = SegTree(tuple6_add, (0, 0, 0, 0, 0, 0), data['tuple_values'])
    result = seg.all_prod()
    return result[0] ^ result[1] ^ result[2] ^ result[3] ^ result[4] ^ result[5]

@benchmark.implementation("segtree6_max", "all_prod")
def all_prod_segtree6_max(data):
    """Get global max using all_prod on SegTree6"""
    seg = SegTree6(hex_max, (0, 0, 0, 0, 0, 0), data['segtree6_init_data'])
    result = seg.all_prod()
    return result[0] ^ result[1] ^ result[2] ^ result[3] ^ result[4] ^ result[5]

@benchmark.implementation("segtree_tuple_max", "all_prod")
def all_prod_segtree_tuple_max(data):
    """Get global max using all_prod on regular SegTree"""
    seg = SegTree(hex_max, (0, 0, 0, 0, 0, 0), data['tuple_values'])
    result = seg.all_prod()
    return result[0] ^ result[1] ^ result[2] ^ result[3] ^ result[4] ^ result[5]

if __name__ == "__main__":
    # Parse command line args and run appropriate mode
    runner = benchmark.parse_args()
    runner.run()