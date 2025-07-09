---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/popcnt32_fn.py
    title: cp_library/bit/popcnt32_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/array/u32f_fn.py
    title: cp_library/ds/array/u32f_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/wavelet/bit_array_cls.py
    title: cp_library/ds/wavelet/bit_array_cls.py
  - icon: ':warning:'
    path: cp_library/perf/benchmark.py
    title: cp_library/perf/benchmark.py
  - icon: ':warning:'
    path: cp_library/perf/generators.py
    title: cp_library/perf/generators.py
  - icon: ':warning:'
    path: cp_library/perf/plotters.py
    title: cp_library/perf/plotters.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.16/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.10.16/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 101, in bundle\n    return bundler.update(path)\n  File \"/opt/hostedtoolcache/PyPy/3.10.16/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python_bundle.py\"\
    , line 154, in update\n    self.process_file(path)\n  File \"/opt/hostedtoolcache/PyPy/3.10.16/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python_bundle.py\"\
    , line 24, in process_file\n    self.bundled_code[file_path] = self.process_imports(tree,\
    \ file_path, source, file_is_top_level)\n  File \"/opt/hostedtoolcache/PyPy/3.10.16/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python_bundle.py\"\
    , line 102, in process_imports\n    processor.visit(tree)\n  File \"/opt/hostedtoolcache/PyPy/3.10.16/x64/lib/pypy3.10/ast.py\"\
    , line 418, in visit\n    return visitor(node)\n  File \"/opt/hostedtoolcache/PyPy/3.10.16/x64/lib/pypy3.10/ast.py\"\
    , line 426, in generic_visit\n    self.visit(item)\n  File \"/opt/hostedtoolcache/PyPy/3.10.16/x64/lib/pypy3.10/ast.py\"\
    , line 418, in visit\n    return visitor(node)\n  File \"/opt/hostedtoolcache/PyPy/3.10.16/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python_bundle.py\"\
    , line 80, in visit_ImportFrom\n    self.process_module(node, module_path, file_is_top_level,\
    \ from_import=True, import_names=node.names)\n  File \"/opt/hostedtoolcache/PyPy/3.10.16/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python_bundle.py\"\
    , line 92, in process_module\n    imported_code = self.bundler.import_file(module_path,\
    \ is_top_level)\n  File \"/opt/hostedtoolcache/PyPy/3.10.16/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python_bundle.py\"\
    , line 31, in import_file\n    self.process_file(file_path, is_top_level)\n  File\
    \ \"/opt/hostedtoolcache/PyPy/3.10.16/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python_bundle.py\"\
    , line 24, in process_file\n    self.bundled_code[file_path] = self.process_imports(tree,\
    \ file_path, source, file_is_top_level)\n  File \"/opt/hostedtoolcache/PyPy/3.10.16/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python_bundle.py\"\
    , line 102, in process_imports\n    processor.visit(tree)\n  File \"/opt/hostedtoolcache/PyPy/3.10.16/x64/lib/pypy3.10/ast.py\"\
    , line 418, in visit\n    return visitor(node)\n  File \"/opt/hostedtoolcache/PyPy/3.10.16/x64/lib/pypy3.10/ast.py\"\
    , line 426, in generic_visit\n    self.visit(item)\n  File \"/opt/hostedtoolcache/PyPy/3.10.16/x64/lib/pypy3.10/ast.py\"\
    , line 418, in visit\n    return visitor(node)\n  File \"/opt/hostedtoolcache/PyPy/3.10.16/x64/lib/pypy3.10/ast.py\"\
    , line 426, in generic_visit\n    self.visit(item)\n  File \"/opt/hostedtoolcache/PyPy/3.10.16/x64/lib/pypy3.10/ast.py\"\
    , line 418, in visit\n    return visitor(node)\n  File \"/opt/hostedtoolcache/PyPy/3.10.16/x64/lib/pypy3.10/ast.py\"\
    , line 426, in generic_visit\n    self.visit(item)\n  File \"/opt/hostedtoolcache/PyPy/3.10.16/x64/lib/pypy3.10/ast.py\"\
    , line 418, in visit\n    return visitor(node)\n  File \"/opt/hostedtoolcache/PyPy/3.10.16/x64/lib/pypy3.10/ast.py\"\
    , line 426, in generic_visit\n    self.visit(item)\n  File \"/opt/hostedtoolcache/PyPy/3.10.16/x64/lib/pypy3.10/ast.py\"\
    , line 418, in visit\n    return visitor(node)\n  File \"/opt/hostedtoolcache/PyPy/3.10.16/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python_bundle.py\"\
    , line 64, in visit_ImportFrom\n    raise NotImplementedError(\"Relative imports\
    \ are not supported\")\nNotImplementedError: Relative imports are not supported\n"
  code: "\"\"\"\nComprehensive benchmark for boolean list representations using cp_library.perf\
    \ framework.\n\nCompares:\n- list[bool]\n- list[int] (0/1)\n- array.array('b')\
    \ - signed char\n- array.array('B') - unsigned char  \n- bitarray (if available)\n\
    \"\"\"\n\nfrom cp_library.perf.benchmark import Benchmark, BenchmarkConfig, TestCase\n\
    from cp_library.perf.generators import DataGenerator\nfrom typing import Dict,\
    \ List, Any, Callable, Tuple\nimport time\nimport array\nimport random\nimport\
    \ statistics\n\ntry:\n    import bitarray\n    HAS_BITARRAY = True\nexcept ImportError:\n\
    \    HAS_BITARRAY = False\n    print(\"Note: bitarray module not available. Install\
    \ with: pip install bitarray\")\n\ntry:\n    import sys\n    import os\n    #\
    \ Add the cp_library path to import the local version\n    sys.path.insert(0,\
    \ os.path.join(os.path.dirname(__file__), '..'))\n    from cp_library.ds.wavelet.bit_array_cls\
    \ import BitArray\n    HAS_CUSTOM_BITARRAY = True\nexcept ImportError as e:\n\
    \    HAS_CUSTOM_BITARRAY = False\n    print(f\"Note: Custom BitArray not available:\
    \ {e}\")\n\n\nclass BooleanDataGenerator(DataGenerator):\n    \"\"\"Generate boolean\
    \ test data in various formats\"\"\"\n    \n    def __init__(self, true_probability:\
    \ float = 0.5):\n        self.true_probability = true_probability\n    \n    def\
    \ generate(self, size: int, **params) -> Dict[str, Any]:\n        \"\"\"Generate\
    \ test data with all formats needed\"\"\"\n        bool_list = [random.random()\
    \ < self.true_probability for _ in range(size)]\n        int_list = [int(b) for\
    \ b in bool_list]\n        \n        return {\n            'bool_list': bool_list,\n\
    \            'int_list': int_list,\n            'size': size,\n            'operation':\
    \ params.get('operation', 'access')\n        }\n\n\nclass BooleanListBenchmark(Benchmark):\n\
    \    \"\"\"Benchmark boolean list operations with fair timing\"\"\"\n    \n  \
    \  def __init__(self, config: BenchmarkConfig):\n        super().__init__(config)\n\
    \        self.exclude_init = getattr(config, 'exclude_init', False)\n        self.preinitialized\
    \ = {}\n    \n    def generate_test_cases(self, param_grid: Dict[str, List[Any]])\
    \ -> List[TestCase]:\n        \"\"\"Generate test cases and optionally pre-initialize\
    \ data structures\"\"\"\n        test_cases = []\n        generator = BooleanDataGenerator()\n\
    \        \n        for size in param_grid.get('size', [1000]):\n            for\
    \ operation in param_grid.get('operation', ['access']):\n                # Generate\
    \ base data\n                test_data = generator.generate(size, operation=operation)\n\
    \                \n                # Pre-initialize if excluding init time\n \
    \               if self.exclude_init:\n                    test_key = f\"{operation}_{size}\"\
    \n                    self.preinitialized[test_key] = self._create_structures(test_data)\n\
    \                    test_data['test_key'] = test_key\n                \n    \
    \            test_cases.append(TestCase(\n                    name=f\"{operation}_size_{size}\"\
    ,\n                    params={'size': size, 'operation': operation},\n      \
    \              data=test_data\n                ))\n        \n        return test_cases\n\
    \    \n    def _create_structures(self, test_data: Dict[str, Any]) -> Dict[str,\
    \ Any]:\n        \"\"\"Pre-create data structures and auxiliary data for fair\
    \ timing\"\"\"\n        size = test_data['size']\n        \n        # Generate\
    \ auxiliary data for binary operations using native types\n        other_bool\
    \ = [random.random() > 0.5 for _ in range(size)]\n        other_int = [1 if b\
    \ else 0 for b in other_bool]  # Native 1/0\n        \n        # Convert bool\
    \ list to bytes (pack 8 bools per byte)\n        bytes_data = bytearray((size\
    \ + 7) // 8)\n        for i, bit in enumerate(test_data['bool_list']):\n     \
    \       if bit:\n                bytes_data[i // 8] |= 1 << (7 - (i % 8))  # MSB\
    \ first\n        \n        # Convert other_bool to bytes for binary operations\n\
    \        other_bytes_data = bytearray((size + 7) // 8)\n        for i, bit in\
    \ enumerate(other_bool):\n            if bit:\n                other_bytes_data[i\
    \ // 8] |= 1 << (7 - (i % 8))\n        \n        structures = {\n            'list_bool':\
    \ list(test_data['bool_list']),\n            'list_int': list(test_data['int_list']),\n\
    \            'array_b': array.array('b', test_data['int_list']),\n           \
    \ 'array_B': array.array('B', test_data['int_list']),\n            'bytes': bytes(bytes_data),\n\
    \            # Pre-generated auxiliary data\n            'other_bool': other_bool,\n\
    \            'other_int': other_int,\n            'other_array_b': array.array('b',\
    \ other_int),\n            'other_array_B': array.array('B', other_int),\n   \
    \         'other_bytes': bytes(other_bytes_data),\n        }\n        \n     \
    \   if HAS_BITARRAY:\n            # Use frombytes for better performance\n   \
    \         ba = bitarray.bitarray()\n            ba.frombytes(bytes_data)\n   \
    \         # Trim to exact size since frombytes might add extra bits\n        \
    \    if len(ba) > size:\n                ba = ba[:size]\n            structures['bitarray']\
    \ = ba\n            \n            # Pre-create auxiliary bitarray using frombytes\n\
    \            other_ba = bitarray.bitarray()\n            other_ba.frombytes(other_bytes_data)\n\
    \            if len(other_ba) > size:\n                other_ba = other_ba[:size]\n\
    \            structures['other_bitarray'] = other_ba\n        \n        if HAS_CUSTOM_BITARRAY:\n\
    \            # Create custom BitArray from int list (not bytes - keep original\
    \ approach)\n            custom_ba = BitArray(test_data['int_list'])\n       \
    \     custom_ba.build()  # Build the auxiliary data structures\n            structures['custom_bitarray']\
    \ = custom_ba\n            \n            # Pre-create auxiliary custom bitarray\n\
    \            other_custom_ba = BitArray(other_int)\n            other_custom_ba.build()\n\
    \            structures['other_custom_bitarray'] = other_custom_ba\n        \n\
    \        return structures\n    \n    def get_implementations(self) -> Dict[str,\
    \ Callable]:\n        \"\"\"Return implementation functions\"\"\"\n        implementations\
    \ = {\n            'list_bool': self._list_bool_ops,\n            'list_int':\
    \ self._list_int_ops,\n            'array_b': self._array_b_ops,\n           \
    \ 'array_B': self._array_B_ops,\n            'bytes': self._bytes_ops,\n     \
    \   }\n        \n        if HAS_BITARRAY:\n            implementations['bitarray']\
    \ = self._bitarray_ops\n        \n        if HAS_CUSTOM_BITARRAY:\n          \
    \  implementations['custom_bitarray'] = self._custom_bitarray_ops\n        \n\
    \        return implementations\n    \n    def validate_result(self, expected:\
    \ Any, actual: Any) -> bool:\n        \"\"\"Custom validation - just verify we\
    \ got a result\"\"\"\n        return actual is not None\n    \n    def measure_time(self,\
    \ func: Callable, test_data: Dict) -> Tuple[Any, float]:\n        \"\"\"Custom\
    \ timing to handle initialization exclusion\"\"\"\n        operation = test_data['operation']\n\
    \        size = test_data['size']\n        \n        # Adjust iterations based\
    \ on operation complexity\n        if operation in ['and', 'or', 'xor'] and size\
    \ > 10000:\n            iterations = max(1, 100 // (size // 10000))\n        elif\
    \ operation == 'access':\n            iterations = 10\n        elif operation\
    \ == 'count' and size > 100000:\n            iterations = 5\n        else:\n \
    \           iterations = self.config.iterations\n        \n        # Warmup\n\
    \        for _ in range(min(self.config.warmup, 2)):\n            func(**test_data)\n\
    \        \n        # Time measurement\n        start = time.perf_counter()\n \
    \       for _ in range(iterations):\n            result = func(**test_data)\n\
    \        elapsed_ms = (time.perf_counter() - start) * 1000 / iterations\n    \
    \    \n        return result, elapsed_ms\n    \n    # Implementation methods\n\
    \    def _list_bool_ops(self, bool_list: List[bool], int_list: List[int], \n \
    \                      size: int, operation: str, test_key: str = None, **kwargs):\n\
    \        \"\"\"Operations on list[bool]\"\"\"\n        # Get data (pre-initialized\
    \ or create new)\n        if self.exclude_init and test_key:\n            lst\
    \ = self.preinitialized[test_key]['list_bool'].copy()\n        else:\n       \
    \     lst = list(bool_list)\n        \n        if operation == 'access':\n   \
    \         # Use sequential access for better PyPy performance\n            total\
    \ = 0\n            access_count = min(1000, size)\n            step = max(1, size\
    \ // access_count)\n            for i in range(0, size, step):\n             \
    \   if i < size and lst[i]:\n                    total += 1\n            return\
    \ total\n        \n        elif operation == 'count':\n            return lst.count(True)\n\
    \        \n        elif operation == 'sum':\n            return sum(lst)\n   \
    \     \n        elif operation == 'flip':\n            for i in range(len(lst)):\n\
    \                lst[i] = not lst[i]\n            return lst\n        \n     \
    \   elif operation == 'and':\n            if self.exclude_init and test_key:\n\
    \                other = self.preinitialized[test_key]['other_bool']\n       \
    \     else:\n                other = [random.random() > 0.5 for _ in range(size)]\n\
    \            # Use manual loop for PyPy optimization\n            result = [False]\
    \ * size  # Pre-allocate\n            for i in range(size):\n                result[i]\
    \ = lst[i] and other[i]\n            return result\n        \n        elif operation\
    \ == 'or':\n            if self.exclude_init and test_key:\n                other\
    \ = self.preinitialized[test_key]['other_bool']\n            else:\n         \
    \       other = [random.random() > 0.5 for _ in range(size)]\n            # Use\
    \ manual loop for PyPy optimization\n            result = [False] * size  # Pre-allocate\n\
    \            for i in range(size):\n                result[i] = lst[i] or other[i]\n\
    \            return result\n        \n        elif operation == 'slice':\n   \
    \         slices = []\n            slice_size = min(100, size // 10)\n       \
    \     for _ in range(100):\n                start = random.randint(0, max(0, size\
    \ - slice_size))\n                slices.append(lst[start:start + slice_size])\n\
    \            return slices\n    \n    def _list_int_ops(self, bool_list: List[bool],\
    \ int_list: List[int], \n                      size: int, operation: str, test_key:\
    \ str = None, **kwargs):\n        \"\"\"Operations on list[int]\"\"\"\n      \
    \  if self.exclude_init and test_key:\n            lst = self.preinitialized[test_key]['list_int'].copy()\n\
    \        else:\n            lst = list(int_list)\n        \n        if operation\
    \ == 'access':\n            # Use sequential access for better PyPy performance\n\
    \            total = 0\n            access_count = min(1000, size)\n         \
    \   step = max(1, size // access_count)\n            for i in range(0, size, step):\n\
    \                if i < size and lst[i]:\n                    total += 1\n   \
    \         return total\n        \n        elif operation == 'count':\n       \
    \     return lst.count(1)\n        \n        elif operation == 'sum':\n      \
    \      return sum(lst)\n        \n        elif operation == 'flip':\n        \
    \    for i in range(len(lst)):\n                lst[i] = 1 ^ lst[i]\n        \
    \    return lst\n        \n        elif operation == 'and':\n            if self.exclude_init\
    \ and test_key:\n                other = self.preinitialized[test_key]['other_int']\n\
    \            else:\n                other = [1 if random.random() > 0.5 else 0\
    \ for _ in range(size)]  # Native 1/0\n            # Use manual loop for PyPy\
    \ optimization\n            result = [0] * size  # Pre-allocate\n            for\
    \ i in range(size):\n                result[i] = lst[i] & other[i]\n         \
    \   return result\n        \n        elif operation == 'or':\n            if self.exclude_init\
    \ and test_key:\n                other = self.preinitialized[test_key]['other_int']\n\
    \            else:\n                other = [1 if random.random() > 0.5 else 0\
    \ for _ in range(size)]  # Native 1/0\n            # Use manual loop for PyPy\
    \ optimization\n            result = [0] * size  # Pre-allocate\n            for\
    \ i in range(size):\n                result[i] = lst[i] | other[i]\n         \
    \   return result\n        \n        elif operation == 'slice':\n            slices\
    \ = []\n            slice_size = min(100, size // 10)\n            for _ in range(100):\n\
    \                start = random.randint(0, max(0, size - slice_size))\n      \
    \          slices.append(lst[start:start + slice_size])\n            return slices\n\
    \    \n    def _array_b_ops(self, bool_list: List[bool], int_list: List[int],\
    \ \n                     size: int, operation: str, test_key: str = None, **kwargs):\n\
    \        \"\"\"Operations on array.array('b')\"\"\"\n        if self.exclude_init\
    \ and test_key:\n            arr = self.preinitialized[test_key]['array_b'][:]\n\
    \        else:\n            arr = array.array('b', int_list)\n        \n     \
    \   if operation == 'access':\n            # Use sequential access for better\
    \ PyPy performance\n            total = 0\n            access_count = min(1000,\
    \ size)\n            step = max(1, size // access_count)\n            for i in\
    \ range(0, size, step):\n                if i < size and arr[i]:\n           \
    \         total += 1\n            return total\n        \n        elif operation\
    \ == 'count':\n            return arr.count(1)\n        \n        elif operation\
    \ == 'sum':\n            return sum(arr)\n        \n        elif operation ==\
    \ 'flip':\n            for i in range(len(arr)):\n                arr[i] = 1 ^\
    \ arr[i]\n            return arr\n        \n        elif operation == 'and':\n\
    \            if self.exclude_init and test_key:\n                other = self.preinitialized[test_key]['other_array_b']\n\
    \            else:\n                other = array.array('b', [1 if random.random()\
    \ > 0.5 else 0 for _ in range(size)])\n            # Use manual loop for PyPy\
    \ optimization\n            result = array.array('b', [0] * size)  # Pre-allocate\n\
    \            for i in range(size):\n                result[i] = arr[i] & other[i]\n\
    \            return result\n        \n        elif operation == 'or':\n      \
    \      if self.exclude_init and test_key:\n                other = self.preinitialized[test_key]['other_array_b']\n\
    \            else:\n                other = array.array('b', [1 if random.random()\
    \ > 0.5 else 0 for _ in range(size)])\n            # Use manual loop for PyPy\
    \ optimization\n            result = array.array('b', [0] * size)  # Pre-allocate\n\
    \            for i in range(size):\n                result[i] = arr[i] | other[i]\n\
    \            return result\n        \n        elif operation == 'slice':\n   \
    \         slices = []\n            slice_size = min(100, size // 10)\n       \
    \     for _ in range(100):\n                start = random.randint(0, max(0, size\
    \ - slice_size))\n                slices.append(arr[start:start + slice_size])\n\
    \            return slices\n    \n    def _array_B_ops(self, bool_list: List[bool],\
    \ int_list: List[int], \n                     size: int, operation: str, test_key:\
    \ str = None, **kwargs):\n        \"\"\"Operations on array.array('B')\"\"\"\n\
    \        if self.exclude_init and test_key:\n            arr = self.preinitialized[test_key]['array_B'][:]\n\
    \        else:\n            arr = array.array('B', int_list)\n        \n     \
    \   if operation == 'access':\n            # Use sequential access for better\
    \ PyPy performance\n            total = 0\n            access_count = min(1000,\
    \ size)\n            step = max(1, size // access_count)\n            for i in\
    \ range(0, size, step):\n                if i < size and arr[i]:\n           \
    \         total += 1\n            return total\n        \n        elif operation\
    \ == 'count':\n            return arr.count(1)\n        \n        elif operation\
    \ == 'sum':\n            return sum(arr)\n        \n        elif operation ==\
    \ 'flip':\n            for i in range(len(arr)):\n                arr[i] = 1 -\
    \ arr[i]\n            return arr\n        \n        elif operation == 'and':\n\
    \            if self.exclude_init and test_key:\n                other = self.preinitialized[test_key]['other_array_B']\n\
    \            else:\n                other = array.array('B', [1 if random.random()\
    \ > 0.5 else 0 for _ in range(size)])\n            # Use manual loop for PyPy\
    \ optimization\n            result = array.array('B', [0] * size)  # Pre-allocate\n\
    \            for i in range(size):\n                result[i] = arr[i] & other[i]\n\
    \            return result\n        \n        elif operation == 'or':\n      \
    \      if self.exclude_init and test_key:\n                other = self.preinitialized[test_key]['other_array_B']\n\
    \            else:\n                other = array.array('B', [1 if random.random()\
    \ > 0.5 else 0 for _ in range(size)])\n            # Use manual loop for PyPy\
    \ optimization\n            result = array.array('B', [0] * size)  # Pre-allocate\n\
    \            for i in range(size):\n                result[i] = arr[i] | other[i]\n\
    \            return result\n        \n        elif operation == 'slice':\n   \
    \         slices = []\n            slice_size = min(100, size // 10)\n       \
    \     for _ in range(100):\n                start = random.randint(0, max(0, size\
    \ - slice_size))\n                slices.append(arr[start:start + slice_size])\n\
    \            return slices\n    \n    def _bitarray_ops(self, bool_list: List[bool],\
    \ int_list: List[int], \n                      size: int, operation: str, test_key:\
    \ str = None, **kwargs):\n        \"\"\"Operations on bitarray\"\"\"\n       \
    \ if self.exclude_init and test_key:\n            ba = self.preinitialized[test_key]['bitarray'].copy()\n\
    \        else:\n            ba = bitarray.bitarray(int_list)\n        \n     \
    \   if operation == 'access':\n            # Use sequential access for better\
    \ PyPy performance\n            total = 0\n            access_count = min(1000,\
    \ size)\n            step = max(1, size // access_count)\n            for i in\
    \ range(0, size, step):\n                if i < size and ba[i]:\n            \
    \        total += 1\n            return total\n        \n        elif operation\
    \ == 'count':\n            return ba.count(1)\n        \n        elif operation\
    \ == 'sum':\n            return ba.count(1)  # Same as count for bitarray\n  \
    \      \n        elif operation == 'flip':\n            ba.invert()\n        \
    \    return ba\n        \n        elif operation == 'and':\n            if self.exclude_init\
    \ and test_key:\n                other = self.preinitialized[test_key]['other_bitarray']\n\
    \            else:\n                other = bitarray.bitarray([random.random()\
    \ > 0.5 for _ in range(size)])\n            return ba & other\n        \n    \
    \    elif operation == 'or':\n            if self.exclude_init and test_key:\n\
    \                other = self.preinitialized[test_key]['other_bitarray']\n   \
    \         else:\n                other = bitarray.bitarray([random.random() >\
    \ 0.5 for _ in range(size)])\n            return ba | other\n        \n      \
    \  elif operation == 'slice':\n            slices = []\n            slice_size\
    \ = min(100, size // 10)\n            for _ in range(100):\n                start\
    \ = random.randint(0, max(0, size - slice_size))\n                slices.append(ba[start:start\
    \ + slice_size])\n            return slices\n    \n    def _bytes_ops(self, bool_list:\
    \ List[bool], int_list: List[int], \n                   size: int, operation:\
    \ str, test_key: str = None, **kwargs):\n        \"\"\"Operations on bytes (packed\
    \ bits)\"\"\"\n        if self.exclude_init and test_key:\n            data =\
    \ self.preinitialized[test_key]['bytes']\n        else:\n            # Pack bool\
    \ list into bytes\n            data = bytearray((size + 7) // 8)\n           \
    \ for i, bit in enumerate(bool_list):\n                if bit:\n             \
    \       data[i // 8] |= 1 << (7 - (i % 8))  # MSB first\n            data = bytes(data)\n\
    \        \n        if operation == 'access':\n            # Use sequential access\
    \ for better PyPy performance\n            total = 0\n            access_count\
    \ = min(1000, size)\n            step = max(1, size // access_count)\n       \
    \     for i in range(0, size, step):\n                if i < size:\n         \
    \           byte_idx = i // 8\n                    bit_idx = i % 8\n         \
    \           if byte_idx < len(data) and data[byte_idx] & (1 << (7 - bit_idx)):\n\
    \                        total += 1\n            return total\n        \n    \
    \    elif operation == 'count':\n            # Count all set bits in the bytes\n\
    \            count = 0\n            for i in range(size):\n                byte_idx\
    \ = i // 8\n                bit_idx = i % 8\n                if byte_idx < len(data)\
    \ and data[byte_idx] & (1 << (7 - bit_idx)):\n                    count += 1\n\
    \            return count\n        \n        elif operation == 'sum':\n      \
    \      return self._bytes_ops(bool_list, int_list, size, 'count', test_key, **kwargs)\n\
    \        \n        elif operation == 'flip':\n            # Flip all bits in bytes\n\
    \            flipped = bytearray(len(data))\n            for i, byte_val in enumerate(data):\n\
    \                flipped[i] = byte_val ^ 0xFF  # Flip all 8 bits\n           \
    \ # Handle partial last byte if size is not multiple of 8\n            if size\
    \ % 8 != 0:\n                last_byte_mask = (1 << (8 - (size % 8))) - 1\n  \
    \              flipped[-1] &= ~last_byte_mask  # Clear unused bits\n         \
    \   return bytes(flipped)\n        \n        elif operation == 'and':\n      \
    \      if self.exclude_init and test_key:\n                other_data = self.preinitialized[test_key]['other_bytes']\n\
    \            else:\n                other_data = bytearray((size + 7) // 8)\n\
    \                for i in range(size):\n                    if random.random()\
    \ > 0.5:\n                        other_data[i // 8] |= 1 << (7 - (i % 8))\n \
    \               other_data = bytes(other_data)\n            \n            # Manual\
    \ AND operation on bytes\n            result = bytearray(len(data))\n        \
    \    for i in range(len(data)):\n                if i < len(other_data):\n   \
    \                 result[i] = data[i] & other_data[i]\n                else:\n\
    \                    result[i] = 0\n            return bytes(result)\n       \
    \ \n        elif operation == 'or':\n            if self.exclude_init and test_key:\n\
    \                other_data = self.preinitialized[test_key]['other_bytes']\n \
    \           else:\n                other_data = bytearray((size + 7) // 8)\n \
    \               for i in range(size):\n                    if random.random()\
    \ > 0.5:\n                        other_data[i // 8] |= 1 << (7 - (i % 8))\n \
    \               other_data = bytes(other_data)\n            \n            # Manual\
    \ OR operation on bytes\n            result = bytearray(len(data))\n         \
    \   for i in range(len(data)):\n                if i < len(other_data):\n    \
    \                result[i] = data[i] | other_data[i]\n                else:\n\
    \                    result[i] = data[i]\n            return bytes(result)\n \
    \       \n        elif operation == 'slice':\n            # Extract bit slices\
    \ from bytes\n            slices = []\n            slice_size = min(100, size\
    \ // 10)\n            for _ in range(100):\n                start = random.randint(0,\
    \ max(0, size - slice_size))\n                slice_bits = []\n              \
    \  for i in range(start, min(start + slice_size, size)):\n                   \
    \ byte_idx = i // 8\n                    bit_idx = i % 8\n                   \
    \ if byte_idx < len(data) and data[byte_idx] & (1 << (7 - bit_idx)):\n       \
    \                 slice_bits.append(1)\n                    else:\n          \
    \              slice_bits.append(0)\n                slices.append(slice_bits)\n\
    \            return slices\n    \n    def _custom_bitarray_ops(self, bool_list:\
    \ List[bool], int_list: List[int], \n                           size: int, operation:\
    \ str, test_key: str = None, **kwargs):\n        \"\"\"Operations on custom BitArray\"\
    \"\"\n        if self.exclude_init and test_key:\n            # For custom bitarray,\
    \ we need to copy manually since it doesn't have .copy()\n            source_ba\
    \ = self.preinitialized[test_key]['custom_bitarray']\n            # Create a new\
    \ instance with same data - use a list of zeros first\n            data = [0]\
    \ * size\n            for i in range(size):\n                if source_ba[i]:\n\
    \                    data[i] = 1\n            ba = BitArray(data)\n          \
    \  ba.build()\n        else:\n            ba = BitArray(int_list)\n          \
    \  ba.build()\n        \n        if operation == 'access':\n            # Use\
    \ sequential access for better PyPy performance\n            total = 0\n     \
    \       access_count = min(1000, size)\n            step = max(1, size // access_count)\n\
    \            for i in range(0, size, step):\n                if i < size and ba[i]:\n\
    \                    total += 1\n            return total\n        \n        elif\
    \ operation == 'count':\n            return ba.count1(size)\n        \n      \
    \  elif operation == 'sum':\n            return ba.count1(size)  # Same as count\
    \ for BitArray\n        \n        elif operation == 'flip':\n            # BitArray\
    \ doesn't have invert, so we'll flip manually\n            for i in range(size):\n\
    \                if ba[i]:\n                    ba.set0(i)\n                else:\n\
    \                    ba.set1(i)\n            # ba.build()  # Rebuild auxiliary\
    \ structures\n            return ba\n        \n        elif operation == 'and':\n\
    \            if self.exclude_init and test_key:\n                other = self.preinitialized[test_key]['other_custom_bitarray']\n\
    \            else:\n                other = BitArray([1 if random.random() > 0.5\
    \ else 0 for _ in range(size)])\n                other.build()\n            #\
    \ Manual AND operation since BitArray doesn't have native & operator\n       \
    \     result_data = [0] * size\n            for i in range(size):\n          \
    \      if ba[i] and other[i]:\n                    result_data[i] = 1\n      \
    \      result = BitArray(result_data)\n            result.build()\n          \
    \  return result\n        \n        elif operation == 'or':\n            if self.exclude_init\
    \ and test_key:\n                other = self.preinitialized[test_key]['other_custom_bitarray']\n\
    \            else:\n                other = BitArray([1 if random.random() > 0.5\
    \ else 0 for _ in range(size)])\n                other.build()\n            #\
    \ Manual OR operation since BitArray doesn't have native | operator\n        \
    \    result_data = [0] * size\n            for i in range(size):\n           \
    \     if ba[i] or other[i]:\n                    result_data[i] = 1\n        \
    \    result = BitArray(result_data)\n            result.build()\n            return\
    \ result\n        \n        elif operation == 'slice':\n            # BitArray\
    \ doesn't support slicing, so we'll extract values manually\n            slices\
    \ = []\n            slice_size = min(100, size // 10)\n            for _ in range(100):\n\
    \                start = random.randint(0, max(0, size - slice_size))\n      \
    \          slice_data = []\n                for i in range(start, min(start +\
    \ slice_size, size)):\n                    slice_data.append(ba[i])\n        \
    \        slices.append(slice_data)\n            return slices\n    \n    def run(self,\
    \ param_grid: Dict[str, List[Any]]):\n        \"\"\"Override to add custom analysis\"\
    \"\"\n        super().run(param_grid)\n        \n        # Add memory usage analysis\n\
    \        self._print_memory_analysis()\n        \n        # Add performance summary\n\
    \        self._print_performance_summary()\n    \n    def _print_memory_analysis(self):\n\
    \        \"\"\"Print memory usage comparison\"\"\"\n        print(\"\\n\" + \"\
    =\"*70)\n        print(\"MEMORY USAGE ANALYSIS\")\n        print(\"=\"*70)\n \
    \       print(f\"{'Type':<20} {'Bytes/element':<15} {'MB for 1M items':<15} {'Efficiency':<15}\"\
    )\n        print(\"-\"*70)\n        \n        memory_info = [\n            ('list[bool]',\
    \ 28, 'Python object overhead'),\n            ('list[int]', 28, 'Python object\
    \ overhead'),\n            ('array.array(b)', 1, '8-bit signed'),\n          \
    \  ('array.array(B)', 1, '8-bit unsigned'),\n            ('bytes', 0.125, '1 bit\
    \ per bool (packed)'),\n            ('bitarray', 0.125, '1 bit per bool'),\n \
    \           ('custom_bitarray', 0.125, '1 bit per bool (custom)'),\n        ]\n\
    \        \n        for name, bytes_per, desc in memory_info:\n            if name\
    \ == 'bitarray' and not HAS_BITARRAY:\n                continue\n            if\
    \ name == 'custom_bitarray' and not HAS_CUSTOM_BITARRAY:\n                continue\n\
    \            mb_per_million = (bytes_per * 1_000_000) / (1024 * 1024)\n      \
    \      efficiency = (0.125 / bytes_per) * 100\n            print(f\"{name:<20}\
    \ {bytes_per:<15} {mb_per_million:<15.2f} {efficiency:<14.1f}%\")\n    \n    def\
    \ _print_performance_summary(self):\n        \"\"\"Print performance summary by\
    \ operation\"\"\"\n        if not self.results:\n            return\n        \n\
    \        print(\"\\n\" + \"=\"*70)\n        print(\"PERFORMANCE SUMMARY\")\n \
    \       print(\"=\"*70)\n        \n        # Group results by operation\n    \
    \    by_operation = {}\n        for result in self.results:\n            if result.error\
    \ or result.time_ms == float('inf'):\n                continue\n            op\
    \ = result.test_case.params['operation']\n            if op not in by_operation:\n\
    \                by_operation[op] = {}\n            impl = result.implementation\n\
    \            if impl not in by_operation[op]:\n                by_operation[op][impl]\
    \ = []\n            by_operation[op][impl].append(result.time_ms)\n        \n\
    \        # Find best implementation for each operation\n        print(f\"{'Operation':<15}\
    \ {'Best Implementation':<20} {'Avg Time (ms)':<15} {'vs Worst':<10}\")\n    \
    \    print(\"-\"*60)\n        \n        for op, impl_times in sorted(by_operation.items()):\n\
    \            # Calculate averages\n            avg_times = []\n            for\
    \ impl, times in impl_times.items():\n                avg = statistics.mean(times)\n\
    \                avg_times.append((impl, avg))\n            \n            # Sort\
    \ by time\n            avg_times.sort(key=lambda x: x[1])\n            \n    \
    \        if avg_times:\n                best_impl, best_time = avg_times[0]\n\
    \                worst_time = avg_times[-1][1]\n                speedup = worst_time\
    \ / best_time if best_time > 0 else 0\n                \n                print(f\"\
    {op:<15} {best_impl:<20} {best_time:<15.3f} {speedup:<10.1f}x\")\n\n\ndef run_comprehensive_benchmark():\n\
    \    \"\"\"Run comprehensive boolean benchmark suite\"\"\"\n    \n    # Define\
    \ operations to test\n    operations = ['access', 'count', 'sum', 'flip', 'and',\
    \ 'or', 'slice']\n    sizes = [100, 1000, 10000, 100000]\n    \n    if HAS_BITARRAY:\n\
    \        sizes.append(1000000)  # Add larger size if bitarray available\n    \n\
    \    print(\"=\"*80)\n    print(\"BOOLEAN LIST COMPREHENSIVE BENCHMARK\")\n  \
    \  print(\"=\"*80)\n    \n    # Run benchmark with initialization included\n \
    \   print(\"\\n1. WITH INITIALIZATION TIME:\")\n    config_with_init = BenchmarkConfig(\n\
    \        name=\"bool_ops_with_init\",\n        iterations=10,\n        warmup=2,\n\
    \        save_results=True,\n        plot_results=True,\n        output_dir=\"\
    ./output/benchmark_results/bool_list\"\n    )\n    config_with_init.exclude_init\
    \ = False\n    \n    benchmark_with = BooleanListBenchmark(config_with_init)\n\
    \    benchmark_with.run({\n        'size': sizes,\n        'operation': operations\n\
    \    })\n    \n    # Run benchmark without initialization\n    print(\"\\n2. WITHOUT\
    \ INITIALIZATION TIME (Operations Only):\")\n    config_without_init = BenchmarkConfig(\n\
    \        name=\"bool_ops_without_init\",\n        iterations=10,\n        warmup=2,\n\
    \        save_results=True,\n        plot_results=True,\n        output_dir=\"\
    ./output/benchmark_results/bool_list\"\n    )\n    config_without_init.exclude_init\
    \ = True\n    \n    benchmark_without = BooleanListBenchmark(config_without_init)\n\
    \    benchmark_without.run({\n        'size': sizes,\n        'operation': operations\n\
    \    })\n\nif __name__ == \"__main__\":\n    run_comprehensive_benchmark()\n \
    \   "
  dependsOn:
  - cp_library/perf/benchmark.py
  - cp_library/perf/generators.py
  - cp_library/ds/wavelet/bit_array_cls.py
  - cp_library/perf/plotters.py
  - cp_library/bit/popcnt32_fn.py
  - cp_library/ds/array/u32f_fn.py
  isVerificationFile: false
  path: perf/bool_list_benchmark.py
  requiredBy: []
  timestamp: '2025-07-09 08:31:42+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: perf/bool_list_benchmark.py
layout: document
redirect_from:
- /library/perf/bool_list_benchmark.py
- /library/perf/bool_list_benchmark.py.html
title: perf/bool_list_benchmark.py
---
