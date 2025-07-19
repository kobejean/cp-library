---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/heap/fast_heapq.py
    title: cp_library/ds/heap/fast_heapq.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/list/list_find_fn.py
    title: cp_library/ds/list/list_find_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/view/csr_cls.py
    title: cp_library/ds/view/csr_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/view/view_cls.py
    title: cp_library/ds/view/view_cls.py
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
  bundledCode: "#!/usr/bin/env python3\n\"\"\"\nBenchmark comparing heap operations\
    \ on CSR sparse rows vs list of lists/heaps.\nTests heapify, heappop, heapreplace,\
    \ heappush, heappushpop operations.\n\"\"\"\n\nimport random\nimport sys\nimport\
    \ os\nsys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))\n\
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
    \              \n'''\nfrom typing import Generic\nfrom typing import TypeVar\n\
    _S = TypeVar('S')\n_T = TypeVar('T')\n_U = TypeVar('U')\n_T1 = TypeVar('T1')\n\
    _T2 = TypeVar('T2')\n_T3 = TypeVar('T3')\n_T4 = TypeVar('T4')\n_T5 = TypeVar('T5')\n\
    _T6 = TypeVar('T6')\n\n\n\n\n\ndef list_find(lst: list, value, start = 0, stop\
    \ = sys.maxsize):\n    try:\n        return lst.index(value, start, stop)\n  \
    \  except:\n        return -1\n\nclass view(Generic[_T]):\n    __slots__ = 'A',\
    \ 'l', 'r'\n    def __init__(V, A: list[_T], l: int, r: int): V.A, V.l, V.r =\
    \ A, l, r\n    def __len__(V): return V.r - V.l\n    def __getitem__(V, i: int):\
    \ \n        if 0 <= i < V.r - V.l: return V.A[V.l+i]\n        else: raise IndexError\n\
    \    def __setitem__(V, i: int, v: _T): V.A[V.l+i] = v\n    def __contains__(V,\
    \ v: _T): return list_find(V.A, v, V.l, V.r) != -1\n    def set_range(V, l: int,\
    \ r: int): V.l, V.r = l, r\n    def index(V, v: _T): return V.A.index(v, V.l,\
    \ V.r) - V.l\n    def reverse(V):\n        l, r = V.l, V.r-1\n        while l\
    \ < r: V.A[l], V.A[r] = V.A[r], V.A[l]; l += 1; r -= 1\n    def sort(V, /, *args,\
    \ **kwargs):\n        A = V.A[V.l:V.r]; A.sort(*args, **kwargs)\n        for i,a\
    \ in enumerate(A,V.l): V.A[i] = a\n    def pop(V): V.r -= 1; return V.A[V.r]\n\
    \    def append(V, v: _T): V.A[V.r] = v; V.r += 1\n    def popleft(V): V.l +=\
    \ 1; return V.A[V.l-1]\n    def appendleft(V, v: _T): V.l -= 1; V.A[V.l] = v;\
    \ \n    def validate(V): return 0 <= V.l <= V.r <= len(V.A)\n\nclass CSR(Generic[_T]):\n\
    \    __slots__ = 'A', 'O'\n    def __init__(csr, A: list[_T], O: list[int]): csr.A,\
    \ csr.O = A, O\n    def __len__(csr): return len(csr.O)-1\n    def __getitem__(csr,\
    \ i: int): return view(csr.A, csr.O[i], csr.O[i+1])\n    def __call__(csr, i:\
    \ int, j: int): return csr.A[csr.O[i]+j]\n    def set(csr, i: int, j: int, v:\
    \ _T): csr.A[csr.O[i]+j] = v\n    @classmethod\n    def bucketize(cls, N: int,\
    \ K: list[int], V: list[_T]):\n        A: list[_T] = [0]*len(K); O = [0]*(N+1)\n\
    \        for k in K: O[k] += 1\n        for i in range(N): O[i+1] += O[i]\n  \
    \      for e in range(len(K)): k = K[~e]; O[k] -= 1; A[O[k]] = V[~e]\n       \
    \ return cls(A, O)\n\n\ndef heappush(heap: list, item):\n    heap.append(item)\n\
    \    heapsiftdown(heap, 0, len(heap)-1)\n\ndef heappop(heap: list):\n    item\
    \ = heap.pop()\n    if heap: item, heap[0] = heap[0], item; heapsiftup(heap, 0)\n\
    \    return item\n\ndef heapreplace(heap: list, item):\n    item, heap[0] = heap[0],\
    \ item; heapsiftup(heap, 0)\n    return item\n\ndef heappushpop(heap: list, item):\n\
    \    if heap and heap[0] < item: item, heap[0] = heap[0], item; heapsiftup(heap,\
    \ 0)\n    return item\n\ndef heapify(x: list):\n    for i in reversed(range(len(x)//2)):\
    \ heapsiftup(x, i)\n\ndef heapsiftdown(heap: list, root: int, pos: int):\n   \
    \ item = heap[pos]\n    while root < pos and item < heap[p := (pos-1)>>1]: heap[pos],\
    \ pos = heap[p], p\n    heap[pos] = item\n\ndef heapsiftup(heap: list, pos: int):\n\
    \    n, item, c = len(heap)-1, heap[pos], pos<<1|1\n    while c < n and heap[c\
    \ := c+(heap[c+1]<heap[c])] < item: heap[pos], pos, c = heap[c], c, c<<1|1\n \
    \   if c == n and heap[c] < item: heap[pos], pos = heap[c], c\n    heap[pos] =\
    \ item\n\ndef heappop_max(heap: list):\n    item = heap.pop()\n    if heap: item,\
    \ heap[0] = heap[0], item; heapsiftup_max(heap, 0)\n    return item\n\ndef heapreplace_max(heap:\
    \ list, item):\n    item, heap[0] = heap[0], item; heapsiftup_max(heap, 0)\n \
    \   return item\n\ndef heapify_max(x: list):\n    for i in reversed(range(len(x)//2)):\
    \ heapsiftup_max(x, i)\n\ndef heappush_max(heap: list, item):\n    heap.append(item);\
    \ heapsiftdown_max(heap, 0, len(heap)-1)\n\ndef heapreplace_max(heap: list, item):\n\
    \    item, heap[0] = heap[0], item; heapsiftup_max(heap, 0)\n    return item\n\
    \ndef heappushpop_max(heap: list, item):\n    if heap and heap[0] > item: item,\
    \ heap[0] = heap[0], item; heapsiftup_max(heap, 0)\n    return item\n\ndef heapsiftdown_max(heap:\
    \ list, root: int, pos: int):\n    item = heap[pos]\n    while root < pos and\
    \ heap[p := (pos-1)>>1] < item: heap[pos], pos = heap[p], p\n    heap[pos] = item\n\
    \ndef heapsiftup_max(heap: list, pos: int):\n    n, item, c = len(heap)-1, heap[pos],\
    \ pos<<1|1\n    while c < n and item < heap[c := c+(heap[c]<heap[c+1])]: heap[pos],\
    \ pos, c = heap[c], c, c<<1|1\n    if c == n and item < heap[c]: heap[pos], pos\
    \ = heap[c], c\n    heap[pos] = item\n\n# Configure benchmark\nconfig = BenchmarkConfig(\n\
    \    name=\"heap_csr\",\n    sizes=[10000000, 1000000, 100000, 10000, 1000, 100,\
    \ 10],  # Reverse order to warm up JIT\n    operations=['initialization', 'initialization_bucketize',\
    \ 'heapify', 'heappop', 'heapreplace', 'heappush', 'heappushpop'],\n    iterations=10,\n\
    \    warmup=3,\n    output_dir=\"./output/benchmark_results/heap_csr\"\n)\n\n\
    # Create benchmark instance\nbenchmark = Benchmark(config)\n\n# Data generator\
    \ for initialization\n@benchmark.data_generator(\"initialization\")\ndef generate_initialization_data(size:\
    \ int, operation: str):\n    \"\"\"Generate raw data for initialization benchmark\"\
    \"\"\n    # Generate multiple sparse rows (each row is a heap)\n    num_rows =\
    \ max(10, size // 100)  # 10-100 rows depending on size\n    total_elements =\
    \ size\n    \n    # Generate raw row data\n    raw_rows = []\n    elements_per_row\
    \ = total_elements // num_rows\n    remaining = total_elements % num_rows\n  \
    \  \n    for i in range(num_rows):\n        # Variable row sizes (some rows get\
    \ extra elements)\n        row_size = elements_per_row + (1 if i < remaining else\
    \ 0)\n        row_size = max(1, row_size)  # Ensure at least 1 element per row\n\
    \        \n        # Generate random heap data for this row\n        row_data\
    \ = [random.randint(1, 1000000) for _ in range(row_size)]\n        raw_rows.append(row_data)\n\
    \    \n    return {\n        'raw_rows': raw_rows,\n        'num_rows': num_rows,\n\
    \        'size': size,\n        'operation': operation\n    }\n\n# Data generator\
    \ for bucketize initialization\n@benchmark.data_generator(\"initialization_bucketize\"\
    )\ndef generate_bucketize_data(size: int, operation: str):\n    \"\"\"Generate\
    \ (key, value) pairs for bucketize initialization benchmark\"\"\"\n    # Generate\
    \ multiple sparse rows (each row is a heap)\n    num_rows = max(10, size // 100)\
    \  # 10-100 rows depending on size\n    total_elements = size\n    \n    # Generate\
    \ (key, value) pairs\n    keys = []\n    values = []\n    \n    elements_per_row\
    \ = total_elements // num_rows\n    remaining = total_elements % num_rows\n  \
    \  \n    for i in range(num_rows):\n        # Variable row sizes (some rows get\
    \ extra elements)\n        row_size = elements_per_row + (1 if i < remaining else\
    \ 0)\n        row_size = max(1, row_size)  # Ensure at least 1 element per row\n\
    \        \n        # Generate random heap data for this row\n        for _ in\
    \ range(row_size):\n            keys.append(i)  # Row index as key\n         \
    \   values.append(random.randint(1, 1000000))  # Random value\n    \n    # Shuffle\
    \ to simulate unsorted input\n    combined = list(zip(keys, values))\n    random.shuffle(combined)\n\
    \    keys, values = zip(*combined)\n    keys, values = list(keys), list(values)\n\
    \    \n    # Create equivalent raw rows for list_of_lists comparison\n    raw_rows\
    \ = [[] for _ in range(num_rows)]\n    for key, value in zip(keys, values):\n\
    \        raw_rows[key].append(value)\n    \n    return {\n        'keys': keys,\n\
    \        'values': values,\n        'raw_rows': raw_rows,\n        'num_rows':\
    \ num_rows,\n        'size': size,\n        'operation': operation\n    }\n\n\
    # Data generator for other operations\n@benchmark.data_generator(\"default\")\n\
    def generate_csr_heap_data(size: int, operation: str):\n    \"\"\"Generate test\
    \ data for CSR heap operations\"\"\"\n    # Generate multiple sparse rows (each\
    \ row is a heap)\n    num_rows = max(10, size // 100)  # 10-100 rows depending\
    \ on size\n    total_elements = size\n    \n    # Create sparse row data\n   \
    \ A = []  # All elements concatenated\n    O = [0]  # Offsets for each row\n \
    \   \n    elements_per_row = total_elements // num_rows\n    remaining = total_elements\
    \ % num_rows\n    \n    for i in range(num_rows):\n        # Variable row sizes\
    \ (some rows get extra elements)\n        row_size = elements_per_row + (1 if\
    \ i < remaining else 0)\n        row_size = max(1, row_size)  # Ensure at least\
    \ 1 element per row\n        \n        # Generate random heap data for this row\n\
    \        row_data = [random.randint(1, 1000000) for _ in range(row_size)]\n  \
    \      A.extend(row_data)\n        O.append(len(A))\n    \n    # Create list of\
    \ lists equivalent\n    list_of_lists = []\n    for i in range(num_rows):\n  \
    \      start, end = O[i], O[i + 1]\n        list_of_lists.append(A[start:end].copy())\n\
    \    \n    return {\n        'A': A,\n        'O': O,\n        'list_of_lists':\
    \ list_of_lists,\n        'num_rows': num_rows,\n        'new_value': random.randint(1,\
    \ 1000000),\n        'target_row': random.randint(0, num_rows - 1),\n        'size':\
    \ size,\n        'operation': operation\n    }\n\n# Setup functions for operations\
    \ that modify data\n@benchmark.setup(\"csr\", [\"heappop\", \"heapreplace\", \"\
    heappush\", \"heappushpop\"])\ndef setup_csr_heap(data):\n    \"\"\"Setup function\
    \ that copies data and heapifies CSR rows\"\"\"\n    new_data = data.copy()\n\
    \    new_data['A'] = data['A'].copy()\n    new_data['O'] = data['O'].copy()\n\
    \    \n    # Create CSR and pre-heapify all rows\n    csr = CSR(new_data['A'],\
    \ new_data['O'])\n    for row_view in csr:\n        heapify(row_view)\n    \n\
    \    new_data['csr'] = csr\n    return new_data\n\n@benchmark.setup(\"list_of_lists\"\
    , [\"heappop\", \"heapreplace\", \"heappush\", \"heappushpop\"])\ndef setup_list_of_lists_heap(data):\n\
    \    \"\"\"Setup function that copies data and heapifies list of lists\"\"\"\n\
    \    new_data = data.copy()\n    # Deep copy list of lists\n    new_data['list_of_lists']\
    \ = [row.copy() for row in data['list_of_lists']]\n    \n    # Pre-heapify all\
    \ lists\n    for row in new_data['list_of_lists']:\n        heapify(row)\n   \
    \ \n    return new_data\n\n# For heapify operation, we need setup without pre-heapifying\n\
    @benchmark.setup(\"csr\", [\"heapify\"])\ndef setup_csr_heapify(data):\n    \"\
    \"\"Setup function that only copies data for heapify operation\"\"\"\n    new_data\
    \ = data.copy()\n    new_data['A'] = data['A'].copy()\n    new_data['O'] = data['O'].copy()\n\
    \    new_data['csr'] = CSR(new_data['A'], new_data['O'])\n    return new_data\n\
    \n@benchmark.setup(\"list_of_lists\", [\"heapify\"])\ndef setup_list_of_lists_heapify(data):\n\
    \    \"\"\"Setup function that only copies data for heapify operation\"\"\"\n\
    \    new_data = data.copy()\n    new_data['list_of_lists'] = [row.copy() for row\
    \ in data['list_of_lists']]\n    return new_data\n\n# Initialization operation\n\
    @benchmark.implementation(\"csr\", \"initialization\")\ndef initialization_csr(data):\n\
    \    \"\"\"Initialize CSR from raw row data\"\"\"\n    raw_rows = data['raw_rows']\n\
    \    \n    # Create CSR structure\n    A = []  # All elements concatenated\n \
    \   O = [0]  # Offsets for each row\n    \n    for row_data in raw_rows:\n   \
    \     A.extend(row_data)\n        O.append(len(A))\n    \n    # Create CSR object\n\
    \    csr = CSR(A, O)\n    \n    # Return checksum to ensure it's not optimized\
    \ away\n    checksum = 0\n    for i in range(min(10, len(csr))):  # First 10 rows\n\
    \        row_view = csr[i]\n        for j in range(min(3, len(row_view))):  #\
    \ First 3 elements per row\n            checksum ^= row_view[j]\n    \n    return\
    \ checksum\n\n@benchmark.implementation(\"list_of_lists\", \"initialization\"\
    )\ndef initialization_list_of_lists(data):\n    \"\"\"Initialize list of lists\
    \ from raw row data\"\"\"\n    raw_rows = data['raw_rows']\n    \n    # Create\
    \ list of lists (deep copy)\n    list_of_lists = [row.copy() for row in raw_rows]\n\
    \    \n    # Return checksum to ensure it's not optimized away\n    checksum =\
    \ 0\n    for i in range(min(10, len(list_of_lists))):  # First 10 rows\n     \
    \   row = list_of_lists[i]\n        for j in range(min(3, len(row))):  # First\
    \ 3 elements per row\n            checksum ^= row[j]\n    \n    return checksum\n\
    \n# Bucketize initialization operation\n@benchmark.implementation(\"csr\", \"\
    initialization_bucketize\")\ndef initialization_bucketize_csr(data):\n    \"\"\
    \"Initialize CSR using bucketize from (key, value) pairs\"\"\"\n    keys = data['keys']\n\
    \    values = data['values']\n    num_rows = data['num_rows']\n    \n    # Create\
    \ CSR using bucketize\n    csr = CSR.bucketize(num_rows, keys, values)\n    \n\
    \    # Return checksum to ensure it's not optimized away\n    checksum = 0\n \
    \   for i in range(min(10, len(csr))):  # First 10 rows\n        row_view = csr[i]\n\
    \        for j in range(min(3, len(row_view))):  # First 3 elements per row\n\
    \            checksum ^= row_view[j]\n    \n    return checksum\n\n@benchmark.implementation(\"\
    list_of_lists\", \"initialization_bucketize\")\ndef initialization_bucketize_list_of_lists(data):\n\
    \    \"\"\"Initialize list of lists by grouping (key, value) pairs manually\"\"\
    \"\n    keys = data['keys']\n    values = data['values']\n    num_rows = data['num_rows']\n\
    \    \n    # Group by key manually (simulating what bucketize does)\n    list_of_lists\
    \ = [[] for _ in range(num_rows)]\n    for e, k in enumerate(keys):\n        list_of_lists[k].append(values[e])\n\
    \    \n    # Return checksum to ensure it's not optimized away\n    checksum =\
    \ 0\n    for i in range(min(10, len(list_of_lists))):  # First 10 rows\n     \
    \   row = list_of_lists[i]\n        for j in range(min(3, len(row))):  # First\
    \ 3 elements per row\n            checksum ^= row[j]\n    \n    return checksum\n\
    \n# Heapify operation\n@benchmark.implementation(\"csr\", \"heapify\")\ndef heapify_csr(data):\n\
    \    \"\"\"Heapify all CSR rows\"\"\"\n    csr = data['csr']\n    \n    checksum\
    \ = 0\n    for row_view in csr:\n        heapify(row_view)\n        # Add first\
    \ few elements to checksum\n        for j in range(min(3, len(row_view))):\n \
    \           checksum ^= row_view[j]\n    \n    return checksum\n\n@benchmark.implementation(\"\
    list_of_lists\", \"heapify\")\ndef heapify_list_of_lists(data):\n    \"\"\"Heapify\
    \ all lists in list of lists\"\"\"\n    list_of_lists = data['list_of_lists']\n\
    \    \n    checksum = 0\n    for row in list_of_lists:\n        heapify(row)\n\
    \        # Add first few elements to checksum\n        for j in range(min(3, len(row))):\n\
    \            checksum ^= row[j]\n    \n    return checksum\n\n# Heappop operation\
    \ (heaps are already heapified in setup)\n@benchmark.implementation(\"csr\", \"\
    heappop\")\ndef heappop_csr(data):\n    \"\"\"Pop from CSR heaps\"\"\"\n    csr\
    \ = data['csr']\n    \n    checksum = 0\n    # Pop from multiple rows\n    for\
    \ row_view in csr:\n        pop_count = min(3, len(row_view))  # Pop up to 3 elements\
    \ per row\n        for _ in range(pop_count):\n            if row_view:\n    \
    \            val = heappop(row_view)\n                checksum ^= val\n    \n\
    \    return checksum\n\n@benchmark.implementation(\"list_of_lists\", \"heappop\"\
    )\ndef heappop_list_of_lists(data):\n    \"\"\"Pop from list of lists heaps\"\"\
    \"\n    list_of_lists = data['list_of_lists']\n    \n    checksum = 0\n    # Pop\
    \ from multiple rows\n    for row in list_of_lists:\n        pop_count = min(3,\
    \ len(row))  # Pop up to 3 elements per row\n        for _ in range(pop_count):\n\
    \            if row:\n                val = heappop(row)\n                checksum\
    \ ^= val\n    \n    return checksum\n\n# Heapreplace operation (heaps are already\
    \ heapified in setup)\n@benchmark.implementation(\"csr\", \"heapreplace\")\ndef\
    \ heapreplace_csr(data):\n    \"\"\"Replace in CSR heaps\"\"\"\n    csr = data['csr']\n\
    \    new_value = data['new_value']\n    \n    checksum = 0\n    # Replace in multiple\
    \ rows\n    for row_view in csr:\n        if row_view:\n            replace_count\
    \ = min(2, len(row_view))  # Replace up to 2 elements per row\n            for\
    \ j in range(replace_count):\n                if row_view:\n                 \
    \   val = heapreplace(row_view, new_value + j)\n                    checksum ^=\
    \ val\n    \n    return checksum\n\n@benchmark.implementation(\"list_of_lists\"\
    , \"heapreplace\")\ndef heapreplace_list_of_lists(data):\n    \"\"\"Replace in\
    \ list of lists heaps\"\"\"\n    list_of_lists = data['list_of_lists']\n    new_value\
    \ = data['new_value']\n    \n    checksum = 0\n    # Replace in multiple rows\n\
    \    for row in list_of_lists:\n        if row:\n            replace_count = min(2,\
    \ len(row))  # Replace up to 2 elements per row\n            for j in range(replace_count):\n\
    \                if row:\n                    val = heapreplace(row, new_value\
    \ + j)\n                    checksum ^= val\n    \n    return checksum\n\n# Heappush\
    \ operation (heaps are already heapified in setup)\n@benchmark.implementation(\"\
    csr\", \"heappush\")\ndef heappush_csr(data):\n    \"\"\"Push to CSR heaps\"\"\
    \"\n    csr = data['csr']\n    new_value = data['new_value']\n    \n    checksum\
    \ = 0\n    # Push to multiple rows\n    for i in range(min(5, len(csr))):  # Push\
    \ to first 5 rows\n        row_view = csr[i]\n        # Check if there's space\
    \ to expand (view can grow within A bounds)\n        if row_view.r < len(csr.A):\n\
    \            push_count = min(2, len(csr.A) - row_view.r)  # Push up to 2 elements\
    \ per row\n            for j in range(push_count):\n                val = new_value\
    \ + i * 10 + j\n                heappush(row_view, val)\n                checksum\
    \ ^= val\n    \n    return checksum\n\n@benchmark.implementation(\"list_of_lists\"\
    , \"heappush\")\ndef heappush_list_of_lists(data):\n    \"\"\"Push to list of\
    \ lists heaps\"\"\"\n    list_of_lists = data['list_of_lists']\n    new_value\
    \ = data['new_value']\n    \n    checksum = 0\n    # Push to multiple rows\n \
    \   for i in range(min(5, len(list_of_lists))):  # Push to first 5 rows\n    \
    \    row = list_of_lists[i]\n        push_count = 2  # Push 2 elements per row\n\
    \        for j in range(push_count):\n            val = new_value + i * 10 + j\n\
    \            heappush(row, val)\n            checksum ^= val\n    \n    return\
    \ checksum\n\n# Heappushpop operation (heaps are already heapified in setup)\n\
    @benchmark.implementation(\"csr\", \"heappushpop\")\ndef heappushpop_csr(data):\n\
    \    \"\"\"Push and pop from CSR heaps\"\"\"\n    csr = data['csr']\n    new_value\
    \ = data['new_value']\n    \n    checksum = 0\n    # Pushpop from multiple rows\n\
    \    for i, row_view in enumerate(csr):\n        if row_view:\n            pushpop_count\
    \ = min(2, len(row_view))  # Pushpop up to 2 elements per row\n            for\
    \ j in range(pushpop_count):\n                val = new_value + i * 10 + j\n \
    \               popped = heappushpop(row_view, val)\n                checksum\
    \ ^= popped\n    \n    return checksum\n\n@benchmark.implementation(\"list_of_lists\"\
    , \"heappushpop\")\ndef heappushpop_list_of_lists(data):\n    \"\"\"Push and pop\
    \ from list of lists heaps\"\"\"\n    list_of_lists = data['list_of_lists']\n\
    \    new_value = data['new_value']\n    \n    checksum = 0\n    # Pushpop from\
    \ multiple rows\n    for i, row in enumerate(list_of_lists):\n        if row:\n\
    \            pushpop_count = min(2, len(row))  # Pushpop up to 2 elements per\
    \ row\n            for j in range(pushpop_count):\n                val = new_value\
    \ + i * 10 + j\n                popped = heappushpop(row, val)\n             \
    \   checksum ^= popped\n    \n    return checksum\n\nif __name__ == \"__main__\"\
    :\n    # Parse command line args and run appropriate mode\n    runner = benchmark.parse_args()\n\
    \    runner.run()\n"
  code: "#!/usr/bin/env python3\n\"\"\"\nBenchmark comparing heap operations on CSR\
    \ sparse rows vs list of lists/heaps.\nTests heapify, heappop, heapreplace, heappush,\
    \ heappushpop operations.\n\"\"\"\n\nimport random\nimport sys\nimport os\nsys.path.insert(0,\
    \ os.path.dirname(os.path.dirname(os.path.abspath(__file__))))\n\nfrom cp_library.perf.benchmark\
    \ import Benchmark, BenchmarkConfig\nfrom cp_library.ds.view.csr_cls import CSR\n\
    from cp_library.ds.heap.fast_heapq import heapify, heappop, heapreplace, heappush,\
    \ heappushpop\n\n# Configure benchmark\nconfig = BenchmarkConfig(\n    name=\"\
    heap_csr\",\n    sizes=[10000000, 1000000, 100000, 10000, 1000, 100, 10],  # Reverse\
    \ order to warm up JIT\n    operations=['initialization', 'initialization_bucketize',\
    \ 'heapify', 'heappop', 'heapreplace', 'heappush', 'heappushpop'],\n    iterations=10,\n\
    \    warmup=3,\n    output_dir=\"./output/benchmark_results/heap_csr\"\n)\n\n\
    # Create benchmark instance\nbenchmark = Benchmark(config)\n\n# Data generator\
    \ for initialization\n@benchmark.data_generator(\"initialization\")\ndef generate_initialization_data(size:\
    \ int, operation: str):\n    \"\"\"Generate raw data for initialization benchmark\"\
    \"\"\n    # Generate multiple sparse rows (each row is a heap)\n    num_rows =\
    \ max(10, size // 100)  # 10-100 rows depending on size\n    total_elements =\
    \ size\n    \n    # Generate raw row data\n    raw_rows = []\n    elements_per_row\
    \ = total_elements // num_rows\n    remaining = total_elements % num_rows\n  \
    \  \n    for i in range(num_rows):\n        # Variable row sizes (some rows get\
    \ extra elements)\n        row_size = elements_per_row + (1 if i < remaining else\
    \ 0)\n        row_size = max(1, row_size)  # Ensure at least 1 element per row\n\
    \        \n        # Generate random heap data for this row\n        row_data\
    \ = [random.randint(1, 1000000) for _ in range(row_size)]\n        raw_rows.append(row_data)\n\
    \    \n    return {\n        'raw_rows': raw_rows,\n        'num_rows': num_rows,\n\
    \        'size': size,\n        'operation': operation\n    }\n\n# Data generator\
    \ for bucketize initialization\n@benchmark.data_generator(\"initialization_bucketize\"\
    )\ndef generate_bucketize_data(size: int, operation: str):\n    \"\"\"Generate\
    \ (key, value) pairs for bucketize initialization benchmark\"\"\"\n    # Generate\
    \ multiple sparse rows (each row is a heap)\n    num_rows = max(10, size // 100)\
    \  # 10-100 rows depending on size\n    total_elements = size\n    \n    # Generate\
    \ (key, value) pairs\n    keys = []\n    values = []\n    \n    elements_per_row\
    \ = total_elements // num_rows\n    remaining = total_elements % num_rows\n  \
    \  \n    for i in range(num_rows):\n        # Variable row sizes (some rows get\
    \ extra elements)\n        row_size = elements_per_row + (1 if i < remaining else\
    \ 0)\n        row_size = max(1, row_size)  # Ensure at least 1 element per row\n\
    \        \n        # Generate random heap data for this row\n        for _ in\
    \ range(row_size):\n            keys.append(i)  # Row index as key\n         \
    \   values.append(random.randint(1, 1000000))  # Random value\n    \n    # Shuffle\
    \ to simulate unsorted input\n    combined = list(zip(keys, values))\n    random.shuffle(combined)\n\
    \    keys, values = zip(*combined)\n    keys, values = list(keys), list(values)\n\
    \    \n    # Create equivalent raw rows for list_of_lists comparison\n    raw_rows\
    \ = [[] for _ in range(num_rows)]\n    for key, value in zip(keys, values):\n\
    \        raw_rows[key].append(value)\n    \n    return {\n        'keys': keys,\n\
    \        'values': values,\n        'raw_rows': raw_rows,\n        'num_rows':\
    \ num_rows,\n        'size': size,\n        'operation': operation\n    }\n\n\
    # Data generator for other operations\n@benchmark.data_generator(\"default\")\n\
    def generate_csr_heap_data(size: int, operation: str):\n    \"\"\"Generate test\
    \ data for CSR heap operations\"\"\"\n    # Generate multiple sparse rows (each\
    \ row is a heap)\n    num_rows = max(10, size // 100)  # 10-100 rows depending\
    \ on size\n    total_elements = size\n    \n    # Create sparse row data\n   \
    \ A = []  # All elements concatenated\n    O = [0]  # Offsets for each row\n \
    \   \n    elements_per_row = total_elements // num_rows\n    remaining = total_elements\
    \ % num_rows\n    \n    for i in range(num_rows):\n        # Variable row sizes\
    \ (some rows get extra elements)\n        row_size = elements_per_row + (1 if\
    \ i < remaining else 0)\n        row_size = max(1, row_size)  # Ensure at least\
    \ 1 element per row\n        \n        # Generate random heap data for this row\n\
    \        row_data = [random.randint(1, 1000000) for _ in range(row_size)]\n  \
    \      A.extend(row_data)\n        O.append(len(A))\n    \n    # Create list of\
    \ lists equivalent\n    list_of_lists = []\n    for i in range(num_rows):\n  \
    \      start, end = O[i], O[i + 1]\n        list_of_lists.append(A[start:end].copy())\n\
    \    \n    return {\n        'A': A,\n        'O': O,\n        'list_of_lists':\
    \ list_of_lists,\n        'num_rows': num_rows,\n        'new_value': random.randint(1,\
    \ 1000000),\n        'target_row': random.randint(0, num_rows - 1),\n        'size':\
    \ size,\n        'operation': operation\n    }\n\n# Setup functions for operations\
    \ that modify data\n@benchmark.setup(\"csr\", [\"heappop\", \"heapreplace\", \"\
    heappush\", \"heappushpop\"])\ndef setup_csr_heap(data):\n    \"\"\"Setup function\
    \ that copies data and heapifies CSR rows\"\"\"\n    new_data = data.copy()\n\
    \    new_data['A'] = data['A'].copy()\n    new_data['O'] = data['O'].copy()\n\
    \    \n    # Create CSR and pre-heapify all rows\n    csr = CSR(new_data['A'],\
    \ new_data['O'])\n    for row_view in csr:\n        heapify(row_view)\n    \n\
    \    new_data['csr'] = csr\n    return new_data\n\n@benchmark.setup(\"list_of_lists\"\
    , [\"heappop\", \"heapreplace\", \"heappush\", \"heappushpop\"])\ndef setup_list_of_lists_heap(data):\n\
    \    \"\"\"Setup function that copies data and heapifies list of lists\"\"\"\n\
    \    new_data = data.copy()\n    # Deep copy list of lists\n    new_data['list_of_lists']\
    \ = [row.copy() for row in data['list_of_lists']]\n    \n    # Pre-heapify all\
    \ lists\n    for row in new_data['list_of_lists']:\n        heapify(row)\n   \
    \ \n    return new_data\n\n# For heapify operation, we need setup without pre-heapifying\n\
    @benchmark.setup(\"csr\", [\"heapify\"])\ndef setup_csr_heapify(data):\n    \"\
    \"\"Setup function that only copies data for heapify operation\"\"\"\n    new_data\
    \ = data.copy()\n    new_data['A'] = data['A'].copy()\n    new_data['O'] = data['O'].copy()\n\
    \    new_data['csr'] = CSR(new_data['A'], new_data['O'])\n    return new_data\n\
    \n@benchmark.setup(\"list_of_lists\", [\"heapify\"])\ndef setup_list_of_lists_heapify(data):\n\
    \    \"\"\"Setup function that only copies data for heapify operation\"\"\"\n\
    \    new_data = data.copy()\n    new_data['list_of_lists'] = [row.copy() for row\
    \ in data['list_of_lists']]\n    return new_data\n\n# Initialization operation\n\
    @benchmark.implementation(\"csr\", \"initialization\")\ndef initialization_csr(data):\n\
    \    \"\"\"Initialize CSR from raw row data\"\"\"\n    raw_rows = data['raw_rows']\n\
    \    \n    # Create CSR structure\n    A = []  # All elements concatenated\n \
    \   O = [0]  # Offsets for each row\n    \n    for row_data in raw_rows:\n   \
    \     A.extend(row_data)\n        O.append(len(A))\n    \n    # Create CSR object\n\
    \    csr = CSR(A, O)\n    \n    # Return checksum to ensure it's not optimized\
    \ away\n    checksum = 0\n    for i in range(min(10, len(csr))):  # First 10 rows\n\
    \        row_view = csr[i]\n        for j in range(min(3, len(row_view))):  #\
    \ First 3 elements per row\n            checksum ^= row_view[j]\n    \n    return\
    \ checksum\n\n@benchmark.implementation(\"list_of_lists\", \"initialization\"\
    )\ndef initialization_list_of_lists(data):\n    \"\"\"Initialize list of lists\
    \ from raw row data\"\"\"\n    raw_rows = data['raw_rows']\n    \n    # Create\
    \ list of lists (deep copy)\n    list_of_lists = [row.copy() for row in raw_rows]\n\
    \    \n    # Return checksum to ensure it's not optimized away\n    checksum =\
    \ 0\n    for i in range(min(10, len(list_of_lists))):  # First 10 rows\n     \
    \   row = list_of_lists[i]\n        for j in range(min(3, len(row))):  # First\
    \ 3 elements per row\n            checksum ^= row[j]\n    \n    return checksum\n\
    \n# Bucketize initialization operation\n@benchmark.implementation(\"csr\", \"\
    initialization_bucketize\")\ndef initialization_bucketize_csr(data):\n    \"\"\
    \"Initialize CSR using bucketize from (key, value) pairs\"\"\"\n    keys = data['keys']\n\
    \    values = data['values']\n    num_rows = data['num_rows']\n    \n    # Create\
    \ CSR using bucketize\n    csr = CSR.bucketize(num_rows, keys, values)\n    \n\
    \    # Return checksum to ensure it's not optimized away\n    checksum = 0\n \
    \   for i in range(min(10, len(csr))):  # First 10 rows\n        row_view = csr[i]\n\
    \        for j in range(min(3, len(row_view))):  # First 3 elements per row\n\
    \            checksum ^= row_view[j]\n    \n    return checksum\n\n@benchmark.implementation(\"\
    list_of_lists\", \"initialization_bucketize\")\ndef initialization_bucketize_list_of_lists(data):\n\
    \    \"\"\"Initialize list of lists by grouping (key, value) pairs manually\"\"\
    \"\n    keys = data['keys']\n    values = data['values']\n    num_rows = data['num_rows']\n\
    \    \n    # Group by key manually (simulating what bucketize does)\n    list_of_lists\
    \ = [[] for _ in range(num_rows)]\n    for e, k in enumerate(keys):\n        list_of_lists[k].append(values[e])\n\
    \    \n    # Return checksum to ensure it's not optimized away\n    checksum =\
    \ 0\n    for i in range(min(10, len(list_of_lists))):  # First 10 rows\n     \
    \   row = list_of_lists[i]\n        for j in range(min(3, len(row))):  # First\
    \ 3 elements per row\n            checksum ^= row[j]\n    \n    return checksum\n\
    \n# Heapify operation\n@benchmark.implementation(\"csr\", \"heapify\")\ndef heapify_csr(data):\n\
    \    \"\"\"Heapify all CSR rows\"\"\"\n    csr = data['csr']\n    \n    checksum\
    \ = 0\n    for row_view in csr:\n        heapify(row_view)\n        # Add first\
    \ few elements to checksum\n        for j in range(min(3, len(row_view))):\n \
    \           checksum ^= row_view[j]\n    \n    return checksum\n\n@benchmark.implementation(\"\
    list_of_lists\", \"heapify\")\ndef heapify_list_of_lists(data):\n    \"\"\"Heapify\
    \ all lists in list of lists\"\"\"\n    list_of_lists = data['list_of_lists']\n\
    \    \n    checksum = 0\n    for row in list_of_lists:\n        heapify(row)\n\
    \        # Add first few elements to checksum\n        for j in range(min(3, len(row))):\n\
    \            checksum ^= row[j]\n    \n    return checksum\n\n# Heappop operation\
    \ (heaps are already heapified in setup)\n@benchmark.implementation(\"csr\", \"\
    heappop\")\ndef heappop_csr(data):\n    \"\"\"Pop from CSR heaps\"\"\"\n    csr\
    \ = data['csr']\n    \n    checksum = 0\n    # Pop from multiple rows\n    for\
    \ row_view in csr:\n        pop_count = min(3, len(row_view))  # Pop up to 3 elements\
    \ per row\n        for _ in range(pop_count):\n            if row_view:\n    \
    \            val = heappop(row_view)\n                checksum ^= val\n    \n\
    \    return checksum\n\n@benchmark.implementation(\"list_of_lists\", \"heappop\"\
    )\ndef heappop_list_of_lists(data):\n    \"\"\"Pop from list of lists heaps\"\"\
    \"\n    list_of_lists = data['list_of_lists']\n    \n    checksum = 0\n    # Pop\
    \ from multiple rows\n    for row in list_of_lists:\n        pop_count = min(3,\
    \ len(row))  # Pop up to 3 elements per row\n        for _ in range(pop_count):\n\
    \            if row:\n                val = heappop(row)\n                checksum\
    \ ^= val\n    \n    return checksum\n\n# Heapreplace operation (heaps are already\
    \ heapified in setup)\n@benchmark.implementation(\"csr\", \"heapreplace\")\ndef\
    \ heapreplace_csr(data):\n    \"\"\"Replace in CSR heaps\"\"\"\n    csr = data['csr']\n\
    \    new_value = data['new_value']\n    \n    checksum = 0\n    # Replace in multiple\
    \ rows\n    for row_view in csr:\n        if row_view:\n            replace_count\
    \ = min(2, len(row_view))  # Replace up to 2 elements per row\n            for\
    \ j in range(replace_count):\n                if row_view:\n                 \
    \   val = heapreplace(row_view, new_value + j)\n                    checksum ^=\
    \ val\n    \n    return checksum\n\n@benchmark.implementation(\"list_of_lists\"\
    , \"heapreplace\")\ndef heapreplace_list_of_lists(data):\n    \"\"\"Replace in\
    \ list of lists heaps\"\"\"\n    list_of_lists = data['list_of_lists']\n    new_value\
    \ = data['new_value']\n    \n    checksum = 0\n    # Replace in multiple rows\n\
    \    for row in list_of_lists:\n        if row:\n            replace_count = min(2,\
    \ len(row))  # Replace up to 2 elements per row\n            for j in range(replace_count):\n\
    \                if row:\n                    val = heapreplace(row, new_value\
    \ + j)\n                    checksum ^= val\n    \n    return checksum\n\n# Heappush\
    \ operation (heaps are already heapified in setup)\n@benchmark.implementation(\"\
    csr\", \"heappush\")\ndef heappush_csr(data):\n    \"\"\"Push to CSR heaps\"\"\
    \"\n    csr = data['csr']\n    new_value = data['new_value']\n    \n    checksum\
    \ = 0\n    # Push to multiple rows\n    for i in range(min(5, len(csr))):  # Push\
    \ to first 5 rows\n        row_view = csr[i]\n        # Check if there's space\
    \ to expand (view can grow within A bounds)\n        if row_view.r < len(csr.A):\n\
    \            push_count = min(2, len(csr.A) - row_view.r)  # Push up to 2 elements\
    \ per row\n            for j in range(push_count):\n                val = new_value\
    \ + i * 10 + j\n                heappush(row_view, val)\n                checksum\
    \ ^= val\n    \n    return checksum\n\n@benchmark.implementation(\"list_of_lists\"\
    , \"heappush\")\ndef heappush_list_of_lists(data):\n    \"\"\"Push to list of\
    \ lists heaps\"\"\"\n    list_of_lists = data['list_of_lists']\n    new_value\
    \ = data['new_value']\n    \n    checksum = 0\n    # Push to multiple rows\n \
    \   for i in range(min(5, len(list_of_lists))):  # Push to first 5 rows\n    \
    \    row = list_of_lists[i]\n        push_count = 2  # Push 2 elements per row\n\
    \        for j in range(push_count):\n            val = new_value + i * 10 + j\n\
    \            heappush(row, val)\n            checksum ^= val\n    \n    return\
    \ checksum\n\n# Heappushpop operation (heaps are already heapified in setup)\n\
    @benchmark.implementation(\"csr\", \"heappushpop\")\ndef heappushpop_csr(data):\n\
    \    \"\"\"Push and pop from CSR heaps\"\"\"\n    csr = data['csr']\n    new_value\
    \ = data['new_value']\n    \n    checksum = 0\n    # Pushpop from multiple rows\n\
    \    for i, row_view in enumerate(csr):\n        if row_view:\n            pushpop_count\
    \ = min(2, len(row_view))  # Pushpop up to 2 elements per row\n            for\
    \ j in range(pushpop_count):\n                val = new_value + i * 10 + j\n \
    \               popped = heappushpop(row_view, val)\n                checksum\
    \ ^= popped\n    \n    return checksum\n\n@benchmark.implementation(\"list_of_lists\"\
    , \"heappushpop\")\ndef heappushpop_list_of_lists(data):\n    \"\"\"Push and pop\
    \ from list of lists heaps\"\"\"\n    list_of_lists = data['list_of_lists']\n\
    \    new_value = data['new_value']\n    \n    checksum = 0\n    # Pushpop from\
    \ multiple rows\n    for i, row in enumerate(list_of_lists):\n        if row:\n\
    \            pushpop_count = min(2, len(row))  # Pushpop up to 2 elements per\
    \ row\n            for j in range(pushpop_count):\n                val = new_value\
    \ + i * 10 + j\n                popped = heappushpop(row, val)\n             \
    \   checksum ^= popped\n    \n    return checksum\n\nif __name__ == \"__main__\"\
    :\n    # Parse command line args and run appropriate mode\n    runner = benchmark.parse_args()\n\
    \    runner.run()"
  dependsOn:
  - cp_library/perf/benchmark.py
  - cp_library/ds/view/csr_cls.py
  - cp_library/ds/heap/fast_heapq.py
  - cp_library/ds/view/view_cls.py
  - cp_library/ds/list/list_find_fn.py
  isVerificationFile: false
  path: perf/heap_csr.py
  requiredBy: []
  timestamp: '2025-07-20 06:26:01+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: perf/heap_csr.py
layout: document
redirect_from:
- /library/perf/heap_csr.py
- /library/perf/heap_csr.py.html
title: perf/heap_csr.py
---
