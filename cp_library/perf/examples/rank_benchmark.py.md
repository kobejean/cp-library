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
  bundledCode: "\"\"\"\nDeclarative benchmark framework with minimal boilerplate.\n\
    \nFeatures:\n- Decorator-based benchmark registration\n- Automatic data generation\
    \ and validation\n- Built-in timing with warmup\n- Configurable operations and\
    \ sizes\n- JSON results and matplotlib plotting\n\"\"\"\n\nimport time\nimport\
    \ json\nimport statistics\nfrom typing import Dict, List, Any, Callable, Union\n\
    from dataclasses import dataclass\nfrom pathlib import Path\nfrom collections\
    \ import defaultdict\n\n@dataclass\nclass BenchmarkConfig:\n    \"\"\"Configuration\
    \ for benchmark runs\"\"\"\n    name: str\n    sizes: List[int] = None\n    operations:\
    \ List[str] = None\n    iterations: int = 10\n    warmup: int = 2\n    output_dir:\
    \ str = \"./output/benchmark_results\"\n    save_results: bool = True\n    plot_results:\
    \ bool = True\n    plot_scale: str = \"loglog\"  # Options: \"loglog\", \"linear\"\
    , \"semilogx\", \"semilogy\"\n    \n    def __post_init__(self):\n        if self.sizes\
    \ is None:\n            self.sizes = [100, 1000, 10000, 100000]\n        if self.operations\
    \ is None:\n            self.operations = ['default']\n\nclass Benchmark:\n  \
    \  \"\"\"Declarative benchmark framework using decorators\"\"\"\n    \n    def\
    \ __init__(self, config: BenchmarkConfig):\n        self.config = config\n   \
    \     self.data_generators = {}\n        self.implementations = {}\n        self.validators\
    \ = {}\n        self.results = []\n        \n    def data_generator(self, name:\
    \ str = \"default\"):\n        \"\"\"Decorator to register data generator\"\"\"\
    \n        def decorator(func):\n            self.data_generators[name] = func\n\
    \            return func\n        return decorator\n    \n    def implementation(self,\
    \ name: str, operations: Union[str, List[str]] = None):\n        \"\"\"Decorator\
    \ to register implementation\"\"\"\n        if operations is None:\n         \
    \   operations = ['default']\n        elif isinstance(operations, str):\n    \
    \        operations = [operations]\n            \n        def decorator(func):\n\
    \            for op in operations:\n                if op not in self.implementations:\n\
    \                    self.implementations[op] = {}\n                self.implementations[op][name]\
    \ = func\n            return func\n        return decorator\n    \n    def validator(self,\
    \ operation: str = \"default\"):\n        \"\"\"Decorator to register custom validator\"\
    \"\"\n        def decorator(func):\n            self.validators[operation] = func\n\
    \            return func\n        return decorator\n    \n    def measure_time(self,\
    \ func: Callable, data: Any) -> tuple[Any, float]:\n        \"\"\"Measure execution\
    \ time with warmup\"\"\"\n        # Warmup runs\n        for _ in range(self.config.warmup):\n\
    \            try:\n                func(data)\n            except Exception:\n\
    \                # If warmup fails, let the main measurement handle the error\n\
    \                break\n        \n        # Actual measurement\n        start\
    \ = time.perf_counter()\n        for _ in range(self.config.iterations):\n   \
    \         result = func(data)\n        elapsed_ms = (time.perf_counter() - start)\
    \ * 1000 / self.config.iterations\n        \n        return result, elapsed_ms\n\
    \    \n    def validate_result(self, expected: Any, actual: Any, operation: str)\
    \ -> bool:\n        \"\"\"Validate result using custom validator or default comparison\"\
    \"\"\n        if operation in self.validators:\n            return self.validators[operation](expected,\
    \ actual)\n        return expected == actual\n    \n    def run(self):\n     \
    \   \"\"\"Run all benchmarks\"\"\"\n        print(f\"Running {self.config.name}\"\
    )\n        print(f\"Sizes: {self.config.sizes}\")\n        print(f\"Operations:\
    \ {self.config.operations}\")\n        print(\"=\"*80)\n        \n        for\
    \ size in self.config.sizes:\n            for operation in self.config.operations:\n\
    \                print(f\"\\nOperation: {operation}, Size: {size}\")\n       \
    \         print(\"-\" * 50)\n                \n                # Generate test\
    \ data\n                generator = self.data_generators.get(operation, \n   \
    \                                                self.data_generators.get('default'))\n\
    \                if not generator:\n                    raise ValueError(f\"No\
    \ data generator for operation: {operation}\")\n                \n           \
    \     test_data = generator(size, operation)\n                \n             \
    \   # Get implementations for this operation\n                impls = self.implementations.get(operation,\
    \ {})\n                if not impls:\n                    print(f\"No implementations\
    \ for operation: {operation}\")\n                    continue\n              \
    \  \n                # Run reference implementation first\n                ref_name,\
    \ ref_impl = next(iter(impls.items()))\n                expected_result, _ = self.measure_time(ref_impl,\
    \ test_data)\n                \n                # Run all implementations\n  \
    \              for impl_name, impl_func in impls.items():\n                  \
    \  try:\n                        result, time_ms = self.measure_time(impl_func,\
    \ test_data)\n                        correct = self.validate_result(expected_result,\
    \ result, operation)\n                        \n                        # Store\
    \ result\n                        self.results.append({\n                    \
    \        'operation': operation,\n                            'size': size,\n\
    \                            'implementation': impl_name,\n                  \
    \          'time_ms': time_ms,\n                            'correct': correct,\n\
    \                            'error': None\n                        })\n     \
    \                   \n                        status = \"OK\" if correct else\
    \ \"FAIL\"\n                        print(f\"  {impl_name:<20} {time_ms:>8.3f}\
    \ ms  {status}\")\n                        \n                    except Exception\
    \ as e:\n                        self.results.append({\n                     \
    \       'operation': operation,\n                            'size': size,\n \
    \                           'implementation': impl_name,\n                   \
    \         'time_ms': float('inf'),\n                            'correct': False,\n\
    \                            'error': str(e)\n                        })\n   \
    \                     print(f\"  {impl_name:<20} ERROR: {str(e)[:40]}\")\n   \
    \     \n        # Save and plot results\n        if self.config.save_results:\n\
    \            self._save_results()\n        \n        if self.config.plot_results:\n\
    \            self._plot_results()\n        \n        # Print summary\n       \
    \ self._print_summary()\n    \n    def _save_results(self):\n        \"\"\"Save\
    \ results to JSON\"\"\"\n        output_dir = Path(self.config.output_dir)\n \
    \       output_dir.mkdir(parents=True, exist_ok=True)\n        \n        filename\
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
    \ {speedup:<10.1f}x\")\n\n\nfrom cp_library.perf.generators import create_generator\n\
    '''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\n   \
    \          https://kobejean.github.io/cp-library               \n'''\n\n\n\n\n\
    def irank(A: list[int], distinct = False):\n    P = Packer(len(A)-1); V = P.enumerate(A);\
    \ V.sort()\n    if distinct:\n        for r, ai in enumerate(V): a, i = P.dec(ai);\
    \ A[i], V[r] = r, a\n    elif V:\n        r, p = -1, V[-1]+1 # set p to unique\
    \ value to trigger `if a != p` on first elm\n        for ai in V:\n          \
    \  a, i = P.dec(ai)\n            if a!=p: V[r:=r+1] = p = a\n            A[i]\
    \ = r\n        del V[r+1:]\n    return V\n\n\n\nclass Packer:\n    def __init__(P,\
    \ mx: int):\n        P.s = mx.bit_length()\n        P.m = (1 << P.s) - 1\n   \
    \ def enc(P, a: int, b: int): return a << P.s | b\n    def dec(P, x: int) -> tuple[int,\
    \ int]: return x >> P.s, x & P.m\n    def enumerate(P, A, reverse=False): P.ienumerate(A:=A.copy(),\
    \ reverse); return A\n    def ienumerate(P, A, reverse=False):\n        if reverse:\n\
    \            for i,a in enumerate(A): A[i] = P.enc(-a, i)\n        else:\n   \
    \         for i,a in enumerate(A): A[i] = P.enc(a, i)\n    def indices(P, A: list[int]):\
    \ P.iindices(A:=A.copy()); return A\n    def iindices(P, A):\n        for i,a\
    \ in enumerate(A): A[i] = P.m&a\n\n\ndef max2(a, b):\n    return a if a > b else\
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
    from itertools import product\nfrom typing import Dict, List, Any, Callable, Tuple\n\
    \nclass RankingBenchmark(Benchmark):\n    \"\"\"Benchmark for comparing ranking\
    \ algorithm implementations\"\"\"\n    \n    def generate_test_cases(self, param_grid:\
    \ Dict[str, List[Any]]) -> List[TestCase]:\n        \"\"\"Generate test cases\
    \ from parameter grid\"\"\"\n        test_cases = []\n        \n        # Extract\
    \ parameters\n        param_names = list(param_grid.keys())\n        param_values\
    \ = [param_grid[name] for name in param_names]\n        \n        for values in\
    \ product(*param_values):\n            params = dict(zip(param_names, values))\n\
    \            \n            # Generate data based on distribution parameter\n \
    \           size = params['size']\n            distribution = params['distribution']\n\
    \            \n            # Use the generator factory\n            generator\
    \ = create_generator(distribution)\n            data = generator.generate(size=size)\n\
    \            \n            # Create descriptive name\n            name = f\"size={size},\
    \ dist={distribution}, distinct={params.get('distinct', False)}\"\n          \
    \  \n            test_cases.append(TestCase(\n                name=name,\n   \
    \             params=params,\n                data={'data': data, 'distinct':\
    \ params.get('distinct', False)}\n            ))\n        \n        return test_cases\n\
    \    \n    def get_implementations(self) -> Dict[str, Callable]:\n        \"\"\
    \"Return implementations to benchmark\"\"\"\n        return {\n            'irank':\
    \ lambda data, distinct=False: irank(data.copy(), distinct=distinct),\n      \
    \      'irank_multi': lambda data, distinct=False: irank_multi(data.copy(), distinct=distinct)\n\
    \        }\n    \n    def measure_time(self, func: Callable, test_data: Dict)\
    \ -> Tuple[Any, float]:\n        \"\"\"Override to handle dict test data\"\"\"\
    \n        \n        # Warmup\n        for _ in range(self.config.warmup):\n  \
    \          func(**test_data)\n        \n        # Actual measurement\n       \
    \ start = time.perf_counter()\n        for _ in range(self.config.iterations):\n\
    \            result = func(**test_data)\n        elapsed_ms = (time.perf_counter()\
    \ - start) * 1000 / self.config.iterations\n        \n        return result, elapsed_ms\n\
    \ndef run_ranking_benchmark():\n    \"\"\"Run a comprehensive ranking algorithm\
    \ benchmark\"\"\"\n    \n    # Configure benchmark\n    config = BenchmarkConfig(\n\
    \        name=\"ranking_algorithms\",\n        iterations=10,\n        warmup=2,\n\
    \        save_results=True,\n        plot_results=False,  # Set to True if matplotlib\
    \ is installed\n        output_dir=\"./benchmark_results/ranking\"\n    )\n  \
    \  \n    # Create benchmark instance\n    benchmark = RankingBenchmark(config)\n\
    \    \n    # Define parameter grid\n    param_grid = {\n        'size': [100,\
    \ 1000, 10000, 50000],\n        'distribution': ['random', 'sorted', 'reverse',\
    \ 'duplicates', 'almost_sorted', 'plateau'],\n        'distinct': [True, False]\n\
    \    }\n    \n    # Run benchmark\n    benchmark.run(param_grid)\n    \n    #\
    \ Print summary statistics\n    print_summary(benchmark.results)\n\ndef print_summary(results):\n\
    \    \"\"\"Print summary statistics from benchmark results\"\"\"\n    \n    #\
    \ Group results by implementation\n    impl_times = defaultdict(list)\n    \n\
    \    for result in results:\n        if result.time_ms != float('inf'):\n    \
    \        impl_times[result.implementation].append(result.time_ms)\n    \n    print(\"\
    \\n\" + \"=\"*60)\n    print(\"SUMMARY STATISTICS\")\n    print(\"=\"*60)\n  \
    \  \n    print(f\"\\n{'Implementation':<20} {'Mean (ms)':<12} {'Std Dev':<12}\
    \ {'Min':<12} {'Max':<12} {'Samples':<10}\")\n    print(\"-\"*80)\n    \n    for\
    \ impl, times in impl_times.items():\n        if times:\n            mean_time\
    \ = statistics.mean(times)\n            std_time = statistics.stdev(times) if\
    \ len(times) > 1 else 0\n            min_time = min(times)\n            max_time\
    \ = max(times)\n            \n            print(f\"{impl:<20} {mean_time:<12.3f}\
    \ {std_time:<12.3f} {min_time:<12.3f} {max_time:<12.3f} {len(times):<10}\")\n\
    \    \n    # Calculate speedup ratios\n    if len(impl_times) == 2:\n        impls\
    \ = list(impl_times.keys())\n        impl1_mean = statistics.mean(impl_times[impls[0]])\n\
    \        impl2_mean = statistics.mean(impl_times[impls[1]])\n        speedup =\
    \ impl1_mean / impl2_mean\n        \n        faster = impls[1] if speedup > 1\
    \ else impls[0]\n        ratio = max(speedup, 1/speedup)\n        \n        print(f\"\
    \\n{faster} is {ratio:.2f}x faster on average\")\n\nif __name__ == \"__main__\"\
    :\n    run_ranking_benchmark()\n"
  code: "from cp_library.perf.benchmark import Benchmark, BenchmarkConfig, TestCase\n\
    from cp_library.perf.generators import create_generator\nfrom cp_library.alg.iter.rank.irank_fn\
    \ import irank\nfrom cp_library.alg.iter.rank.irank_multi_fn import irank as irank_multi\n\
    from itertools import product\nfrom typing import Dict, List, Any, Callable, Tuple\n\
    \nclass RankingBenchmark(Benchmark):\n    \"\"\"Benchmark for comparing ranking\
    \ algorithm implementations\"\"\"\n    \n    def generate_test_cases(self, param_grid:\
    \ Dict[str, List[Any]]) -> List[TestCase]:\n        \"\"\"Generate test cases\
    \ from parameter grid\"\"\"\n        test_cases = []\n        \n        # Extract\
    \ parameters\n        param_names = list(param_grid.keys())\n        param_values\
    \ = [param_grid[name] for name in param_names]\n        \n        for values in\
    \ product(*param_values):\n            params = dict(zip(param_names, values))\n\
    \            \n            # Generate data based on distribution parameter\n \
    \           size = params['size']\n            distribution = params['distribution']\n\
    \            \n            # Use the generator factory\n            generator\
    \ = create_generator(distribution)\n            data = generator.generate(size=size)\n\
    \            \n            # Create descriptive name\n            name = f\"size={size},\
    \ dist={distribution}, distinct={params.get('distinct', False)}\"\n          \
    \  \n            test_cases.append(TestCase(\n                name=name,\n   \
    \             params=params,\n                data={'data': data, 'distinct':\
    \ params.get('distinct', False)}\n            ))\n        \n        return test_cases\n\
    \    \n    def get_implementations(self) -> Dict[str, Callable]:\n        \"\"\
    \"Return implementations to benchmark\"\"\"\n        return {\n            'irank':\
    \ lambda data, distinct=False: irank(data.copy(), distinct=distinct),\n      \
    \      'irank_multi': lambda data, distinct=False: irank_multi(data.copy(), distinct=distinct)\n\
    \        }\n    \n    def measure_time(self, func: Callable, test_data: Dict)\
    \ -> Tuple[Any, float]:\n        \"\"\"Override to handle dict test data\"\"\"\
    \n        import time\n        \n        # Warmup\n        for _ in range(self.config.warmup):\n\
    \            func(**test_data)\n        \n        # Actual measurement\n     \
    \   start = time.perf_counter()\n        for _ in range(self.config.iterations):\n\
    \            result = func(**test_data)\n        elapsed_ms = (time.perf_counter()\
    \ - start) * 1000 / self.config.iterations\n        \n        return result, elapsed_ms\n\
    \ndef run_ranking_benchmark():\n    \"\"\"Run a comprehensive ranking algorithm\
    \ benchmark\"\"\"\n    \n    # Configure benchmark\n    config = BenchmarkConfig(\n\
    \        name=\"ranking_algorithms\",\n        iterations=10,\n        warmup=2,\n\
    \        save_results=True,\n        plot_results=False,  # Set to True if matplotlib\
    \ is installed\n        output_dir=\"./benchmark_results/ranking\"\n    )\n  \
    \  \n    # Create benchmark instance\n    benchmark = RankingBenchmark(config)\n\
    \    \n    # Define parameter grid\n    param_grid = {\n        'size': [100,\
    \ 1000, 10000, 50000],\n        'distribution': ['random', 'sorted', 'reverse',\
    \ 'duplicates', 'almost_sorted', 'plateau'],\n        'distinct': [True, False]\n\
    \    }\n    \n    # Run benchmark\n    benchmark.run(param_grid)\n    \n    #\
    \ Print summary statistics\n    print_summary(benchmark.results)\n\ndef print_summary(results):\n\
    \    \"\"\"Print summary statistics from benchmark results\"\"\"\n    from collections\
    \ import defaultdict\n    import statistics\n    \n    # Group results by implementation\n\
    \    impl_times = defaultdict(list)\n    \n    for result in results:\n      \
    \  if result.time_ms != float('inf'):\n            impl_times[result.implementation].append(result.time_ms)\n\
    \    \n    print(\"\\n\" + \"=\"*60)\n    print(\"SUMMARY STATISTICS\")\n    print(\"\
    =\"*60)\n    \n    print(f\"\\n{'Implementation':<20} {'Mean (ms)':<12} {'Std\
    \ Dev':<12} {'Min':<12} {'Max':<12} {'Samples':<10}\")\n    print(\"-\"*80)\n\
    \    \n    for impl, times in impl_times.items():\n        if times:\n       \
    \     mean_time = statistics.mean(times)\n            std_time = statistics.stdev(times)\
    \ if len(times) > 1 else 0\n            min_time = min(times)\n            max_time\
    \ = max(times)\n            \n            print(f\"{impl:<20} {mean_time:<12.3f}\
    \ {std_time:<12.3f} {min_time:<12.3f} {max_time:<12.3f} {len(times):<10}\")\n\
    \    \n    # Calculate speedup ratios\n    if len(impl_times) == 2:\n        impls\
    \ = list(impl_times.keys())\n        impl1_mean = statistics.mean(impl_times[impls[0]])\n\
    \        impl2_mean = statistics.mean(impl_times[impls[1]])\n        speedup =\
    \ impl1_mean / impl2_mean\n        \n        faster = impls[1] if speedup > 1\
    \ else impls[0]\n        ratio = max(speedup, 1/speedup)\n        \n        print(f\"\
    \\n{faster} is {ratio:.2f}x faster on average\")\n\nif __name__ == \"__main__\"\
    :\n    run_ranking_benchmark()"
  dependsOn:
  - cp_library/perf/benchmark.py
  - cp_library/alg/iter/rank/irank_fn.py
  - cp_library/alg/iter/rank/irank_multi_fn.py
  - cp_library/bit/pack/packer_cls.py
  - cp_library/alg/dp/max2_fn.py
  - cp_library/bit/pack/packer3_cls.py
  isVerificationFile: false
  path: cp_library/perf/examples/rank_benchmark.py
  requiredBy: []
  timestamp: '2025-07-10 02:39:49+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/perf/examples/rank_benchmark.py
layout: document
redirect_from:
- /library/cp_library/perf/examples/rank_benchmark.py
- /library/cp_library/perf/examples/rank_benchmark.py.html
title: cp_library/perf/examples/rank_benchmark.py
---
