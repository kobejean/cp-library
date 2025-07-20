---
data:
  _extendedDependsOn:
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
  bundledCode: "\"\"\"\nBenchmark registry implementation following Single Responsibility\
    \ Principle.\n\"\"\"\n\nfrom typing import Callable, Dict, List, Union\n\"\"\"\
    \nInterfaces for the benchmark framework following SOLID principles.\n\"\"\"\n\
    \nfrom abc import ABC, abstractmethod\nfrom typing import Any, Callable, Dict,\
    \ List, Optional, Union\nfrom dataclasses import dataclass\n\n\n@dataclass\nclass\
    \ BenchmarkResult:\n    \"\"\"Immutable benchmark result value object\"\"\"\n\
    \    operation: str\n    size: int\n    implementation: str\n    time_ms: float\n\
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
    \        \"\"\"Execute benchmarks and return results\"\"\"\n        pass\n\n\n\
    class DefaultResultValidator(ResultValidator):\n    \"\"\"Default validator that\
    \ uses equality comparison\"\"\"\n    \n    def validate(self, expected, actual)\
    \ -> bool:\n        return expected == actual\n\n\nclass FunctionDataGenerator(DataGenerator):\n\
    \    \"\"\"Adapter to wrap function-based data generators\"\"\"\n    \n    def\
    \ __init__(self, func: Callable):\n        self.func = func\n    \n    def generate(self,\
    \ size: int, operation: str):\n        return self.func(size, operation)\n\n\n\
    class BenchmarkRegistryImpl(BenchmarkRegistry):\n    \"\"\"Implementation of benchmark\
    \ component registry\"\"\"\n    \n    def __init__(self):\n        self.implementations:\
    \ Dict[str, Dict[str, Callable]] = {}\n        self.data_generators: Dict[str,\
    \ DataGenerator] = {}\n        self.validators: Dict[str, ResultValidator] = {}\n\
    \        self.setups: Dict[str, Dict[str, Callable]] = {}\n        \n        #\
    \ Register default validator\n        self.default_validator = DefaultResultValidator()\n\
    \    \n    def register_implementation(self, name: str, func: Callable, operations:\
    \ List[str]) -> None:\n        \"\"\"Register a benchmark implementation\"\"\"\
    \n        for op in operations:\n            if op not in self.implementations:\n\
    \                self.implementations[op] = {}\n            self.implementations[op][name]\
    \ = func\n    \n    def register_data_generator(self, name: str, generator: DataGenerator)\
    \ -> None:\n        \"\"\"Register a data generator\"\"\"\n        self.data_generators[name]\
    \ = generator\n    \n    def register_validator(self, operation: str, validator:\
    \ ResultValidator) -> None:\n        \"\"\"Register a result validator\"\"\"\n\
    \        self.validators[operation] = validator\n    \n    def register_setup(self,\
    \ name: str, setup_func: Callable, operations: List[str]) -> None:\n        \"\
    \"\"Register a setup function\"\"\"\n        for op in operations:\n         \
    \   if op not in self.setups:\n                self.setups[op] = {}\n        \
    \    self.setups[op][name] = setup_func\n    \n    def get_implementations(self,\
    \ operation: str) -> Dict[str, Callable]:\n        \"\"\"Get implementations for\
    \ an operation\"\"\"\n        return self.implementations.get(operation, {})\n\
    \    \n    def get_data_generator(self, operation: str) -> DataGenerator:\n  \
    \      \"\"\"Get data generator for an operation\"\"\"\n        return self.data_generators.get(operation,\
    \ self.data_generators.get('default'))\n    \n    def get_validator(self, operation:\
    \ str) -> ResultValidator:\n        \"\"\"Get validator for an operation\"\"\"\
    \n        return self.validators.get(operation, self.default_validator)\n    \n\
    \    def get_setup(self, operation: str, implementation: str) -> Callable:\n \
    \       \"\"\"Get setup function for operation and implementation\"\"\"\n    \
    \    return self.setups.get(operation, {}).get(implementation)\n    \n    # Decorator\
    \ methods for backward compatibility\n    def data_generator(self, name: str =\
    \ \"default\"):\n        \"\"\"Decorator to register data generator function\"\
    \"\"\n        def decorator(func):\n            generator = FunctionDataGenerator(func)\n\
    \            self.register_data_generator(name, generator)\n            return\
    \ func\n        return decorator\n    \n    def implementation(self, name: str,\
    \ operations: Union[str, List[str]] = None):\n        \"\"\"Decorator to register\
    \ implementation function\"\"\"\n        if operations is None:\n            operations\
    \ = ['default']\n        elif isinstance(operations, str):\n            operations\
    \ = [operations]\n            \n        def decorator(func):\n            self.register_implementation(name,\
    \ func, operations)\n            return func\n        return decorator\n    \n\
    \    def validator(self, operation: str = \"default\"):\n        \"\"\"Decorator\
    \ to register custom validator function\"\"\"\n        def decorator(func):\n\
    \            class FunctionValidator(ResultValidator):\n                def validate(self,\
    \ expected, actual) -> bool:\n                    return func(expected, actual)\n\
    \            \n            self.register_validator(operation, FunctionValidator())\n\
    \            return func\n        return decorator\n    \n    def setup(self,\
    \ name: str, operations: Union[str, List[str]] = None):\n        \"\"\"Decorator\
    \ to register setup function\"\"\"\n        if operations is None:\n         \
    \   operations = ['default']\n        elif isinstance(operations, str):\n    \
    \        operations = [operations]\n            \n        def decorator(func):\n\
    \            self.register_setup(name, func, operations)\n            return func\n\
    \        return decorator\n"
  code: "\"\"\"\nBenchmark registry implementation following Single Responsibility\
    \ Principle.\n\"\"\"\n\nfrom typing import Callable, Dict, List, Union\nfrom cp_library.perf.interfaces\
    \ import BenchmarkRegistry, DataGenerator, ResultValidator\n\n\nclass DefaultResultValidator(ResultValidator):\n\
    \    \"\"\"Default validator that uses equality comparison\"\"\"\n    \n    def\
    \ validate(self, expected, actual) -> bool:\n        return expected == actual\n\
    \n\nclass FunctionDataGenerator(DataGenerator):\n    \"\"\"Adapter to wrap function-based\
    \ data generators\"\"\"\n    \n    def __init__(self, func: Callable):\n     \
    \   self.func = func\n    \n    def generate(self, size: int, operation: str):\n\
    \        return self.func(size, operation)\n\n\nclass BenchmarkRegistryImpl(BenchmarkRegistry):\n\
    \    \"\"\"Implementation of benchmark component registry\"\"\"\n    \n    def\
    \ __init__(self):\n        self.implementations: Dict[str, Dict[str, Callable]]\
    \ = {}\n        self.data_generators: Dict[str, DataGenerator] = {}\n        self.validators:\
    \ Dict[str, ResultValidator] = {}\n        self.setups: Dict[str, Dict[str, Callable]]\
    \ = {}\n        \n        # Register default validator\n        self.default_validator\
    \ = DefaultResultValidator()\n    \n    def register_implementation(self, name:\
    \ str, func: Callable, operations: List[str]) -> None:\n        \"\"\"Register\
    \ a benchmark implementation\"\"\"\n        for op in operations:\n          \
    \  if op not in self.implementations:\n                self.implementations[op]\
    \ = {}\n            self.implementations[op][name] = func\n    \n    def register_data_generator(self,\
    \ name: str, generator: DataGenerator) -> None:\n        \"\"\"Register a data\
    \ generator\"\"\"\n        self.data_generators[name] = generator\n    \n    def\
    \ register_validator(self, operation: str, validator: ResultValidator) -> None:\n\
    \        \"\"\"Register a result validator\"\"\"\n        self.validators[operation]\
    \ = validator\n    \n    def register_setup(self, name: str, setup_func: Callable,\
    \ operations: List[str]) -> None:\n        \"\"\"Register a setup function\"\"\
    \"\n        for op in operations:\n            if op not in self.setups:\n   \
    \             self.setups[op] = {}\n            self.setups[op][name] = setup_func\n\
    \    \n    def get_implementations(self, operation: str) -> Dict[str, Callable]:\n\
    \        \"\"\"Get implementations for an operation\"\"\"\n        return self.implementations.get(operation,\
    \ {})\n    \n    def get_data_generator(self, operation: str) -> DataGenerator:\n\
    \        \"\"\"Get data generator for an operation\"\"\"\n        return self.data_generators.get(operation,\
    \ self.data_generators.get('default'))\n    \n    def get_validator(self, operation:\
    \ str) -> ResultValidator:\n        \"\"\"Get validator for an operation\"\"\"\
    \n        return self.validators.get(operation, self.default_validator)\n    \n\
    \    def get_setup(self, operation: str, implementation: str) -> Callable:\n \
    \       \"\"\"Get setup function for operation and implementation\"\"\"\n    \
    \    return self.setups.get(operation, {}).get(implementation)\n    \n    # Decorator\
    \ methods for backward compatibility\n    def data_generator(self, name: str =\
    \ \"default\"):\n        \"\"\"Decorator to register data generator function\"\
    \"\"\n        def decorator(func):\n            generator = FunctionDataGenerator(func)\n\
    \            self.register_data_generator(name, generator)\n            return\
    \ func\n        return decorator\n    \n    def implementation(self, name: str,\
    \ operations: Union[str, List[str]] = None):\n        \"\"\"Decorator to register\
    \ implementation function\"\"\"\n        if operations is None:\n            operations\
    \ = ['default']\n        elif isinstance(operations, str):\n            operations\
    \ = [operations]\n            \n        def decorator(func):\n            self.register_implementation(name,\
    \ func, operations)\n            return func\n        return decorator\n    \n\
    \    def validator(self, operation: str = \"default\"):\n        \"\"\"Decorator\
    \ to register custom validator function\"\"\"\n        def decorator(func):\n\
    \            class FunctionValidator(ResultValidator):\n                def validate(self,\
    \ expected, actual) -> bool:\n                    return func(expected, actual)\n\
    \            \n            self.register_validator(operation, FunctionValidator())\n\
    \            return func\n        return decorator\n    \n    def setup(self,\
    \ name: str, operations: Union[str, List[str]] = None):\n        \"\"\"Decorator\
    \ to register setup function\"\"\"\n        if operations is None:\n         \
    \   operations = ['default']\n        elif isinstance(operations, str):\n    \
    \        operations = [operations]\n            \n        def decorator(func):\n\
    \            self.register_setup(name, func, operations)\n            return func\n\
    \        return decorator"
  dependsOn:
  - cp_library/perf/interfaces.py
  isVerificationFile: false
  path: cp_library/perf/registry.py
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
  timestamp: '2025-07-21 03:35:11+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/perf/registry.py
layout: document
redirect_from:
- /library/cp_library/perf/registry.py
- /library/cp_library/perf/registry.py.html
title: cp_library/perf/registry.py
---
