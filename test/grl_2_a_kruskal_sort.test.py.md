---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/kruskal_sort_fn.py
    title: cp_library/alg/graph/kruskal_sort_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/dsu_cls.py
    title: cp_library/ds/dsu_cls.py
  - icon: ':question:'
    path: cp_library/io/parsable_cls.py
    title: cp_library/io/parsable_cls.py
  - icon: ':question:'
    path: cp_library/io/parse_stream_fn.py
    title: cp_library/io/parse_stream_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/read_edges_weighted_fn.py
    title: cp_library/io/read_edges_weighted_fn.py
  - icon: ':question:'
    path: cp_library/io/read_specs_fn.py
    title: cp_library/io/read_specs_fn.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/2/GRL_2_A
    links:
    - https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/2/GRL_2_A
  bundledCode: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/2/GRL_2_A\n\
    '''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\n   \
    \          https://kobejean.github.io/cp-library               \n'''\n\nimport\
    \ sys\nfrom typing import Type, TypeVar\n\nT = TypeVar('T')\ndef read(spec: Type[T]|T=[int])\
    \ -> T:\n    return parse_stream(sys.stdin, spec)\n\n\nimport typing\nfrom collections\
    \ import deque\nfrom numbers import Number\nfrom typing import Collection, Iterator,\
    \ Type, TypeVar\n\n\nclass Parsable:\n    @classmethod\n    def parse(cls, parse_spec):\n\
    \        return parse_spec(lambda s: cls(s))\n\nT = TypeVar('T')\ndef parse_stream(stream:\
    \ Iterator[str], spec: Type[T]|T) -> T:\n\n    def parse_tuple(cls, specs):\n\
    \        match specs:\n            case [spec, end] if end is ...: \n        \
    \        return cls(parse_line(spec))\n            case specs:               \
    \      \n                return cls(parse_spec(spec) for spec in specs)\n\n  \
    \  def parse_collection(cls, specs) -> list:\n        match specs:\n         \
    \   case [ ] | [_] | set():          \n                return cls(parse_line(*specs))\n\
    \            case [spec, int() as n]: \n                return cls(parse_spec(spec)\
    \ for _ in range(n))\n            case _:\n                raise NotImplementedError()\n\
    \n    def parse_spec(spec):\n        if args := match_spec(spec, Parsable):\n\
    \            cls, args = args\n            return cls.parse(parse_spec, *args)\n\
    \        elif args := match_spec(spec, tuple):      \n            return parse_tuple(*args)\n\
    \        elif args := match_spec(spec, Collection): \n            return parse_collection(*args)\n\
    \        elif issubclass(cls := type(offset := spec), Number):         \n    \
    \        return cls(next_token()) + offset\n        elif callable(cls := spec):\
    \                  \n            return cls(next_token())\n        else:\n   \
    \         raise NotImplementedError()\n\n    def next_token():\n        if not\
    \ queue: queue.extend(next_line())\n        return queue.popleft()\n    \n   \
    \ def parse_line(spec=int):\n        if not queue: queue.extend(next_line())\n\
    \        while queue: yield parse_spec(spec)\n        \n    def next_line():\n\
    \        return next(stream).rstrip().split()\n    \n    def match_spec(spec,\
    \ types):\n        if issubclass(cls := type(specs := spec), types):\n       \
    \     return cls, specs\n        elif (isinstance(spec, type) and \n         \
    \    issubclass(cls := typing.get_origin(spec) or spec, types)):\n           \
    \ return cls, (typing.get_args(spec) or tuple())\n        \n    queue = deque()\
    \ \n    return parse_spec(spec)\n\ndef read_edges(M, i0=1):\n    return [(w,u,v)\
    \ for u,v,w in read(list[tuple[-i0,-i0,int], M])]\n\n\nclass DSU:\n    def __init__(self,\
    \ n):\n        self.n = n\n        self.par = [-1] * n\n\n    def merge(self,\
    \ u, v):\n        assert 0 <= u < self.n\n        assert 0 <= v < self.n\n\n \
    \       x, y = self.leader(u), self.leader(v)\n        if x == y: return x\n\n\
    \        if -self.par[x] < -self.par[y]:\n            x, y = y, x\n\n        self.par[x]\
    \ += self.par[y]\n        self.par[y] = x\n\n        return x\n\n    def same(self,\
    \ u: int, v: int):\n        assert 0 <= u < self.n\n        assert 0 <= v < self.n\n\
    \        return self.leader(u) == self.leader(v)\n\n    def leader(self, i) ->\
    \ int:\n        assert 0 <= i < self.n\n\n        p = self.par[i]\n        while\
    \ p >= 0:\n            if self.par[p] < 0:\n                return p\n       \
    \     self.par[i], i, p = self.par[p], self.par[p], self.par[self.par[p]]\n\n\
    \        return i\n\n    def size(self, i) -> int:\n        assert 0 <= i < self.n\n\
    \        \n        return -self.par[self.leader(i)]\n\n    def groups(self) ->\
    \ list[list[int]]:\n        leader_buf = [self.leader(i) for i in range(self.n)]\n\
    \n        result = [[] for _ in range(self.n)]\n        for i in range(self.n):\n\
    \            result[leader_buf[i]].append(i)\n\n        return list(filter(lambda\
    \ r: r, result))\n\ndef kruskal(E, N):\n    E.sort(reverse=True)\n    dsu = DSU(N)\n\
    \    MST = []\n    need = N-1\n    while E and need > 0:\n        edge = E.pop()\n\
    \        _,u,v = edge\n        if not dsu.same(u,v):\n            dsu.merge(u,v)\n\
    \            MST.append(edge)\n            need -= 1\n    return MST\n\nN, M =\
    \ read((int,int))\nE = read_edges(M, 0)\nMST = kruskal(E, N)\nans = sum(w for\
    \ w,u,v in MST)\nprint(ans)\n"
  code: '# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/2/GRL_2_A

    from cp_library.io.read_specs_fn import read

    from cp_library.io.read_edges_weighted_fn import read_edges

    from cp_library.alg.graph.kruskal_sort_fn import kruskal


    N, M = read((int,int))

    E = read_edges(M, 0)

    MST = kruskal(E, N)

    ans = sum(w for w,u,v in MST)

    print(ans)'
  dependsOn:
  - cp_library/io/read_specs_fn.py
  - cp_library/io/read_edges_weighted_fn.py
  - cp_library/alg/graph/kruskal_sort_fn.py
  - cp_library/ds/dsu_cls.py
  - cp_library/io/parse_stream_fn.py
  - cp_library/io/parsable_cls.py
  isVerificationFile: true
  path: test/grl_2_a_kruskal_sort.test.py
  requiredBy: []
  timestamp: '2024-09-20 02:31:14+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/grl_2_a_kruskal_sort.test.py
layout: document
redirect_from:
- /verify/test/grl_2_a_kruskal_sort.test.py
- /verify/test/grl_2_a_kruskal_sort.test.py.html
title: test/grl_2_a_kruskal_sort.test.py
---
