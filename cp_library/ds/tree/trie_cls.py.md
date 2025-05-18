---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/ahocorasick_cls.py
    title: cp_library/ds/tree/ahocorasick_cls.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/atcoder/abc/abc362_g_count_substring_query_ahocorasick.test.py
    title: test/atcoder/abc/abc362_g_count_substring_query_ahocorasick.test.py
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
    from collections import deque\nfrom typing import Optional\n\n\n\nclass Trie:\n\
    \    __slots__ = 'sub', 'par', 'chr', 'cnt', 'word'\n\n    def __init__(T):\n\
    \        T.sub: dict[str, Trie] = {}\n        T.par: Optional[Trie] = None\n \
    \       T.chr: str = \"\"\n        T.cnt: int = 0\n        T.word: bool = False\n\
    \n    def add(T, word: str):\n        (node := T).cnt += 1\n        for chr in\
    \ word:\n            if chr not in node.sub:   \n                node.sub[chr]\
    \ = T.__class__()\n            par, node = node, node.sub[chr]\n            node.par,\
    \ node.chr = par, chr\n            node.cnt += 1\n        node.word = True\n\n\
    \    def remove(T, word: str):\n        node = T.find(word)\n        assert node\
    \ and node.cnt >= 1\n        if node.cnt == 1 and node.par:\n            del node.par.sub[node.chr]\n\
    \        while node:\n            node.cnt -= 1\n            node = node.par\n\
    \    \n    def discard(T, word: str):\n        node = T.find(word)\n        if\
    \ node:\n            if node.par:\n                del node.par.sub[node.chr]\n\
    \            cnt = node.cnt\n            while node:\n                node.cnt\
    \ -= cnt\n                node = node.par\n\n    def find(T, prefix: str, full\
    \ = True) -> Optional['Trie']:\n        node = T\n        for chr in prefix:\n\
    \            if chr not in node.sub: return None if full else node\n         \
    \   node = node.sub[chr]\n        return node\n    \n    def __contains__(T, word:\
    \ str) -> bool:\n        node = T.find(word)\n        return node.word if node\
    \ is not None else False\n\n    def __len__(T):\n        return T.cnt\n\n    def\
    \ __str__(T) -> str:\n        ret, node = [], T\n        while node.par:\n   \
    \         ret.append(node.chr); node = node.par\n        ret.reverse()\n     \
    \   return \"\".join(ret)\n    \n"
  code: "import cp_library.__header__\nfrom collections import deque\nfrom typing\
    \ import Optional\nimport cp_library.ds.__header__\nimport cp_library.ds.tree.__header__\n\
    \nclass Trie:\n    __slots__ = 'sub', 'par', 'chr', 'cnt', 'word'\n\n    def __init__(T):\n\
    \        T.sub: dict[str, Trie] = {}\n        T.par: Optional[Trie] = None\n \
    \       T.chr: str = \"\"\n        T.cnt: int = 0\n        T.word: bool = False\n\
    \n    def add(T, word: str):\n        (node := T).cnt += 1\n        for chr in\
    \ word:\n            if chr not in node.sub:   \n                node.sub[chr]\
    \ = T.__class__()\n            par, node = node, node.sub[chr]\n            node.par,\
    \ node.chr = par, chr\n            node.cnt += 1\n        node.word = True\n\n\
    \    def remove(T, word: str):\n        node = T.find(word)\n        assert node\
    \ and node.cnt >= 1\n        if node.cnt == 1 and node.par:\n            del node.par.sub[node.chr]\n\
    \        while node:\n            node.cnt -= 1\n            node = node.par\n\
    \    \n    def discard(T, word: str):\n        node = T.find(word)\n        if\
    \ node:\n            if node.par:\n                del node.par.sub[node.chr]\n\
    \            cnt = node.cnt\n            while node:\n                node.cnt\
    \ -= cnt\n                node = node.par\n\n    def find(T, prefix: str, full\
    \ = True) -> Optional['Trie']:\n        node = T\n        for chr in prefix:\n\
    \            if chr not in node.sub: return None if full else node\n         \
    \   node = node.sub[chr]\n        return node\n    \n    def __contains__(T, word:\
    \ str) -> bool:\n        node = T.find(word)\n        return node.word if node\
    \ is not None else False\n\n    def __len__(T):\n        return T.cnt\n\n    def\
    \ __str__(T) -> str:\n        ret, node = [], T\n        while node.par:\n   \
    \         ret.append(node.chr); node = node.par\n        ret.reverse()\n     \
    \   return \"\".join(ret)\n    \n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/ds/tree/trie_cls.py
  requiredBy:
  - cp_library/ds/tree/ahocorasick_cls.py
  timestamp: '2025-05-19 05:52:10+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/atcoder/abc/abc362_g_count_substring_query_ahocorasick.test.py
documentation_of: cp_library/ds/tree/trie_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/tree/trie_cls.py
- /library/cp_library/ds/tree/trie_cls.py.html
title: cp_library/ds/tree/trie_cls.py
---
