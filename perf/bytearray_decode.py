#!/usr/bin/env python3
"""
Benchmark comparing bytearray vs memoryview decoding performance.
Tests decoding slices from bytearray vs memoryview with different methods.
"""

import random
import string
import sys
import os
import io
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from cp_library.perf.benchmark import Benchmark, BenchmarkConfig
from cp_library.ds.list.reserve_fn import reserve

# Configure benchmark
config = BenchmarkConfig(
    name="bytearray_decode",
    sizes=[1000000, 100000, 10000, 1000, 100],  # Reverse order to warm up JIT
    operations=['small_slices', 'medium_slices', 'large_slices', 'all_slices', 'extend'],
    iterations=20,
    warmup=3,
    output_dir="./output/benchmark_results/bytearray_decode"
)

# Create benchmark instance
benchmark = Benchmark(config)

# Data generator
@benchmark.data_generator("default")
def generate_data(size: int, operation: str):
    """Generate test data for bytearray/memoryview decode operations"""
    # Generate random ASCII text with newlines
    chars = string.ascii_letters + string.digits + ' \n'
    text = ''.join(random.choice(chars) for _ in range(size))
    B = bytearray(text.encode('ascii'))
    V = memoryview(B)
    
    # Calculate proportional slice sizes based on data size
    small_max = max(1, size // 1000)  # 0.1% of size
    medium_max = max(small_max + 1, size // 100)  # 1% of size
    large_max = max(medium_max + 1, size // 10)  # 10% of size
    
    # Generate different slice sets based on operation
    num_slices = 1000
    small_slices = []
    medium_slices = []
    large_slices = []
    all_slices = []
    
    for _ in range(num_slices):
        l = random.randint(0, max(0, size - 2))
        remaining = size - l
        
        # Small slices
        if remaining > 0:
            max_small_len = min(small_max, remaining)
            if max_small_len > 0:
                slice_len = random.randint(1, max_small_len)
                small_slices.append((l, l + slice_len))
        
        # Medium slices
        if remaining > small_max and medium_max > small_max:
            max_medium_len = min(medium_max, remaining)
            if max_medium_len > small_max:
                slice_len = random.randint(small_max + 1, max_medium_len)
                medium_slices.append((l, l + slice_len))
        
        # Large slices
        if remaining > medium_max and large_max > medium_max:
            max_large_len = min(large_max, remaining)
            if max_large_len > medium_max:
                slice_len = random.randint(medium_max + 1, max_large_len)
                large_slices.append((l, l + slice_len))
        
        # All slices - mixed sizes
        if remaining > 0:
            slice_type = random.random()
            if slice_type < 0.33:
                # Small slice
                max_len = min(small_max, remaining)
                if max_len > 0:
                    slice_len = random.randint(1, max_len)
                else:
                    slice_len = 1
            elif slice_type < 0.66:
                # Medium slice
                if remaining > small_max and medium_max > small_max:
                    max_len = min(medium_max, remaining)
                    slice_len = random.randint(small_max + 1, max_len)
                else:
                    # Fall back to small slice
                    max_len = min(small_max, remaining)
                    slice_len = random.randint(1, max(1, max_len))
            else:
                # Large slice
                if remaining > medium_max and large_max > medium_max:
                    max_len = min(large_max, remaining)
                    slice_len = random.randint(medium_max + 1, max_len)
                else:
                    # Fall back to whatever size is available
                    slice_len = random.randint(1, min(large_max, remaining))
            all_slices.append((l, l + slice_len))
    
    # Create BytesIO
    bio = io.BytesIO(B)
    
    # Return appropriate slices based on operation
    if operation == 'small_slices':
        slices = small_slices
    elif operation == 'medium_slices':
        slices = medium_slices
    elif operation == 'large_slices':
        slices = large_slices
    elif operation == 'all_slices':
        slices = all_slices
    else:
        slices = []  # No slices needed for extend operations
    
    # For extend operations, generate data chunks
    if operation == 'extend':
        # Generate chunks to extend
        num_chunks = 1000
        chunks = []
        chunk_sizes = [1, 10, 100, 1000]  # Various chunk sizes
        
        for _ in range(num_chunks):
            chunk_size = random.choice(chunk_sizes)
            chunk_text = ''.join(random.choice(chars) for _ in range(chunk_size))
            chunk_bytes = chunk_text.encode('ascii')
            chunks.append(chunk_bytes)
        
        return {
            'bytearray': B,
            'memoryview': V,
            'bytesio': bio,
            'slices': slices,
            'chunks': chunks,
            'size': size,
            'operation': operation
        }
    
    return {
        'bytearray': B,
        'memoryview': V,
        'bytesio': bio,
        'slices': slices,
        'size': size,
        'operation': operation
    }

# Memoryview bytes implementations
@benchmark.implementation("memoryview_bytes", ['small_slices', 'medium_slices', 'large_slices', 'all_slices'])
def memoryview_bytes_decode(data):
    """Decode slices using memoryview[l:r].tobytes().decode()"""
    V = data['memoryview']
    slices = data['slices']
    checksum = 0
    
    for l, r in slices:
        s = V[l:r].tobytes().decode('ascii', 'ignore')
        checksum += len(s)  # Use length for checksum
    
    return checksum

# Bytearray implementations
@benchmark.implementation("bytearray", ['small_slices', 'medium_slices', 'large_slices', 'all_slices'])
def bytearray_decode(data):
    """Decode slices using bytearray[l:r].decode()"""
    B = data['bytearray']
    slices = data['slices']
    checksum = 0
    
    for l, r in slices:
        s = B[l:r].decode('ascii', 'ignore')
        checksum += len(s)  # Use length for checksum
    
    return checksum

# Memoryview implementations
@benchmark.implementation("memoryview", ['small_slices', 'medium_slices', 'large_slices', 'all_slices'])
def memoryview_decode(data):
    """Decode slices using str(memoryview[l:r], encoding)"""
    V = data['memoryview']
    slices = data['slices']
    checksum = 0
    
    for l, r in slices:
        s = str(V[l:r], 'ascii', 'ignore')
        checksum += len(s)  # Use length for checksum
    
    return checksum

# BytesIO implementations
@benchmark.implementation("bytesio", ['small_slices', 'medium_slices', 'large_slices', 'all_slices'])
def bytesio_decode(data):
    """Decode slices using BytesIO seek/read operations"""
    bio = data['bytesio']
    slices = data['slices']
    checksum = 0
    
    for l, r in slices:
        bio.seek(l)
        s = bio.read(r - l).decode('ascii', 'ignore')
        checksum += len(s)  # Use length for checksum
    
    return checksum

# Setup functions for extend operations
@benchmark.setup("bytearray", ["extend"])
def setup_bytearray_extend(data):
    """Pre-initialize bytearray for extend operations"""
    prepared = data.copy()
    prepared['bytearray'] = bytearray()
    return prepared

@benchmark.setup("bytesio", ["extend"]) 
def setup_bytesio_extend(data):
    """Pre-initialize BytesIO for extend operations"""
    prepared = data.copy()
    prepared['bytesio'] = io.BytesIO()
    return prepared

# Extend implementations
@benchmark.implementation("bytearray", "extend")
def bytearray_extend(data):
    """Extend bytearray with chunks"""
    B = data['bytearray']
    chunks = data['chunks']
    
    for chunk in chunks:
        B.extend(chunk)
    
    return len(B)

@benchmark.implementation("bytesio", "extend")
def bytesio_extend(data):
    """Write chunks to BytesIO"""
    bio = data['bytesio']
    chunks = data['chunks']
    
    for chunk in chunks:
        bio.write(chunk)
    
    return bio.tell()

if __name__ == "__main__":
    # Parse command line args and run appropriate mode
    runner = benchmark.parse_args()
    
    runner.run()