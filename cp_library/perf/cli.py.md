---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':warning:'
    path: cp_library/perf/benchmark.py
    title: cp_library/perf/benchmark.py
  - icon: ':warning:'
    path: perf/bit2.py
    title: perf/bit2.py
  - icon: ':warning:'
    path: perf/bit6.py
    title: perf/bit6.py
  - icon: ':warning:'
    path: perf/bool_list.py
    title: perf/bool_list.py
  - icon: ':warning:'
    path: perf/bytearray_decode.py
    title: perf/bytearray_decode.py
  - icon: ':warning:'
    path: perf/csr.py
    title: perf/csr.py
  - icon: ':warning:'
    path: perf/csr2.py
    title: perf/csr2.py
  - icon: ':warning:'
    path: perf/csr6.py
    title: perf/csr6.py
  - icon: ':warning:'
    path: perf/deque.py
    title: perf/deque.py
  - icon: ':warning:'
    path: perf/edge_list.py
    title: perf/edge_list.py
  - icon: ':warning:'
    path: perf/grid.py
    title: perf/grid.py
  - icon: ':warning:'
    path: perf/heap_csr.py
    title: perf/heap_csr.py
  - icon: ':warning:'
    path: perf/heap_view.py
    title: perf/heap_view.py
  - icon: ':warning:'
    path: perf/list2.py
    title: perf/list2.py
  - icon: ':warning:'
    path: perf/list6.py
    title: perf/list6.py
  - icon: ':warning:'
    path: perf/list_view.py
    title: perf/list_view.py
  - icon: ':warning:'
    path: perf/mlist.py
    title: perf/mlist.py
  - icon: ':warning:'
    path: perf/que.py
    title: perf/que.py
  - icon: ':warning:'
    path: perf/rank.py
    title: perf/rank.py
  - icon: ':warning:'
    path: perf/segtree2.py
    title: perf/segtree2.py
  - icon: ':warning:'
    path: perf/segtree6.py
    title: perf/segtree6.py
  - icon: ':warning:'
    path: perf/view2.py
    title: perf/view2.py
  - icon: ':warning:'
    path: perf/view6.py
    title: perf/view6.py
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "\"\"\"\nCommand-line interface for the benchmark framework.\n\"\"\"\
    \n\nimport argparse\nimport sys\nfrom typing import List, Optional\nfrom dataclasses\
    \ import dataclass\n\n\n@dataclass\nclass CLIConfig:\n    \"\"\"Configuration\
    \ parsed from command line arguments\"\"\"\n    profile_mode: bool = False\n \
    \   operation: Optional[str] = None\n    size: Optional[int] = None\n    implementation:\
    \ Optional[str] = None\n\n\nclass BenchmarkCLI:\n    \"\"\"Command-line interface\
    \ handler\"\"\"\n    \n    def __init__(self, name: str, operations: List[str],\
    \ sizes: List[int]):\n        self.name = name\n        self.operations = operations\n\
    \        self.sizes = sizes\n    \n    def parse_args(self) -> CLIConfig:\n  \
    \      \"\"\"Parse command line arguments\"\"\"\n        parser = argparse.ArgumentParser(\n\
    \            description=f\"Benchmark {self.name} with optional profiling mode\"\
    ,\n            formatter_class=argparse.RawDescriptionHelpFormatter,\n       \
    \     epilog=\"\"\"\nExamples:\n  # Normal benchmark mode (all operations and\
    \ sizes)\n  python benchmark.py\n  \n  # Normal mode with specific operation\n\
    \  python benchmark.py --operation access\n  \n  # Normal mode with specific size\n\
    \  python benchmark.py --size 1000\n  \n  # Normal mode with specific operation\
    \ and size\n  python benchmark.py --operation access --size 100\n  \n  # Profile\
    \ specific operation and implementation\n  python benchmark.py --profile --operation\
    \ random_access --implementation grid\n  \n  # Profile with specific size\n  python\
    \ benchmark.py --profile --size 1000000\n\"\"\"\n        )\n        \n       \
    \ parser.add_argument('--profile', action='store_true',\n                    \
    \      help='Run in profiling mode (minimal overhead for profilers)')\n      \
    \  parser.add_argument('--operation', type=str, \n                          help=f'Filter\
    \ to specific operation. Options: {\", \".join(self.operations)}')\n        parser.add_argument('--size',\
    \ type=int,\n                          help=f'Filter to specific size. Options:\
    \ {\", \".join(map(str, self.sizes))}')\n        parser.add_argument('--implementation',\
    \ type=str,\n                          help='Specific implementation (profile\
    \ mode only)')\n        \n        args = parser.parse_args()\n        \n     \
    \   return CLIConfig(\n            profile_mode=args.profile,\n            operation=args.operation,\n\
    \            size=args.size,\n            implementation=args.implementation\n\
    \        )\n    \n    def validate_args(self, config: CLIConfig) -> None:\n  \
    \      \"\"\"Validate command line arguments\"\"\"\n        if config.operation\
    \ and config.operation not in self.operations:\n            print(f\"Error: Unknown\
    \ operation '{config.operation}'\")\n            print(f\"Available operations:\
    \ {', '.join(self.operations)}\")\n            sys.exit(1)\n        \n       \
    \ if config.size and config.size not in self.sizes:\n            print(f\"Error:\
    \ Unknown size '{config.size}'\")\n            print(f\"Available sizes: {', '.join(map(str,\
    \ self.sizes))}\")\n            sys.exit(1)\n"
  code: "\"\"\"\nCommand-line interface for the benchmark framework.\n\"\"\"\n\nimport\
    \ argparse\nimport sys\nfrom typing import List, Optional\nfrom dataclasses import\
    \ dataclass\n\n\n@dataclass\nclass CLIConfig:\n    \"\"\"Configuration parsed\
    \ from command line arguments\"\"\"\n    profile_mode: bool = False\n    operation:\
    \ Optional[str] = None\n    size: Optional[int] = None\n    implementation: Optional[str]\
    \ = None\n\n\nclass BenchmarkCLI:\n    \"\"\"Command-line interface handler\"\"\
    \"\n    \n    def __init__(self, name: str, operations: List[str], sizes: List[int]):\n\
    \        self.name = name\n        self.operations = operations\n        self.sizes\
    \ = sizes\n    \n    def parse_args(self) -> CLIConfig:\n        \"\"\"Parse command\
    \ line arguments\"\"\"\n        parser = argparse.ArgumentParser(\n          \
    \  description=f\"Benchmark {self.name} with optional profiling mode\",\n    \
    \        formatter_class=argparse.RawDescriptionHelpFormatter,\n            epilog=\"\
    \"\"\nExamples:\n  # Normal benchmark mode (all operations and sizes)\n  python\
    \ benchmark.py\n  \n  # Normal mode with specific operation\n  python benchmark.py\
    \ --operation access\n  \n  # Normal mode with specific size\n  python benchmark.py\
    \ --size 1000\n  \n  # Normal mode with specific operation and size\n  python\
    \ benchmark.py --operation access --size 100\n  \n  # Profile specific operation\
    \ and implementation\n  python benchmark.py --profile --operation random_access\
    \ --implementation grid\n  \n  # Profile with specific size\n  python benchmark.py\
    \ --profile --size 1000000\n\"\"\"\n        )\n        \n        parser.add_argument('--profile',\
    \ action='store_true',\n                          help='Run in profiling mode\
    \ (minimal overhead for profilers)')\n        parser.add_argument('--operation',\
    \ type=str, \n                          help=f'Filter to specific operation. Options:\
    \ {\", \".join(self.operations)}')\n        parser.add_argument('--size', type=int,\n\
    \                          help=f'Filter to specific size. Options: {\", \".join(map(str,\
    \ self.sizes))}')\n        parser.add_argument('--implementation', type=str,\n\
    \                          help='Specific implementation (profile mode only)')\n\
    \        \n        args = parser.parse_args()\n        \n        return CLIConfig(\n\
    \            profile_mode=args.profile,\n            operation=args.operation,\n\
    \            size=args.size,\n            implementation=args.implementation\n\
    \        )\n    \n    def validate_args(self, config: CLIConfig) -> None:\n  \
    \      \"\"\"Validate command line arguments\"\"\"\n        if config.operation\
    \ and config.operation not in self.operations:\n            print(f\"Error: Unknown\
    \ operation '{config.operation}'\")\n            print(f\"Available operations:\
    \ {', '.join(self.operations)}\")\n            sys.exit(1)\n        \n       \
    \ if config.size and config.size not in self.sizes:\n            print(f\"Error:\
    \ Unknown size '{config.size}'\")\n            print(f\"Available sizes: {', '.join(map(str,\
    \ self.sizes))}\")\n            sys.exit(1)"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/perf/cli.py
  requiredBy:
  - cp_library/perf/benchmark.py
  - perf/bool_list.py
  - perf/view2.py
  - perf/heap_view.py
  - perf/list_view.py
  - perf/mlist.py
  - perf/que.py
  - perf/list6.py
  - perf/grid.py
  - perf/edge_list.py
  - perf/csr.py
  - perf/bit6.py
  - perf/deque.py
  - perf/segtree2.py
  - perf/view6.py
  - perf/csr6.py
  - perf/segtree6.py
  - perf/csr2.py
  - perf/bit2.py
  - perf/rank.py
  - perf/list2.py
  - perf/heap_csr.py
  - perf/bytearray_decode.py
  timestamp: '2025-07-28 14:17:34+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/perf/cli.py
layout: document
redirect_from:
- /library/cp_library/perf/cli.py
- /library/cp_library/perf/cli.py.html
title: cp_library/perf/cli.py
---
