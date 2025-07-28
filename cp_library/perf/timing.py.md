---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: cp_library/perf/checksum.py
    title: cp_library/perf/checksum.py
  - icon: ':warning:'
    path: cp_library/perf/interfaces.py
    title: cp_library/perf/interfaces.py
  _extendedRequiredBy:
  - icon: ':warning:'
    path: cp_library/perf/benchmark.py
    title: cp_library/perf/benchmark.py
  - icon: ':warning:'
    path: perf/bit2.py
    title: perf/bit2.py
  - icon: ':warning:'
    path: perf/bit6.py
    title: perf/bit6.py
  - icon: ':warning:'
    path: perf/bool_list.py
    title: perf/bool_list.py
  - icon: ':warning:'
    path: perf/bytearray_decode.py
    title: perf/bytearray_decode.py
  - icon: ':warning:'
    path: perf/csr.py
    title: perf/csr.py
  - icon: ':warning:'
    path: perf/csr2.py
    title: perf/csr2.py
  - icon: ':warning:'
    path: perf/csr6.py
    title: perf/csr6.py
  - icon: ':warning:'
    path: perf/deque.py
    title: perf/deque.py
  - icon: ':warning:'
    path: perf/edge_list.py
    title: perf/edge_list.py
  - icon: ':warning:'
    path: perf/grid.py
    title: perf/grid.py
  - icon: ':warning:'
    path: perf/heap_csr.py
    title: perf/heap_csr.py
  - icon: ':warning:'
    path: perf/heap_view.py
    title: perf/heap_view.py
  - icon: ':warning:'
    path: perf/list2.py
    title: perf/list2.py
  - icon: ':warning:'
    path: perf/list6.py
    title: perf/list6.py
  - icon: ':warning:'
    path: perf/list_view.py
    title: perf/list_view.py
  - icon: ':warning:'
    path: perf/mlist.py
    title: perf/mlist.py
  - icon: ':warning:'
    path: perf/que.py
    title: perf/que.py
  - icon: ':warning:'
    path: perf/rank.py
    title: perf/rank.py
  - icon: ':warning:'
    path: perf/segtree2.py
    title: perf/segtree2.py
  - icon: ':warning:'
    path: perf/segtree6.py
    title: perf/segtree6.py
  - icon: ':warning:'
    path: perf/view2.py
    title: perf/view2.py
  - icon: ':warning:'
    path: perf/view6.py
    title: perf/view6.py
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "\"\"\"\nTiming and measurement utilities for benchmarks.\nSeparated\
    \ from main benchmark class for single responsibility.\n\"\"\"\n\nimport time\n\
    from typing import Any, Callable, Tuple\n\"\"\"\nInterfaces for the benchmark\
    \ framework following SOLID principles.\n\"\"\"\n\nfrom abc import ABC, abstractmethod\n\
    from typing import Any, Callable, Dict, List, Optional, Union\nfrom dataclasses\
    \ import dataclass\n\n\n@dataclass\nclass BenchmarkResult:\n    \"\"\"Immutable\
    \ benchmark result value object\"\"\"\n    operation: str\n    size: int\n   \
    \ implementation: str\n    time_ms: float\n    correct: bool\n    error: Optional[str]\
    \ = None\n\n\nclass TimerInterface(ABC):\n    \"\"\"Interface for timing implementations\"\
    \"\"\n    \n    @abstractmethod\n    def measure_time(self, func: Callable, data:\
    \ Any, setup_func: Callable = None) -> tuple[Any, float]:\n        \"\"\"Measure\
    \ execution time of a function\"\"\"\n        pass\n\n\nclass PlotRenderer(ABC):\n\
    \    \"\"\"Interface for plot rendering implementations\"\"\"\n    \n    @abstractmethod\n\
    \    def can_render(self) -> bool:\n        \"\"\"Check if this renderer is available\"\
    \"\"\n        pass\n    \n    @abstractmethod\n    def create_plots(self, results:\
    \ List[BenchmarkResult], config: Any) -> None:\n        \"\"\"Create plots from\
    \ benchmark results\"\"\"\n        pass\n\n\nclass ResultValidator(ABC):\n   \
    \ \"\"\"Interface for result validation strategies\"\"\"\n    \n    @abstractmethod\n\
    \    def validate(self, expected: Any, actual: Any) -> bool:\n        \"\"\"Validate\
    \ benchmark result\"\"\"\n        pass\n\n\nclass DataGenerator(ABC):\n    \"\"\
    \"Interface for data generation strategies\"\"\"\n    \n    @abstractmethod\n\
    \    def generate(self, size: int, operation: str) -> Any:\n        \"\"\"Generate\
    \ test data for given size and operation\"\"\"\n        pass\n\n\nclass OutputManager(ABC):\n\
    \    \"\"\"Interface for output management\"\"\"\n    \n    @abstractmethod\n\
    \    def save_results(self, results: List[BenchmarkResult], config: Any) -> None:\n\
    \        \"\"\"Save benchmark results\"\"\"\n        pass\n\n\nclass BenchmarkRegistry(ABC):\n\
    \    \"\"\"Interface for benchmark component registration\"\"\"\n    \n    @abstractmethod\n\
    \    def register_implementation(self, name: str, func: Callable, operations:\
    \ List[str]) -> None:\n        \"\"\"Register a benchmark implementation\"\"\"\
    \n        pass\n    \n    @abstractmethod\n    def register_data_generator(self,\
    \ name: str, generator: DataGenerator) -> None:\n        \"\"\"Register a data\
    \ generator\"\"\"\n        pass\n    \n    @abstractmethod\n    def register_validator(self,\
    \ operation: str, validator: ResultValidator) -> None:\n        \"\"\"Register\
    \ a result validator\"\"\"\n        pass\n    \n    @abstractmethod\n    def register_setup(self,\
    \ name: str, setup_func: Callable, operations: List[str]) -> None:\n        \"\
    \"\"Register a setup function\"\"\"\n        pass\n\n\nclass BenchmarkOrchestrator(ABC):\n\
    \    \"\"\"Interface for benchmark execution orchestration\"\"\"\n    \n    @abstractmethod\n\
    \    def run_benchmarks(self, operations: List[str], sizes: List[int]) -> List[BenchmarkResult]:\n\
    \        \"\"\"Execute benchmarks and return results\"\"\"\n        pass\n\"\"\
    \"\nChecksum utilities for benchmark validation.\nProvides consistent ways to\
    \ compute checksums across benchmarks.\n\"\"\"\n\n\n\ndef update_checksum(current:\
    \ int, value: int) -> int:\n    \"\"\"Update checksum with a single value using\
    \ hash-like function.\"\"\"\n    return (current * 31 + value) & 0xFFFFFFFF\n\n\
    \ndef result_checksum(result: Any) -> Any:\n    \"\"\"\n    Calculate checksum\
    \ for benchmark result with fallback for non-hashable types.\n    \n    This function\
    \ tries to create a consistent hash for any type of result,\n    with intelligent\
    \ fallbacks for common non-hashable types like lists, sets, and dicts.\n    \n\
    \    Args:\n        result: The result to checksum (can be any type)\n       \
    \ \n    Returns:\n        Hash value if successful, original result if all fallbacks\
    \ fail\n    \"\"\"\n    # Try direct hash first (fastest path for hashable objects)\n\
    \    try:\n        return hash(result)\n    except TypeError:\n        pass\n\
    \    \n    # Try common fallback conversions for non-hashable types\n    try:\n\
    \        if isinstance(result, dict):\n            # Convert dict to sorted tuple\
    \ of items for consistent ordering\n            return hash(tuple(sorted(result.items())))\n\
    \        elif isinstance(result, set):\n            # Convert set to sorted tuple\
    \ for consistent ordering\n            return hash(tuple(sorted(result)))\n  \
    \      elif _is_iterable_not_string(result):\n            # Convert other iterables\
    \ (lists, etc.) to tuple\n            return hash(tuple(result))\n        elif\
    \ hasattr(result, '__dict__'):\n            # Convert objects with attributes\
    \ to tuple of sorted items\n            return hash(tuple(sorted(result.__dict__.items())))\n\
    \        else:\n            # For other types, convert to string as last resort\n\
    \            return hash(str(result))\n    except (TypeError, RecursionError):\n\
    \        # If all fallbacks fail, return the original result\n        # The validation\
    \ logic will handle it\n        return result\n\n\ndef _is_iterable_not_string(obj:\
    \ Any) -> bool:\n    \"\"\"\n    Check if object is iterable but not a string\
    \ or bytes.\n    \n    Uses both __iter__ and __getitem__ checks to catch more\
    \ iterable types\n    while excluding strings and bytes which should be handled\
    \ differently.\n    \"\"\"\n    return (\n        (hasattr(obj, '__iter__') or\
    \ hasattr(obj, '__getitem__')) \n        and not isinstance(obj, (str, bytes))\n\
    \    )\n\n\nclass BenchmarkTimer(TimerInterface):\n    \"\"\"Handles timing and\
    \ measurement of benchmark functions\"\"\"\n    \n    def __init__(self, iterations:\
    \ int = 10, warmup: int = 2):\n        self.iterations = iterations\n        self.warmup\
    \ = warmup\n    \n    def measure_time(self, func: Callable, data: Any, setup_func:\
    \ Callable = None) -> Tuple[Any, float]:\n        \"\"\"Measure execution time\
    \ with warmup and optional setup\"\"\"\n        # Warmup runs\n        for _ in\
    \ range(self.warmup):\n            try:\n                if setup_func:\n    \
    \                setup_data = setup_func(data)\n                    func(setup_data)\n\
    \                else:\n                    func(data)\n            except Exception:\n\
    \                # If warmup fails, let the main measurement handle the error\n\
    \                break\n        \n        # Actual measurement\n        start\
    \ = time.perf_counter()\n        for _ in range(self.iterations):\n          \
    \  if setup_func:\n                setup_data = setup_func(data)\n           \
    \     result = func(setup_data)\n            else:\n                result = func(data)\n\
    \        elapsed_ms = (time.perf_counter() - start) * 1000 / self.iterations\n\
    \        \n        # Calculate checksum after timing with fallback for non-hashable\
    \ types\n        # This reduces overhead during the timed section\n        checksum\
    \ = result_checksum(result)\n        \n        return checksum, elapsed_ms\n"
  code: "\"\"\"\nTiming and measurement utilities for benchmarks.\nSeparated from\
    \ main benchmark class for single responsibility.\n\"\"\"\n\nimport time\nfrom\
    \ typing import Any, Callable, Tuple\nfrom cp_library.perf.interfaces import TimerInterface\n\
    from cp_library.perf.checksum import result_checksum\n\n\nclass BenchmarkTimer(TimerInterface):\n\
    \    \"\"\"Handles timing and measurement of benchmark functions\"\"\"\n    \n\
    \    def __init__(self, iterations: int = 10, warmup: int = 2):\n        self.iterations\
    \ = iterations\n        self.warmup = warmup\n    \n    def measure_time(self,\
    \ func: Callable, data: Any, setup_func: Callable = None) -> Tuple[Any, float]:\n\
    \        \"\"\"Measure execution time with warmup and optional setup\"\"\"\n \
    \       # Warmup runs\n        for _ in range(self.warmup):\n            try:\n\
    \                if setup_func:\n                    setup_data = setup_func(data)\n\
    \                    func(setup_data)\n                else:\n               \
    \     func(data)\n            except Exception:\n                # If warmup fails,\
    \ let the main measurement handle the error\n                break\n        \n\
    \        # Actual measurement\n        start = time.perf_counter()\n        for\
    \ _ in range(self.iterations):\n            if setup_func:\n                setup_data\
    \ = setup_func(data)\n                result = func(setup_data)\n            else:\n\
    \                result = func(data)\n        elapsed_ms = (time.perf_counter()\
    \ - start) * 1000 / self.iterations\n        \n        # Calculate checksum after\
    \ timing with fallback for non-hashable types\n        # This reduces overhead\
    \ during the timed section\n        checksum = result_checksum(result)\n     \
    \   \n        return checksum, elapsed_ms"
  dependsOn:
  - cp_library/perf/interfaces.py
  - cp_library/perf/checksum.py
  isVerificationFile: false
  path: cp_library/perf/timing.py
  requiredBy:
  - cp_library/perf/benchmark.py
  - perf/bool_list.py
  - perf/view2.py
  - perf/heap_view.py
  - perf/list_view.py
  - perf/mlist.py
  - perf/que.py
  - perf/list6.py
  - perf/grid.py
  - perf/edge_list.py
  - perf/csr.py
  - perf/bit6.py
  - perf/deque.py
  - perf/segtree2.py
  - perf/view6.py
  - perf/csr6.py
  - perf/segtree6.py
  - perf/csr2.py
  - perf/bit2.py
  - perf/rank.py
  - perf/list2.py
  - perf/heap_csr.py
  - perf/bytearray_decode.py
  timestamp: '2025-07-28 19:59:52+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/perf/timing.py
layout: document
redirect_from:
- /library/cp_library/perf/timing.py
- /library/cp_library/perf/timing.py.html
title: cp_library/perf/timing.py
---
