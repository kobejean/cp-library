---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "#!/usr/bin/env python3\n\"\"\"\nPerformance benchmark runner for cp-library.\n\
    \nThis script makes it easy to run all performance benchmarks or specific subsets.\n\
    \"\"\"\n\nimport os\nimport sys\nimport argparse\nimport subprocess\nimport time\n\
    from pathlib import Path\nfrom typing import List, Optional\n\n\nclass BenchmarkRunner:\n\
    \    \"\"\"Runner for performance benchmarks\"\"\"\n    \n    def __init__(self):\n\
    \        self.script_dir = Path(__file__).parent\n        self.perf_dir = self.script_dir\
    \ / \"perf\"\n        self.benchmark_files = self._discover_benchmarks()\n   \
    \ \n    def _discover_benchmarks(self) -> List[Path]:\n        \"\"\"Discover\
    \ all benchmark files in the perf directory\"\"\"\n        benchmark_files = []\n\
    \        for file_path in self.perf_dir.glob(\"*.py\"):\n            # Skip module\
    \ files and framework files\n            if file_path.name.startswith(\"__\")\
    \ or file_path.name in {\n                \"benchmark.py\", \"interfaces.py\"\
    , \"registry.py\", \"orchestrator.py\", \n                \"timing.py\", \"output.py\"\
    , \"renderers.py\", \"cli.py\", \"checksum.py\", \"plotting.py\"\n           \
    \ }:\n                continue\n            benchmark_files.append(file_path)\n\
    \        \n        return sorted(benchmark_files)\n    \n    def list_benchmarks(self):\n\
    \        \"\"\"List all available benchmarks\"\"\"\n        print(\"Available\
    \ benchmarks:\")\n        print(\"=\" * 50)\n        for i, benchmark in enumerate(self.benchmark_files,\
    \ 1):\n            print(f\"{i:2d}. {benchmark.stem}\")\n    \n    def run_benchmark(self,\
    \ benchmark_file: Path, operation: Optional[str] = None, \n                  \
    \   size: Optional[int] = None, quiet: bool = False) -> bool:\n        \"\"\"\
    Run a single benchmark file\"\"\"\n        cmd = ['pypy', str(benchmark_file)]\n\
    \        \n        if operation:\n            cmd.extend([\"--operation\", operation])\n\
    \        if size:\n            cmd.extend([\"--size\", str(size)])\n        \n\
    \        if not quiet:\n            print(f\"\\n{'='*60}\")\n            print(f\"\
    Running: {benchmark_file.stem}\")\n            if operation:\n               \
    \ print(f\"Operation: {operation}\")\n            if size:\n                print(f\"\
    Size: {size}\")\n            print('='*60)\n        \n        try:\n         \
    \   result = subprocess.run(\n                cmd, \n                cwd=self.script_dir,\n\
    \                capture_output=quiet,\n                text=True,\n         \
    \       timeout=300  # 5 minute timeout per benchmark\n            )\n       \
    \     \n            if result.returncode == 0:\n                if not quiet:\n\
    \                    print(f\"\u2705 {benchmark_file.stem} completed successfully\"\
    )\n                return True\n            else:\n                print(f\"\u274C\
    \ {benchmark_file.stem} failed with return code {result.returncode}\")\n     \
    \           if quiet and result.stderr:\n                    print(f\"Error: {result.stderr}\"\
    )\n                return False\n                \n        except subprocess.TimeoutExpired:\n\
    \            print(f\"\u23F0 {benchmark_file.stem} timed out after 5 minutes\"\
    )\n            return False\n        except Exception as e:\n            print(f\"\
    \U0001F4A5 {benchmark_file.stem} crashed: {e}\")\n            return False\n \
    \   \n    def run_all(self, operation: Optional[str] = None, size: Optional[int]\
    \ = None, \n                quiet: bool = False, fast: bool = False):\n      \
    \  \"\"\"Run all benchmarks\"\"\"\n        if fast:\n            # Fast mode:\
    \ smaller sizes and fewer iterations\n            if not size:\n             \
    \   size = 1000\n        \n        print(f\"Running {len(self.benchmark_files)}\
    \ benchmarks...\")\n        if operation:\n            print(f\"Filtering to operation:\
    \ {operation}\")\n        if size:\n            print(f\"Filtering to size: {size}\"\
    )\n        if fast:\n            print(\"Fast mode: using smaller test sizes\"\
    )\n        \n        start_time = time.time()\n        successful = 0\n      \
    \  failed = 0\n        \n        for benchmark in self.benchmark_files:\n    \
    \        success = self.run_benchmark(benchmark, operation, size, quiet)\n   \
    \         if success:\n                successful += 1\n            else:\n  \
    \              failed += 1\n        \n        total_time = time.time() - start_time\n\
    \        \n        print(f\"\\n{'='*60}\")\n        print(f\"BENCHMARK SUMMARY\"\
    )\n        print('='*60)\n        print(f\"Total benchmarks: {len(self.benchmark_files)}\"\
    )\n        print(f\"Successful: {successful}\")\n        print(f\"Failed: {failed}\"\
    )\n        print(f\"Total time: {total_time:.1f} seconds\")\n        \n      \
    \  if failed > 0:\n            print(f\"\\n\u274C {failed} benchmarks failed\"\
    )\n            sys.exit(1)\n        else:\n            print(f\"\\n\u2705 All\
    \ benchmarks completed successfully!\")\n    \n    def run_specific(self, names:\
    \ List[str], operation: Optional[str] = None, \n                    size: Optional[int]\
    \ = None, quiet: bool = False):\n        \"\"\"Run specific benchmarks by name\"\
    \"\"\n        benchmarks_to_run = []\n        \n        for name in names:\n \
    \           # Try exact match first\n            matching = [b for b in self.benchmark_files\
    \ if b.stem == name]\n            if not matching:\n                # Try partial\
    \ match\n                matching = [b for b in self.benchmark_files if name.lower()\
    \ in b.stem.lower()]\n            \n            if matching:\n               \
    \ benchmarks_to_run.extend(matching)\n            else:\n                print(f\"\
    \u274C No benchmark found matching '{name}'\")\n                return False\n\
    \        \n        # Remove duplicates while preserving order\n        benchmarks_to_run\
    \ = list(dict.fromkeys(benchmarks_to_run))\n        \n        print(f\"Running\
    \ {len(benchmarks_to_run)} benchmark(s)...\")\n        \n        successful =\
    \ 0\n        failed = 0\n        \n        for benchmark in benchmarks_to_run:\n\
    \            success = self.run_benchmark(benchmark, operation, size, quiet)\n\
    \            if success:\n                successful += 1\n            else:\n\
    \                failed += 1\n        \n        print(f\"\\n{'='*40}\")\n    \
    \    print(f\"Results: {successful} successful, {failed} failed\")\n        \n\
    \        return failed == 0\n\n\ndef main():\n    parser = argparse.ArgumentParser(\n\
    \        description=\"Run performance benchmarks for cp-library\",\n        formatter_class=argparse.RawDescriptionHelpFormatter,\n\
    \        epilog=\"\"\"\nExamples:\n  # List all available benchmarks\n  python\
    \ run_benchmarks.py --list\n  \n  # Run all benchmarks\n  python run_benchmarks.py\
    \ --all\n  \n  # Run all benchmarks quickly with smaller sizes\n  python run_benchmarks.py\
    \ --all --fast\n  \n  # Run specific benchmarks\n  python run_benchmarks.py que\
    \ deque segtree2\n  \n  # Run benchmarks with specific operation\n  python run_benchmarks.py\
    \ --all --operation construction\n  \n  # Run benchmarks with specific size\n\
    \  python run_benchmarks.py --all --size 1000\n  \n  # Run quietly (less output)\n\
    \  python run_benchmarks.py --all --quiet\n\"\"\"\n    )\n    \n    parser.add_argument(\"\
    benchmarks\", nargs=\"*\", \n                       help=\"Specific benchmark\
    \ names to run (e.g., 'que', 'segtree2')\")\n    parser.add_argument(\"--list\"\
    , action=\"store_true\",\n                       help=\"List all available benchmarks\"\
    )\n    parser.add_argument(\"--all\", action=\"store_true\",\n               \
    \        help=\"Run all benchmarks\")\n    parser.add_argument(\"--operation\"\
    , type=str,\n                       help=\"Filter to specific operation\")\n \
    \   parser.add_argument(\"--size\", type=int,\n                       help=\"\
    Filter to specific size\")\n    parser.add_argument(\"--quiet\", action=\"store_true\"\
    ,\n                       help=\"Reduce output (show only summaries)\")\n    parser.add_argument(\"\
    --fast\", action=\"store_true\",\n                       help=\"Fast mode: use\
    \ smaller test sizes\")\n    \n    args = parser.parse_args()\n    \n    runner\
    \ = BenchmarkRunner()\n    \n    if args.list:\n        runner.list_benchmarks()\n\
    \    elif args.all:\n        runner.run_all(args.operation, args.size, args.quiet,\
    \ args.fast)\n    elif args.benchmarks:\n        success = runner.run_specific(args.benchmarks,\
    \ args.operation, args.size, args.quiet)\n        if not success:\n          \
    \  sys.exit(1)\n    else:\n        parser.print_help()\n\n\nif __name__ == \"\
    __main__\":\n    main()\n"
  code: "#!/usr/bin/env python3\n\"\"\"\nPerformance benchmark runner for cp-library.\n\
    \nThis script makes it easy to run all performance benchmarks or specific subsets.\n\
    \"\"\"\n\nimport os\nimport sys\nimport argparse\nimport subprocess\nimport time\n\
    from pathlib import Path\nfrom typing import List, Optional\n\n\nclass BenchmarkRunner:\n\
    \    \"\"\"Runner for performance benchmarks\"\"\"\n    \n    def __init__(self):\n\
    \        self.script_dir = Path(__file__).parent\n        self.perf_dir = self.script_dir\
    \ / \"perf\"\n        self.benchmark_files = self._discover_benchmarks()\n   \
    \ \n    def _discover_benchmarks(self) -> List[Path]:\n        \"\"\"Discover\
    \ all benchmark files in the perf directory\"\"\"\n        benchmark_files = []\n\
    \        for file_path in self.perf_dir.glob(\"*.py\"):\n            # Skip module\
    \ files and framework files\n            if file_path.name.startswith(\"__\")\
    \ or file_path.name in {\n                \"benchmark.py\", \"interfaces.py\"\
    , \"registry.py\", \"orchestrator.py\", \n                \"timing.py\", \"output.py\"\
    , \"renderers.py\", \"cli.py\", \"checksum.py\", \"plotting.py\"\n           \
    \ }:\n                continue\n            benchmark_files.append(file_path)\n\
    \        \n        return sorted(benchmark_files)\n    \n    def list_benchmarks(self):\n\
    \        \"\"\"List all available benchmarks\"\"\"\n        print(\"Available\
    \ benchmarks:\")\n        print(\"=\" * 50)\n        for i, benchmark in enumerate(self.benchmark_files,\
    \ 1):\n            print(f\"{i:2d}. {benchmark.stem}\")\n    \n    def run_benchmark(self,\
    \ benchmark_file: Path, operation: Optional[str] = None, \n                  \
    \   size: Optional[int] = None, quiet: bool = False) -> bool:\n        \"\"\"\
    Run a single benchmark file\"\"\"\n        cmd = ['pypy', str(benchmark_file)]\n\
    \        \n        if operation:\n            cmd.extend([\"--operation\", operation])\n\
    \        if size:\n            cmd.extend([\"--size\", str(size)])\n        \n\
    \        if not quiet:\n            print(f\"\\n{'='*60}\")\n            print(f\"\
    Running: {benchmark_file.stem}\")\n            if operation:\n               \
    \ print(f\"Operation: {operation}\")\n            if size:\n                print(f\"\
    Size: {size}\")\n            print('='*60)\n        \n        try:\n         \
    \   result = subprocess.run(\n                cmd, \n                cwd=self.script_dir,\n\
    \                capture_output=quiet,\n                text=True,\n         \
    \       timeout=300  # 5 minute timeout per benchmark\n            )\n       \
    \     \n            if result.returncode == 0:\n                if not quiet:\n\
    \                    print(f\"\u2705 {benchmark_file.stem} completed successfully\"\
    )\n                return True\n            else:\n                print(f\"\u274C\
    \ {benchmark_file.stem} failed with return code {result.returncode}\")\n     \
    \           if quiet and result.stderr:\n                    print(f\"Error: {result.stderr}\"\
    )\n                return False\n                \n        except subprocess.TimeoutExpired:\n\
    \            print(f\"\u23F0 {benchmark_file.stem} timed out after 5 minutes\"\
    )\n            return False\n        except Exception as e:\n            print(f\"\
    \U0001F4A5 {benchmark_file.stem} crashed: {e}\")\n            return False\n \
    \   \n    def run_all(self, operation: Optional[str] = None, size: Optional[int]\
    \ = None, \n                quiet: bool = False, fast: bool = False):\n      \
    \  \"\"\"Run all benchmarks\"\"\"\n        if fast:\n            # Fast mode:\
    \ smaller sizes and fewer iterations\n            if not size:\n             \
    \   size = 1000\n        \n        print(f\"Running {len(self.benchmark_files)}\
    \ benchmarks...\")\n        if operation:\n            print(f\"Filtering to operation:\
    \ {operation}\")\n        if size:\n            print(f\"Filtering to size: {size}\"\
    )\n        if fast:\n            print(\"Fast mode: using smaller test sizes\"\
    )\n        \n        start_time = time.time()\n        successful = 0\n      \
    \  failed = 0\n        \n        for benchmark in self.benchmark_files:\n    \
    \        success = self.run_benchmark(benchmark, operation, size, quiet)\n   \
    \         if success:\n                successful += 1\n            else:\n  \
    \              failed += 1\n        \n        total_time = time.time() - start_time\n\
    \        \n        print(f\"\\n{'='*60}\")\n        print(f\"BENCHMARK SUMMARY\"\
    )\n        print('='*60)\n        print(f\"Total benchmarks: {len(self.benchmark_files)}\"\
    )\n        print(f\"Successful: {successful}\")\n        print(f\"Failed: {failed}\"\
    )\n        print(f\"Total time: {total_time:.1f} seconds\")\n        \n      \
    \  if failed > 0:\n            print(f\"\\n\u274C {failed} benchmarks failed\"\
    )\n            sys.exit(1)\n        else:\n            print(f\"\\n\u2705 All\
    \ benchmarks completed successfully!\")\n    \n    def run_specific(self, names:\
    \ List[str], operation: Optional[str] = None, \n                    size: Optional[int]\
    \ = None, quiet: bool = False):\n        \"\"\"Run specific benchmarks by name\"\
    \"\"\n        benchmarks_to_run = []\n        \n        for name in names:\n \
    \           # Try exact match first\n            matching = [b for b in self.benchmark_files\
    \ if b.stem == name]\n            if not matching:\n                # Try partial\
    \ match\n                matching = [b for b in self.benchmark_files if name.lower()\
    \ in b.stem.lower()]\n            \n            if matching:\n               \
    \ benchmarks_to_run.extend(matching)\n            else:\n                print(f\"\
    \u274C No benchmark found matching '{name}'\")\n                return False\n\
    \        \n        # Remove duplicates while preserving order\n        benchmarks_to_run\
    \ = list(dict.fromkeys(benchmarks_to_run))\n        \n        print(f\"Running\
    \ {len(benchmarks_to_run)} benchmark(s)...\")\n        \n        successful =\
    \ 0\n        failed = 0\n        \n        for benchmark in benchmarks_to_run:\n\
    \            success = self.run_benchmark(benchmark, operation, size, quiet)\n\
    \            if success:\n                successful += 1\n            else:\n\
    \                failed += 1\n        \n        print(f\"\\n{'='*40}\")\n    \
    \    print(f\"Results: {successful} successful, {failed} failed\")\n        \n\
    \        return failed == 0\n\n\ndef main():\n    parser = argparse.ArgumentParser(\n\
    \        description=\"Run performance benchmarks for cp-library\",\n        formatter_class=argparse.RawDescriptionHelpFormatter,\n\
    \        epilog=\"\"\"\nExamples:\n  # List all available benchmarks\n  python\
    \ run_benchmarks.py --list\n  \n  # Run all benchmarks\n  python run_benchmarks.py\
    \ --all\n  \n  # Run all benchmarks quickly with smaller sizes\n  python run_benchmarks.py\
    \ --all --fast\n  \n  # Run specific benchmarks\n  python run_benchmarks.py que\
    \ deque segtree2\n  \n  # Run benchmarks with specific operation\n  python run_benchmarks.py\
    \ --all --operation construction\n  \n  # Run benchmarks with specific size\n\
    \  python run_benchmarks.py --all --size 1000\n  \n  # Run quietly (less output)\n\
    \  python run_benchmarks.py --all --quiet\n\"\"\"\n    )\n    \n    parser.add_argument(\"\
    benchmarks\", nargs=\"*\", \n                       help=\"Specific benchmark\
    \ names to run (e.g., 'que', 'segtree2')\")\n    parser.add_argument(\"--list\"\
    , action=\"store_true\",\n                       help=\"List all available benchmarks\"\
    )\n    parser.add_argument(\"--all\", action=\"store_true\",\n               \
    \        help=\"Run all benchmarks\")\n    parser.add_argument(\"--operation\"\
    , type=str,\n                       help=\"Filter to specific operation\")\n \
    \   parser.add_argument(\"--size\", type=int,\n                       help=\"\
    Filter to specific size\")\n    parser.add_argument(\"--quiet\", action=\"store_true\"\
    ,\n                       help=\"Reduce output (show only summaries)\")\n    parser.add_argument(\"\
    --fast\", action=\"store_true\",\n                       help=\"Fast mode: use\
    \ smaller test sizes\")\n    \n    args = parser.parse_args()\n    \n    runner\
    \ = BenchmarkRunner()\n    \n    if args.list:\n        runner.list_benchmarks()\n\
    \    elif args.all:\n        runner.run_all(args.operation, args.size, args.quiet,\
    \ args.fast)\n    elif args.benchmarks:\n        success = runner.run_specific(args.benchmarks,\
    \ args.operation, args.size, args.quiet)\n        if not success:\n          \
    \  sys.exit(1)\n    else:\n        parser.print_help()\n\n\nif __name__ == \"\
    __main__\":\n    main()"
  dependsOn: []
  isVerificationFile: false
  path: run_benchmarks.py
  requiredBy: []
  timestamp: '2025-07-26 11:14:31+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: run_benchmarks.py
layout: document
redirect_from:
- /library/run_benchmarks.py
- /library/run_benchmarks.py.html
title: run_benchmarks.py
---
