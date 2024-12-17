---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/trie_cls.py
    title: cp_library/ds/trie_cls.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/abc362_q_count_substring_query_ahocorasick.test.py
    title: test/abc362_q_count_substring_query_ahocorasick.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2578\n             https://kobejean.github.io/cp-library               \n'''\n\
    from collections import deque\nfrom typing import Dict, List, Optional\n\nclass\
    \ Trie:\n    __slots__ = 'dic', 'parent', 'last', 'count', 'word'\n\n    def __init__(self):\n\
    \        self.dic: Dict[str, Trie] = {}\n        self.parent: Optional[Trie] =\
    \ None\n        self.last: str = \"\"\n        self.count: int = 0\n        self.word:\
    \ bool = False\n    \n    def add(self, word: str) -> None:\n        p = self\n\
    \        for c in word:\n            if c not in p.dic:   \n                p.dic[c]\
    \ = type(self)()\n            parent = p\n            p = p.dic[c]\n         \
    \   p.parent = parent\n            p.last = c\n        p.word = True\n    \n \
    \   def find(self, prefix: str) -> 'Trie':\n        node = self\n        for char\
    \ in prefix:\n            if char not in node.dic:\n                return None\n\
    \            node = node.dic[char]\n        return node\n    \n    def search(self,\
    \ word: str) -> bool:\n        node = self.find(word)\n        return node.word\
    \ if node is not None else False\n\n    def bfs(self) -> List['Trie']:\n     \
    \   output = []\n        queue = deque([self])\n        while queue:\n       \
    \     p = queue.popleft()\n            output.append(p)\n            queue.extend(p.dic.values())\n\
    \        return output\n    \n    def prefix(self) -> str:\n        output = []\n\
    \        curr = self\n        while curr.parent is not None:\n            output.append(curr.last)\n\
    \            curr = curr.parent\n        return \"\".join(reversed(output))\n\n\
    class AhoCorasick(Trie):\n    __slots__ = 'failed',\n\n    def __init__(self):\n\
    \        super().__init__()\n        self.failed: 'AhoCorasick' = None\n\n   \
    \ def build_fail(self):\n        arr_bfs = self.bfs()\n        for p in arr_bfs:\n\
    \            curr = p.parent\n            if curr:\n                c = p.last\n\
    \                while curr.failed:\n                    if c in curr.failed.dic:\n\
    \                        p.failed = curr.failed.dic[c]\n                     \
    \   break\n                    curr = curr.failed\n                else:\n   \
    \                 p.failed = self\n        self.failed = self\n        return\
    \ arr_bfs\n\n    def count_freq(self, text: str) -> dict[str, int]:\n        arr_bfs\
    \ = self.build_fail()\n        p = self\n        for c in text:\n            while\
    \ p != self and c not in p.dic:\n                p = p.failed\n            p =\
    \ p.dic.get(c, self)\n            p.count += 1\n\n        output = {}\n      \
    \  for i in range(len(arr_bfs) - 1, 0, -1):\n            p = arr_bfs[i]\n    \
    \        p.failed.count += p.count\n            if p.word:\n                output[p.prefix()]\
    \ = p.count\n        return output\n"
  code: "import cp_library.ds.__header__\nfrom cp_library.ds.trie_cls import Trie\n\
    \nclass AhoCorasick(Trie):\n    __slots__ = 'failed',\n\n    def __init__(self):\n\
    \        super().__init__()\n        self.failed: 'AhoCorasick' = None\n\n   \
    \ def build_fail(self):\n        arr_bfs = self.bfs()\n        for p in arr_bfs:\n\
    \            curr = p.parent\n            if curr:\n                c = p.last\n\
    \                while curr.failed:\n                    if c in curr.failed.dic:\n\
    \                        p.failed = curr.failed.dic[c]\n                     \
    \   break\n                    curr = curr.failed\n                else:\n   \
    \                 p.failed = self\n        self.failed = self\n        return\
    \ arr_bfs\n\n    def count_freq(self, text: str) -> dict[str, int]:\n        arr_bfs\
    \ = self.build_fail()\n        p = self\n        for c in text:\n            while\
    \ p != self and c not in p.dic:\n                p = p.failed\n            p =\
    \ p.dic.get(c, self)\n            p.count += 1\n\n        output = {}\n      \
    \  for i in range(len(arr_bfs) - 1, 0, -1):\n            p = arr_bfs[i]\n    \
    \        p.failed.count += p.count\n            if p.word:\n                output[p.prefix()]\
    \ = p.count\n        return output\n"
  dependsOn:
  - cp_library/ds/trie_cls.py
  isVerificationFile: false
  path: cp_library/ds/ahocorasick_cls.py
  requiredBy: []
  timestamp: '2024-12-18 08:34:54+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/abc362_q_count_substring_query_ahocorasick.test.py
documentation_of: cp_library/ds/ahocorasick_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/ahocorasick_cls.py
- /library/cp_library/ds/ahocorasick_cls.py.html
title: cp_library/ds/ahocorasick_cls.py
---
