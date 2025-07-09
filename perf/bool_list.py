#!/usr/bin/env python3
"""
Simple boolean list benchmark using the new declarative framework.
Compares different boolean data structures and operations.
"""

import random
import array
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from cp_library.perf.benchmark import Benchmark, BenchmarkConfig

# Import optional dependencies
try:
    import bitarray
    HAS_BITARRAY = True
except ImportError:
    HAS_BITARRAY = False

try:
    from cp_library.ds.wavelet.bit_array_cls import BitArray
    HAS_CUSTOM_BITARRAY = True
except ImportError:
    HAS_CUSTOM_BITARRAY = False

# Configure benchmark
config = BenchmarkConfig(
    name="bool_list",
    sizes=[100, 1000, 10000, 100000],
    operations=['access', 'count', 'sum', 'flip', 'and', 'or'],
    iterations=10,
    warmup=2,
    output_dir="./output/benchmark_results/bool_list"
)

# Create benchmark instance
benchmark = Benchmark(config)

# Data generator
@benchmark.data_generator("default")
def generate_bool_data(size: int, operation: str):
    """Generate boolean data in various formats"""
    # Generate random boolean data
    bool_list = [random.random() < 0.5 for _ in range(size)]
    int_list = [int(b) for b in bool_list]
    
    # Create different representations
    array_b = array.array('b', int_list)
    array_B = array.array('B', int_list)
    
    # Pack into bytes (8 bits per byte)
    bytes_data = bytearray((size + 7) // 8)
    for i, bit in enumerate(bool_list):
        if bit:
            bytes_data[i // 8] |= 1 << (7 - (i % 8))
    bytes_data = bytes(bytes_data)
    
    # Create bitarray if available
    bit_array = None
    if HAS_BITARRAY:
        bit_array = bitarray.bitarray(bool_list)
    
    # Create custom BitArray if available
    custom_bitarray = None
    if HAS_CUSTOM_BITARRAY:
        custom_bitarray = BitArray(int_list)
        custom_bitarray.build()
    
    # Pre-generate auxiliary data for binary operations
    other_bool = [random.random() < 0.5 for _ in range(size)]
    other_int = [int(b) for b in other_bool]
    
    return {
        'bool_list': bool_list,
        'int_list': int_list,
        'array_b': array_b,
        'array_B': array_B,
        'bytes_data': bytes_data,
        'bit_array': bit_array,
        'custom_bitarray': custom_bitarray,
        'other_bool': other_bool,
        'other_int': other_int,
        'size': size,
        'operation': operation
    }

# Access operations
@benchmark.implementation("list_bool", "access")
def access_list_bool(data):
    """Access operation on list[bool]"""
    lst = data['bool_list']
    total = 0
    access_count = min(1000, len(lst))
    step = max(1, len(lst) // access_count)
    for i in range(0, len(lst), step):
        if i < len(lst) and lst[i]:
            total += 1
    return total

@benchmark.implementation("list_int", "access")
def access_list_int(data):
    """Access operation on list[int]"""
    lst = data['int_list']
    total = 0
    access_count = min(1000, len(lst))
    step = max(1, len(lst) // access_count)
    for i in range(0, len(lst), step):
        if i < len(lst) and lst[i]:
            total += 1
    return total

@benchmark.implementation("array_b", "access")
def access_array_b(data):
    """Access operation on array.array('b')"""
    arr = data['array_b']
    total = 0
    access_count = min(1000, len(arr))
    step = max(1, len(arr) // access_count)
    for i in range(0, len(arr), step):
        if i < len(arr) and arr[i]:
            total += 1
    return total

# Count operations
@benchmark.implementation("list_bool", "count")
def count_list_bool(data):
    """Count True values in list[bool]"""
    return data['bool_list'].count(True)

@benchmark.implementation("list_int", "count")
def count_list_int(data):
    """Count True values in list[int]"""
    return sum(data['int_list'])

@benchmark.implementation("array_b", "count")
def count_array_b(data):
    """Count True values in array.array('b')"""
    return sum(data['array_b'])

# Sum operations (same as count for boolean data)
@benchmark.implementation("list_bool", "sum")
def sum_list_bool(data):
    """Sum boolean values in list[bool]"""
    return sum(data['bool_list'])

@benchmark.implementation("list_int", "sum")
def sum_list_int(data):
    """Sum boolean values in list[int]"""
    return sum(data['int_list'])

@benchmark.implementation("array_b", "sum")
def sum_array_b(data):
    """Sum boolean values in array.array('b')"""
    return sum(data['array_b'])

# Flip operations
@benchmark.implementation("list_bool", "flip")
def flip_list_bool(data):
    """Flip all boolean values in list[bool]"""
    lst = list(data['bool_list'])  # Create copy
    for i in range(len(lst)):
        lst[i] = not lst[i]
    return lst

@benchmark.implementation("list_int", "flip")
def flip_list_int(data):
    """Flip all boolean values in list[int]"""
    lst = list(data['int_list'])  # Create copy
    for i in range(len(lst)):
        lst[i] = 1 - lst[i]
    return lst

@benchmark.implementation("array_b", "flip")
def flip_array_b(data):
    """Flip all boolean values in array.array('b')"""
    arr = array.array('b', data['array_b'])  # Create copy
    for i in range(len(arr)):
        arr[i] = 1 - arr[i]
    return arr

# AND operations
@benchmark.implementation("list_bool", "and")
def and_list_bool(data):
    """AND operation on list[bool]"""
    lst = data['bool_list']
    other = data['other_bool']
    result = [False] * len(lst)
    for i in range(len(lst)):
        result[i] = lst[i] and other[i]
    return result

@benchmark.implementation("list_int", "and")
def and_list_int(data):
    """AND operation on list[int]"""
    lst = data['int_list']
    other = data['other_int']
    result = [0] * len(lst)
    for i in range(len(lst)):
        result[i] = lst[i] & other[i]
    return result

@benchmark.implementation("array_b", "and")
def and_array_b(data):
    """AND operation on array.array('b')"""
    arr = data['array_b']
    other = array.array('b', data['other_int'])
    result = array.array('b', [0] * len(arr))
    for i in range(len(arr)):
        result[i] = arr[i] & other[i]
    return result

# OR operations
@benchmark.implementation("list_bool", "or")
def or_list_bool(data):
    """OR operation on list[bool]"""
    lst = data['bool_list']
    other = data['other_bool']
    result = [False] * len(lst)
    for i in range(len(lst)):
        result[i] = lst[i] or other[i]
    return result

@benchmark.implementation("list_int", "or")
def or_list_int(data):
    """OR operation on list[int]"""
    lst = data['int_list']
    other = data['other_int']
    result = [0] * len(lst)
    for i in range(len(lst)):
        result[i] = lst[i] | other[i]
    return result

@benchmark.implementation("array_b", "or")
def or_array_b(data):
    """OR operation on array.array('b')"""
    arr = data['array_b']
    other = array.array('b', data['other_int'])
    result = array.array('b', [0] * len(arr))
    for i in range(len(arr)):
        result[i] = arr[i] | other[i]
    return result

# Add bitarray implementations if available
if HAS_BITARRAY:
    @benchmark.implementation("bitarray", ["access", "count", "sum", "flip", "and", "or"])
    def bitarray_operations(data):
        """Operations on bitarray"""
        operation = data['operation']
        bit_arr = data['bit_array']
        
        if operation == 'access':
            total = 0
            access_count = min(1000, len(bit_arr))
            step = max(1, len(bit_arr) // access_count)
            for i in range(0, len(bit_arr), step):
                if i < len(bit_arr) and bit_arr[i]:
                    total += 1
            return total
        elif operation == 'count':
            return bit_arr.count(True)
        elif operation == 'sum':
            return bit_arr.count(True)
        elif operation == 'flip':
            result = bitarray.bitarray(bit_arr)
            result.invert()
            return result
        elif operation == 'and':
            other = bitarray.bitarray(data['other_bool'])
            return bit_arr & other
        elif operation == 'or':
            other = bitarray.bitarray(data['other_bool'])
            return bit_arr | other

# Add custom BitArray implementations if available
if HAS_CUSTOM_BITARRAY:
    @benchmark.implementation("custom_bitarray", ["access", "count", "sum"])
    def custom_bitarray_operations(data):
        """Operations on custom BitArray"""
        operation = data['operation']
        bit_arr = data['custom_bitarray']
        
        if operation == 'access':
            total = 0
            access_count = min(1000, len(bit_arr))
            step = max(1, len(bit_arr) // access_count)
            for i in range(0, len(bit_arr), step):
                if i < len(bit_arr) and bit_arr[i]:
                    total += 1
            return total
        elif operation in ['count', 'sum']:
            return sum(bit_arr[i] for i in range(len(bit_arr)))

# Custom validator for boolean operations
@benchmark.validator("default")
def validate_bool_result(expected, actual):
    """Validate boolean operation results"""
    # Convert results to comparable format
    if hasattr(expected, 'tolist'):  # array.array
        expected = expected.tolist()
    if hasattr(actual, 'tolist'):  # array.array
        actual = actual.tolist()
    
    # Handle bitarray
    if hasattr(expected, 'to01'):  # bitarray
        expected = [int(b) for b in expected.to01()]
    if hasattr(actual, 'to01'):  # bitarray
        actual = [int(b) for b in actual.to01()]
    
    # Convert booleans to ints for comparison
    if isinstance(expected, list) and len(expected) > 0:
        if isinstance(expected[0], bool):
            expected = [int(b) for b in expected]
    if isinstance(actual, list) and len(actual) > 0:
        if isinstance(actual[0], bool):
            actual = [int(b) for b in actual]
    
    return expected == actual

if __name__ == "__main__":
    benchmark.run()