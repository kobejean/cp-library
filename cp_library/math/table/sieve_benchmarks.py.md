---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: cp_library/math/table/linear_sieve_cls.py
    title: cp_library/math/table/linear_sieve_cls.py
  - icon: ':warning:'
    path: cp_library/math/table/linear_sieve_cnts_cls.py
    title: cp_library/math/table/linear_sieve_cnts_cls.py
  - icon: ':warning:'
    path: cp_library/math/table/primes_cls.py
    title: cp_library/math/table/primes_cls.py
  - icon: ':warning:'
    path: cp_library/math/table/sieve_cls.py
    title: cp_library/math/table/sieve_cls.py
  - icon: ':warning:'
    path: cp_library/math/table/sieve_proto.py
    title: cp_library/math/table/sieve_proto.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "import time\nimport random\nimport math\nimport numpy as np\nimport\
    \ pandas as pd\nimport matplotlib.pyplot as plt\n\n# Import your sieve classes\n\
    '''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\n   \
    \          https://kobejean.github.io/cp-library               \n'''\nfrom functools\
    \ import cached_property\nfrom typing import Protocol\n\nclass Primes(list):\n\
    \    def __init__(primes, N: int):\n        super().__init__()\n        spf =\
    \ [0] * (N + 1)\n        spf[0], spf[1] = 0, 1\n\n        for i in range(2, N\
    \ + 1):\n            if spf[i] == 0:\n                spf[i] = i\n           \
    \     primes.append(i)\n            for p in primes:\n                if p > spf[i]\
    \ or i * p > N:\n                    break\n                spf[i * p] = p\n\n\
    class SieveProtocol(Protocol):\n    primes: Primes\n    def factor_cnts(self,\
    \ N): ...\n    def factors(self, N): ...\n    def unique_factors(self, N): ...\n\
    \    def __getitem__(self, key) -> int: ...\n\nclass Sieve(list[int], SieveProtocol):\n\
    \    def __init__(spf, N):\n        super().__init__(i for i in range(N+1))\n\
    \        spf[0] = 1\n        for x in range(2, N+1):\n            x2 = x*x\n \
    \           if x2 > N: break\n            if spf[x] == x:\n                for\
    \ j in range(x2, N+1, x):\n                    if spf[j] == j:\n             \
    \           spf[j] = x\n    @cached_property\n    def primes(spf) -> Primes:\n\
    \        gen = (x for x,f in enumerate(spf) if f == x)\n        primes = Primes.__new__(Primes)\n\
    \        super(Primes, primes).__init__(gen)\n        return primes\n\n    def\
    \ factor_cnts(spf, N):\n        assert N < len(spf)\n        pairs = []\n    \
    \    while N > 1:\n            match pairs:\n                case [*_, (f,cnt)]\
    \ if f == spf[N]:\n                    pairs[-1] = (f,cnt+1)\n               \
    \ case _:\n                    pairs.append((spf[N], 1))\n            N //= spf[N]\n\
    \        return pairs\n\n    def factors(spf, N):\n        assert N < len(spf)\n\
    \        factors = []\n        while N > 1:\n            factors.append(spf[N])\n\
    \            N //= spf[N]\n        return factors\n    \n    def unique_factors(spf,\
    \ N):\n        assert N < len(spf)\n        factors = []\n        while N > 1:\n\
    \            if factors and factors[-1] != spf[N]: \n                factors.append(spf[N])\n\
    \            N //= spf[N]\n        return factors\n\nclass LinearSieve(list[int],\
    \ SieveProtocol):\n    def __init__(spf, N):\n        super().__init__([0] * (N\
    \ + 1))\n        spf[0], spf[1] = 0, 1\n        primes = Primes.__new__(Primes)\n\
    \n        for i in range(2, N + 1):\n            if spf[i] == 0:\n           \
    \     spf[i] = i\n                primes.append(i)\n            for p in primes:\n\
    \                if p > spf[i] or i * p > N:\n                    break\n    \
    \            spf[i * p] = p\n        spf.primes = spf\n\n    def factor_cnts(spf,\
    \ N):\n        assert N < len(spf)\n        pairs = []\n        while N > 1:\n\
    \            match pairs:\n                case [*_, (f,cnt)] if f == spf[N]:\n\
    \                    pairs[-1] = (f,cnt+1)\n                case _:\n        \
    \            pairs.append((spf[N], 1))\n            N //= spf[N]\n        return\
    \ pairs\n    \n    def factors(spf, N):\n        assert N < len(spf)\n       \
    \ factors = []\n        while N > 1:\n            factors.append(spf[N])\n   \
    \         N //= spf[N]\n        return factors\n \n\nclass LinearSieveCounts(list[int],\
    \ SieveProtocol):\n\n    def __init__(spf, N: int):\n        super().__init__([0]\
    \ * (N + 1))\n        exp = [0] * (N + 1)\n        nxt = [0] * (N + 1)\n     \
    \   primes = Primes.__new__(Primes)\n        spf[0], spf[1] = 0, 1\n        exp[1]\
    \ = 1\n        for x in range(2,N+1):\n            if spf[x] == 0:\n         \
    \       spf[x],exp[x] = x,1\n                primes.append(x)\n            for\
    \ p in primes:\n                if (y := x*p) > N or p > spf[x]: break\n     \
    \           spf[y] = p\n                if x%p:\n                    nxt[y], exp[y]\
    \ = x, 1\n                else:\n                    nxt[y], exp[y] = nxt[x],\
    \ exp[x]+1\n        spf.primes = primes\n        spf.exp = exp\n        spf.nxt\
    \ = nxt\n    \n    def factor_cnts(spf, N: int):\n        assert N < len(spf)\n\
    \        exp,nxt = spf.exp, spf.nxt\n        pairs = []\n        while spf[N]\
    \ != N:\n            pairs.append((spf[N],exp[N]))\n            N = nxt[N]\n \
    \       if N:\n            pairs.append((spf[N],exp[N]))\n        return pairs\n\
    \n    def factors(spf, N):\n        assert N < len(spf)\n        exp,nxt = spf.exp,\
    \ spf.nxt\n        factors = []\n        while N > 1:\n            factors.extend(spf[N]\
    \ for _ in range(exp[N]))\n            N = nxt[N]\n        return factors\n\n\
    def benchmark_construction(Ns):\n    sieve_classes = [\n        ('LinearSieveCounts',\
    \ LinearSieveCounts),\n        ('LinearSieve', LinearSieve),\n        ('Sieve',\
    \ Sieve)\n    ]\n    construction_results = []\n\n    for N in Ns:\n        sieves\
    \ = {}\n        for name, cls in sieve_classes:\n            print(f\"Constructing\
    \ {name} with N = {N}\")\n            start_time = time.perf_counter()\n     \
    \       sieve = cls(N)\n            total_time = time.perf_counter() - start_time\n\
    \            sieves[name] = sieve\n            construction_results.append({'Sieve':\
    \ name, 'ConstructionTime': total_time, 'N': N})\n        yield N, sieves, construction_results[-len(sieve_classes):]\
    \  # Return only the latest results\n\ndef warm_up_methods(sieves, test_numbers,\
    \ warm_up_runs=3):\n    print(\"\\nWarming up methods...\")\n    for _ in range(warm_up_runs):\n\
    \        for sieve_name, sieve in sieves.items():\n            for method_name\
    \ in ['factor_cnts', 'factors']:\n                method = getattr(sieve, method_name)\n\
    \                for num in test_numbers[:100]:  # Use a subset for warm-up\n\
    \                    method(num)\n    print(\"Warm-up completed.\\n\")\n\ndef\
    \ benchmark_methods(sieves, test_numbers, N, warm_up_runs=3):\n    timings = []\n\
    \    num_numbers = len(test_numbers)\n\n    # Warm-up phase\n    warm_up_methods(sieves,\
    \ test_numbers, warm_up_runs)\n\n    for sieve_name, sieve in sieves.items():\n\
    \        for method_name in ['factor_cnts', 'factors']:\n            method =\
    \ getattr(sieve, method_name)\n            print(f\"Benchmarking {sieve_name}.{method_name}\
    \ with N = {N}\")\n            start_time = time.perf_counter()\n            for\
    \ num in test_numbers:\n                method(num)\n            total_time =\
    \ time.perf_counter() - start_time\n            avg_time = total_time / num_numbers\n\
    \            timings.append({\n                'Sieve': sieve_name,\n        \
    \        'Method': method_name,\n                'AvgTimePerNumber': avg_time,\n\
    \                'N': N\n            })\n\n    return timings\n\ndef verify_correctness(sieves,\
    \ test_numbers):\n    correct = True\n    for num in test_numbers:\n        factors_results\
    \ = []\n        factor_cnts_results = []\n        for sieve_name, sieve in sieves.items():\n\
    \            factors_results.append((sieve_name, sieve.factors(num)))\n      \
    \      factor_cnts_results.append((sieve_name, sorted(sieve.factor_cnts(num))))\n\
    \        # Check if all factors results are the same\n        factors_set = set(tuple(res[1])\
    \ for res in factors_results)\n        if len(factors_set) > 1:\n            print(f\"\
    Mismatch in factors for number {num}\")\n            for name, res in factors_results:\n\
    \                print(f\"{name}: {res}\")\n            correct = False\n    \
    \        break\n        # Check if all factor_cnts results are the same\n    \
    \    factor_cnts_set = set(tuple(res[1]) for res in factor_cnts_results)\n   \
    \     if len(factor_cnts_set) > 1:\n            print(f\"Mismatch in factor_cnts\
    \ for number {num}\")\n            for name, res in factor_cnts_results:\n   \
    \             print(f\"{name}: {res}\")\n            correct = False\n       \
    \     break\n    if correct:\n        print(\"All methods produce correct results.\"\
    )\n    return correct\n\ndef benchmark_specific_cases(sieves, N, repetitions=50,\
    \ warm_up_runs=3):\n    # Benchmarking factorials and powers of 2\n    factorial_numbers\
    \ = []\n    max_i = 20  # Adjust as needed for more factorials\n    for i in range(1,\
    \ max_i + 1):\n        fact = math.factorial(i)\n        if fact >= N:\n     \
    \       break\n        factorial_numbers.append(fact)\n    \n    # Extend the\
    \ list by repeating numbers to increase sample size\n    factorial_numbers *=\
    \ repetitions  # Repeat the list 'repetitions' times\n    random.shuffle(factorial_numbers)\
    \  # Shuffle to randomize the order\n\n    powers_of_two = [1 << k for k in range(1,\
    \ int(math.log2(N)) + 1)]\n    powers_of_two *= repetitions  # Repeat the list\
    \ 'repetitions' times\n    random.shuffle(powers_of_two)  # Shuffle to randomize\
    \ the order\n\n    specific_cases_results = []\n\n    # Warm-up phase\n    warm_up_methods(sieves,\
    \ factorial_numbers + powers_of_two, warm_up_runs)\n\n    for case_name, numbers\
    \ in [('Factorials', factorial_numbers), ('PowersOfTwo', powers_of_two)]:\n  \
    \      num_numbers = len(numbers)\n        for sieve_name, sieve in sieves.items():\n\
    \            if num_numbers == 0:\n                continue  # Skip if no numbers\
    \ to test\n            print(f\"Benchmarking {sieve_name} on {case_name} with\
    \ N = {N}\")\n            method = sieve.factor_cnts\n            start_time =\
    \ time.perf_counter()\n            for num in numbers:\n                method(num)\n\
    \            total_time = time.perf_counter() - start_time\n            avg_time\
    \ = total_time / num_numbers\n            specific_cases_results.append({\n  \
    \              'Case': case_name,\n                'Sieve': sieve_name,\n    \
    \            'AvgTimePerNumber': avg_time,\n                'NumNumbers': num_numbers,\n\
    \                'N': N\n            })\n    return specific_cases_results\n\n\
    def plot_results(construction_df, methods_df, specific_cases_df):\n    # Plot\
    \ construction times\n    plt.figure(figsize=(10, 6))\n    for sieve in construction_df['Sieve'].unique():\n\
    \        sieve_data = construction_df[construction_df['Sieve'] == sieve]\n   \
    \     sieve_data = sieve_data.sort_values('N')  # Ensure data is sorted by N\n\
    \        plt.plot(sieve_data['N'], sieve_data['ConstructionTime'], marker='o',\
    \ label=sieve)\n    plt.xlabel('N')\n    plt.ylabel('Construction Time (s)')\n\
    \    plt.title('Sieve Construction Time')\n    plt.legend()\n    plt.xscale('log')\n\
    \    plt.yscale('log')\n    plt.grid(True)\n    plt.show()\n\n    # Plot method\
    \ average times per number\n    for method in methods_df['Method'].unique():\n\
    \        plt.figure(figsize=(10, 6))\n        for sieve in methods_df['Sieve'].unique():\n\
    \            sieve_data = methods_df[(methods_df['Sieve'] == sieve) & (methods_df['Method']\
    \ == method)]\n            sieve_data = sieve_data.sort_values('N')  # Ensure\
    \ data is sorted by N\n            plt.plot(sieve_data['N'], sieve_data['AvgTimePerNumber'],\
    \ marker='o', label=sieve)\n        plt.xlabel('N')\n        plt.ylabel('Average\
    \ Time per Number (s)')\n        plt.title(f'Method {method} Average Time per\
    \ Number')\n        plt.legend()\n        plt.xscale('log')\n        plt.yscale('log')\n\
    \        plt.grid(True)\n        plt.show()\n\n    # Compute and plot percentage\
    \ speedup for methods\n    baseline_sieve = 'Sieve'  # Set the baseline sieve\n\
    \    for method in methods_df['Method'].unique():\n        plt.figure(figsize=(10,\
    \ 6))\n        # Get the baseline timings\n        baseline_data = methods_df[(methods_df['Sieve']\
    \ == baseline_sieve) & (methods_df['Method'] == method)]\n        baseline_data\
    \ = baseline_data[['N', 'AvgTimePerNumber']].set_index('N')\n        for sieve\
    \ in methods_df['Sieve'].unique():\n            if sieve == baseline_sieve:\n\
    \                continue\n            sieve_data = methods_df[(methods_df['Sieve']\
    \ == sieve) & (methods_df['Method'] == method)]\n            sieve_data = sieve_data[['N',\
    \ 'AvgTimePerNumber']].set_index('N')\n            # Align data on N\n       \
    \     combined = baseline_data.join(sieve_data, lsuffix='_baseline', rsuffix='_other',\
    \ how='inner')\n            # Compute percentage speedup\n            combined['PercentSpeedup']\
    \ = ((combined['AvgTimePerNumber_baseline'] - combined['AvgTimePerNumber_other'])\
    \ / combined['AvgTimePerNumber_baseline']) * 100\n            combined = combined.reset_index()\n\
    \            combined = combined.sort_values('N')\n            plt.plot(combined['N'],\
    \ combined['PercentSpeedup'], marker='o', label=sieve)\n        plt.xlabel('N')\n\
    \        plt.ylabel('Percentage Speedup (%)')\n        plt.title(f'Method {method}\
    \ Percentage Speedup over {baseline_sieve}')\n        plt.legend()\n        plt.xscale('log')\n\
    \        plt.grid(True)\n        plt.show()\n\n    # Compute and plot percentage\
    \ speedup for specific cases\n    for case in specific_cases_df['Case'].unique():\n\
    \        plt.figure(figsize=(10, 6))\n        # Get the baseline timings\n   \
    \     baseline_data = specific_cases_df[(specific_cases_df['Sieve'] == baseline_sieve)\
    \ & (specific_cases_df['Case'] == case)]\n        baseline_data = baseline_data[['N',\
    \ 'AvgTimePerNumber']].set_index('N')\n        for sieve in specific_cases_df['Sieve'].unique():\n\
    \            if sieve == baseline_sieve:\n                continue\n         \
    \   sieve_data = specific_cases_df[(specific_cases_df['Sieve'] == sieve) & (specific_cases_df['Case']\
    \ == case)]\n            sieve_data = sieve_data[['N', 'AvgTimePerNumber']].set_index('N')\n\
    \            # Align data on N\n            combined = baseline_data.join(sieve_data,\
    \ lsuffix='_baseline', rsuffix='_other', how='inner')\n            # Compute percentage\
    \ speedup\n            combined['PercentSpeedup'] = ((combined['AvgTimePerNumber_baseline']\
    \ - combined['AvgTimePerNumber_other']) / combined['AvgTimePerNumber_baseline'])\
    \ * 100\n            combined = combined.reset_index()\n            combined =\
    \ combined.sort_values('N')\n            plt.plot(combined['N'], combined['PercentSpeedup'],\
    \ marker='o', label=sieve)\n        plt.xlabel('N')\n        plt.ylabel('Percentage\
    \ Speedup (%)')\n        plt.title(f'{case} Percentage Speedup over {baseline_sieve}')\n\
    \        plt.legend()\n        plt.xscale('log')\n        plt.grid(True)\n   \
    \     plt.show()\n\n    # Compute and plot percentage speedup for construction\
    \ times\n    plt.figure(figsize=(10, 6))\n    # Get the baseline timings\n   \
    \ baseline_data = construction_df[construction_df['Sieve'] == baseline_sieve]\n\
    \    baseline_data = baseline_data[['N', 'ConstructionTime']].set_index('N')\n\
    \    for sieve in construction_df['Sieve'].unique():\n        if sieve == baseline_sieve:\n\
    \            continue\n        sieve_data = construction_df[construction_df['Sieve']\
    \ == sieve]\n        sieve_data = sieve_data[['N', 'ConstructionTime']].set_index('N')\n\
    \        # Align data on N\n        combined = baseline_data.join(sieve_data,\
    \ lsuffix='_baseline', rsuffix='_other', how='inner')\n        # Compute percentage\
    \ speedup\n        combined['PercentSpeedup'] = ((combined['ConstructionTime_baseline']\
    \ - combined['ConstructionTime_other']) / combined['ConstructionTime_baseline'])\
    \ * 100\n        combined = combined.reset_index()\n        combined = combined.sort_values('N')\n\
    \        plt.plot(combined['N'], combined['PercentSpeedup'], marker='o', label=sieve)\n\
    \    plt.xlabel('N')\n    plt.ylabel('Percentage Speedup (%)')\n    plt.title(f'Construction\
    \ Time Percentage Speedup over {baseline_sieve}')\n    plt.legend()\n    plt.xscale('log')\n\
    \    plt.grid(True)\n    plt.show()\n\ndef main():\n    # Create a finer list\
    \ of N values, ranging from 1e5 to 1e8 with more steps\n    Ns = [int(N) for N\
    \ in np.logspace(5, 8, num=30)]  # 30 steps from 1e5 to 1e8\n    num_tests = 20000\
    \  # Increased number of random numbers to test methods on\n\n    construction_results\
    \ = []\n    method_results = []\n    specific_cases_results = []\n\n    for N_data\
    \ in benchmark_construction(Ns):\n        N, sieves, construction_timings = N_data\n\
    \        construction_results.extend(construction_timings)\n\n        # Generate\
    \ random test numbers\n        test_numbers = [random.randint(2, N - 1) for _\
    \ in range(num_tests)]\n\n        method_timings = benchmark_methods(sieves, test_numbers,\
    \ N, warm_up_runs=3)\n        method_results.extend(method_timings)\n\n      \
    \  print(f\"\\nVerifying correctness of methods for N = {N}...\")\n        verify_correctness(sieves,\
    \ test_numbers[:100])  # Check correctness for first 100 numbers\n\n        specific_case_timings\
    \ = benchmark_specific_cases(sieves, N, repetitions=50, warm_up_runs=3)\n    \
    \    specific_cases_results.extend(specific_case_timings)\n\n    # Convert results\
    \ to DataFrames\n    construction_df = pd.DataFrame(construction_results)\n  \
    \  methods_df = pd.DataFrame(method_results)\n    specific_cases_df = pd.DataFrame(specific_cases_results)\n\
    \n    # Plotting\n    plot_results(construction_df, methods_df, specific_cases_df)\n\
    \nif __name__ == \"__main__\":\n    main()\n"
  code: "import time\nimport random\nimport math\nimport numpy as np\nimport pandas\
    \ as pd\nimport matplotlib.pyplot as plt\n\n# Import your sieve classes\nfrom\
    \ cp_library.math.table.sieve_cls import Sieve\nfrom cp_library.math.table.linear_sieve_cls\
    \ import LinearSieve\nfrom cp_library.math.table.linear_sieve_cnts_cls import\
    \ LinearSieveCounts\n\ndef benchmark_construction(Ns):\n    sieve_classes = [\n\
    \        ('LinearSieveCounts', LinearSieveCounts),\n        ('LinearSieve', LinearSieve),\n\
    \        ('Sieve', Sieve)\n    ]\n    construction_results = []\n\n    for N in\
    \ Ns:\n        sieves = {}\n        for name, cls in sieve_classes:\n        \
    \    print(f\"Constructing {name} with N = {N}\")\n            start_time = time.perf_counter()\n\
    \            sieve = cls(N)\n            total_time = time.perf_counter() - start_time\n\
    \            sieves[name] = sieve\n            construction_results.append({'Sieve':\
    \ name, 'ConstructionTime': total_time, 'N': N})\n        yield N, sieves, construction_results[-len(sieve_classes):]\
    \  # Return only the latest results\n\ndef warm_up_methods(sieves, test_numbers,\
    \ warm_up_runs=3):\n    print(\"\\nWarming up methods...\")\n    for _ in range(warm_up_runs):\n\
    \        for sieve_name, sieve in sieves.items():\n            for method_name\
    \ in ['factor_cnts', 'factors']:\n                method = getattr(sieve, method_name)\n\
    \                for num in test_numbers[:100]:  # Use a subset for warm-up\n\
    \                    method(num)\n    print(\"Warm-up completed.\\n\")\n\ndef\
    \ benchmark_methods(sieves, test_numbers, N, warm_up_runs=3):\n    timings = []\n\
    \    num_numbers = len(test_numbers)\n\n    # Warm-up phase\n    warm_up_methods(sieves,\
    \ test_numbers, warm_up_runs)\n\n    for sieve_name, sieve in sieves.items():\n\
    \        for method_name in ['factor_cnts', 'factors']:\n            method =\
    \ getattr(sieve, method_name)\n            print(f\"Benchmarking {sieve_name}.{method_name}\
    \ with N = {N}\")\n            start_time = time.perf_counter()\n            for\
    \ num in test_numbers:\n                method(num)\n            total_time =\
    \ time.perf_counter() - start_time\n            avg_time = total_time / num_numbers\n\
    \            timings.append({\n                'Sieve': sieve_name,\n        \
    \        'Method': method_name,\n                'AvgTimePerNumber': avg_time,\n\
    \                'N': N\n            })\n\n    return timings\n\ndef verify_correctness(sieves,\
    \ test_numbers):\n    correct = True\n    for num in test_numbers:\n        factors_results\
    \ = []\n        factor_cnts_results = []\n        for sieve_name, sieve in sieves.items():\n\
    \            factors_results.append((sieve_name, sieve.factors(num)))\n      \
    \      factor_cnts_results.append((sieve_name, sorted(sieve.factor_cnts(num))))\n\
    \        # Check if all factors results are the same\n        factors_set = set(tuple(res[1])\
    \ for res in factors_results)\n        if len(factors_set) > 1:\n            print(f\"\
    Mismatch in factors for number {num}\")\n            for name, res in factors_results:\n\
    \                print(f\"{name}: {res}\")\n            correct = False\n    \
    \        break\n        # Check if all factor_cnts results are the same\n    \
    \    factor_cnts_set = set(tuple(res[1]) for res in factor_cnts_results)\n   \
    \     if len(factor_cnts_set) > 1:\n            print(f\"Mismatch in factor_cnts\
    \ for number {num}\")\n            for name, res in factor_cnts_results:\n   \
    \             print(f\"{name}: {res}\")\n            correct = False\n       \
    \     break\n    if correct:\n        print(\"All methods produce correct results.\"\
    )\n    return correct\n\ndef benchmark_specific_cases(sieves, N, repetitions=50,\
    \ warm_up_runs=3):\n    # Benchmarking factorials and powers of 2\n    factorial_numbers\
    \ = []\n    max_i = 20  # Adjust as needed for more factorials\n    for i in range(1,\
    \ max_i + 1):\n        fact = math.factorial(i)\n        if fact >= N:\n     \
    \       break\n        factorial_numbers.append(fact)\n    \n    # Extend the\
    \ list by repeating numbers to increase sample size\n    factorial_numbers *=\
    \ repetitions  # Repeat the list 'repetitions' times\n    random.shuffle(factorial_numbers)\
    \  # Shuffle to randomize the order\n\n    powers_of_two = [1 << k for k in range(1,\
    \ int(math.log2(N)) + 1)]\n    powers_of_two *= repetitions  # Repeat the list\
    \ 'repetitions' times\n    random.shuffle(powers_of_two)  # Shuffle to randomize\
    \ the order\n\n    specific_cases_results = []\n\n    # Warm-up phase\n    warm_up_methods(sieves,\
    \ factorial_numbers + powers_of_two, warm_up_runs)\n\n    for case_name, numbers\
    \ in [('Factorials', factorial_numbers), ('PowersOfTwo', powers_of_two)]:\n  \
    \      num_numbers = len(numbers)\n        for sieve_name, sieve in sieves.items():\n\
    \            if num_numbers == 0:\n                continue  # Skip if no numbers\
    \ to test\n            print(f\"Benchmarking {sieve_name} on {case_name} with\
    \ N = {N}\")\n            method = sieve.factor_cnts\n            start_time =\
    \ time.perf_counter()\n            for num in numbers:\n                method(num)\n\
    \            total_time = time.perf_counter() - start_time\n            avg_time\
    \ = total_time / num_numbers\n            specific_cases_results.append({\n  \
    \              'Case': case_name,\n                'Sieve': sieve_name,\n    \
    \            'AvgTimePerNumber': avg_time,\n                'NumNumbers': num_numbers,\n\
    \                'N': N\n            })\n    return specific_cases_results\n\n\
    def plot_results(construction_df, methods_df, specific_cases_df):\n    # Plot\
    \ construction times\n    plt.figure(figsize=(10, 6))\n    for sieve in construction_df['Sieve'].unique():\n\
    \        sieve_data = construction_df[construction_df['Sieve'] == sieve]\n   \
    \     sieve_data = sieve_data.sort_values('N')  # Ensure data is sorted by N\n\
    \        plt.plot(sieve_data['N'], sieve_data['ConstructionTime'], marker='o',\
    \ label=sieve)\n    plt.xlabel('N')\n    plt.ylabel('Construction Time (s)')\n\
    \    plt.title('Sieve Construction Time')\n    plt.legend()\n    plt.xscale('log')\n\
    \    plt.yscale('log')\n    plt.grid(True)\n    plt.show()\n\n    # Plot method\
    \ average times per number\n    for method in methods_df['Method'].unique():\n\
    \        plt.figure(figsize=(10, 6))\n        for sieve in methods_df['Sieve'].unique():\n\
    \            sieve_data = methods_df[(methods_df['Sieve'] == sieve) & (methods_df['Method']\
    \ == method)]\n            sieve_data = sieve_data.sort_values('N')  # Ensure\
    \ data is sorted by N\n            plt.plot(sieve_data['N'], sieve_data['AvgTimePerNumber'],\
    \ marker='o', label=sieve)\n        plt.xlabel('N')\n        plt.ylabel('Average\
    \ Time per Number (s)')\n        plt.title(f'Method {method} Average Time per\
    \ Number')\n        plt.legend()\n        plt.xscale('log')\n        plt.yscale('log')\n\
    \        plt.grid(True)\n        plt.show()\n\n    # Compute and plot percentage\
    \ speedup for methods\n    baseline_sieve = 'Sieve'  # Set the baseline sieve\n\
    \    for method in methods_df['Method'].unique():\n        plt.figure(figsize=(10,\
    \ 6))\n        # Get the baseline timings\n        baseline_data = methods_df[(methods_df['Sieve']\
    \ == baseline_sieve) & (methods_df['Method'] == method)]\n        baseline_data\
    \ = baseline_data[['N', 'AvgTimePerNumber']].set_index('N')\n        for sieve\
    \ in methods_df['Sieve'].unique():\n            if sieve == baseline_sieve:\n\
    \                continue\n            sieve_data = methods_df[(methods_df['Sieve']\
    \ == sieve) & (methods_df['Method'] == method)]\n            sieve_data = sieve_data[['N',\
    \ 'AvgTimePerNumber']].set_index('N')\n            # Align data on N\n       \
    \     combined = baseline_data.join(sieve_data, lsuffix='_baseline', rsuffix='_other',\
    \ how='inner')\n            # Compute percentage speedup\n            combined['PercentSpeedup']\
    \ = ((combined['AvgTimePerNumber_baseline'] - combined['AvgTimePerNumber_other'])\
    \ / combined['AvgTimePerNumber_baseline']) * 100\n            combined = combined.reset_index()\n\
    \            combined = combined.sort_values('N')\n            plt.plot(combined['N'],\
    \ combined['PercentSpeedup'], marker='o', label=sieve)\n        plt.xlabel('N')\n\
    \        plt.ylabel('Percentage Speedup (%)')\n        plt.title(f'Method {method}\
    \ Percentage Speedup over {baseline_sieve}')\n        plt.legend()\n        plt.xscale('log')\n\
    \        plt.grid(True)\n        plt.show()\n\n    # Compute and plot percentage\
    \ speedup for specific cases\n    for case in specific_cases_df['Case'].unique():\n\
    \        plt.figure(figsize=(10, 6))\n        # Get the baseline timings\n   \
    \     baseline_data = specific_cases_df[(specific_cases_df['Sieve'] == baseline_sieve)\
    \ & (specific_cases_df['Case'] == case)]\n        baseline_data = baseline_data[['N',\
    \ 'AvgTimePerNumber']].set_index('N')\n        for sieve in specific_cases_df['Sieve'].unique():\n\
    \            if sieve == baseline_sieve:\n                continue\n         \
    \   sieve_data = specific_cases_df[(specific_cases_df['Sieve'] == sieve) & (specific_cases_df['Case']\
    \ == case)]\n            sieve_data = sieve_data[['N', 'AvgTimePerNumber']].set_index('N')\n\
    \            # Align data on N\n            combined = baseline_data.join(sieve_data,\
    \ lsuffix='_baseline', rsuffix='_other', how='inner')\n            # Compute percentage\
    \ speedup\n            combined['PercentSpeedup'] = ((combined['AvgTimePerNumber_baseline']\
    \ - combined['AvgTimePerNumber_other']) / combined['AvgTimePerNumber_baseline'])\
    \ * 100\n            combined = combined.reset_index()\n            combined =\
    \ combined.sort_values('N')\n            plt.plot(combined['N'], combined['PercentSpeedup'],\
    \ marker='o', label=sieve)\n        plt.xlabel('N')\n        plt.ylabel('Percentage\
    \ Speedup (%)')\n        plt.title(f'{case} Percentage Speedup over {baseline_sieve}')\n\
    \        plt.legend()\n        plt.xscale('log')\n        plt.grid(True)\n   \
    \     plt.show()\n\n    # Compute and plot percentage speedup for construction\
    \ times\n    plt.figure(figsize=(10, 6))\n    # Get the baseline timings\n   \
    \ baseline_data = construction_df[construction_df['Sieve'] == baseline_sieve]\n\
    \    baseline_data = baseline_data[['N', 'ConstructionTime']].set_index('N')\n\
    \    for sieve in construction_df['Sieve'].unique():\n        if sieve == baseline_sieve:\n\
    \            continue\n        sieve_data = construction_df[construction_df['Sieve']\
    \ == sieve]\n        sieve_data = sieve_data[['N', 'ConstructionTime']].set_index('N')\n\
    \        # Align data on N\n        combined = baseline_data.join(sieve_data,\
    \ lsuffix='_baseline', rsuffix='_other', how='inner')\n        # Compute percentage\
    \ speedup\n        combined['PercentSpeedup'] = ((combined['ConstructionTime_baseline']\
    \ - combined['ConstructionTime_other']) / combined['ConstructionTime_baseline'])\
    \ * 100\n        combined = combined.reset_index()\n        combined = combined.sort_values('N')\n\
    \        plt.plot(combined['N'], combined['PercentSpeedup'], marker='o', label=sieve)\n\
    \    plt.xlabel('N')\n    plt.ylabel('Percentage Speedup (%)')\n    plt.title(f'Construction\
    \ Time Percentage Speedup over {baseline_sieve}')\n    plt.legend()\n    plt.xscale('log')\n\
    \    plt.grid(True)\n    plt.show()\n\ndef main():\n    # Create a finer list\
    \ of N values, ranging from 1e5 to 1e8 with more steps\n    Ns = [int(N) for N\
    \ in np.logspace(5, 8, num=30)]  # 30 steps from 1e5 to 1e8\n    num_tests = 20000\
    \  # Increased number of random numbers to test methods on\n\n    construction_results\
    \ = []\n    method_results = []\n    specific_cases_results = []\n\n    for N_data\
    \ in benchmark_construction(Ns):\n        N, sieves, construction_timings = N_data\n\
    \        construction_results.extend(construction_timings)\n\n        # Generate\
    \ random test numbers\n        test_numbers = [random.randint(2, N - 1) for _\
    \ in range(num_tests)]\n\n        method_timings = benchmark_methods(sieves, test_numbers,\
    \ N, warm_up_runs=3)\n        method_results.extend(method_timings)\n\n      \
    \  print(f\"\\nVerifying correctness of methods for N = {N}...\")\n        verify_correctness(sieves,\
    \ test_numbers[:100])  # Check correctness for first 100 numbers\n\n        specific_case_timings\
    \ = benchmark_specific_cases(sieves, N, repetitions=50, warm_up_runs=3)\n    \
    \    specific_cases_results.extend(specific_case_timings)\n\n    # Convert results\
    \ to DataFrames\n    construction_df = pd.DataFrame(construction_results)\n  \
    \  methods_df = pd.DataFrame(method_results)\n    specific_cases_df = pd.DataFrame(specific_cases_results)\n\
    \n    # Plotting\n    plot_results(construction_df, methods_df, specific_cases_df)\n\
    \nif __name__ == \"__main__\":\n    main()"
  dependsOn:
  - cp_library/math/table/sieve_cls.py
  - cp_library/math/table/linear_sieve_cls.py
  - cp_library/math/table/linear_sieve_cnts_cls.py
  - cp_library/math/table/sieve_proto.py
  - cp_library/math/table/primes_cls.py
  isVerificationFile: false
  path: cp_library/math/table/sieve_benchmarks.py
  requiredBy: []
  timestamp: '2024-11-15 01:34:01+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/math/table/sieve_benchmarks.py
layout: document
redirect_from:
- /library/cp_library/math/table/sieve_benchmarks.py
- /library/cp_library/math/table/sieve_benchmarks.py.html
title: cp_library/math/table/sieve_benchmarks.py
---
