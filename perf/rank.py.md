---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/dp/max2_fn.py
    title: cp_library/alg/dp/max2_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/iter/rank/irank_fn.py
    title: cp_library/alg/iter/rank/irank_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/iter/rank/irank_multi_fn.py
    title: cp_library/alg/iter/rank/irank_multi_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/pack/packer3_cls.py
    title: cp_library/bit/pack/packer3_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/pack/packer_cls.py
    title: cp_library/bit/pack/packer_cls.py
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
  bundledCode: "#!/usr/bin/env python3\n\"\"\"\nSimple ranking benchmark using the\
    \ new declarative framework.\nCompares irank vs irank_multi performance across\
    \ different data patterns.\n\"\"\"\n\nimport random\nimport sys\nimport os\nsys.path.insert(0,\
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
    \              \n'''\n\n\n\n\ndef irank(A: list[int], distinct = False):\n   \
    \ P = Packer(len(A)-1); V = P.enumerate(A); V.sort()\n    if distinct:\n     \
    \   for r, ai in enumerate(V): a, i = P.dec(ai); A[i], V[r] = r, a\n    elif V:\n\
    \        r, p = -1, V[-1]+1 # set p to unique value to trigger `if a != p` on\
    \ first elm\n        for ai in V:\n            a, i = P.dec(ai)\n            if\
    \ a!=p: V[r:=r+1] = p = a\n            A[i] = r\n        del V[r+1:]\n    return\
    \ V\n\n\n\nclass Packer:\n    __slots__ = 's', 'm'\n    def __init__(P, mx: int):\
    \ P.s = mx.bit_length(); P.m = (1 << P.s) - 1\n    def enc(P, a: int, b: int):\
    \ return a << P.s | b\n    def dec(P, x: int) -> tuple[int, int]: return x >>\
    \ P.s, x & P.m\n    def enumerate(P, A, reverse=False): P.ienumerate(A:=list(A),\
    \ reverse); return A\n    def ienumerate(P, A, reverse=False):\n        if reverse:\n\
    \            for i,a in enumerate(A): A[i] = P.enc(-a, i)\n        else:\n   \
    \         for i,a in enumerate(A): A[i] = P.enc(a, i)\n    def indices(P, A: list[int]):\
    \ P.iindices(A:=list(A)); return A\n    def iindices(P, A):\n        for i,a in\
    \ enumerate(A): A[i] = P.m&a\n\n\ndef max2(a, b):\n    return a if a > b else\
    \ b\n\ndef irank(*A: list[int], distinct = False):\n    N = mxj = 0\n    for Ai\
    \ in A: N += len(Ai); mxj = max2(mxj, len(Ai))\n    P = Packer3(len(A)-1, mxj);\
    \ V = P.enumerate(A, N); V.sort()\n    if distinct:\n        for r,aij in enumerate(V):a,i,j=P.dec(aij);A[i][j],V[r]=r,a\n\
    \    elif V:\n        r, p = -1, V[-1]+1 # set p to unique value to trigger `if\
    \ a != p` on first elm\n        for aij in V:\n            a,i,j=P.dec(aij)\n\
    \            if a!=p:V[r:=r+1]=p=a\n            A[i][j]=r\n        del V[r+1:]\n\
    \    return V\n\nclass Packer3:\n    def __init__(P, mxb: int, mxc: int):\n  \
    \      bb, bc = mxb.bit_length(), mxc.bit_length()\n        P.mc, P.mb, P.sb,\
    \ P.sa = (1<<bc)-1, (1<<bb)-1, bc, bc+bb\n    def enc(P, a: int, b: int, c: int):\
    \ return a << P.sa | b << P.sb | c\n    def dec(P, x: int) -> tuple[int, int,\
    \ int]: return x >> P.sa, (x >> P.sb) & P.mb, x & P.mc\n    def enumerate(P, A,\
    \ N, reverse=False): \n        V, k = [0]*N, 0\n        if reverse:\n        \
    \    for i,Ai in enumerate(A):\n                for j, a in enumerate(Ai):V[k]=P.enc(-a,\
    \ i, j);k+=1\n        else:\n            for i,Ai in enumerate(A):\n         \
    \       for j, a in enumerate(Ai):V[k]=P.enc(a, i, j);k+=1\n        return V\n\
    \n# Configure benchmark\nconfig = BenchmarkConfig(\n    name=\"rank\",\n    sizes=[1000000,\
    \ 100000, 10000, 1000, 100, 10, 1],  # Reverse order to warm up JIT\n    operations=['construction',\
    \ 'random', 'sorted', 'duplicates', 'reverse'],\n    iterations=5,\n    warmup=3,\n\
    \    output_dir=\"./output/benchmark_results/rank\"\n)\n\n# Create benchmark instance\n\
    benchmark = Benchmark(config)\n\n# Data generator\n@benchmark.data_generator(\"\
    default\")\ndef generate_rank_data(size: int, operation: str):\n    \"\"\"Generate\
    \ ranking data in different patterns\"\"\"\n    if operation == 'random':\n  \
    \      data = [random.randint(1, size) for _ in range(size)]\n    elif operation\
    \ == 'sorted':\n        data = list(range(size))\n    elif operation == 'duplicates':\n\
    \        # Many duplicates (10% unique values)\n        unique_count = max(1,\
    \ size // 10)\n        data = [random.randint(1, unique_count) for _ in range(size)]\n\
    \    elif operation == 'reverse':\n        data = list(range(size, 0, -1))\n \
    \   else:\n        raise ValueError(f\"Unknown operation: {operation}\")\n   \
    \ \n    # Pre-initialize data for fair timing (exclude copy overhead)\n    preinitialized\
    \ = {\n        'data_copy1': list(data),\n        'data_copy2': list(data),\n\
    \        'distinct': False\n    }\n    \n    return {\n        'data': data,\n\
    \        'distinct': False,\n        'size': size,\n        'operation': operation,\n\
    \        'preinitialized': preinitialized\n    }\n\n# Construction operation\n\
    @benchmark.implementation(\"irank\", \"construction\")\ndef construction_irank(data):\n\
    \    \"\"\"Construct data copy for irank\"\"\"\n    data_copy = list(data['data'])\n\
    \    checksum = 0\n    for x in data_copy:\n        checksum ^= x\n    return\
    \ checksum\n\n@benchmark.implementation(\"irank_multi\", \"construction\")\ndef\
    \ construction_irank_multi(data):\n    \"\"\"Construct data copy for irank_multi\"\
    \"\"\n    data_copy = list(data['data'])\n    checksum = 0\n    for x in data_copy:\n\
    \        checksum ^= x\n    return checksum\n\n# Random operation\n@benchmark.implementation(\"\
    irank\", \"random\")\ndef random_irank(data):\n    \"\"\"Standard irank implementation\
    \ for random data\"\"\"\n    pre = data['preinitialized']\n    result = irank(pre['data_copy1'],\
    \ distinct=pre['distinct'])\n    checksum = 0\n    for x in result:\n        checksum\
    \ ^= x\n    return checksum\n\n@benchmark.implementation(\"irank_multi\", \"random\"\
    )\ndef random_irank_multi(data):\n    \"\"\"Multi-pass irank implementation for\
    \ random data\"\"\"\n    pre = data['preinitialized']\n    result = irank_multi(pre['data_copy2'],\
    \ distinct=pre['distinct'])\n    checksum = 0\n    for x in result:\n        checksum\
    \ ^= x\n    return checksum\n\n# Sorted operation\n@benchmark.implementation(\"\
    irank\", \"sorted\")\ndef sorted_irank(data):\n    \"\"\"Standard irank implementation\
    \ for sorted data\"\"\"\n    pre = data['preinitialized']\n    result = irank(pre['data_copy1'],\
    \ distinct=pre['distinct'])\n    checksum = 0\n    for x in result:\n        checksum\
    \ ^= x\n    return checksum\n\n@benchmark.implementation(\"irank_multi\", \"sorted\"\
    )\ndef sorted_irank_multi(data):\n    \"\"\"Multi-pass irank implementation for\
    \ sorted data\"\"\"\n    pre = data['preinitialized']\n    result = irank_multi(pre['data_copy2'],\
    \ distinct=pre['distinct'])\n    checksum = 0\n    for x in result:\n        checksum\
    \ ^= x\n    return checksum\n\n# Duplicates operation\n@benchmark.implementation(\"\
    irank\", \"duplicates\")\ndef duplicates_irank(data):\n    \"\"\"Standard irank\
    \ implementation for data with duplicates\"\"\"\n    pre = data['preinitialized']\n\
    \    result = irank(pre['data_copy1'], distinct=pre['distinct'])\n    checksum\
    \ = 0\n    for x in result:\n        checksum ^= x\n    return checksum\n\n@benchmark.implementation(\"\
    irank_multi\", \"duplicates\")\ndef duplicates_irank_multi(data):\n    \"\"\"\
    Multi-pass irank implementation for data with duplicates\"\"\"\n    pre = data['preinitialized']\n\
    \    result = irank_multi(pre['data_copy2'], distinct=pre['distinct'])\n    checksum\
    \ = 0\n    for x in result:\n        checksum ^= x\n    return checksum\n\n# Reverse\
    \ operation\n@benchmark.implementation(\"irank\", \"reverse\")\ndef reverse_irank(data):\n\
    \    \"\"\"Standard irank implementation for reverse data\"\"\"\n    pre = data['preinitialized']\n\
    \    result = irank(pre['data_copy1'], distinct=pre['distinct'])\n    checksum\
    \ = 0\n    for x in result:\n        checksum ^= x\n    return checksum\n\n@benchmark.implementation(\"\
    irank_multi\", \"reverse\")\ndef reverse_irank_multi(data):\n    \"\"\"Multi-pass\
    \ irank implementation for reverse data\"\"\"\n    pre = data['preinitialized']\n\
    \    result = irank_multi(pre['data_copy2'], distinct=pre['distinct'])\n    checksum\
    \ = 0\n    for x in result:\n        checksum ^= x\n    return checksum\n\n# Additional\
    \ benchmark with distinct=True\n@benchmark.data_generator(\"distinct\")\ndef generate_rank_data_distinct(size:\
    \ int, operation: str):\n    \"\"\"Generate ranking data with distinct=True\"\"\
    \"\n    base_data = generate_rank_data(size, operation)\n    base_data['distinct']\
    \ = True\n    base_data['preinitialized']['distinct'] = True\n    return base_data\n\
    \ndef irank_distinct_implementation(data):\n    \"\"\"irank with distinct=True\"\
    \"\"\n    pre = data['preinitialized']\n    result = irank(pre['data_copy1'],\
    \ distinct=True)\n    checksum = 0\n    for x in result:\n        checksum ^=\
    \ x\n    return checksum\n\ndef irank_multi_distinct_implementation(data):\n \
    \   \"\"\"irank_multi with distinct=True\"\"\"\n    pre = data['preinitialized']\n\
    \    result = irank_multi(pre['data_copy2'], distinct=True)\n    checksum = 0\n\
    \    for x in result:\n        checksum ^= x\n    return checksum\n\n# Custom\
    \ validator for rank results (now using XOR checksums)\n@benchmark.validator(\"\
    default\")\ndef validate_rank_result(expected, actual):\n    \"\"\"Validate ranking\
    \ results using XOR checksums\"\"\"\n    try:\n        # Compare XOR checksums\
    \ directly\n        return int(expected) == int(actual)\n    except Exception:\n\
    \        return False\n\nif __name__ == \"__main__\":\n    # Parse command line\
    \ args and run appropriate mode\n    runner = benchmark.parse_args()\n    runner.run()\n"
  code: "#!/usr/bin/env python3\n\"\"\"\nSimple ranking benchmark using the new declarative\
    \ framework.\nCompares irank vs irank_multi performance across different data\
    \ patterns.\n\"\"\"\n\nimport random\nimport sys\nimport os\nsys.path.insert(0,\
    \ os.path.dirname(os.path.dirname(os.path.abspath(__file__))))\n\nfrom cp_library.perf.benchmark\
    \ import Benchmark, BenchmarkConfig\nfrom cp_library.alg.iter.rank.irank_fn import\
    \ irank\nfrom cp_library.alg.iter.rank.irank_multi_fn import irank as irank_multi\n\
    \n# Configure benchmark\nconfig = BenchmarkConfig(\n    name=\"rank\",\n    sizes=[1000000,\
    \ 100000, 10000, 1000, 100, 10, 1],  # Reverse order to warm up JIT\n    operations=['construction',\
    \ 'random', 'sorted', 'duplicates', 'reverse'],\n    iterations=5,\n    warmup=3,\n\
    \    output_dir=\"./output/benchmark_results/rank\"\n)\n\n# Create benchmark instance\n\
    benchmark = Benchmark(config)\n\n# Data generator\n@benchmark.data_generator(\"\
    default\")\ndef generate_rank_data(size: int, operation: str):\n    \"\"\"Generate\
    \ ranking data in different patterns\"\"\"\n    if operation == 'random':\n  \
    \      data = [random.randint(1, size) for _ in range(size)]\n    elif operation\
    \ == 'sorted':\n        data = list(range(size))\n    elif operation == 'duplicates':\n\
    \        # Many duplicates (10% unique values)\n        unique_count = max(1,\
    \ size // 10)\n        data = [random.randint(1, unique_count) for _ in range(size)]\n\
    \    elif operation == 'reverse':\n        data = list(range(size, 0, -1))\n \
    \   else:\n        raise ValueError(f\"Unknown operation: {operation}\")\n   \
    \ \n    # Pre-initialize data for fair timing (exclude copy overhead)\n    preinitialized\
    \ = {\n        'data_copy1': list(data),\n        'data_copy2': list(data),\n\
    \        'distinct': False\n    }\n    \n    return {\n        'data': data,\n\
    \        'distinct': False,\n        'size': size,\n        'operation': operation,\n\
    \        'preinitialized': preinitialized\n    }\n\n# Construction operation\n\
    @benchmark.implementation(\"irank\", \"construction\")\ndef construction_irank(data):\n\
    \    \"\"\"Construct data copy for irank\"\"\"\n    data_copy = list(data['data'])\n\
    \    checksum = 0\n    for x in data_copy:\n        checksum ^= x\n    return\
    \ checksum\n\n@benchmark.implementation(\"irank_multi\", \"construction\")\ndef\
    \ construction_irank_multi(data):\n    \"\"\"Construct data copy for irank_multi\"\
    \"\"\n    data_copy = list(data['data'])\n    checksum = 0\n    for x in data_copy:\n\
    \        checksum ^= x\n    return checksum\n\n# Random operation\n@benchmark.implementation(\"\
    irank\", \"random\")\ndef random_irank(data):\n    \"\"\"Standard irank implementation\
    \ for random data\"\"\"\n    pre = data['preinitialized']\n    result = irank(pre['data_copy1'],\
    \ distinct=pre['distinct'])\n    checksum = 0\n    for x in result:\n        checksum\
    \ ^= x\n    return checksum\n\n@benchmark.implementation(\"irank_multi\", \"random\"\
    )\ndef random_irank_multi(data):\n    \"\"\"Multi-pass irank implementation for\
    \ random data\"\"\"\n    pre = data['preinitialized']\n    result = irank_multi(pre['data_copy2'],\
    \ distinct=pre['distinct'])\n    checksum = 0\n    for x in result:\n        checksum\
    \ ^= x\n    return checksum\n\n# Sorted operation\n@benchmark.implementation(\"\
    irank\", \"sorted\")\ndef sorted_irank(data):\n    \"\"\"Standard irank implementation\
    \ for sorted data\"\"\"\n    pre = data['preinitialized']\n    result = irank(pre['data_copy1'],\
    \ distinct=pre['distinct'])\n    checksum = 0\n    for x in result:\n        checksum\
    \ ^= x\n    return checksum\n\n@benchmark.implementation(\"irank_multi\", \"sorted\"\
    )\ndef sorted_irank_multi(data):\n    \"\"\"Multi-pass irank implementation for\
    \ sorted data\"\"\"\n    pre = data['preinitialized']\n    result = irank_multi(pre['data_copy2'],\
    \ distinct=pre['distinct'])\n    checksum = 0\n    for x in result:\n        checksum\
    \ ^= x\n    return checksum\n\n# Duplicates operation\n@benchmark.implementation(\"\
    irank\", \"duplicates\")\ndef duplicates_irank(data):\n    \"\"\"Standard irank\
    \ implementation for data with duplicates\"\"\"\n    pre = data['preinitialized']\n\
    \    result = irank(pre['data_copy1'], distinct=pre['distinct'])\n    checksum\
    \ = 0\n    for x in result:\n        checksum ^= x\n    return checksum\n\n@benchmark.implementation(\"\
    irank_multi\", \"duplicates\")\ndef duplicates_irank_multi(data):\n    \"\"\"\
    Multi-pass irank implementation for data with duplicates\"\"\"\n    pre = data['preinitialized']\n\
    \    result = irank_multi(pre['data_copy2'], distinct=pre['distinct'])\n    checksum\
    \ = 0\n    for x in result:\n        checksum ^= x\n    return checksum\n\n# Reverse\
    \ operation\n@benchmark.implementation(\"irank\", \"reverse\")\ndef reverse_irank(data):\n\
    \    \"\"\"Standard irank implementation for reverse data\"\"\"\n    pre = data['preinitialized']\n\
    \    result = irank(pre['data_copy1'], distinct=pre['distinct'])\n    checksum\
    \ = 0\n    for x in result:\n        checksum ^= x\n    return checksum\n\n@benchmark.implementation(\"\
    irank_multi\", \"reverse\")\ndef reverse_irank_multi(data):\n    \"\"\"Multi-pass\
    \ irank implementation for reverse data\"\"\"\n    pre = data['preinitialized']\n\
    \    result = irank_multi(pre['data_copy2'], distinct=pre['distinct'])\n    checksum\
    \ = 0\n    for x in result:\n        checksum ^= x\n    return checksum\n\n# Additional\
    \ benchmark with distinct=True\n@benchmark.data_generator(\"distinct\")\ndef generate_rank_data_distinct(size:\
    \ int, operation: str):\n    \"\"\"Generate ranking data with distinct=True\"\"\
    \"\n    base_data = generate_rank_data(size, operation)\n    base_data['distinct']\
    \ = True\n    base_data['preinitialized']['distinct'] = True\n    return base_data\n\
    \ndef irank_distinct_implementation(data):\n    \"\"\"irank with distinct=True\"\
    \"\"\n    pre = data['preinitialized']\n    result = irank(pre['data_copy1'],\
    \ distinct=True)\n    checksum = 0\n    for x in result:\n        checksum ^=\
    \ x\n    return checksum\n\ndef irank_multi_distinct_implementation(data):\n \
    \   \"\"\"irank_multi with distinct=True\"\"\"\n    pre = data['preinitialized']\n\
    \    result = irank_multi(pre['data_copy2'], distinct=True)\n    checksum = 0\n\
    \    for x in result:\n        checksum ^= x\n    return checksum\n\n# Custom\
    \ validator for rank results (now using XOR checksums)\n@benchmark.validator(\"\
    default\")\ndef validate_rank_result(expected, actual):\n    \"\"\"Validate ranking\
    \ results using XOR checksums\"\"\"\n    try:\n        # Compare XOR checksums\
    \ directly\n        return int(expected) == int(actual)\n    except Exception:\n\
    \        return False\n\nif __name__ == \"__main__\":\n    # Parse command line\
    \ args and run appropriate mode\n    runner = benchmark.parse_args()\n    runner.run()"
  dependsOn:
  - cp_library/perf/benchmark.py
  - cp_library/alg/iter/rank/irank_fn.py
  - cp_library/alg/iter/rank/irank_multi_fn.py
  - cp_library/bit/pack/packer_cls.py
  - cp_library/alg/dp/max2_fn.py
  - cp_library/bit/pack/packer3_cls.py
  isVerificationFile: false
  path: perf/rank.py
  requiredBy: []
  timestamp: '2025-07-11 23:11:42+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: perf/rank.py
layout: document
redirect_from:
- /library/perf/rank.py
- /library/perf/rank.py.html
title: perf/rank.py
---
