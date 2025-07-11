#!/usr/bin/env python3
"""
Simple Grid benchmark - minimal overhead, focused on core operations.
"""

import random
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from cp_library.perf.benchmark import Benchmark, BenchmarkConfig
from cp_library.perf.checksum import update_checksum
from cp_library.ds.grid.grid_cls import Grid

config = BenchmarkConfig(
    name="grid",
    sizes=[10000000, 1000000, 100000, 10000, 1000, 100],
    operations=['construction', 'random_access', 'row_access', 'sequential_access'],
    iterations=10,
    warmup=2,
    output_dir="./output/benchmark_results/grid"
)

benchmark = Benchmark(config)

@benchmark.data_generator("default")
def generate_data(size: int, _: str):
    H = int(size ** 0.5)
    W = size // H
    
    data = [[random.randint(1, 1000000) for _ in range(W)] for _ in range(H)]
    flat = [val for row in data for val in row]
    
    return {
        'grid': Grid(H, W, data),
        'lists': data,
        'flat': flat,
        'H': H, 'W': W,
        'coords': [(random.randint(0, H-1), random.randint(0, W-1)) for _ in range(min(100, size))]
    }

# Construction
@benchmark.implementation("grid", "construction")
def construction_grid(data):
    H, W = data['H'], data['W']
    grid = Grid(H, W, data['flat'])
    result = 0
    for i in range(H):
        for j in range(W):
            result = update_checksum(result, grid(i, j))
    return result

@benchmark.implementation("lists", "construction")
def construction_lists(data):
    H, W = data['H'], data['W']
    lists = [row[:] for row in data['lists']]
    result = 0
    for i in range(H):
        for j in range(W):
            result = update_checksum(result, lists[i][j])
    return result

@benchmark.implementation("flat", "construction")
def construction_flat(data):
    H, W = data['H'], data['W']
    flat = data['flat'][:]
    result = 0
    for i in range(H):
        for j in range(W):
            result = update_checksum(result, flat[i * W + j])
    return result

# Random access
@benchmark.implementation("grid", "random_access")
def random_access_grid(data):
    grid = data['grid']
    result = 0
    for i, j in data['coords']:
        result = update_checksum(result, grid(i, j))
    return result

@benchmark.implementation("lists", "random_access")
def random_access_lists(data):
    lists = data['lists']
    result = 0
    for i, j in data['coords']:
        result = update_checksum(result, lists[i][j])
    return result

@benchmark.implementation("flat", "random_access")
def random_access_flat(data):
    flat, W = data['flat'], data['W']
    result = 0
    for i, j in data['coords']:
        result = update_checksum(result, flat[i * W + j])
    return result

# Row access
@benchmark.implementation("grid", "row_access")
def row_access_grid(data):
    H, W = data['H'], data['W']
    grid = data['grid']
    return sum(W for i in range(H) if grid[i])  # Count logical width

@benchmark.implementation("lists", "row_access")
def row_access_lists(data):
    H = data['H']
    lists = data['lists']
    return sum(len(lists[i]) for i in range(H))

@benchmark.implementation("flat", "row_access")
def row_access_flat(data):
    H, W = data['H'], data['W']
    flat = data['flat']
    return sum(len(flat[i * W:(i + 1) * W]) for i in range(H))

# Sequential access
@benchmark.implementation("grid", "sequential_access")
def sequential_access_grid(data):
    H, W = data['H'], data['W']
    grid = data['grid']
    result = 0
    for i in range(H):
        for j in range(W):
            result = update_checksum(result, grid(i, j))
    return result

@benchmark.implementation("lists", "sequential_access")
def sequential_access_lists(data):
    H, W = data['H'], data['W']
    lists = data['lists']
    result = 0
    for i in range(H):
        for j in range(W):
            result = update_checksum(result, lists[i][j])
    return result

@benchmark.implementation("flat", "sequential_access")
def sequential_access_flat(data):
    H, W = data['H'], data['W']
    flat = data['flat']
    result = 0
    for i in range(H):
        for j in range(W):
            result = update_checksum(result, flat[i * W + j])
    return result

if __name__ == "__main__":
    # Parse command line args and run appropriate mode
    runner = benchmark.parse_args()
    runner.run()