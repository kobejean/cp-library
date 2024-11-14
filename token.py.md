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
  bundledCode: 'import sys

    import __pypy__

    sys.stdin._CHUNK_SIZE = 6

    chunked = len(sys.stdin.buffer.peek())

    print("peek", sys.stdin.buffer.peek())

    print("chunked", chunked-len(sys.stdin.buffer.peek()))

    print("tell", sys.stdin.tell(), sys.stdin.buffer.tell())

    print()


    print("readline", sys.stdin.readline())


    print("peek", sys.stdin.buffer.peek())

    print("chunked", chunked-len(sys.stdin.buffer.peek()))

    print("tell", sys.stdin.tell(), sys.stdin.buffer.tell())

    print()


    offset = sys.stdin.buffer.tell()-sys.stdin.tell()

    print("seek", sys.stdin.read(offset), "offset", offset)


    print("peek", sys.stdin.buffer.peek())

    print("chunked", chunked-len(sys.stdin.buffer.peek()))

    print("tell", sys.stdin.tell(), sys.stdin.buffer.tell())



    print("buffer.read", sys.stdin.buffer.read(4))


    print("peek", sys.stdin.buffer.peek())

    print("chunked", chunked-len(sys.stdin.buffer.peek()))

    print("tell", sys.stdin.tell(), sys.stdin.buffer.tell())

    print()



    print("readline", sys.stdin.readline())


    print("peek", sys.stdin.buffer.peek())

    print("chunked", chunked-len(sys.stdin.buffer.peek()))

    print("tell", sys.stdin.tell(), sys.stdin.buffer.tell())

    print()

    '
  code: 'import sys

    import __pypy__

    sys.stdin._CHUNK_SIZE = 6

    chunked = len(sys.stdin.buffer.peek())

    print("peek", sys.stdin.buffer.peek())

    print("chunked", chunked-len(sys.stdin.buffer.peek()))

    print("tell", sys.stdin.tell(), sys.stdin.buffer.tell())

    print()


    print("readline", sys.stdin.readline())


    print("peek", sys.stdin.buffer.peek())

    print("chunked", chunked-len(sys.stdin.buffer.peek()))

    print("tell", sys.stdin.tell(), sys.stdin.buffer.tell())

    print()


    offset = sys.stdin.buffer.tell()-sys.stdin.tell()

    print("seek", sys.stdin.read(offset), "offset", offset)


    print("peek", sys.stdin.buffer.peek())

    print("chunked", chunked-len(sys.stdin.buffer.peek()))

    print("tell", sys.stdin.tell(), sys.stdin.buffer.tell())



    print("buffer.read", sys.stdin.buffer.read(4))


    print("peek", sys.stdin.buffer.peek())

    print("chunked", chunked-len(sys.stdin.buffer.peek()))

    print("tell", sys.stdin.tell(), sys.stdin.buffer.tell())

    print()



    print("readline", sys.stdin.readline())


    print("peek", sys.stdin.buffer.peek())

    print("chunked", chunked-len(sys.stdin.buffer.peek()))

    print("tell", sys.stdin.tell(), sys.stdin.buffer.tell())

    print()'
  dependsOn: []
  isVerificationFile: false
  path: token.py
  requiredBy: []
  timestamp: '2024-11-15 01:34:01+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: token.py
layout: document
redirect_from:
- /library/token.py
- /library/token.py.html
title: token.py
---
