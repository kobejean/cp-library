---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/math/mod/mint_cls.py
    title: cp_library/math/mod/mint_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/mod/mint_ntt_cls.py
    title: cp_library/math/mod/mint_ntt_cls.py
  - icon: ':warning:'
    path: cp_library/math/mod/mlist_cls.py
    title: cp_library/math/mod/mlist_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/nt/mod_inv_fn.py
    title: cp_library/math/nt/mod_inv_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/nt/ntt_cls.py
    title: cp_library/math/nt/ntt_cls.py
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
  bundledCode: "#!/usr/bin/env python3\n\"\"\"\nComprehensive benchmark comparing\
    \ modular arithmetic approaches on lists:\n1. Plain int list with manual modular\
    \ operations\n2. mlist_cls (optimized modular list)\n3. List of mint_cls (modular\
    \ integers)\n\nTests various operations to provide fair comparison across different\
    \ use cases.\n\"\"\"\n\nimport random\nimport sys\nimport os\nsys.path.insert(0,\
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
    \              \n'''\n    \nclass mint(int):\n    mod: int\n    zero: 'mint'\n\
    \    one: 'mint'\n    two: 'mint'\n    cache: list['mint']\n\n    def __new__(cls,\
    \ *args, **kwargs):\n        if 0 <= (x := int(*args, **kwargs)) < 64:\n     \
    \       return cls.cache[x]\n        else:\n            return cls.fix(x)\n\n\
    \    @classmethod\n    def set_mod(cls, mod: int):\n        mint.mod = cls.mod\
    \ = mod\n        mint.zero = cls.zero = cls.cast(0)\n        mint.one = cls.one\
    \ = cls.fix(1)\n        mint.two = cls.two = cls.fix(2)\n        mint.cache =\
    \ cls.cache = [cls.zero, cls.one, cls.two]\n        for x in range(3,64): mint.cache.append(cls.fix(x))\n\
    \n    @classmethod\n    def fix(cls, x): return cls.cast(x%cls.mod)\n\n    @classmethod\n\
    \    def cast(cls, x): return super().__new__(cls,x)\n\n    @classmethod\n   \
    \ def mod_inv(cls, x):\n        a,b,s,t = int(x), cls.mod, 1, 0\n        while\
    \ b: a,b,s,t = b,a%b,t,s-a//b*t\n        if a == 1: return cls.fix(s)\n      \
    \  raise ValueError(f\"{x} is not invertible in mod {cls.mod}\")\n    \n    @property\n\
    \    def inv(self): return mint.mod_inv(self)\n\n    def __add__(self, x): return\
    \ mint.fix(super().__add__(x))\n    def __radd__(self, x): return mint.fix(super().__radd__(x))\n\
    \    def __sub__(self, x): return mint.fix(super().__sub__(x))\n    def __rsub__(self,\
    \ x): return mint.fix(super().__rsub__(x))\n    def __mul__(self, x): return mint.fix(super().__mul__(x))\n\
    \    def __rmul__(self, x): return mint.fix(super().__rmul__(x))\n    def __floordiv__(self,\
    \ x): return self * mint.mod_inv(x)\n    def __rfloordiv__(self, x): return self.inv\
    \ * x\n    def __truediv__(self, x): return self * mint.mod_inv(x)\n    def __rtruediv__(self,\
    \ x): return self.inv * x\n    def __pow__(self, x): \n        return self.cast(super().__pow__(x,\
    \ self.mod))\n    def __neg__(self): return mint.mod-self\n    def __pos__(self):\
    \ return self\n    def __abs__(self): return self\n    def __class_getitem__(self,\
    \ x: int): return self.cache[x]\n\n\n\ndef mod_inv(x, mod):\n    a,b,s,t = x,\
    \ mod, 1, 0\n    while b:\n        a,b,s,t = b,a%b,t,s-a//b*t\n    if a == 1:\
    \ return s % mod\n    raise ValueError(f\"{x} is not invertible in mod {mod}\"\
    )\n\nclass NTT:\n    def __init__(self, mod = 998244353) -> None:\n        self.mod\
    \ = m = mod\n        self.g = g = self.primitive_root(m)\n        self.rank2 =\
    \ rank2 = ((m-1)&(1-m)).bit_length() - 1\n        self.root = root = [0] * (rank2\
    \ + 1)\n        root[rank2] = pow(g, (m - 1) >> rank2, m)\n        self.iroot\
    \ = iroot = [0] * (rank2 + 1)\n        iroot[rank2] = pow(root[rank2], m - 2,\
    \ m)\n        for i in range(rank2 - 1, -1, -1):\n            root[i] = root[i+1]\
    \ * root[i+1] % m\n            iroot[i] = iroot[i+1] * iroot[i+1] % m\n      \
    \  def rates(s):\n            r8,ir8 = [0]*max(0,rank2-s+1), [0]*max(0,rank2-s+1)\n\
    \            p = ip = 1\n            for i in range(rank2-s+1):\n            \
    \    r, ir = root[i+s], iroot[i+s]\n                p,ip,r8[i],ir8[i]= p*ir%m,ip*r%m,r*p%m,ir*ip%m\n\
    \            return r8, ir8\n        self.rate2, self.irate2 = rates(2)\n    \
    \    self.rate3, self.irate3 = rates(3)\n \n    def primitive_root(self, m):\n\
    \        if m == 2: return 1\n        if m == 167772161: return 3\n        if\
    \ m == 469762049: return 3\n        if m == 754974721: return 11\n        if m\
    \ == 998244353: return 3\n        divs = [0] * 20\n        cnt, divs[0], x = 1,\
    \ 2, (m - 1) // 2\n        while x % 2 == 0: x //= 2\n        i=3\n        while\
    \ i*i <= x:\n            if x%i == 0:\n                divs[cnt],cnt = i,cnt+1\n\
    \                while x%i==0:x//=i\n            i+=2\n        if x > 1: divs[cnt],cnt\
    \ = x,cnt+1\n        for g in range(2,m):\n            for i in range(cnt):\n\
    \                if pow(g,(m-1)//divs[i],m)==1:break\n            else:return\
    \ g\n    \n    def fntt(self, A: list[int]):\n        im, r8, m, h = self.root[2],self.rate3,self.mod,(len(A)-1).bit_length()\n\
    \        for L in range(0,h-1,2):\n            p, r = 1<<(h-L-2),1\n         \
    \   for s in range(1 << L):\n                r3,of=(r2:=r*r%m)*r%m,s<<(h-L)\n\
    \                for i in range(p):\n                    i3=(i2:=(i1:=(i0:=i+of)+p)+p)+p\n\
    \                    a0,a1,a2,a3 = A[i0],A[i1]*r,A[i2]*r2,A[i3]*r3\n         \
    \           a0,a1,a2,a3 = a0+a2,a1+a3,a0-a2,(a1-a3)%m*im\n                   \
    \ A[i0],A[i1],A[i2],A[i3] = (a0+a1)%m,(a0-a1)%m,(a2+a3)%m,(a2-a3)%m\n        \
    \        r=r*r8[(~s&-~s).bit_length()-1]%m\n        if h&1:\n            r, r8\
    \ = 1, self.rate2\n            for s in range(1<<(h-1)):\n                i1=(i0:=s<<1)+1\n\
    \                al,ar = A[i0],A[i1]*r%m\n                A[i0],A[i1] = (al+ar)%m,(al-ar)%m\n\
    \                r=r*r8[(~s&-~s).bit_length()-1]%m\n        return A\n    \n \
    \   def _ifntt(self, A: list[int]):\n        im, r8, m, h = self.iroot[2],self.irate3,self.mod,(len(A)-1).bit_length()\n\
    \        for L in range(h,1,-2):\n            p,r = 1<<(h-L),1\n            for\
    \ s in range(1<<(L-2)):\n                r3,of=(r2:=r*r%m)*r%m,s<<(h-L+2)\n  \
    \              for i in range(p):\n                    i3=(i2:=(i1:=(i0:=i+of)+p)+p)+p\n\
    \                    a0,a1,a2,a3 = A[i0],A[i1],A[i2],A[i3]\n                 \
    \   a0,a1,a2,a3 = a0+a1,a2+a3,a0-a1,(a2-a3)*im%m\n                    A[i0],A[i1],A[i2],A[i3]\
    \ = (a0+a1)%m,(a2+a3)*r%m,(a0-a1)*r2%m,(a2-a3)*r3%m\n                r=r*r8[(~s&-~s).bit_length()-1]%m\n\
    \        if h&1:\n            for i0 in range(p:=1<<(h-1)):\n                al,ar\
    \ = A[i0],A[i1:=i0+p]\n                A[i0],A[i1] = (al+ar)%m,(al-ar)%m\n   \
    \     return A\n\n    def ifntt(self, A: list[int]):\n        self._ifntt(A)\n\
    \        iz = mod_inv(N:=len(A),mod:=self.mod)\n        for i in range(N): A[i]=A[i]*iz%mod\n\
    \        return A\n    \n    def conv_naive(self, A, B, N):\n        n, m, mod\
    \ = len(A),len(B),self.mod\n        C = [0]*N\n        if n < m: A,B,n,m = B,A,m,n\n\
    \        for i,a in enumerate(A):\n            for j in range(min(m,N-i)):\n \
    \               C[ij]=(C[ij:=i+j]+a*B[j])%mod\n        return C\n    \n    def\
    \ conv_fntt(self, A, B, N):\n        n,m,mod=len(A),len(B),self.mod\n        z=1<<(n+m-2).bit_length()\n\
    \        self.fntt(A:=A+[0]*(z-n)), self.fntt(B:=B+[0]*(z-m))\n        for i,\
    \ b in enumerate(B): A[i] = A[i] * b % mod\n        self.ifntt(A)\n        del\
    \ A[N:]\n        return A\n    \n    def deconv(self, C, B, N = None):\n     \
    \   n, m = len(C), len(B)\n        if N is None: N = n - m + 1\n        z = 1\
    \ << (n + m - 2).bit_length()\n        self.fntt(C := C+[0]*(z-n)), self.fntt(B\
    \ := B+[0]*(z - m))\n\n        A = [0] * z\n        for i in range(z):\n     \
    \       if B[i] == 0:\n                raise ValueError(\"Division by zero in\
    \ NTT domain - deconvolution not possible\")\n            b_inv = mod_inv(B[i],\
    \ self.mod)\n            A[i] = (C[i] * b_inv) % self.mod\n        \n        self.ifntt(A)\n\
    \        return A[:N]\n    \n    def conv_half(self, A, Bres):\n        mod =\
    \ self.mod\n        self.fntt(A)\n        for i, b in enumerate(Bres): A[i] =\
    \ A[i] * b % mod\n        self.ifntt(A)\n        return A\n    \n    def conv(self,\
    \ A, B, N = None):\n        n,m = len(A), len(B)\n        N = n+m-1 if N is None\
    \ else N\n        if min(n,m) <= 60: return self.conv_naive(A, B, N)\n       \
    \ return self.conv_fntt(A, B, N)\n\n    def cycle_conv(self, A, B):\n        n,m,mod=len(A),len(B),self.mod\n\
    \        assert n == m\n        if n==0:return[]\n        con,res=self.conv(A,B),[0]*n\n\
    \        for i in range(n-1):res[i]=(con[i]+con[i+n])%mod\n        res[n-1]=con[n-1]\n\
    \        return res\n\nclass mint(mint):\n    ntt: NTT\n\n    @classmethod\n \
    \   def set_mod(cls, mod: int):\n        super().set_mod(mod)\n        cls.ntt\
    \ = NTT(mod)\n\nclass mlist:\n    def __init__(lst, data): lst.data = [0]*data\
    \ if isinstance(data, int) else [int(x) for x in data]\n    @staticmethod\n  \
    \  def from_raw(data: list[int]):\n        (lst := mlist.__new__(mlist)).data\
    \ = data\n        return lst\n    def __getitem__(lst, i) -> mint: return mint(lst.data[i])\n\
    \    def __setitem__(lst, i, x): lst.data[i] = int(x)\n    def __len__(lst): return\
    \ len(lst.data)\n    def conv(A, B, N):\n        A = A.data\n        B = B.data\
    \ if hasattr(B, 'data') else B\n        return mlist.from_raw(mint.ntt.conv(A,\
    \ B, N))\n\n# Setup modular arithmetic with a common modulus\nMOD = 998244353\n\
    mint.set_mod(MOD)\n\n# Configure benchmark\nconfig = BenchmarkConfig(\n    name=\"\
    mlist\",\n    sizes=[1000000, 100000, 10000, 1000, 100, 10, 1],  # Reverse order\
    \ to warm up JIT\n    operations=['construction', 'addition', 'multiplication',\
    \ 'mixed_ops', 'elementwise_mul', 'sum_all', 'conv'],\n    iterations=10,\n  \
    \  warmup=3,\n    output_dir=\"./output/benchmark_results/mlist\"\n)\n\n# Create\
    \ benchmark instance\nbenchmark = Benchmark(config)\n\n# Data generators\n@benchmark.data_generator(\"\
    default\")\ndef generate_modular_data(size: int, operation: str):\n    \"\"\"\
    Generate test data for modular arithmetic operations\"\"\"\n    # Generate two\
    \ random lists for operations\n    list1 = [random.randint(1, MOD-1) for _ in\
    \ range(size)]\n    list2 = [random.randint(1, MOD-1) for _ in range(size)]\n\
    \    \n    # Pre-initialize data for fair timing (exclude initialization overhead)\n\
    \    preinitialized = {\n        'list1_copy': list(list1),\n        'list2_copy':\
    \ list(list2),\n        'mlist1': mlist(list(list1)),\n        'mlist2': mlist(list(list2)),\n\
    \        'mint_list1': [mint(x) for x in list1],\n        'mint_list2': [mint(x)\
    \ for x in list2],\n        'result_buffer': [0] * size,\n        'mlist_result':\
    \ mlist(size),\n        'constant': 12345,\n        'mint_constant': mint(12345)\n\
    \    }\n    \n    return {\n        'list1': list1,\n        'list2': list2,\n\
    \        'size': size,\n        'operation': operation,\n        'mod': MOD,\n\
    \        'preinitialized': preinitialized\n    }\n\n# Construction operation\n\
    @benchmark.implementation(\"int_list\", \"construction\")\ndef construction_int_list(data):\n\
    \    \"\"\"Construct int list from raw data\"\"\"\n    list1 = list(data['list1'])\n\
    \    list2 = list(data['list2'])\n    checksum = 0\n    for x in list1:\n    \
    \    checksum ^= x\n    for x in list2:\n        checksum ^= x\n    return checksum\n\
    \n@benchmark.implementation(\"mlist\", \"construction\")\ndef construction_mlist(data):\n\
    \    \"\"\"Construct mlist from raw data\"\"\"\n    mlist1 = mlist(data['list1'])\n\
    \    mlist2 = mlist(data['list2'])\n    checksum = 0\n    for x in mlist1.data:\n\
    \        checksum ^= x\n    for x in mlist2.data:\n        checksum ^= x\n   \
    \ return checksum\n\n@benchmark.implementation(\"mint_list\", \"construction\"\
    )\ndef construction_mint_list(data):\n    \"\"\"Construct mint list from raw data\"\
    \"\"\n    mint_list1 = [mint(x) for x in data['list1']]\n    mint_list2 = [mint(x)\
    \ for x in data['list2']]\n    checksum = 0\n    for x in mint_list1:\n      \
    \  checksum ^= x\n    for x in mint_list2:\n        checksum ^= x\n    return\
    \ checksum\n\n# Addition operation\n@benchmark.implementation(\"int_list\", \"\
    addition\")\ndef addition_int_list(data):\n    \"\"\"Element-wise addition with\
    \ manual modulo\"\"\"\n    pre = data['preinitialized']\n    list1, list2, mod\
    \ = pre['list1_copy'], pre['list2_copy'], data['mod']\n    checksum = 0\n    for\
    \ i in range(data['size']):\n        checksum ^= (list1[i] + list2[i]) % mod\n\
    \    return checksum\n\n@benchmark.implementation(\"mlist\", \"addition\")\ndef\
    \ addition_mlist(data):\n    \"\"\"Element-wise addition using mlist\"\"\"\n \
    \   pre = data['preinitialized']\n    list1, list2 = pre['mlist1'], pre['mlist2']\n\
    \    checksum = 0\n    for i in range(data['size']):\n        checksum ^= list1[i]\
    \ + list2[i]\n    return checksum\n\n@benchmark.implementation(\"mint_list\",\
    \ \"addition\")\ndef addition_mint_list(data):\n    \"\"\"Element-wise addition\
    \ using mint list\"\"\"\n    pre = data['preinitialized']\n    list1, list2 =\
    \ pre['mint_list1'], pre['mint_list2']\n    checksum = 0\n    for i in range(data['size']):\n\
    \        checksum ^= list1[i] + list2[i]\n    return checksum\n\n# Multiplication\
    \ operation\n@benchmark.implementation(\"int_list\", \"multiplication\")\ndef\
    \ multiplication_int_list(data):\n    \"\"\"Element-wise multiplication with manual\
    \ modulo\"\"\"\n    pre = data['preinitialized']\n    list1, list2, mod = pre['list1_copy'],\
    \ pre['list2_copy'], data['mod']\n    checksum = 0\n    for i in range(data['size']):\n\
    \        checksum ^= (list1[i] * list2[i]) % mod\n    return checksum\n\n@benchmark.implementation(\"\
    mlist\", \"multiplication\")\ndef multiplication_mlist(data):\n    \"\"\"Element-wise\
    \ multiplication using mlist\"\"\"\n    pre = data['preinitialized']\n    list1,\
    \ list2 = pre['mlist1'], pre['mlist2']\n    checksum = 0\n    for i in range(data['size']):\n\
    \        checksum ^= list1[i] * list2[i]\n    return checksum\n\n@benchmark.implementation(\"\
    mint_list\", \"multiplication\")\ndef multiplication_mint_list(data):\n    \"\"\
    \"Element-wise multiplication using mint list\"\"\"\n    pre = data['preinitialized']\n\
    \    list1, list2 = pre['mint_list1'], pre['mint_list2']\n    checksum = 0\n \
    \   for i in range(data['size']):\n        checksum ^= list1[i] * list2[i]\n \
    \   return checksum\n\n# Mixed operations\n@benchmark.implementation(\"int_list\"\
    , \"mixed_ops\")\ndef mixed_ops_int_list(data):\n    \"\"\"Mix of addition, multiplication,\
    \ and subtraction\"\"\"\n    pre = data['preinitialized']\n    list1, list2, mod\
    \ = pre['list1_copy'], pre['list2_copy'], data['mod']\n    checksum = 0\n    for\
    \ i in range(data['size']):\n        if i % 3 == 0:\n            checksum ^= (list1[i]\
    \ + list2[i]) % mod\n        elif i % 3 == 1:\n            checksum ^= (list1[i]\
    \ * list2[i]) % mod\n        else:\n            checksum ^= (list1[i] - list2[i])\
    \ % mod\n    return checksum\n\n@benchmark.implementation(\"mlist\", \"mixed_ops\"\
    )\ndef mixed_ops_mlist(data):\n    \"\"\"Mix of operations using mlist\"\"\"\n\
    \    pre = data['preinitialized']\n    list1, list2 = pre['mlist1'], pre['mlist2']\n\
    \    checksum = 0\n    for i in range(data['size']):\n        if i % 3 == 0:\n\
    \            checksum ^= list1[i] + list2[i]\n        elif i % 3 == 1:\n     \
    \       checksum ^= list1[i] * list2[i]\n        else:\n            checksum ^=\
    \ list1[i] - list2[i]\n    return checksum\n\n@benchmark.implementation(\"mint_list\"\
    , \"mixed_ops\")\ndef mixed_ops_mint_list(data):\n    \"\"\"Mix of operations\
    \ using mint list\"\"\"\n    pre = data['preinitialized']\n    list1, list2 =\
    \ pre['mint_list1'], pre['mint_list2']\n    checksum = 0\n    for i in range(data['size']):\n\
    \        if i % 3 == 0:\n            checksum ^= list1[i] + list2[i]\n       \
    \ elif i % 3 == 1:\n            checksum ^= list1[i] * list2[i]\n        else:\n\
    \            checksum ^= list1[i] - list2[i]\n    return checksum\n\n\n@benchmark.implementation(\"\
    int_list_e\", \"mixed_ops\")\ndef mixed_ops_int_list(data):\n    \"\"\"Mix of\
    \ addition, multiplication, and subtraction\"\"\"\n    pre = data['preinitialized']\n\
    \    list1, list2, mod = pre['list1_copy'], pre['list2_copy'], data['mod']\n \
    \   checksum = 0\n    for i, x in enumerate(list1):\n        if i % 3 == 0:\n\
    \            checksum ^= (x + list2[i]) % mod\n        elif i % 3 == 1:\n    \
    \        checksum ^= (x * list2[i]) % mod\n        else:\n            checksum\
    \ ^= (x - list2[i]) % mod\n    return checksum\n\n@benchmark.implementation(\"\
    mlist_e\", \"mixed_ops\")\ndef mixed_ops_mlist(data):\n    \"\"\"Mix of operations\
    \ using mlist\"\"\"\n    pre = data['preinitialized']\n    list1, list2 = pre['mlist1'],\
    \ pre['mlist2']\n    checksum = 0\n    for i, x in enumerate(list1):\n       \
    \ if i % 3 == 0:\n            checksum ^= x + list2[i]\n        elif i % 3 ==\
    \ 1:\n            checksum ^= x * list2[i]\n        else:\n            checksum\
    \ ^= x - list2[i]\n    return checksum\n\n@benchmark.implementation(\"mint_list_e\"\
    , \"mixed_ops\")\ndef mixed_ops_mint_list(data):\n    \"\"\"Mix of operations\
    \ using mint list\"\"\"\n    pre = data['preinitialized']\n    list1, list2 =\
    \ pre['mint_list1'], pre['mint_list2']\n    checksum = 0\n    for i, x in enumerate(list1):\n\
    \        if i % 3 == 0:\n            checksum ^= x + list2[i]\n        elif i\
    \ % 3 == 1:\n            checksum ^= x * list2[i]\n        else:\n           \
    \ checksum ^= x - list2[i]\n    return checksum\n\n# Element-wise multiplication\
    \ by constant\n@benchmark.implementation(\"int_list\", \"elementwise_mul\")\n\
    def elementwise_mul_int_list(data):\n    \"\"\"Multiply each element by a constant\"\
    \"\"\n    pre = data['preinitialized']\n    list1, mod, constant = pre['list1_copy'],\
    \ data['mod'], pre['constant']\n    checksum = 0\n    for x in list1:\n      \
    \  checksum ^= (x * constant) % mod\n    return checksum\n\n@benchmark.implementation(\"\
    mlist\", \"elementwise_mul\")\ndef elementwise_mul_mlist(data):\n    \"\"\"Multiply\
    \ each element by a constant using mlist\"\"\"\n    pre = data['preinitialized']\n\
    \    list1, constant = pre['mlist1'], pre['mint_constant']\n    checksum = 0\n\
    \    for x in list1:\n        checksum ^= x * constant\n    return checksum\n\n\
    @benchmark.implementation(\"mint_list\", \"elementwise_mul\")\ndef elementwise_mul_mint_list(data):\n\
    \    \"\"\"Multiply each element by a constant using mint list\"\"\"\n    pre\
    \ = data['preinitialized']\n    list1, constant = pre['mint_list1'], pre['mint_constant']\n\
    \    checksum = 0\n    for x in list1:\n        result = x * constant\n      \
    \  checksum ^= result\n    return checksum\n\n# Sum all elements\n@benchmark.implementation(\"\
    int_list\", \"sum_all\")\ndef sum_all_int_list(data):\n    \"\"\"Sum all elements\"\
    \"\"\n    pre = data['preinitialized']\n    list1, mod = pre['list1_copy'], data['mod']\n\
    \    result = 0\n    for x in list1:\n        result = (result + x) % mod\n  \
    \  return result\n\n@benchmark.implementation(\"mlist\", \"sum_all\")\ndef sum_all_mlist(data):\n\
    \    \"\"\"Sum all elements using mlist\"\"\"\n    pre = data['preinitialized']\n\
    \    list1 = pre['mlist1']\n    result = mint(0)\n    for x in list1:\n      \
    \  result = result + x\n    return int(result)\n\n@benchmark.implementation(\"\
    mint_list\", \"sum_all\")\ndef sum_all_mint_list(data):\n    \"\"\"Sum all elements\
    \ using mint list\"\"\"\n    pre = data['preinitialized']\n    list1 = pre['mint_list1']\n\
    \    result = mint(0)\n    for x in list1:\n        result = result + x\n    return\
    \ int(result)\n\n# Convolution operation\n@benchmark.implementation(\"int_list\"\
    , \"conv\")\ndef conv_int_list(data):\n    \"\"\"Convolution using mint.ntt.conv\
    \ with int lists\"\"\"\n    pre = data['preinitialized']\n    list1, list2 = pre['list1_copy'],\
    \ pre['list2_copy']\n    # Use mint.ntt.conv for convolution\n    result = mint.ntt.conv(list1,\
    \ list2, len(list1) + len(list2) - 1)\n    checksum = 0\n    for x in result:\n\
    \        checksum ^= x\n    return checksum\n\n@benchmark.implementation(\"mlist\"\
    , \"conv\")\ndef conv_mlist(data):\n    \"\"\"Convolution using mlist.conv method\"\
    \"\"\n    pre = data['preinitialized']\n    mlist1, mlist2 = pre['mlist1'], pre['mlist2']\n\
    \    # Use mlist.conv method\n    result = mlist1.conv(mlist2, len(mlist1) + len(mlist2)\
    \ - 1)\n    checksum = 0\n    for x in result.data:\n        checksum ^= x\n \
    \   return checksum\n\n@benchmark.implementation(\"mint_list\", \"conv\")\ndef\
    \ conv_mint_list(data):\n    \"\"\"Convolution using mint.ntt.conv with mint lists\"\
    \"\"\n    pre = data['preinitialized']\n    mint_list1, mint_list2 = pre['mint_list1'],\
    \ pre['mint_list2']\n    # Convert to int lists, convolve, convert back\n    int_list1\
    \ = [int(x) for x in mint_list1]\n    int_list2 = [int(x) for x in mint_list2]\n\
    \    result_ints = mint.ntt.conv(int_list1, int_list2, len(int_list1) + len(int_list2)\
    \ - 1)\n    result = [mint(x) for x in result_ints]\n    checksum = 0\n    for\
    \ x in result:\n        checksum ^= x\n    return checksum\n\n@benchmark.implementation(\"\
    mint_list_direct\", \"conv\")\ndef conv_mint_list_direct(data):\n    \"\"\"Convolution\
    \ using mint.ntt.conv directly with mint lists\"\"\"\n    pre = data['preinitialized']\n\
    \    mint_list1, mint_list2 = pre['mint_list1'], pre['mint_list2']\n    result\
    \ = mint.ntt.conv(mint_list1, mint_list2, len(mint_list1) + len(mint_list2) -\
    \ 1)\n    checksum = 0\n    for x in result:\n        checksum ^= x\n    return\
    \ checksum\n\n# Custom validator for modular arithmetic results (now using XOR\
    \ checksums)\n@benchmark.validator(\"default\")\ndef validate_modular_result(expected,\
    \ actual):\n    \"\"\"Validate modular arithmetic results using XOR checksums\"\
    \"\"\n    try:\n        # Compare XOR checksums directly\n        return int(expected)\
    \ == int(actual)\n    except Exception:\n        return False\n\nif __name__ ==\
    \ \"__main__\":\n    # Parse command line args and run appropriate mode\n    runner\
    \ = benchmark.parse_args()\n    runner.run()\n"
  code: "#!/usr/bin/env python3\n\"\"\"\nComprehensive benchmark comparing modular\
    \ arithmetic approaches on lists:\n1. Plain int list with manual modular operations\n\
    2. mlist_cls (optimized modular list)\n3. List of mint_cls (modular integers)\n\
    \nTests various operations to provide fair comparison across different use cases.\n\
    \"\"\"\n\nimport random\nimport sys\nimport os\nsys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))\n\
    \nfrom cp_library.perf.benchmark import Benchmark, BenchmarkConfig\nfrom cp_library.math.mod.mlist_cls\
    \ import mlist\nfrom cp_library.math.mod.mint_ntt_cls import mint\n\n# Setup modular\
    \ arithmetic with a common modulus\nMOD = 998244353\nmint.set_mod(MOD)\n\n# Configure\
    \ benchmark\nconfig = BenchmarkConfig(\n    name=\"mlist\",\n    sizes=[1000000,\
    \ 100000, 10000, 1000, 100, 10, 1],  # Reverse order to warm up JIT\n    operations=['construction',\
    \ 'addition', 'multiplication', 'mixed_ops', 'elementwise_mul', 'sum_all', 'conv'],\n\
    \    iterations=10,\n    warmup=3,\n    output_dir=\"./output/benchmark_results/mlist\"\
    \n)\n\n# Create benchmark instance\nbenchmark = Benchmark(config)\n\n# Data generators\n\
    @benchmark.data_generator(\"default\")\ndef generate_modular_data(size: int, operation:\
    \ str):\n    \"\"\"Generate test data for modular arithmetic operations\"\"\"\n\
    \    # Generate two random lists for operations\n    list1 = [random.randint(1,\
    \ MOD-1) for _ in range(size)]\n    list2 = [random.randint(1, MOD-1) for _ in\
    \ range(size)]\n    \n    # Pre-initialize data for fair timing (exclude initialization\
    \ overhead)\n    preinitialized = {\n        'list1_copy': list(list1),\n    \
    \    'list2_copy': list(list2),\n        'mlist1': mlist(list(list1)),\n     \
    \   'mlist2': mlist(list(list2)),\n        'mint_list1': [mint(x) for x in list1],\n\
    \        'mint_list2': [mint(x) for x in list2],\n        'result_buffer': [0]\
    \ * size,\n        'mlist_result': mlist(size),\n        'constant': 12345,\n\
    \        'mint_constant': mint(12345)\n    }\n    \n    return {\n        'list1':\
    \ list1,\n        'list2': list2,\n        'size': size,\n        'operation':\
    \ operation,\n        'mod': MOD,\n        'preinitialized': preinitialized\n\
    \    }\n\n# Construction operation\n@benchmark.implementation(\"int_list\", \"\
    construction\")\ndef construction_int_list(data):\n    \"\"\"Construct int list\
    \ from raw data\"\"\"\n    list1 = list(data['list1'])\n    list2 = list(data['list2'])\n\
    \    checksum = 0\n    for x in list1:\n        checksum ^= x\n    for x in list2:\n\
    \        checksum ^= x\n    return checksum\n\n@benchmark.implementation(\"mlist\"\
    , \"construction\")\ndef construction_mlist(data):\n    \"\"\"Construct mlist\
    \ from raw data\"\"\"\n    mlist1 = mlist(data['list1'])\n    mlist2 = mlist(data['list2'])\n\
    \    checksum = 0\n    for x in mlist1.data:\n        checksum ^= x\n    for x\
    \ in mlist2.data:\n        checksum ^= x\n    return checksum\n\n@benchmark.implementation(\"\
    mint_list\", \"construction\")\ndef construction_mint_list(data):\n    \"\"\"\
    Construct mint list from raw data\"\"\"\n    mint_list1 = [mint(x) for x in data['list1']]\n\
    \    mint_list2 = [mint(x) for x in data['list2']]\n    checksum = 0\n    for\
    \ x in mint_list1:\n        checksum ^= x\n    for x in mint_list2:\n        checksum\
    \ ^= x\n    return checksum\n\n# Addition operation\n@benchmark.implementation(\"\
    int_list\", \"addition\")\ndef addition_int_list(data):\n    \"\"\"Element-wise\
    \ addition with manual modulo\"\"\"\n    pre = data['preinitialized']\n    list1,\
    \ list2, mod = pre['list1_copy'], pre['list2_copy'], data['mod']\n    checksum\
    \ = 0\n    for i in range(data['size']):\n        checksum ^= (list1[i] + list2[i])\
    \ % mod\n    return checksum\n\n@benchmark.implementation(\"mlist\", \"addition\"\
    )\ndef addition_mlist(data):\n    \"\"\"Element-wise addition using mlist\"\"\"\
    \n    pre = data['preinitialized']\n    list1, list2 = pre['mlist1'], pre['mlist2']\n\
    \    checksum = 0\n    for i in range(data['size']):\n        checksum ^= list1[i]\
    \ + list2[i]\n    return checksum\n\n@benchmark.implementation(\"mint_list\",\
    \ \"addition\")\ndef addition_mint_list(data):\n    \"\"\"Element-wise addition\
    \ using mint list\"\"\"\n    pre = data['preinitialized']\n    list1, list2 =\
    \ pre['mint_list1'], pre['mint_list2']\n    checksum = 0\n    for i in range(data['size']):\n\
    \        checksum ^= list1[i] + list2[i]\n    return checksum\n\n# Multiplication\
    \ operation\n@benchmark.implementation(\"int_list\", \"multiplication\")\ndef\
    \ multiplication_int_list(data):\n    \"\"\"Element-wise multiplication with manual\
    \ modulo\"\"\"\n    pre = data['preinitialized']\n    list1, list2, mod = pre['list1_copy'],\
    \ pre['list2_copy'], data['mod']\n    checksum = 0\n    for i in range(data['size']):\n\
    \        checksum ^= (list1[i] * list2[i]) % mod\n    return checksum\n\n@benchmark.implementation(\"\
    mlist\", \"multiplication\")\ndef multiplication_mlist(data):\n    \"\"\"Element-wise\
    \ multiplication using mlist\"\"\"\n    pre = data['preinitialized']\n    list1,\
    \ list2 = pre['mlist1'], pre['mlist2']\n    checksum = 0\n    for i in range(data['size']):\n\
    \        checksum ^= list1[i] * list2[i]\n    return checksum\n\n@benchmark.implementation(\"\
    mint_list\", \"multiplication\")\ndef multiplication_mint_list(data):\n    \"\"\
    \"Element-wise multiplication using mint list\"\"\"\n    pre = data['preinitialized']\n\
    \    list1, list2 = pre['mint_list1'], pre['mint_list2']\n    checksum = 0\n \
    \   for i in range(data['size']):\n        checksum ^= list1[i] * list2[i]\n \
    \   return checksum\n\n# Mixed operations\n@benchmark.implementation(\"int_list\"\
    , \"mixed_ops\")\ndef mixed_ops_int_list(data):\n    \"\"\"Mix of addition, multiplication,\
    \ and subtraction\"\"\"\n    pre = data['preinitialized']\n    list1, list2, mod\
    \ = pre['list1_copy'], pre['list2_copy'], data['mod']\n    checksum = 0\n    for\
    \ i in range(data['size']):\n        if i % 3 == 0:\n            checksum ^= (list1[i]\
    \ + list2[i]) % mod\n        elif i % 3 == 1:\n            checksum ^= (list1[i]\
    \ * list2[i]) % mod\n        else:\n            checksum ^= (list1[i] - list2[i])\
    \ % mod\n    return checksum\n\n@benchmark.implementation(\"mlist\", \"mixed_ops\"\
    )\ndef mixed_ops_mlist(data):\n    \"\"\"Mix of operations using mlist\"\"\"\n\
    \    pre = data['preinitialized']\n    list1, list2 = pre['mlist1'], pre['mlist2']\n\
    \    checksum = 0\n    for i in range(data['size']):\n        if i % 3 == 0:\n\
    \            checksum ^= list1[i] + list2[i]\n        elif i % 3 == 1:\n     \
    \       checksum ^= list1[i] * list2[i]\n        else:\n            checksum ^=\
    \ list1[i] - list2[i]\n    return checksum\n\n@benchmark.implementation(\"mint_list\"\
    , \"mixed_ops\")\ndef mixed_ops_mint_list(data):\n    \"\"\"Mix of operations\
    \ using mint list\"\"\"\n    pre = data['preinitialized']\n    list1, list2 =\
    \ pre['mint_list1'], pre['mint_list2']\n    checksum = 0\n    for i in range(data['size']):\n\
    \        if i % 3 == 0:\n            checksum ^= list1[i] + list2[i]\n       \
    \ elif i % 3 == 1:\n            checksum ^= list1[i] * list2[i]\n        else:\n\
    \            checksum ^= list1[i] - list2[i]\n    return checksum\n\n\n@benchmark.implementation(\"\
    int_list_e\", \"mixed_ops\")\ndef mixed_ops_int_list(data):\n    \"\"\"Mix of\
    \ addition, multiplication, and subtraction\"\"\"\n    pre = data['preinitialized']\n\
    \    list1, list2, mod = pre['list1_copy'], pre['list2_copy'], data['mod']\n \
    \   checksum = 0\n    for i, x in enumerate(list1):\n        if i % 3 == 0:\n\
    \            checksum ^= (x + list2[i]) % mod\n        elif i % 3 == 1:\n    \
    \        checksum ^= (x * list2[i]) % mod\n        else:\n            checksum\
    \ ^= (x - list2[i]) % mod\n    return checksum\n\n@benchmark.implementation(\"\
    mlist_e\", \"mixed_ops\")\ndef mixed_ops_mlist(data):\n    \"\"\"Mix of operations\
    \ using mlist\"\"\"\n    pre = data['preinitialized']\n    list1, list2 = pre['mlist1'],\
    \ pre['mlist2']\n    checksum = 0\n    for i, x in enumerate(list1):\n       \
    \ if i % 3 == 0:\n            checksum ^= x + list2[i]\n        elif i % 3 ==\
    \ 1:\n            checksum ^= x * list2[i]\n        else:\n            checksum\
    \ ^= x - list2[i]\n    return checksum\n\n@benchmark.implementation(\"mint_list_e\"\
    , \"mixed_ops\")\ndef mixed_ops_mint_list(data):\n    \"\"\"Mix of operations\
    \ using mint list\"\"\"\n    pre = data['preinitialized']\n    list1, list2 =\
    \ pre['mint_list1'], pre['mint_list2']\n    checksum = 0\n    for i, x in enumerate(list1):\n\
    \        if i % 3 == 0:\n            checksum ^= x + list2[i]\n        elif i\
    \ % 3 == 1:\n            checksum ^= x * list2[i]\n        else:\n           \
    \ checksum ^= x - list2[i]\n    return checksum\n\n# Element-wise multiplication\
    \ by constant\n@benchmark.implementation(\"int_list\", \"elementwise_mul\")\n\
    def elementwise_mul_int_list(data):\n    \"\"\"Multiply each element by a constant\"\
    \"\"\n    pre = data['preinitialized']\n    list1, mod, constant = pre['list1_copy'],\
    \ data['mod'], pre['constant']\n    checksum = 0\n    for x in list1:\n      \
    \  checksum ^= (x * constant) % mod\n    return checksum\n\n@benchmark.implementation(\"\
    mlist\", \"elementwise_mul\")\ndef elementwise_mul_mlist(data):\n    \"\"\"Multiply\
    \ each element by a constant using mlist\"\"\"\n    pre = data['preinitialized']\n\
    \    list1, constant = pre['mlist1'], pre['mint_constant']\n    checksum = 0\n\
    \    for x in list1:\n        checksum ^= x * constant\n    return checksum\n\n\
    @benchmark.implementation(\"mint_list\", \"elementwise_mul\")\ndef elementwise_mul_mint_list(data):\n\
    \    \"\"\"Multiply each element by a constant using mint list\"\"\"\n    pre\
    \ = data['preinitialized']\n    list1, constant = pre['mint_list1'], pre['mint_constant']\n\
    \    checksum = 0\n    for x in list1:\n        result = x * constant\n      \
    \  checksum ^= result\n    return checksum\n\n# Sum all elements\n@benchmark.implementation(\"\
    int_list\", \"sum_all\")\ndef sum_all_int_list(data):\n    \"\"\"Sum all elements\"\
    \"\"\n    pre = data['preinitialized']\n    list1, mod = pre['list1_copy'], data['mod']\n\
    \    result = 0\n    for x in list1:\n        result = (result + x) % mod\n  \
    \  return result\n\n@benchmark.implementation(\"mlist\", \"sum_all\")\ndef sum_all_mlist(data):\n\
    \    \"\"\"Sum all elements using mlist\"\"\"\n    pre = data['preinitialized']\n\
    \    list1 = pre['mlist1']\n    result = mint(0)\n    for x in list1:\n      \
    \  result = result + x\n    return int(result)\n\n@benchmark.implementation(\"\
    mint_list\", \"sum_all\")\ndef sum_all_mint_list(data):\n    \"\"\"Sum all elements\
    \ using mint list\"\"\"\n    pre = data['preinitialized']\n    list1 = pre['mint_list1']\n\
    \    result = mint(0)\n    for x in list1:\n        result = result + x\n    return\
    \ int(result)\n\n# Convolution operation\n@benchmark.implementation(\"int_list\"\
    , \"conv\")\ndef conv_int_list(data):\n    \"\"\"Convolution using mint.ntt.conv\
    \ with int lists\"\"\"\n    pre = data['preinitialized']\n    list1, list2 = pre['list1_copy'],\
    \ pre['list2_copy']\n    # Use mint.ntt.conv for convolution\n    result = mint.ntt.conv(list1,\
    \ list2, len(list1) + len(list2) - 1)\n    checksum = 0\n    for x in result:\n\
    \        checksum ^= x\n    return checksum\n\n@benchmark.implementation(\"mlist\"\
    , \"conv\")\ndef conv_mlist(data):\n    \"\"\"Convolution using mlist.conv method\"\
    \"\"\n    pre = data['preinitialized']\n    mlist1, mlist2 = pre['mlist1'], pre['mlist2']\n\
    \    # Use mlist.conv method\n    result = mlist1.conv(mlist2, len(mlist1) + len(mlist2)\
    \ - 1)\n    checksum = 0\n    for x in result.data:\n        checksum ^= x\n \
    \   return checksum\n\n@benchmark.implementation(\"mint_list\", \"conv\")\ndef\
    \ conv_mint_list(data):\n    \"\"\"Convolution using mint.ntt.conv with mint lists\"\
    \"\"\n    pre = data['preinitialized']\n    mint_list1, mint_list2 = pre['mint_list1'],\
    \ pre['mint_list2']\n    # Convert to int lists, convolve, convert back\n    int_list1\
    \ = [int(x) for x in mint_list1]\n    int_list2 = [int(x) for x in mint_list2]\n\
    \    result_ints = mint.ntt.conv(int_list1, int_list2, len(int_list1) + len(int_list2)\
    \ - 1)\n    result = [mint(x) for x in result_ints]\n    checksum = 0\n    for\
    \ x in result:\n        checksum ^= x\n    return checksum\n\n@benchmark.implementation(\"\
    mint_list_direct\", \"conv\")\ndef conv_mint_list_direct(data):\n    \"\"\"Convolution\
    \ using mint.ntt.conv directly with mint lists\"\"\"\n    pre = data['preinitialized']\n\
    \    mint_list1, mint_list2 = pre['mint_list1'], pre['mint_list2']\n    result\
    \ = mint.ntt.conv(mint_list1, mint_list2, len(mint_list1) + len(mint_list2) -\
    \ 1)\n    checksum = 0\n    for x in result:\n        checksum ^= x\n    return\
    \ checksum\n\n# Custom validator for modular arithmetic results (now using XOR\
    \ checksums)\n@benchmark.validator(\"default\")\ndef validate_modular_result(expected,\
    \ actual):\n    \"\"\"Validate modular arithmetic results using XOR checksums\"\
    \"\"\n    try:\n        # Compare XOR checksums directly\n        return int(expected)\
    \ == int(actual)\n    except Exception:\n        return False\n\nif __name__ ==\
    \ \"__main__\":\n    # Parse command line args and run appropriate mode\n    runner\
    \ = benchmark.parse_args()\n    runner.run()"
  dependsOn:
  - cp_library/perf/benchmark.py
  - cp_library/math/mod/mlist_cls.py
  - cp_library/math/mod/mint_ntt_cls.py
  - cp_library/math/mod/mint_cls.py
  - cp_library/math/nt/ntt_cls.py
  - cp_library/math/nt/mod_inv_fn.py
  isVerificationFile: false
  path: perf/mlist.py
  requiredBy: []
  timestamp: '2025-07-20 06:26:01+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: perf/mlist.py
layout: document
redirect_from:
- /library/perf/mlist.py
- /library/perf/mlist.py.html
title: perf/mlist.py
---
