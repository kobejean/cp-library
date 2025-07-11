---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/pack/packer_cls.py
    title: cp_library/bit/pack/packer_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/grid/grid_cls.py
    title: cp_library/ds/grid/grid_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/list/list_find_fn.py
    title: cp_library/ds/list/list_find_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/view/view_cls.py
    title: cp_library/ds/view/view_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/fast_io_cls.py
    title: cp_library/io/fast_io_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/parser_cls.py
    title: cp_library/io/parser_cls.py
  - icon: ':warning:'
    path: cp_library/perf/benchmark.py
    title: cp_library/perf/benchmark.py
  - icon: ':warning:'
    path: cp_library/perf/checksum.py
    title: cp_library/perf/checksum.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "#!/usr/bin/env python3\n\"\"\"\nSimple Grid benchmark - minimal overhead,\
    \ focused on core operations.\n\"\"\"\n\nimport random\nimport sys\nimport os\n\
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
    \ {speedup:<10.1f}x\")\n\n\n\"\"\"\nMinimal checksum utilities for benchmark validation.\n\
    \"\"\"\n\ndef update_checksum(current: int, value: int) -> int:\n    \"\"\"Update\
    \ checksum with a single value.\"\"\"\n    return (current * 31 + value) & 0xFFFFFFFF\n\
    '''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\n   \
    \          https://kobejean.github.io/cp-library               \n'''\nimport typing\n\
    from collections import deque\nfrom numbers import Number\nfrom types import GenericAlias\
    \ \nfrom typing import Callable, Collection, Iterator, Union\nfrom io import BytesIO,\
    \ IOBase\n\n\nclass FastIO(IOBase):\n    BUFSIZE = 8192\n    newlines = 0\n\n\
    \    def __init__(self, file):\n        self._fd = file.fileno()\n        self.buffer\
    \ = BytesIO()\n        self.writable = \"x\" in file.mode or \"r\" not in file.mode\n\
    \        self.write = self.buffer.write if self.writable else None\n\n    def\
    \ read(self):\n        BUFSIZE = self.BUFSIZE\n        while True:\n         \
    \   b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))\n        \
    \    if not b: break\n            ptr = self.buffer.tell()\n            self.buffer.seek(0,\
    \ 2), self.buffer.write(b), self.buffer.seek(ptr)\n        self.newlines = 0\n\
    \        return self.buffer.read()\n\n    def readline(self):\n        BUFSIZE\
    \ = self.BUFSIZE\n        while self.newlines == 0:\n            b = os.read(self._fd,\
    \ max(os.fstat(self._fd).st_size, BUFSIZE))\n            self.newlines = b.count(b\"\
    \\n\") + (not b)\n            ptr = self.buffer.tell()\n            self.buffer.seek(0,\
    \ 2), self.buffer.write(b), self.buffer.seek(ptr)\n        self.newlines -= 1\n\
    \        return self.buffer.readline()\n\n    def flush(self):\n        if self.writable:\n\
    \            os.write(self._fd, self.buffer.getvalue())\n            self.buffer.truncate(0),\
    \ self.buffer.seek(0)\n\n\nclass IOWrapper(IOBase):\n    stdin: 'IOWrapper' =\
    \ None\n    stdout: 'IOWrapper' = None\n    \n    def __init__(self, file):\n\
    \        self.buffer = FastIO(file)\n        self.flush = self.buffer.flush\n\
    \        self.writable = self.buffer.writable\n\n    def write(self, s):\n   \
    \     return self.buffer.write(s.encode(\"ascii\"))\n    \n    def read(self):\n\
    \        return self.buffer.read().decode(\"ascii\")\n    \n    def readline(self):\n\
    \        return self.buffer.readline().decode(\"ascii\")\ntry:\n    sys.stdin\
    \ = IOWrapper.stdin = IOWrapper(sys.stdin)\n    sys.stdout = IOWrapper.stdout\
    \ = IOWrapper(sys.stdout)\nexcept:\n    pass\nfrom typing import TypeVar\n_S =\
    \ TypeVar('S')\n_T = TypeVar('T')\n_U = TypeVar('U')\n\nclass TokenStream(Iterator):\n\
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
    \ __class_getitem__(cls, item):\n        return GenericAlias(cls, item)\n\nfrom\
    \ typing import Generic\n\n\n\ndef list_find(lst: list, value, start = 0, stop\
    \ = sys.maxsize):\n    try:\n        return lst.index(value, start, stop)\n  \
    \  except:\n        return -1\n\n\nclass view(Generic[_T]):\n    __slots__ = 'A',\
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
    \ \n    def validate(V): return 0 <= V.l <= V.r <= len(V.A)\n\n\n\nclass Packer:\n\
    \    __slots__ = 's', 'm'\n    def __init__(P, mx: int): P.s = mx.bit_length();\
    \ P.m = (1 << P.s) - 1\n    def enc(P, a: int, b: int): return a << P.s | b\n\
    \    def dec(P, x: int) -> tuple[int, int]: return x >> P.s, x & P.m\n    def\
    \ enumerate(P, A, reverse=False): P.ienumerate(A:=list(A), reverse); return A\n\
    \    def ienumerate(P, A, reverse=False):\n        if reverse:\n            for\
    \ i,a in enumerate(A): A[i] = P.enc(-a, i)\n        else:\n            for i,a\
    \ in enumerate(A): A[i] = P.enc(a, i)\n    def indices(P, A: list[int]): P.iindices(A:=list(A));\
    \ return A\n    def iindices(P, A):\n        for i,a in enumerate(A): A[i] = P.m&a\n\
    \n\nclass Grid(Generic[_T], Parsable):\n    __slots__ = 'pkr', 'size', 'H', 'W',\
    \ 'A'\n    def __init__(G, H: int, W: int, A: Union[_T, list[_T], list[list[_T]]],\
    \ pkr = None):\n        G.pkr = pkr or Packer(W-1); G.size = H << G.pkr.s; G.H,\
    \ G.W = H, W\n        if isinstance(A, list):\n            if isinstance(A[0],\
    \ list):\n                G.A = [A[0][0]]*G.size\n                for i in range(H):\n\
    \                    ii = i << G.pkr.s\n                    for j in range(W):\
    \ G.A[ii|j] = A[i][j]\n            elif len(A) < G.size:\n                G.A\
    \ = [A[0]]*G.size\n                for i in range(H):\n                    ii\
    \ = i << G.pkr.s\n                    for j in range(W): G.A[ii|j] = A[i*W+j]\n\
    \            else:\n                G.A = A\n        else:\n            G.A =\
    \ [A] * G.size\n    def __len__(G): return G.H\n    def __getitem__(G, i: int):\
    \ \n        if 0 <= i < G.H: return view(G.A, i<<G.pkr.s, (i+1)<<G.pkr.s)\n  \
    \      else: raise IndexError\n    def __call__(G, i: int, j: int): return G.A[G.pkr.enc(i,j)]\n\
    \    def set(G, i: int, j: int, v: _T): G.A[G.pkr.enc(i,j)] = v\n\n    @classmethod\n\
    \    def compile(cls, H: int, W: int, T: type = int):\n        pkr = Packer(W-1);\
    \ size = H << pkr.s\n        if T is int:\n            def parse(ts: TokenStream):\n\
    \                A = [0]*size\n                for i in range(H):\n          \
    \          for j,s in ts.line(): A[pkr.enc(i,j)] = int(s)\n                return\
    \ cls(H, W, A, pkr)\n        elif T is str:\n            def parse(ts: TokenStream):\n\
    \                A = ['']*size\n                for i in range(H):\n         \
    \           for j,s in ts.line(): A[pkr.enc(i,j)] = s\n                return\
    \ cls(H, W, A, pkr)\n        else:\n            elm = Parser.compile(T)\n    \
    \        def parse(ts: TokenStream):\n                A = [None]*size\n      \
    \          for i in range(H):\n                    for j in range(W): A[pkr.enc(i,j)]\
    \ = elm(ts)\n                return cls(H, W, A, pkr)\n        return parse\n\n\
    config = BenchmarkConfig(\n    name=\"grid\",\n    sizes=[10000000, 1000000, 100000,\
    \ 10000, 1000, 100],\n    operations=['construction', 'random_access', 'row_access',\
    \ 'sequential_access'],\n    iterations=10,\n    warmup=2,\n    output_dir=\"\
    ./output/benchmark_results/grid\"\n)\n\nbenchmark = Benchmark(config)\n\n@benchmark.data_generator(\"\
    default\")\ndef generate_data(size: int, _: str):\n    H = int(size ** 0.5)\n\
    \    W = size // H\n    \n    data = [[random.randint(1, 1000000) for _ in range(W)]\
    \ for _ in range(H)]\n    flat = [val for row in data for val in row]\n    \n\
    \    return {\n        'grid': Grid(H, W, data),\n        'lists': data,\n   \
    \     'flat': flat,\n        'H': H, 'W': W,\n        'coords': [(random.randint(0,\
    \ H-1), random.randint(0, W-1)) for _ in range(min(100, size))]\n    }\n\n# Construction\n\
    @benchmark.implementation(\"grid\", \"construction\")\ndef construction_grid(data):\n\
    \    H, W = data['H'], data['W']\n    grid = Grid(H, W, data['flat'])\n    result\
    \ = 0\n    for i in range(H):\n        for j in range(W):\n            result\
    \ = update_checksum(result, grid(i, j))\n    return result\n\n@benchmark.implementation(\"\
    lists\", \"construction\")\ndef construction_lists(data):\n    H, W = data['H'],\
    \ data['W']\n    lists = [row[:] for row in data['lists']]\n    result = 0\n \
    \   for i in range(H):\n        for j in range(W):\n            result = update_checksum(result,\
    \ lists[i][j])\n    return result\n\n@benchmark.implementation(\"flat\", \"construction\"\
    )\ndef construction_flat(data):\n    H, W = data['H'], data['W']\n    flat = data['flat'][:]\n\
    \    result = 0\n    for i in range(H):\n        for j in range(W):\n        \
    \    result = update_checksum(result, flat[i * W + j])\n    return result\n\n\
    # Random access\n@benchmark.implementation(\"grid\", \"random_access\")\ndef random_access_grid(data):\n\
    \    grid = data['grid']\n    result = 0\n    for i, j in data['coords']:\n  \
    \      result = update_checksum(result, grid(i, j))\n    return result\n\n@benchmark.implementation(\"\
    lists\", \"random_access\")\ndef random_access_lists(data):\n    lists = data['lists']\n\
    \    result = 0\n    for i, j in data['coords']:\n        result = update_checksum(result,\
    \ lists[i][j])\n    return result\n\n@benchmark.implementation(\"flat\", \"random_access\"\
    )\ndef random_access_flat(data):\n    flat, W = data['flat'], data['W']\n    result\
    \ = 0\n    for i, j in data['coords']:\n        result = update_checksum(result,\
    \ flat[i * W + j])\n    return result\n\n# Row access\n@benchmark.implementation(\"\
    grid\", \"row_access\")\ndef row_access_grid(data):\n    H, W = data['H'], data['W']\n\
    \    grid = data['grid']\n    return sum(W for i in range(H) if grid[i])  # Count\
    \ logical width\n\n@benchmark.implementation(\"lists\", \"row_access\")\ndef row_access_lists(data):\n\
    \    H = data['H']\n    lists = data['lists']\n    return sum(len(lists[i]) for\
    \ i in range(H))\n\n@benchmark.implementation(\"flat\", \"row_access\")\ndef row_access_flat(data):\n\
    \    H, W = data['H'], data['W']\n    flat = data['flat']\n    return sum(len(flat[i\
    \ * W:(i + 1) * W]) for i in range(H))\n\n# Sequential access\n@benchmark.implementation(\"\
    grid\", \"sequential_access\")\ndef sequential_access_grid(data):\n    H, W =\
    \ data['H'], data['W']\n    grid = data['grid']\n    result = 0\n    for i in\
    \ range(H):\n        for j in range(W):\n            result = update_checksum(result,\
    \ grid(i, j))\n    return result\n\n@benchmark.implementation(\"lists\", \"sequential_access\"\
    )\ndef sequential_access_lists(data):\n    H, W = data['H'], data['W']\n    lists\
    \ = data['lists']\n    result = 0\n    for i in range(H):\n        for j in range(W):\n\
    \            result = update_checksum(result, lists[i][j])\n    return result\n\
    \n@benchmark.implementation(\"flat\", \"sequential_access\")\ndef sequential_access_flat(data):\n\
    \    H, W = data['H'], data['W']\n    flat = data['flat']\n    result = 0\n  \
    \  for i in range(H):\n        for j in range(W):\n            result = update_checksum(result,\
    \ flat[i * W + j])\n    return result\n\nif __name__ == \"__main__\":\n    # Parse\
    \ command line args and run appropriate mode\n    runner = benchmark.parse_args()\n\
    \    runner.run()\n"
  code: "#!/usr/bin/env python3\n\"\"\"\nSimple Grid benchmark - minimal overhead,\
    \ focused on core operations.\n\"\"\"\n\nimport random\nimport sys\nimport os\n\
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))\n\
    \nfrom cp_library.perf.benchmark import Benchmark, BenchmarkConfig\nfrom cp_library.perf.checksum\
    \ import update_checksum\nfrom cp_library.ds.grid.grid_cls import Grid\n\nconfig\
    \ = BenchmarkConfig(\n    name=\"grid\",\n    sizes=[10000000, 1000000, 100000,\
    \ 10000, 1000, 100],\n    operations=['construction', 'random_access', 'row_access',\
    \ 'sequential_access'],\n    iterations=10,\n    warmup=2,\n    output_dir=\"\
    ./output/benchmark_results/grid\"\n)\n\nbenchmark = Benchmark(config)\n\n@benchmark.data_generator(\"\
    default\")\ndef generate_data(size: int, _: str):\n    H = int(size ** 0.5)\n\
    \    W = size // H\n    \n    data = [[random.randint(1, 1000000) for _ in range(W)]\
    \ for _ in range(H)]\n    flat = [val for row in data for val in row]\n    \n\
    \    return {\n        'grid': Grid(H, W, data),\n        'lists': data,\n   \
    \     'flat': flat,\n        'H': H, 'W': W,\n        'coords': [(random.randint(0,\
    \ H-1), random.randint(0, W-1)) for _ in range(min(100, size))]\n    }\n\n# Construction\n\
    @benchmark.implementation(\"grid\", \"construction\")\ndef construction_grid(data):\n\
    \    H, W = data['H'], data['W']\n    grid = Grid(H, W, data['flat'])\n    result\
    \ = 0\n    for i in range(H):\n        for j in range(W):\n            result\
    \ = update_checksum(result, grid(i, j))\n    return result\n\n@benchmark.implementation(\"\
    lists\", \"construction\")\ndef construction_lists(data):\n    H, W = data['H'],\
    \ data['W']\n    lists = [row[:] for row in data['lists']]\n    result = 0\n \
    \   for i in range(H):\n        for j in range(W):\n            result = update_checksum(result,\
    \ lists[i][j])\n    return result\n\n@benchmark.implementation(\"flat\", \"construction\"\
    )\ndef construction_flat(data):\n    H, W = data['H'], data['W']\n    flat = data['flat'][:]\n\
    \    result = 0\n    for i in range(H):\n        for j in range(W):\n        \
    \    result = update_checksum(result, flat[i * W + j])\n    return result\n\n\
    # Random access\n@benchmark.implementation(\"grid\", \"random_access\")\ndef random_access_grid(data):\n\
    \    grid = data['grid']\n    result = 0\n    for i, j in data['coords']:\n  \
    \      result = update_checksum(result, grid(i, j))\n    return result\n\n@benchmark.implementation(\"\
    lists\", \"random_access\")\ndef random_access_lists(data):\n    lists = data['lists']\n\
    \    result = 0\n    for i, j in data['coords']:\n        result = update_checksum(result,\
    \ lists[i][j])\n    return result\n\n@benchmark.implementation(\"flat\", \"random_access\"\
    )\ndef random_access_flat(data):\n    flat, W = data['flat'], data['W']\n    result\
    \ = 0\n    for i, j in data['coords']:\n        result = update_checksum(result,\
    \ flat[i * W + j])\n    return result\n\n# Row access\n@benchmark.implementation(\"\
    grid\", \"row_access\")\ndef row_access_grid(data):\n    H, W = data['H'], data['W']\n\
    \    grid = data['grid']\n    return sum(W for i in range(H) if grid[i])  # Count\
    \ logical width\n\n@benchmark.implementation(\"lists\", \"row_access\")\ndef row_access_lists(data):\n\
    \    H = data['H']\n    lists = data['lists']\n    return sum(len(lists[i]) for\
    \ i in range(H))\n\n@benchmark.implementation(\"flat\", \"row_access\")\ndef row_access_flat(data):\n\
    \    H, W = data['H'], data['W']\n    flat = data['flat']\n    return sum(len(flat[i\
    \ * W:(i + 1) * W]) for i in range(H))\n\n# Sequential access\n@benchmark.implementation(\"\
    grid\", \"sequential_access\")\ndef sequential_access_grid(data):\n    H, W =\
    \ data['H'], data['W']\n    grid = data['grid']\n    result = 0\n    for i in\
    \ range(H):\n        for j in range(W):\n            result = update_checksum(result,\
    \ grid(i, j))\n    return result\n\n@benchmark.implementation(\"lists\", \"sequential_access\"\
    )\ndef sequential_access_lists(data):\n    H, W = data['H'], data['W']\n    lists\
    \ = data['lists']\n    result = 0\n    for i in range(H):\n        for j in range(W):\n\
    \            result = update_checksum(result, lists[i][j])\n    return result\n\
    \n@benchmark.implementation(\"flat\", \"sequential_access\")\ndef sequential_access_flat(data):\n\
    \    H, W = data['H'], data['W']\n    flat = data['flat']\n    result = 0\n  \
    \  for i in range(H):\n        for j in range(W):\n            result = update_checksum(result,\
    \ flat[i * W + j])\n    return result\n\nif __name__ == \"__main__\":\n    # Parse\
    \ command line args and run appropriate mode\n    runner = benchmark.parse_args()\n\
    \    runner.run()"
  dependsOn:
  - cp_library/perf/benchmark.py
  - cp_library/perf/checksum.py
  - cp_library/ds/grid/grid_cls.py
  - cp_library/io/parser_cls.py
  - cp_library/ds/view/view_cls.py
  - cp_library/bit/pack/packer_cls.py
  - cp_library/io/fast_io_cls.py
  - cp_library/ds/list/list_find_fn.py
  isVerificationFile: false
  path: perf/grid.py
  requiredBy: []
  timestamp: '2025-07-11 23:11:42+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: perf/grid.py
layout: document
redirect_from:
- /library/perf/grid.py
- /library/perf/grid.py.html
title: perf/grid.py
---
