"""
Comprehensive benchmark for boolean list representations using cp_library.perf framework.

Compares:
- list[bool]
- list[int] (0/1)
- array.array('b') - signed char
- array.array('B') - unsigned char  
- bitarray (if available)
"""

from cp_library.perf.benchmark import Benchmark, BenchmarkConfig, TestCase
from cp_library.perf.generators import DataGenerator
from typing import Dict, List, Any, Callable, Tuple
import time
import array
import random
import statistics

try:
    import bitarray
    HAS_BITARRAY = True
except ImportError:
    HAS_BITARRAY = False
    print("Note: bitarray module not available. Install with: pip install bitarray")

try:
    import sys
    import os
    # Add the cp_library path to import the local version
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
    from cp_library.ds.wavelet.bit_array_cls import BitArray
    HAS_CUSTOM_BITARRAY = True
except ImportError as e:
    HAS_CUSTOM_BITARRAY = False
    print(f"Note: Custom BitArray not available: {e}")


class BooleanDataGenerator(DataGenerator):
    """Generate boolean test data in various formats"""
    
    def __init__(self, true_probability: float = 0.5):
        self.true_probability = true_probability
    
    def generate(self, size: int, **params) -> Dict[str, Any]:
        """Generate test data with all formats needed"""
        bool_list = [random.random() < self.true_probability for _ in range(size)]
        int_list = [int(b) for b in bool_list]
        
        return {
            'bool_list': bool_list,
            'int_list': int_list,
            'size': size,
            'operation': params.get('operation', 'access')
        }


class BooleanListBenchmark(Benchmark):
    """Benchmark boolean list operations with fair timing"""
    
    def __init__(self, config: BenchmarkConfig):
        super().__init__(config)
        self.exclude_init = getattr(config, 'exclude_init', False)
        self.preinitialized = {}
    
    def generate_test_cases(self, param_grid: Dict[str, List[Any]]) -> List[TestCase]:
        """Generate test cases and optionally pre-initialize data structures"""
        test_cases = []
        generator = BooleanDataGenerator()
        
        for size in param_grid.get('size', [1000]):
            for operation in param_grid.get('operation', ['access']):
                # Generate base data
                test_data = generator.generate(size, operation=operation)
                
                # Pre-initialize if excluding init time
                if self.exclude_init:
                    test_key = f"{operation}_{size}"
                    self.preinitialized[test_key] = self._create_structures(test_data)
                    test_data['test_key'] = test_key
                
                test_cases.append(TestCase(
                    name=f"{operation}_size_{size}",
                    params={'size': size, 'operation': operation},
                    data=test_data
                ))
        
        return test_cases
    
    def _create_structures(self, test_data: Dict[str, Any]) -> Dict[str, Any]:
        """Pre-create data structures and auxiliary data for fair timing"""
        size = test_data['size']
        
        # Generate auxiliary data for binary operations using native types
        other_bool = [random.random() > 0.5 for _ in range(size)]
        other_int = [1 if b else 0 for b in other_bool]  # Native 1/0
        
        # Convert bool list to bytes (pack 8 bools per byte)
        bytes_data = bytearray((size + 7) // 8)
        for i, bit in enumerate(test_data['bool_list']):
            if bit:
                bytes_data[i // 8] |= 1 << (7 - (i % 8))  # MSB first
        
        # Convert other_bool to bytes for binary operations
        other_bytes_data = bytearray((size + 7) // 8)
        for i, bit in enumerate(other_bool):
            if bit:
                other_bytes_data[i // 8] |= 1 << (7 - (i % 8))
        
        structures = {
            'list_bool': list(test_data['bool_list']),
            'list_int': list(test_data['int_list']),
            'array_b': array.array('b', test_data['int_list']),
            'array_B': array.array('B', test_data['int_list']),
            'bytes': bytes(bytes_data),
            # Pre-generated auxiliary data
            'other_bool': other_bool,
            'other_int': other_int,
            'other_array_b': array.array('b', other_int),
            'other_array_B': array.array('B', other_int),
            'other_bytes': bytes(other_bytes_data),
        }
        
        if HAS_BITARRAY:
            # Use frombytes for better performance
            ba = bitarray.bitarray()
            ba.frombytes(bytes_data)
            # Trim to exact size since frombytes might add extra bits
            if len(ba) > size:
                ba = ba[:size]
            structures['bitarray'] = ba
            
            # Pre-create auxiliary bitarray using frombytes
            other_ba = bitarray.bitarray()
            other_ba.frombytes(other_bytes_data)
            if len(other_ba) > size:
                other_ba = other_ba[:size]
            structures['other_bitarray'] = other_ba
        
        if HAS_CUSTOM_BITARRAY:
            # Create custom BitArray from int list (not bytes - keep original approach)
            custom_ba = BitArray(test_data['int_list'])
            custom_ba.build()  # Build the auxiliary data structures
            structures['custom_bitarray'] = custom_ba
            
            # Pre-create auxiliary custom bitarray
            other_custom_ba = BitArray(other_int)
            other_custom_ba.build()
            structures['other_custom_bitarray'] = other_custom_ba
        
        return structures
    
    def get_implementations(self) -> Dict[str, Callable]:
        """Return implementation functions"""
        implementations = {
            'list_bool': self._list_bool_ops,
            'list_int': self._list_int_ops,
            'array_b': self._array_b_ops,
            'array_B': self._array_B_ops,
            'bytes': self._bytes_ops,
        }
        
        if HAS_BITARRAY:
            implementations['bitarray'] = self._bitarray_ops
        
        if HAS_CUSTOM_BITARRAY:
            implementations['custom_bitarray'] = self._custom_bitarray_ops
        
        return implementations
    
    def validate_result(self, expected: Any, actual: Any) -> bool:
        """Custom validation - just verify we got a result"""
        return actual is not None
    
    def measure_time(self, func: Callable, test_data: Dict) -> Tuple[Any, float]:
        """Custom timing to handle initialization exclusion"""
        operation = test_data['operation']
        size = test_data['size']
        
        # Adjust iterations based on operation complexity
        if operation in ['and', 'or', 'xor'] and size > 10000:
            iterations = max(1, 100 // (size // 10000))
        elif operation == 'access':
            iterations = 10
        elif operation == 'count' and size > 100000:
            iterations = 5
        else:
            iterations = self.config.iterations
        
        # Warmup
        for _ in range(min(self.config.warmup, 2)):
            func(**test_data)
        
        # Time measurement
        start = time.perf_counter()
        for _ in range(iterations):
            result = func(**test_data)
        elapsed_ms = (time.perf_counter() - start) * 1000 / iterations
        
        return result, elapsed_ms
    
    # Implementation methods
    def _list_bool_ops(self, bool_list: List[bool], int_list: List[int], 
                       size: int, operation: str, test_key: str = None, **kwargs):
        """Operations on list[bool]"""
        # Get data (pre-initialized or create new)
        if self.exclude_init and test_key:
            lst = self.preinitialized[test_key]['list_bool'].copy()
        else:
            lst = list(bool_list)
        
        if operation == 'access':
            # Use sequential access for better PyPy performance
            total = 0
            access_count = min(1000, size)
            step = max(1, size // access_count)
            for i in range(0, size, step):
                if i < size and lst[i]:
                    total += 1
            return total
        
        elif operation == 'count':
            return lst.count(True)
        
        elif operation == 'sum':
            return sum(lst)
        
        elif operation == 'flip':
            for i in range(len(lst)):
                lst[i] = not lst[i]
            return lst
        
        elif operation == 'and':
            if self.exclude_init and test_key:
                other = self.preinitialized[test_key]['other_bool']
            else:
                other = [random.random() > 0.5 for _ in range(size)]
            # Use manual loop for PyPy optimization
            result = [False] * size  # Pre-allocate
            for i in range(size):
                result[i] = lst[i] and other[i]
            return result
        
        elif operation == 'or':
            if self.exclude_init and test_key:
                other = self.preinitialized[test_key]['other_bool']
            else:
                other = [random.random() > 0.5 for _ in range(size)]
            # Use manual loop for PyPy optimization
            result = [False] * size  # Pre-allocate
            for i in range(size):
                result[i] = lst[i] or other[i]
            return result
        
        elif operation == 'slice':
            slices = []
            slice_size = min(100, size // 10)
            for _ in range(100):
                start = random.randint(0, max(0, size - slice_size))
                slices.append(lst[start:start + slice_size])
            return slices
    
    def _list_int_ops(self, bool_list: List[bool], int_list: List[int], 
                      size: int, operation: str, test_key: str = None, **kwargs):
        """Operations on list[int]"""
        if self.exclude_init and test_key:
            lst = self.preinitialized[test_key]['list_int'].copy()
        else:
            lst = list(int_list)
        
        if operation == 'access':
            # Use sequential access for better PyPy performance
            total = 0
            access_count = min(1000, size)
            step = max(1, size // access_count)
            for i in range(0, size, step):
                if i < size and lst[i]:
                    total += 1
            return total
        
        elif operation == 'count':
            return lst.count(1)
        
        elif operation == 'sum':
            return sum(lst)
        
        elif operation == 'flip':
            for i in range(len(lst)):
                lst[i] = 1 ^ lst[i]
            return lst
        
        elif operation == 'and':
            if self.exclude_init and test_key:
                other = self.preinitialized[test_key]['other_int']
            else:
                other = [1 if random.random() > 0.5 else 0 for _ in range(size)]  # Native 1/0
            # Use manual loop for PyPy optimization
            result = [0] * size  # Pre-allocate
            for i in range(size):
                result[i] = lst[i] & other[i]
            return result
        
        elif operation == 'or':
            if self.exclude_init and test_key:
                other = self.preinitialized[test_key]['other_int']
            else:
                other = [1 if random.random() > 0.5 else 0 for _ in range(size)]  # Native 1/0
            # Use manual loop for PyPy optimization
            result = [0] * size  # Pre-allocate
            for i in range(size):
                result[i] = lst[i] | other[i]
            return result
        
        elif operation == 'slice':
            slices = []
            slice_size = min(100, size // 10)
            for _ in range(100):
                start = random.randint(0, max(0, size - slice_size))
                slices.append(lst[start:start + slice_size])
            return slices
    
    def _array_b_ops(self, bool_list: List[bool], int_list: List[int], 
                     size: int, operation: str, test_key: str = None, **kwargs):
        """Operations on array.array('b')"""
        if self.exclude_init and test_key:
            arr = self.preinitialized[test_key]['array_b'][:]
        else:
            arr = array.array('b', int_list)
        
        if operation == 'access':
            # Use sequential access for better PyPy performance
            total = 0
            access_count = min(1000, size)
            step = max(1, size // access_count)
            for i in range(0, size, step):
                if i < size and arr[i]:
                    total += 1
            return total
        
        elif operation == 'count':
            return arr.count(1)
        
        elif operation == 'sum':
            return sum(arr)
        
        elif operation == 'flip':
            for i in range(len(arr)):
                arr[i] = 1 ^ arr[i]
            return arr
        
        elif operation == 'and':
            if self.exclude_init and test_key:
                other = self.preinitialized[test_key]['other_array_b']
            else:
                other = array.array('b', [1 if random.random() > 0.5 else 0 for _ in range(size)])
            # Use manual loop for PyPy optimization
            result = array.array('b', [0] * size)  # Pre-allocate
            for i in range(size):
                result[i] = arr[i] & other[i]
            return result
        
        elif operation == 'or':
            if self.exclude_init and test_key:
                other = self.preinitialized[test_key]['other_array_b']
            else:
                other = array.array('b', [1 if random.random() > 0.5 else 0 for _ in range(size)])
            # Use manual loop for PyPy optimization
            result = array.array('b', [0] * size)  # Pre-allocate
            for i in range(size):
                result[i] = arr[i] | other[i]
            return result
        
        elif operation == 'slice':
            slices = []
            slice_size = min(100, size // 10)
            for _ in range(100):
                start = random.randint(0, max(0, size - slice_size))
                slices.append(arr[start:start + slice_size])
            return slices
    
    def _array_B_ops(self, bool_list: List[bool], int_list: List[int], 
                     size: int, operation: str, test_key: str = None, **kwargs):
        """Operations on array.array('B')"""
        if self.exclude_init and test_key:
            arr = self.preinitialized[test_key]['array_B'][:]
        else:
            arr = array.array('B', int_list)
        
        if operation == 'access':
            # Use sequential access for better PyPy performance
            total = 0
            access_count = min(1000, size)
            step = max(1, size // access_count)
            for i in range(0, size, step):
                if i < size and arr[i]:
                    total += 1
            return total
        
        elif operation == 'count':
            return arr.count(1)
        
        elif operation == 'sum':
            return sum(arr)
        
        elif operation == 'flip':
            for i in range(len(arr)):
                arr[i] = 1 - arr[i]
            return arr
        
        elif operation == 'and':
            if self.exclude_init and test_key:
                other = self.preinitialized[test_key]['other_array_B']
            else:
                other = array.array('B', [1 if random.random() > 0.5 else 0 for _ in range(size)])
            # Use manual loop for PyPy optimization
            result = array.array('B', [0] * size)  # Pre-allocate
            for i in range(size):
                result[i] = arr[i] & other[i]
            return result
        
        elif operation == 'or':
            if self.exclude_init and test_key:
                other = self.preinitialized[test_key]['other_array_B']
            else:
                other = array.array('B', [1 if random.random() > 0.5 else 0 for _ in range(size)])
            # Use manual loop for PyPy optimization
            result = array.array('B', [0] * size)  # Pre-allocate
            for i in range(size):
                result[i] = arr[i] | other[i]
            return result
        
        elif operation == 'slice':
            slices = []
            slice_size = min(100, size // 10)
            for _ in range(100):
                start = random.randint(0, max(0, size - slice_size))
                slices.append(arr[start:start + slice_size])
            return slices
    
    def _bitarray_ops(self, bool_list: List[bool], int_list: List[int], 
                      size: int, operation: str, test_key: str = None, **kwargs):
        """Operations on bitarray"""
        if self.exclude_init and test_key:
            ba = self.preinitialized[test_key]['bitarray'].copy()
        else:
            ba = bitarray.bitarray(int_list)
        
        if operation == 'access':
            # Use sequential access for better PyPy performance
            total = 0
            access_count = min(1000, size)
            step = max(1, size // access_count)
            for i in range(0, size, step):
                if i < size and ba[i]:
                    total += 1
            return total
        
        elif operation == 'count':
            return ba.count(1)
        
        elif operation == 'sum':
            return ba.count(1)  # Same as count for bitarray
        
        elif operation == 'flip':
            ba.invert()
            return ba
        
        elif operation == 'and':
            if self.exclude_init and test_key:
                other = self.preinitialized[test_key]['other_bitarray']
            else:
                other = bitarray.bitarray([random.random() > 0.5 for _ in range(size)])
            return ba & other
        
        elif operation == 'or':
            if self.exclude_init and test_key:
                other = self.preinitialized[test_key]['other_bitarray']
            else:
                other = bitarray.bitarray([random.random() > 0.5 for _ in range(size)])
            return ba | other
        
        elif operation == 'slice':
            slices = []
            slice_size = min(100, size // 10)
            for _ in range(100):
                start = random.randint(0, max(0, size - slice_size))
                slices.append(ba[start:start + slice_size])
            return slices
    
    def _bytes_ops(self, bool_list: List[bool], int_list: List[int], 
                   size: int, operation: str, test_key: str = None, **kwargs):
        """Operations on bytes (packed bits)"""
        if self.exclude_init and test_key:
            data = self.preinitialized[test_key]['bytes']
        else:
            # Pack bool list into bytes
            data = bytearray((size + 7) // 8)
            for i, bit in enumerate(bool_list):
                if bit:
                    data[i // 8] |= 1 << (7 - (i % 8))  # MSB first
            data = bytes(data)
        
        if operation == 'access':
            # Use sequential access for better PyPy performance
            total = 0
            access_count = min(1000, size)
            step = max(1, size // access_count)
            for i in range(0, size, step):
                if i < size:
                    byte_idx = i // 8
                    bit_idx = i % 8
                    if byte_idx < len(data) and data[byte_idx] & (1 << (7 - bit_idx)):
                        total += 1
            return total
        
        elif operation == 'count':
            # Count all set bits in the bytes
            count = 0
            for i in range(size):
                byte_idx = i // 8
                bit_idx = i % 8
                if byte_idx < len(data) and data[byte_idx] & (1 << (7 - bit_idx)):
                    count += 1
            return count
        
        elif operation == 'sum':
            return self._bytes_ops(bool_list, int_list, size, 'count', test_key, **kwargs)
        
        elif operation == 'flip':
            # Flip all bits in bytes
            flipped = bytearray(len(data))
            for i, byte_val in enumerate(data):
                flipped[i] = byte_val ^ 0xFF  # Flip all 8 bits
            # Handle partial last byte if size is not multiple of 8
            if size % 8 != 0:
                last_byte_mask = (1 << (8 - (size % 8))) - 1
                flipped[-1] &= ~last_byte_mask  # Clear unused bits
            return bytes(flipped)
        
        elif operation == 'and':
            if self.exclude_init and test_key:
                other_data = self.preinitialized[test_key]['other_bytes']
            else:
                other_data = bytearray((size + 7) // 8)
                for i in range(size):
                    if random.random() > 0.5:
                        other_data[i // 8] |= 1 << (7 - (i % 8))
                other_data = bytes(other_data)
            
            # Manual AND operation on bytes
            result = bytearray(len(data))
            for i in range(len(data)):
                if i < len(other_data):
                    result[i] = data[i] & other_data[i]
                else:
                    result[i] = 0
            return bytes(result)
        
        elif operation == 'or':
            if self.exclude_init and test_key:
                other_data = self.preinitialized[test_key]['other_bytes']
            else:
                other_data = bytearray((size + 7) // 8)
                for i in range(size):
                    if random.random() > 0.5:
                        other_data[i // 8] |= 1 << (7 - (i % 8))
                other_data = bytes(other_data)
            
            # Manual OR operation on bytes
            result = bytearray(len(data))
            for i in range(len(data)):
                if i < len(other_data):
                    result[i] = data[i] | other_data[i]
                else:
                    result[i] = data[i]
            return bytes(result)
        
        elif operation == 'slice':
            # Extract bit slices from bytes
            slices = []
            slice_size = min(100, size // 10)
            for _ in range(100):
                start = random.randint(0, max(0, size - slice_size))
                slice_bits = []
                for i in range(start, min(start + slice_size, size)):
                    byte_idx = i // 8
                    bit_idx = i % 8
                    if byte_idx < len(data) and data[byte_idx] & (1 << (7 - bit_idx)):
                        slice_bits.append(1)
                    else:
                        slice_bits.append(0)
                slices.append(slice_bits)
            return slices
    
    def _custom_bitarray_ops(self, bool_list: List[bool], int_list: List[int], 
                           size: int, operation: str, test_key: str = None, **kwargs):
        """Operations on custom BitArray"""
        if self.exclude_init and test_key:
            # For custom bitarray, we need to copy manually since it doesn't have .copy()
            source_ba = self.preinitialized[test_key]['custom_bitarray']
            # Create a new instance with same data - use a list of zeros first
            data = [0] * size
            for i in range(size):
                if source_ba[i]:
                    data[i] = 1
            ba = BitArray(data)
            ba.build()
        else:
            ba = BitArray(int_list)
            ba.build()
        
        if operation == 'access':
            # Use sequential access for better PyPy performance
            total = 0
            access_count = min(1000, size)
            step = max(1, size // access_count)
            for i in range(0, size, step):
                if i < size and ba[i]:
                    total += 1
            return total
        
        elif operation == 'count':
            return ba.count1(size)
        
        elif operation == 'sum':
            return ba.count1(size)  # Same as count for BitArray
        
        elif operation == 'flip':
            # BitArray doesn't have invert, so we'll flip manually
            for i in range(size):
                if ba[i]:
                    ba.set0(i)
                else:
                    ba.set1(i)
            # ba.build()  # Rebuild auxiliary structures
            return ba
        
        elif operation == 'and':
            if self.exclude_init and test_key:
                other = self.preinitialized[test_key]['other_custom_bitarray']
            else:
                other = BitArray([1 if random.random() > 0.5 else 0 for _ in range(size)])
                other.build()
            # Manual AND operation since BitArray doesn't have native & operator
            result_data = [0] * size
            for i in range(size):
                if ba[i] and other[i]:
                    result_data[i] = 1
            result = BitArray(result_data)
            result.build()
            return result
        
        elif operation == 'or':
            if self.exclude_init and test_key:
                other = self.preinitialized[test_key]['other_custom_bitarray']
            else:
                other = BitArray([1 if random.random() > 0.5 else 0 for _ in range(size)])
                other.build()
            # Manual OR operation since BitArray doesn't have native | operator
            result_data = [0] * size
            for i in range(size):
                if ba[i] or other[i]:
                    result_data[i] = 1
            result = BitArray(result_data)
            result.build()
            return result
        
        elif operation == 'slice':
            # BitArray doesn't support slicing, so we'll extract values manually
            slices = []
            slice_size = min(100, size // 10)
            for _ in range(100):
                start = random.randint(0, max(0, size - slice_size))
                slice_data = []
                for i in range(start, min(start + slice_size, size)):
                    slice_data.append(ba[i])
                slices.append(slice_data)
            return slices
    
    def run(self, param_grid: Dict[str, List[Any]]):
        """Override to add custom analysis"""
        super().run(param_grid)
        
        # Add memory usage analysis
        self._print_memory_analysis()
        
        # Add performance summary
        self._print_performance_summary()
    
    def _print_memory_analysis(self):
        """Print memory usage comparison"""
        print("\n" + "="*70)
        print("MEMORY USAGE ANALYSIS")
        print("="*70)
        print(f"{'Type':<20} {'Bytes/element':<15} {'MB for 1M items':<15} {'Efficiency':<15}")
        print("-"*70)
        
        memory_info = [
            ('list[bool]', 28, 'Python object overhead'),
            ('list[int]', 28, 'Python object overhead'),
            ('array.array(b)', 1, '8-bit signed'),
            ('array.array(B)', 1, '8-bit unsigned'),
            ('bytes', 0.125, '1 bit per bool (packed)'),
            ('bitarray', 0.125, '1 bit per bool'),
            ('custom_bitarray', 0.125, '1 bit per bool (custom)'),
        ]
        
        for name, bytes_per, desc in memory_info:
            if name == 'bitarray' and not HAS_BITARRAY:
                continue
            if name == 'custom_bitarray' and not HAS_CUSTOM_BITARRAY:
                continue
            mb_per_million = (bytes_per * 1_000_000) / (1024 * 1024)
            efficiency = (0.125 / bytes_per) * 100
            print(f"{name:<20} {bytes_per:<15} {mb_per_million:<15.2f} {efficiency:<14.1f}%")
    
    def _print_performance_summary(self):
        """Print performance summary by operation"""
        if not self.results:
            return
        
        print("\n" + "="*70)
        print("PERFORMANCE SUMMARY")
        print("="*70)
        
        # Group results by operation
        by_operation = {}
        for result in self.results:
            if result.error or result.time_ms == float('inf'):
                continue
            op = result.test_case.params['operation']
            if op not in by_operation:
                by_operation[op] = {}
            impl = result.implementation
            if impl not in by_operation[op]:
                by_operation[op][impl] = []
            by_operation[op][impl].append(result.time_ms)
        
        # Find best implementation for each operation
        print(f"{'Operation':<15} {'Best Implementation':<20} {'Avg Time (ms)':<15} {'vs Worst':<10}")
        print("-"*60)
        
        for op, impl_times in sorted(by_operation.items()):
            # Calculate averages
            avg_times = []
            for impl, times in impl_times.items():
                avg = statistics.mean(times)
                avg_times.append((impl, avg))
            
            # Sort by time
            avg_times.sort(key=lambda x: x[1])
            
            if avg_times:
                best_impl, best_time = avg_times[0]
                worst_time = avg_times[-1][1]
                speedup = worst_time / best_time if best_time > 0 else 0
                
                print(f"{op:<15} {best_impl:<20} {best_time:<15.3f} {speedup:<10.1f}x")


def run_comprehensive_benchmark():
    """Run comprehensive boolean benchmark suite"""
    
    # Define operations to test
    operations = ['access', 'count', 'sum', 'flip', 'and', 'or', 'slice']
    sizes = [100, 1000, 10000, 100000]
    
    if HAS_BITARRAY:
        sizes.append(1000000)  # Add larger size if bitarray available
    
    print("="*80)
    print("BOOLEAN LIST COMPREHENSIVE BENCHMARK")
    print("="*80)
    
    # Run benchmark with initialization included
    print("\n1. WITH INITIALIZATION TIME:")
    config_with_init = BenchmarkConfig(
        name="bool_ops_with_init",
        iterations=10,
        warmup=2,
        save_results=True,
        plot_results=True,
        output_dir="./output/benchmark_results/bool_list"
    )
    config_with_init.exclude_init = False
    
    benchmark_with = BooleanListBenchmark(config_with_init)
    benchmark_with.run({
        'size': sizes,
        'operation': operations
    })
    
    # Run benchmark without initialization
    print("\n2. WITHOUT INITIALIZATION TIME (Operations Only):")
    config_without_init = BenchmarkConfig(
        name="bool_ops_without_init",
        iterations=10,
        warmup=2,
        save_results=True,
        plot_results=True,
        output_dir="./output/benchmark_results/bool_list"
    )
    config_without_init.exclude_init = True
    
    benchmark_without = BooleanListBenchmark(config_without_init)
    benchmark_without.run({
        'size': sizes,
        'operation': operations
    })

if __name__ == "__main__":
    run_comprehensive_benchmark()
    