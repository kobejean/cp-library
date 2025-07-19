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
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "#!/usr/bin/env python3\n\"\"\"\nSimple boolean list benchmark using\
    \ the new declarative framework.\nCompares different boolean data structures and\
    \ operations.\n\"\"\"\n\nimport random\nimport array\nimport sys\nimport os\n\
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))\n\
    \n\"\"\"\nDeclarative benchmark framework with minimal boilerplate.\n\nFeatures:\n\
    - Decorator-based benchmark registration\n- Automatic data generation and validation\n\
    - Built-in timing with warmup\n- Configurable operations and sizes\n- JSON results\
    \ and matplotlib plotting\n\"\"\"\n\nimport time\nimport json\nimport statistics\n\
    import argparse\nfrom typing import Dict, List, Any, Callable, Union\nfrom dataclasses\
    \ import dataclass\nfrom pathlib import Path\nfrom collections import defaultdict\n\
    \n@dataclass\nclass BenchmarkConfig:\n    \"\"\"Configuration for benchmark runs\"\
    \"\"\n    name: str\n    sizes: List[int] = None\n    operations: List[str] =\
    \ None\n    iterations: int = 10\n    warmup: int = 2\n    output_dir: str = \"\
    ./output/benchmark_results\"\n    save_results: bool = True\n    plot_results:\
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
    \ {speedup:<10.1f}x\")\n\n\n\n# Import optional dependencies\ntry:\n    import\
    \ bitarray\n    HAS_BITARRAY = True\nexcept ImportError:\n    HAS_BITARRAY = False\n\
    \ntry:\n    '''\n    \u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2578\n                 https://kobejean.github.io/cp-library         \
    \      \n    '''\n    '''\n    \u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2578\n                 https://kobejean.github.io/cp-library\
    \               \n    '''\n    '''\n    \u257A\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2578\n                 https://kobejean.github.io/cp-library\
    \               \n    '''\n    \n    class BitArray:\n        def __init__(B,\
    \ N):\n            if isinstance(N, list):\n                # If N is a list,\
    \ assume it's a list of 1s and 0s\n                B.N = len(N)\n            \
    \    B.Z = (B.N+31)>>5\n                B.bits, B.cnt = u32f(B.Z+1), u32f(B.Z+1)\n\
    \                # Set bits based on list values\n                for i, bit in\
    \ enumerate(N):\n                    if bit: B.set1(i)\n            elif isinstance(N,\
    \ (bytes, bytearray)):\n                # If N is bytes, convert each byte to\
    \ 8 bits\n                B.N = len(N) * 8\n                B.Z = (B.N+31)>>5\n\
    \                B.bits, B.cnt = u32f(B.Z+1), u32f(B.Z+1)\n                # Set\
    \ bits based on byte values (MSB first for each byte)\n                for byte_idx,\
    \ byte_val in enumerate(N):\n                    for bit_idx in range(8):\n  \
    \                      if byte_val & (1 << (7 - bit_idx)):  # MSB first\n    \
    \                        B.set1(byte_idx * 8 + bit_idx)\n            else:\n \
    \               # Original behavior: N is an integer\n                B.N = N\n\
    \                B.Z = (N+31)>>5\n                B.bits, B.cnt = u32f(B.Z+1),\
    \ u32f(B.Z+1)\n        def build(B):\n            B.bits.pop()\n            for\
    \ i,b in enumerate(B.bits): B.cnt[i+1] = B.cnt[i]+popcnt32(b)\n            B.bits.append(1)\n\
    \        def __len__(B): return B.N\n        def __getitem__(B, i: int): return\
    \ B.bits[i>>5]>>(31-(i&31))&1\n        def set0(B, i: int): B.bits[i>>5]&=~(1<<31-(i&31))\n\
    \        def set1(B, i: int): B.bits[i>>5]|=1<<31-(i&31)\n        def count0(B,\
    \ r: int): return r-B.count1(r)\n        def count1(B, r: int): return B.cnt[r>>5]+popcnt32(B.bits[r>>5]>>32-(r&31))\n\
    \        def select0(B, k: int):\n            if not 0<=k<B.N-B.cnt[-1]: return\
    \ -1\n            l,r,k=0,B.N,k+1\n            while 1<r-l:\n                if\
    \ B.count0(m:=(l+r)>>1)<k:l=m\n                else:r=m\n            return l\n\
    \        def select1(B, k: int):\n            if not 0<=k<B.cnt[-1]: return -1\n\
    \            l,r,k=0,B.N,k+1\n            while 1<r-l:\n                if B.count1(m:=(l+r)>>1)<k:l=m\n\
    \                else:r=m\n            return l\n    '''\n    \u257A\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\n                 https://kobejean.github.io/cp-library\
    \               \n    '''\n    \n    def popcnt32(x):\n        x = ((x >> 1) \
    \ & 0x55555555) + (x & 0x55555555)\n        x = ((x >> 2)  & 0x33333333) + (x\
    \ & 0x33333333)\n        x = ((x >> 4)  & 0x0f0f0f0f) + (x & 0x0f0f0f0f)\n   \
    \     x = ((x >> 8)  & 0x00ff00ff) + (x & 0x00ff00ff)\n        x = ((x >> 16)\
    \ & 0x0000ffff) + (x & 0x0000ffff)\n        return x\n    if hasattr(int, 'bit_count'):\n\
    \        popcnt32 = int.bit_count\n    '''\n    \u257A\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2578\n                 https://kobejean.github.io/cp-library\
    \               \n    '''\n    '''\n    \u257A\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2578\n                 https://kobejean.github.io/cp-library\
    \               \n    '''\n    '''\n    \u257A\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2578\n                 https://kobejean.github.io/cp-library\
    \               \n    '''\n    from array import array\n    def u32f(N: int, elm:\
    \ int = 0):     return array('I', (elm,))*N  # unsigned int\n    HAS_CUSTOM_BITARRAY\
    \ = True\nexcept ImportError:\n    HAS_CUSTOM_BITARRAY = False\n\n# Configure\
    \ benchmark\nconfig = BenchmarkConfig(\n    name=\"bool_list\",\n    sizes=[1000000,\
    \ 100000, 10000, 1000, 100, 10, 1],  # Reverse order to warm up JIT\n    operations=['construction',\
    \ 'access', 'count', 'sum', 'flip', 'and', 'or'],\n    iterations=10,\n    warmup=2,\n\
    \    output_dir=\"./output/benchmark_results/bool_list\"\n)\n\n# Create benchmark\
    \ instance\nbenchmark = Benchmark(config)\n\n# Data generator\n@benchmark.data_generator(\"\
    default\")\ndef generate_bool_data(size: int, operation: str):\n    \"\"\"Generate\
    \ boolean data in various formats\"\"\"\n    # Generate random boolean data\n\
    \    bool_list = [random.random() < 0.5 for _ in range(size)]\n    int_list =\
    \ [int(b) for b in bool_list]\n    \n    # Create different representations\n\
    \    array_b = array.array('b', int_list)\n    array_B = array.array('B', int_list)\n\
    \    \n    # Pack into bytes (8 bits per byte)\n    bytes_data = bytearray((size\
    \ + 7) // 8)\n    for i, bit in enumerate(bool_list):\n        if bit:\n     \
    \       bytes_data[i // 8] |= 1 << (7 - (i % 8))\n    bytes_data = bytes(bytes_data)\n\
    \    \n    # Create bitarray if available\n    bit_array = None\n    if HAS_BITARRAY:\n\
    \        bit_array = bitarray.bitarray(bool_list)\n    \n    # Create custom BitArray\
    \ if available\n    custom_bitarray = None\n    if HAS_CUSTOM_BITARRAY:\n    \
    \    custom_bitarray = BitArray(int_list)\n        custom_bitarray.build()\n \
    \   \n    # Pre-generate auxiliary data for binary operations\n    other_bool\
    \ = [random.random() < 0.5 for _ in range(size)]\n    other_int = [int(b) for\
    \ b in other_bool]\n    \n    return {\n        'bool_list': bool_list,\n    \
    \    'int_list': int_list,\n        'array_b': array_b,\n        'array_B': array_B,\n\
    \        'bytes_data': bytes_data,\n        'bit_array': bit_array,\n        'custom_bitarray':\
    \ custom_bitarray,\n        'other_bool': other_bool,\n        'other_int': other_int,\n\
    \        'size': size,\n        'operation': operation\n    }\n\n# Construction\
    \ operations\n@benchmark.implementation(\"list_bool\", \"construction\")\ndef\
    \ construction_list_bool(data):\n    \"\"\"Construct list[bool] from raw data\"\
    \"\"\n    # Use the same source data for all implementations\n    raw_data = data['bool_list']\n\
    \    result = list(raw_data)  # Create a copy\n    # Return consistent checksum\
    \ based on source data\n    checksum = 0\n    for i, b in enumerate(raw_data):\n\
    \        if b:\n            checksum ^= i\n    return checksum\n\n@benchmark.implementation(\"\
    list_int\", \"construction\")\ndef construction_list_int(data):\n    \"\"\"Construct\
    \ list[int] from raw data\"\"\"\n    # Use the same source data for all implementations\n\
    \    raw_data = data['bool_list']\n    int_list = [int(b) for b in raw_data]\n\
    \    # Return consistent checksum based on source data\n    checksum = 0\n   \
    \ for i, b in enumerate(raw_data):\n        if b:\n            checksum ^= i\n\
    \    return checksum\n\n@benchmark.implementation(\"array_b\", \"construction\"\
    )\ndef construction_array_b(data):\n    \"\"\"Construct array.array('b') from\
    \ raw data\"\"\"\n    # Use the same source data for all implementations\n   \
    \ raw_data = data['bool_list']\n    int_list = [int(b) for b in raw_data]\n  \
    \  array_b = array.array('b', int_list)\n    # Return consistent checksum based\
    \ on source data\n    checksum = 0\n    for i, b in enumerate(raw_data):\n   \
    \     if b:\n            checksum ^= i\n    return checksum\n\n@benchmark.implementation(\"\
    array_B\", \"construction\")\ndef construction_array_B(data):\n    \"\"\"Construct\
    \ array.array('B') from raw data\"\"\"\n    # Use the same source data for all\
    \ implementations\n    raw_data = data['bool_list']\n    int_list = [int(b) for\
    \ b in raw_data]\n    array_B = array.array('B', int_list)\n    # Return consistent\
    \ checksum based on source data\n    checksum = 0\n    for i, b in enumerate(raw_data):\n\
    \        if b:\n            checksum ^= i\n    return checksum\n\n@benchmark.implementation(\"\
    bytes\", \"construction\")\ndef construction_bytes(data):\n    \"\"\"Construct\
    \ bytes from raw data\"\"\"\n    # Use the same source data for all implementations\n\
    \    raw_data = data['bool_list']\n    size = data['size']\n    bytes_data = bytearray((size\
    \ + 7) // 8)\n    for i, bit in enumerate(raw_data):\n        if bit:\n      \
    \      bytes_data[i // 8] |= 1 << (7 - (i % 8))\n    bytes_data = bytes(bytes_data)\n\
    \    # Return consistent checksum based on source data\n    checksum = 0\n   \
    \ for i, b in enumerate(raw_data):\n        if b:\n            checksum ^= i\n\
    \    return checksum\n\nif HAS_BITARRAY:\n    @benchmark.implementation(\"bitarray\"\
    , \"construction\")\n    def construction_bitarray(data):\n        \"\"\"Construct\
    \ bitarray from raw data\"\"\"\n        # Use the same source data for all implementations\n\
    \        raw_data = data['bool_list']\n        bit_array = bitarray.bitarray(raw_data)\n\
    \        # Return consistent checksum based on source data\n        checksum =\
    \ 0\n        for i, b in enumerate(raw_data):\n            if b:\n           \
    \     checksum ^= i\n        return checksum\n\nif HAS_CUSTOM_BITARRAY:\n    @benchmark.implementation(\"\
    custom_bitarray\", \"construction\")\n    def construction_custom_bitarray(data):\n\
    \        \"\"\"Construct custom BitArray from raw data\"\"\"\n        # Use the\
    \ same source data for all implementations\n        raw_data = data['bool_list']\n\
    \        int_list = [int(b) for b in raw_data]\n        custom_bitarray = BitArray(int_list)\n\
    \        custom_bitarray.build()\n        # Return consistent checksum based on\
    \ source data\n        checksum = 0\n        for i, b in enumerate(raw_data):\n\
    \            if b:\n                checksum ^= i\n        return checksum\n\n\
    # Access operations\n@benchmark.implementation(\"list_bool\", \"access\")\ndef\
    \ access_list_bool(data):\n    \"\"\"Access operation on list[bool]\"\"\"\n  \
    \  lst = data['bool_list']\n    total = 0\n    access_count = min(1000, len(lst))\n\
    \    step = max(1, len(lst) // access_count)\n    for i in range(0, len(lst),\
    \ step):\n        if i < len(lst) and lst[i]:\n            total += 1\n    return\
    \ total\n\n@benchmark.implementation(\"list_int\", \"access\")\ndef access_list_int(data):\n\
    \    \"\"\"Access operation on list[int]\"\"\"\n    lst = data['int_list']\n \
    \   total = 0\n    access_count = min(1000, len(lst))\n    step = max(1, len(lst)\
    \ // access_count)\n    for i in range(0, len(lst), step):\n        if i < len(lst)\
    \ and lst[i]:\n            total += 1\n    return total\n\n@benchmark.implementation(\"\
    array_b\", \"access\")\ndef access_array_b(data):\n    \"\"\"Access operation\
    \ on array.array('b')\"\"\"\n    arr = data['array_b']\n    total = 0\n    access_count\
    \ = min(1000, len(arr))\n    step = max(1, len(arr) // access_count)\n    for\
    \ i in range(0, len(arr), step):\n        if i < len(arr) and arr[i]:\n      \
    \      total += 1\n    return total\n\n# Count operations\n@benchmark.implementation(\"\
    list_bool\", \"count\")\ndef count_list_bool(data):\n    \"\"\"Count True values\
    \ in list[bool]\"\"\"\n    return data['bool_list'].count(True)\n\n@benchmark.implementation(\"\
    list_int\", \"count\")\ndef count_list_int(data):\n    \"\"\"Count True values\
    \ in list[int]\"\"\"\n    return sum(data['int_list'])\n\n@benchmark.implementation(\"\
    array_b\", \"count\")\ndef count_array_b(data):\n    \"\"\"Count True values in\
    \ array.array('b')\"\"\"\n    return sum(data['array_b'])\n\n# Sum operations\
    \ (same as count for boolean data)\n@benchmark.implementation(\"list_bool\", \"\
    sum\")\ndef sum_list_bool(data):\n    \"\"\"Sum boolean values in list[bool]\"\
    \"\"\n    return sum(data['bool_list'])\n\n@benchmark.implementation(\"list_int\"\
    , \"sum\")\ndef sum_list_int(data):\n    \"\"\"Sum boolean values in list[int]\"\
    \"\"\n    return sum(data['int_list'])\n\n@benchmark.implementation(\"array_b\"\
    , \"sum\")\ndef sum_array_b(data):\n    \"\"\"Sum boolean values in array.array('b')\"\
    \"\"\n    return sum(data['array_b'])\n\n# Flip operations\n@benchmark.implementation(\"\
    list_bool\", \"flip\")\ndef flip_list_bool(data):\n    \"\"\"Flip all boolean\
    \ values in list[bool]\"\"\"\n    lst = list(data['bool_list'])  # Create copy\n\
    \    checksum = 0\n    for i in range(len(lst)):\n        lst[i] = not lst[i]\n\
    \        if lst[i]:\n            checksum ^= i\n    return checksum\n\n@benchmark.implementation(\"\
    list_int\", \"flip\")\ndef flip_list_int(data):\n    \"\"\"Flip all boolean values\
    \ in list[int]\"\"\"\n    lst = list(data['int_list'])  # Create copy\n    checksum\
    \ = 0\n    for i in range(len(lst)):\n        lst[i] = 1 - lst[i]\n        if\
    \ lst[i]:\n            checksum ^= i\n    return checksum\n\n@benchmark.implementation(\"\
    array_b\", \"flip\")\ndef flip_array_b(data):\n    \"\"\"Flip all boolean values\
    \ in array.array('b')\"\"\"\n    arr = array.array('b', data['array_b'])  # Create\
    \ copy\n    checksum = 0\n    for i in range(len(arr)):\n        arr[i] = 1 -\
    \ arr[i]\n        if arr[i]:\n            checksum ^= i\n    return checksum\n\
    \n@benchmark.implementation(\"array_B\", \"flip\")\ndef flip_array_B(data):\n\
    \    \"\"\"Flip all boolean values in array.array('B')\"\"\"\n    arr = array.array('B',\
    \ data['array_B'])  # Create copy\n    checksum = 0\n    for i in range(len(arr)):\n\
    \        arr[i] = 1 - arr[i]\n        if arr[i]:\n            checksum ^= i\n\
    \    return checksum\n\n@benchmark.implementation(\"bytearray\", \"flip\")\ndef\
    \ flip_bytearray(data):\n    \"\"\"Flip all boolean values in bytearray (non-bit-packed)\"\
    \"\"\n    # Use int_list as source for non-bit-packed\n    int_list = data['int_list']\n\
    \    result = bytearray(int_list)  # Create copy\n    checksum = 0\n    for i\
    \ in range(len(result)):\n        result[i] = 1 - result[i]\n        if result[i]:\n\
    \            checksum ^= i\n    return checksum\n\n@benchmark.implementation(\"\
    bytes\", \"flip\")\ndef flip_bytes(data):\n    \"\"\"Flip all boolean values in\
    \ bytes (non-bit-packed)\"\"\"\n    # Use int_list as source for non-bit-packed\n\
    \    int_list = data['int_list']\n    result = bytearray(int_list)  # Convert\
    \ to mutable\n    checksum = 0\n    for i in range(len(result)):\n        result[i]\
    \ = 1 - result[i]\n        if result[i]:\n            checksum ^= i\n    result\
    \ = bytes(result)  # Convert back to immutable\n    return checksum\n\n@benchmark.implementation(\"\
    bytearray_packed\", \"flip\")\ndef flip_bytearray_packed(data):\n    \"\"\"Flip\
    \ all boolean values in bytearray (bit-packed)\"\"\"\n    # Use bit-packed bytes_data\n\
    \    size = data['size']\n    bytes_data = data['bytes_data']\n    result = bytearray(bytes_data)\
    \  # Create copy\n    checksum = 0\n    \n    # Flip each bit\n    for i in range(size):\n\
    \        byte_idx = i // 8\n        bit_idx = 7 - (i % 8)\n        \n        #\
    \ Get current bit\n        current_bit = (result[byte_idx] >> bit_idx) & 1\n \
    \       \n        # Flip the bit\n        if current_bit:\n            result[byte_idx]\
    \ &= ~(1 << bit_idx)  # Clear bit\n        else:\n            result[byte_idx]\
    \ |= (1 << bit_idx)   # Set bit\n            checksum ^= i\n    \n    return checksum\n\
    \n@benchmark.implementation(\"bytes_packed\", \"flip\")\ndef flip_bytes_packed(data):\n\
    \    \"\"\"Flip all boolean values in bytes (bit-packed)\"\"\"\n    # Use bit-packed\
    \ bytes_data\n    size = data['size']\n    bytes_data = data['bytes_data']\n \
    \   result = bytearray(bytes_data)  # Convert to mutable\n    checksum = 0\n \
    \   \n    # Flip each bit\n    for i in range(size):\n        byte_idx = i //\
    \ 8\n        bit_idx = 7 - (i % 8)\n        \n        # Get current bit\n    \
    \    current_bit = (result[byte_idx] >> bit_idx) & 1\n        \n        # Flip\
    \ the bit\n        if current_bit:\n            result[byte_idx] &= ~(1 << bit_idx)\
    \  # Clear bit\n        else:\n            result[byte_idx] |= (1 << bit_idx)\
    \   # Set bit\n            checksum ^= i\n    \n    result = bytes(result)  #\
    \ Convert back to immutable\n    return checksum\n\n# AND operations\n@benchmark.implementation(\"\
    list_bool\", \"and\")\ndef and_list_bool(data):\n    \"\"\"AND operation on list[bool]\"\
    \"\"\n    lst = data['bool_list']\n    other = data['other_bool']\n    checksum\
    \ = 0\n    for i in range(len(lst)):\n        if lst[i] and other[i]:\n      \
    \      checksum ^= i\n    return checksum\n\n@benchmark.implementation(\"list_int\"\
    , \"and\")\ndef and_list_int(data):\n    \"\"\"AND operation on list[int]\"\"\"\
    \n    lst = data['int_list']\n    other = data['other_int']\n    checksum = 0\n\
    \    for i in range(len(lst)):\n        if lst[i] & other[i]:\n            checksum\
    \ ^= i\n    return checksum\n\n@benchmark.implementation(\"array_b\", \"and\"\
    )\ndef and_array_b(data):\n    \"\"\"AND operation on array.array('b')\"\"\"\n\
    \    arr = data['array_b']\n    other = array.array('b', data['other_int'])\n\
    \    checksum = 0\n    for i in range(len(arr)):\n        if arr[i] & other[i]:\n\
    \            checksum ^= i\n    return checksum\n\n@benchmark.implementation(\"\
    array_B\", \"and\")\ndef and_array_B(data):\n    \"\"\"AND operation on array.array('B')\"\
    \"\"\n    arr = data['array_B']\n    other = array.array('B', data['other_int'])\n\
    \    checksum = 0\n    for i in range(len(arr)):\n        if arr[i] & other[i]:\n\
    \            checksum ^= i\n    return checksum\n\n@benchmark.implementation(\"\
    bytearray\", \"and\")\ndef and_bytearray(data):\n    \"\"\"AND operation on bytearray\
    \ (non-bit-packed)\"\"\"\n    arr = bytearray(data['int_list'])\n    other = bytearray(data['other_int'])\n\
    \    checksum = 0\n    for i in range(len(arr)):\n        if arr[i] & other[i]:\n\
    \            checksum ^= i\n    return checksum\n\n@benchmark.implementation(\"\
    bytes\", \"and\")\ndef and_bytes(data):\n    \"\"\"AND operation on bytes (non-bit-packed)\"\
    \"\"\n    arr = bytes(data['int_list'])\n    other = bytes(data['other_int'])\n\
    \    checksum = 0\n    for i in range(len(arr)):\n        if arr[i] & other[i]:\n\
    \            checksum ^= i\n    return checksum\n\n@benchmark.implementation(\"\
    bytearray_packed\", \"and\")\ndef and_bytearray_packed(data):\n    \"\"\"AND operation\
    \ on bytearray (bit-packed)\"\"\"\n    size = data['size']\n    bytes_data = data['bytes_data']\n\
    \    other_bool = data['other_bool']\n    checksum = 0\n    \n    # AND each bit\n\
    \    for i in range(size):\n        byte_idx = i // 8\n        bit_idx = 7 - (i\
    \ % 8)\n        \n        # Get bits from both arrays\n        bit1 = (bytes_data[byte_idx]\
    \ >> bit_idx) & 1\n        bit2 = other_bool[i]\n        \n        # AND operation\n\
    \        if bit1 and bit2:\n            checksum ^= i\n    \n    return checksum\n\
    \n@benchmark.implementation(\"bytes_packed\", \"and\")\ndef and_bytes_packed(data):\n\
    \    \"\"\"AND operation on bytes (bit-packed)\"\"\"\n    size = data['size']\n\
    \    bytes_data = data['bytes_data']\n    other_bool = data['other_bool']\n  \
    \  checksum = 0\n    \n    # AND each bit\n    for i in range(size):\n       \
    \ byte_idx = i // 8\n        bit_idx = 7 - (i % 8)\n        \n        # Get bits\
    \ from both arrays\n        bit1 = (bytes_data[byte_idx] >> bit_idx) & 1\n   \
    \     bit2 = other_bool[i]\n        \n        # AND operation\n        if bit1\
    \ and bit2:\n            checksum ^= i\n    \n    return checksum\n\n# OR operations\n\
    @benchmark.implementation(\"list_bool\", \"or\")\ndef or_list_bool(data):\n  \
    \  \"\"\"OR operation on list[bool]\"\"\"\n    lst = data['bool_list']\n    other\
    \ = data['other_bool']\n    checksum = 0\n    for i in range(len(lst)):\n    \
    \    if lst[i] or other[i]:\n            checksum ^= i\n    return checksum\n\n\
    @benchmark.implementation(\"list_int\", \"or\")\ndef or_list_int(data):\n    \"\
    \"\"OR operation on list[int]\"\"\"\n    lst = data['int_list']\n    other = data['other_int']\n\
    \    checksum = 0\n    for i in range(len(lst)):\n        if lst[i] | other[i]:\n\
    \            checksum ^= i\n    return checksum\n\n@benchmark.implementation(\"\
    array_b\", \"or\")\ndef or_array_b(data):\n    \"\"\"OR operation on array.array('b')\"\
    \"\"\n    arr = data['array_b']\n    other = array.array('b', data['other_int'])\n\
    \    checksum = 0\n    for i in range(len(arr)):\n        if arr[i] | other[i]:\n\
    \            checksum ^= i\n    return checksum\n\n@benchmark.implementation(\"\
    array_B\", \"or\")\ndef or_array_B(data):\n    \"\"\"OR operation on array.array('B')\"\
    \"\"\n    arr = data['array_B']\n    other = array.array('B', data['other_int'])\n\
    \    checksum = 0\n    for i in range(len(arr)):\n        if arr[i] | other[i]:\n\
    \            checksum ^= i\n    return checksum\n\n@benchmark.implementation(\"\
    bytearray\", \"or\")\ndef or_bytearray(data):\n    \"\"\"OR operation on bytearray\
    \ (non-bit-packed)\"\"\"\n    arr = bytearray(data['int_list'])\n    other = bytearray(data['other_int'])\n\
    \    checksum = 0\n    for i in range(len(arr)):\n        if arr[i] | other[i]:\n\
    \            checksum ^= i\n    return checksum\n\n@benchmark.implementation(\"\
    bytes\", \"or\")\ndef or_bytes(data):\n    \"\"\"OR operation on bytes (non-bit-packed)\"\
    \"\"\n    arr = bytes(data['int_list'])\n    other = bytes(data['other_int'])\n\
    \    checksum = 0\n    for i in range(len(arr)):\n        if arr[i] | other[i]:\n\
    \            checksum ^= i\n    return checksum\n\n@benchmark.implementation(\"\
    bytearray_packed\", \"or\")\ndef or_bytearray_packed(data):\n    \"\"\"OR operation\
    \ on bytearray (bit-packed)\"\"\"\n    size = data['size']\n    bytes_data = data['bytes_data']\n\
    \    other_bool = data['other_bool']\n    checksum = 0\n    \n    # OR each bit\n\
    \    for i in range(size):\n        byte_idx = i // 8\n        bit_idx = 7 - (i\
    \ % 8)\n        \n        # Get bits from both arrays\n        bit1 = (bytes_data[byte_idx]\
    \ >> bit_idx) & 1\n        bit2 = other_bool[i]\n        \n        # OR operation\n\
    \        if bit1 or bit2:\n            checksum ^= i\n    \n    return checksum\n\
    \n@benchmark.implementation(\"bytes_packed\", \"or\")\ndef or_bytes_packed(data):\n\
    \    \"\"\"OR operation on bytes (bit-packed)\"\"\"\n    size = data['size']\n\
    \    bytes_data = data['bytes_data']\n    other_bool = data['other_bool']\n  \
    \  checksum = 0\n    \n    # OR each bit\n    for i in range(size):\n        byte_idx\
    \ = i // 8\n        bit_idx = 7 - (i % 8)\n        \n        # Get bits from both\
    \ arrays\n        bit1 = (bytes_data[byte_idx] >> bit_idx) & 1\n        bit2 =\
    \ other_bool[i]\n        \n        # OR operation\n        if bit1 or bit2:\n\
    \            checksum ^= i\n    \n    return checksum\n\n# Add bitarray implementations\
    \ if available\nif HAS_BITARRAY:\n    @benchmark.implementation(\"bitarray\",\
    \ [\"access\", \"count\", \"sum\", \"flip\", \"and\", \"or\"])\n    def bitarray_operations(data):\n\
    \        \"\"\"Operations on bitarray\"\"\"\n        operation = data['operation']\n\
    \        bit_arr = data['bit_array']\n        \n        if operation == 'access':\n\
    \            total = 0\n            access_count = min(1000, len(bit_arr))\n \
    \           step = max(1, len(bit_arr) // access_count)\n            for i in\
    \ range(0, len(bit_arr), step):\n                if i < len(bit_arr) and bit_arr[i]:\n\
    \                    total += 1\n            return total\n        elif operation\
    \ == 'count':\n            return bit_arr.count(True)\n        elif operation\
    \ == 'sum':\n            return bit_arr.count(True)\n        elif operation ==\
    \ 'flip':\n            result = bitarray.bitarray(bit_arr)\n            result.invert()\n\
    \            checksum = 0\n            for i, bit in enumerate(result):\n    \
    \            if bit:\n                    checksum ^= i\n            return checksum\n\
    \        elif operation == 'and':\n            other = bitarray.bitarray(data['other_bool'])\n\
    \            result = bit_arr & other\n            checksum = 0\n            for\
    \ i, bit in enumerate(result):\n                if bit:\n                    checksum\
    \ ^= i\n            return checksum\n        elif operation == 'or':\n       \
    \     other = bitarray.bitarray(data['other_bool'])\n            result = bit_arr\
    \ | other\n            checksum = 0\n            for i, bit in enumerate(result):\n\
    \                if bit:\n                    checksum ^= i\n            return\
    \ checksum\n\n# Add custom BitArray implementations if available\nif HAS_CUSTOM_BITARRAY:\n\
    \    @benchmark.implementation(\"custom_bitarray\", [\"access\", \"count\", \"\
    sum\"])\n    def custom_bitarray_operations(data):\n        \"\"\"Operations on\
    \ custom BitArray\"\"\"\n        operation = data['operation']\n        bit_arr\
    \ = data['custom_bitarray']\n        \n        if operation == 'access':\n   \
    \         total = 0\n            access_count = min(1000, len(bit_arr))\n    \
    \        step = max(1, len(bit_arr) // access_count)\n            for i in range(0,\
    \ len(bit_arr), step):\n                if i < len(bit_arr) and bit_arr[i]:\n\
    \                    total += 1\n            return total\n        elif operation\
    \ in ['count', 'sum']:\n            return sum(bit_arr[i] for i in range(len(bit_arr)))\n\
    \n# Custom validator for boolean operations\n@benchmark.validator(\"default\"\
    )\ndef validate_bool_result(expected, actual):\n    \"\"\"Validate boolean operation\
    \ results\"\"\"\n    # Convert results to comparable format\n    if hasattr(expected,\
    \ 'tolist'):  # array.array\n        expected = expected.tolist()\n    if hasattr(actual,\
    \ 'tolist'):  # array.array\n        actual = actual.tolist()\n    \n    # Handle\
    \ bitarray\n    if hasattr(expected, 'to01'):  # bitarray\n        expected =\
    \ [int(b) for b in expected.to01()]\n    if hasattr(actual, 'to01'):  # bitarray\n\
    \        actual = [int(b) for b in actual.to01()]\n    \n    # Convert booleans\
    \ to ints for comparison\n    if isinstance(expected, list) and len(expected)\
    \ > 0:\n        if isinstance(expected[0], bool):\n            expected = [int(b)\
    \ for b in expected]\n    if isinstance(actual, list) and len(actual) > 0:\n \
    \       if isinstance(actual[0], bool):\n            actual = [int(b) for b in\
    \ actual]\n    \n    return expected == actual\n\nif __name__ == \"__main__\"\
    :\n    # Parse command line args and run appropriate mode\n    runner = benchmark.parse_args()\n\
    \    runner.run()\n"
  code: "#!/usr/bin/env python3\n\"\"\"\nSimple boolean list benchmark using the new\
    \ declarative framework.\nCompares different boolean data structures and operations.\n\
    \"\"\"\n\nimport random\nimport array\nimport sys\nimport os\nsys.path.insert(0,\
    \ os.path.dirname(os.path.dirname(os.path.abspath(__file__))))\n\nfrom cp_library.perf.benchmark\
    \ import Benchmark, BenchmarkConfig\n\n# Import optional dependencies\ntry:\n\
    \    import bitarray\n    HAS_BITARRAY = True\nexcept ImportError:\n    HAS_BITARRAY\
    \ = False\n\ntry:\n    from cp_library.ds.wavelet.bit_array_cls import BitArray\n\
    \    HAS_CUSTOM_BITARRAY = True\nexcept ImportError:\n    HAS_CUSTOM_BITARRAY\
    \ = False\n\n# Configure benchmark\nconfig = BenchmarkConfig(\n    name=\"bool_list\"\
    ,\n    sizes=[1000000, 100000, 10000, 1000, 100, 10, 1],  # Reverse order to warm\
    \ up JIT\n    operations=['construction', 'access', 'count', 'sum', 'flip', 'and',\
    \ 'or'],\n    iterations=10,\n    warmup=2,\n    output_dir=\"./output/benchmark_results/bool_list\"\
    \n)\n\n# Create benchmark instance\nbenchmark = Benchmark(config)\n\n# Data generator\n\
    @benchmark.data_generator(\"default\")\ndef generate_bool_data(size: int, operation:\
    \ str):\n    \"\"\"Generate boolean data in various formats\"\"\"\n    # Generate\
    \ random boolean data\n    bool_list = [random.random() < 0.5 for _ in range(size)]\n\
    \    int_list = [int(b) for b in bool_list]\n    \n    # Create different representations\n\
    \    array_b = array.array('b', int_list)\n    array_B = array.array('B', int_list)\n\
    \    \n    # Pack into bytes (8 bits per byte)\n    bytes_data = bytearray((size\
    \ + 7) // 8)\n    for i, bit in enumerate(bool_list):\n        if bit:\n     \
    \       bytes_data[i // 8] |= 1 << (7 - (i % 8))\n    bytes_data = bytes(bytes_data)\n\
    \    \n    # Create bitarray if available\n    bit_array = None\n    if HAS_BITARRAY:\n\
    \        bit_array = bitarray.bitarray(bool_list)\n    \n    # Create custom BitArray\
    \ if available\n    custom_bitarray = None\n    if HAS_CUSTOM_BITARRAY:\n    \
    \    custom_bitarray = BitArray(int_list)\n        custom_bitarray.build()\n \
    \   \n    # Pre-generate auxiliary data for binary operations\n    other_bool\
    \ = [random.random() < 0.5 for _ in range(size)]\n    other_int = [int(b) for\
    \ b in other_bool]\n    \n    return {\n        'bool_list': bool_list,\n    \
    \    'int_list': int_list,\n        'array_b': array_b,\n        'array_B': array_B,\n\
    \        'bytes_data': bytes_data,\n        'bit_array': bit_array,\n        'custom_bitarray':\
    \ custom_bitarray,\n        'other_bool': other_bool,\n        'other_int': other_int,\n\
    \        'size': size,\n        'operation': operation\n    }\n\n# Construction\
    \ operations\n@benchmark.implementation(\"list_bool\", \"construction\")\ndef\
    \ construction_list_bool(data):\n    \"\"\"Construct list[bool] from raw data\"\
    \"\"\n    # Use the same source data for all implementations\n    raw_data = data['bool_list']\n\
    \    result = list(raw_data)  # Create a copy\n    # Return consistent checksum\
    \ based on source data\n    checksum = 0\n    for i, b in enumerate(raw_data):\n\
    \        if b:\n            checksum ^= i\n    return checksum\n\n@benchmark.implementation(\"\
    list_int\", \"construction\")\ndef construction_list_int(data):\n    \"\"\"Construct\
    \ list[int] from raw data\"\"\"\n    # Use the same source data for all implementations\n\
    \    raw_data = data['bool_list']\n    int_list = [int(b) for b in raw_data]\n\
    \    # Return consistent checksum based on source data\n    checksum = 0\n   \
    \ for i, b in enumerate(raw_data):\n        if b:\n            checksum ^= i\n\
    \    return checksum\n\n@benchmark.implementation(\"array_b\", \"construction\"\
    )\ndef construction_array_b(data):\n    \"\"\"Construct array.array('b') from\
    \ raw data\"\"\"\n    # Use the same source data for all implementations\n   \
    \ raw_data = data['bool_list']\n    int_list = [int(b) for b in raw_data]\n  \
    \  array_b = array.array('b', int_list)\n    # Return consistent checksum based\
    \ on source data\n    checksum = 0\n    for i, b in enumerate(raw_data):\n   \
    \     if b:\n            checksum ^= i\n    return checksum\n\n@benchmark.implementation(\"\
    array_B\", \"construction\")\ndef construction_array_B(data):\n    \"\"\"Construct\
    \ array.array('B') from raw data\"\"\"\n    # Use the same source data for all\
    \ implementations\n    raw_data = data['bool_list']\n    int_list = [int(b) for\
    \ b in raw_data]\n    array_B = array.array('B', int_list)\n    # Return consistent\
    \ checksum based on source data\n    checksum = 0\n    for i, b in enumerate(raw_data):\n\
    \        if b:\n            checksum ^= i\n    return checksum\n\n@benchmark.implementation(\"\
    bytes\", \"construction\")\ndef construction_bytes(data):\n    \"\"\"Construct\
    \ bytes from raw data\"\"\"\n    # Use the same source data for all implementations\n\
    \    raw_data = data['bool_list']\n    size = data['size']\n    bytes_data = bytearray((size\
    \ + 7) // 8)\n    for i, bit in enumerate(raw_data):\n        if bit:\n      \
    \      bytes_data[i // 8] |= 1 << (7 - (i % 8))\n    bytes_data = bytes(bytes_data)\n\
    \    # Return consistent checksum based on source data\n    checksum = 0\n   \
    \ for i, b in enumerate(raw_data):\n        if b:\n            checksum ^= i\n\
    \    return checksum\n\nif HAS_BITARRAY:\n    @benchmark.implementation(\"bitarray\"\
    , \"construction\")\n    def construction_bitarray(data):\n        \"\"\"Construct\
    \ bitarray from raw data\"\"\"\n        # Use the same source data for all implementations\n\
    \        raw_data = data['bool_list']\n        bit_array = bitarray.bitarray(raw_data)\n\
    \        # Return consistent checksum based on source data\n        checksum =\
    \ 0\n        for i, b in enumerate(raw_data):\n            if b:\n           \
    \     checksum ^= i\n        return checksum\n\nif HAS_CUSTOM_BITARRAY:\n    @benchmark.implementation(\"\
    custom_bitarray\", \"construction\")\n    def construction_custom_bitarray(data):\n\
    \        \"\"\"Construct custom BitArray from raw data\"\"\"\n        # Use the\
    \ same source data for all implementations\n        raw_data = data['bool_list']\n\
    \        int_list = [int(b) for b in raw_data]\n        custom_bitarray = BitArray(int_list)\n\
    \        custom_bitarray.build()\n        # Return consistent checksum based on\
    \ source data\n        checksum = 0\n        for i, b in enumerate(raw_data):\n\
    \            if b:\n                checksum ^= i\n        return checksum\n\n\
    # Access operations\n@benchmark.implementation(\"list_bool\", \"access\")\ndef\
    \ access_list_bool(data):\n    \"\"\"Access operation on list[bool]\"\"\"\n  \
    \  lst = data['bool_list']\n    total = 0\n    access_count = min(1000, len(lst))\n\
    \    step = max(1, len(lst) // access_count)\n    for i in range(0, len(lst),\
    \ step):\n        if i < len(lst) and lst[i]:\n            total += 1\n    return\
    \ total\n\n@benchmark.implementation(\"list_int\", \"access\")\ndef access_list_int(data):\n\
    \    \"\"\"Access operation on list[int]\"\"\"\n    lst = data['int_list']\n \
    \   total = 0\n    access_count = min(1000, len(lst))\n    step = max(1, len(lst)\
    \ // access_count)\n    for i in range(0, len(lst), step):\n        if i < len(lst)\
    \ and lst[i]:\n            total += 1\n    return total\n\n@benchmark.implementation(\"\
    array_b\", \"access\")\ndef access_array_b(data):\n    \"\"\"Access operation\
    \ on array.array('b')\"\"\"\n    arr = data['array_b']\n    total = 0\n    access_count\
    \ = min(1000, len(arr))\n    step = max(1, len(arr) // access_count)\n    for\
    \ i in range(0, len(arr), step):\n        if i < len(arr) and arr[i]:\n      \
    \      total += 1\n    return total\n\n# Count operations\n@benchmark.implementation(\"\
    list_bool\", \"count\")\ndef count_list_bool(data):\n    \"\"\"Count True values\
    \ in list[bool]\"\"\"\n    return data['bool_list'].count(True)\n\n@benchmark.implementation(\"\
    list_int\", \"count\")\ndef count_list_int(data):\n    \"\"\"Count True values\
    \ in list[int]\"\"\"\n    return sum(data['int_list'])\n\n@benchmark.implementation(\"\
    array_b\", \"count\")\ndef count_array_b(data):\n    \"\"\"Count True values in\
    \ array.array('b')\"\"\"\n    return sum(data['array_b'])\n\n# Sum operations\
    \ (same as count for boolean data)\n@benchmark.implementation(\"list_bool\", \"\
    sum\")\ndef sum_list_bool(data):\n    \"\"\"Sum boolean values in list[bool]\"\
    \"\"\n    return sum(data['bool_list'])\n\n@benchmark.implementation(\"list_int\"\
    , \"sum\")\ndef sum_list_int(data):\n    \"\"\"Sum boolean values in list[int]\"\
    \"\"\n    return sum(data['int_list'])\n\n@benchmark.implementation(\"array_b\"\
    , \"sum\")\ndef sum_array_b(data):\n    \"\"\"Sum boolean values in array.array('b')\"\
    \"\"\n    return sum(data['array_b'])\n\n# Flip operations\n@benchmark.implementation(\"\
    list_bool\", \"flip\")\ndef flip_list_bool(data):\n    \"\"\"Flip all boolean\
    \ values in list[bool]\"\"\"\n    lst = list(data['bool_list'])  # Create copy\n\
    \    checksum = 0\n    for i in range(len(lst)):\n        lst[i] = not lst[i]\n\
    \        if lst[i]:\n            checksum ^= i\n    return checksum\n\n@benchmark.implementation(\"\
    list_int\", \"flip\")\ndef flip_list_int(data):\n    \"\"\"Flip all boolean values\
    \ in list[int]\"\"\"\n    lst = list(data['int_list'])  # Create copy\n    checksum\
    \ = 0\n    for i in range(len(lst)):\n        lst[i] = 1 - lst[i]\n        if\
    \ lst[i]:\n            checksum ^= i\n    return checksum\n\n@benchmark.implementation(\"\
    array_b\", \"flip\")\ndef flip_array_b(data):\n    \"\"\"Flip all boolean values\
    \ in array.array('b')\"\"\"\n    arr = array.array('b', data['array_b'])  # Create\
    \ copy\n    checksum = 0\n    for i in range(len(arr)):\n        arr[i] = 1 -\
    \ arr[i]\n        if arr[i]:\n            checksum ^= i\n    return checksum\n\
    \n@benchmark.implementation(\"array_B\", \"flip\")\ndef flip_array_B(data):\n\
    \    \"\"\"Flip all boolean values in array.array('B')\"\"\"\n    arr = array.array('B',\
    \ data['array_B'])  # Create copy\n    checksum = 0\n    for i in range(len(arr)):\n\
    \        arr[i] = 1 - arr[i]\n        if arr[i]:\n            checksum ^= i\n\
    \    return checksum\n\n@benchmark.implementation(\"bytearray\", \"flip\")\ndef\
    \ flip_bytearray(data):\n    \"\"\"Flip all boolean values in bytearray (non-bit-packed)\"\
    \"\"\n    # Use int_list as source for non-bit-packed\n    int_list = data['int_list']\n\
    \    result = bytearray(int_list)  # Create copy\n    checksum = 0\n    for i\
    \ in range(len(result)):\n        result[i] = 1 - result[i]\n        if result[i]:\n\
    \            checksum ^= i\n    return checksum\n\n@benchmark.implementation(\"\
    bytes\", \"flip\")\ndef flip_bytes(data):\n    \"\"\"Flip all boolean values in\
    \ bytes (non-bit-packed)\"\"\"\n    # Use int_list as source for non-bit-packed\n\
    \    int_list = data['int_list']\n    result = bytearray(int_list)  # Convert\
    \ to mutable\n    checksum = 0\n    for i in range(len(result)):\n        result[i]\
    \ = 1 - result[i]\n        if result[i]:\n            checksum ^= i\n    result\
    \ = bytes(result)  # Convert back to immutable\n    return checksum\n\n@benchmark.implementation(\"\
    bytearray_packed\", \"flip\")\ndef flip_bytearray_packed(data):\n    \"\"\"Flip\
    \ all boolean values in bytearray (bit-packed)\"\"\"\n    # Use bit-packed bytes_data\n\
    \    size = data['size']\n    bytes_data = data['bytes_data']\n    result = bytearray(bytes_data)\
    \  # Create copy\n    checksum = 0\n    \n    # Flip each bit\n    for i in range(size):\n\
    \        byte_idx = i // 8\n        bit_idx = 7 - (i % 8)\n        \n        #\
    \ Get current bit\n        current_bit = (result[byte_idx] >> bit_idx) & 1\n \
    \       \n        # Flip the bit\n        if current_bit:\n            result[byte_idx]\
    \ &= ~(1 << bit_idx)  # Clear bit\n        else:\n            result[byte_idx]\
    \ |= (1 << bit_idx)   # Set bit\n            checksum ^= i\n    \n    return checksum\n\
    \n@benchmark.implementation(\"bytes_packed\", \"flip\")\ndef flip_bytes_packed(data):\n\
    \    \"\"\"Flip all boolean values in bytes (bit-packed)\"\"\"\n    # Use bit-packed\
    \ bytes_data\n    size = data['size']\n    bytes_data = data['bytes_data']\n \
    \   result = bytearray(bytes_data)  # Convert to mutable\n    checksum = 0\n \
    \   \n    # Flip each bit\n    for i in range(size):\n        byte_idx = i //\
    \ 8\n        bit_idx = 7 - (i % 8)\n        \n        # Get current bit\n    \
    \    current_bit = (result[byte_idx] >> bit_idx) & 1\n        \n        # Flip\
    \ the bit\n        if current_bit:\n            result[byte_idx] &= ~(1 << bit_idx)\
    \  # Clear bit\n        else:\n            result[byte_idx] |= (1 << bit_idx)\
    \   # Set bit\n            checksum ^= i\n    \n    result = bytes(result)  #\
    \ Convert back to immutable\n    return checksum\n\n# AND operations\n@benchmark.implementation(\"\
    list_bool\", \"and\")\ndef and_list_bool(data):\n    \"\"\"AND operation on list[bool]\"\
    \"\"\n    lst = data['bool_list']\n    other = data['other_bool']\n    checksum\
    \ = 0\n    for i in range(len(lst)):\n        if lst[i] and other[i]:\n      \
    \      checksum ^= i\n    return checksum\n\n@benchmark.implementation(\"list_int\"\
    , \"and\")\ndef and_list_int(data):\n    \"\"\"AND operation on list[int]\"\"\"\
    \n    lst = data['int_list']\n    other = data['other_int']\n    checksum = 0\n\
    \    for i in range(len(lst)):\n        if lst[i] & other[i]:\n            checksum\
    \ ^= i\n    return checksum\n\n@benchmark.implementation(\"array_b\", \"and\"\
    )\ndef and_array_b(data):\n    \"\"\"AND operation on array.array('b')\"\"\"\n\
    \    arr = data['array_b']\n    other = array.array('b', data['other_int'])\n\
    \    checksum = 0\n    for i in range(len(arr)):\n        if arr[i] & other[i]:\n\
    \            checksum ^= i\n    return checksum\n\n@benchmark.implementation(\"\
    array_B\", \"and\")\ndef and_array_B(data):\n    \"\"\"AND operation on array.array('B')\"\
    \"\"\n    arr = data['array_B']\n    other = array.array('B', data['other_int'])\n\
    \    checksum = 0\n    for i in range(len(arr)):\n        if arr[i] & other[i]:\n\
    \            checksum ^= i\n    return checksum\n\n@benchmark.implementation(\"\
    bytearray\", \"and\")\ndef and_bytearray(data):\n    \"\"\"AND operation on bytearray\
    \ (non-bit-packed)\"\"\"\n    arr = bytearray(data['int_list'])\n    other = bytearray(data['other_int'])\n\
    \    checksum = 0\n    for i in range(len(arr)):\n        if arr[i] & other[i]:\n\
    \            checksum ^= i\n    return checksum\n\n@benchmark.implementation(\"\
    bytes\", \"and\")\ndef and_bytes(data):\n    \"\"\"AND operation on bytes (non-bit-packed)\"\
    \"\"\n    arr = bytes(data['int_list'])\n    other = bytes(data['other_int'])\n\
    \    checksum = 0\n    for i in range(len(arr)):\n        if arr[i] & other[i]:\n\
    \            checksum ^= i\n    return checksum\n\n@benchmark.implementation(\"\
    bytearray_packed\", \"and\")\ndef and_bytearray_packed(data):\n    \"\"\"AND operation\
    \ on bytearray (bit-packed)\"\"\"\n    size = data['size']\n    bytes_data = data['bytes_data']\n\
    \    other_bool = data['other_bool']\n    checksum = 0\n    \n    # AND each bit\n\
    \    for i in range(size):\n        byte_idx = i // 8\n        bit_idx = 7 - (i\
    \ % 8)\n        \n        # Get bits from both arrays\n        bit1 = (bytes_data[byte_idx]\
    \ >> bit_idx) & 1\n        bit2 = other_bool[i]\n        \n        # AND operation\n\
    \        if bit1 and bit2:\n            checksum ^= i\n    \n    return checksum\n\
    \n@benchmark.implementation(\"bytes_packed\", \"and\")\ndef and_bytes_packed(data):\n\
    \    \"\"\"AND operation on bytes (bit-packed)\"\"\"\n    size = data['size']\n\
    \    bytes_data = data['bytes_data']\n    other_bool = data['other_bool']\n  \
    \  checksum = 0\n    \n    # AND each bit\n    for i in range(size):\n       \
    \ byte_idx = i // 8\n        bit_idx = 7 - (i % 8)\n        \n        # Get bits\
    \ from both arrays\n        bit1 = (bytes_data[byte_idx] >> bit_idx) & 1\n   \
    \     bit2 = other_bool[i]\n        \n        # AND operation\n        if bit1\
    \ and bit2:\n            checksum ^= i\n    \n    return checksum\n\n# OR operations\n\
    @benchmark.implementation(\"list_bool\", \"or\")\ndef or_list_bool(data):\n  \
    \  \"\"\"OR operation on list[bool]\"\"\"\n    lst = data['bool_list']\n    other\
    \ = data['other_bool']\n    checksum = 0\n    for i in range(len(lst)):\n    \
    \    if lst[i] or other[i]:\n            checksum ^= i\n    return checksum\n\n\
    @benchmark.implementation(\"list_int\", \"or\")\ndef or_list_int(data):\n    \"\
    \"\"OR operation on list[int]\"\"\"\n    lst = data['int_list']\n    other = data['other_int']\n\
    \    checksum = 0\n    for i in range(len(lst)):\n        if lst[i] | other[i]:\n\
    \            checksum ^= i\n    return checksum\n\n@benchmark.implementation(\"\
    array_b\", \"or\")\ndef or_array_b(data):\n    \"\"\"OR operation on array.array('b')\"\
    \"\"\n    arr = data['array_b']\n    other = array.array('b', data['other_int'])\n\
    \    checksum = 0\n    for i in range(len(arr)):\n        if arr[i] | other[i]:\n\
    \            checksum ^= i\n    return checksum\n\n@benchmark.implementation(\"\
    array_B\", \"or\")\ndef or_array_B(data):\n    \"\"\"OR operation on array.array('B')\"\
    \"\"\n    arr = data['array_B']\n    other = array.array('B', data['other_int'])\n\
    \    checksum = 0\n    for i in range(len(arr)):\n        if arr[i] | other[i]:\n\
    \            checksum ^= i\n    return checksum\n\n@benchmark.implementation(\"\
    bytearray\", \"or\")\ndef or_bytearray(data):\n    \"\"\"OR operation on bytearray\
    \ (non-bit-packed)\"\"\"\n    arr = bytearray(data['int_list'])\n    other = bytearray(data['other_int'])\n\
    \    checksum = 0\n    for i in range(len(arr)):\n        if arr[i] | other[i]:\n\
    \            checksum ^= i\n    return checksum\n\n@benchmark.implementation(\"\
    bytes\", \"or\")\ndef or_bytes(data):\n    \"\"\"OR operation on bytes (non-bit-packed)\"\
    \"\"\n    arr = bytes(data['int_list'])\n    other = bytes(data['other_int'])\n\
    \    checksum = 0\n    for i in range(len(arr)):\n        if arr[i] | other[i]:\n\
    \            checksum ^= i\n    return checksum\n\n@benchmark.implementation(\"\
    bytearray_packed\", \"or\")\ndef or_bytearray_packed(data):\n    \"\"\"OR operation\
    \ on bytearray (bit-packed)\"\"\"\n    size = data['size']\n    bytes_data = data['bytes_data']\n\
    \    other_bool = data['other_bool']\n    checksum = 0\n    \n    # OR each bit\n\
    \    for i in range(size):\n        byte_idx = i // 8\n        bit_idx = 7 - (i\
    \ % 8)\n        \n        # Get bits from both arrays\n        bit1 = (bytes_data[byte_idx]\
    \ >> bit_idx) & 1\n        bit2 = other_bool[i]\n        \n        # OR operation\n\
    \        if bit1 or bit2:\n            checksum ^= i\n    \n    return checksum\n\
    \n@benchmark.implementation(\"bytes_packed\", \"or\")\ndef or_bytes_packed(data):\n\
    \    \"\"\"OR operation on bytes (bit-packed)\"\"\"\n    size = data['size']\n\
    \    bytes_data = data['bytes_data']\n    other_bool = data['other_bool']\n  \
    \  checksum = 0\n    \n    # OR each bit\n    for i in range(size):\n        byte_idx\
    \ = i // 8\n        bit_idx = 7 - (i % 8)\n        \n        # Get bits from both\
    \ arrays\n        bit1 = (bytes_data[byte_idx] >> bit_idx) & 1\n        bit2 =\
    \ other_bool[i]\n        \n        # OR operation\n        if bit1 or bit2:\n\
    \            checksum ^= i\n    \n    return checksum\n\n# Add bitarray implementations\
    \ if available\nif HAS_BITARRAY:\n    @benchmark.implementation(\"bitarray\",\
    \ [\"access\", \"count\", \"sum\", \"flip\", \"and\", \"or\"])\n    def bitarray_operations(data):\n\
    \        \"\"\"Operations on bitarray\"\"\"\n        operation = data['operation']\n\
    \        bit_arr = data['bit_array']\n        \n        if operation == 'access':\n\
    \            total = 0\n            access_count = min(1000, len(bit_arr))\n \
    \           step = max(1, len(bit_arr) // access_count)\n            for i in\
    \ range(0, len(bit_arr), step):\n                if i < len(bit_arr) and bit_arr[i]:\n\
    \                    total += 1\n            return total\n        elif operation\
    \ == 'count':\n            return bit_arr.count(True)\n        elif operation\
    \ == 'sum':\n            return bit_arr.count(True)\n        elif operation ==\
    \ 'flip':\n            result = bitarray.bitarray(bit_arr)\n            result.invert()\n\
    \            checksum = 0\n            for i, bit in enumerate(result):\n    \
    \            if bit:\n                    checksum ^= i\n            return checksum\n\
    \        elif operation == 'and':\n            other = bitarray.bitarray(data['other_bool'])\n\
    \            result = bit_arr & other\n            checksum = 0\n            for\
    \ i, bit in enumerate(result):\n                if bit:\n                    checksum\
    \ ^= i\n            return checksum\n        elif operation == 'or':\n       \
    \     other = bitarray.bitarray(data['other_bool'])\n            result = bit_arr\
    \ | other\n            checksum = 0\n            for i, bit in enumerate(result):\n\
    \                if bit:\n                    checksum ^= i\n            return\
    \ checksum\n\n# Add custom BitArray implementations if available\nif HAS_CUSTOM_BITARRAY:\n\
    \    @benchmark.implementation(\"custom_bitarray\", [\"access\", \"count\", \"\
    sum\"])\n    def custom_bitarray_operations(data):\n        \"\"\"Operations on\
    \ custom BitArray\"\"\"\n        operation = data['operation']\n        bit_arr\
    \ = data['custom_bitarray']\n        \n        if operation == 'access':\n   \
    \         total = 0\n            access_count = min(1000, len(bit_arr))\n    \
    \        step = max(1, len(bit_arr) // access_count)\n            for i in range(0,\
    \ len(bit_arr), step):\n                if i < len(bit_arr) and bit_arr[i]:\n\
    \                    total += 1\n            return total\n        elif operation\
    \ in ['count', 'sum']:\n            return sum(bit_arr[i] for i in range(len(bit_arr)))\n\
    \n# Custom validator for boolean operations\n@benchmark.validator(\"default\"\
    )\ndef validate_bool_result(expected, actual):\n    \"\"\"Validate boolean operation\
    \ results\"\"\"\n    # Convert results to comparable format\n    if hasattr(expected,\
    \ 'tolist'):  # array.array\n        expected = expected.tolist()\n    if hasattr(actual,\
    \ 'tolist'):  # array.array\n        actual = actual.tolist()\n    \n    # Handle\
    \ bitarray\n    if hasattr(expected, 'to01'):  # bitarray\n        expected =\
    \ [int(b) for b in expected.to01()]\n    if hasattr(actual, 'to01'):  # bitarray\n\
    \        actual = [int(b) for b in actual.to01()]\n    \n    # Convert booleans\
    \ to ints for comparison\n    if isinstance(expected, list) and len(expected)\
    \ > 0:\n        if isinstance(expected[0], bool):\n            expected = [int(b)\
    \ for b in expected]\n    if isinstance(actual, list) and len(actual) > 0:\n \
    \       if isinstance(actual[0], bool):\n            actual = [int(b) for b in\
    \ actual]\n    \n    return expected == actual\n\nif __name__ == \"__main__\"\
    :\n    # Parse command line args and run appropriate mode\n    runner = benchmark.parse_args()\n\
    \    runner.run()"
  dependsOn:
  - cp_library/perf/benchmark.py
  - cp_library/ds/wavelet/bit_array_cls.py
  - cp_library/bit/popcnt32_fn.py
  - cp_library/ds/array/u32f_fn.py
  isVerificationFile: false
  path: perf/bool_list.py
  requiredBy: []
  timestamp: '2025-07-20 06:26:01+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: perf/bool_list.py
layout: document
redirect_from:
- /library/perf/bool_list.py
- /library/perf/bool_list.py.html
title: perf/bool_list.py
---
