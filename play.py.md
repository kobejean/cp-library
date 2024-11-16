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
  bundledCode: "from cffi import FFI\nfrom enum import IntEnum\nfrom math import isqrt\n\
    \nclass MoOp(IntEnum):\n    ADD_LEFT = 0\n    REMOVE_LEFT = 1\n    ADD_RIGHT =\
    \ 2\n    REMOVE_RIGHT = 3\n    ANSWER = 4\n\nffi = FFI()\n\nffi.cdef(\"\"\"\n\
    \    void process_queries(unsigned long long* ops, int* op_count,\n          \
    \              unsigned long long* queries, int Q, int N,\n                  \
    \      int qbits, int nbits);\n\"\"\")\n\nlib = ffi.verify(\"\"\"\n    #include\
    \ <stdlib.h>\n    #include <math.h>\n    \n    static inline int decode_i(unsigned\
    \ long long bits, int qbits) {\n        return bits & ((1ULL << qbits) - 1);\n\
    \    }\n    \n    static inline int decode_l(unsigned long long bits, int qbits,\
    \ int nbits) {\n        return (bits >> qbits) & ((1ULL << nbits) - 1);\n    }\n\
    \    \n    static inline int decode_r(unsigned long long bits, int qbits, int\
    \ nbits) {\n        return bits >> (qbits + nbits);\n    }\n    \n    static inline\
    \ unsigned long long encode_op(unsigned char op, int a, int b, int c) {\n    \
    \    // Ensure op is only using 3 bits (0-7)\n        unsigned long long result\
    \ = ((unsigned long long)(op & 7) << 61);\n        // Use 20 bits each for a,\
    \ b\n        result |= ((unsigned long long)(a & 0xFFFFF) << 41);\n        result\
    \ |= ((unsigned long long)(b & 0xFFFFF) << 21);\n        // Handle c specially\
    \ for negative numbers\n        if (c < 0) {\n            result |= (1ULL << 20);\
    \  // Set sign bit\n            result |= (unsigned long long)((-c) & 0xFFFFF);\n\
    \        } else {\n            result |= (unsigned long long)(c & 0xFFFFF);\n\
    \        }\n        return result;\n    }\n    \n    static int g_qbits;\n   \
    \ static int g_nbits;\n    static int g_block_size;\n    \n    static int compare_queries(const\
    \ void* a, const void* b) {\n        unsigned long long qa = *(const unsigned\
    \ long long*)a;\n        unsigned long long qb = *(const unsigned long long*)b;\n\
    \        \n        int l_a = decode_l(qa, g_qbits, g_nbits);\n        int l_b\
    \ = decode_l(qb, g_qbits, g_nbits);\n        \n        int block_a = l_a / g_block_size;\n\
    \        int block_b = l_b / g_block_size;\n        \n        if (block_a != block_b)\
    \ \n            return block_a - block_b;\n        \n        int r_a = decode_r(qa,\
    \ g_qbits, g_nbits);\n        int r_b = decode_r(qb, g_qbits, g_nbits);\n    \
    \    \n        return (block_a & 1) ? (r_b - r_a) : (r_a - r_b);\n    }\n    \n\
    \    void process_queries(unsigned long long* ops, int* op_count,\n          \
    \              unsigned long long* queries, int Q, int N,\n                  \
    \      int qbits, int nbits) {\n        g_qbits = qbits;\n        g_nbits = nbits;\n\
    \        g_block_size = (int)sqrt(N);\n        \n        qsort(queries, Q, sizeof(unsigned\
    \ long long), compare_queries);\n        \n        int nl = 0, nr = 0;\n     \
    \   int op_idx = 0;\n        \n        for (int q = 0; q < Q; q++) {\n       \
    \     unsigned long long query = queries[q];\n            int i = decode_i(query,\
    \ qbits);\n            int l = decode_l(query, qbits, nbits);\n            int\
    \ r = decode_r(query, qbits, nbits);\n            \n            if (l < nl) {\n\
    \                ops[op_idx++] = encode_op(0, nl - 1, l - 1, -1);  // ADD_LEFT\n\
    \            } \n            else if (l > nl) {\n                ops[op_idx++]\
    \ = encode_op(1, nl, l, 1);  // REMOVE_LEFT\n            }\n            \n   \
    \         if (r > nr) {\n                ops[op_idx++] = encode_op(2, nr, r, 1);\
    \  // ADD_RIGHT\n            }\n            else if (r < nr) {\n             \
    \   ops[op_idx++] = encode_op(3, nr - 1, r - 1, -1);  // REMOVE_RIGHT\n      \
    \      }\n            \n            ops[op_idx++] = encode_op(4, i, l, r);  //\
    \ ANSWER\n            \n            nl = l;\n            nr = r;\n        }\n\
    \        \n        *op_count = op_idx;\n    }\n\"\"\",  extra_compile_args=['-O3',\
    \ '-march=native', '-ffast-math'], extra_link_args=['-O3'])\n\nclass MoAlgorithm:\n\
    \    def encode(self, i, l, r):\n        return (((r << self.nbits) + l) << self.qbits)\
    \ + i\n    \n    def decode_op(self, encoded):\n        op = (encoded >> 61) &\
    \ 7  # Get 3 bits for op\n        a = (encoded >> 41) & 0xFFFFF  # Get 20 bits\
    \ for a\n        b = (encoded >> 21) & 0xFFFFF  # Get 20 bits for b\n        c\
    \ = encoded & 0xFFFFF  # Get value bits\n        sign = (encoded >> 20) & 1  #\
    \ Get sign bit\n        if sign:\n            c = -c\n        return MoOp(op),\
    \ a, b, c\n\n    def __init__(self, queries: list[tuple[int, int]], N: int):\n\
    \        Q = len(queries)\n        self.qbits = Q.bit_length()\n        self.nbits\
    \ = N.bit_length()\n        \n        # Encode queries\n        encoded_queries\
    \ = [self.encode(i, l, r) for i, (l, r) in enumerate(queries)]\n        \n   \
    \     # Prepare C arrays\n        query_arr = ffi.new(\"unsigned long long[]\"\
    , encoded_queries)\n        max_ops = 3 * Q\n        op_arr = ffi.new(\"unsigned\
    \ long long[]\", max_ops)\n        op_count = ffi.new(\"int*\", 0)\n        \n\
    \        # Process queries and generate operations\n        lib.process_queries(op_arr,\
    \ op_count, query_arr, Q, N, \n                          self.qbits, self.nbits)\n\
    \        \n        # Convert to Python list and decode operations\n        self.ops\
    \ = []\n        for i in range(op_count[0]):\n            self.ops.append(self.decode_op(op_arr[i]))\n\
    \n# Test and debug\ndef test():\n    queries = [(0, 3), (1, 4), (2, 5), (0, 2),\
    \ (3, 5), (2, 3)]\n    N = 6\n    \n    mo = MoAlgorithm(queries, N)\n    \n \
    \   print(\"Generated Operations:\")\n    for op in mo.ops:\n        print(op)\n\
    \nif __name__ == \"__main__\":\n    test()\n"
  code: "from cffi import FFI\nfrom enum import IntEnum\nfrom math import isqrt\n\n\
    class MoOp(IntEnum):\n    ADD_LEFT = 0\n    REMOVE_LEFT = 1\n    ADD_RIGHT = 2\n\
    \    REMOVE_RIGHT = 3\n    ANSWER = 4\n\nffi = FFI()\n\nffi.cdef(\"\"\"\n    void\
    \ process_queries(unsigned long long* ops, int* op_count,\n                  \
    \      unsigned long long* queries, int Q, int N,\n                        int\
    \ qbits, int nbits);\n\"\"\")\n\nlib = ffi.verify(\"\"\"\n    #include <stdlib.h>\n\
    \    #include <math.h>\n    \n    static inline int decode_i(unsigned long long\
    \ bits, int qbits) {\n        return bits & ((1ULL << qbits) - 1);\n    }\n  \
    \  \n    static inline int decode_l(unsigned long long bits, int qbits, int nbits)\
    \ {\n        return (bits >> qbits) & ((1ULL << nbits) - 1);\n    }\n    \n  \
    \  static inline int decode_r(unsigned long long bits, int qbits, int nbits) {\n\
    \        return bits >> (qbits + nbits);\n    }\n    \n    static inline unsigned\
    \ long long encode_op(unsigned char op, int a, int b, int c) {\n        // Ensure\
    \ op is only using 3 bits (0-7)\n        unsigned long long result = ((unsigned\
    \ long long)(op & 7) << 61);\n        // Use 20 bits each for a, b\n        result\
    \ |= ((unsigned long long)(a & 0xFFFFF) << 41);\n        result |= ((unsigned\
    \ long long)(b & 0xFFFFF) << 21);\n        // Handle c specially for negative\
    \ numbers\n        if (c < 0) {\n            result |= (1ULL << 20);  // Set sign\
    \ bit\n            result |= (unsigned long long)((-c) & 0xFFFFF);\n        }\
    \ else {\n            result |= (unsigned long long)(c & 0xFFFFF);\n        }\n\
    \        return result;\n    }\n    \n    static int g_qbits;\n    static int\
    \ g_nbits;\n    static int g_block_size;\n    \n    static int compare_queries(const\
    \ void* a, const void* b) {\n        unsigned long long qa = *(const unsigned\
    \ long long*)a;\n        unsigned long long qb = *(const unsigned long long*)b;\n\
    \        \n        int l_a = decode_l(qa, g_qbits, g_nbits);\n        int l_b\
    \ = decode_l(qb, g_qbits, g_nbits);\n        \n        int block_a = l_a / g_block_size;\n\
    \        int block_b = l_b / g_block_size;\n        \n        if (block_a != block_b)\
    \ \n            return block_a - block_b;\n        \n        int r_a = decode_r(qa,\
    \ g_qbits, g_nbits);\n        int r_b = decode_r(qb, g_qbits, g_nbits);\n    \
    \    \n        return (block_a & 1) ? (r_b - r_a) : (r_a - r_b);\n    }\n    \n\
    \    void process_queries(unsigned long long* ops, int* op_count,\n          \
    \              unsigned long long* queries, int Q, int N,\n                  \
    \      int qbits, int nbits) {\n        g_qbits = qbits;\n        g_nbits = nbits;\n\
    \        g_block_size = (int)sqrt(N);\n        \n        qsort(queries, Q, sizeof(unsigned\
    \ long long), compare_queries);\n        \n        int nl = 0, nr = 0;\n     \
    \   int op_idx = 0;\n        \n        for (int q = 0; q < Q; q++) {\n       \
    \     unsigned long long query = queries[q];\n            int i = decode_i(query,\
    \ qbits);\n            int l = decode_l(query, qbits, nbits);\n            int\
    \ r = decode_r(query, qbits, nbits);\n            \n            if (l < nl) {\n\
    \                ops[op_idx++] = encode_op(0, nl - 1, l - 1, -1);  // ADD_LEFT\n\
    \            } \n            else if (l > nl) {\n                ops[op_idx++]\
    \ = encode_op(1, nl, l, 1);  // REMOVE_LEFT\n            }\n            \n   \
    \         if (r > nr) {\n                ops[op_idx++] = encode_op(2, nr, r, 1);\
    \  // ADD_RIGHT\n            }\n            else if (r < nr) {\n             \
    \   ops[op_idx++] = encode_op(3, nr - 1, r - 1, -1);  // REMOVE_RIGHT\n      \
    \      }\n            \n            ops[op_idx++] = encode_op(4, i, l, r);  //\
    \ ANSWER\n            \n            nl = l;\n            nr = r;\n        }\n\
    \        \n        *op_count = op_idx;\n    }\n\"\"\",  extra_compile_args=['-O3',\
    \ '-march=native', '-ffast-math'], extra_link_args=['-O3'])\n\nclass MoAlgorithm:\n\
    \    def encode(self, i, l, r):\n        return (((r << self.nbits) + l) << self.qbits)\
    \ + i\n    \n    def decode_op(self, encoded):\n        op = (encoded >> 61) &\
    \ 7  # Get 3 bits for op\n        a = (encoded >> 41) & 0xFFFFF  # Get 20 bits\
    \ for a\n        b = (encoded >> 21) & 0xFFFFF  # Get 20 bits for b\n        c\
    \ = encoded & 0xFFFFF  # Get value bits\n        sign = (encoded >> 20) & 1  #\
    \ Get sign bit\n        if sign:\n            c = -c\n        return MoOp(op),\
    \ a, b, c\n\n    def __init__(self, queries: list[tuple[int, int]], N: int):\n\
    \        Q = len(queries)\n        self.qbits = Q.bit_length()\n        self.nbits\
    \ = N.bit_length()\n        \n        # Encode queries\n        encoded_queries\
    \ = [self.encode(i, l, r) for i, (l, r) in enumerate(queries)]\n        \n   \
    \     # Prepare C arrays\n        query_arr = ffi.new(\"unsigned long long[]\"\
    , encoded_queries)\n        max_ops = 3 * Q\n        op_arr = ffi.new(\"unsigned\
    \ long long[]\", max_ops)\n        op_count = ffi.new(\"int*\", 0)\n        \n\
    \        # Process queries and generate operations\n        lib.process_queries(op_arr,\
    \ op_count, query_arr, Q, N, \n                          self.qbits, self.nbits)\n\
    \        \n        # Convert to Python list and decode operations\n        self.ops\
    \ = []\n        for i in range(op_count[0]):\n            self.ops.append(self.decode_op(op_arr[i]))\n\
    \n# Test and debug\ndef test():\n    queries = [(0, 3), (1, 4), (2, 5), (0, 2),\
    \ (3, 5), (2, 3)]\n    N = 6\n    \n    mo = MoAlgorithm(queries, N)\n    \n \
    \   print(\"Generated Operations:\")\n    for op in mo.ops:\n        print(op)\n\
    \nif __name__ == \"__main__\":\n    test()"
  dependsOn: []
  isVerificationFile: false
  path: play.py
  requiredBy: []
  timestamp: '2024-11-16 11:24:00+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: play.py
layout: document
redirect_from:
- /library/play.py
- /library/play.py.html
title: play.py
---
