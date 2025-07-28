---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':warning:'
    path: cp_library/perf/benchmark.py
    title: cp_library/perf/benchmark.py
  - icon: ':warning:'
    path: cp_library/perf/orchestrator.py
    title: cp_library/perf/orchestrator.py
  - icon: ':warning:'
    path: cp_library/perf/output.py
    title: cp_library/perf/output.py
  - icon: ':warning:'
    path: cp_library/perf/registry.py
    title: cp_library/perf/registry.py
  - icon: ':warning:'
    path: cp_library/perf/renderers.py
    title: cp_library/perf/renderers.py
  - icon: ':warning:'
    path: cp_library/perf/timing.py
    title: cp_library/perf/timing.py
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
  bundledCode: "\"\"\"\nInterfaces for the benchmark framework following SOLID principles.\n\
    \"\"\"\n\nfrom abc import ABC, abstractmethod\nfrom typing import Any, Callable,\
    \ Dict, List, Optional, Union\nfrom dataclasses import dataclass\n\n\n@dataclass\n\
    class BenchmarkResult:\n    \"\"\"Immutable benchmark result value object\"\"\"\
    \n    operation: str\n    size: int\n    implementation: str\n    time_ms: float\n\
    \    correct: bool\n    error: Optional[str] = None\n\n\nclass TimerInterface(ABC):\n\
    \    \"\"\"Interface for timing implementations\"\"\"\n    \n    @abstractmethod\n\
    \    def measure_time(self, func: Callable, data: Any, setup_func: Callable =\
    \ None) -> tuple[Any, float]:\n        \"\"\"Measure execution time of a function\"\
    \"\"\n        pass\n\n\nclass PlotRenderer(ABC):\n    \"\"\"Interface for plot\
    \ rendering implementations\"\"\"\n    \n    @abstractmethod\n    def can_render(self)\
    \ -> bool:\n        \"\"\"Check if this renderer is available\"\"\"\n        pass\n\
    \    \n    @abstractmethod\n    def create_plots(self, results: List[BenchmarkResult],\
    \ config: Any) -> None:\n        \"\"\"Create plots from benchmark results\"\"\
    \"\n        pass\n\n\nclass ResultValidator(ABC):\n    \"\"\"Interface for result\
    \ validation strategies\"\"\"\n    \n    @abstractmethod\n    def validate(self,\
    \ expected: Any, actual: Any) -> bool:\n        \"\"\"Validate benchmark result\"\
    \"\"\n        pass\n\n\nclass DataGenerator(ABC):\n    \"\"\"Interface for data\
    \ generation strategies\"\"\"\n    \n    @abstractmethod\n    def generate(self,\
    \ size: int, operation: str) -> Any:\n        \"\"\"Generate test data for given\
    \ size and operation\"\"\"\n        pass\n\n\nclass OutputManager(ABC):\n    \"\
    \"\"Interface for output management\"\"\"\n    \n    @abstractmethod\n    def\
    \ save_results(self, results: List[BenchmarkResult], config: Any) -> None:\n \
    \       \"\"\"Save benchmark results\"\"\"\n        pass\n\n\nclass BenchmarkRegistry(ABC):\n\
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
    \        \"\"\"Execute benchmarks and return results\"\"\"\n        pass\n"
  code: "\"\"\"\nInterfaces for the benchmark framework following SOLID principles.\n\
    \"\"\"\n\nfrom abc import ABC, abstractmethod\nfrom typing import Any, Callable,\
    \ Dict, List, Optional, Union\nfrom dataclasses import dataclass\n\n\n@dataclass\n\
    class BenchmarkResult:\n    \"\"\"Immutable benchmark result value object\"\"\"\
    \n    operation: str\n    size: int\n    implementation: str\n    time_ms: float\n\
    \    correct: bool\n    error: Optional[str] = None\n\n\nclass TimerInterface(ABC):\n\
    \    \"\"\"Interface for timing implementations\"\"\"\n    \n    @abstractmethod\n\
    \    def measure_time(self, func: Callable, data: Any, setup_func: Callable =\
    \ None) -> tuple[Any, float]:\n        \"\"\"Measure execution time of a function\"\
    \"\"\n        pass\n\n\nclass PlotRenderer(ABC):\n    \"\"\"Interface for plot\
    \ rendering implementations\"\"\"\n    \n    @abstractmethod\n    def can_render(self)\
    \ -> bool:\n        \"\"\"Check if this renderer is available\"\"\"\n        pass\n\
    \    \n    @abstractmethod\n    def create_plots(self, results: List[BenchmarkResult],\
    \ config: Any) -> None:\n        \"\"\"Create plots from benchmark results\"\"\
    \"\n        pass\n\n\nclass ResultValidator(ABC):\n    \"\"\"Interface for result\
    \ validation strategies\"\"\"\n    \n    @abstractmethod\n    def validate(self,\
    \ expected: Any, actual: Any) -> bool:\n        \"\"\"Validate benchmark result\"\
    \"\"\n        pass\n\n\nclass DataGenerator(ABC):\n    \"\"\"Interface for data\
    \ generation strategies\"\"\"\n    \n    @abstractmethod\n    def generate(self,\
    \ size: int, operation: str) -> Any:\n        \"\"\"Generate test data for given\
    \ size and operation\"\"\"\n        pass\n\n\nclass OutputManager(ABC):\n    \"\
    \"\"Interface for output management\"\"\"\n    \n    @abstractmethod\n    def\
    \ save_results(self, results: List[BenchmarkResult], config: Any) -> None:\n \
    \       \"\"\"Save benchmark results\"\"\"\n        pass\n\n\nclass BenchmarkRegistry(ABC):\n\
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
    \        \"\"\"Execute benchmarks and return results\"\"\"\n        pass"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/perf/interfaces.py
  requiredBy:
  - cp_library/perf/registry.py
  - cp_library/perf/timing.py
  - cp_library/perf/output.py
  - cp_library/perf/benchmark.py
  - cp_library/perf/renderers.py
  - cp_library/perf/orchestrator.py
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
  timestamp: '2025-07-28 14:11:54+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/perf/interfaces.py
layout: document
redirect_from:
- /library/cp_library/perf/interfaces.py
- /library/cp_library/perf/interfaces.py.html
title: cp_library/perf/interfaces.py
---
