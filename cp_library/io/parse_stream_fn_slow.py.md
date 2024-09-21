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
    \nimport typing\nfrom collections import deque\nfrom numbers import Number\nfrom\
    \ typing import Collection, Iterator, Type, TypeVar\n\nfrom cp_library.io.parsable_cls\
    \ import Parsable\n\nT = TypeVar('T')\ndef parse_stream(stream: Iterator[str],\
    \ spec: Type[T]|T) -> T:\n\n    def parse_tuple(cls, specs):\n        match specs:\n\
    \            case [spec, end] if end is ...: \n                return cls(parse_line(spec))\n\
    \            case specs:                     \n                return cls(parse_spec(spec)\
    \ for spec in specs)\n\n    def parse_collection(cls, specs) -> list:\n      \
    \  match specs:\n            case [ ] | [_] | set():          \n             \
    \   return cls(parse_line(*specs))\n            case [spec, int() as n]: \n  \
    \              return cls(parse_spec(spec) for _ in range(n))\n            case\
    \ _:\n                raise NotImplementedError()\n\n    def parse_spec(spec):\n\
    \        if args := match_spec(spec, Parsable):\n            cls, args = args\n\
    \            return cls.parse(parse_spec, *args)\n        elif args := match_spec(spec,\
    \ tuple):      \n            return parse_tuple(*args)\n        elif args := match_spec(spec,\
    \ Collection): \n            return parse_collection(*args)\n        elif issubclass(cls\
    \ := type(offset := spec), Number):         \n            return cls(next_token())\
    \ + offset\n        elif callable(cls := spec):                  \n          \
    \  return cls(next_token())\n        else:\n            raise NotImplementedError()\n\
    \n    def next_token():\n        if not queue: queue.extend(next_line())\n   \
    \     return queue.popleft()\n    \n    def parse_line(spec=int):\n        if\
    \ not queue: queue.extend(next_line())\n        while queue: yield parse_spec(spec)\n\
    \        \n    def next_line():\n        return next(stream).rstrip().split()\n\
    \    \n    def match_spec(spec, types):\n        if issubclass(cls := type(specs\
    \ := spec), types):\n            return cls, specs\n        elif (isinstance(spec,\
    \ type) and \n             issubclass(cls := typing.get_origin(spec) or spec,\
    \ types)):\n            return cls, (typing.get_args(spec) or tuple())\n     \
    \   \n    queue = deque() \n    return parse_spec(spec)\n"
  code: "import cp_library.io.__header__\n\nimport typing\nfrom collections import\
    \ deque\nfrom numbers import Number\nfrom typing import Collection, Iterator,\
    \ Type, TypeVar\n\nfrom cp_library.io.parsable_cls import Parsable\n\nT = TypeVar('T')\n\
    def parse_stream(stream: Iterator[str], spec: Type[T]|T) -> T:\n\n    def parse_tuple(cls,\
    \ specs):\n        match specs:\n            case [spec, end] if end is ...: \n\
    \                return cls(parse_line(spec))\n            case specs:       \
    \              \n                return cls(parse_spec(spec) for spec in specs)\n\
    \n    def parse_collection(cls, specs) -> list:\n        match specs:\n      \
    \      case [ ] | [_] | set():          \n                return cls(parse_line(*specs))\n\
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
    \ \n    return parse_spec(spec)\n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/io/parse_stream_fn_slow.py
  requiredBy: []
  timestamp: '2024-09-21 16:44:49+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/io/parse_stream_fn_slow.py
layout: document
redirect_from:
- /library/cp_library/io/parse_stream_fn_slow.py
- /library/cp_library/io/parse_stream_fn_slow.py.html
title: cp_library/io/parse_stream_fn_slow.py
---
