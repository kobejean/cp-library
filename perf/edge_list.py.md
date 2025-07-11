---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/edge/edge_list_weighted_cls.py
    title: cp_library/alg/graph/edge/edge_list_weighted_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/iter/arg/argsort_fn.py
    title: argsort
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/iter/sort/isort_parallel_fn.py
    title: cp_library/alg/iter/sort/isort_parallel_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/iter/sort/sort_parallel_fn.py
    title: cp_library/alg/iter/sort/sort_parallel_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/pack/packer_cls.py
    title: cp_library/bit/pack/packer_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/csr/csr_incremental_cls.py
    title: cp_library/ds/csr/csr_incremental_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/dsu_cls.py
    title: cp_library/ds/dsu_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/elist_fn.py
    title: cp_library/ds/elist_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/heap/skew_heap_forrest_cls.py
    title: cp_library/ds/heap/skew_heap_forrest_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/fast_io_cls.py
    title: cp_library/io/fast_io_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/parser_cls.py
    title: cp_library/io/parser_cls.py
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
  bundledCode: "#!/usr/bin/env python3\n\"\"\"\nSimple edge list benchmark using the\
    \ new declarative framework.\nMuch less boilerplate, easier to understand and\
    \ extend.\n\"\"\"\n\nimport random\nimport sys\nimport os\nsys.path.insert(0,\
    \ os.path.dirname(os.path.dirname(os.path.abspath(__file__))))\n\n\"\"\"\nDeclarative\
    \ benchmark framework with minimal boilerplate.\n\nFeatures:\n- Decorator-based\
    \ benchmark registration\n- Automatic data generation and validation\n- Built-in\
    \ timing with warmup\n- Configurable operations and sizes\n- JSON results and\
    \ matplotlib plotting\n\"\"\"\n\nimport time\nimport json\nimport statistics\n\
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
    \ {speedup:<10.1f}x\")\n\n\n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2578\n             https://kobejean.github.io/cp-library \
    \              \n'''\n\n\n\n\ndef argsort(A: list[int], reverse=False):\n    P\
    \ = Packer(len(I := list(A))-1); P.ienumerate(I, reverse); I.sort(); P.iindices(I)\n\
    \    return I\n\n\n\nclass Packer:\n    __slots__ = 's', 'm'\n    def __init__(P,\
    \ mx: int): P.s = mx.bit_length(); P.m = (1 << P.s) - 1\n    def enc(P, a: int,\
    \ b: int): return a << P.s | b\n    def dec(P, x: int) -> tuple[int, int]: return\
    \ x >> P.s, x & P.m\n    def enumerate(P, A, reverse=False): P.ienumerate(A:=list(A),\
    \ reverse); return A\n    def ienumerate(P, A, reverse=False):\n        if reverse:\n\
    \            for i,a in enumerate(A): A[i] = P.enc(-a, i)\n        else:\n   \
    \         for i,a in enumerate(A): A[i] = P.enc(a, i)\n    def indices(P, A: list[int]):\
    \ P.iindices(A:=list(A)); return A\n    def iindices(P, A):\n        for i,a in\
    \ enumerate(A): A[i] = P.m&a\n\n\ndef isort_parallel(*L: list, reverse=False):\n\
    \    inv, order = [0]*len(L[0]), argsort(L[0], reverse=reverse)\n    for i, j\
    \ in enumerate(order): inv[j] = i\n    for i, j in enumerate(order):\n       \
    \ for A in L: A[i], A[j] = A[j], A[i]\n        order[inv[i]], inv[j] = j, inv[i]\n\
    \    return L\n\ndef sort_parallel(*L: list, reverse=False):\n    N, K, order\
    \ = len(L[0]), len(L), argsort(L[0], reverse)\n    R = tuple([0]*N for _ in range(K))\n\
    \    for k, Lk in enumerate(L):\n        Rk = R[k]\n        for i, j in enumerate(order):\
    \ Rk[i] = Lk[j]\n    return R\n\nimport typing\nfrom collections import deque\n\
    from numbers import Number\nfrom types import GenericAlias \nfrom typing import\
    \ Callable, Collection, Iterator, Union\nfrom io import BytesIO, IOBase\n\n\n\
    class FastIO(IOBase):\n    BUFSIZE = 8192\n    newlines = 0\n\n    def __init__(self,\
    \ file):\n        self._fd = file.fileno()\n        self.buffer = BytesIO()\n\
    \        self.writable = \"x\" in file.mode or \"r\" not in file.mode\n      \
    \  self.write = self.buffer.write if self.writable else None\n\n    def read(self):\n\
    \        BUFSIZE = self.BUFSIZE\n        while True:\n            b = os.read(self._fd,\
    \ max(os.fstat(self._fd).st_size, BUFSIZE))\n            if not b: break\n   \
    \         ptr = self.buffer.tell()\n            self.buffer.seek(0, 2), self.buffer.write(b),\
    \ self.buffer.seek(ptr)\n        self.newlines = 0\n        return self.buffer.read()\n\
    \n    def readline(self):\n        BUFSIZE = self.BUFSIZE\n        while self.newlines\
    \ == 0:\n            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))\n\
    \            self.newlines = b.count(b\"\\n\") + (not b)\n            ptr = self.buffer.tell()\n\
    \            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)\n\
    \        self.newlines -= 1\n        return self.buffer.readline()\n\n    def\
    \ flush(self):\n        if self.writable:\n            os.write(self._fd, self.buffer.getvalue())\n\
    \            self.buffer.truncate(0), self.buffer.seek(0)\n\n\nclass IOWrapper(IOBase):\n\
    \    stdin: 'IOWrapper' = None\n    stdout: 'IOWrapper' = None\n    \n    def\
    \ __init__(self, file):\n        self.buffer = FastIO(file)\n        self.flush\
    \ = self.buffer.flush\n        self.writable = self.buffer.writable\n\n    def\
    \ write(self, s):\n        return self.buffer.write(s.encode(\"ascii\"))\n   \
    \ \n    def read(self):\n        return self.buffer.read().decode(\"ascii\")\n\
    \    \n    def readline(self):\n        return self.buffer.readline().decode(\"\
    ascii\")\ntry:\n    sys.stdin = IOWrapper.stdin = IOWrapper(sys.stdin)\n    sys.stdout\
    \ = IOWrapper.stdout = IOWrapper(sys.stdout)\nexcept:\n    pass\nfrom typing import\
    \ TypeVar\n_S = TypeVar('S')\n_T = TypeVar('T')\n_U = TypeVar('U')\n\nclass TokenStream(Iterator):\n\
    \    stream = IOWrapper.stdin\n\n    def __init__(self):\n        self.queue =\
    \ deque()\n\n    def __next__(self):\n        if not self.queue: self.queue.extend(self._line())\n\
    \        return self.queue.popleft()\n    \n    def wait(self):\n        if not\
    \ self.queue: self.queue.extend(self._line())\n        while self.queue: yield\n\
    \ \n    def _line(self):\n        return TokenStream.stream.readline().split()\n\
    \n    def line(self):\n        if self.queue:\n            A = list(self.queue)\n\
    \            self.queue.clear()\n            return A\n        return self._line()\n\
    TokenStream.default = TokenStream()\n\nclass CharStream(TokenStream):\n    def\
    \ _line(self):\n        return TokenStream.stream.readline().rstrip()\nCharStream.default\
    \ = CharStream()\n\nParseFn = Callable[[TokenStream],_T]\nclass Parser:\n    def\
    \ __init__(self, spec: Union[type[_T],_T]):\n        self.parse = Parser.compile(spec)\n\
    \n    def __call__(self, ts: TokenStream) -> _T:\n        return self.parse(ts)\n\
    \    \n    @staticmethod\n    def compile_type(cls: type[_T], args = ()) -> _T:\n\
    \        if issubclass(cls, Parsable):\n            return cls.compile(*args)\n\
    \        elif issubclass(cls, (Number, str)):\n            def parse(ts: TokenStream):\
    \ return cls(next(ts))              \n            return parse\n        elif issubclass(cls,\
    \ tuple):\n            return Parser.compile_tuple(cls, args)\n        elif issubclass(cls,\
    \ Collection):\n            return Parser.compile_collection(cls, args)\n    \
    \    elif callable(cls):\n            def parse(ts: TokenStream):\n          \
    \      return cls(next(ts))              \n            return parse\n        else:\n\
    \            raise NotImplementedError()\n    \n    @staticmethod\n    def compile(spec:\
    \ Union[type[_T],_T]=int) -> ParseFn[_T]:\n        if isinstance(spec, (type,\
    \ GenericAlias)):\n            cls = typing.get_origin(spec) or spec\n       \
    \     args = typing.get_args(spec) or tuple()\n            return Parser.compile_type(cls,\
    \ args)\n        elif isinstance(offset := spec, Number): \n            cls =\
    \ type(spec)  \n            def parse(ts: TokenStream): return cls(next(ts)) +\
    \ offset\n            return parse\n        elif isinstance(args := spec, tuple):\
    \      \n            return Parser.compile_tuple(type(spec), args)\n        elif\
    \ isinstance(args := spec, Collection):\n            return Parser.compile_collection(type(spec),\
    \ args)\n        elif isinstance(fn := spec, Callable): \n            def parse(ts:\
    \ TokenStream): return fn(next(ts))\n            return parse\n        else:\n\
    \            raise NotImplementedError()\n\n    @staticmethod\n    def compile_line(cls:\
    \ _T, spec=int) -> ParseFn[_T]:\n        if spec is int:\n            fn = Parser.compile(spec)\n\
    \            def parse(ts: TokenStream): return cls([int(token) for token in ts.line()])\n\
    \            return parse\n        else:\n            fn = Parser.compile(spec)\n\
    \            def parse(ts: TokenStream): return cls([fn(ts) for _ in ts.wait()])\n\
    \            return parse\n\n    @staticmethod\n    def compile_repeat(cls: _T,\
    \ spec, N) -> ParseFn[_T]:\n        fn = Parser.compile(spec)\n        def parse(ts:\
    \ TokenStream): return cls([fn(ts) for _ in range(N)])\n        return parse\n\
    \n    @staticmethod\n    def compile_children(cls: _T, specs) -> ParseFn[_T]:\n\
    \        fns = tuple((Parser.compile(spec) for spec in specs))\n        def parse(ts:\
    \ TokenStream): return cls([fn(ts) for fn in fns])  \n        return parse\n \
    \           \n    @staticmethod\n    def compile_tuple(cls: type[_T], specs) ->\
    \ ParseFn[_T]:\n        if isinstance(specs, (tuple,list)) and len(specs) == 2\
    \ and specs[1] is ...:\n            return Parser.compile_line(cls, specs[0])\n\
    \        else:\n            return Parser.compile_children(cls, specs)\n\n   \
    \ @staticmethod\n    def compile_collection(cls, specs):\n        if not specs\
    \ or len(specs) == 1 or isinstance(specs, set):\n            return Parser.compile_line(cls,\
    \ *specs)\n        elif (isinstance(specs, (tuple,list)) and len(specs) == 2 and\
    \ isinstance(specs[1], int)):\n            return Parser.compile_repeat(cls, specs[0],\
    \ specs[1])\n        else:\n            raise NotImplementedError()\n\nclass Parsable:\n\
    \    @classmethod\n    def compile(cls):\n        def parser(ts: TokenStream):\
    \ return cls(next(ts))\n        return parser\n    \n    @classmethod\n    def\
    \ __class_getitem__(cls, item):\n        return GenericAlias(cls, item)\n\n\n\
    class EdgeListWeighted(Parsable):\n    def __init__(E, N: int, U: list[int], V:\
    \ list[int], W: list[int]): E.N, E.M, E.U, E.V, E.W = N, len(U), U, V, W\n   \
    \ def __len__(E): return E.M\n    def __getitem__(E, e): return E.U[e], E.V[e],\
    \ E.W[e]\n    @classmethod\n    def compile(cls, N: int, M: int, I: int = -1):\n\
    \        def parse(ts: TokenStream):\n            U, V, W = [0]*M, [0]*M, [0]*M\n\
    \            for e in range(M): u, v, w = ts.line(); U[e], V[e], W[e] = int(u)+I,\
    \ int(v)+I, int(w)\n            return cls(N, U, V, W)\n        return parse\n\
    \    def kruskal(E):\n        dsu, I = DSU(E.N), elist(E.N-1)\n        for e in\
    \ argsort(E.W):\n            x, y = dsu.merge(E.U[e], E.V[e])\n            if\
    \ x != y: I.append(e)\n        return I\n    def edmond(E, root):\n        U,\
    \ W, F, pkr, dsu = [0]*E.N, [0]*E.N, SkewHeapForrest(E.N, E.M), Packer(E.M), DSU(E.N)\n\
    \        Ein, stem, cyc, I, C = [-1]*E.M, [-1]*E.N, [], [], []; vis = [0]*E.N;\
    \ vis[root] = 2\n        for e in range(E.M): F.push(E.V[e], pkr.enc(E.W[e], e))\n\
    \        for v in range(E.N):\n            if vis[v := dsu.root(v)]: continue\n\
    \            cycle = 0; C.clear()\n            while vis[v] != 2:\n          \
    \      if F.empty(v): return None\n                vis[v] = 1; cyc.append(v);\
    \ W[v], e = pkr.dec(F.pop(v)); U[v] = dsu.root(E.U[e])\n                if stem[v]\
    \ == -1: stem[v] = e\n                if U[v] == v: continue\n               \
    \ while cycle: Ein[C.pop()] = e; cycle -= 1\n                I.append(e); C.append(e)\n\
    \                if vis[U[v]] == 1:\n                    if not F.empty(v): F.add(v,\
    \ -W[v]<<pkr.s)\n                    U[v] = p = dsu.root(U[v]); cycle += 1\n \
    \                   while p != v:\n                        if not F.empty(p):\
    \ F.add(p, -W[p]<<pkr.s)\n                        F.roots[v := dsu.merge_dest(v,\
    \ p)] = F.merge(F.roots[v], F.roots[p])\n                        U[p] = p = dsu.root(U[p]);\
    \ cycle += 1\n                else:\n                    v = U[v]\n          \
    \  while cyc: vis[cyc.pop()] = 2\n\n        vis, T = [0]*E.M, []\n        for\
    \ e in reversed(I):\n            if vis[e]: continue\n            f = stem[E.V[e]];\
    \ T.append(e)\n            while f != e: vis[f] = 1; f = Ein[f]\n        return\
    \ T\n    \n    def sort(E):\n        isort_parallel(E.W, E.U, E.V)\n\n    def\
    \ sub(E, I: list[int]):\n        U, V, W = elist(E.N-1), elist(E.N-1), elist(E.N-1)\n\
    \        for e in I: U.append(E.U[e]); V.append(E.V[e]); W.append(E.W[e])\n  \
    \      return E.__class__(E.N, U, V, W)\n\n\n\nclass DSU(Parsable):\n    def __init__(dsu,\
    \ N): dsu.N, dsu.cc, dsu.par = N, N, [-1]*N\n    def merge(dsu, u, v):\n     \
    \   x, y = dsu.root(u), dsu.root(v)\n        if x == y: return x,y\n        if\
    \ dsu.par[x] > dsu.par[y]: x, y = y, x\n        dsu.par[x] += dsu.par[y]; dsu.par[y]\
    \ = x; dsu.cc -= 1\n        return x, y\n    def root(dsu, i) -> int:\n      \
    \  p = (par := dsu.par)[i]\n        while p >= 0:\n            if par[p] < 0:\
    \ return p\n            par[i], i, p = par[p], par[p], par[par[p]]\n        return\
    \ i\n    def groups(dsu) -> 'CSRIncremental[int]':\n        sizes, row, p = [0]*dsu.cc,\
    \ [-1]*dsu.N, 0\n        for i in range(dsu.cc):\n            while dsu.par[p]\
    \ >= 0: p += 1\n            sizes[i], row[p] = -dsu.par[p], i; p += 1\n      \
    \  csr = CSRIncremental(sizes)\n        for i in range(dsu.N): csr.append(row[dsu.root(i)],\
    \ i)\n        return csr\n    __iter__ = groups\n    def merge_dest(dsu, u, v):\
    \ return dsu.merge(u, v)[0]\n    def same(dsu, u: int, v: int):  return dsu.root(u)\
    \ == dsu.root(v)\n    def size(dsu, i) -> int: return -dsu.par[dsu.root(i)]\n\
    \    def __len__(dsu): return dsu.cc\n    def __contains__(dsu, uv): u, v = uv;\
    \ return dsu.same(u, v)\n    @classmethod\n    def compile(cls, N: int, M: int,\
    \ shift = -1):\n        def parse_fn(ts: TokenStream):\n            dsu = cls(N)\n\
    \            for _ in range(M): u, v = ts._line(); dsu.merge(int(u)+shift, int(v)+shift)\n\
    \            return dsu\n        return parse_fn\nfrom typing import Sequence\n\
    \n\nclass CSRIncremental(Sequence[list[_T]]):\n    def __init__(csr, sizes: list[int]):\n\
    \        csr.L, N = [0]*len(sizes), 0\n        for i,sz in enumerate(sizes):\n\
    \            csr.L[i] = N; N += sz\n        csr.R, csr.A = csr.L[:], [0]*N\n\n\
    \    def append(csr, i: int, x: _T):\n        csr.A[csr.R[i]] = x; csr.R[i] +=\
    \ 1\n    \n    def __iter__(csr):\n        for i,l in enumerate(csr.L):\n    \
    \        yield csr.A[l:csr.R[i]]\n    \n    def __getitem__(csr, i: int) -> _T:\n\
    \        return csr.A[i]\n    \n    def __len__(dsu):\n        return len(dsu.L)\n\
    \n    def range(csr, i: int) -> _T:\n        return range(csr.L[i], csr.R[i])\n\
    \ndef elist(est_len: int) -> list: ...\ntry:\n    from __pypy__ import newlist_hint\n\
    except:\n    def newlist_hint(hint):\n        return []\nelist = newlist_hint\n\
    \    \nimport operator\nfrom typing import Generic\n\n\nclass SkewHeapForrest(Generic[_T]):\n\
    \    def __init__(shf, N, M, e: _T = 0, op = operator.add):\n        shf.V, shf.A,\
    \ shf.L, shf.R, shf.roots = [e]*M, [e]*M, [-1]*M, [-1]*M, [-1]*N\n        shf.id,\
    \ shf.st, shf.e, shf.op = 0, elist(M), e, op\n    \n    def propagate(shf, u:\
    \ int):\n        if (a := shf.A[u]) != shf.e:\n            if ~(l := shf.L[u]):\
    \ shf.A[l] = shf.op(shf.A[l], a)\n            if ~(r := shf.R[u]): shf.A[r] =\
    \ shf.op(shf.A[r], a)\n            shf.V[u] = shf.op(shf.V[u], a); shf.A[u] =\
    \ shf.e\n\n    def merge(shf, u: int, v: int):\n        while ~u and ~v:\n   \
    \         shf.propagate(u); shf.propagate(v)\n            if shf.V[v] < shf.V[u]:\
    \ u, v = v, u\n            shf.st.append(u); shf.R[u], u = shf.L[u], shf.R[u]\n\
    \        u = u if ~u else v\n        while shf.st: shf.L[u := shf.st.pop()] =\
    \ u\n        return u\n    \n    def min(shf, i: int):\n        assert ~(root\
    \ := shf.roots[i])\n        shf.propagate(root)\n        return shf.V[root]\n\n\
    \    def push(shf, i: int, x: _T):\n        shf.V[shf.id] = x\n        shf.roots[i]\
    \ = shf.merge(shf.roots[i], shf.id)\n        shf.id += 1\n\n    def pop(shf, i:\
    \ int) -> _T:\n        assert ~(root := shf.roots[i])\n        shf.propagate(root)\n\
    \        val, shf.roots[i] = shf.V[root], shf.merge(shf.L[root], shf.R[root])\n\
    \        return val\n    \n    def add(shf, i: int, val: _T): shf.A[shf.roots[i]]\
    \ = shf.op(shf.A[shf.roots[i]], val)\n    def empty(shf, i: int): return shf.roots[i]\
    \ == -1\n    \n\n# Configure benchmark\nconfig = BenchmarkConfig(\n    name=\"\
    edge_list\",\n    sizes=[1000000, 100000, 10000, 1000, 100, 10, 1],  # Reverse\
    \ order to warm up JIT\n    operations=['sum_weights', 'filter', 'degree_count',\
    \ 'transform', 'sort', 'construction'],\n    iterations=10,\n    warmup=2,\n \
    \   output_dir=\"./output/benchmark_results/edge_list\"\n)\n\n# Create benchmark\
    \ instance\nbenchmark = Benchmark(config)\n\n# Data generators\n@benchmark.data_generator(\"\
    default\")\ndef generate_edge_data(size: int, operation: str):\n    \"\"\"Generate\
    \ edge list data in all formats\"\"\"\n    max_node = max(1, int(size ** 0.5)\
    \ * 2)\n    \n    # Generate raw edge data\n    U = [random.randint(0, max_node)\
    \ for _ in range(size)]\n    V = [random.randint(0, max_node) for _ in range(size)]\n\
    \    W = [random.randint(1, 1000) for _ in range(size)]\n    \n    # Create different\
    \ representations\n    edges_tuple = [(U[i], V[i], W[i]) for i in range(size)]\n\
    \    edge_list = EdgeListWeighted(max_node + 1, U, V, W)\n    \n    # Pre-initialize\
    \ data for fair timing (exclude initialization)\n    preinitialized = {\n    \
    \    'edges_tuple': list(edges_tuple),\n        'edge_list': EdgeListWeighted(max_node\
    \ + 1, list(U), list(V), list(W)),\n        'U': list(U), 'V': list(V), 'W': list(W),\n\
    \        'threshold': 500,\n        'max_node': max_node,\n        'degree_array':\
    \ [0] * (max_node + 1)\n    }\n    \n    return {\n        'edges_tuple': edges_tuple,\n\
    \        'edge_list': edge_list,\n        'U': U, 'V': V, 'W': W,\n        'size':\
    \ size,\n        'operation': operation,\n        'threshold': 500,\n        'max_node':\
    \ max_node,\n        'preinitialized': preinitialized\n    }\n\n# Construction\
    \ benchmarks - all should do equivalent work\n@benchmark.implementation(\"construct_tuple\"\
    , \"construction\")\ndef construct_tuple_list(data):\n    \"\"\"Construct list\
    \ of tuples from raw data\"\"\"\n    U, V, W = data['U'], data['V'], data['W']\n\
    \    return [(U[i], V[i], W[i]) for i in range(len(U))]\n\n@benchmark.implementation(\"\
    construct_edge_list_ref\", \"construction\")\ndef construct_edge_list_ref(data):\n\
    \    \"\"\"Construct EdgeListWeighted from raw data (reference assignment)\"\"\
    \"\n    U, V, W = data['U'], data['V'], data['W']\n    return EdgeListWeighted(data['max_node']\
    \ + 1, U, V, W)\n\n@benchmark.implementation(\"construct_edge_list_copy\", \"\
    construction\")\ndef construct_edge_list_copy(data):\n    \"\"\"Construct EdgeListWeighted\
    \ from copied data (fair comparison)\"\"\"\n    U, V, W = data['U'], data['V'],\
    \ data['W']\n    return EdgeListWeighted(data['max_node'] + 1, list(U), list(V),\
    \ list(W))\n\n@benchmark.implementation(\"construct_separated\", \"construction\"\
    )\ndef construct_separated_lists(data):\n    \"\"\"Create separated lists (copy\
    \ data)\"\"\"\n    U, V, W = data['U'], data['V'], data['W']\n    return (list(U),\
    \ list(V), list(W))\n\n# Sum weights operation\n@benchmark.implementation(\"tuple_direct\"\
    , \"sum_weights\")\ndef sum_weights_tuple_direct(data):\n    \"\"\"Sum weights\
    \ using direct tuple iteration\"\"\"\n    return sum(w for u, v, w in data['edges_tuple'])\n\
    \n@benchmark.implementation(\"edge_list_iter\", \"sum_weights\")\ndef sum_weights_edge_list_iter(data):\n\
    \    \"\"\"Sum weights using EdgeListWeighted iteration\"\"\"\n    return sum(w\
    \ for u, v, w in data['edge_list'])\n\n@benchmark.implementation(\"edge_list_direct\"\
    , \"sum_weights\")\ndef sum_weights_edge_list_direct(data):\n    \"\"\"Sum weights\
    \ using EdgeListWeighted direct access\"\"\"\n    return sum(data['edge_list'].W)\n\
    \n@benchmark.implementation(\"separated_lists\", \"sum_weights\")\ndef sum_weights_separated(data):\n\
    \    \"\"\"Sum weights using separated lists\"\"\"\n    return sum(data['W'])\n\
    \n# Filter operation\n@benchmark.implementation(\"tuple_direct\", \"filter\")\n\
    def filter_tuple_direct(data):\n    \"\"\"Filter edges using tuple iteration\"\
    \"\"\n    threshold = data['threshold']\n    return [(u, v, w) for u, v, w in\
    \ data['edges_tuple'] if w > threshold]\n\n@benchmark.implementation(\"edge_list_iter\"\
    , \"filter\")\ndef filter_edge_list_iter(data):\n    \"\"\"Filter edges using\
    \ EdgeListWeighted iteration\"\"\"\n    threshold = data['threshold']\n    return\
    \ [(u, v, w) for u, v, w in data['edge_list'] if w > threshold]\n\n@benchmark.implementation(\"\
    edge_list_direct\", \"filter\")\ndef filter_edge_list_direct(data):\n    \"\"\"\
    Filter edges using EdgeListWeighted direct access\"\"\"\n    threshold = data['threshold']\n\
    \    edge_list = data['edge_list']\n    result = []\n    for i in range(len(edge_list)):\n\
    \        if edge_list.W[i] > threshold:\n            result.append((edge_list.U[i],\
    \ edge_list.V[i], edge_list.W[i]))\n    return result\n\n@benchmark.implementation(\"\
    separated_lists\", \"filter\")\ndef filter_separated(data):\n    \"\"\"Filter\
    \ edges using separated lists\"\"\"\n    threshold = data['threshold']\n    U,\
    \ V, W = data['U'], data['V'], data['W']\n    return [(U[i], V[i], W[i]) for i\
    \ in range(len(W)) if W[i] > threshold]\n\n# Degree count operation\n@benchmark.implementation(\"\
    tuple_direct\", \"degree_count\")\ndef degree_count_tuple_direct(data):\n    \"\
    \"\"Count degrees using tuple iteration\"\"\"\n    degree = [0] * (data['max_node']\
    \ + 1)\n    for u, v, w in data['edges_tuple']:\n        degree[u] += 1\n    return\
    \ degree\n\n@benchmark.implementation(\"edge_list_iter\", \"degree_count\")\n\
    def degree_count_edge_list_iter(data):\n    \"\"\"Count degrees using EdgeListWeighted\
    \ iteration\"\"\"\n    degree = [0] * (data['max_node'] + 1)\n    for u, v, w\
    \ in data['edge_list']:\n        degree[u] += 1\n    return degree\n\n@benchmark.implementation(\"\
    edge_list_direct\", \"degree_count\")\ndef degree_count_edge_list_direct(data):\n\
    \    \"\"\"Count degrees using EdgeListWeighted direct access\"\"\"\n    degree\
    \ = [0] * (data['max_node'] + 1)\n    for u in data['edge_list'].U:\n        degree[u]\
    \ += 1\n    return degree\n\n@benchmark.implementation(\"separated_lists\", \"\
    degree_count\")\ndef degree_count_separated(data):\n    \"\"\"Count degrees using\
    \ separated lists\"\"\"\n    degree = [0] * (data['max_node'] + 1)\n    for u\
    \ in data['U']:\n        degree[u] += 1\n    return degree\n\n# Transform operation\n\
    @benchmark.implementation(\"tuple_direct\", \"transform\")\ndef transform_tuple_direct(data):\n\
    \    \"\"\"Transform edges using tuple iteration\"\"\"\n    return [(u, v, w *\
    \ 2) for u, v, w in data['edges_tuple']]\n\n@benchmark.implementation(\"edge_list_iter\"\
    , \"transform\")\ndef transform_edge_list_iter(data):\n    \"\"\"Transform edges\
    \ using EdgeListWeighted iteration\"\"\"\n    return [(u, v, w * 2) for u, v,\
    \ w in data['edge_list']]\n\n@benchmark.implementation(\"edge_list_direct\", \"\
    transform\")\ndef transform_edge_list_direct(data):\n    \"\"\"Transform edges\
    \ using EdgeListWeighted direct access\"\"\"\n    edge_list = data['edge_list']\n\
    \    return [(edge_list.U[i], edge_list.V[i], edge_list.W[i] * 2) \n         \
    \   for i in range(len(edge_list))]\n\n@benchmark.implementation(\"separated_lists\"\
    , \"transform\")\ndef transform_separated(data):\n    \"\"\"Transform edges using\
    \ separated lists\"\"\"\n    U, V, W = data['U'], data['V'], data['W']\n    return\
    \ [(U[i], V[i], W[i] * 2) for i in range(len(W))]\n\n# Sort operation\n@benchmark.implementation(\"\
    tuple_direct\", \"sort\")\ndef sort_tuple_direct(data):\n    \"\"\"Sort edges\
    \ using tuple list\"\"\"\n    edges = list(data['edges_tuple'])\n    edges.sort(key=lambda\
    \ x: x[2])\n    return edges\n\n@benchmark.implementation(\"edge_list_sort\",\
    \ \"sort\")\ndef sort_edge_list_builtin(data):\n    \"\"\"Sort edges using EdgeListWeighted\
    \ built-in sort\"\"\"\n    edge_list = EdgeListWeighted(data['edge_list'].N, \n\
    \                                list(data['edge_list'].U), \n               \
    \                 list(data['edge_list'].V), \n                              \
    \  list(data['edge_list'].W))\n    edge_list.sort()\n    return edge_list\n\n\
    @benchmark.implementation(\"separated_lists\", \"sort\")\ndef sort_separated(data):\n\
    \    \"\"\"Sort edges using separated lists\"\"\"\n    U, V, W = list(data['U']),\
    \ list(data['V']), list(data['W'])\n    # Sort by weight using indices\n    indices\
    \ = sorted(range(len(W)), key=lambda i: W[i])\n    return ([U[i] for i in indices],\
    \ [V[i] for i in indices], [W[i] for i in indices])\n\n# Custom validators\n@benchmark.validator(\"\
    sort\")\ndef validate_sort(expected, actual):\n    \"\"\"Validate that sort results\
    \ are equivalent\"\"\"\n    # Convert both to comparable format\n    if hasattr(expected,\
    \ 'W'):  # EdgeListWeighted\n        expected_weights = expected.W\n    elif isinstance(expected,\
    \ tuple):  # separated lists\n        expected_weights = expected[2]\n    else:\
    \  # list of tuples\n        expected_weights = [w for u, v, w in expected]\n\
    \    \n    if hasattr(actual, 'W'):  # EdgeListWeighted\n        actual_weights\
    \ = actual.W\n    elif isinstance(actual, tuple):  # separated lists\n       \
    \ actual_weights = actual[2]\n    else:  # list of tuples\n        actual_weights\
    \ = [w for u, v, w in actual]\n    \n    return expected_weights == actual_weights\n\
    \n@benchmark.validator(\"construction\")\ndef validate_construction(expected,\
    \ actual):\n    \"\"\"Validate construction results\"\"\"\n    # Just check that\
    \ something was created and has the right size\n    if actual is None:\n     \
    \   return False\n    \n    # Check based on type\n    if isinstance(actual, list):\
    \  # tuple list\n        return len(actual) > 0\n    elif hasattr(actual, 'M'):\
    \  # EdgeListWeighted\n        return actual.M > 0\n    elif isinstance(actual,\
    \ tuple):  # separated lists\n        return len(actual[0]) > 0\n    \n    return\
    \ True\n\nif __name__ == \"__main__\":\n    # Parse command line args and run\
    \ appropriate mode\n    runner = benchmark.parse_args()\n    runner.run()\n"
  code: "#!/usr/bin/env python3\n\"\"\"\nSimple edge list benchmark using the new\
    \ declarative framework.\nMuch less boilerplate, easier to understand and extend.\n\
    \"\"\"\n\nimport random\nimport sys\nimport os\nsys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))\n\
    \nfrom cp_library.perf.benchmark import Benchmark, BenchmarkConfig\nfrom cp_library.alg.graph.edge.edge_list_weighted_cls\
    \ import EdgeListWeighted\n\n# Configure benchmark\nconfig = BenchmarkConfig(\n\
    \    name=\"edge_list\",\n    sizes=[1000000, 100000, 10000, 1000, 100, 10, 1],\
    \  # Reverse order to warm up JIT\n    operations=['sum_weights', 'filter', 'degree_count',\
    \ 'transform', 'sort', 'construction'],\n    iterations=10,\n    warmup=2,\n \
    \   output_dir=\"./output/benchmark_results/edge_list\"\n)\n\n# Create benchmark\
    \ instance\nbenchmark = Benchmark(config)\n\n# Data generators\n@benchmark.data_generator(\"\
    default\")\ndef generate_edge_data(size: int, operation: str):\n    \"\"\"Generate\
    \ edge list data in all formats\"\"\"\n    max_node = max(1, int(size ** 0.5)\
    \ * 2)\n    \n    # Generate raw edge data\n    U = [random.randint(0, max_node)\
    \ for _ in range(size)]\n    V = [random.randint(0, max_node) for _ in range(size)]\n\
    \    W = [random.randint(1, 1000) for _ in range(size)]\n    \n    # Create different\
    \ representations\n    edges_tuple = [(U[i], V[i], W[i]) for i in range(size)]\n\
    \    edge_list = EdgeListWeighted(max_node + 1, U, V, W)\n    \n    # Pre-initialize\
    \ data for fair timing (exclude initialization)\n    preinitialized = {\n    \
    \    'edges_tuple': list(edges_tuple),\n        'edge_list': EdgeListWeighted(max_node\
    \ + 1, list(U), list(V), list(W)),\n        'U': list(U), 'V': list(V), 'W': list(W),\n\
    \        'threshold': 500,\n        'max_node': max_node,\n        'degree_array':\
    \ [0] * (max_node + 1)\n    }\n    \n    return {\n        'edges_tuple': edges_tuple,\n\
    \        'edge_list': edge_list,\n        'U': U, 'V': V, 'W': W,\n        'size':\
    \ size,\n        'operation': operation,\n        'threshold': 500,\n        'max_node':\
    \ max_node,\n        'preinitialized': preinitialized\n    }\n\n# Construction\
    \ benchmarks - all should do equivalent work\n@benchmark.implementation(\"construct_tuple\"\
    , \"construction\")\ndef construct_tuple_list(data):\n    \"\"\"Construct list\
    \ of tuples from raw data\"\"\"\n    U, V, W = data['U'], data['V'], data['W']\n\
    \    return [(U[i], V[i], W[i]) for i in range(len(U))]\n\n@benchmark.implementation(\"\
    construct_edge_list_ref\", \"construction\")\ndef construct_edge_list_ref(data):\n\
    \    \"\"\"Construct EdgeListWeighted from raw data (reference assignment)\"\"\
    \"\n    U, V, W = data['U'], data['V'], data['W']\n    return EdgeListWeighted(data['max_node']\
    \ + 1, U, V, W)\n\n@benchmark.implementation(\"construct_edge_list_copy\", \"\
    construction\")\ndef construct_edge_list_copy(data):\n    \"\"\"Construct EdgeListWeighted\
    \ from copied data (fair comparison)\"\"\"\n    U, V, W = data['U'], data['V'],\
    \ data['W']\n    return EdgeListWeighted(data['max_node'] + 1, list(U), list(V),\
    \ list(W))\n\n@benchmark.implementation(\"construct_separated\", \"construction\"\
    )\ndef construct_separated_lists(data):\n    \"\"\"Create separated lists (copy\
    \ data)\"\"\"\n    U, V, W = data['U'], data['V'], data['W']\n    return (list(U),\
    \ list(V), list(W))\n\n# Sum weights operation\n@benchmark.implementation(\"tuple_direct\"\
    , \"sum_weights\")\ndef sum_weights_tuple_direct(data):\n    \"\"\"Sum weights\
    \ using direct tuple iteration\"\"\"\n    return sum(w for u, v, w in data['edges_tuple'])\n\
    \n@benchmark.implementation(\"edge_list_iter\", \"sum_weights\")\ndef sum_weights_edge_list_iter(data):\n\
    \    \"\"\"Sum weights using EdgeListWeighted iteration\"\"\"\n    return sum(w\
    \ for u, v, w in data['edge_list'])\n\n@benchmark.implementation(\"edge_list_direct\"\
    , \"sum_weights\")\ndef sum_weights_edge_list_direct(data):\n    \"\"\"Sum weights\
    \ using EdgeListWeighted direct access\"\"\"\n    return sum(data['edge_list'].W)\n\
    \n@benchmark.implementation(\"separated_lists\", \"sum_weights\")\ndef sum_weights_separated(data):\n\
    \    \"\"\"Sum weights using separated lists\"\"\"\n    return sum(data['W'])\n\
    \n# Filter operation\n@benchmark.implementation(\"tuple_direct\", \"filter\")\n\
    def filter_tuple_direct(data):\n    \"\"\"Filter edges using tuple iteration\"\
    \"\"\n    threshold = data['threshold']\n    return [(u, v, w) for u, v, w in\
    \ data['edges_tuple'] if w > threshold]\n\n@benchmark.implementation(\"edge_list_iter\"\
    , \"filter\")\ndef filter_edge_list_iter(data):\n    \"\"\"Filter edges using\
    \ EdgeListWeighted iteration\"\"\"\n    threshold = data['threshold']\n    return\
    \ [(u, v, w) for u, v, w in data['edge_list'] if w > threshold]\n\n@benchmark.implementation(\"\
    edge_list_direct\", \"filter\")\ndef filter_edge_list_direct(data):\n    \"\"\"\
    Filter edges using EdgeListWeighted direct access\"\"\"\n    threshold = data['threshold']\n\
    \    edge_list = data['edge_list']\n    result = []\n    for i in range(len(edge_list)):\n\
    \        if edge_list.W[i] > threshold:\n            result.append((edge_list.U[i],\
    \ edge_list.V[i], edge_list.W[i]))\n    return result\n\n@benchmark.implementation(\"\
    separated_lists\", \"filter\")\ndef filter_separated(data):\n    \"\"\"Filter\
    \ edges using separated lists\"\"\"\n    threshold = data['threshold']\n    U,\
    \ V, W = data['U'], data['V'], data['W']\n    return [(U[i], V[i], W[i]) for i\
    \ in range(len(W)) if W[i] > threshold]\n\n# Degree count operation\n@benchmark.implementation(\"\
    tuple_direct\", \"degree_count\")\ndef degree_count_tuple_direct(data):\n    \"\
    \"\"Count degrees using tuple iteration\"\"\"\n    degree = [0] * (data['max_node']\
    \ + 1)\n    for u, v, w in data['edges_tuple']:\n        degree[u] += 1\n    return\
    \ degree\n\n@benchmark.implementation(\"edge_list_iter\", \"degree_count\")\n\
    def degree_count_edge_list_iter(data):\n    \"\"\"Count degrees using EdgeListWeighted\
    \ iteration\"\"\"\n    degree = [0] * (data['max_node'] + 1)\n    for u, v, w\
    \ in data['edge_list']:\n        degree[u] += 1\n    return degree\n\n@benchmark.implementation(\"\
    edge_list_direct\", \"degree_count\")\ndef degree_count_edge_list_direct(data):\n\
    \    \"\"\"Count degrees using EdgeListWeighted direct access\"\"\"\n    degree\
    \ = [0] * (data['max_node'] + 1)\n    for u in data['edge_list'].U:\n        degree[u]\
    \ += 1\n    return degree\n\n@benchmark.implementation(\"separated_lists\", \"\
    degree_count\")\ndef degree_count_separated(data):\n    \"\"\"Count degrees using\
    \ separated lists\"\"\"\n    degree = [0] * (data['max_node'] + 1)\n    for u\
    \ in data['U']:\n        degree[u] += 1\n    return degree\n\n# Transform operation\n\
    @benchmark.implementation(\"tuple_direct\", \"transform\")\ndef transform_tuple_direct(data):\n\
    \    \"\"\"Transform edges using tuple iteration\"\"\"\n    return [(u, v, w *\
    \ 2) for u, v, w in data['edges_tuple']]\n\n@benchmark.implementation(\"edge_list_iter\"\
    , \"transform\")\ndef transform_edge_list_iter(data):\n    \"\"\"Transform edges\
    \ using EdgeListWeighted iteration\"\"\"\n    return [(u, v, w * 2) for u, v,\
    \ w in data['edge_list']]\n\n@benchmark.implementation(\"edge_list_direct\", \"\
    transform\")\ndef transform_edge_list_direct(data):\n    \"\"\"Transform edges\
    \ using EdgeListWeighted direct access\"\"\"\n    edge_list = data['edge_list']\n\
    \    return [(edge_list.U[i], edge_list.V[i], edge_list.W[i] * 2) \n         \
    \   for i in range(len(edge_list))]\n\n@benchmark.implementation(\"separated_lists\"\
    , \"transform\")\ndef transform_separated(data):\n    \"\"\"Transform edges using\
    \ separated lists\"\"\"\n    U, V, W = data['U'], data['V'], data['W']\n    return\
    \ [(U[i], V[i], W[i] * 2) for i in range(len(W))]\n\n# Sort operation\n@benchmark.implementation(\"\
    tuple_direct\", \"sort\")\ndef sort_tuple_direct(data):\n    \"\"\"Sort edges\
    \ using tuple list\"\"\"\n    edges = list(data['edges_tuple'])\n    edges.sort(key=lambda\
    \ x: x[2])\n    return edges\n\n@benchmark.implementation(\"edge_list_sort\",\
    \ \"sort\")\ndef sort_edge_list_builtin(data):\n    \"\"\"Sort edges using EdgeListWeighted\
    \ built-in sort\"\"\"\n    edge_list = EdgeListWeighted(data['edge_list'].N, \n\
    \                                list(data['edge_list'].U), \n               \
    \                 list(data['edge_list'].V), \n                              \
    \  list(data['edge_list'].W))\n    edge_list.sort()\n    return edge_list\n\n\
    @benchmark.implementation(\"separated_lists\", \"sort\")\ndef sort_separated(data):\n\
    \    \"\"\"Sort edges using separated lists\"\"\"\n    U, V, W = list(data['U']),\
    \ list(data['V']), list(data['W'])\n    # Sort by weight using indices\n    indices\
    \ = sorted(range(len(W)), key=lambda i: W[i])\n    return ([U[i] for i in indices],\
    \ [V[i] for i in indices], [W[i] for i in indices])\n\n# Custom validators\n@benchmark.validator(\"\
    sort\")\ndef validate_sort(expected, actual):\n    \"\"\"Validate that sort results\
    \ are equivalent\"\"\"\n    # Convert both to comparable format\n    if hasattr(expected,\
    \ 'W'):  # EdgeListWeighted\n        expected_weights = expected.W\n    elif isinstance(expected,\
    \ tuple):  # separated lists\n        expected_weights = expected[2]\n    else:\
    \  # list of tuples\n        expected_weights = [w for u, v, w in expected]\n\
    \    \n    if hasattr(actual, 'W'):  # EdgeListWeighted\n        actual_weights\
    \ = actual.W\n    elif isinstance(actual, tuple):  # separated lists\n       \
    \ actual_weights = actual[2]\n    else:  # list of tuples\n        actual_weights\
    \ = [w for u, v, w in actual]\n    \n    return expected_weights == actual_weights\n\
    \n@benchmark.validator(\"construction\")\ndef validate_construction(expected,\
    \ actual):\n    \"\"\"Validate construction results\"\"\"\n    # Just check that\
    \ something was created and has the right size\n    if actual is None:\n     \
    \   return False\n    \n    # Check based on type\n    if isinstance(actual, list):\
    \  # tuple list\n        return len(actual) > 0\n    elif hasattr(actual, 'M'):\
    \  # EdgeListWeighted\n        return actual.M > 0\n    elif isinstance(actual,\
    \ tuple):  # separated lists\n        return len(actual[0]) > 0\n    \n    return\
    \ True\n\nif __name__ == \"__main__\":\n    # Parse command line args and run\
    \ appropriate mode\n    runner = benchmark.parse_args()\n    runner.run()"
  dependsOn:
  - cp_library/perf/benchmark.py
  - cp_library/alg/graph/edge/edge_list_weighted_cls.py
  - cp_library/alg/iter/sort/isort_parallel_fn.py
  - cp_library/alg/iter/sort/sort_parallel_fn.py
  - cp_library/io/parser_cls.py
  - cp_library/alg/iter/arg/argsort_fn.py
  - cp_library/bit/pack/packer_cls.py
  - cp_library/ds/dsu_cls.py
  - cp_library/ds/elist_fn.py
  - cp_library/ds/heap/skew_heap_forrest_cls.py
  - cp_library/ds/csr/csr_incremental_cls.py
  - cp_library/io/fast_io_cls.py
  isVerificationFile: false
  path: perf/edge_list.py
  requiredBy: []
  timestamp: '2025-07-11 23:11:42+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: perf/edge_list.py
layout: document
redirect_from:
- /library/perf/edge_list.py
- /library/perf/edge_list.py.html
title: perf/edge_list.py
---
