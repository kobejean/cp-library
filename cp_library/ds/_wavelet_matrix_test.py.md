---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: cp_library/ds/wavelet_matrix_cls.py
    title: cp_library/ds/wavelet_matrix_cls.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 94, in bundle\n    return bundler.update(path)\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python_bundle.py\"\
    , line 183, in update\n    self.process_file(path)\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python_bundle.py\"\
    , line 24, in process_file\n    self.bundled_code[file_path] = self.process_imports(tree,\
    \ file_path, source)\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python_bundle.py\"\
    , line 107, in process_imports\n    processor.visit(tree)\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/ast.py\"\
    , line 418, in visit\n    return visitor(node)\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/ast.py\"\
    , line 426, in generic_visit\n    self.visit(item)\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/ast.py\"\
    , line 418, in visit\n    return visitor(node)\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python_bundle.py\"\
    , line 85, in visit_ImportFrom\n    self.process_module(node, module_path, from_import=True,\
    \ import_names=node.names)\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python_bundle.py\"\
    , line 97, in process_module\n    imported_code = self.bundler.import_file(module_path,\
    \ is_top_level)\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python_bundle.py\"\
    , line 31, in import_file\n    self.process_file(file_path)\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python_bundle.py\"\
    , line 21, in process_file\n    with open(file_path, 'r') as file:\nFileNotFoundError:\
    \ [Errno 2] No such file or directory: 'cp_library/wavelet_matrix_cls'\n"
  code: "import unittest\n\nfrom .wavelet_matrix_cls import WaveletMatrix\n\nclass\
    \ TestWaveletMatrix(unittest.TestCase):\n    def setUp(self):\n        self.data\
    \ = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]\n        self.wm = WaveletMatrix(self.data)\n\
    \n    def test_access(self):\n        for i, val in enumerate(self.data):\n  \
    \          self.assertEqual(self.wm.access(i), val, f\"access({i}) should return\
    \ {val}\")\n        \n        with self.assertRaises(IndexError):\n          \
    \  self.wm.access(-1)\n        with self.assertRaises(IndexError):\n         \
    \   self.wm.access(len(self.data))\n\n    def test_count(self):\n        test_cases\
    \ = [\n            (3, 5, 1),  # count of 3 up to index 5 is 1\n            (1,\
    \ 4, 2),  # count of 1 up to index 4 is 2\n            (5, 11, 3),  # count of\
    \ 5 up to the end is 3\n            (9, 6, 1),  # count of 9 up to index 6 is\
    \ 1\n            (7, 11, 0)  # count of 7 (not in the list) is 0\n        ]\n\
    \        for val, index, expected in test_cases:\n            self.assertEqual(self.wm.count(val,\
    \ index), expected, \n                             f\"count({val}, {index}) should\
    \ return {expected}\")\n\n    def test_select(self):\n        test_cases = [\n\
    \            (3, 0, 0),  # 1st occurrence of 3 is at index 0\n            (1,\
    \ 1, 3),  # 2nd occurrence of 1 is at index 3\n            (5, 2, 10),  # 3rd\
    \ occurrence of 5 is at index 10\n            (9, 0, 5),  # 1st occurrence of\
    \ 9 is at index 5\n            (7, 0, -1)  # 7 is not in the list, should return\
    \ -1\n        ]\n        for val, k, expected in test_cases:\n            self.assertEqual(self.wm.select(val,\
    \ k), expected, \n                             f\"select({val}, {k}) should return\
    \ {expected}\")\n    def test_topk(self):\n        test_cases = [\n          \
    \  (0, 11, 3, [(5, 3), (3, 2), (1, 2)]),  # Top 3 elements in the entire array\n\
    \            (0, 5, 2, [(1, 2), (4, 1)]),  # Top 2 elements in the range [0, 5)\n\
    \            (5, 11, 4, [(5, 2), (9, 1), (2, 1), (6, 1)]),  # Top 4 elements in\
    \ the range [5, 11)\n            (0, 11, 1, [(5, 3)]),  # Top 1 element in the\
    \ entire array\n            (0, 11, 11, [(5, 3), (3, 2), (1, 2), (9, 1), (6, 1),\
    \ (4, 1), (2, 1)]),  # All elements\n            (0, 2, 5, [(3, 1), (1, 1)]),\
    \  # Requesting more elements than in the range\n            (5, 6, 1, [(9, 1)]),\
    \  # Top 1 element in a single-element range\n            (0, 0, 1, []),  # Empty\
    \ range\n            (0, 11, 0, [])  # Requesting 0 elements\n        ]\n    \
    \    for l, r, k, expected in test_cases:\n            self.assertEqual(self.wm.topk(l,\
    \ r, k), expected,\n                            f\"topk({l}, {r}, {k}) should\
    \ return {expected}\")\n\n    def test_topk_edge_cases(self):\n        # Test\
    \ with out-of-range indices\n        self.assertEqual(self.wm.topk(-1, 5, 3),\
    \ [], \"Should return empty list for negative start index\")\n        self.assertEqual(self.wm.topk(0,\
    \ 20, 3), [], \"Should return empty list for end index > array length\")\n   \
    \     self.assertEqual(self.wm.topk(5, 3, 2), [], \"Should return empty list when\
    \ start > end\")\n\n        # Test with very large k\n        self.assertEqual(self.wm.topk(0,\
    \ 11, 100), [(5, 3), (3, 2), (1, 2), (9, 1), (6, 1), (4, 1), (2, 1)],\n      \
    \                  \"Should return all elements when k > array length\")\n\nif\
    \ __name__ == \"__main__\":\n    unittest.main()"
  dependsOn:
  - cp_library/ds/wavelet_matrix_cls.py
  isVerificationFile: false
  path: cp_library/ds/_wavelet_matrix_test.py
  requiredBy: []
  timestamp: '2024-09-16 19:46:13+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/ds/_wavelet_matrix_test.py
layout: document
redirect_from:
- /library/cp_library/ds/_wavelet_matrix_test.py
- /library/cp_library/ds/_wavelet_matrix_test.py.html
title: cp_library/ds/_wavelet_matrix_test.py
---
