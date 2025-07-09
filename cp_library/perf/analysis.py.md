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
  bundledCode: "'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2578\n             https://kobejean.github.io/cp-library               \n'''\n\
    \n\"\"\"Advanced analysis tools for benchmark results\"\"\"\n\nfrom typing import\
    \ List, Dict, Any\nimport json\nimport statistics\nfrom pathlib import Path\n\n\
    class BenchmarkAnalyzer:\n    \"\"\"Analyze and compare benchmark results\"\"\"\
    \n    \n    def __init__(self, results_file: str = None, results_data: List =\
    \ None):\n        if results_file:\n            with open(results_file, 'r') as\
    \ f:\n                self.results = json.load(f)\n        elif results_data:\n\
    \            self.results = results_data\n        else:\n            raise ValueError(\"\
    Must provide either results_file or results_data\")\n    \n    def group_by_implementation(self)\
    \ -> Dict[str, List[Dict]]:\n        \"\"\"Group results by implementation\"\"\
    \"\n        grouped = {}\n        for result in self.results:\n            impl\
    \ = result['implementation']\n            if impl not in grouped:\n          \
    \      grouped[impl] = []\n            grouped[impl].append(result)\n        return\
    \ grouped\n    \n    def group_by_operation(self) -> Dict[str, List[Dict]]:\n\
    \        \"\"\"Group results by operation\"\"\"\n        grouped = {}\n      \
    \  for result in self.results:\n            if 'params' in result and 'operation'\
    \ in result['params']:\n                op = result['params']['operation']\n \
    \               if op not in grouped:\n                    grouped[op] = []\n\
    \                grouped[op].append(result)\n        return grouped\n    \n  \
    \  def group_by_size(self) -> Dict[int, List[Dict]]:\n        \"\"\"Group results\
    \ by size\"\"\"\n        grouped = {}\n        for result in self.results:\n \
    \           if 'params' in result and 'size' in result['params']:\n          \
    \      size = result['params']['size']\n                if size not in grouped:\n\
    \                    grouped[size] = []\n                grouped[size].append(result)\n\
    \        return grouped\n    \n    def find_best_implementation(self, operation:\
    \ str = None, size: int = None) -> Dict[str, Any]:\n        \"\"\"Find best implementation\
    \ for given constraints\"\"\"\n        filtered = self.results\n        \n   \
    \     if operation:\n            filtered = [r for r in filtered if r.get('params',\
    \ {}).get('operation') == operation]\n        if size:\n            filtered =\
    \ [r for r in filtered if r.get('params', {}).get('size') == size]\n        \n\
    \        if not filtered:\n            return None\n        \n        # Group\
    \ by implementation and calculate averages\n        impl_times = {}\n        for\
    \ result in filtered:\n            if result.get('error') or result.get('time_ms')\
    \ == float('inf'):\n                continue\n            impl = result['implementation']\n\
    \            if impl not in impl_times:\n                impl_times[impl] = []\n\
    \            impl_times[impl].append(result['time_ms'])\n        \n        # Calculate\
    \ statistics\n        impl_stats = {}\n        for impl, times in impl_times.items():\n\
    \            if times:\n                impl_stats[impl] = {\n               \
    \     'mean': statistics.mean(times),\n                    'std': statistics.stdev(times)\
    \ if len(times) > 1 else 0,\n                    'min': min(times),\n        \
    \            'max': max(times),\n                    'count': len(times)\n   \
    \             }\n        \n        # Find best\n        if impl_stats:\n     \
    \       best_impl = min(impl_stats.keys(), key=lambda k: impl_stats[k]['mean'])\n\
    \            return {\n                'implementation': best_impl,\n        \
    \        'stats': impl_stats[best_impl],\n                'all_stats': impl_stats\n\
    \            }\n        \n        return None\n    \n    def calculate_speedup_matrix(self,\
    \ baseline: str = None) -> Dict[str, Dict[str, float]]:\n        \"\"\"Calculate\
    \ speedup matrix between implementations\"\"\"\n        impls = set(r['implementation']\
    \ for r in self.results)\n        \n        if baseline and baseline not in impls:\n\
    \            baseline = None\n        \n        if not baseline:\n           \
    \ # Use slowest as baseline\n            impl_times = {}\n            for impl\
    \ in impls:\n                times = [r['time_ms'] for r in self.results \n  \
    \                      if r['implementation'] == impl and not r.get('error')]\n\
    \                if times:\n                    impl_times[impl] = statistics.mean(times)\n\
    \            baseline = max(impl_times.keys(), key=lambda k: impl_times[k]) if\
    \ impl_times else list(impls)[0]\n        \n        # Calculate pairwise speedups\n\
    \        speedup_matrix = {}\n        for impl_a in impls:\n            speedup_matrix[impl_a]\
    \ = {}\n            for impl_b in impls:\n                if impl_a == impl_b:\n\
    \                    speedup_matrix[impl_a][impl_b] = 1.0\n                else:\n\
    \                    # Get comparable results (same operation and size)\n    \
    \                speedups = []\n                    for result_a in self.results:\n\
    \                        if result_a['implementation'] != impl_a or result_a.get('error'):\n\
    \                            continue\n                        \n            \
    \            # Find matching result for impl_b\n                        for result_b\
    \ in self.results:\n                            if (result_b['implementation']\
    \ == impl_b and \n                                not result_b.get('error') and\n\
    \                                result_a.get('params') == result_b.get('params')):\n\
    \                                \n                                if result_a['time_ms']\
    \ > 0:\n                                    speedup = result_b['time_ms'] / result_a['time_ms']\n\
    \                                    speedups.append(speedup)\n              \
    \                  break\n                    \n                    speedup_matrix[impl_a][impl_b]\
    \ = statistics.mean(speedups) if speedups else 0.0\n        \n        return speedup_matrix\n\
    \    \n    def analyze_scaling(self) -> Dict[str, Dict[str, float]]:\n       \
    \ \"\"\"Analyze how implementations scale with size\"\"\"\n        scaling_analysis\
    \ = {}\n        \n        by_impl = self.group_by_implementation()\n        \n\
    \        for impl, results in by_impl.items():\n            # Group by operation\n\
    \            op_results = {}\n            for result in results:\n           \
    \     if result.get('error') or not result.get('params'):\n                  \
    \  continue\n                op = result['params'].get('operation', 'unknown')\n\
    \                if op not in op_results:\n                    op_results[op]\
    \ = []\n                op_results[op].append((result['params']['size'], result['time_ms']))\n\
    \            \n            scaling_analysis[impl] = {}\n            \n       \
    \     for op, size_times in op_results.items():\n                if len(size_times)\
    \ < 2:\n                    continue\n                \n                # Sort\
    \ by size\n                size_times.sort()\n                \n             \
    \   # Calculate scaling factor (rough estimate)\n                sizes = [st[0]\
    \ for st in size_times]\n                times = [st[1] for st in size_times]\n\
    \                \n                # Simple linear regression to estimate scaling\n\
    \                if len(sizes) >= 2:\n                    # Calculate log-log\
    \ slope for complexity estimation\n                    import math\n         \
    \           log_sizes = [math.log(s) for s in sizes if s > 0]\n              \
    \      log_times = [math.log(t) for t in times if t > 0]\n                   \
    \ \n                    if len(log_sizes) >= 2:\n                        # Simple\
    \ slope calculation\n                        n = len(log_sizes)\n            \
    \            slope = (n * sum(x*y for x,y in zip(log_sizes, log_times)) - \n \
    \                               sum(log_sizes) * sum(log_times)) / (n * sum(x*x\
    \ for x in log_sizes) - sum(log_sizes)**2)\n                        \n       \
    \                 scaling_analysis[impl][op] = {\n                           \
    \ 'complexity_exponent': slope,\n                            'size_range': (min(sizes),\
    \ max(sizes)),\n                            'time_range': (min(times), max(times))\n\
    \                        }\n        \n        return scaling_analysis\n    \n\
    \    def generate_summary_report(self) -> str:\n        \"\"\"Generate a comprehensive\
    \ summary report\"\"\"\n        report = [\"BENCHMARK ANALYSIS REPORT\", \"=\"\
    *50, \"\"]\n        \n        # Basic stats\n        total_results = len(self.results)\n\
    \        implementations = len(set(r['implementation'] for r in self.results))\n\
    \        operations = len(set(r.get('params', {}).get('operation', 'unknown')\
    \ for r in self.results))\n        \n        report.extend([\n            f\"\
    Total results: {total_results}\",\n            f\"Implementations tested: {implementations}\"\
    ,\n            f\"Operations tested: {operations}\",\n            \"\"\n     \
    \   ])\n        \n        # Best implementation per operation\n        operations_tested\
    \ = set(r.get('params', {}).get('operation') for r in self.results if r.get('params'))\n\
    \        operations_tested.discard(None)\n        \n        if operations_tested:\n\
    \            report.extend([\"Best Implementation by Operation:\", \"-\"*40])\n\
    \            for op in sorted(operations_tested):\n                best = self.find_best_implementation(operation=op)\n\
    \                if best:\n                    impl = best['implementation']\n\
    \                    time_ms = best['stats']['mean']\n                    report.append(f\"\
    {op:<15} {impl:<20} {time_ms:.3f} ms\")\n            report.append(\"\")\n   \
    \     \n        # Scaling analysis\n        scaling = self.analyze_scaling()\n\
    \        if scaling:\n            report.extend([\"Complexity Analysis:\", \"\
    -\"*40])\n            for impl, ops in scaling.items():\n                if ops:\n\
    \                    report.append(f\"{impl}:\")\n                    for op,\
    \ data in ops.items():\n                        exp = data['complexity_exponent']\n\
    \                        if exp < 0.5:\n                            complexity\
    \ = \"O(1) or sub-linear\"\n                        elif exp < 1.2:\n        \
    \                    complexity = \"O(n)\"\n                        elif exp <\
    \ 1.8:\n                            complexity = \"O(n log n)\"\n            \
    \            elif exp < 2.2:\n                            complexity = \"O(n\xB2\
    )\"\n                        else:\n                            complexity = f\"\
    O(n^{exp:.1f})\"\n                        report.append(f\"  {op}: {complexity}\"\
    )\n                    report.append(\"\")\n        \n        return \"\\n\".join(report)\n\
    \n\ndef compare_benchmark_files(file1: str, file2: str) -> str:\n    \"\"\"Compare\
    \ two benchmark result files\"\"\"\n    analyzer1 = BenchmarkAnalyzer(results_file=file1)\n\
    \    analyzer2 = BenchmarkAnalyzer(results_file=file2)\n    \n    report = [f\"\
    COMPARISON: {Path(file1).name} vs {Path(file2).name}\", \"=\"*60, \"\"]\n    \n\
    \    # Find common operations and implementations\n    ops1 = set(r.get('params',\
    \ {}).get('operation') for r in analyzer1.results)\n    ops2 = set(r.get('params',\
    \ {}).get('operation') for r in analyzer2.results)\n    common_ops = ops1 & ops2\n\
    \    \n    impls1 = set(r['implementation'] for r in analyzer1.results)\n    impls2\
    \ = set(r['implementation'] for r in analyzer2.results)\n    common_impls = impls1\
    \ & impls2\n    \n    report.extend([\n        f\"Common operations: {len(common_ops)}\"\
    ,\n        f\"Common implementations: {len(common_impls)}\",\n        \"\"\n \
    \   ])\n    \n    # Compare performance for common operations\n    if common_ops\
    \ and common_impls:\n        report.extend([\"Performance Comparison:\", \"-\"\
    *30])\n        report.append(f\"{'Operation':<15} {'Implementation':<15} {'File1\
    \ (ms)':<12} {'File2 (ms)':<12} {'Speedup':<10}\")\n        report.append(\"-\"\
    *70)\n        \n        for op in sorted(common_ops):\n            for impl in\
    \ sorted(common_impls):\n                best1 = analyzer1.find_best_implementation(operation=op)\n\
    \                best2 = analyzer2.find_best_implementation(operation=op)\n  \
    \              \n                if (best1 and best2 and \n                  \
    \  impl in best1['all_stats'] and impl in best2['all_stats']):\n             \
    \       time1 = best1['all_stats'][impl]['mean']\n                    time2 =\
    \ best2['all_stats'][impl]['mean']\n                    speedup = time1 / time2\
    \ if time2 > 0 else 0\n                    \n                    report.append(f\"\
    {op:<15} {impl:<15} {time1:<12.3f} {time2:<12.3f} {speedup:<10.2f}x\")\n    \n\
    \    return \"\\n\".join(report)\n"
  code: "import cp_library.__header__\nimport cp_library.perf.__header__\n\"\"\"Advanced\
    \ analysis tools for benchmark results\"\"\"\n\nfrom typing import List, Dict,\
    \ Any\nimport json\nimport statistics\nfrom pathlib import Path\n\nclass BenchmarkAnalyzer:\n\
    \    \"\"\"Analyze and compare benchmark results\"\"\"\n    \n    def __init__(self,\
    \ results_file: str = None, results_data: List = None):\n        if results_file:\n\
    \            with open(results_file, 'r') as f:\n                self.results\
    \ = json.load(f)\n        elif results_data:\n            self.results = results_data\n\
    \        else:\n            raise ValueError(\"Must provide either results_file\
    \ or results_data\")\n    \n    def group_by_implementation(self) -> Dict[str,\
    \ List[Dict]]:\n        \"\"\"Group results by implementation\"\"\"\n        grouped\
    \ = {}\n        for result in self.results:\n            impl = result['implementation']\n\
    \            if impl not in grouped:\n                grouped[impl] = []\n   \
    \         grouped[impl].append(result)\n        return grouped\n    \n    def\
    \ group_by_operation(self) -> Dict[str, List[Dict]]:\n        \"\"\"Group results\
    \ by operation\"\"\"\n        grouped = {}\n        for result in self.results:\n\
    \            if 'params' in result and 'operation' in result['params']:\n    \
    \            op = result['params']['operation']\n                if op not in\
    \ grouped:\n                    grouped[op] = []\n                grouped[op].append(result)\n\
    \        return grouped\n    \n    def group_by_size(self) -> Dict[int, List[Dict]]:\n\
    \        \"\"\"Group results by size\"\"\"\n        grouped = {}\n        for\
    \ result in self.results:\n            if 'params' in result and 'size' in result['params']:\n\
    \                size = result['params']['size']\n                if size not\
    \ in grouped:\n                    grouped[size] = []\n                grouped[size].append(result)\n\
    \        return grouped\n    \n    def find_best_implementation(self, operation:\
    \ str = None, size: int = None) -> Dict[str, Any]:\n        \"\"\"Find best implementation\
    \ for given constraints\"\"\"\n        filtered = self.results\n        \n   \
    \     if operation:\n            filtered = [r for r in filtered if r.get('params',\
    \ {}).get('operation') == operation]\n        if size:\n            filtered =\
    \ [r for r in filtered if r.get('params', {}).get('size') == size]\n        \n\
    \        if not filtered:\n            return None\n        \n        # Group\
    \ by implementation and calculate averages\n        impl_times = {}\n        for\
    \ result in filtered:\n            if result.get('error') or result.get('time_ms')\
    \ == float('inf'):\n                continue\n            impl = result['implementation']\n\
    \            if impl not in impl_times:\n                impl_times[impl] = []\n\
    \            impl_times[impl].append(result['time_ms'])\n        \n        # Calculate\
    \ statistics\n        impl_stats = {}\n        for impl, times in impl_times.items():\n\
    \            if times:\n                impl_stats[impl] = {\n               \
    \     'mean': statistics.mean(times),\n                    'std': statistics.stdev(times)\
    \ if len(times) > 1 else 0,\n                    'min': min(times),\n        \
    \            'max': max(times),\n                    'count': len(times)\n   \
    \             }\n        \n        # Find best\n        if impl_stats:\n     \
    \       best_impl = min(impl_stats.keys(), key=lambda k: impl_stats[k]['mean'])\n\
    \            return {\n                'implementation': best_impl,\n        \
    \        'stats': impl_stats[best_impl],\n                'all_stats': impl_stats\n\
    \            }\n        \n        return None\n    \n    def calculate_speedup_matrix(self,\
    \ baseline: str = None) -> Dict[str, Dict[str, float]]:\n        \"\"\"Calculate\
    \ speedup matrix between implementations\"\"\"\n        impls = set(r['implementation']\
    \ for r in self.results)\n        \n        if baseline and baseline not in impls:\n\
    \            baseline = None\n        \n        if not baseline:\n           \
    \ # Use slowest as baseline\n            impl_times = {}\n            for impl\
    \ in impls:\n                times = [r['time_ms'] for r in self.results \n  \
    \                      if r['implementation'] == impl and not r.get('error')]\n\
    \                if times:\n                    impl_times[impl] = statistics.mean(times)\n\
    \            baseline = max(impl_times.keys(), key=lambda k: impl_times[k]) if\
    \ impl_times else list(impls)[0]\n        \n        # Calculate pairwise speedups\n\
    \        speedup_matrix = {}\n        for impl_a in impls:\n            speedup_matrix[impl_a]\
    \ = {}\n            for impl_b in impls:\n                if impl_a == impl_b:\n\
    \                    speedup_matrix[impl_a][impl_b] = 1.0\n                else:\n\
    \                    # Get comparable results (same operation and size)\n    \
    \                speedups = []\n                    for result_a in self.results:\n\
    \                        if result_a['implementation'] != impl_a or result_a.get('error'):\n\
    \                            continue\n                        \n            \
    \            # Find matching result for impl_b\n                        for result_b\
    \ in self.results:\n                            if (result_b['implementation']\
    \ == impl_b and \n                                not result_b.get('error') and\n\
    \                                result_a.get('params') == result_b.get('params')):\n\
    \                                \n                                if result_a['time_ms']\
    \ > 0:\n                                    speedup = result_b['time_ms'] / result_a['time_ms']\n\
    \                                    speedups.append(speedup)\n              \
    \                  break\n                    \n                    speedup_matrix[impl_a][impl_b]\
    \ = statistics.mean(speedups) if speedups else 0.0\n        \n        return speedup_matrix\n\
    \    \n    def analyze_scaling(self) -> Dict[str, Dict[str, float]]:\n       \
    \ \"\"\"Analyze how implementations scale with size\"\"\"\n        scaling_analysis\
    \ = {}\n        \n        by_impl = self.group_by_implementation()\n        \n\
    \        for impl, results in by_impl.items():\n            # Group by operation\n\
    \            op_results = {}\n            for result in results:\n           \
    \     if result.get('error') or not result.get('params'):\n                  \
    \  continue\n                op = result['params'].get('operation', 'unknown')\n\
    \                if op not in op_results:\n                    op_results[op]\
    \ = []\n                op_results[op].append((result['params']['size'], result['time_ms']))\n\
    \            \n            scaling_analysis[impl] = {}\n            \n       \
    \     for op, size_times in op_results.items():\n                if len(size_times)\
    \ < 2:\n                    continue\n                \n                # Sort\
    \ by size\n                size_times.sort()\n                \n             \
    \   # Calculate scaling factor (rough estimate)\n                sizes = [st[0]\
    \ for st in size_times]\n                times = [st[1] for st in size_times]\n\
    \                \n                # Simple linear regression to estimate scaling\n\
    \                if len(sizes) >= 2:\n                    # Calculate log-log\
    \ slope for complexity estimation\n                    import math\n         \
    \           log_sizes = [math.log(s) for s in sizes if s > 0]\n              \
    \      log_times = [math.log(t) for t in times if t > 0]\n                   \
    \ \n                    if len(log_sizes) >= 2:\n                        # Simple\
    \ slope calculation\n                        n = len(log_sizes)\n            \
    \            slope = (n * sum(x*y for x,y in zip(log_sizes, log_times)) - \n \
    \                               sum(log_sizes) * sum(log_times)) / (n * sum(x*x\
    \ for x in log_sizes) - sum(log_sizes)**2)\n                        \n       \
    \                 scaling_analysis[impl][op] = {\n                           \
    \ 'complexity_exponent': slope,\n                            'size_range': (min(sizes),\
    \ max(sizes)),\n                            'time_range': (min(times), max(times))\n\
    \                        }\n        \n        return scaling_analysis\n    \n\
    \    def generate_summary_report(self) -> str:\n        \"\"\"Generate a comprehensive\
    \ summary report\"\"\"\n        report = [\"BENCHMARK ANALYSIS REPORT\", \"=\"\
    *50, \"\"]\n        \n        # Basic stats\n        total_results = len(self.results)\n\
    \        implementations = len(set(r['implementation'] for r in self.results))\n\
    \        operations = len(set(r.get('params', {}).get('operation', 'unknown')\
    \ for r in self.results))\n        \n        report.extend([\n            f\"\
    Total results: {total_results}\",\n            f\"Implementations tested: {implementations}\"\
    ,\n            f\"Operations tested: {operations}\",\n            \"\"\n     \
    \   ])\n        \n        # Best implementation per operation\n        operations_tested\
    \ = set(r.get('params', {}).get('operation') for r in self.results if r.get('params'))\n\
    \        operations_tested.discard(None)\n        \n        if operations_tested:\n\
    \            report.extend([\"Best Implementation by Operation:\", \"-\"*40])\n\
    \            for op in sorted(operations_tested):\n                best = self.find_best_implementation(operation=op)\n\
    \                if best:\n                    impl = best['implementation']\n\
    \                    time_ms = best['stats']['mean']\n                    report.append(f\"\
    {op:<15} {impl:<20} {time_ms:.3f} ms\")\n            report.append(\"\")\n   \
    \     \n        # Scaling analysis\n        scaling = self.analyze_scaling()\n\
    \        if scaling:\n            report.extend([\"Complexity Analysis:\", \"\
    -\"*40])\n            for impl, ops in scaling.items():\n                if ops:\n\
    \                    report.append(f\"{impl}:\")\n                    for op,\
    \ data in ops.items():\n                        exp = data['complexity_exponent']\n\
    \                        if exp < 0.5:\n                            complexity\
    \ = \"O(1) or sub-linear\"\n                        elif exp < 1.2:\n        \
    \                    complexity = \"O(n)\"\n                        elif exp <\
    \ 1.8:\n                            complexity = \"O(n log n)\"\n            \
    \            elif exp < 2.2:\n                            complexity = \"O(n\xB2\
    )\"\n                        else:\n                            complexity = f\"\
    O(n^{exp:.1f})\"\n                        report.append(f\"  {op}: {complexity}\"\
    )\n                    report.append(\"\")\n        \n        return \"\\n\".join(report)\n\
    \n\ndef compare_benchmark_files(file1: str, file2: str) -> str:\n    \"\"\"Compare\
    \ two benchmark result files\"\"\"\n    analyzer1 = BenchmarkAnalyzer(results_file=file1)\n\
    \    analyzer2 = BenchmarkAnalyzer(results_file=file2)\n    \n    report = [f\"\
    COMPARISON: {Path(file1).name} vs {Path(file2).name}\", \"=\"*60, \"\"]\n    \n\
    \    # Find common operations and implementations\n    ops1 = set(r.get('params',\
    \ {}).get('operation') for r in analyzer1.results)\n    ops2 = set(r.get('params',\
    \ {}).get('operation') for r in analyzer2.results)\n    common_ops = ops1 & ops2\n\
    \    \n    impls1 = set(r['implementation'] for r in analyzer1.results)\n    impls2\
    \ = set(r['implementation'] for r in analyzer2.results)\n    common_impls = impls1\
    \ & impls2\n    \n    report.extend([\n        f\"Common operations: {len(common_ops)}\"\
    ,\n        f\"Common implementations: {len(common_impls)}\",\n        \"\"\n \
    \   ])\n    \n    # Compare performance for common operations\n    if common_ops\
    \ and common_impls:\n        report.extend([\"Performance Comparison:\", \"-\"\
    *30])\n        report.append(f\"{'Operation':<15} {'Implementation':<15} {'File1\
    \ (ms)':<12} {'File2 (ms)':<12} {'Speedup':<10}\")\n        report.append(\"-\"\
    *70)\n        \n        for op in sorted(common_ops):\n            for impl in\
    \ sorted(common_impls):\n                best1 = analyzer1.find_best_implementation(operation=op)\n\
    \                best2 = analyzer2.find_best_implementation(operation=op)\n  \
    \              \n                if (best1 and best2 and \n                  \
    \  impl in best1['all_stats'] and impl in best2['all_stats']):\n             \
    \       time1 = best1['all_stats'][impl]['mean']\n                    time2 =\
    \ best2['all_stats'][impl]['mean']\n                    speedup = time1 / time2\
    \ if time2 > 0 else 0\n                    \n                    report.append(f\"\
    {op:<15} {impl:<15} {time1:<12.3f} {time2:<12.3f} {speedup:<10.2f}x\")\n    \n\
    \    return \"\\n\".join(report)"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/perf/analysis.py
  requiredBy: []
  timestamp: '2025-07-09 08:31:42+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/perf/analysis.py
layout: document
redirect_from:
- /library/cp_library/perf/analysis.py
- /library/cp_library/perf/analysis.py.html
title: cp_library/perf/analysis.py
---
