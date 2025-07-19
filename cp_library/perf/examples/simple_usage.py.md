---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: cp_library/perf/benchmark.py
    title: cp_library/perf/benchmark.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "\"\"\"Simple example of using the benchmarking framework\"\"\"\n\n\
    \"\"\"\nDeclarative benchmark framework with minimal boilerplate.\n\nFeatures:\n\
    - Decorator-based benchmark registration\n- Automatic data generation and validation\n\
    - Built-in timing with warmup\n- Configurable operations and sizes\n- JSON results\
    \ and matplotlib plotting\n\"\"\"\n\nimport time\nimport json\nimport statistics\n\
    import sys\nimport argparse\nfrom typing import Dict, List, Any, Callable, Union\n\
    from dataclasses import dataclass\nfrom pathlib import Path\nfrom collections\
    \ import defaultdict\n\n@dataclass\nclass BenchmarkConfig:\n    \"\"\"Configuration\
    \ for benchmark runs\"\"\"\n    name: str\n    sizes: List[int] = None\n    operations:\
    \ List[str] = None\n    iterations: int = 10\n    warmup: int = 2\n    output_dir:\
    \ str = \"./output/benchmark_results\"\n    save_results: bool = True\n    plot_results:\
    \ bool = True\n    plot_scale: str = \"loglog\"  # Options: \"loglog\", \"linear\"\
    , \"semilogx\", \"semilogy\"\n    progressive: bool = True  # Show results operation\
    \ by operation across sizes\n    # Profiling mode\n    profile_mode: bool = False\n\
    \    profile_size: int = None\n    profile_operation: str = None\n    profile_implementation:\
    \ str = None\n    \n    def __post_init__(self):\n        if self.sizes is None:\n\
    \            self.sizes = [100, 1000, 10000, 100000]\n        if self.operations\
    \ is None:\n            self.operations = ['default']\n\nclass Benchmark:\n  \
    \  \"\"\"Declarative benchmark framework using decorators\"\"\"\n    \n    def\
    \ __init__(self, config: BenchmarkConfig):\n        self.config = config\n   \
    \     self.data_generators = {}\n        self.implementations = {}\n        self.validators\
    \ = {}\n        self.setups = {}\n        self.results = []\n    \n    def profile(self,\
    \ operation: str = None, size: int = None, implementation: str = None):\n    \
    \    \"\"\"Create a profiling version of this benchmark\"\"\"\n        profile_config\
    \ = BenchmarkConfig(\n            name=f\"{self.config.name}_profile\",\n    \
    \        sizes=self.config.sizes,\n            operations=self.config.operations,\n\
    \            profile_mode=True,\n            profile_operation=operation,\n  \
    \          profile_size=size,\n            profile_implementation=implementation,\n\
    \            save_results=False,\n            plot_results=False\n        )\n\
    \        \n        profile_benchmark = Benchmark(profile_config)\n        profile_benchmark.data_generators\
    \ = self.data_generators\n        profile_benchmark.implementations = self.implementations\n\
    \        profile_benchmark.validators = self.validators\n        profile_benchmark.setups\
    \ = self.setups\n        \n        return profile_benchmark\n    \n    def parse_args(self):\n\
    \        \"\"\"Parse command line arguments for profiling mode\"\"\"\n       \
    \ parser = argparse.ArgumentParser(\n            description=f\"Benchmark {self.config.name}\
    \ with optional profiling mode\",\n            formatter_class=argparse.RawDescriptionHelpFormatter,\n\
    \            epilog=\"\"\"\nExamples:\n  # Normal benchmark mode\n  python benchmark.py\n\
    \  \n  # Profile specific operation and implementation\n  python benchmark.py\
    \ --profile --operation random_access --implementation grid\n  \n  # Profile with\
    \ specific size\n  python benchmark.py --profile --size 1000000\n  \n  # Profile\
    \ all implementations of an operation\n  python benchmark.py --profile --operation\
    \ construction\n\"\"\"\n        )\n        \n        parser.add_argument('--profile',\
    \ action='store_true',\n                          help='Run in profiling mode\
    \ (minimal overhead for profilers)')\n        parser.add_argument('--operation',\
    \ type=str, \n                          help=f'Operation to profile. Options:\
    \ {\", \".join(self.config.operations)}')\n        parser.add_argument('--size',\
    \ type=int,\n                          help=f'Size to profile. Options: {\", \"\
    .join(map(str, self.config.sizes))}')\n        parser.add_argument('--implementation',\
    \ type=str,\n                          help='Specific implementation to profile\
    \ (default: all)')\n        \n        args = parser.parse_args()\n        \n \
    \       # If profile mode requested, return a profiling benchmark\n        if\
    \ args.profile:\n            return self.profile(\n                operation=args.operation,\n\
    \                size=args.size,\n                implementation=args.implementation\n\
    \            )\n        \n        # Otherwise return self for normal mode\n  \
    \      return self\n        \n    def data_generator(self, name: str = \"default\"\
    ):\n        \"\"\"Decorator to register data generator\"\"\"\n        def decorator(func):\n\
    \            self.data_generators[name] = func\n            return func\n    \
    \    return decorator\n    \n    def implementation(self, name: str, operations:\
    \ Union[str, List[str]] = None):\n        \"\"\"Decorator to register implementation\"\
    \"\"\n        if operations is None:\n            operations = ['default']\n \
    \       elif isinstance(operations, str):\n            operations = [operations]\n\
    \            \n        def decorator(func):\n            for op in operations:\n\
    \                if op not in self.implementations:\n                    self.implementations[op]\
    \ = {}\n                self.implementations[op][name] = func\n            return\
    \ func\n        return decorator\n    \n    def validator(self, operation: str\
    \ = \"default\"):\n        \"\"\"Decorator to register custom validator\"\"\"\n\
    \        def decorator(func):\n            self.validators[operation] = func\n\
    \            return func\n        return decorator\n    \n    def setup(self,\
    \ name: str, operations: Union[str, List[str]] = None):\n        \"\"\"Decorator\
    \ to register setup function that runs before timing\"\"\"\n        if operations\
    \ is None:\n            operations = ['default']\n        elif isinstance(operations,\
    \ str):\n            operations = [operations]\n            \n        def decorator(func):\n\
    \            for op in operations:\n                if op not in self.setups:\n\
    \                    self.setups[op] = {}\n                self.setups[op][name]\
    \ = func\n            return func\n        return decorator\n    \n    def measure_time(self,\
    \ func: Callable, data: Any, setup_func: Callable = None) -> tuple[Any, float]:\n\
    \        \"\"\"Measure execution time with warmup and optional setup\"\"\"\n \
    \       # Warmup runs\n        for _ in range(self.config.warmup):\n         \
    \   try:\n                if setup_func:\n                    setup_data = setup_func(data)\n\
    \                    func(setup_data)\n                else:\n               \
    \     func(data)\n            except Exception:\n                # If warmup fails,\
    \ let the main measurement handle the error\n                break\n        \n\
    \        # Actual measurement\n        start = time.perf_counter()\n        for\
    \ _ in range(self.config.iterations):\n            if setup_func:\n          \
    \      setup_data = setup_func(data)\n                result = func(setup_data)\n\
    \            else:\n                result = func(data)\n        elapsed_ms =\
    \ (time.perf_counter() - start) * 1000 / self.config.iterations\n        \n  \
    \      return result, elapsed_ms\n    \n    def validate_result(self, expected:\
    \ Any, actual: Any, operation: str) -> bool:\n        \"\"\"Validate result using\
    \ custom validator or default comparison\"\"\"\n        if operation in self.validators:\n\
    \            return self.validators[operation](expected, actual)\n        return\
    \ expected == actual\n    \n    def run(self):\n        \"\"\"Run all benchmarks\"\
    \"\"\n        if self.config.profile_mode:\n            self._run_profile_mode()\n\
    \        else:\n            self._run_normal_mode()\n    \n    def _run_normal_mode(self):\n\
    \        \"\"\"Run normal benchmark mode\"\"\"\n        print(f\"Running {self.config.name}\"\
    )\n        print(f\"Sizes: {self.config.sizes}\")\n        print(f\"Operations:\
    \ {self.config.operations}\")\n        print(\"=\"*80)\n        \n        # Always\
    \ show progressive results: operation by operation across all sizes\n        for\
    \ operation in self.config.operations:\n            for size in self.config.sizes:\n\
    \                self._run_single(operation, size)\n        \n        # Save and\
    \ plot results\n        if self.config.save_results:\n            self._save_results()\n\
    \        \n        if self.config.plot_results:\n            self._plot_results()\n\
    \        \n        # Print summary\n        self._print_summary()\n    \n    def\
    \ _run_profile_mode(self):\n        \"\"\"Run profiling mode with minimal overhead\
    \ for use with vmprof\"\"\"\n        operation = self.config.profile_operation\
    \ or self.config.operations[0]\n        size = self.config.profile_size or max(self.config.sizes)\n\
    \        impl_name = self.config.profile_implementation\n        \n        print(f\"\
    PROFILING MODE: {self.config.name}\")\n        print(f\"Operation: {operation},\
    \ Size: {size}\")\n        if impl_name:\n            print(f\"Implementation:\
    \ {impl_name}\")\n        print(\"=\"*80)\n        print(\"Run with vmprof: vmprof\
    \ --web \" + ' '.join(sys.argv))\n        print(\"=\"*80)\n        \n        #\
    \ Generate test data\n        generator = self.data_generators.get(operation,\
    \ self.data_generators.get('default'))\n        if not generator:\n          \
    \  raise ValueError(f\"No data generator for operation: {operation}\")\n     \
    \   \n        test_data = generator(size, operation)\n        \n        # Get\
    \ implementations\n        impls = self.implementations.get(operation, {})\n \
    \       if not impls:\n            raise ValueError(f\"No implementations for\
    \ operation: {operation}\")\n        \n        # Filter to specific implementation\
    \ if requested\n        if impl_name:\n            if impl_name not in impls:\n\
    \                raise ValueError(f\"Implementation '{impl_name}' not found for\
    \ operation '{operation}'\")\n            impls = {impl_name: impls[impl_name]}\n\
    \        \n        # Run with minimal overhead - no timing, no validation\n  \
    \      for name, func in impls.items():\n            print(f\"\\nRunning {name}...\"\
    )\n            sys.stdout.flush()\n            \n            # Setup if needed\n\
    \            setup_func = self.setups.get(operation, {}).get(name)\n         \
    \   if setup_func:\n                data = setup_func(test_data)\n           \
    \ else:\n                data = test_data\n            \n            # Run the\
    \ actual function (this is what vmprof will profile)\n            result = func(data)\n\
    \            print(f\"Completed {name}, result checksum: {result}\")\n       \
    \     sys.stdout.flush()\n    \n    def _run_single(self, operation: str, size:\
    \ int):\n        \"\"\"Run a single operation/size combination\"\"\"\n       \
    \ print(f\"\\nOperation: {operation}, Size: {size}\")\n        print(\"-\" * 50)\n\
    \        sys.stdout.flush()\n        \n        # Generate test data\n        generator\
    \ = self.data_generators.get(operation, \n                                   \
    \        self.data_generators.get('default'))\n        if not generator:\n   \
    \         raise ValueError(f\"No data generator for operation: {operation}\")\n\
    \        \n        test_data = generator(size, operation)\n        \n        #\
    \ Get implementations for this operation\n        impls = self.implementations.get(operation,\
    \ {})\n        if not impls:\n            print(f\"No implementations for operation:\
    \ {operation}\")\n            return\n        \n        # Get setup functions\
    \ for this operation\n        setups = self.setups.get(operation, {})\n      \
    \  \n        # Run reference implementation first\n        ref_name, ref_impl\
    \ = next(iter(impls.items()))\n        ref_setup = setups.get(ref_name)\n    \
    \    expected_result, _ = self.measure_time(ref_impl, test_data, ref_setup)\n\
    \        \n        # Run all implementations\n        for impl_name, impl_func\
    \ in impls.items():\n            try:\n                setup_func = setups.get(impl_name)\n\
    \                result, time_ms = self.measure_time(impl_func, test_data, setup_func)\n\
    \                correct = self.validate_result(expected_result, result, operation)\n\
    \                \n                # Store result\n                self.results.append({\n\
    \                    'operation': operation,\n                    'size': size,\n\
    \                    'implementation': impl_name,\n                    'time_ms':\
    \ time_ms,\n                    'correct': correct,\n                    'error':\
    \ None\n                })\n                \n                status = \"OK\"\
    \ if correct else \"FAIL\"\n                print(f\"  {impl_name:<20} {time_ms:>8.3f}\
    \ ms  {status}\")\n                sys.stdout.flush()\n                \n    \
    \        except Exception as e:\n                self.results.append({\n     \
    \               'operation': operation,\n                    'size': size,\n \
    \                   'implementation': impl_name,\n                    'time_ms':\
    \ float('inf'),\n                    'correct': False,\n                    'error':\
    \ str(e)\n                })\n                print(f\"  {impl_name:<20} ERROR:\
    \ {str(e)[:40]}\")\n                sys.stdout.flush()\n    \n    def _save_results(self):\n\
    \        \"\"\"Save results to JSON\"\"\"\n        output_dir = Path(self.config.output_dir)\n\
    \        output_dir.mkdir(parents=True, exist_ok=True)\n        \n        filename\
    \ = output_dir / f\"{self.config.name}_{int(time.time())}.json\"\n        with\
    \ open(filename, 'w') as f:\n            json.dump(self.results, f, indent=2)\n\
    \        print(f\"\\nResults saved to {filename}\")\n    \n    def _plot_results(self):\n\
    \        \"\"\"Generate plots using matplotlib if available\"\"\"\n        try:\n\
    \            import matplotlib.pyplot as plt\n            \n            output_dir\
    \ = Path(self.config.output_dir)\n            output_dir.mkdir(parents=True, exist_ok=True)\n\
    \            \n            # Group and prepare data for plotting\n           \
    \ data_by_op = self._group_results_by_operation()\n            \n            #\
    \ Create plots for each operation\n            for operation, operation_data in\
    \ data_by_op.items():\n                self._create_performance_plot(plt, operation,\
    \ operation_data, output_dir)\n                \n        except ImportError:\n\
    \            print(\"Matplotlib not available - skipping plots\")\n        except\
    \ Exception as e:\n            print(f\"Plotting failed: {e}\")\n    \n    def\
    \ _group_results_by_operation(self) -> Dict[str, Dict[int, List[Dict[str, Any]]]]:\n\
    \        \"\"\"Group results by operation and size for plotting\"\"\"\n      \
    \  data_by_op = defaultdict(lambda: defaultdict(list))\n        for r in self.results:\n\
    \            if r['time_ms'] != float('inf') and r['correct']:\n             \
    \   data_by_op[r['operation']][r['size']].append({\n                    'implementation':\
    \ r['implementation'],\n                    'time_ms': r['time_ms']\n        \
    \        })\n        return data_by_op\n    \n    def _create_performance_plot(self,\
    \ plt, operation: str, operation_data: Dict[int, List[Dict[str, Any]]], output_dir:\
    \ Path):\n        \"\"\"Create a performance plot for a single operation\"\"\"\
    \n        sizes = sorted(operation_data.keys())\n        implementations = set()\n\
    \        for size_data in operation_data.values():\n            for entry in size_data:\n\
    \                implementations.add(entry['implementation'])\n        \n    \
    \    implementations = sorted(implementations)\n        \n        plt.figure(figsize=(10,\
    \ 6))\n        for impl in implementations:\n            impl_times = []\n   \
    \         impl_sizes = []\n            for size in sizes:\n                times\
    \ = [entry['time_ms'] for entry in operation_data[size] \n                   \
    \     if entry['implementation'] == impl]\n                if times:\n       \
    \             impl_times.append(statistics.mean(times))\n                    impl_sizes.append(size)\n\
    \            \n            if impl_times:\n                plt.plot(impl_sizes,\
    \ impl_times, 'o-', label=impl)\n        \n        plt.xlabel('Input Size')\n\
    \        plt.ylabel('Time (ms)')\n        plt.title(f'{self.config.name} - {operation}\
    \ Operation')\n        plt.legend()\n        plt.grid(True, alpha=0.3)\n     \
    \   \n        # Apply the configured scaling\n        if self.config.plot_scale\
    \ == \"loglog\":\n            plt.loglog()\n        elif self.config.plot_scale\
    \ == \"linear\":\n            pass  # Default linear scale\n        elif self.config.plot_scale\
    \ == \"semilogx\":\n            plt.semilogx()\n        elif self.config.plot_scale\
    \ == \"semilogy\":\n            plt.semilogy()\n        else:\n            # Default\
    \ to loglog if invalid option\n            plt.loglog()\n        \n        plot_file\
    \ = output_dir / f\"{self.config.name}_{operation}_performance.png\"\n       \
    \ plt.savefig(plot_file, dpi=300, bbox_inches='tight')\n        plt.close()\n\
    \        print(f\"Plot saved: {plot_file}\")\n    \n    def _print_summary(self):\n\
    \        \"\"\"Print performance summary\"\"\"\n        print(\"\\n\" + \"=\"\
    *80)\n        print(\"PERFORMANCE SUMMARY\")\n        print(\"=\"*80)\n      \
    \  \n        # Group by operation\n        by_operation = defaultdict(lambda:\
    \ defaultdict(list))\n        for r in self.results:\n            if r['error']\
    \ is None and r['time_ms'] != float('inf'):\n                by_operation[r['operation']][r['implementation']].append(r['time_ms'])\n\
    \        \n        print(f\"{'Operation':<15} {'Best Implementation':<20} {'Avg\
    \ Time (ms)':<15} {'Speedup':<10}\")\n        print(\"-\" * 70)\n        \n  \
    \      for op, impl_times in sorted(by_operation.items()):\n            # Calculate\
    \ averages\n            avg_times = [(impl, statistics.mean(times)) \n       \
    \                 for impl, times in impl_times.items()]\n            avg_times.sort(key=lambda\
    \ x: x[1])\n            \n            if avg_times:\n                best_impl,\
    \ best_time = avg_times[0]\n                worst_time = avg_times[-1][1]\n  \
    \              speedup = worst_time / best_time if best_time > 0 else 0\n    \
    \            \n                print(f\"{op:<15} {best_impl:<20} {best_time:<15.3f}\
    \ {speedup:<10.1f}x\")\n\n\nfrom cp_library.perf.generators import RandomArrayGenerator,\
    \ SortedArrayGenerator\n\nclass SimpleSortBenchmark(Benchmark):\n    \"\"\"Example\
    \ benchmark comparing different sorting approaches\"\"\"\n    \n    def generate_test_cases(self,\
    \ param_grid: Dict[str, List[Any]]) -> List[TestCase]:\n        test_cases = []\n\
    \        \n        for size in param_grid['size']:\n            # Random data\n\
    \            random_gen = RandomArrayGenerator()\n            test_cases.append(TestCase(\n\
    \                name=f\"random_size_{size}\",\n                params={'size':\
    \ size, 'type': 'random'},\n                data=random_gen.generate(size)\n \
    \           ))\n            \n            # Sorted data\n            sorted_gen\
    \ = SortedArrayGenerator()\n            test_cases.append(TestCase(\n        \
    \        name=f\"sorted_size_{size}\",\n                params={'size': size,\
    \ 'type': 'sorted'},\n                data=sorted_gen.generate(size)\n       \
    \     ))\n            \n            # Reverse sorted\n            reverse_gen\
    \ = SortedArrayGenerator(reverse=True)\n            test_cases.append(TestCase(\n\
    \                name=f\"reverse_size_{size}\",\n                params={'size':\
    \ size, 'type': 'reverse'},\n                data=reverse_gen.generate(size)\n\
    \            ))\n        \n        return test_cases\n    \n    def get_implementations(self)\
    \ -> Dict[str, Callable]:\n        \"\"\"Different sorting implementations to\
    \ compare\"\"\"\n        return {\n            'builtin_sort': lambda data: sorted(data),\n\
    \            'list_sort': lambda data: (data.copy(), data.sort())[0],\n      \
    \      'custom_sort': lambda data: self._custom_sort(data.copy())\n        }\n\
    \    \n    def _custom_sort(self, data):\n        \"\"\"Example custom sorting\
    \ implementation\"\"\"\n        # Simple selection sort for demonstration\n  \
    \      n = len(data)\n        for i in range(n):\n            min_idx = i\n  \
    \          for j in range(i + 1, n):\n                if data[j] < data[min_idx]:\n\
    \                    min_idx = j\n            data[i], data[min_idx] = data[min_idx],\
    \ data[i]\n        return data\n\ndef main():\n    \"\"\"Run the example benchmark\"\
    \"\"\n    \n    # Create configuration\n    config = BenchmarkConfig(\n      \
    \  name=\"sorting_example\",\n        iterations=5,\n        warmup=1,\n     \
    \   save_results=True,\n        plot_results=False,  # Set to True if you have\
    \ matplotlib\n        output_dir=\"./benchmark_results/example\"\n    )\n    \n\
    \    # Create and run benchmark\n    benchmark = SimpleSortBenchmark(config)\n\
    \    \n    # Small sizes for the example\n    param_grid = {\n        'size':\
    \ [10, 50, 100, 500]\n    }\n    \n    benchmark.run(param_grid)\n    \n    #\
    \ Access results programmatically\n    print(\"\\nAccessing results programmatically:\"\
    )\n    for result in benchmark.results[:5]:  # First 5 results\n        if result.error\
    \ is None:\n            print(f\"  {result.test_case.name}: {result.implementation}\
    \ = {result.time_ms:.3f}ms\")\n\nif __name__ == \"__main__\":\n    main()\n"
  code: "\"\"\"Simple example of using the benchmarking framework\"\"\"\n\nfrom cp_library.perf.benchmark\
    \ import Benchmark, BenchmarkConfig, TestCase\nfrom cp_library.perf.generators\
    \ import RandomArrayGenerator, SortedArrayGenerator\nfrom typing import Dict,\
    \ List, Any, Callable\n\nclass SimpleSortBenchmark(Benchmark):\n    \"\"\"Example\
    \ benchmark comparing different sorting approaches\"\"\"\n    \n    def generate_test_cases(self,\
    \ param_grid: Dict[str, List[Any]]) -> List[TestCase]:\n        test_cases = []\n\
    \        \n        for size in param_grid['size']:\n            # Random data\n\
    \            random_gen = RandomArrayGenerator()\n            test_cases.append(TestCase(\n\
    \                name=f\"random_size_{size}\",\n                params={'size':\
    \ size, 'type': 'random'},\n                data=random_gen.generate(size)\n \
    \           ))\n            \n            # Sorted data\n            sorted_gen\
    \ = SortedArrayGenerator()\n            test_cases.append(TestCase(\n        \
    \        name=f\"sorted_size_{size}\",\n                params={'size': size,\
    \ 'type': 'sorted'},\n                data=sorted_gen.generate(size)\n       \
    \     ))\n            \n            # Reverse sorted\n            reverse_gen\
    \ = SortedArrayGenerator(reverse=True)\n            test_cases.append(TestCase(\n\
    \                name=f\"reverse_size_{size}\",\n                params={'size':\
    \ size, 'type': 'reverse'},\n                data=reverse_gen.generate(size)\n\
    \            ))\n        \n        return test_cases\n    \n    def get_implementations(self)\
    \ -> Dict[str, Callable]:\n        \"\"\"Different sorting implementations to\
    \ compare\"\"\"\n        return {\n            'builtin_sort': lambda data: sorted(data),\n\
    \            'list_sort': lambda data: (data.copy(), data.sort())[0],\n      \
    \      'custom_sort': lambda data: self._custom_sort(data.copy())\n        }\n\
    \    \n    def _custom_sort(self, data):\n        \"\"\"Example custom sorting\
    \ implementation\"\"\"\n        # Simple selection sort for demonstration\n  \
    \      n = len(data)\n        for i in range(n):\n            min_idx = i\n  \
    \          for j in range(i + 1, n):\n                if data[j] < data[min_idx]:\n\
    \                    min_idx = j\n            data[i], data[min_idx] = data[min_idx],\
    \ data[i]\n        return data\n\ndef main():\n    \"\"\"Run the example benchmark\"\
    \"\"\n    \n    # Create configuration\n    config = BenchmarkConfig(\n      \
    \  name=\"sorting_example\",\n        iterations=5,\n        warmup=1,\n     \
    \   save_results=True,\n        plot_results=False,  # Set to True if you have\
    \ matplotlib\n        output_dir=\"./benchmark_results/example\"\n    )\n    \n\
    \    # Create and run benchmark\n    benchmark = SimpleSortBenchmark(config)\n\
    \    \n    # Small sizes for the example\n    param_grid = {\n        'size':\
    \ [10, 50, 100, 500]\n    }\n    \n    benchmark.run(param_grid)\n    \n    #\
    \ Access results programmatically\n    print(\"\\nAccessing results programmatically:\"\
    )\n    for result in benchmark.results[:5]:  # First 5 results\n        if result.error\
    \ is None:\n            print(f\"  {result.test_case.name}: {result.implementation}\
    \ = {result.time_ms:.3f}ms\")\n\nif __name__ == \"__main__\":\n    main()"
  dependsOn:
  - cp_library/perf/benchmark.py
  isVerificationFile: false
  path: cp_library/perf/examples/simple_usage.py
  requiredBy: []
  timestamp: '2025-07-20 06:26:01+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/perf/examples/simple_usage.py
layout: document
redirect_from:
- /library/cp_library/perf/examples/simple_usage.py
- /library/cp_library/perf/examples/simple_usage.py.html
title: cp_library/perf/examples/simple_usage.py
---
