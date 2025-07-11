#!/usr/bin/env python3
"""
Comprehensive benchmark comparing modular arithmetic approaches on lists:
1. Plain int list with manual modular operations
2. mlist_cls (optimized modular list)
3. List of mint_cls (modular integers)

Tests various operations to provide fair comparison across different use cases.
"""

import random
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from cp_library.perf.benchmark import Benchmark, BenchmarkConfig
from cp_library.math.mod.mlist_cls import mlist
from cp_library.math.mod.mint_ntt_cls import mint

# Setup modular arithmetic with a common modulus
MOD = 998244353
mint.set_mod(MOD)

# Configure benchmark
config = BenchmarkConfig(
    name="mlist",
    sizes=[1000000, 100000, 10000, 1000, 100, 10, 1],  # Reverse order to warm up JIT
    operations=['construction', 'addition', 'multiplication', 'mixed_ops', 'elementwise_mul', 'sum_all', 'conv'],
    iterations=10,
    warmup=3,
    output_dir="./output/benchmark_results/mlist"
)

# Create benchmark instance
benchmark = Benchmark(config)

# Data generators
@benchmark.data_generator("default")
def generate_modular_data(size: int, operation: str):
    """Generate test data for modular arithmetic operations"""
    # Generate two random lists for operations
    list1 = [random.randint(1, MOD-1) for _ in range(size)]
    list2 = [random.randint(1, MOD-1) for _ in range(size)]
    
    # Pre-initialize data for fair timing (exclude initialization overhead)
    preinitialized = {
        'list1_copy': list(list1),
        'list2_copy': list(list2),
        'mlist1': mlist(list(list1)),
        'mlist2': mlist(list(list2)),
        'mint_list1': [mint(x) for x in list1],
        'mint_list2': [mint(x) for x in list2],
        'result_buffer': [0] * size,
        'mlist_result': mlist(size),
        'constant': 12345,
        'mint_constant': mint(12345)
    }
    
    return {
        'list1': list1,
        'list2': list2,
        'size': size,
        'operation': operation,
        'mod': MOD,
        'preinitialized': preinitialized
    }

# Construction operation
@benchmark.implementation("int_list", "construction")
def construction_int_list(data):
    """Construct int list from raw data"""
    list1 = list(data['list1'])
    list2 = list(data['list2'])
    checksum = 0
    for x in list1:
        checksum ^= x
    for x in list2:
        checksum ^= x
    return checksum

@benchmark.implementation("mlist", "construction")
def construction_mlist(data):
    """Construct mlist from raw data"""
    mlist1 = mlist(data['list1'])
    mlist2 = mlist(data['list2'])
    checksum = 0
    for x in mlist1.data:
        checksum ^= x
    for x in mlist2.data:
        checksum ^= x
    return checksum

@benchmark.implementation("mint_list", "construction")
def construction_mint_list(data):
    """Construct mint list from raw data"""
    mint_list1 = [mint(x) for x in data['list1']]
    mint_list2 = [mint(x) for x in data['list2']]
    checksum = 0
    for x in mint_list1:
        checksum ^= x
    for x in mint_list2:
        checksum ^= x
    return checksum

# Addition operation
@benchmark.implementation("int_list", "addition")
def addition_int_list(data):
    """Element-wise addition with manual modulo"""
    pre = data['preinitialized']
    list1, list2, mod = pre['list1_copy'], pre['list2_copy'], data['mod']
    checksum = 0
    for i in range(data['size']):
        checksum ^= (list1[i] + list2[i]) % mod
    return checksum

@benchmark.implementation("mlist", "addition")
def addition_mlist(data):
    """Element-wise addition using mlist"""
    pre = data['preinitialized']
    list1, list2 = pre['mlist1'], pre['mlist2']
    checksum = 0
    for i in range(data['size']):
        checksum ^= list1[i] + list2[i]
    return checksum

@benchmark.implementation("mint_list", "addition")
def addition_mint_list(data):
    """Element-wise addition using mint list"""
    pre = data['preinitialized']
    list1, list2 = pre['mint_list1'], pre['mint_list2']
    checksum = 0
    for i in range(data['size']):
        checksum ^= list1[i] + list2[i]
    return checksum

# Multiplication operation
@benchmark.implementation("int_list", "multiplication")
def multiplication_int_list(data):
    """Element-wise multiplication with manual modulo"""
    pre = data['preinitialized']
    list1, list2, mod = pre['list1_copy'], pre['list2_copy'], data['mod']
    checksum = 0
    for i in range(data['size']):
        checksum ^= (list1[i] * list2[i]) % mod
    return checksum

@benchmark.implementation("mlist", "multiplication")
def multiplication_mlist(data):
    """Element-wise multiplication using mlist"""
    pre = data['preinitialized']
    list1, list2 = pre['mlist1'], pre['mlist2']
    checksum = 0
    for i in range(data['size']):
        checksum ^= list1[i] * list2[i]
    return checksum

@benchmark.implementation("mint_list", "multiplication")
def multiplication_mint_list(data):
    """Element-wise multiplication using mint list"""
    pre = data['preinitialized']
    list1, list2 = pre['mint_list1'], pre['mint_list2']
    checksum = 0
    for i in range(data['size']):
        checksum ^= list1[i] * list2[i]
    return checksum

# Mixed operations
@benchmark.implementation("int_list", "mixed_ops")
def mixed_ops_int_list(data):
    """Mix of addition, multiplication, and subtraction"""
    pre = data['preinitialized']
    list1, list2, mod = pre['list1_copy'], pre['list2_copy'], data['mod']
    checksum = 0
    for i in range(data['size']):
        if i % 3 == 0:
            checksum ^= (list1[i] + list2[i]) % mod
        elif i % 3 == 1:
            checksum ^= (list1[i] * list2[i]) % mod
        else:
            checksum ^= (list1[i] - list2[i]) % mod
    return checksum

@benchmark.implementation("mlist", "mixed_ops")
def mixed_ops_mlist(data):
    """Mix of operations using mlist"""
    pre = data['preinitialized']
    list1, list2 = pre['mlist1'], pre['mlist2']
    checksum = 0
    for i in range(data['size']):
        if i % 3 == 0:
            checksum ^= list1[i] + list2[i]
        elif i % 3 == 1:
            checksum ^= list1[i] * list2[i]
        else:
            checksum ^= list1[i] - list2[i]
    return checksum

@benchmark.implementation("mint_list", "mixed_ops")
def mixed_ops_mint_list(data):
    """Mix of operations using mint list"""
    pre = data['preinitialized']
    list1, list2 = pre['mint_list1'], pre['mint_list2']
    checksum = 0
    for i in range(data['size']):
        if i % 3 == 0:
            checksum ^= list1[i] + list2[i]
        elif i % 3 == 1:
            checksum ^= list1[i] * list2[i]
        else:
            checksum ^= list1[i] - list2[i]
    return checksum


@benchmark.implementation("int_list_e", "mixed_ops")
def mixed_ops_int_list(data):
    """Mix of addition, multiplication, and subtraction"""
    pre = data['preinitialized']
    list1, list2, mod = pre['list1_copy'], pre['list2_copy'], data['mod']
    checksum = 0
    for i, x in enumerate(list1):
        if i % 3 == 0:
            checksum ^= (x + list2[i]) % mod
        elif i % 3 == 1:
            checksum ^= (x * list2[i]) % mod
        else:
            checksum ^= (x - list2[i]) % mod
    return checksum

@benchmark.implementation("mlist_e", "mixed_ops")
def mixed_ops_mlist(data):
    """Mix of operations using mlist"""
    pre = data['preinitialized']
    list1, list2 = pre['mlist1'], pre['mlist2']
    checksum = 0
    for i, x in enumerate(list1):
        if i % 3 == 0:
            checksum ^= x + list2[i]
        elif i % 3 == 1:
            checksum ^= x * list2[i]
        else:
            checksum ^= x - list2[i]
    return checksum

@benchmark.implementation("mint_list_e", "mixed_ops")
def mixed_ops_mint_list(data):
    """Mix of operations using mint list"""
    pre = data['preinitialized']
    list1, list2 = pre['mint_list1'], pre['mint_list2']
    checksum = 0
    for i, x in enumerate(list1):
        if i % 3 == 0:
            checksum ^= x + list2[i]
        elif i % 3 == 1:
            checksum ^= x * list2[i]
        else:
            checksum ^= x - list2[i]
    return checksum

# Element-wise multiplication by constant
@benchmark.implementation("int_list", "elementwise_mul")
def elementwise_mul_int_list(data):
    """Multiply each element by a constant"""
    pre = data['preinitialized']
    list1, mod, constant = pre['list1_copy'], data['mod'], pre['constant']
    checksum = 0
    for x in list1:
        checksum ^= (x * constant) % mod
    return checksum

@benchmark.implementation("mlist", "elementwise_mul")
def elementwise_mul_mlist(data):
    """Multiply each element by a constant using mlist"""
    pre = data['preinitialized']
    list1, constant = pre['mlist1'], pre['mint_constant']
    checksum = 0
    for x in list1:
        checksum ^= x * constant
    return checksum

@benchmark.implementation("mint_list", "elementwise_mul")
def elementwise_mul_mint_list(data):
    """Multiply each element by a constant using mint list"""
    pre = data['preinitialized']
    list1, constant = pre['mint_list1'], pre['mint_constant']
    checksum = 0
    for x in list1:
        result = x * constant
        checksum ^= result
    return checksum

# Sum all elements
@benchmark.implementation("int_list", "sum_all")
def sum_all_int_list(data):
    """Sum all elements"""
    pre = data['preinitialized']
    list1, mod = pre['list1_copy'], data['mod']
    result = 0
    for x in list1:
        result = (result + x) % mod
    return result

@benchmark.implementation("mlist", "sum_all")
def sum_all_mlist(data):
    """Sum all elements using mlist"""
    pre = data['preinitialized']
    list1 = pre['mlist1']
    result = mint(0)
    for x in list1:
        result = result + x
    return int(result)

@benchmark.implementation("mint_list", "sum_all")
def sum_all_mint_list(data):
    """Sum all elements using mint list"""
    pre = data['preinitialized']
    list1 = pre['mint_list1']
    result = mint(0)
    for x in list1:
        result = result + x
    return int(result)

# Convolution operation
@benchmark.implementation("int_list", "conv")
def conv_int_list(data):
    """Convolution using mint.ntt.conv with int lists"""
    pre = data['preinitialized']
    list1, list2 = pre['list1_copy'], pre['list2_copy']
    # Use mint.ntt.conv for convolution
    result = mint.ntt.conv(list1, list2, len(list1) + len(list2) - 1)
    checksum = 0
    for x in result:
        checksum ^= x
    return checksum

@benchmark.implementation("mlist", "conv")
def conv_mlist(data):
    """Convolution using mlist.conv method"""
    pre = data['preinitialized']
    mlist1, mlist2 = pre['mlist1'], pre['mlist2']
    # Use mlist.conv method
    result = mlist1.conv(mlist2, len(mlist1) + len(mlist2) - 1)
    checksum = 0
    for x in result.data:
        checksum ^= x
    return checksum

@benchmark.implementation("mint_list", "conv")
def conv_mint_list(data):
    """Convolution using mint.ntt.conv with mint lists"""
    pre = data['preinitialized']
    mint_list1, mint_list2 = pre['mint_list1'], pre['mint_list2']
    # Convert to int lists, convolve, convert back
    int_list1 = [int(x) for x in mint_list1]
    int_list2 = [int(x) for x in mint_list2]
    result_ints = mint.ntt.conv(int_list1, int_list2, len(int_list1) + len(int_list2) - 1)
    result = [mint(x) for x in result_ints]
    checksum = 0
    for x in result:
        checksum ^= x
    return checksum

@benchmark.implementation("mint_list_direct", "conv")
def conv_mint_list_direct(data):
    """Convolution using mint.ntt.conv directly with mint lists"""
    pre = data['preinitialized']
    mint_list1, mint_list2 = pre['mint_list1'], pre['mint_list2']
    result = mint.ntt.conv(mint_list1, mint_list2, len(mint_list1) + len(mint_list2) - 1)
    checksum = 0
    for x in result:
        checksum ^= x
    return checksum

# Custom validator for modular arithmetic results (now using XOR checksums)
@benchmark.validator("default")
def validate_modular_result(expected, actual):
    """Validate modular arithmetic results using XOR checksums"""
    try:
        # Compare XOR checksums directly
        return int(expected) == int(actual)
    except Exception:
        return False

if __name__ == "__main__":
    # Parse command line args and run appropriate mode
    runner = benchmark.parse_args()
    runner.run()