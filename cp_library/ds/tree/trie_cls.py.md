---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/ahocorasick_cls.py
    title: cp_library/ds/tree/ahocorasick_cls.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/atcoder/abc/abc362_q_count_substring_query_ahocorasick.test.py
    title: test/atcoder/abc/abc362_q_count_substring_query_ahocorasick.test.py
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
    from collections import deque\nfrom typing import Dict, List, Optional\n\n\n\n\
    class Trie:\n    __slots__ = 'dic', 'parent', 'last', 'count', 'word'\n\n    def\
    \ __init__(self):\n        self.dic: Dict[str, Trie] = {}\n        self.parent:\
    \ Optional[Trie] = None\n        self.last: str = \"\"\n        self.count: int\
    \ = 0\n        self.word: bool = False\n    \n    def add(self, word: str) ->\
    \ None:\n        p = self\n        for c in word:\n            if c not in p.dic:\
    \   \n                p.dic[c] = type(self)()\n            parent = p\n      \
    \      p = p.dic[c]\n            p.parent = parent\n            p.last = c\n \
    \       p.word = True\n    \n    def find(self, prefix: str) -> 'Trie':\n    \
    \    node = self\n        for char in prefix:\n            if char not in node.dic:\n\
    \                return None\n            node = node.dic[char]\n        return\
    \ node\n    \n    def search(self, word: str) -> bool:\n        node = self.find(word)\n\
    \        return node.word if node is not None else False\n\n    def bfs(self)\
    \ -> List['Trie']:\n        output = []\n        queue = deque([self])\n     \
    \   while queue:\n            p = queue.popleft()\n            output.append(p)\n\
    \            queue.extend(p.dic.values())\n        return output\n    \n    def\
    \ prefix(self) -> str:\n        output = []\n        curr = self\n        while\
    \ curr.parent is not None:\n            output.append(curr.last)\n           \
    \ curr = curr.parent\n        return \"\".join(reversed(output))\n"
  code: "import cp_library.__header__\nfrom collections import deque\nfrom typing\
    \ import Dict, List, Optional\nimport cp_library.ds.__header__\nimport cp_library.ds.tree.__header__\n\
    \nclass Trie:\n    __slots__ = 'dic', 'parent', 'last', 'count', 'word'\n\n  \
    \  def __init__(self):\n        self.dic: Dict[str, Trie] = {}\n        self.parent:\
    \ Optional[Trie] = None\n        self.last: str = \"\"\n        self.count: int\
    \ = 0\n        self.word: bool = False\n    \n    def add(self, word: str) ->\
    \ None:\n        p = self\n        for c in word:\n            if c not in p.dic:\
    \   \n                p.dic[c] = type(self)()\n            parent = p\n      \
    \      p = p.dic[c]\n            p.parent = parent\n            p.last = c\n \
    \       p.word = True\n    \n    def find(self, prefix: str) -> 'Trie':\n    \
    \    node = self\n        for char in prefix:\n            if char not in node.dic:\n\
    \                return None\n            node = node.dic[char]\n        return\
    \ node\n    \n    def search(self, word: str) -> bool:\n        node = self.find(word)\n\
    \        return node.word if node is not None else False\n\n    def bfs(self)\
    \ -> List['Trie']:\n        output = []\n        queue = deque([self])\n     \
    \   while queue:\n            p = queue.popleft()\n            output.append(p)\n\
    \            queue.extend(p.dic.values())\n        return output\n    \n    def\
    \ prefix(self) -> str:\n        output = []\n        curr = self\n        while\
    \ curr.parent is not None:\n            output.append(curr.last)\n           \
    \ curr = curr.parent\n        return \"\".join(reversed(output))\n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/ds/tree/trie_cls.py
  requiredBy:
  - cp_library/ds/tree/ahocorasick_cls.py
  timestamp: '2025-04-06 08:06:21+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/atcoder/abc/abc362_q_count_substring_query_ahocorasick.test.py
documentation_of: cp_library/ds/tree/trie_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/tree/trie_cls.py
- /library/cp_library/ds/tree/trie_cls.py.html
title: cp_library/ds/tree/trie_cls.py
---
