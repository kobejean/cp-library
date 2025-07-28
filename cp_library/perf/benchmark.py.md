---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: cp_library/perf/checksum.py
    title: cp_library/perf/checksum.py
  - icon: ':warning:'
    path: cp_library/perf/cli.py
    title: cp_library/perf/cli.py
  - icon: ':warning:'
    path: cp_library/perf/interfaces.py
    title: cp_library/perf/interfaces.py
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
  _extendedRequiredBy:
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
    , line 418, in visit\n    return visitor(node)\n  File \"/opt/hostedtoolcache/PyPy/3.10.16/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python_bundle.py\"\
    , line 64, in visit_ImportFrom\n    raise NotImplementedError(\"Relative imports\
    \ are not supported\")\nNotImplementedError: Relative imports are not supported\n"
  code: "\"\"\"\nDeclarative benchmark framework with minimal boilerplate.\nRefactored\
    \ to follow SOLID principles for better maintainability and extensibility.\n\n\
    Features:\n- Decorator-based benchmark registration\n- Automatic data generation\
    \ and validation\n- Built-in timing with warmup\n- Configurable operations and\
    \ sizes\n- JSON results and matplotlib plotting\n- Reduced timing overhead with\
    \ post-timing checksums\n- Pluggable renderers and output managers\n- Dependency\
    \ injection for extensibility\n\"\"\"\n\nimport statistics\nfrom dataclasses import\
    \ dataclass\nfrom typing import List, Optional\nfrom collections import defaultdict\n\
    \nfrom cp_library.perf.interfaces import (\n    BenchmarkRegistry, BenchmarkOrchestrator,\
    \ TimerInterface, \n    PlotRenderer, OutputManager, BenchmarkResult\n)\nfrom\
    \ cp_library.perf.registry import BenchmarkRegistryImpl\nfrom cp_library.perf.orchestrator\
    \ import BenchmarkOrchestratorImpl\nfrom cp_library.perf.timing import BenchmarkTimer\n\
    from cp_library.perf.output import JSONOutputManager, NoOpOutputManager\nfrom\
    \ cp_library.perf.renderers import CompositeRenderer\nfrom cp_library.perf.cli\
    \ import BenchmarkCLI, CLIConfig\n\n\n@dataclass\nclass BenchmarkConfig:\n   \
    \ \"\"\"Configuration for benchmark runs\"\"\"\n    name: str\n    sizes: List[int]\
    \ = None\n    operations: List[str] = None\n    iterations: int = 10\n    warmup:\
    \ int = 2\n    output_dir: str = \"./output/benchmark_results\"\n    save_results:\
    \ bool = True\n    plot_results: bool = True\n    plot_scale: str = \"loglog\"\
    \  # Options: \"loglog\", \"linear\", \"semilogx\", \"semilogy\"\n    progressive:\
    \ bool = True  # Show results operation by operation across sizes\n    # Profiling\
    \ mode (maintained for backward compatibility)\n    profile_mode: bool = False\n\
    \    profile_size: int = None\n    profile_operation: str = None\n    profile_implementation:\
    \ str = None\n    \n    def __post_init__(self):\n        if self.sizes is None:\n\
    \            self.sizes = [100, 1000, 10000, 100000]\n        if self.operations\
    \ is None:\n            self.operations = ['default']\n\n\nclass Benchmark:\n\
    \    \"\"\"\n    Declarative benchmark framework using dependency injection and\
    \ composition.\n    Follows SOLID principles for maintainability and extensibility.\n\
    \    \n    Backward compatible with existing benchmarks while providing enhanced\
    \ functionality.\n    \"\"\"\n    \n    def __init__(self, \n                \
    \ config: BenchmarkConfig,\n                 registry: BenchmarkRegistry = None,\n\
    \                 timer: TimerInterface = None,\n                 renderer: PlotRenderer\
    \ = None,\n                 output_manager: OutputManager = None):\n        self.config\
    \ = config\n        \n        # Dependency injection with sensible defaults for\
    \ backward compatibility\n        self.registry = registry or BenchmarkRegistryImpl()\n\
    \        self.timer = timer or BenchmarkTimer(config.iterations, config.warmup)\n\
    \        self.renderer = renderer or CompositeRenderer(config.plot_scale)\n  \
    \      self.output_manager = output_manager or (\n            JSONOutputManager(config.output_dir)\
    \ if config.save_results else NoOpOutputManager()\n        )\n        \n     \
    \   # Create orchestrator with injected dependencies\n        self.orchestrator\
    \ = BenchmarkOrchestratorImpl(\n            self.registry, \n            self.timer,\
    \ \n            self.output_manager if config.save_results else None\n       \
    \ )\n        \n        self.cli = BenchmarkCLI(config.name, config.operations,\
    \ config.sizes)\n        self.results: List[BenchmarkResult] = []\n    \n    def\
    \ parse_args(self):\n        \"\"\"Parse command line arguments and return configured\
    \ benchmark\"\"\"\n        cli_config = self.cli.parse_args()\n        self.cli.validate_args(cli_config)\n\
    \        \n        if cli_config.profile_mode:\n            return self.create_profile_benchmark(\n\
    \                cli_config.operation,\n                cli_config.size,\n   \
    \             cli_config.implementation\n            )\n        \n        # Apply\
    \ filters for normal mode\n        if cli_config.operation:\n            self.config.operations\
    \ = [cli_config.operation]\n        if cli_config.size:\n            self.config.sizes\
    \ = [cli_config.size]\n        \n        return self\n    \n    def create_profile_benchmark(self,\
    \ operation: str = None, size: int = None, implementation: str = None):\n    \
    \    \"\"\"Create a benchmark configured for profiling mode\"\"\"\n        profile_config\
    \ = BenchmarkConfig(\n            name=f\"{self.config.name}_profile\",\n    \
    \        sizes=[size] if size else [max(self.config.sizes)],\n            operations=[operation]\
    \ if operation else [self.config.operations[0]],\n            iterations=1,  #\
    \ Single iteration for profiling\n            warmup=0,      # No warmup for profiling\n\
    \            save_results=False,\n            plot_results=False,\n          \
    \  profile_mode=True,\n            profile_operation=operation,\n            profile_size=size,\n\
    \            profile_implementation=implementation\n        )\n        \n    \
    \    # Create profile benchmark with no-op output manager\n        profile_benchmark\
    \ = Benchmark(\n            profile_config,\n            self.registry,\n    \
    \        BenchmarkTimer(1, 0),  # Minimal timing for profiling\n            None,\
    \  # No plotting in profile mode\n            NoOpOutputManager()\n        )\n\
    \        \n        # If specific implementation requested, filter it\n       \
    \ if implementation:\n            profile_benchmark._filter_implementation = implementation\n\
    \        \n        return profile_benchmark\n    \n    def profile(self, operation:\
    \ str = None, size: int = None, implementation: str = None):\n        \"\"\"Create\
    \ a profiling version of this benchmark (backward compatibility)\"\"\"\n     \
    \   return self.create_profile_benchmark(operation, size, implementation)\n  \
    \  \n    def run(self):\n        \"\"\"Run benchmarks with the configured strategy\"\
    \"\"\n        if hasattr(self, '_filter_implementation') or self.config.profile_mode:\n\
    \            self._run_profile_mode()\n        else:\n            self._run_normal_mode()\n\
    \    \n    def _run_normal_mode(self):\n        \"\"\"Run normal benchmark mode\"\
    \"\"\n        print(f\"Running {self.config.name}\")\n        print(f\"Sizes:\
    \ {self.config.sizes}\")\n        print(f\"Operations: {self.config.operations}\"\
    )\n        print(\"=\"*80)\n        \n        # Execute benchmarks\n        self.results\
    \ = self.orchestrator.run_benchmarks(\n            self.config.operations, \n\
    \            self.config.sizes\n        )\n        \n        # Generate plots\
    \ if enabled\n        if self.config.plot_results and self.renderer:\n       \
    \     self.renderer.create_plots(self.results, self.config)\n        \n      \
    \  # Print summary\n        self._print_summary()\n    \n    def _run_profile_mode(self):\n\
    \        \"\"\"Run profiling mode with minimal overhead\"\"\"\n        operation\
    \ = self.config.operations[0]\n        size = self.config.sizes[0]\n        impl_name\
    \ = getattr(self, '_filter_implementation', None)\n        \n        print(f\"\
    PROFILING MODE: {self.config.name}\")\n        print(f\"Operation: {operation},\
    \ Size: {size}\")\n        if impl_name:\n            print(f\"Implementation:\
    \ {impl_name}\")\n        print(\"=\"*80)\n        print(\"Run with vmprof: vmprof\
    \ --web \" + ' '.join(__import__('sys').argv))\n        print(\"=\"*80)\n    \
    \    \n        # Generate test data\n        generator = self.registry.get_data_generator(operation)\n\
    \        if not generator:\n            raise ValueError(f\"No data generator\
    \ for operation: {operation}\")\n        \n        test_data = generator.generate(size,\
    \ operation)\n        \n        # Get implementations\n        impls = self.registry.get_implementations(operation)\n\
    \        if not impls:\n            raise ValueError(f\"No implementations for\
    \ operation: {operation}\")\n        \n        # Filter to specific implementation\
    \ if requested\n        if impl_name:\n            if impl_name not in impls:\n\
    \                raise ValueError(f\"Implementation '{impl_name}' not found for\
    \ operation '{operation}'\")\n            impls = {impl_name: impls[impl_name]}\n\
    \        \n        # Run with minimal overhead - no timing, no validation\n  \
    \      for name, func in impls.items():\n            print(f\"\\nRunning {name}...\"\
    )\n            __import__('sys').stdout.flush()\n            \n            # Setup\
    \ if needed\n            setup_func = self.registry.get_setup(operation, name)\n\
    \            if setup_func:\n                data = setup_func(test_data)\n  \
    \          else:\n                data = test_data\n            \n           \
    \ # Run the actual function (this is what vmprof will profile)\n            result\
    \ = func(data)\n            print(f\"Completed {name}, result checksum: {result}\"\
    )\n            __import__('sys').stdout.flush()\n    \n    def _print_summary(self):\n\
    \        \"\"\"Print performance summary\"\"\"\n        print(\"\\n\" + \"=\"\
    *80)\n        print(\"PERFORMANCE SUMMARY\")\n        print(\"=\"*80)\n      \
    \  \n        # Group by operation and size\n        by_operation_size = defaultdict(lambda:\
    \ defaultdict(lambda: defaultdict(float)))\n        for r in self.results:\n \
    \           if r.error is None and r.time_ms != float('inf'):\n              \
    \  by_operation_size[r.operation][r.size][r.implementation] = r.time_ms\n    \
    \    \n        print(f\"{'Operation':<15} {'Best Implementation':<20} {'Avg Time\
    \ (ms)':<15} {'Speedup':<10}\")\n        print(\"-\" * 70)\n        \n       \
    \ for op in sorted(by_operation_size.keys()):\n            # For each operation,\
    \ only compare implementations on sizes where ALL implementations ran\n      \
    \      common_times = defaultdict(list)\n            \n            for size, impl_times\
    \ in by_operation_size[op].items():\n                # Get all implementations\
    \ that have results for this operation\n                all_impls = set()\n  \
    \              for s in by_operation_size[op].values():\n                    all_impls.update(s.keys())\n\
    \                \n                # Only include this size if all implementations\
    \ have results\n                if len(impl_times) == len(all_impls):\n      \
    \              for impl, time_ms in impl_times.items():\n                    \
    \    common_times[impl].append(time_ms)\n            \n            # Calculate\
    \ averages only on common sizes\n            if common_times:\n              \
    \  avg_times = [(impl, statistics.mean(times)) \n                            for\
    \ impl, times in common_times.items()]\n                avg_times.sort(key=lambda\
    \ x: x[1])\n                \n                if avg_times:\n                \
    \    best_impl, best_time = avg_times[0]\n                    worst_time = avg_times[-1][1]\n\
    \                    speedup = worst_time / best_time if best_time > 0 else 0\n\
    \                    \n                    print(f\"{op:<15} {best_impl:<20} {best_time:<15.3f}\
    \ {speedup:<10.1f}x\")\n    \n    # Decorator methods for backward compatibility\n\
    \    def data_generator(self, name: str = \"default\"):\n        \"\"\"Decorator\
    \ to register data generator\"\"\"\n        return self.registry.data_generator(name)\n\
    \    \n    def implementation(self, name: str, operations=None):\n        \"\"\
    \"Decorator to register implementation\"\"\"\n        return self.registry.implementation(name,\
    \ operations)\n    \n    def validator(self, operation: str = \"default\"):\n\
    \        \"\"\"Decorator to register validator\"\"\"\n        return self.registry.validator(operation)\n\
    \    \n    def setup(self, name: str, operations=None):\n        \"\"\"Decorator\
    \ to register setup function\"\"\"\n        return self.registry.setup(name, operations)\n\
    \    \n    # Backward compatibility methods\n    def measure_time(self, func,\
    \ data, setup_func=None):\n        \"\"\"Measure execution time (backward compatibility)\"\
    \"\"\n        return self.timer.measure_time(func, data, setup_func)\n    \n \
    \   def validate_result(self, expected, actual, operation):\n        \"\"\"Validate\
    \ result (backward compatibility)\"\"\"\n        validator = self.registry.get_validator(operation)\n\
    \        return validator.validate(expected, actual)"
  dependsOn:
  - cp_library/perf/interfaces.py
  - cp_library/perf/registry.py
  - cp_library/perf/orchestrator.py
  - cp_library/perf/timing.py
  - cp_library/perf/output.py
  - cp_library/perf/renderers.py
  - cp_library/perf/cli.py
  - cp_library/perf/checksum.py
  isVerificationFile: false
  path: cp_library/perf/benchmark.py
  requiredBy:
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
documentation_of: cp_library/perf/benchmark.py
layout: document
redirect_from:
- /library/cp_library/perf/benchmark.py
- /library/cp_library/perf/benchmark.py.html
title: cp_library/perf/benchmark.py
---
