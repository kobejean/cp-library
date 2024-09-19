---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/cht_monotone_add_min_cls.py
    title: cp_library/ds/cht_monotone_add_min_cls.py
  - icon: ':question:'
    path: cp_library/io/parsable_cls.py
    title: cp_library/io/parsable_cls.py
  - icon: ':question:'
    path: cp_library/io/parse_stream_fn.py
    title: cp_library/io/parse_stream_fn.py
  - icon: ':question:'
    path: cp_library/io/read_specs_fn.py
    title: cp_library/io/read_specs_fn.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://atcoder.jp/contests/dp/tasks/dp_z
    links:
    - https://atcoder.jp/contests/dp/tasks/dp_z
  bundledCode: "# verification-helper: PROBLEM https://atcoder.jp/contests/dp/tasks/dp_z\n\
    '''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\n   \
    \          https://kobejean.github.io/cp-library               \n'''\n\nfrom bisect\
    \ import bisect_left\n\nclass CHTMonotoneAddMin:\n    def __init__(self):\n  \
    \      self.hull = []\n\n    def insert(self, m: int, b: int) -> None:\n     \
    \   # Remove lines with greater or equal slopes (maintaining monotonicity)\n \
    \       while self.hull and self.hull[-1][0] <= m:\n            self.hull.pop()\n\
    \n        def is_obsolete():\n            (m1, b1), (m2, b2) = self.hull[-2],\
    \ self.hull[-1]\n            return (b - b1) * (m1 - m2) <= (b2 - b1) * (m1 -\
    \ m)\n        \n        # Remove lines that are no longer part of the lower envelope\n\
    \        while len(self.hull) >= 2 and is_obsolete():\n            self.hull.pop()\n\
    \        \n        self.hull.append((m, b))\n\n    def min(self, x: int) -> int:\n\
    \        def eval(i):\n            m, b = self.hull[i]\n            return m *\
    \ x + b\n        def key(i):\n            m1, b1 = self.hull[i]\n            m2,\
    \ b2 = self.hull[i+1]\n            return (m2-m1)*x + (b2-b1)\n        return\
    \ eval(bisect_left(range(len(self.hull) - 1), 0, key=key))\n\n\nimport sys\nfrom\
    \ typing import Type, TypeVar\n\nT = TypeVar('T')\ndef read(spec: Type[T]|T=[int])\
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
    \ \n    return parse_spec(spec)\n\nN, C = read()\nH = read()\ndp = 0\ncht = CHTMonotoneAddMin()\n\
    \nfor i in range(N-1):\n    m = -2*H[i]\n    b = H[i]**2 + dp\n    cht.insert(m,b)\n\
    \    i+=1\n    dp = cht.min(H[i]) + H[i]**2 + C\n\nprint(dp)\n"
  code: "# verification-helper: PROBLEM https://atcoder.jp/contests/dp/tasks/dp_z\n\
    from cp_library.ds.cht_monotone_add_min_cls import CHTMonotoneAddMin\nfrom cp_library.io.read_specs_fn\
    \ import read\n\nN, C = read()\nH = read()\ndp = 0\ncht = CHTMonotoneAddMin()\n\
    \nfor i in range(N-1):\n    m = -2*H[i]\n    b = H[i]**2 + dp\n    cht.insert(m,b)\n\
    \    i+=1\n    dp = cht.min(H[i]) + H[i]**2 + C\n\nprint(dp)"
  dependsOn:
  - cp_library/ds/cht_monotone_add_min_cls.py
  - cp_library/io/read_specs_fn.py
  - cp_library/io/parse_stream_fn.py
  - cp_library/io/parsable_cls.py
  isVerificationFile: true
  path: test/dp_z_cht_monotone_add_min.test.py
  requiredBy: []
  timestamp: '2024-09-20 02:31:14+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/dp_z_cht_monotone_add_min.test.py
layout: document
redirect_from:
- /verify/test/dp_z_cht_monotone_add_min.test.py
- /verify/test/dp_z_cht_monotone_add_min.test.py.html
title: test/dp_z_cht_monotone_add_min.test.py
---
