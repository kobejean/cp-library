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
    \ on list slices vs view objects vs direct indexing.\nTests heapify, heappop,\
    \ heapreplace, heappush, heappushpop operations.\n\"\"\"\n\nimport random\nimport\
    \ sys\nimport os\nsys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))\n\
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
    _S = TypeVar('S')\n_T = TypeVar('T')\n_U = TypeVar('U')\n\n\n\ndef list_find(lst:\
    \ list, value, start = 0, stop = sys.maxsize):\n    try:\n        return lst.index(value,\
    \ start, stop)\n    except:\n        return -1\n\n\nclass view(Generic[_T]):\n\
    \    __slots__ = 'A', 'l', 'r'\n    def __init__(V, A: list[_T], l: int, r: int):\
    \ V.A, V.l, V.r = A, l, r\n    def __len__(V): return V.r - V.l\n    def __getitem__(V,\
    \ i: int): \n        if 0 <= i < V.r - V.l: return V.A[V.l+i]\n        else: raise\
    \ IndexError\n    def __setitem__(V, i: int, v: _T): V.A[V.l+i] = v\n    def __contains__(V,\
    \ v: _T): return list_find(V.A, v, V.l, V.r) != -1\n    def set_range(V, l: int,\
    \ r: int): V.l, V.r = l, r\n    def index(V, v: _T): return V.A.index(v, V.l,\
    \ V.r) - V.l\n    def reverse(V):\n        l, r = V.l, V.r-1\n        while l\
    \ < r: V.A[l], V.A[r] = V.A[r], V.A[l]; l += 1; r -= 1\n    def sort(V, /, *args,\
    \ **kwargs):\n        A = V.A[V.l:V.r]; A.sort(*args, **kwargs)\n        for i,a\
    \ in enumerate(A,V.l): V.A[i] = a\n    def pop(V): V.r -= 1; return V.A[V.r]\n\
    \    def append(V, v: _T): V.A[V.r] = v; V.r += 1\n    def popleft(V): V.l +=\
    \ 1; return V.A[V.l-1]\n    def appendleft(V, v: _T): V.l -= 1; V.A[V.l] = v;\
    \ \n    def validate(V): return 0 <= V.l <= V.r <= len(V.A)\n\n\ndef heappush(heap:\
    \ list, item):\n    heap.append(item)\n    heapsiftdown(heap, 0, len(heap)-1)\n\
    \ndef heappop(heap: list):\n    item = heap.pop()\n    if heap: item, heap[0]\
    \ = heap[0], item; heapsiftup(heap, 0)\n    return item\n\ndef heapreplace(heap:\
    \ list, item):\n    item, heap[0] = heap[0], item; heapsiftup(heap, 0)\n    return\
    \ item\n\ndef heappushpop(heap: list, item):\n    if heap and heap[0] < item:\
    \ item, heap[0] = heap[0], item; heapsiftup(heap, 0)\n    return item\n\ndef heapify(x:\
    \ list):\n    for i in reversed(range(len(x)//2)): heapsiftup(x, i)\n\ndef heapsiftdown(heap:\
    \ list, root: int, pos: int):\n    item = heap[pos]\n    while root < pos and\
    \ item < heap[p := (pos-1)>>1]: heap[pos], pos = heap[p], p\n    heap[pos] = item\n\
    \ndef heapsiftup(heap: list, pos: int):\n    n, item, c = len(heap)-1, heap[pos],\
    \ pos<<1|1\n    while c < n and heap[c := c+(heap[c+1]<heap[c])] < item: heap[pos],\
    \ pos, c = heap[c], c, c<<1|1\n    if c == n and heap[c] < item: heap[pos], pos\
    \ = heap[c], c\n    heap[pos] = item\n\ndef heappop_max(heap: list):\n    item\
    \ = heap.pop()\n    if heap: item, heap[0] = heap[0], item; heapsiftup_max(heap,\
    \ 0)\n    return item\n\ndef heapreplace_max(heap: list, item):\n    item, heap[0]\
    \ = heap[0], item; heapsiftup_max(heap, 0)\n    return item\n\ndef heapify_max(x:\
    \ list):\n    for i in reversed(range(len(x)//2)): heapsiftup_max(x, i)\n\ndef\
    \ heappush_max(heap: list, item):\n    heap.append(item); heapsiftdown_max(heap,\
    \ 0, len(heap)-1)\n\ndef heapreplace_max(heap: list, item):\n    item, heap[0]\
    \ = heap[0], item; heapsiftup_max(heap, 0)\n    return item\n\ndef heappushpop_max(heap:\
    \ list, item):\n    if heap and heap[0] > item: item, heap[0] = heap[0], item;\
    \ heapsiftup_max(heap, 0)\n    return item\n\ndef heapsiftdown_max(heap: list,\
    \ root: int, pos: int):\n    item = heap[pos]\n    while root < pos and heap[p\
    \ := (pos-1)>>1] < item: heap[pos], pos = heap[p], p\n    heap[pos] = item\n\n\
    def heapsiftup_max(heap: list, pos: int):\n    n, item, c = len(heap)-1, heap[pos],\
    \ pos<<1|1\n    while c < n and item < heap[c := c+(heap[c]<heap[c+1])]: heap[pos],\
    \ pos, c = heap[c], c, c<<1|1\n    if c == n and item < heap[c]: heap[pos], pos\
    \ = heap[c], c\n    heap[pos] = item\nimport heapq  # Standard library for comparison\n\
    \n# Configure benchmark\nconfig = BenchmarkConfig(\n    name=\"heap_view\",\n\
    \    sizes=[100000, 10000, 1000, 100, 50],  # Reverse order to warm up JIT\n \
    \   operations=['heapify', 'heappop', 'heapreplace', 'heappush', 'heappushpop'],\n\
    \    iterations=10,\n    warmup=3,\n    output_dir=\"./output/benchmark_results/heap_view\"\
    \n)\n\n# Create benchmark instance\nbenchmark = Benchmark(config)\n\n# Data generator\n\
    @benchmark.data_generator(\"default\")\ndef generate_heap_data(size: int, operation:\
    \ str):\n    \"\"\"Generate test data for heap operations\"\"\"\n    # Generate\
    \ random list for heap operations\n    data = [random.randint(1, 1000000) for\
    \ _ in range(size)]\n    \n    # Generate random slice boundaries (30-70% of list\
    \ for reasonable heap size)\n    slice_size = random.randint(size // 3, min(size\
    \ * 2 // 3, size - 1))\n    start = random.randint(0, size - slice_size)\n   \
    \ end = start + slice_size\n    \n    return {\n        'data': data,\n      \
    \  'start': start,\n        'end': end,\n        'slice_size': slice_size,\n \
    \       'new_value': random.randint(1, 1000000),\n        'replace_value': random.randint(1,\
    \ 1000000),\n        'size': size,\n        'operation': operation\n    }\n\n\
    # Setup functions for operations that modify data\n@benchmark.setup(\"slice\"\
    , [\"heappop\", \"heapreplace\", \"heappush\", \"heappushpop\"])\ndef setup_slice_heap(data):\n\
    \    \"\"\"Setup function that copies data and heapifies before heap operations\"\
    \"\"\n    new_data = data.copy()\n    new_data['data'] = data['data'].copy()\n\
    \    \n    # Pre-heapify the slice for operations that need it\n    lst = new_data['data']\n\
    \    start, end = new_data['start'], new_data['end']\n    slice_copy = lst[start:end]\n\
    \    heapify(slice_copy)\n    for i, val in enumerate(slice_copy):\n        lst[start\
    \ + i] = val\n    \n    return new_data\n\n@benchmark.setup(\"view\", [\"heappop\"\
    , \"heapreplace\", \"heappush\", \"heappushpop\"])\ndef setup_view_heap(data):\n\
    \    \"\"\"Setup function that copies data and heapifies before heap operations\"\
    \"\"\n    new_data = data.copy()\n    new_data['data'] = data['data'].copy()\n\
    \    \n    # Pre-heapify the view for operations that need it\n    lst = new_data['data']\n\
    \    start, end = new_data['start'], new_data['end']\n    heap_view = view(lst,\
    \ start, end)\n    heapify(heap_view)\n    \n    return new_data\n\n@benchmark.setup(\"\
    direct\", [\"heappop\", \"heapreplace\", \"heappush\", \"heappushpop\"])\ndef\
    \ setup_direct_heap(data):\n    \"\"\"Setup function that copies data and heapifies\
    \ before heap operations\"\"\"\n    new_data = data.copy()\n    new_data['data']\
    \ = data['data'].copy()\n    \n    # Pre-heapify the range for operations that\
    \ need it\n    lst = new_data['data']\n    start, end = new_data['start'], new_data['end']\n\
    \    temp_list = lst[start:end]\n    heapify(temp_list)\n    for i, val in enumerate(temp_list):\n\
    \        lst[start + i] = val\n    \n    return new_data\n\n@benchmark.setup(\"\
    stdlib\", [\"heappop\", \"heapreplace\", \"heappush\", \"heappushpop\"])\ndef\
    \ setup_stdlib_heap(data):\n    \"\"\"Setup function that copies data and heapifies\
    \ before heap operations\"\"\"\n    new_data = data.copy()\n    new_data['data']\
    \ = data['data'].copy()\n    \n    # Pre-heapify the slice for operations that\
    \ need it\n    lst = new_data['data']\n    start, end = new_data['start'], new_data['end']\n\
    \    slice_copy = lst[start:end]\n    heapq.heapify(slice_copy)\n    for i, val\
    \ in enumerate(slice_copy):\n        lst[start + i] = val\n    \n    return new_data\n\
    \n# For heapify operation, we need setup without pre-heapifying\n@benchmark.setup(\"\
    slice\", [\"heapify\"])\ndef setup_slice_heapify(data):\n    \"\"\"Setup function\
    \ that only copies data for heapify operation\"\"\"\n    new_data = data.copy()\n\
    \    new_data['data'] = data['data'].copy()\n    return new_data\n\n@benchmark.setup(\"\
    view\", [\"heapify\"])\ndef setup_view_heapify(data):\n    \"\"\"Setup function\
    \ that only copies data for heapify operation\"\"\"\n    new_data = data.copy()\n\
    \    new_data['data'] = data['data'].copy()\n    return new_data\n\n@benchmark.setup(\"\
    direct\", [\"heapify\"])\ndef setup_direct_heapify(data):\n    \"\"\"Setup function\
    \ that only copies data for heapify operation\"\"\"\n    new_data = data.copy()\n\
    \    new_data['data'] = data['data'].copy()\n    return new_data\n\n@benchmark.setup(\"\
    stdlib\", [\"heapify\"])\ndef setup_stdlib_heapify(data):\n    \"\"\"Setup function\
    \ that only copies data for heapify operation\"\"\"\n    new_data = data.copy()\n\
    \    new_data['data'] = data['data'].copy()\n    return new_data\n\n# Heapify\
    \ operation\n@benchmark.implementation(\"slice\", \"heapify\")\ndef heapify_slice(data):\n\
    \    \"\"\"Heapify a slice\"\"\"\n    lst = data['data']\n    start, end = data['start'],\
    \ data['end']\n    \n    # Create slice and heapify\n    slice_copy = lst[start:end]\n\
    \    heapify(slice_copy)\n    \n    # Copy back manually\n    for i, val in enumerate(slice_copy):\n\
    \        lst[start + i] = val\n    \n    # Return checksum\n    checksum = 0\n\
    \    for i in range(start, min(start + 10, end)):  # First 10 elements\n     \
    \   checksum ^= lst[i]\n    return checksum\n\n@benchmark.implementation(\"view\"\
    , \"heapify\")\ndef heapify_view(data):\n    \"\"\"Heapify through a view\"\"\"\
    \n    lst = data['data']\n    start, end = data['start'], data['end']\n    \n\
    \    # Create view and heapify\n    heap_view = view(lst, start, end)\n    heapify(heap_view)\n\
    \    \n    # Return checksum\n    checksum = 0\n    for i in range(start, min(start\
    \ + 10, end)):  # First 10 elements\n        checksum ^= lst[i]\n    return checksum\n\
    \n@benchmark.implementation(\"direct\", \"heapify\")\ndef heapify_direct(data):\n\
    \    \"\"\"Heapify using direct list access\"\"\"\n    lst = data['data']\n  \
    \  start, end = data['start'], data['end']\n    \n    # Heapify the range directly\
    \ in the list\n    temp_list = lst[start:end]\n    heapify(temp_list)\n    for\
    \ i, val in enumerate(temp_list):\n        lst[start + i] = val\n    \n    # Return\
    \ checksum\n    checksum = 0\n    for i in range(start, min(start + 10, end)):\
    \  # First 10 elements\n        checksum ^= lst[i]\n    return checksum\n\n@benchmark.implementation(\"\
    stdlib\", \"heapify\")\ndef heapify_stdlib(data):\n    \"\"\"Heapify using standard\
    \ library\"\"\"\n    lst = data['data']\n    start, end = data['start'], data['end']\n\
    \    \n    # Create slice and heapify with stdlib\n    slice_copy = lst[start:end]\n\
    \    heapq.heapify(slice_copy)\n    \n    # Copy back manually\n    for i, val\
    \ in enumerate(slice_copy):\n        lst[start + i] = val\n    \n    # Return\
    \ checksum\n    checksum = 0\n    for i in range(start, min(start + 10, end)):\
    \  # First 10 elements\n        checksum ^= lst[i]\n    return checksum\n\n# Heappop\
    \ operation (heap is already heapified in setup)\n@benchmark.implementation(\"\
    slice\", \"heappop\")\ndef heappop_slice(data):\n    \"\"\"Pop from heap slice\"\
    \"\"\n    lst = data['data']\n    start, end = data['start'], data['end']\n  \
    \  \n    # Create slice and pop (already heapified)\n    slice_copy = lst[start:end]\n\
    \    \n    checksum = 0\n    for _ in range(min(10, len(slice_copy))):  # Pop\
    \ up to 10 elements\n        if slice_copy:\n            val = heappop(slice_copy)\n\
    \            checksum ^= val\n    \n    # Copy back\n    for i, val in enumerate(slice_copy):\n\
    \        lst[start + i] = val\n    \n    return checksum\n\n@benchmark.implementation(\"\
    view\", \"heappop\")\ndef heappop_view(data):\n    \"\"\"Pop from heap view\"\"\
    \"\n    lst = data['data']\n    start, end = data['start'], data['end']\n    \n\
    \    # Create view and pop (already heapified)\n    heap_view = view(lst, start,\
    \ end)\n    \n    checksum = 0\n    for _ in range(min(10, len(heap_view))): \
    \ # Pop up to 10 elements\n        if len(heap_view) > 0:\n            val = heappop(heap_view)\n\
    \            checksum ^= val\n    \n    return checksum\n\n@benchmark.implementation(\"\
    direct\", \"heappop\")\ndef heappop_direct(data):\n    \"\"\"Pop from heap using\
    \ direct access\"\"\"\n    lst = data['data']\n    start, end = data['start'],\
    \ data['end']\n    \n    # Pop from range (already heapified)\n    temp_list =\
    \ lst[start:end]\n    \n    checksum = 0\n    for _ in range(min(10, len(temp_list))):\
    \  # Pop up to 10 elements\n        if temp_list:\n            val = heappop(temp_list)\n\
    \            checksum ^= val\n    \n    # Copy back\n    for i, val in enumerate(temp_list):\n\
    \        lst[start + i] = val\n    \n    return checksum\n\n@benchmark.implementation(\"\
    stdlib\", \"heappop\")\ndef heappop_stdlib(data):\n    \"\"\"Pop from heap using\
    \ standard library\"\"\"\n    lst = data['data']\n    start, end = data['start'],\
    \ data['end']\n    \n    # Create slice and pop with stdlib (already heapified)\n\
    \    slice_copy = lst[start:end]\n    \n    checksum = 0\n    for _ in range(min(10,\
    \ len(slice_copy))):  # Pop up to 10 elements\n        if slice_copy:\n      \
    \      val = heapq.heappop(slice_copy)\n            checksum ^= val\n    \n  \
    \  # Copy back\n    for i, val in enumerate(slice_copy):\n        lst[start +\
    \ i] = val\n    \n    return checksum\n\n# Heapreplace operation (heap is already\
    \ heapified in setup)\n@benchmark.implementation(\"slice\", \"heapreplace\")\n\
    def heapreplace_slice(data):\n    \"\"\"Replace in heap slice\"\"\"\n    lst =\
    \ data['data']\n    start, end = data['start'], data['end']\n    new_value = data['new_value']\n\
    \    \n    # Create slice and replace (already heapified)\n    slice_copy = lst[start:end]\n\
    \    if slice_copy:\n        checksum = 0\n        for _ in range(min(5, len(slice_copy))):\
    \  # Replace up to 5 elements\n            if slice_copy:\n                val\
    \ = heapreplace(slice_copy, new_value)\n                checksum ^= val\n    \
    \            new_value = (new_value + 1) & 0xFFFFFFFF\n        \n        # Copy\
    \ back\n        for i, val in enumerate(slice_copy):\n            lst[start +\
    \ i] = val\n        \n        return checksum\n    return 0\n\n@benchmark.implementation(\"\
    view\", \"heapreplace\")\ndef heapreplace_view(data):\n    \"\"\"Replace in heap\
    \ view\"\"\"\n    lst = data['data']\n    start, end = data['start'], data['end']\n\
    \    new_value = data['new_value']\n    \n    # Create view and replace (already\
    \ heapified)\n    heap_view = view(lst, start, end)\n    if len(heap_view) > 0:\n\
    \        checksum = 0\n        for _ in range(min(5, len(heap_view))):  # Replace\
    \ up to 5 elements\n            if len(heap_view) > 0:\n                val =\
    \ heapreplace(heap_view, new_value)\n                checksum ^= val\n       \
    \         new_value = (new_value + 1) & 0xFFFFFFFF\n        \n        return checksum\n\
    \    return 0\n\n@benchmark.implementation(\"direct\", \"heapreplace\")\ndef heapreplace_direct(data):\n\
    \    \"\"\"Replace in heap using direct access\"\"\"\n    lst = data['data']\n\
    \    start, end = data['start'], data['end']\n    new_value = data['new_value']\n\
    \    \n    # Replace from range (already heapified)\n    temp_list = lst[start:end]\n\
    \    if temp_list:\n        checksum = 0\n        for _ in range(min(5, len(temp_list))):\
    \  # Replace up to 5 elements\n            if temp_list:\n                val\
    \ = heapreplace(temp_list, new_value)\n                checksum ^= val\n     \
    \           new_value = (new_value + 1) & 0xFFFFFFFF\n        \n        # Copy\
    \ back\n        for i, val in enumerate(temp_list):\n            lst[start + i]\
    \ = val\n        \n        return checksum\n    return 0\n\n@benchmark.implementation(\"\
    stdlib\", \"heapreplace\")\ndef heapreplace_stdlib(data):\n    \"\"\"Replace in\
    \ heap using standard library\"\"\"\n    lst = data['data']\n    start, end =\
    \ data['start'], data['end']\n    new_value = data['new_value']\n    \n    # Create\
    \ slice and replace with stdlib (already heapified)\n    slice_copy = lst[start:end]\n\
    \    if slice_copy:\n        checksum = 0\n        for _ in range(min(5, len(slice_copy))):\
    \  # Replace up to 5 elements\n            if slice_copy:\n                val\
    \ = heapq.heapreplace(slice_copy, new_value)\n                checksum ^= val\n\
    \                new_value = (new_value + 1) & 0xFFFFFFFF\n        \n        #\
    \ Copy back\n        for i, val in enumerate(slice_copy):\n            lst[start\
    \ + i] = val\n        \n        return checksum\n    return 0\n\n# Heappush operation\
    \ (heap is already heapified in setup)\n@benchmark.implementation(\"slice\", \"\
    heappush\")\ndef heappush_slice(data):\n    \"\"\"Push to heap slice\"\"\"\n \
    \   lst = data['data']\n    start, end = data['start'], data['end']\n    new_value\
    \ = data['new_value']\n    \n    # Create slice and push (already heapified)\n\
    \    slice_copy = lst[start:end]\n    \n    checksum = 0\n    for i in range(5):\
    \  # Push 5 elements\n        val = (new_value + i) & 0xFFFFFFFF\n        heappush(slice_copy,\
    \ val)\n        checksum ^= val\n    \n    # Note: Can't copy back easily since\
    \ slice grew, just return checksum\n    return checksum\n\n@benchmark.implementation(\"\
    view\", \"heappush\")\ndef heappush_view(data):\n    \"\"\"Push to heap view\"\
    \"\"\n    lst = data['data']\n    start, end = data['start'], data['end']\n  \
    \  new_value = data['new_value']\n    \n    # Create view and push (already heapified)\n\
    \    heap_view = view(lst, start, end)\n    \n    checksum = 0\n    max_push =\
    \ min(5, len(lst) - end)  # Limited by available space\n    for i in range(max_push):\n\
    \        val = (new_value + i) & 0xFFFFFFFF\n        heappush(heap_view, val)\n\
    \        checksum ^= val\n    \n    return checksum\n\n@benchmark.implementation(\"\
    direct\", \"heappush\")\ndef heappush_direct(data):\n    \"\"\"Push to heap using\
    \ direct access\"\"\"\n    lst = data['data']\n    start, end = data['start'],\
    \ data['end']\n    new_value = data['new_value']\n    \n    # Push to range (already\
    \ heapified)\n    temp_list = lst[start:end]\n    \n    checksum = 0\n    for\
    \ i in range(5):  # Push 5 elements\n        val = (new_value + i) & 0xFFFFFFFF\n\
    \        heappush(temp_list, val)\n        checksum ^= val\n    \n    # Note:\
    \ Can't copy back easily since temp_list grew, just return checksum\n    return\
    \ checksum\n\n@benchmark.implementation(\"stdlib\", \"heappush\")\ndef heappush_stdlib(data):\n\
    \    \"\"\"Push to heap using standard library\"\"\"\n    lst = data['data']\n\
    \    start, end = data['start'], data['end']\n    new_value = data['new_value']\n\
    \    \n    # Create slice and push with stdlib (already heapified)\n    slice_copy\
    \ = lst[start:end]\n    \n    checksum = 0\n    for i in range(5):  # Push 5 elements\n\
    \        val = (new_value + i) & 0xFFFFFFFF\n        heapq.heappush(slice_copy,\
    \ val)\n        checksum ^= val\n    \n    # Note: Can't copy back easily since\
    \ slice grew, just return checksum\n    return checksum\n\n# Heappushpop operation\
    \ (heap is already heapified in setup)\n@benchmark.implementation(\"slice\", \"\
    heappushpop\")\ndef heappushpop_slice(data):\n    \"\"\"Push and pop from heap\
    \ slice\"\"\"\n    lst = data['data']\n    start, end = data['start'], data['end']\n\
    \    new_value = data['new_value']\n    \n    # Create slice and pushpop (already\
    \ heapified)\n    slice_copy = lst[start:end]\n    if slice_copy:\n        checksum\
    \ = 0\n        for i in range(min(5, len(slice_copy))):  # Pushpop up to 5 elements\n\
    \            val = (new_value + i) & 0xFFFFFFFF\n            popped = heappushpop(slice_copy,\
    \ val)\n            checksum ^= popped\n        \n        # Copy back\n      \
    \  for i, val in enumerate(slice_copy):\n            lst[start + i] = val\n  \
    \      \n        return checksum\n    return 0\n\n@benchmark.implementation(\"\
    view\", \"heappushpop\")\ndef heappushpop_view(data):\n    \"\"\"Push and pop\
    \ from heap view\"\"\"\n    lst = data['data']\n    start, end = data['start'],\
    \ data['end']\n    new_value = data['new_value']\n    \n    # Create view and\
    \ pushpop (already heapified)\n    heap_view = view(lst, start, end)\n    if len(heap_view)\
    \ > 0:\n        checksum = 0\n        for i in range(min(5, len(heap_view))):\
    \  # Pushpop up to 5 elements\n            val = (new_value + i) & 0xFFFFFFFF\n\
    \            popped = heappushpop(heap_view, val)\n            checksum ^= popped\n\
    \        \n        return checksum\n    return 0\n\n@benchmark.implementation(\"\
    direct\", \"heappushpop\")\ndef heappushpop_direct(data):\n    \"\"\"Push and\
    \ pop from heap using direct access\"\"\"\n    lst = data['data']\n    start,\
    \ end = data['start'], data['end']\n    new_value = data['new_value']\n    \n\
    \    # Pushpop from range (already heapified)\n    temp_list = lst[start:end]\n\
    \    if temp_list:\n        checksum = 0\n        for i in range(min(5, len(temp_list))):\
    \  # Pushpop up to 5 elements\n            val = (new_value + i) & 0xFFFFFFFF\n\
    \            popped = heappushpop(temp_list, val)\n            checksum ^= popped\n\
    \        \n        # Copy back\n        for i, val in enumerate(temp_list):\n\
    \            lst[start + i] = val\n        \n        return checksum\n    return\
    \ 0\n\n@benchmark.implementation(\"stdlib\", \"heappushpop\")\ndef heappushpop_stdlib(data):\n\
    \    \"\"\"Push and pop from heap using standard library\"\"\"\n    lst = data['data']\n\
    \    start, end = data['start'], data['end']\n    new_value = data['new_value']\n\
    \    \n    # Create slice and pushpop with stdlib (already heapified)\n    slice_copy\
    \ = lst[start:end]\n    if slice_copy:\n        checksum = 0\n        for i in\
    \ range(min(5, len(slice_copy))):  # Pushpop up to 5 elements\n            val\
    \ = (new_value + i) & 0xFFFFFFFF\n            popped = heapq.heappushpop(slice_copy,\
    \ val)\n            checksum ^= popped\n        \n        # Copy back\n      \
    \  for i, val in enumerate(slice_copy):\n            lst[start + i] = val\n  \
    \      \n        return checksum\n    return 0\n\nif __name__ == \"__main__\"\
    :\n    # Parse command line args and run appropriate mode\n    runner = benchmark.parse_args()\n\
    \    runner.run()\n"
  code: "#!/usr/bin/env python3\n\"\"\"\nBenchmark comparing heap operations on list\
    \ slices vs view objects vs direct indexing.\nTests heapify, heappop, heapreplace,\
    \ heappush, heappushpop operations.\n\"\"\"\n\nimport random\nimport sys\nimport\
    \ os\nsys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))\n\
    \nfrom cp_library.perf.benchmark import Benchmark, BenchmarkConfig\nfrom cp_library.ds.view.view_cls\
    \ import view\nfrom cp_library.ds.heap.fast_heapq import heapify, heappop, heapreplace,\
    \ heappush, heappushpop\nimport heapq  # Standard library for comparison\n\n#\
    \ Configure benchmark\nconfig = BenchmarkConfig(\n    name=\"heap_view\",\n  \
    \  sizes=[100000, 10000, 1000, 100, 50],  # Reverse order to warm up JIT\n   \
    \ operations=['heapify', 'heappop', 'heapreplace', 'heappush', 'heappushpop'],\n\
    \    iterations=10,\n    warmup=3,\n    output_dir=\"./output/benchmark_results/heap_view\"\
    \n)\n\n# Create benchmark instance\nbenchmark = Benchmark(config)\n\n# Data generator\n\
    @benchmark.data_generator(\"default\")\ndef generate_heap_data(size: int, operation:\
    \ str):\n    \"\"\"Generate test data for heap operations\"\"\"\n    # Generate\
    \ random list for heap operations\n    data = [random.randint(1, 1000000) for\
    \ _ in range(size)]\n    \n    # Generate random slice boundaries (30-70% of list\
    \ for reasonable heap size)\n    slice_size = random.randint(size // 3, min(size\
    \ * 2 // 3, size - 1))\n    start = random.randint(0, size - slice_size)\n   \
    \ end = start + slice_size\n    \n    return {\n        'data': data,\n      \
    \  'start': start,\n        'end': end,\n        'slice_size': slice_size,\n \
    \       'new_value': random.randint(1, 1000000),\n        'replace_value': random.randint(1,\
    \ 1000000),\n        'size': size,\n        'operation': operation\n    }\n\n\
    # Setup functions for operations that modify data\n@benchmark.setup(\"slice\"\
    , [\"heappop\", \"heapreplace\", \"heappush\", \"heappushpop\"])\ndef setup_slice_heap(data):\n\
    \    \"\"\"Setup function that copies data and heapifies before heap operations\"\
    \"\"\n    new_data = data.copy()\n    new_data['data'] = data['data'].copy()\n\
    \    \n    # Pre-heapify the slice for operations that need it\n    lst = new_data['data']\n\
    \    start, end = new_data['start'], new_data['end']\n    slice_copy = lst[start:end]\n\
    \    heapify(slice_copy)\n    for i, val in enumerate(slice_copy):\n        lst[start\
    \ + i] = val\n    \n    return new_data\n\n@benchmark.setup(\"view\", [\"heappop\"\
    , \"heapreplace\", \"heappush\", \"heappushpop\"])\ndef setup_view_heap(data):\n\
    \    \"\"\"Setup function that copies data and heapifies before heap operations\"\
    \"\"\n    new_data = data.copy()\n    new_data['data'] = data['data'].copy()\n\
    \    \n    # Pre-heapify the view for operations that need it\n    lst = new_data['data']\n\
    \    start, end = new_data['start'], new_data['end']\n    heap_view = view(lst,\
    \ start, end)\n    heapify(heap_view)\n    \n    return new_data\n\n@benchmark.setup(\"\
    direct\", [\"heappop\", \"heapreplace\", \"heappush\", \"heappushpop\"])\ndef\
    \ setup_direct_heap(data):\n    \"\"\"Setup function that copies data and heapifies\
    \ before heap operations\"\"\"\n    new_data = data.copy()\n    new_data['data']\
    \ = data['data'].copy()\n    \n    # Pre-heapify the range for operations that\
    \ need it\n    lst = new_data['data']\n    start, end = new_data['start'], new_data['end']\n\
    \    temp_list = lst[start:end]\n    heapify(temp_list)\n    for i, val in enumerate(temp_list):\n\
    \        lst[start + i] = val\n    \n    return new_data\n\n@benchmark.setup(\"\
    stdlib\", [\"heappop\", \"heapreplace\", \"heappush\", \"heappushpop\"])\ndef\
    \ setup_stdlib_heap(data):\n    \"\"\"Setup function that copies data and heapifies\
    \ before heap operations\"\"\"\n    new_data = data.copy()\n    new_data['data']\
    \ = data['data'].copy()\n    \n    # Pre-heapify the slice for operations that\
    \ need it\n    lst = new_data['data']\n    start, end = new_data['start'], new_data['end']\n\
    \    slice_copy = lst[start:end]\n    heapq.heapify(slice_copy)\n    for i, val\
    \ in enumerate(slice_copy):\n        lst[start + i] = val\n    \n    return new_data\n\
    \n# For heapify operation, we need setup without pre-heapifying\n@benchmark.setup(\"\
    slice\", [\"heapify\"])\ndef setup_slice_heapify(data):\n    \"\"\"Setup function\
    \ that only copies data for heapify operation\"\"\"\n    new_data = data.copy()\n\
    \    new_data['data'] = data['data'].copy()\n    return new_data\n\n@benchmark.setup(\"\
    view\", [\"heapify\"])\ndef setup_view_heapify(data):\n    \"\"\"Setup function\
    \ that only copies data for heapify operation\"\"\"\n    new_data = data.copy()\n\
    \    new_data['data'] = data['data'].copy()\n    return new_data\n\n@benchmark.setup(\"\
    direct\", [\"heapify\"])\ndef setup_direct_heapify(data):\n    \"\"\"Setup function\
    \ that only copies data for heapify operation\"\"\"\n    new_data = data.copy()\n\
    \    new_data['data'] = data['data'].copy()\n    return new_data\n\n@benchmark.setup(\"\
    stdlib\", [\"heapify\"])\ndef setup_stdlib_heapify(data):\n    \"\"\"Setup function\
    \ that only copies data for heapify operation\"\"\"\n    new_data = data.copy()\n\
    \    new_data['data'] = data['data'].copy()\n    return new_data\n\n# Heapify\
    \ operation\n@benchmark.implementation(\"slice\", \"heapify\")\ndef heapify_slice(data):\n\
    \    \"\"\"Heapify a slice\"\"\"\n    lst = data['data']\n    start, end = data['start'],\
    \ data['end']\n    \n    # Create slice and heapify\n    slice_copy = lst[start:end]\n\
    \    heapify(slice_copy)\n    \n    # Copy back manually\n    for i, val in enumerate(slice_copy):\n\
    \        lst[start + i] = val\n    \n    # Return checksum\n    checksum = 0\n\
    \    for i in range(start, min(start + 10, end)):  # First 10 elements\n     \
    \   checksum ^= lst[i]\n    return checksum\n\n@benchmark.implementation(\"view\"\
    , \"heapify\")\ndef heapify_view(data):\n    \"\"\"Heapify through a view\"\"\"\
    \n    lst = data['data']\n    start, end = data['start'], data['end']\n    \n\
    \    # Create view and heapify\n    heap_view = view(lst, start, end)\n    heapify(heap_view)\n\
    \    \n    # Return checksum\n    checksum = 0\n    for i in range(start, min(start\
    \ + 10, end)):  # First 10 elements\n        checksum ^= lst[i]\n    return checksum\n\
    \n@benchmark.implementation(\"direct\", \"heapify\")\ndef heapify_direct(data):\n\
    \    \"\"\"Heapify using direct list access\"\"\"\n    lst = data['data']\n  \
    \  start, end = data['start'], data['end']\n    \n    # Heapify the range directly\
    \ in the list\n    temp_list = lst[start:end]\n    heapify(temp_list)\n    for\
    \ i, val in enumerate(temp_list):\n        lst[start + i] = val\n    \n    # Return\
    \ checksum\n    checksum = 0\n    for i in range(start, min(start + 10, end)):\
    \  # First 10 elements\n        checksum ^= lst[i]\n    return checksum\n\n@benchmark.implementation(\"\
    stdlib\", \"heapify\")\ndef heapify_stdlib(data):\n    \"\"\"Heapify using standard\
    \ library\"\"\"\n    lst = data['data']\n    start, end = data['start'], data['end']\n\
    \    \n    # Create slice and heapify with stdlib\n    slice_copy = lst[start:end]\n\
    \    heapq.heapify(slice_copy)\n    \n    # Copy back manually\n    for i, val\
    \ in enumerate(slice_copy):\n        lst[start + i] = val\n    \n    # Return\
    \ checksum\n    checksum = 0\n    for i in range(start, min(start + 10, end)):\
    \  # First 10 elements\n        checksum ^= lst[i]\n    return checksum\n\n# Heappop\
    \ operation (heap is already heapified in setup)\n@benchmark.implementation(\"\
    slice\", \"heappop\")\ndef heappop_slice(data):\n    \"\"\"Pop from heap slice\"\
    \"\"\n    lst = data['data']\n    start, end = data['start'], data['end']\n  \
    \  \n    # Create slice and pop (already heapified)\n    slice_copy = lst[start:end]\n\
    \    \n    checksum = 0\n    for _ in range(min(10, len(slice_copy))):  # Pop\
    \ up to 10 elements\n        if slice_copy:\n            val = heappop(slice_copy)\n\
    \            checksum ^= val\n    \n    # Copy back\n    for i, val in enumerate(slice_copy):\n\
    \        lst[start + i] = val\n    \n    return checksum\n\n@benchmark.implementation(\"\
    view\", \"heappop\")\ndef heappop_view(data):\n    \"\"\"Pop from heap view\"\"\
    \"\n    lst = data['data']\n    start, end = data['start'], data['end']\n    \n\
    \    # Create view and pop (already heapified)\n    heap_view = view(lst, start,\
    \ end)\n    \n    checksum = 0\n    for _ in range(min(10, len(heap_view))): \
    \ # Pop up to 10 elements\n        if len(heap_view) > 0:\n            val = heappop(heap_view)\n\
    \            checksum ^= val\n    \n    return checksum\n\n@benchmark.implementation(\"\
    direct\", \"heappop\")\ndef heappop_direct(data):\n    \"\"\"Pop from heap using\
    \ direct access\"\"\"\n    lst = data['data']\n    start, end = data['start'],\
    \ data['end']\n    \n    # Pop from range (already heapified)\n    temp_list =\
    \ lst[start:end]\n    \n    checksum = 0\n    for _ in range(min(10, len(temp_list))):\
    \  # Pop up to 10 elements\n        if temp_list:\n            val = heappop(temp_list)\n\
    \            checksum ^= val\n    \n    # Copy back\n    for i, val in enumerate(temp_list):\n\
    \        lst[start + i] = val\n    \n    return checksum\n\n@benchmark.implementation(\"\
    stdlib\", \"heappop\")\ndef heappop_stdlib(data):\n    \"\"\"Pop from heap using\
    \ standard library\"\"\"\n    lst = data['data']\n    start, end = data['start'],\
    \ data['end']\n    \n    # Create slice and pop with stdlib (already heapified)\n\
    \    slice_copy = lst[start:end]\n    \n    checksum = 0\n    for _ in range(min(10,\
    \ len(slice_copy))):  # Pop up to 10 elements\n        if slice_copy:\n      \
    \      val = heapq.heappop(slice_copy)\n            checksum ^= val\n    \n  \
    \  # Copy back\n    for i, val in enumerate(slice_copy):\n        lst[start +\
    \ i] = val\n    \n    return checksum\n\n# Heapreplace operation (heap is already\
    \ heapified in setup)\n@benchmark.implementation(\"slice\", \"heapreplace\")\n\
    def heapreplace_slice(data):\n    \"\"\"Replace in heap slice\"\"\"\n    lst =\
    \ data['data']\n    start, end = data['start'], data['end']\n    new_value = data['new_value']\n\
    \    \n    # Create slice and replace (already heapified)\n    slice_copy = lst[start:end]\n\
    \    if slice_copy:\n        checksum = 0\n        for _ in range(min(5, len(slice_copy))):\
    \  # Replace up to 5 elements\n            if slice_copy:\n                val\
    \ = heapreplace(slice_copy, new_value)\n                checksum ^= val\n    \
    \            new_value = (new_value + 1) & 0xFFFFFFFF\n        \n        # Copy\
    \ back\n        for i, val in enumerate(slice_copy):\n            lst[start +\
    \ i] = val\n        \n        return checksum\n    return 0\n\n@benchmark.implementation(\"\
    view\", \"heapreplace\")\ndef heapreplace_view(data):\n    \"\"\"Replace in heap\
    \ view\"\"\"\n    lst = data['data']\n    start, end = data['start'], data['end']\n\
    \    new_value = data['new_value']\n    \n    # Create view and replace (already\
    \ heapified)\n    heap_view = view(lst, start, end)\n    if len(heap_view) > 0:\n\
    \        checksum = 0\n        for _ in range(min(5, len(heap_view))):  # Replace\
    \ up to 5 elements\n            if len(heap_view) > 0:\n                val =\
    \ heapreplace(heap_view, new_value)\n                checksum ^= val\n       \
    \         new_value = (new_value + 1) & 0xFFFFFFFF\n        \n        return checksum\n\
    \    return 0\n\n@benchmark.implementation(\"direct\", \"heapreplace\")\ndef heapreplace_direct(data):\n\
    \    \"\"\"Replace in heap using direct access\"\"\"\n    lst = data['data']\n\
    \    start, end = data['start'], data['end']\n    new_value = data['new_value']\n\
    \    \n    # Replace from range (already heapified)\n    temp_list = lst[start:end]\n\
    \    if temp_list:\n        checksum = 0\n        for _ in range(min(5, len(temp_list))):\
    \  # Replace up to 5 elements\n            if temp_list:\n                val\
    \ = heapreplace(temp_list, new_value)\n                checksum ^= val\n     \
    \           new_value = (new_value + 1) & 0xFFFFFFFF\n        \n        # Copy\
    \ back\n        for i, val in enumerate(temp_list):\n            lst[start + i]\
    \ = val\n        \n        return checksum\n    return 0\n\n@benchmark.implementation(\"\
    stdlib\", \"heapreplace\")\ndef heapreplace_stdlib(data):\n    \"\"\"Replace in\
    \ heap using standard library\"\"\"\n    lst = data['data']\n    start, end =\
    \ data['start'], data['end']\n    new_value = data['new_value']\n    \n    # Create\
    \ slice and replace with stdlib (already heapified)\n    slice_copy = lst[start:end]\n\
    \    if slice_copy:\n        checksum = 0\n        for _ in range(min(5, len(slice_copy))):\
    \  # Replace up to 5 elements\n            if slice_copy:\n                val\
    \ = heapq.heapreplace(slice_copy, new_value)\n                checksum ^= val\n\
    \                new_value = (new_value + 1) & 0xFFFFFFFF\n        \n        #\
    \ Copy back\n        for i, val in enumerate(slice_copy):\n            lst[start\
    \ + i] = val\n        \n        return checksum\n    return 0\n\n# Heappush operation\
    \ (heap is already heapified in setup)\n@benchmark.implementation(\"slice\", \"\
    heappush\")\ndef heappush_slice(data):\n    \"\"\"Push to heap slice\"\"\"\n \
    \   lst = data['data']\n    start, end = data['start'], data['end']\n    new_value\
    \ = data['new_value']\n    \n    # Create slice and push (already heapified)\n\
    \    slice_copy = lst[start:end]\n    \n    checksum = 0\n    for i in range(5):\
    \  # Push 5 elements\n        val = (new_value + i) & 0xFFFFFFFF\n        heappush(slice_copy,\
    \ val)\n        checksum ^= val\n    \n    # Note: Can't copy back easily since\
    \ slice grew, just return checksum\n    return checksum\n\n@benchmark.implementation(\"\
    view\", \"heappush\")\ndef heappush_view(data):\n    \"\"\"Push to heap view\"\
    \"\"\n    lst = data['data']\n    start, end = data['start'], data['end']\n  \
    \  new_value = data['new_value']\n    \n    # Create view and push (already heapified)\n\
    \    heap_view = view(lst, start, end)\n    \n    checksum = 0\n    max_push =\
    \ min(5, len(lst) - end)  # Limited by available space\n    for i in range(max_push):\n\
    \        val = (new_value + i) & 0xFFFFFFFF\n        heappush(heap_view, val)\n\
    \        checksum ^= val\n    \n    return checksum\n\n@benchmark.implementation(\"\
    direct\", \"heappush\")\ndef heappush_direct(data):\n    \"\"\"Push to heap using\
    \ direct access\"\"\"\n    lst = data['data']\n    start, end = data['start'],\
    \ data['end']\n    new_value = data['new_value']\n    \n    # Push to range (already\
    \ heapified)\n    temp_list = lst[start:end]\n    \n    checksum = 0\n    for\
    \ i in range(5):  # Push 5 elements\n        val = (new_value + i) & 0xFFFFFFFF\n\
    \        heappush(temp_list, val)\n        checksum ^= val\n    \n    # Note:\
    \ Can't copy back easily since temp_list grew, just return checksum\n    return\
    \ checksum\n\n@benchmark.implementation(\"stdlib\", \"heappush\")\ndef heappush_stdlib(data):\n\
    \    \"\"\"Push to heap using standard library\"\"\"\n    lst = data['data']\n\
    \    start, end = data['start'], data['end']\n    new_value = data['new_value']\n\
    \    \n    # Create slice and push with stdlib (already heapified)\n    slice_copy\
    \ = lst[start:end]\n    \n    checksum = 0\n    for i in range(5):  # Push 5 elements\n\
    \        val = (new_value + i) & 0xFFFFFFFF\n        heapq.heappush(slice_copy,\
    \ val)\n        checksum ^= val\n    \n    # Note: Can't copy back easily since\
    \ slice grew, just return checksum\n    return checksum\n\n# Heappushpop operation\
    \ (heap is already heapified in setup)\n@benchmark.implementation(\"slice\", \"\
    heappushpop\")\ndef heappushpop_slice(data):\n    \"\"\"Push and pop from heap\
    \ slice\"\"\"\n    lst = data['data']\n    start, end = data['start'], data['end']\n\
    \    new_value = data['new_value']\n    \n    # Create slice and pushpop (already\
    \ heapified)\n    slice_copy = lst[start:end]\n    if slice_copy:\n        checksum\
    \ = 0\n        for i in range(min(5, len(slice_copy))):  # Pushpop up to 5 elements\n\
    \            val = (new_value + i) & 0xFFFFFFFF\n            popped = heappushpop(slice_copy,\
    \ val)\n            checksum ^= popped\n        \n        # Copy back\n      \
    \  for i, val in enumerate(slice_copy):\n            lst[start + i] = val\n  \
    \      \n        return checksum\n    return 0\n\n@benchmark.implementation(\"\
    view\", \"heappushpop\")\ndef heappushpop_view(data):\n    \"\"\"Push and pop\
    \ from heap view\"\"\"\n    lst = data['data']\n    start, end = data['start'],\
    \ data['end']\n    new_value = data['new_value']\n    \n    # Create view and\
    \ pushpop (already heapified)\n    heap_view = view(lst, start, end)\n    if len(heap_view)\
    \ > 0:\n        checksum = 0\n        for i in range(min(5, len(heap_view))):\
    \  # Pushpop up to 5 elements\n            val = (new_value + i) & 0xFFFFFFFF\n\
    \            popped = heappushpop(heap_view, val)\n            checksum ^= popped\n\
    \        \n        return checksum\n    return 0\n\n@benchmark.implementation(\"\
    direct\", \"heappushpop\")\ndef heappushpop_direct(data):\n    \"\"\"Push and\
    \ pop from heap using direct access\"\"\"\n    lst = data['data']\n    start,\
    \ end = data['start'], data['end']\n    new_value = data['new_value']\n    \n\
    \    # Pushpop from range (already heapified)\n    temp_list = lst[start:end]\n\
    \    if temp_list:\n        checksum = 0\n        for i in range(min(5, len(temp_list))):\
    \  # Pushpop up to 5 elements\n            val = (new_value + i) & 0xFFFFFFFF\n\
    \            popped = heappushpop(temp_list, val)\n            checksum ^= popped\n\
    \        \n        # Copy back\n        for i, val in enumerate(temp_list):\n\
    \            lst[start + i] = val\n        \n        return checksum\n    return\
    \ 0\n\n@benchmark.implementation(\"stdlib\", \"heappushpop\")\ndef heappushpop_stdlib(data):\n\
    \    \"\"\"Push and pop from heap using standard library\"\"\"\n    lst = data['data']\n\
    \    start, end = data['start'], data['end']\n    new_value = data['new_value']\n\
    \    \n    # Create slice and pushpop with stdlib (already heapified)\n    slice_copy\
    \ = lst[start:end]\n    if slice_copy:\n        checksum = 0\n        for i in\
    \ range(min(5, len(slice_copy))):  # Pushpop up to 5 elements\n            val\
    \ = (new_value + i) & 0xFFFFFFFF\n            popped = heapq.heappushpop(slice_copy,\
    \ val)\n            checksum ^= popped\n        \n        # Copy back\n      \
    \  for i, val in enumerate(slice_copy):\n            lst[start + i] = val\n  \
    \      \n        return checksum\n    return 0\n\nif __name__ == \"__main__\"\
    :\n    # Parse command line args and run appropriate mode\n    runner = benchmark.parse_args()\n\
    \    runner.run()"
  dependsOn:
  - cp_library/perf/benchmark.py
  - cp_library/ds/view/view_cls.py
  - cp_library/ds/heap/fast_heapq.py
  - cp_library/ds/list/list_find_fn.py
  isVerificationFile: false
  path: perf/heap_view.py
  requiredBy: []
  timestamp: '2025-07-11 23:11:42+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: perf/heap_view.py
layout: document
redirect_from:
- /library/perf/heap_view.py
- /library/perf/heap_view.py.html
title: perf/heap_view.py
---
