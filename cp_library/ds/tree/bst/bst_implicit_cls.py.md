---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/masks/i64_max_cnst.py
    title: cp_library/bit/masks/i64_max_cnst.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/reserve_fn.py
    title: cp_library/ds/reserve_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/bst/bst_cls.py
    title: cp_library/ds/tree/bst/bst_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/bst/bst_updates_cls.py
    title: cp_library/ds/tree/bst/bst_updates_cls.py
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/bst/bst_reversible_cls.py
    title: cp_library/ds/tree/bst/bst_reversible_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/bst/cartesian_tree_implicit_cls.py
    title: cp_library/ds/tree/bst/cartesian_tree_implicit_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/bst/cartesian_tree_reversible_cls.py
    title: cp_library/ds/tree/bst/cartesian_tree_reversible_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/bst/treap_implicit_cls.py
    title: cp_library/ds/tree/bst/treap_implicit_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/bst/treap_monoid_reversible_cls.py
    title: cp_library/ds/tree/bst/treap_monoid_reversible_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/bst/treap_reversible_cls.py
    title: cp_library/ds/tree/bst/treap_reversible_cls.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library-checker/data-structure/range_reverse_range_sum.test.py
    title: test/library-checker/data-structure/range_reverse_range_sum.test.py
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
    \n\ndef reserve(A: list, est_len: int) -> None: ...\ntry:\n    from __pypy__ import\
    \ resizelist_hint\nexcept:\n    def resizelist_hint(A: list, est_len: int):\n\
    \        pass\nreserve = resizelist_hint\n\n\n\n\ni64_max = (1<<63)-1\n\nclass\
    \ BST:\n    __slots__ = 'r'\n    K,sub,st=[-1],[-1,-1],[]\n    def __init__(T):T.r=T._nr()\n\
    \    def _nt(T):return T.__class__()\n    def _nr(T):r=len(T.K);T.K.append(i64_max);T.sub.append(-1);T.sub.append(-1);return\
    \ r\n    def _nn(T,k):n=len(T.K);T.K.append(k);T.sub.append(-1);T.sub.append(-1);return\
    \ n\n    def insert(T,k):T._i(T.r<<1,k,n:=T._nn(k));T._r();return n\n    def get(T,k):\n\
    \        if~(i:=T._f(T.r<<1,k)):return i\n        raise KeyError\n    def pop(T,k):\n\
    \        if ~(i:=T._t(T.r<<1,k)):T._d(i,T.st[-1]);T._r();return i\n        else:T.st.clear();raise\
    \ KeyError\n    def __delitem__(T,k):\n        if~(i:=T._t(T.r<<1,k)):T._d(i,T.st[-1]);T._r()\n\
    \        else:T.st.clear();raise KeyError\n    def __contains__(T,k):return 0<=T._f(T.r<<1,k)\n\
    \    def _f(T,s,k):\n        i = T.sub[s]\n        while~i and T.K[i]!=k:T._p(i);i=T.sub[i<<1|(T.K[i]<k)]\n\
    \        return i\n    def _t(T,s,k):\n        T.st.append(s)\n        while~(i:=T.sub[s])and\
    \ T.K[i]!=k:T._p(i);T.st.append(s:=i<<1|(T.K[i]<k))\n        return i\n    def\
    \ _i(T,s,k,n):\n        T.st.append(s)\n        while ~T.sub[s]:T._p(i:=T.sub[s]);T.st.append(s:=i<<1|(T.K[i]<k))\n\
    \        i,T.sub[s]=T.sub[s],n\n    def _d(T,i,s): raise NotImplemented\n    def\
    \ _r(T):T.st.clear()\n    def _p(T,i): pass\n    @classmethod\n    def reserve(cls,sz):sz+=1;reserve(cls.K,sz);reserve(cls.sub,sz<<1);reserve(cls.st,sz.bit_length()<<1)\n\
    \    def _node_str(T, i): return f\"{T.K[i]}\"\n    def __str__(T):\n        def\
    \ rec(i, pre=\"\", is_right=False):\n            if i == -1: return \"\"\n   \
    \         ret = \"\";T._p(i)\n            if ~(r:=T.sub[i<<1|1]):ret+=rec(r,pre+(\"\
    \   \"if is_right else\"\u2502  \"),True)\n            ret+=pre+(\"\u250C\u2500\
    \ \"if is_right else\"\u2514\u2500 \")+T._node_str(i)+\"\\n\"\n            if\
    \ ~(l:=T.sub[i<<1]):ret+=rec(l,pre+(\"   \"if not is_right else\"\u2502  \"),False)\n\
    \            return ret\n        return rec(T.sub[T.r<<1]).rstrip()\n\nclass BSTUpdates(BST):\n\
    \    def _u(T,i): pass\n    def _r(T):\n        while T.st:T._u(T.st.pop()>>1)\n\
    \nclass BSTSized(BSTUpdates):\n    K,sz,sub,st=[-1],[0,0],[-1,-1],[]\n    def\
    \ _nr(T):T.sz.append(0);T.sz.append(0);return super()._nr()\n    def _nn(T,k):T.sz.append(0);T.sz.append(0);return\
    \ super()._nn(k)\n    def kth(T,k):\n        if 0<=k<len(T):return T._k(T.r<<1,k)\n\
    \        raise KeyError\n    def __len__(T):return T.sz[T.r<<1]\n    def _k(T,s,k):\n\
    \        while ~k:\n            T._p(T.sub[s])\n            if (sz:=T.sz[s:=T.sub[s]<<1])<=k:k-=1+sz;s^=1\n\
    \        return s>>1\n    def _kt(T,s,k):\n        while ~k:\n            T._p(T.sub[s]);T.st.append(s)\n\
    \            if (sz:=T.sz[s:=T.sub[s]<<1])<=k:k-=1+sz;s^=1\n        return s>>1\n\
    \    def _u(T,i):\n        T.sz[s]=T.sz[l<<1]+1+T.sz[l<<1|1] if~(l:=T.sub[s:=i<<1])\
    \ else 0\n        T.sz[s]=T.sz[r<<1]+1+T.sz[r<<1|1] if~(r:=T.sub[s:=i<<1|1]) else\
    \ 0\n    @classmethod\n    def reserve(cls,sz):super().reserve(sz);reserve(cls.sz,(sz+1)<<1)\n\
    \nclass BSTImplicit(BSTSized):\n    K,sz,sub,st=None,[0,0],[-1,-1],[]\n    def\
    \ _nr(T):r=len(T.sz)>>1;T.sz.append(0);T.sz.append(0);T.sub.append(-1);T.sub.append(-1);return\
    \ r\n    def _nn(T,k):n=len(T.sz)>>1;T.sz.append(0);T.sz.append(0);T.sub.append(-1);T.sub.append(-1);return\
    \ n\n    def pop(T,k):\n        if 0<=k<len(T):T._d(i:=T._kt(T.r<<1,k),T.st[-1]);T._r();return\
    \ i\n        else:raise KeyError\n    def __contains__(T,k):raise NotImplemented\n\
    \    def __delitem__(T,k):\n        if 0<=k<len(T):T._d(T._kt(T.r<<1,k),T.st[-1]);T._r()\n\
    \        else:raise KeyError\n    def _f(T,s,k):return T._k(s,k)\n    def _t(T,s,k):return\
    \ T._kt(s,k)\n    def _i(T,s,k,n):T.sub[T._kt(s,k)]=n\n    @classmethod\n    def\
    \ reserve(cls,sz):sz+=1;reserve(cls.st,sz.bit_length()<<1);reserve(cls.sz,sz<<1);reserve(cls.sub,sz<<1)\n\
    \nclass BSTReversible(BSTImplicit):\n    K,rev,sz,sub,st=None,[0],[0,0],[-1,-1],[]\n\
    \    def _nr(T):T.rev.append(0);return super()._nr()\n    def _nn(T,k):T.rev.append(0);return\
    \ super()._nn(k)\n    def _p(T,i):\n        if T.rev[i]:\n            T.sub[l],T.sub[r],T.sz[l],T.sz[r]=T.sub[r:=i<<1|1],T.sub[l:=i<<1],T.sz[r],T.sz[l]\n\
    \            if~(l:=T.sub[l]):T.rev[l]^=1\n            if~(r:=T.sub[r]):T.rev[r]^=1\n\
    \            T.rev[i]=0\n    @classmethod\n    def reserve(cls,sz):super().reserve(sz);reserve(cls.rev,sz+1)\n"
  code: "import cp_library.__header__\nimport cp_library.ds.__header__\nfrom cp_library.ds.reserve_fn\
    \ import reserve\nimport cp_library.ds.tree.__header__\nimport cp_library.ds.tree.bst.__header__\n\
    from cp_library.ds.tree.bst.bst_updates_cls import BSTUpdates\n\nclass BSTSized(BSTUpdates):\n\
    \    K,sz,sub,st=[-1],[0,0],[-1,-1],[]\n    def _nr(T):T.sz.append(0);T.sz.append(0);return\
    \ super()._nr()\n    def _nn(T,k):T.sz.append(0);T.sz.append(0);return super()._nn(k)\n\
    \    def kth(T,k):\n        if 0<=k<len(T):return T._k(T.r<<1,k)\n        raise\
    \ KeyError\n    def __len__(T):return T.sz[T.r<<1]\n    def _k(T,s,k):\n     \
    \   while ~k:\n            T._p(T.sub[s])\n            if (sz:=T.sz[s:=T.sub[s]<<1])<=k:k-=1+sz;s^=1\n\
    \        return s>>1\n    def _kt(T,s,k):\n        while ~k:\n            T._p(T.sub[s]);T.st.append(s)\n\
    \            if (sz:=T.sz[s:=T.sub[s]<<1])<=k:k-=1+sz;s^=1\n        return s>>1\n\
    \    def _u(T,i):\n        T.sz[s]=T.sz[l<<1]+1+T.sz[l<<1|1] if~(l:=T.sub[s:=i<<1])\
    \ else 0\n        T.sz[s]=T.sz[r<<1]+1+T.sz[r<<1|1] if~(r:=T.sub[s:=i<<1|1]) else\
    \ 0\n    @classmethod\n    def reserve(cls,sz):super().reserve(sz);reserve(cls.sz,(sz+1)<<1)\n\
    \nclass BSTImplicit(BSTSized):\n    K,sz,sub,st=None,[0,0],[-1,-1],[]\n    def\
    \ _nr(T):r=len(T.sz)>>1;T.sz.append(0);T.sz.append(0);T.sub.append(-1);T.sub.append(-1);return\
    \ r\n    def _nn(T,k):n=len(T.sz)>>1;T.sz.append(0);T.sz.append(0);T.sub.append(-1);T.sub.append(-1);return\
    \ n\n    def pop(T,k):\n        if 0<=k<len(T):T._d(i:=T._kt(T.r<<1,k),T.st[-1]);T._r();return\
    \ i\n        else:raise KeyError\n    def __contains__(T,k):raise NotImplemented\n\
    \    def __delitem__(T,k):\n        if 0<=k<len(T):T._d(T._kt(T.r<<1,k),T.st[-1]);T._r()\n\
    \        else:raise KeyError\n    def _f(T,s,k):return T._k(s,k)\n    def _t(T,s,k):return\
    \ T._kt(s,k)\n    def _i(T,s,k,n):T.sub[T._kt(s,k)]=n\n    @classmethod\n    def\
    \ reserve(cls,sz):sz+=1;reserve(cls.st,sz.bit_length()<<1);reserve(cls.sz,sz<<1);reserve(cls.sub,sz<<1)\n\
    \nclass BSTReversible(BSTImplicit):\n    K,rev,sz,sub,st=None,[0],[0,0],[-1,-1],[]\n\
    \    def _nr(T):T.rev.append(0);return super()._nr()\n    def _nn(T,k):T.rev.append(0);return\
    \ super()._nn(k)\n    def _p(T,i):\n        if T.rev[i]:\n            T.sub[l],T.sub[r],T.sz[l],T.sz[r]=T.sub[r:=i<<1|1],T.sub[l:=i<<1],T.sz[r],T.sz[l]\n\
    \            if~(l:=T.sub[l]):T.rev[l]^=1\n            if~(r:=T.sub[r]):T.rev[r]^=1\n\
    \            T.rev[i]=0\n    @classmethod\n    def reserve(cls,sz):super().reserve(sz);reserve(cls.rev,sz+1)"
  dependsOn:
  - cp_library/ds/reserve_fn.py
  - cp_library/ds/tree/bst/bst_updates_cls.py
  - cp_library/ds/tree/bst/bst_cls.py
  - cp_library/bit/masks/i64_max_cnst.py
  isVerificationFile: false
  path: cp_library/ds/tree/bst/bst_implicit_cls.py
  requiredBy:
  - cp_library/ds/tree/bst/cartesian_tree_implicit_cls.py
  - cp_library/ds/tree/bst/cartesian_tree_reversible_cls.py
  - cp_library/ds/tree/bst/bst_reversible_cls.py
  - cp_library/ds/tree/bst/treap_monoid_reversible_cls.py
  - cp_library/ds/tree/bst/treap_reversible_cls.py
  - cp_library/ds/tree/bst/treap_implicit_cls.py
  timestamp: '2025-07-10 00:37:15+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library-checker/data-structure/range_reverse_range_sum.test.py
documentation_of: cp_library/ds/tree/bst/bst_implicit_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/tree/bst/bst_implicit_cls.py
- /library/cp_library/ds/tree/bst/bst_implicit_cls.py.html
title: cp_library/ds/tree/bst/bst_implicit_cls.py
---
