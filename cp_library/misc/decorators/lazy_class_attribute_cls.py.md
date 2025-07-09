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
    \nclass lazy_class_attribute:\n    def __init__(self, fn):\n        self.fn =\
    \ fn\n        self.value = None\n    \n    def __get__(self, instance, owner):\n\
    \        if self.value is None:\n            # Call with owner (the class) as\
    \ the first argument\n            self.value = self.fn(owner)\n        return\
    \ self.value\n"
  code: "import cp_library.misc.decorators.__header__\n\nclass lazy_class_attribute:\n\
    \    def __init__(self, fn):\n        self.fn = fn\n        self.value = None\n\
    \    \n    def __get__(self, instance, owner):\n        if self.value is None:\n\
    \            # Call with owner (the class) as the first argument\n           \
    \ self.value = self.fn(owner)\n        return self.value"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/misc/decorators/lazy_class_attribute_cls.py
  requiredBy: []
  timestamp: '2025-07-10 00:37:15+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/misc/decorators/lazy_class_attribute_cls.py
layout: document
redirect_from:
- /library/cp_library/misc/decorators/lazy_class_attribute_cls.py
- /library/cp_library/misc/decorators/lazy_class_attribute_cls.py.html
title: cp_library/misc/decorators/lazy_class_attribute_cls.py
---
