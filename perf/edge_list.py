#!/usr/bin/env python3
"""
Simple edge list benchmark using the new declarative framework.
Much less boilerplate, easier to understand and extend.
"""

import random
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from cp_library.perf.benchmark import Benchmark, BenchmarkConfig
from cp_library.alg.graph.edge.edge_list_weighted_cls import EdgeListWeighted

# Configure benchmark
config = BenchmarkConfig(
    name="edge_list",
    sizes=[1000000, 100000, 10000, 1000, 100, 10, 1],  # Reverse order to warm up JIT
    operations=['sum_weights', 'filter', 'degree_count', 'transform', 'sort', 'construction'],
    iterations=10,
    warmup=2,
    output_dir="./output/benchmark_results/edge_list"
)

# Create benchmark instance
benchmark = Benchmark(config)

# Data generators
@benchmark.data_generator("default")
def generate_edge_data(size: int, operation: str):
    """Generate edge list data in all formats"""
    max_node = max(1, int(size ** 0.5) * 2)
    
    # Generate raw edge data
    U = [random.randint(0, max_node) for _ in range(size)]
    V = [random.randint(0, max_node) for _ in range(size)]
    W = [random.randint(1, 1000) for _ in range(size)]
    
    # Create different representations
    edges_tuple = [(U[i], V[i], W[i]) for i in range(size)]
    edge_list = EdgeListWeighted(max_node + 1, U, V, W)
    
    # Pre-initialize data for fair timing (exclude initialization)
    preinitialized = {
        'edges_tuple': list(edges_tuple),
        'edge_list': EdgeListWeighted(max_node + 1, list(U), list(V), list(W)),
        'U': list(U), 'V': list(V), 'W': list(W),
        'threshold': 500,
        'max_node': max_node,
        'degree_array': [0] * (max_node + 1)
    }
    
    return {
        'edges_tuple': edges_tuple,
        'edge_list': edge_list,
        'U': U, 'V': V, 'W': W,
        'size': size,
        'operation': operation,
        'threshold': 500,
        'max_node': max_node,
        'preinitialized': preinitialized
    }

# Construction benchmarks - all should do equivalent work
@benchmark.implementation("construct_tuple", "construction")
def construct_tuple_list(data):
    """Construct list of tuples from raw data"""
    U, V, W = data['U'], data['V'], data['W']
    return [(U[i], V[i], W[i]) for i in range(len(U))]

@benchmark.implementation("construct_edge_list_ref", "construction")
def construct_edge_list_ref(data):
    """Construct EdgeListWeighted from raw data (reference assignment)"""
    U, V, W = data['U'], data['V'], data['W']
    return EdgeListWeighted(data['max_node'] + 1, U, V, W)

@benchmark.implementation("construct_edge_list_copy", "construction")
def construct_edge_list_copy(data):
    """Construct EdgeListWeighted from copied data (fair comparison)"""
    U, V, W = data['U'], data['V'], data['W']
    return EdgeListWeighted(data['max_node'] + 1, list(U), list(V), list(W))

@benchmark.implementation("construct_separated", "construction")
def construct_separated_lists(data):
    """Create separated lists (copy data)"""
    U, V, W = data['U'], data['V'], data['W']
    return (list(U), list(V), list(W))

# Sum weights operation
@benchmark.implementation("tuple_direct", "sum_weights")
def sum_weights_tuple_direct(data):
    """Sum weights using direct tuple iteration"""
    return sum(w for u, v, w in data['edges_tuple'])

@benchmark.implementation("edge_list_iter", "sum_weights")
def sum_weights_edge_list_iter(data):
    """Sum weights using EdgeListWeighted iteration"""
    return sum(w for u, v, w in data['edge_list'])

@benchmark.implementation("edge_list_direct", "sum_weights")
def sum_weights_edge_list_direct(data):
    """Sum weights using EdgeListWeighted direct access"""
    return sum(data['edge_list'].W)

@benchmark.implementation("separated_lists", "sum_weights")
def sum_weights_separated(data):
    """Sum weights using separated lists"""
    return sum(data['W'])

# Filter operation
@benchmark.implementation("tuple_direct", "filter")
def filter_tuple_direct(data):
    """Filter edges using tuple iteration"""
    threshold = data['threshold']
    return [(u, v, w) for u, v, w in data['edges_tuple'] if w > threshold]

@benchmark.implementation("edge_list_iter", "filter")
def filter_edge_list_iter(data):
    """Filter edges using EdgeListWeighted iteration"""
    threshold = data['threshold']
    return [(u, v, w) for u, v, w in data['edge_list'] if w > threshold]

@benchmark.implementation("edge_list_direct", "filter")
def filter_edge_list_direct(data):
    """Filter edges using EdgeListWeighted direct access"""
    threshold = data['threshold']
    edge_list = data['edge_list']
    result = []
    for i in range(len(edge_list)):
        if edge_list.W[i] > threshold:
            result.append((edge_list.U[i], edge_list.V[i], edge_list.W[i]))
    return result

@benchmark.implementation("separated_lists", "filter")
def filter_separated(data):
    """Filter edges using separated lists"""
    threshold = data['threshold']
    U, V, W = data['U'], data['V'], data['W']
    return [(U[i], V[i], W[i]) for i in range(len(W)) if W[i] > threshold]

# Degree count operation
@benchmark.implementation("tuple_direct", "degree_count")
def degree_count_tuple_direct(data):
    """Count degrees using tuple iteration"""
    degree = [0] * (data['max_node'] + 1)
    for u, v, w in data['edges_tuple']:
        degree[u] += 1
    return degree

@benchmark.implementation("edge_list_iter", "degree_count")
def degree_count_edge_list_iter(data):
    """Count degrees using EdgeListWeighted iteration"""
    degree = [0] * (data['max_node'] + 1)
    for u, v, w in data['edge_list']:
        degree[u] += 1
    return degree

@benchmark.implementation("edge_list_direct", "degree_count")
def degree_count_edge_list_direct(data):
    """Count degrees using EdgeListWeighted direct access"""
    degree = [0] * (data['max_node'] + 1)
    for u in data['edge_list'].U:
        degree[u] += 1
    return degree

@benchmark.implementation("separated_lists", "degree_count")
def degree_count_separated(data):
    """Count degrees using separated lists"""
    degree = [0] * (data['max_node'] + 1)
    for u in data['U']:
        degree[u] += 1
    return degree

# Transform operation
@benchmark.implementation("tuple_direct", "transform")
def transform_tuple_direct(data):
    """Transform edges using tuple iteration"""
    return [(u, v, w * 2) for u, v, w in data['edges_tuple']]

@benchmark.implementation("edge_list_iter", "transform")
def transform_edge_list_iter(data):
    """Transform edges using EdgeListWeighted iteration"""
    return [(u, v, w * 2) for u, v, w in data['edge_list']]

@benchmark.implementation("edge_list_direct", "transform")
def transform_edge_list_direct(data):
    """Transform edges using EdgeListWeighted direct access"""
    edge_list = data['edge_list']
    return [(edge_list.U[i], edge_list.V[i], edge_list.W[i] * 2) 
            for i in range(len(edge_list))]

@benchmark.implementation("separated_lists", "transform")
def transform_separated(data):
    """Transform edges using separated lists"""
    U, V, W = data['U'], data['V'], data['W']
    return [(U[i], V[i], W[i] * 2) for i in range(len(W))]

# Sort operation
@benchmark.implementation("tuple_direct", "sort")
def sort_tuple_direct(data):
    """Sort edges using tuple list"""
    edges = list(data['edges_tuple'])
    edges.sort(key=lambda x: x[2])
    return edges

@benchmark.implementation("edge_list_sort", "sort")
def sort_edge_list_builtin(data):
    """Sort edges using EdgeListWeighted built-in sort"""
    edge_list = EdgeListWeighted(data['edge_list'].N, 
                                list(data['edge_list'].U), 
                                list(data['edge_list'].V), 
                                list(data['edge_list'].W))
    edge_list.sort()
    return edge_list

@benchmark.implementation("separated_lists", "sort")
def sort_separated(data):
    """Sort edges using separated lists"""
    U, V, W = list(data['U']), list(data['V']), list(data['W'])
    # Sort by weight using indices
    indices = sorted(range(len(W)), key=lambda i: W[i])
    return ([U[i] for i in indices], [V[i] for i in indices], [W[i] for i in indices])

# Custom validators
@benchmark.validator("sort")
def validate_sort(expected, actual):
    """Validate that sort results are equivalent"""
    # Convert both to comparable format
    if hasattr(expected, 'W'):  # EdgeListWeighted
        expected_weights = expected.W
    elif isinstance(expected, tuple):  # separated lists
        expected_weights = expected[2]
    else:  # list of tuples
        expected_weights = [w for u, v, w in expected]
    
    if hasattr(actual, 'W'):  # EdgeListWeighted
        actual_weights = actual.W
    elif isinstance(actual, tuple):  # separated lists
        actual_weights = actual[2]
    else:  # list of tuples
        actual_weights = [w for u, v, w in actual]
    
    return expected_weights == actual_weights

@benchmark.validator("construction")
def validate_construction(expected, actual):
    """Validate construction results"""
    # Just check that something was created and has the right size
    if actual is None:
        return False
    
    # Check based on type
    if isinstance(actual, list):  # tuple list
        return len(actual) > 0
    elif hasattr(actual, 'M'):  # EdgeListWeighted
        return actual.M > 0
    elif isinstance(actual, tuple):  # separated lists
        return len(actual[0]) > 0
    
    return True

if __name__ == "__main__":
    # Parse command line args and run appropriate mode
    runner = benchmark.parse_args()
    runner.run()