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
    \nclass NTT:\n\n    def __init__(self, mod = 998244353) -> None:\n        self.mod\
    \ = mod\n        self.g = self.primitive_root(mod)\n        self.rank2 = ((mod\
    \ - 1) & (1 - mod)).bit_length() - 1\n        self.root = [0] * (self.rank2 +\
    \ 1)\n        self.root[self.rank2] = pow(self.g, (mod - 1) >> self.rank2, mod)\n\
    \        self.iroot = [0] * (self.rank2 + 1)\n        self.iroot[self.rank2] =\
    \ pow(self.root[self.rank2], mod - 2, mod)\n        for i in range(self.rank2\
    \ - 1, -1, -1):\n            self.root[i] = self.root[i + 1] * self.root[i + 1]\
    \ % mod\n            self.iroot[i] = self.iroot[i + 1] * self.iroot[i + 1] % mod\n\
    \ \n        self.rate2 = [0] * max(0, self.rank2 - 1)\n        self.irate2 = [0]\
    \ * max(0, self.rank2 - 1)\n        prod = 1\n        iprod = 1\n        for i\
    \ in range(self.rank2 - 1):\n            self.rate2[i] = self.root[i + 2] * prod\
    \ % mod\n            self.irate2[i] = self.iroot[i + 2] * iprod % mod\n      \
    \      prod *= self.iroot[i + 2]\n            prod %= mod\n            iprod *=\
    \ self.root[i + 2]\n            iprod %= mod\n \n        self.rate3 = [0] * max(0,\
    \ self.rank2 - 2)\n        self.irate3 = [0] * max(0, self.rank2 - 2)\n      \
    \  prod = 1\n        iprod = 1\n        for i in range(self.rank2 - 2):\n    \
    \        self.rate3[i] = self.root[i + 3] * prod % mod\n            self.irate3[i]\
    \ = self.iroot[i + 3] * iprod % mod\n            prod *= self.iroot[i + 3]\n \
    \           prod %= mod\n            iprod *= self.root[i + 3]\n            iprod\
    \ %= mod\n \n    def primitive_root(self, m):\n        if m == 2:\n          \
    \  return 1\n        if m == 167772161:\n            return 3\n        if m ==\
    \ 469762049:\n            return 3\n        if m == 754974721:\n            return\
    \ 11\n        if m == 998244353:\n            return 3\n        divs = [0] * 20\n\
    \        divs[0] = 2\n        cnt = 1\n        x = (m - 1) // 2\n        while\
    \ x % 2 == 0:\n            x //= 2\n        i = 3\n        while i * i <= x:\n\
    \            if x % i == 0:\n                divs[cnt] = i\n                cnt\
    \ += 1\n                while x % i == 0:\n                    x //= i\n     \
    \       i += 2\n        if x > 1:\n            divs[cnt] = x\n            cnt\
    \ += 1\n        g = 2\n        while True:\n            ok = True\n          \
    \  for i in range(cnt):\n                if pow(g, (m - 1) // divs[i], m) == 1:\n\
    \                    ok = False\n                    break\n            if ok:\n\
    \                return g\n            g += 1\n    \n    \n\n    def butterfly(self,\
    \ a):\n        n = len(a)\n        h = (n - 1).bit_length()\n    \n        length\
    \ = 0\n        while length < h:\n            if h - length == 1:\n          \
    \      p = 1 << (h - length - 1)\n                rot = 1\n                for\
    \ s in range(1 << length):\n                    offset = s << (h - length)\n \
    \                   for i in range(p):\n                        l = a[i + offset]\n\
    \                        r = a[i + offset + p] * rot % self.mod\n            \
    \            a[i + offset] = (l + r) % self.mod\n                        a[i +\
    \ offset + p] = (l - r) % self.mod\n                    if s + 1 != (1 << length):\n\
    \                        rot *= self.rate2[(~s & -~s).bit_length() - 1]\n    \
    \                    rot %= self.mod\n                length += 1\n          \
    \  else:\n                # 4-base\n                p = 1 << (h - length - 2)\n\
    \                rot = 1\n                imag = self.root[2]\n              \
    \  for s in range(1 << length):\n                    rot2 = rot * rot % self.mod\n\
    \                    rot3 = rot2 * rot % self.mod\n                    offset\
    \ = s << (h - length)\n                    for i in range(p):\n              \
    \          a0 = a[i + offset]\n                        a1 = a[i + offset + p]\
    \ * rot\n                        a2 = a[i + offset + 2 * p] * rot2\n         \
    \               a3 = a[i + offset + 3 * p] * rot3\n                        a1na3imag\
    \ = (a1 - a3) % self.mod * imag\n                        a[i + offset] = (a0 +\
    \ a2 + a1 + a3) % self.mod\n                        a[i + offset + p] = (a0 +\
    \ a2 - a1 - a3) % self.mod\n                        a[i + offset + 2 * p] = (a0\
    \ - a2 + a1na3imag) % self.mod\n                        a[i + offset + 3 * p]\
    \ = (a0 - a2 - a1na3imag) % self.mod\n                    if s + 1 != (1 << length):\n\
    \                        rot *= self.rate3[(~s & -~s).bit_length() - 1]\n    \
    \                    rot %= self.mod\n                length += 2\n    \n    \n\
    \    def butterfly_inv(self, a):\n        n = len(a)\n        h = (n - 1).bit_length()\n\
    \    \n        length = h  # a[i, i+(n<<length), i+2*(n>>length), ...] is transformed\
    \ \n        while length:\n            if length == 1:\n                p = 1\
    \ << (h - length)\n                irot = 1\n                for s in range(1\
    \ << (length - 1)):\n                    offset = s << (h - length + 1)\n    \
    \                for i in range(p):\n                        l = a[i + offset]\n\
    \                        r = a[i + offset + p]\n                        a[i +\
    \ offset] = (l + r) % self.mod\n                        a[i + offset + p] = (l\
    \ - r) * irot % self.mod\n                    if s + 1 != (1 << (length - 1)):\n\
    \                        irot *= self.irate2[(~s & -~s).bit_length() - 1]\n  \
    \                      irot %= self.mod\n                length -= 1\n       \
    \     else:\n                # 4-base\n                p = 1 << (h - length)\n\
    \                irot = 1\n                iimag = self.iroot[2]\n           \
    \     for s in range(1 << (length - 2)):\n                    irot2 = irot * irot\
    \ % self.mod\n                    irot3 = irot2 * irot % self.mod\n          \
    \          offset = s << (h - length + 2)\n                    for i in range(p):\n\
    \                        a0 = a[i + offset]\n                        a1 = a[i\
    \ + offset + p]\n                        a2 = a[i + offset + 2 * p]\n        \
    \                a3 = a[i + offset + 3 * p]\n                        a2na3iimag\
    \ = (a2 - a3) * iimag % self.mod\n                        a[i + offset] = (a0\
    \ + a1 + a2 + a3) % self.mod\n                        a[i + offset + p] = (a0\
    \  - a1 + a2na3iimag) * irot % self.mod\n                        a[i + offset\
    \ + 2 * p] = (a0 + a1 - a2 - a3) * irot2 % self.mod\n                        a[i\
    \ + offset + 3 * p] = (a0  - a1 - a2na3iimag) * irot3 % self.mod\n           \
    \         if s + 1 != (1 << (length - 2)):\n                        irot *= self.irate3[(~s\
    \ & -~s).bit_length() - 1]\n                        irot %= self.mod\n       \
    \         length -= 2\n    \n    \n    def convolution_naive(self, a, b):\n  \
    \      n = len(a)\n        m = len(b)\n        ans = [0] * (n + m - 1)\n     \
    \   if n < m:\n            for j in range(m):\n                for i in range(n):\n\
    \                    ans[i + j] += a[i] * b[j]\n                    ans[i + j]\
    \ %= self.mod\n        else:\n            for i in range(n):\n               \
    \ for j in range(m):\n                    ans[i + j] += a[i] * b[j]\n        \
    \            ans[i + j] %= self.mod\n        return ans\n    \n    \n    def convolution_fft(self,\
    \ a, b):\n        a = a.copy()\n        b = b.copy()\n        n = len(a)\n   \
    \     m = len(b)\n        z = 1 << (n + m - 2).bit_length()\n        a += [0]\
    \ * (z - n)\n        self.butterfly(a)\n        b += [0] * (z - m)\n        self.butterfly(b)\n\
    \        for i in range(z):\n            a[i] *= b[i]\n            a[i] %= self.mod\n\
    \        self.butterfly_inv(a)\n        a = a[:n + m - 1]\n        iz = pow(z,\
    \ self.mod - 2, self.mod)\n        for i in range(n + m - 1):\n            a[i]\
    \ *= iz\n            a[i] %= self.mod\n        return a\n    \n    \n    def convolution(self,\
    \ a, b):\n        n = len(a)\n        m = len(b)\n        if not n or not m:\n\
    \            return []\n        if min(n, m) <= 60:\n            return self.convolution_naive(a,\
    \ b)\n        return self.convolution_fft(a, b)\n\n\n    def cycle_convolution(self,\
    \ a, b):\n        n = len(a)\n        m = len(b)\n        assert n == m\n    \
    \    if n == 0:\n            return []\n        con = self.convolution(a, b)\n\
    \        res = [0]*n\n        for i in range(n-1):\n            res[i] = con[i]\
    \ + con[i+n]\n        res[n-1] = con[n-1]\n        return res\n"
  code: "import cp_library.math.__header__\n\nclass NTT:\n\n    def __init__(self,\
    \ mod = 998244353) -> None:\n        self.mod = mod\n        self.g = self.primitive_root(mod)\n\
    \        self.rank2 = ((mod - 1) & (1 - mod)).bit_length() - 1\n        self.root\
    \ = [0] * (self.rank2 + 1)\n        self.root[self.rank2] = pow(self.g, (mod -\
    \ 1) >> self.rank2, mod)\n        self.iroot = [0] * (self.rank2 + 1)\n      \
    \  self.iroot[self.rank2] = pow(self.root[self.rank2], mod - 2, mod)\n       \
    \ for i in range(self.rank2 - 1, -1, -1):\n            self.root[i] = self.root[i\
    \ + 1] * self.root[i + 1] % mod\n            self.iroot[i] = self.iroot[i + 1]\
    \ * self.iroot[i + 1] % mod\n \n        self.rate2 = [0] * max(0, self.rank2 -\
    \ 1)\n        self.irate2 = [0] * max(0, self.rank2 - 1)\n        prod = 1\n \
    \       iprod = 1\n        for i in range(self.rank2 - 1):\n            self.rate2[i]\
    \ = self.root[i + 2] * prod % mod\n            self.irate2[i] = self.iroot[i +\
    \ 2] * iprod % mod\n            prod *= self.iroot[i + 2]\n            prod %=\
    \ mod\n            iprod *= self.root[i + 2]\n            iprod %= mod\n \n  \
    \      self.rate3 = [0] * max(0, self.rank2 - 2)\n        self.irate3 = [0] *\
    \ max(0, self.rank2 - 2)\n        prod = 1\n        iprod = 1\n        for i in\
    \ range(self.rank2 - 2):\n            self.rate3[i] = self.root[i + 3] * prod\
    \ % mod\n            self.irate3[i] = self.iroot[i + 3] * iprod % mod\n      \
    \      prod *= self.iroot[i + 3]\n            prod %= mod\n            iprod *=\
    \ self.root[i + 3]\n            iprod %= mod\n \n    def primitive_root(self,\
    \ m):\n        if m == 2:\n            return 1\n        if m == 167772161:\n\
    \            return 3\n        if m == 469762049:\n            return 3\n    \
    \    if m == 754974721:\n            return 11\n        if m == 998244353:\n \
    \           return 3\n        divs = [0] * 20\n        divs[0] = 2\n        cnt\
    \ = 1\n        x = (m - 1) // 2\n        while x % 2 == 0:\n            x //=\
    \ 2\n        i = 3\n        while i * i <= x:\n            if x % i == 0:\n  \
    \              divs[cnt] = i\n                cnt += 1\n                while\
    \ x % i == 0:\n                    x //= i\n            i += 2\n        if x >\
    \ 1:\n            divs[cnt] = x\n            cnt += 1\n        g = 2\n       \
    \ while True:\n            ok = True\n            for i in range(cnt):\n     \
    \           if pow(g, (m - 1) // divs[i], m) == 1:\n                    ok = False\n\
    \                    break\n            if ok:\n                return g\n   \
    \         g += 1\n    \n    \n\n    def butterfly(self, a):\n        n = len(a)\n\
    \        h = (n - 1).bit_length()\n    \n        length = 0\n        while length\
    \ < h:\n            if h - length == 1:\n                p = 1 << (h - length\
    \ - 1)\n                rot = 1\n                for s in range(1 << length):\n\
    \                    offset = s << (h - length)\n                    for i in\
    \ range(p):\n                        l = a[i + offset]\n                     \
    \   r = a[i + offset + p] * rot % self.mod\n                        a[i + offset]\
    \ = (l + r) % self.mod\n                        a[i + offset + p] = (l - r) %\
    \ self.mod\n                    if s + 1 != (1 << length):\n                 \
    \       rot *= self.rate2[(~s & -~s).bit_length() - 1]\n                     \
    \   rot %= self.mod\n                length += 1\n            else:\n        \
    \        # 4-base\n                p = 1 << (h - length - 2)\n               \
    \ rot = 1\n                imag = self.root[2]\n                for s in range(1\
    \ << length):\n                    rot2 = rot * rot % self.mod\n             \
    \       rot3 = rot2 * rot % self.mod\n                    offset = s << (h - length)\n\
    \                    for i in range(p):\n                        a0 = a[i + offset]\n\
    \                        a1 = a[i + offset + p] * rot\n                      \
    \  a2 = a[i + offset + 2 * p] * rot2\n                        a3 = a[i + offset\
    \ + 3 * p] * rot3\n                        a1na3imag = (a1 - a3) % self.mod *\
    \ imag\n                        a[i + offset] = (a0 + a2 + a1 + a3) % self.mod\n\
    \                        a[i + offset + p] = (a0 + a2 - a1 - a3) % self.mod\n\
    \                        a[i + offset + 2 * p] = (a0 - a2 + a1na3imag) % self.mod\n\
    \                        a[i + offset + 3 * p] = (a0 - a2 - a1na3imag) % self.mod\n\
    \                    if s + 1 != (1 << length):\n                        rot *=\
    \ self.rate3[(~s & -~s).bit_length() - 1]\n                        rot %= self.mod\n\
    \                length += 2\n    \n    \n    def butterfly_inv(self, a):\n  \
    \      n = len(a)\n        h = (n - 1).bit_length()\n    \n        length = h\
    \  # a[i, i+(n<<length), i+2*(n>>length), ...] is transformed \n        while\
    \ length:\n            if length == 1:\n                p = 1 << (h - length)\n\
    \                irot = 1\n                for s in range(1 << (length - 1)):\n\
    \                    offset = s << (h - length + 1)\n                    for i\
    \ in range(p):\n                        l = a[i + offset]\n                  \
    \      r = a[i + offset + p]\n                        a[i + offset] = (l + r)\
    \ % self.mod\n                        a[i + offset + p] = (l - r) * irot % self.mod\n\
    \                    if s + 1 != (1 << (length - 1)):\n                      \
    \  irot *= self.irate2[(~s & -~s).bit_length() - 1]\n                        irot\
    \ %= self.mod\n                length -= 1\n            else:\n              \
    \  # 4-base\n                p = 1 << (h - length)\n                irot = 1\n\
    \                iimag = self.iroot[2]\n                for s in range(1 << (length\
    \ - 2)):\n                    irot2 = irot * irot % self.mod\n               \
    \     irot3 = irot2 * irot % self.mod\n                    offset = s << (h -\
    \ length + 2)\n                    for i in range(p):\n                      \
    \  a0 = a[i + offset]\n                        a1 = a[i + offset + p]\n      \
    \                  a2 = a[i + offset + 2 * p]\n                        a3 = a[i\
    \ + offset + 3 * p]\n                        a2na3iimag = (a2 - a3) * iimag %\
    \ self.mod\n                        a[i + offset] = (a0 + a1 + a2 + a3) % self.mod\n\
    \                        a[i + offset + p] = (a0  - a1 + a2na3iimag) * irot %\
    \ self.mod\n                        a[i + offset + 2 * p] = (a0 + a1 - a2 - a3)\
    \ * irot2 % self.mod\n                        a[i + offset + 3 * p] = (a0  - a1\
    \ - a2na3iimag) * irot3 % self.mod\n                    if s + 1 != (1 << (length\
    \ - 2)):\n                        irot *= self.irate3[(~s & -~s).bit_length()\
    \ - 1]\n                        irot %= self.mod\n                length -= 2\n\
    \    \n    \n    def convolution_naive(self, a, b):\n        n = len(a)\n    \
    \    m = len(b)\n        ans = [0] * (n + m - 1)\n        if n < m:\n        \
    \    for j in range(m):\n                for i in range(n):\n                \
    \    ans[i + j] += a[i] * b[j]\n                    ans[i + j] %= self.mod\n \
    \       else:\n            for i in range(n):\n                for j in range(m):\n\
    \                    ans[i + j] += a[i] * b[j]\n                    ans[i + j]\
    \ %= self.mod\n        return ans\n    \n    \n    def convolution_fft(self, a,\
    \ b):\n        a = a.copy()\n        b = b.copy()\n        n = len(a)\n      \
    \  m = len(b)\n        z = 1 << (n + m - 2).bit_length()\n        a += [0] * (z\
    \ - n)\n        self.butterfly(a)\n        b += [0] * (z - m)\n        self.butterfly(b)\n\
    \        for i in range(z):\n            a[i] *= b[i]\n            a[i] %= self.mod\n\
    \        self.butterfly_inv(a)\n        a = a[:n + m - 1]\n        iz = pow(z,\
    \ self.mod - 2, self.mod)\n        for i in range(n + m - 1):\n            a[i]\
    \ *= iz\n            a[i] %= self.mod\n        return a\n    \n    \n    def convolution(self,\
    \ a, b):\n        n = len(a)\n        m = len(b)\n        if not n or not m:\n\
    \            return []\n        if min(n, m) <= 60:\n            return self.convolution_naive(a,\
    \ b)\n        return self.convolution_fft(a, b)\n\n\n    def cycle_convolution(self,\
    \ a, b):\n        n = len(a)\n        m = len(b)\n        assert n == m\n    \
    \    if n == 0:\n            return []\n        con = self.convolution(a, b)\n\
    \        res = [0]*n\n        for i in range(n-1):\n            res[i] = con[i]\
    \ + con[i+n]\n        res[n-1] = con[n-1]\n        return res\n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/math/ntt_cls.py
  requiredBy: []
  timestamp: '2024-12-17 21:24:00+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/math/ntt_cls.py
layout: document
redirect_from:
- /library/cp_library/math/ntt_cls.py
- /library/cp_library/math/ntt_cls.py.html
title: cp_library/math/ntt_cls.py
---
