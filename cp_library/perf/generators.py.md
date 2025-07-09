---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':warning:'
    path: cp_library/perf/examples/rank_benchmark.py
    title: cp_library/perf/examples/rank_benchmark.py
  - icon: ':warning:'
    path: cp_library/perf/examples/simple_usage.py
    title: cp_library/perf/examples/simple_usage.py
  - icon: ':warning:'
    path: perf/bool_list_benchmark.py
    title: perf/bool_list_benchmark.py
  - icon: ':warning:'
    path: perf/rank_perf.py
    title: perf/rank_perf.py
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
    \nimport random\nfrom abc import ABC, abstractmethod\nfrom typing import Any,\
    \ List, Dict\nimport math\n\nclass DataGenerator(ABC):\n    \"\"\"Base class for\
    \ test data generators\"\"\"\n    \n    @abstractmethod\n    def generate(self,\
    \ **params) -> Any:\n        \"\"\"Generate test data based on parameters\"\"\"\
    \n        pass\n\nclass RandomArrayGenerator(DataGenerator):\n    \"\"\"Generate\
    \ random integer arrays\"\"\"\n    \n    def __init__(self, min_val: int = 1,\
    \ max_val: int = None):\n        self.min_val = min_val\n        self.max_val\
    \ = max_val\n    \n    def generate(self, size: int, **params) -> List[int]:\n\
    \        max_val = self.max_val if self.max_val is not None else size\n      \
    \  return [random.randint(self.min_val, max_val) for _ in range(size)]\n\nclass\
    \ SortedArrayGenerator(DataGenerator):\n    \"\"\"Generate sorted arrays\"\"\"\
    \n    \n    def __init__(self, reverse: bool = False, step: int = 1):\n      \
    \  self.reverse = reverse\n        self.step = step\n    \n    def generate(self,\
    \ size: int, **params) -> List[int]:\n        arr = list(range(0, size * self.step,\
    \ self.step))\n        if self.reverse:\n            arr.reverse()\n        return\
    \ arr\n\nclass DuplicatesArrayGenerator(DataGenerator):\n    \"\"\"Generate arrays\
    \ with many duplicate values\"\"\"\n    \n    def __init__(self, num_unique: int\
    \ = 10):\n        self.num_unique = num_unique\n    \n    def generate(self, size:\
    \ int, **params) -> List[int]:\n        return [random.randint(1, self.num_unique)\
    \ for _ in range(size)]\n\nclass DistributionArrayGenerator(DataGenerator):\n\
    \    \"\"\"Generate arrays following specific distributions\"\"\"\n    \n    def\
    \ __init__(self, distribution: str = 'uniform'):\n        self.distribution =\
    \ distribution\n    \n    def generate(self, size: int, **params) -> List[int]:\n\
    \        if self.distribution == 'normal':\n            mean = params.get('mean',\
    \ size // 2)\n            std = params.get('std', size // 10)\n            return\
    \ [int(random.gauss(mean, std)) for _ in range(size)]\n        \n        elif\
    \ self.distribution == 'exponential':\n            rate = params.get('rate', 1.0\
    \ / (size // 10))\n            return [int(random.expovariate(rate)) for _ in\
    \ range(size)]\n        \n        elif self.distribution == 'power':\n       \
    \     alpha = params.get('alpha', 2.0)\n            return [int(random.paretovariate(alpha)\
    \ * size // 10) for _ in range(size)]\n        \n        elif self.distribution\
    \ == 'bimodal':\n            # Mix of two normal distributions\n            mean1\
    \ = size // 3\n            mean2 = 2 * size // 3\n            std = size // 20\n\
    \            return [\n                int(random.gauss(mean1 if i % 2 == 0 else\
    \ mean2, std))\n                for i in range(size)\n            ]\n        \n\
    \        else:  # uniform\n            return RandomArrayGenerator().generate(size)\n\
    \nclass PermutationGenerator(DataGenerator):\n    \"\"\"Generate permutations\"\
    \"\"\n    \n    def generate(self, size: int, **params) -> List[int]:\n      \
    \  arr = list(range(size))\n        random.shuffle(arr)\n        return arr\n\n\
    class PlateauArrayGenerator(DataGenerator):\n    \"\"\"Generate arrays with plateaus\
    \ (consecutive equal values)\"\"\"\n    \n    def __init__(self, num_plateaus:\
    \ int = 5):\n        self.num_plateaus = num_plateaus\n    \n    def generate(self,\
    \ size: int, **params) -> List[int]:\n        plateau_size = size // self.num_plateaus\n\
    \        arr = []\n        for i in range(self.num_plateaus):\n            value\
    \ = i * 100\n            arr.extend([value] * plateau_size)\n        \n      \
    \  # Fill remaining with last value\n        while len(arr) < size:\n        \
    \    arr.append((self.num_plateaus - 1) * 100)\n        \n        return arr[:size]\n\
    \nclass SawtoothArrayGenerator(DataGenerator):\n    \"\"\"Generate sawtooth pattern\
    \ arrays\"\"\"\n    \n    def __init__(self, period: int = 10):\n        self.period\
    \ = period\n    \n    def generate(self, size: int, **params) -> List[int]:\n\
    \        return [i % self.period for i in range(size)]\n\nclass AlmostSortedArrayGenerator(DataGenerator):\n\
    \    \"\"\"Generate almost sorted arrays with some inversions\"\"\"\n    \n  \
    \  def __init__(self, inversion_rate: float = 0.05):\n        self.inversion_rate\
    \ = inversion_rate\n    \n    def generate(self, size: int, **params) -> List[int]:\n\
    \        arr = list(range(size))\n        num_swaps = int(size * self.inversion_rate)\n\
    \        \n        for _ in range(num_swaps):\n            i = random.randint(0,\
    \ size - 1)\n            j = random.randint(0, size - 1)\n            arr[i],\
    \ arr[j] = arr[j], arr[i]\n        \n        return arr\n\n# Factory function\
    \ for easy generator creation\ndef create_generator(generator_type: str, **kwargs)\
    \ -> DataGenerator:\n    \"\"\"Create a data generator by type name\"\"\"\n  \
    \  generators = {\n        'random': RandomArrayGenerator,\n        'sorted':\
    \ SortedArrayGenerator,\n        'reverse': lambda: SortedArrayGenerator(reverse=True),\n\
    \        'duplicates': DuplicatesArrayGenerator,\n        'distribution': DistributionArrayGenerator,\n\
    \        'permutation': PermutationGenerator,\n        'plateau': PlateauArrayGenerator,\n\
    \        'sawtooth': SawtoothArrayGenerator,\n        'almost_sorted': AlmostSortedArrayGenerator,\n\
    \    }\n    \n    if generator_type in generators:\n        gen_class = generators[generator_type]\n\
    \        if callable(gen_class) and not isinstance(gen_class, type):\n       \
    \     return gen_class()\n        return gen_class(**kwargs)\n    else:\n    \
    \    raise ValueError(f\"Unknown generator type: {generator_type}\")\n"
  code: "import cp_library.__header__\nimport cp_library.perf.__header__\nimport random\n\
    from abc import ABC, abstractmethod\nfrom typing import Any, List, Dict\nimport\
    \ math\n\nclass DataGenerator(ABC):\n    \"\"\"Base class for test data generators\"\
    \"\"\n    \n    @abstractmethod\n    def generate(self, **params) -> Any:\n  \
    \      \"\"\"Generate test data based on parameters\"\"\"\n        pass\n\nclass\
    \ RandomArrayGenerator(DataGenerator):\n    \"\"\"Generate random integer arrays\"\
    \"\"\n    \n    def __init__(self, min_val: int = 1, max_val: int = None):\n \
    \       self.min_val = min_val\n        self.max_val = max_val\n    \n    def\
    \ generate(self, size: int, **params) -> List[int]:\n        max_val = self.max_val\
    \ if self.max_val is not None else size\n        return [random.randint(self.min_val,\
    \ max_val) for _ in range(size)]\n\nclass SortedArrayGenerator(DataGenerator):\n\
    \    \"\"\"Generate sorted arrays\"\"\"\n    \n    def __init__(self, reverse:\
    \ bool = False, step: int = 1):\n        self.reverse = reverse\n        self.step\
    \ = step\n    \n    def generate(self, size: int, **params) -> List[int]:\n  \
    \      arr = list(range(0, size * self.step, self.step))\n        if self.reverse:\n\
    \            arr.reverse()\n        return arr\n\nclass DuplicatesArrayGenerator(DataGenerator):\n\
    \    \"\"\"Generate arrays with many duplicate values\"\"\"\n    \n    def __init__(self,\
    \ num_unique: int = 10):\n        self.num_unique = num_unique\n    \n    def\
    \ generate(self, size: int, **params) -> List[int]:\n        return [random.randint(1,\
    \ self.num_unique) for _ in range(size)]\n\nclass DistributionArrayGenerator(DataGenerator):\n\
    \    \"\"\"Generate arrays following specific distributions\"\"\"\n    \n    def\
    \ __init__(self, distribution: str = 'uniform'):\n        self.distribution =\
    \ distribution\n    \n    def generate(self, size: int, **params) -> List[int]:\n\
    \        if self.distribution == 'normal':\n            mean = params.get('mean',\
    \ size // 2)\n            std = params.get('std', size // 10)\n            return\
    \ [int(random.gauss(mean, std)) for _ in range(size)]\n        \n        elif\
    \ self.distribution == 'exponential':\n            rate = params.get('rate', 1.0\
    \ / (size // 10))\n            return [int(random.expovariate(rate)) for _ in\
    \ range(size)]\n        \n        elif self.distribution == 'power':\n       \
    \     alpha = params.get('alpha', 2.0)\n            return [int(random.paretovariate(alpha)\
    \ * size // 10) for _ in range(size)]\n        \n        elif self.distribution\
    \ == 'bimodal':\n            # Mix of two normal distributions\n            mean1\
    \ = size // 3\n            mean2 = 2 * size // 3\n            std = size // 20\n\
    \            return [\n                int(random.gauss(mean1 if i % 2 == 0 else\
    \ mean2, std))\n                for i in range(size)\n            ]\n        \n\
    \        else:  # uniform\n            return RandomArrayGenerator().generate(size)\n\
    \nclass PermutationGenerator(DataGenerator):\n    \"\"\"Generate permutations\"\
    \"\"\n    \n    def generate(self, size: int, **params) -> List[int]:\n      \
    \  arr = list(range(size))\n        random.shuffle(arr)\n        return arr\n\n\
    class PlateauArrayGenerator(DataGenerator):\n    \"\"\"Generate arrays with plateaus\
    \ (consecutive equal values)\"\"\"\n    \n    def __init__(self, num_plateaus:\
    \ int = 5):\n        self.num_plateaus = num_plateaus\n    \n    def generate(self,\
    \ size: int, **params) -> List[int]:\n        plateau_size = size // self.num_plateaus\n\
    \        arr = []\n        for i in range(self.num_plateaus):\n            value\
    \ = i * 100\n            arr.extend([value] * plateau_size)\n        \n      \
    \  # Fill remaining with last value\n        while len(arr) < size:\n        \
    \    arr.append((self.num_plateaus - 1) * 100)\n        \n        return arr[:size]\n\
    \nclass SawtoothArrayGenerator(DataGenerator):\n    \"\"\"Generate sawtooth pattern\
    \ arrays\"\"\"\n    \n    def __init__(self, period: int = 10):\n        self.period\
    \ = period\n    \n    def generate(self, size: int, **params) -> List[int]:\n\
    \        return [i % self.period for i in range(size)]\n\nclass AlmostSortedArrayGenerator(DataGenerator):\n\
    \    \"\"\"Generate almost sorted arrays with some inversions\"\"\"\n    \n  \
    \  def __init__(self, inversion_rate: float = 0.05):\n        self.inversion_rate\
    \ = inversion_rate\n    \n    def generate(self, size: int, **params) -> List[int]:\n\
    \        arr = list(range(size))\n        num_swaps = int(size * self.inversion_rate)\n\
    \        \n        for _ in range(num_swaps):\n            i = random.randint(0,\
    \ size - 1)\n            j = random.randint(0, size - 1)\n            arr[i],\
    \ arr[j] = arr[j], arr[i]\n        \n        return arr\n\n# Factory function\
    \ for easy generator creation\ndef create_generator(generator_type: str, **kwargs)\
    \ -> DataGenerator:\n    \"\"\"Create a data generator by type name\"\"\"\n  \
    \  generators = {\n        'random': RandomArrayGenerator,\n        'sorted':\
    \ SortedArrayGenerator,\n        'reverse': lambda: SortedArrayGenerator(reverse=True),\n\
    \        'duplicates': DuplicatesArrayGenerator,\n        'distribution': DistributionArrayGenerator,\n\
    \        'permutation': PermutationGenerator,\n        'plateau': PlateauArrayGenerator,\n\
    \        'sawtooth': SawtoothArrayGenerator,\n        'almost_sorted': AlmostSortedArrayGenerator,\n\
    \    }\n    \n    if generator_type in generators:\n        gen_class = generators[generator_type]\n\
    \        if callable(gen_class) and not isinstance(gen_class, type):\n       \
    \     return gen_class()\n        return gen_class(**kwargs)\n    else:\n    \
    \    raise ValueError(f\"Unknown generator type: {generator_type}\")"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/perf/generators.py
  requiredBy:
  - cp_library/perf/examples/simple_usage.py
  - cp_library/perf/examples/rank_benchmark.py
  - perf/bool_list_benchmark.py
  - perf/rank_perf.py
  timestamp: '2025-07-09 08:31:42+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/perf/generators.py
layout: document
redirect_from:
- /library/cp_library/perf/generators.py
- /library/cp_library/perf/generators.py.html
title: cp_library/perf/generators.py
---
