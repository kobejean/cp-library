---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/iter/arg/argsort_ranged_fn.py
    title: cp_library/alg/iter/arg/argsort_ranged_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/iter/sort/isort_ranged_fn.py
    title: cp_library/alg/iter/sort/isort_ranged_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/pack/packer_cls.py
    title: cp_library/bit/pack/packer_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/view/view2_cls.py
    title: cp_library/ds/view/view2_cls.py
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
  bundledCode: "#!/usr/bin/env python3\n\"\"\"\nBenchmark comparing view2 (dual-array\
    \ view) vs tuple list.\nTests tuple access, iteration, sorting, modification,\
    \ and append/pop operations.\n\"\"\"\n\nimport random\nimport sys\nimport os\n\
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
    \ {speedup:<10.1f}x\")\n\n\n\n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2578\n             https://kobejean.github.io/cp-library \
    \              \n'''\n\n\n\n\ndef argsort_ranged(A: list[int], l: int, r: int,\
    \ reverse=False):\n    P = Packer(r-l-1); I = [A[l+i] for i in range(r-l)]; P.ienumerate(I,\
    \ reverse); I.sort()\n    for i in range(r-l): I[i] = (I[i] & P.m) + l\n    return\
    \ I\n\n\n\nclass Packer:\n    __slots__ = 's', 'm'\n    def __init__(P, mx: int):\
    \ P.s = mx.bit_length(); P.m = (1 << P.s) - 1\n    def enc(P, a: int, b: int):\
    \ return a << P.s | b\n    def dec(P, x: int) -> tuple[int, int]: return x >>\
    \ P.s, x & P.m\n    def enumerate(P, A, reverse=False): P.ienumerate(A:=list(A),\
    \ reverse); return A\n    def ienumerate(P, A, reverse=False):\n        if reverse:\n\
    \            for i,a in enumerate(A): A[i] = P.enc(-a, i)\n        else:\n   \
    \         for i,a in enumerate(A): A[i] = P.enc(a, i)\n    def indices(P, A: list[int]):\
    \ P.iindices(A:=list(A)); return A\n    def iindices(P, A):\n        for i,a in\
    \ enumerate(A): A[i] = P.m&a\n\n\ndef isort_ranged(*L: list, l: int, r: int, reverse=False):\n\
    \    n = r - l\n    order = argsort_ranged(L[0], l, r, reverse=reverse)\n    inv\
    \ = [0] * n\n    # order contains indices in range [l, r), need to map to [0,\
    \ n)\n    for i in range(n): inv[order[i]-l] = i\n    for i in range(n):\n   \
    \     j = order[i] - l  # j is in range [0, n)\n        for A in L: A[l+i], A[l+j]\
    \ = A[l+j], A[l+i]\n        order[inv[i]], order[inv[j]] = order[inv[j]], order[inv[i]]\n\
    \        inv[i], inv[j] = inv[j], inv[i]\n    return L\nfrom typing import Generic\n\
    from typing import TypeVar\n_S = TypeVar('S')\n_T = TypeVar('T')\n_U = TypeVar('U')\n\
    _T1 = TypeVar('T1')\n_T2 = TypeVar('T2')\n_T3 = TypeVar('T3')\n_T4 = TypeVar('T4')\n\
    _T5 = TypeVar('T5')\n_T6 = TypeVar('T6')\n\n\n\nclass view2(Generic[_S, _T]):\n\
    \    __slots__ = 'A', 'B', 'l', 'r'\n    def __init__(V, A: list[_S], B: list[_T],\
    \ l: int, r: int): V.A, V.B, V.l, V.r = A, B, l, r\n    def __len__(V): return\
    \ V.r - V.l\n    def __getitem__(V, i: int): \n        if 0 <= i < V.r - V.l:\
    \ return V.A[V.l+i], V.B[V.l+i]\n        else: raise IndexError\n    def __setitem__(V,\
    \ i: int, v: tuple[_S, _T]): V.A[V.l+i], V.B[V.l+i] = v\n    def __contains__(V,\
    \ v: tuple[_S, _T]): raise NotImplemented\n    def set_range(V, l: int, r: int):\
    \ V.l, V.r = l, r\n    def index(V, v: tuple[_S, _T]): raise NotImplemented\n\
    \    def reverse(V):\n        l, r = V.l, V.r-1\n        while l < r: V.A[l],\
    \ V.A[r] = V.A[r], V.A[l]; V.B[l], V.B[r] = V.B[r], V.B[l]; l += 1; r -= 1\n \
    \   def sort(V, reverse=False): isort_ranged(V.A, V.B, l=V.l, r=V.r, reverse=reverse)\n\
    \    def pop(V): V.r -= 1; return V.A[V.r], V.B[V.r]\n    def append(V, v: tuple[_S,\
    \ _T]): V.A[V.r], V.B[V.r] = v; V.r += 1\n    def popleft(V): V.l += 1; return\
    \ V.A[V.l-1], V.B[V.l-1]\n    def appendleft(V, v: tuple[_S, _T]): V.l -= 1; V.A[V.l],\
    \ V.B[V.l]  = v; \n    def validate(V): return 0 <= V.l <= V.r <= len(V.A)\n\n\
    # Configure benchmark\nconfig = BenchmarkConfig(\n    name=\"view2\",\n    sizes=[1000000,\
    \ 100000, 10000, 1000, 100],  # Reverse order to warm up JIT\n    operations=['tuple_access',\
    \ 'iteration', 'sorting', 'modification', 'append_pop'],\n    iterations=10,\n\
    \    warmup=3,\n    output_dir=\"./output/benchmark_results/view2\"\n)\n\n# Create\
    \ benchmark instance\nbenchmark = Benchmark(config)\n\n# Data generator\n@benchmark.data_generator(\"\
    default\")\ndef generate_view2_data(size: int, operation: str):\n    \"\"\"Generate\
    \ test data for view2 operations\"\"\"\n    # Generate parallel arrays\n    A\
    \ = [random.randint(1, 1000000) for _ in range(size)]\n    B = [random.randint(1,\
    \ 1000000) for _ in range(size)]\n    \n    # Create view2 covering full range\n\
    \    view2 = view2(A.copy(), B.copy(), 0, size)\n    \n    # Create equivalent\
    \ data structures\n    tuple_list = [(A[i], B[i]) for i in range(size)]\n    \n\
    \    return {\n        'view2': view2,\n        'tuple_list': tuple_list,\n  \
    \      'A': A.copy(),\n        'B': B.copy(),\n        'size': size\n    }\n\n\
    # Setup functions for operations that modify data\n@benchmark.setup(\"view2\"\
    , [\"modification\", \"sorting\", \"append_pop\"])\ndef setup_view2_modify(data):\n\
    \    \"\"\"Setup function that copies view2 data before modification\"\"\"\n \
    \   new_data = data.copy()\n    A_copy = data['A'].copy()\n    B_copy = data['B'].copy()\n\
    \    new_data['view2'] = view2(A_copy, B_copy, 0, data['size'])\n    return new_data\n\
    \n@benchmark.setup(\"tuple_list\", [\"modification\", \"sorting\", \"append_pop\"\
    ])\ndef setup_tuple_list_modify(data):\n    \"\"\"Setup function that copies tuple\
    \ list before modification\"\"\"\n    new_data = data.copy()\n    new_data['tuple_list']\
    \ = data['tuple_list'].copy()\n    return new_data\n\n# Tuple access operation\n\
    @benchmark.implementation(\"view2\", \"tuple_access\")\ndef tuple_access_view2(data):\n\
    \    \"\"\"Access tuples using view2[i]\"\"\"\n    view2 = data['view2']\n   \
    \ checksum = 0\n    for i in range(len(view2)):\n        a, b = view2[i]\n   \
    \     checksum ^= a ^ b\n    return checksum\n\n@benchmark.implementation(\"tuple_list\"\
    , \"tuple_access\")\ndef tuple_access_tuple_list(data):\n    \"\"\"Access tuples\
    \ using list[i]\"\"\"\n    tuple_list = data['tuple_list']\n    checksum = 0\n\
    \    for i in range(len(tuple_list)):\n        a, b = tuple_list[i]\n        checksum\
    \ ^= a ^ b\n    return checksum\n\n# Iteration operation\n@benchmark.implementation(\"\
    view2\", \"iteration\")\ndef iteration_view2(data):\n    \"\"\"Iterate through\
    \ view2 using for-in (no __iter__)\"\"\"\n    view2 = data['view2']\n    checksum\
    \ = 0\n    for a, b in view2:  # Uses __getitem__ with IndexError\n        checksum\
    \ ^= a ^ b\n    return checksum\n\n@benchmark.implementation(\"tuple_list\", \"\
    iteration\")\ndef iteration_tuple_list(data):\n    \"\"\"Iterate through tuple\
    \ list using for-in\"\"\"\n    tuple_list = data['tuple_list']\n    checksum =\
    \ 0\n    for a, b in tuple_list:\n        checksum ^= a ^ b\n    return checksum\n\
    \n# Sorting operation\n@benchmark.implementation(\"view2\", \"sorting\")\ndef\
    \ sorting_view2(data):\n    \"\"\"Sort view2 using isort_ranged\"\"\"\n    view2\
    \ = data['view2']\n    view2.sort()  # Uses isort_ranged on view range\n    \n\
    \    checksum = 0\n    for i in range(min(100, len(view2))):\n        a, b = view2[i]\n\
    \        checksum ^= a ^ b\n    return checksum\n\n@benchmark.implementation(\"\
    tuple_list\", \"sorting\")\ndef sorting_tuple_list(data):\n    \"\"\"Sort tuple\
    \ list by first element\"\"\"\n    tuple_list = data['tuple_list']\n    tuple_list.sort(key=lambda\
    \ x: x[0])\n    \n    checksum = 0\n    for i in range(min(100, len(tuple_list))):\n\
    \        a, b = tuple_list[i]\n        checksum ^= a ^ b\n    return checksum\n\
    \n# Modification operation\n@benchmark.implementation(\"view2\", \"modification\"\
    )\ndef modification_view2(data):\n    \"\"\"Modify view2 elements using __setitem__\"\
    \"\"\n    view2 = data['view2']\n    checksum = 0\n    for i in range(len(view2)):\n\
    \        a, b = view2[i]\n        new_a = (a * 2) & 0xFFFFFFFF\n        new_b\
    \ = (b * 3) & 0xFFFFFFFF\n        view2[i] = (new_a, new_b)\n        checksum\
    \ ^= new_a ^ new_b\n    return checksum\n\n@benchmark.implementation(\"tuple_list\"\
    , \"modification\")\ndef modification_tuple_list(data):\n    \"\"\"Modify tuple\
    \ list elements\"\"\"\n    tuple_list = data['tuple_list']\n    checksum = 0\n\
    \    for i in range(len(tuple_list)):\n        a, b = tuple_list[i]\n        new_a\
    \ = (a * 2) & 0xFFFFFFFF\n        new_b = (b * 3) & 0xFFFFFFFF\n        tuple_list[i]\
    \ = (new_a, new_b)\n        checksum ^= new_a ^ new_b\n    return checksum\n\n\
    # Append/pop operation\n@benchmark.implementation(\"view2\", \"append_pop\")\n\
    def append_pop_view2(data):\n    \"\"\"Test view2 append/pop operations\"\"\"\n\
    \    view2 = data['view2']\n    checksum = 0\n    operations = min(1000, len(view2)\
    \ // 10)\n    \n    # Pop from end and append back\n    for _ in range(operations):\n\
    \        a, b = view2.pop()\n        checksum ^= a ^ b\n    for i in range(operations):\n\
    \        view2.append((i + 1000, i + 2000))\n        checksum ^= (i + 1000) ^\
    \ (i + 2000)\n    return checksum\n\n@benchmark.implementation(\"tuple_list\"\
    , \"append_pop\")\ndef append_pop_tuple_list(data):\n    \"\"\"Test tuple list\
    \ append/pop operations\"\"\"\n    tuple_list = data['tuple_list']\n    checksum\
    \ = 0\n    operations = min(1000, len(tuple_list) // 10)\n    \n    # Pop from\
    \ end and append back\n    for _ in range(operations):\n        a, b = tuple_list.pop()\n\
    \        checksum ^= a ^ b\n    for i in range(operations):\n        tuple_list.append((i\
    \ + 1000, i + 2000))\n        checksum ^= (i + 1000) ^ (i + 2000)\n    return\
    \ checksum\n\nif __name__ == \"__main__\":\n    # Parse command line args and\
    \ run appropriate mode\n    runner = benchmark.parse_args()\n    runner.run()\n"
  code: "#!/usr/bin/env python3\n\"\"\"\nBenchmark comparing view2 (dual-array view)\
    \ vs tuple list.\nTests tuple access, iteration, sorting, modification, and append/pop\
    \ operations.\n\"\"\"\n\nimport random\nimport sys\nimport os\nsys.path.insert(0,\
    \ os.path.dirname(os.path.dirname(os.path.abspath(__file__))))\n\nfrom cp_library.perf.benchmark\
    \ import Benchmark, BenchmarkConfig\nfrom cp_library.ds.view.view2_cls import\
    \ view2\n\n# Configure benchmark\nconfig = BenchmarkConfig(\n    name=\"view2\"\
    ,\n    sizes=[1000000, 100000, 10000, 1000, 100],  # Reverse order to warm up\
    \ JIT\n    operations=['tuple_access', 'iteration', 'sorting', 'modification',\
    \ 'append_pop'],\n    iterations=10,\n    warmup=3,\n    output_dir=\"./output/benchmark_results/view2\"\
    \n)\n\n# Create benchmark instance\nbenchmark = Benchmark(config)\n\n# Data generator\n\
    @benchmark.data_generator(\"default\")\ndef generate_view2_data(size: int, operation:\
    \ str):\n    \"\"\"Generate test data for view2 operations\"\"\"\n    # Generate\
    \ parallel arrays\n    A = [random.randint(1, 1000000) for _ in range(size)]\n\
    \    B = [random.randint(1, 1000000) for _ in range(size)]\n    \n    # Create\
    \ view2 covering full range\n    view2 = view2(A.copy(), B.copy(), 0, size)\n\
    \    \n    # Create equivalent data structures\n    tuple_list = [(A[i], B[i])\
    \ for i in range(size)]\n    \n    return {\n        'view2': view2,\n       \
    \ 'tuple_list': tuple_list,\n        'A': A.copy(),\n        'B': B.copy(),\n\
    \        'size': size\n    }\n\n# Setup functions for operations that modify data\n\
    @benchmark.setup(\"view2\", [\"modification\", \"sorting\", \"append_pop\"])\n\
    def setup_view2_modify(data):\n    \"\"\"Setup function that copies view2 data\
    \ before modification\"\"\"\n    new_data = data.copy()\n    A_copy = data['A'].copy()\n\
    \    B_copy = data['B'].copy()\n    new_data['view2'] = view2(A_copy, B_copy,\
    \ 0, data['size'])\n    return new_data\n\n@benchmark.setup(\"tuple_list\", [\"\
    modification\", \"sorting\", \"append_pop\"])\ndef setup_tuple_list_modify(data):\n\
    \    \"\"\"Setup function that copies tuple list before modification\"\"\"\n \
    \   new_data = data.copy()\n    new_data['tuple_list'] = data['tuple_list'].copy()\n\
    \    return new_data\n\n# Tuple access operation\n@benchmark.implementation(\"\
    view2\", \"tuple_access\")\ndef tuple_access_view2(data):\n    \"\"\"Access tuples\
    \ using view2[i]\"\"\"\n    view2 = data['view2']\n    checksum = 0\n    for i\
    \ in range(len(view2)):\n        a, b = view2[i]\n        checksum ^= a ^ b\n\
    \    return checksum\n\n@benchmark.implementation(\"tuple_list\", \"tuple_access\"\
    )\ndef tuple_access_tuple_list(data):\n    \"\"\"Access tuples using list[i]\"\
    \"\"\n    tuple_list = data['tuple_list']\n    checksum = 0\n    for i in range(len(tuple_list)):\n\
    \        a, b = tuple_list[i]\n        checksum ^= a ^ b\n    return checksum\n\
    \n# Iteration operation\n@benchmark.implementation(\"view2\", \"iteration\")\n\
    def iteration_view2(data):\n    \"\"\"Iterate through view2 using for-in (no __iter__)\"\
    \"\"\n    view2 = data['view2']\n    checksum = 0\n    for a, b in view2:  # Uses\
    \ __getitem__ with IndexError\n        checksum ^= a ^ b\n    return checksum\n\
    \n@benchmark.implementation(\"tuple_list\", \"iteration\")\ndef iteration_tuple_list(data):\n\
    \    \"\"\"Iterate through tuple list using for-in\"\"\"\n    tuple_list = data['tuple_list']\n\
    \    checksum = 0\n    for a, b in tuple_list:\n        checksum ^= a ^ b\n  \
    \  return checksum\n\n# Sorting operation\n@benchmark.implementation(\"view2\"\
    , \"sorting\")\ndef sorting_view2(data):\n    \"\"\"Sort view2 using isort_ranged\"\
    \"\"\n    view2 = data['view2']\n    view2.sort()  # Uses isort_ranged on view\
    \ range\n    \n    checksum = 0\n    for i in range(min(100, len(view2))):\n \
    \       a, b = view2[i]\n        checksum ^= a ^ b\n    return checksum\n\n@benchmark.implementation(\"\
    tuple_list\", \"sorting\")\ndef sorting_tuple_list(data):\n    \"\"\"Sort tuple\
    \ list by first element\"\"\"\n    tuple_list = data['tuple_list']\n    tuple_list.sort(key=lambda\
    \ x: x[0])\n    \n    checksum = 0\n    for i in range(min(100, len(tuple_list))):\n\
    \        a, b = tuple_list[i]\n        checksum ^= a ^ b\n    return checksum\n\
    \n# Modification operation\n@benchmark.implementation(\"view2\", \"modification\"\
    )\ndef modification_view2(data):\n    \"\"\"Modify view2 elements using __setitem__\"\
    \"\"\n    view2 = data['view2']\n    checksum = 0\n    for i in range(len(view2)):\n\
    \        a, b = view2[i]\n        new_a = (a * 2) & 0xFFFFFFFF\n        new_b\
    \ = (b * 3) & 0xFFFFFFFF\n        view2[i] = (new_a, new_b)\n        checksum\
    \ ^= new_a ^ new_b\n    return checksum\n\n@benchmark.implementation(\"tuple_list\"\
    , \"modification\")\ndef modification_tuple_list(data):\n    \"\"\"Modify tuple\
    \ list elements\"\"\"\n    tuple_list = data['tuple_list']\n    checksum = 0\n\
    \    for i in range(len(tuple_list)):\n        a, b = tuple_list[i]\n        new_a\
    \ = (a * 2) & 0xFFFFFFFF\n        new_b = (b * 3) & 0xFFFFFFFF\n        tuple_list[i]\
    \ = (new_a, new_b)\n        checksum ^= new_a ^ new_b\n    return checksum\n\n\
    # Append/pop operation\n@benchmark.implementation(\"view2\", \"append_pop\")\n\
    def append_pop_view2(data):\n    \"\"\"Test view2 append/pop operations\"\"\"\n\
    \    view2 = data['view2']\n    checksum = 0\n    operations = min(1000, len(view2)\
    \ // 10)\n    \n    # Pop from end and append back\n    for _ in range(operations):\n\
    \        a, b = view2.pop()\n        checksum ^= a ^ b\n    for i in range(operations):\n\
    \        view2.append((i + 1000, i + 2000))\n        checksum ^= (i + 1000) ^\
    \ (i + 2000)\n    return checksum\n\n@benchmark.implementation(\"tuple_list\"\
    , \"append_pop\")\ndef append_pop_tuple_list(data):\n    \"\"\"Test tuple list\
    \ append/pop operations\"\"\"\n    tuple_list = data['tuple_list']\n    checksum\
    \ = 0\n    operations = min(1000, len(tuple_list) // 10)\n    \n    # Pop from\
    \ end and append back\n    for _ in range(operations):\n        a, b = tuple_list.pop()\n\
    \        checksum ^= a ^ b\n    for i in range(operations):\n        tuple_list.append((i\
    \ + 1000, i + 2000))\n        checksum ^= (i + 1000) ^ (i + 2000)\n    return\
    \ checksum\n\nif __name__ == \"__main__\":\n    # Parse command line args and\
    \ run appropriate mode\n    runner = benchmark.parse_args()\n    runner.run()"
  dependsOn:
  - cp_library/perf/benchmark.py
  - cp_library/ds/view/view2_cls.py
  - cp_library/alg/iter/sort/isort_ranged_fn.py
  - cp_library/alg/iter/arg/argsort_ranged_fn.py
  - cp_library/bit/pack/packer_cls.py
  isVerificationFile: false
  path: perf/view2.py
  requiredBy: []
  timestamp: '2025-07-20 06:26:01+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: perf/view2.py
layout: document
redirect_from:
- /library/perf/view2.py
- /library/perf/view2.py.html
title: perf/view2.py
---
