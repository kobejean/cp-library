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
    \nfrom bisect import bisect_left\nimport heapq\nfrom bitarray import bitarray\n\
    \nclass WaveletMatrix:\n\n    class Level(bitarray):\n        def select(self,\
    \ bit: int, k: int) -> int:\n            def key(i):\n                return self.count(bit,\
    \ 0, i+1)\n            index = bisect_left(range(len(self)), k+1, key=key)\n \
    \           return -1 if index >= len(self) else index\n\n    def __init__(self,\
    \ data: list[int]):\n        self.n = len(data)\n        self.height = max(data).bit_length()\n\
    \        self.rows = []\n        self.start = dict()\n\n        for h in range(self.height\
    \ - 1, -1, -1):\n            bits = WaveletMatrix.Level(self.n)\n            left,\
    \ right = [], []\n\n            for i, num in enumerate(data):\n             \
    \   if num >> h & 1:\n                    bits[i] = 1\n                    right.append(num)\n\
    \                else:\n                    bits[i] = 0\n                    left.append(num)\n\
    \n            self.rows.append((h,bits))\n            data = left + right\n  \
    \      \n        for i in range(self.n-1,-1,-1):\n            self.start[data[i]]\
    \ = i \n    \n    def access(self, i: int) -> int:\n        if i < 0 or i >= self.n:\n\
    \            raise IndexError(\"Index out of range\")\n\n        val = 0\n   \
    \     for _, row in self.rows:\n            bit, val = row[i], (val << 1) | row[i]\n\
    \            i = row.count(bit, 0, i) + row.count(0)*bit\n\n        return val\n\
    \n    def count(self, val: int, i: int) -> int:\n        if i <= 0 or val not\
    \ in self.start: return 0\n\n        for h, row in self.rows:\n            bit\
    \ = val >> h & 1\n            i = row.count(bit, 0, i) + row.count(0)*bit\n\n\
    \        return i - self.start[val]\n         \n    def select(self, val: int,\
    \ k: int) -> int:\n        \"\"\"\n        Find the 0-indexed position of the\
    \ `k+1`-th occurance of `val`.\n        \"\"\"\n        if k < 0 or val not in\
    \ self.start:\n            return -1\n        \n        idx = self.start[val]+k\n\
    \        for h, row in reversed(self.rows):\n            bit = val >> h & 1\n\
    \            idx = row.select(bit, idx - row.count(0)*bit)\n            if idx\
    \ == -1: return -1\n\n        return idx\n\n    def quantile(self, l: int, r:\
    \ int, k: int) -> int:\n        \"\"\"\n        Find the k-th smallest element\
    \ in the range [l, r).\n        k is 0-indexed, so k=0 returns the minimum element\
    \ in the range.\n        \"\"\"\n        if r > self.n or l >= r or k >= r - l:\n\
    \            return -1\n\n        val = 0\n        for _, row in self.rows:\n\
    \            cnt0lr = row.count(0, l, r)\n            bit = 0 if k < cnt0lr else\
    \ 1\n            if bit:\n                k -= cnt0lr\n                cnt0l =\
    \ row.count(0, l)\n                l += cnt0l         # add 0s in [l,N)\n    \
    \            r += cnt0l+cnt0lr  # add 0s in [l,N)\n            else:\n       \
    \         l = row.count(0, 0, l) # 0s in [0,l)\n                r = l+cnt0lr \
    \          # 0s in [0,r)\n            val = (val << 1) | bit\n        return val\n\
    \n    def topk(self, l: int, r: int, k: int) -> list[tuple[int, int]]:\n     \
    \   \"\"\"\n        Find the k most frequent elements in the range [l, r).\n \
    \       \n        :param l: start of the range (inclusive)\n        :param r:\
    \ end of the range (exclusive)\n        :param k: number of top elements to return\n\
    \        :return: list of (value, frequency) pairs, sorted by frequency (descending),\
    \ then by value (descending)\n        \"\"\"\n        if r > self.n or l >= r\
    \ or k <= 0:\n            return []\n\n        heap = []\n        \n        def\
    \ dfs(l: int, r: int, depth: int, val: int):\n            if l >= r:\n       \
    \         return\n            \n            if depth == self.height:\n       \
    \         count = r - l\n                heapq.heappush(heap, (-count, -val, val,\
    \ count))\n                return\n\n            h, row = self.rows[depth]\n \
    \           cnt0 = row.count(0, l, r)\n            cnt1 = r - l - cnt0\n\n   \
    \         # Process 1-bits (larger values) first\n            if cnt1 > 0:\n \
    \               next_l = row.count(0, 0, l) + row.count(0)\n                next_r\
    \ = next_l + cnt1\n                dfs(next_l, next_r, depth + 1, val | (1 <<\
    \ (self.height - depth - 1)))\n\n            # Then process 0-bits\n         \
    \   if cnt0 > 0:\n                next_l = row.count(0, 0, l)\n              \
    \  next_r = next_l + cnt0\n                dfs(next_l, next_r, depth + 1, val)\n\
    \n        dfs(l, r, 0, 0)\n        \n        result = []\n        while heap and\
    \ len(result) < k:\n            _, _, val, count = heapq.heappop(heap)\n     \
    \       result.append((val, count))\n        \n        return result\n"
  code: "import cp_library.ds.__header__\n\nfrom bisect import bisect_left\nimport\
    \ heapq\nfrom bitarray import bitarray\n\nclass WaveletMatrix:\n\n    class Level(bitarray):\n\
    \        def select(self, bit: int, k: int) -> int:\n            def key(i):\n\
    \                return self.count(bit, 0, i+1)\n            index = bisect_left(range(len(self)),\
    \ k+1, key=key)\n            return -1 if index >= len(self) else index\n\n  \
    \  def __init__(self, data: list[int]):\n        self.n = len(data)\n        self.height\
    \ = max(data).bit_length()\n        self.rows = []\n        self.start = dict()\n\
    \n        for h in range(self.height - 1, -1, -1):\n            bits = WaveletMatrix.Level(self.n)\n\
    \            left, right = [], []\n\n            for i, num in enumerate(data):\n\
    \                if num >> h & 1:\n                    bits[i] = 1\n         \
    \           right.append(num)\n                else:\n                    bits[i]\
    \ = 0\n                    left.append(num)\n\n            self.rows.append((h,bits))\n\
    \            data = left + right\n        \n        for i in range(self.n-1,-1,-1):\n\
    \            self.start[data[i]] = i \n    \n    def access(self, i: int) -> int:\n\
    \        if i < 0 or i >= self.n:\n            raise IndexError(\"Index out of\
    \ range\")\n\n        val = 0\n        for _, row in self.rows:\n            bit,\
    \ val = row[i], (val << 1) | row[i]\n            i = row.count(bit, 0, i) + row.count(0)*bit\n\
    \n        return val\n\n    def count(self, val: int, i: int) -> int:\n      \
    \  if i <= 0 or val not in self.start: return 0\n\n        for h, row in self.rows:\n\
    \            bit = val >> h & 1\n            i = row.count(bit, 0, i) + row.count(0)*bit\n\
    \n        return i - self.start[val]\n         \n    def select(self, val: int,\
    \ k: int) -> int:\n        \"\"\"\n        Find the 0-indexed position of the\
    \ `k+1`-th occurance of `val`.\n        \"\"\"\n        if k < 0 or val not in\
    \ self.start:\n            return -1\n        \n        idx = self.start[val]+k\n\
    \        for h, row in reversed(self.rows):\n            bit = val >> h & 1\n\
    \            idx = row.select(bit, idx - row.count(0)*bit)\n            if idx\
    \ == -1: return -1\n\n        return idx\n\n    def quantile(self, l: int, r:\
    \ int, k: int) -> int:\n        \"\"\"\n        Find the k-th smallest element\
    \ in the range [l, r).\n        k is 0-indexed, so k=0 returns the minimum element\
    \ in the range.\n        \"\"\"\n        if r > self.n or l >= r or k >= r - l:\n\
    \            return -1\n\n        val = 0\n        for _, row in self.rows:\n\
    \            cnt0lr = row.count(0, l, r)\n            bit = 0 if k < cnt0lr else\
    \ 1\n            if bit:\n                k -= cnt0lr\n                cnt0l =\
    \ row.count(0, l)\n                l += cnt0l         # add 0s in [l,N)\n    \
    \            r += cnt0l+cnt0lr  # add 0s in [l,N)\n            else:\n       \
    \         l = row.count(0, 0, l) # 0s in [0,l)\n                r = l+cnt0lr \
    \          # 0s in [0,r)\n            val = (val << 1) | bit\n        return val\n\
    \n    def topk(self, l: int, r: int, k: int) -> list[tuple[int, int]]:\n     \
    \   \"\"\"\n        Find the k most frequent elements in the range [l, r).\n \
    \       \n        :param l: start of the range (inclusive)\n        :param r:\
    \ end of the range (exclusive)\n        :param k: number of top elements to return\n\
    \        :return: list of (value, frequency) pairs, sorted by frequency (descending),\
    \ then by value (descending)\n        \"\"\"\n        if r > self.n or l >= r\
    \ or k <= 0:\n            return []\n\n        heap = []\n        \n        def\
    \ dfs(l: int, r: int, depth: int, val: int):\n            if l >= r:\n       \
    \         return\n            \n            if depth == self.height:\n       \
    \         count = r - l\n                heapq.heappush(heap, (-count, -val, val,\
    \ count))\n                return\n\n            h, row = self.rows[depth]\n \
    \           cnt0 = row.count(0, l, r)\n            cnt1 = r - l - cnt0\n\n   \
    \         # Process 1-bits (larger values) first\n            if cnt1 > 0:\n \
    \               next_l = row.count(0, 0, l) + row.count(0)\n                next_r\
    \ = next_l + cnt1\n                dfs(next_l, next_r, depth + 1, val | (1 <<\
    \ (self.height - depth - 1)))\n\n            # Then process 0-bits\n         \
    \   if cnt0 > 0:\n                next_l = row.count(0, 0, l)\n              \
    \  next_r = next_l + cnt0\n                dfs(next_l, next_r, depth + 1, val)\n\
    \n        dfs(l, r, 0, 0)\n        \n        result = []\n        while heap and\
    \ len(result) < k:\n            _, _, val, count = heapq.heappop(heap)\n     \
    \       result.append((val, count))\n        \n        return result\n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/ds/wavelet_matrix_cls.py
  requiredBy: []
  timestamp: '2024-11-03 23:46:02+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/ds/wavelet_matrix_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/wavelet_matrix_cls.py
- /library/cp_library/ds/wavelet_matrix_cls.py.html
title: cp_library/ds/wavelet_matrix_cls.py
---
