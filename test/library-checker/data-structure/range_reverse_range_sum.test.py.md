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
    path: cp_library/ds/tree/bst/bst_implicit_cls.py
    title: cp_library/ds/tree/bst/bst_implicit_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/bst/bst_reversible_cls.py
    title: cp_library/ds/tree/bst/bst_reversible_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/bst/bst_sized_cls.py
    title: cp_library/ds/tree/bst/bst_sized_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/bst/bst_updates_cls.py
    title: cp_library/ds/tree/bst/bst_updates_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/bst/cartesian_tree_cls.py
    title: cp_library/ds/tree/bst/cartesian_tree_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/bst/cartesian_tree_implicit_cls.py
    title: cp_library/ds/tree/bst/cartesian_tree_implicit_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/bst/cartesian_tree_reversible_cls.py
    title: cp_library/ds/tree/bst/cartesian_tree_reversible_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/bst/cartesian_tree_sized_cls.py
    title: cp_library/ds/tree/bst/cartesian_tree_sized_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/bst/treap_cls.py
    title: cp_library/ds/tree/bst/treap_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/bst/treap_implicit_cls.py
    title: cp_library/ds/tree/bst/treap_implicit_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/bst/treap_monoid_cls.py
    title: cp_library/ds/tree/bst/treap_monoid_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/bst/treap_monoid_reversible_cls.py
    title: cp_library/ds/tree/bst/treap_monoid_reversible_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/bst/treap_reversible_cls.py
    title: cp_library/ds/tree/bst/treap_reversible_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/bst/treap_sized_cls.py
    title: cp_library/ds/tree/bst/treap_sized_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/fast_io_cls.py
    title: cp_library/io/fast_io_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/parser_cls.py
    title: cp_library/io/parser_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/read_fn.py
    title: cp_library/io/read_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/write_fn.py
    title: cp_library/io/write_fn.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/range_reverse_range_sum
    links:
    - https://judge.yosupo.jp/problem/range_reverse_range_sum
  bundledCode: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/range_reverse_range_sum\n\
    \nfrom operator import add\n\ndef main():\n    N, Q = read()\n    TreapMonoidReversibe.reserve(1+N+Q)\n\
    \    T = TreapMonoidReversibe(add, 0)\n    T.build(read())\n    for _ in range(Q):\n\
    \        t, l, r = read()\n        if t == 0:\n            T.reverse(l,r)\n  \
    \      else:\n            write(T.prod(l,r))\n\n'''\n\u257A\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2578\n             https://kobejean.github.io/cp-library\
    \               \n'''\n\n\ndef reserve(A: list, est_len: int) -> None: ...\ntry:\n\
    \    from __pypy__ import resizelist_hint\nexcept:\n    def resizelist_hint(A:\
    \ list, est_len: int):\n        pass\nreserve = resizelist_hint\n\n\n\n\ni64_max\
    \ = (1<<63)-1\n\nclass BST:\n    __slots__ = 'r'\n    K,sub,st=[-1],[-1,-1],[]\n\
    \    def __init__(T):T.r=T._nr()\n    def _nt(T):return T.__class__()\n    def\
    \ _nr(T):r=len(T.K);T.K.append(i64_max);T.sub.append(-1);T.sub.append(-1);return\
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
    \nclass CartesianTree(BST):\n    K,P,sub,st=[-1],[42],[-1,-1],[]\n    def _nr(T):T.P.append(-1);return\
    \ super()._nr()\n    def _nn(T,k,p=-1):T.P.append(p);return super()._nn(k)\n \
    \   def get(T,k):return T.P[BST.get(T,k)]\n    def pop(T,k):return T.P[BST.pop(T,k)]\n\
    \    def split(T,k):S=T._nt();T._sp(T.sub[T.r<<1],k,S.r<<1,T.r<<1);T._r();return\
    \ S,T\n    def insert(T,k,p):T._i(T.r<<1,k,n:=T._nn(k,p));T._r();return n\n  \
    \  def __getitem__(T,k):return T.get(k)\n    def _i(T,s,k,n):\n        T.st.append(s)\n\
    \        while~T.sub[s]and T.P[i:=T.sub[s]]<T.P[n]:T._p(i);T.st.append(s:=i<<1|(T.K[i]<k))\n\
    \        i,T.sub[s]=T.sub[s],n\n        if~i:T._sp(i,k,n<<1,n<<1|1)\n    def _sp(T,i,k,l,r):\n\
    \        T.st.append(l)\n        if 1<l^r:T.st.append(r)\n        while~i:\n \
    \           T._p(i)\n            if T.K[i]<k:T.sub[l]=i;i=T.sub[l:=i<<1|1];T.st.append(l)\n\
    \            else:T.sub[r]=i;i=T.sub[r:=i<<1];T.st.append(r)\n        T.sub[l]=T.sub[r]=-1\n\
    \    def _m(T,s,l,r):\n        T.st.append(s)\n        while~l and~r:\n      \
    \      if T.P[l]<T.P[r]:T._p(l);T.sub[s]=l;l=T.sub[s:=l<<1|1]\n            else:T._p(r);T.sub[s]=r;r=T.sub[s:=r<<1]\n\
    \            T.st.append(s)\n        T.sub[s]=l if~l else r\n    def _d(T,i,s):T._p(i);T._m(s,T.sub[i<<1],T.sub[i<<1|1])\n\
    \    @classmethod\n    def reserve(cls,sz):super(CartesianTree,cls).reserve(sz);reserve(cls.P,sz+1)\n\
    \nclass Treap(CartesianTree):\n    __slots__='e'\n    K,V,P,sub,st=[-1],[-1],[42],[-1,-1],[]\n\
    \    def __init__(T,e=-1):T.e=e;super().__init__()\n    def _nt(T):return T.__class__(T.e)\n\
    \    def _nr(T):T.V.append(T.e);return super()._nr()\n    def _nn(T,k,v):T.V.append(v);return\
    \ super()._nn(k,(T.P[-1]*1103515245+12345)&0x7fffffff)\n    def insert(T,k,v):return\
    \ super().insert(k,v)\n    def get(T,k):return T.V[BST.get(T,k)]\n    def pop(T,k):return\
    \ T.V[BST.pop(T,k)]\n    def set(T,k,v):T._s(T.r<<1,k,v);T._r()\n    def __setitem__(T,k,v):T.set(k,v)\n\
    \    def _s(T,s,k,v):\n        if ~(i:=T._t(s,k)):T.V[i]=v;T.st.append(i<<1)\n\
    \        else:\n            n=T._nn(k,v)\n            while T.P[n]<T.P[i:=T.st[-1]>>1]:T._p(T.st.pop())\n\
    \            T._p(i)\n            i,T.sub[s]=T.sub[s:=i<<1|(i!=T.r and T.K[i]<k)],n\n\
    \            if~i:T._sp(i,k,n<<1,n<<1|1)\n    def _node_str(T, i): return f\"\
    {T.K[i]}:{T.V[i]}\"\n    @classmethod\n    def reserve(cls,hint):super(Treap,cls).reserve(hint);reserve(cls.V,hint+1)\n\
    \nclass TreapMonoid(Treap, BSTUpdates):\n    __slots__='op'\n    K,V,A,P,sub,st=[-1],[-1],[-1],[42],[-1,-1],[]\n\
    \    def __init__(T,op,e=-1):T.op=op;super().__init__(e)\n    def _nt(T):return\
    \ T.__class__(T.op,T.e)\n    def _nr(T):T.A.append(T.e);return super()._nr()\n\
    \    def _nn(T,k,v):T.A.append(v);return super()._nn(k, v)\n    def prod(T,l,r):\n\
    \        # find common ancestor\n        a=T.sub[T.r<<1]\n        while~a and\
    \ not l<=T.K[a]<r:T._p(a);a=T.sub[a<<1|(T.K[a]<l)]\n        if a<0:return T.e\n\
    \        # left subtreap\n        ac,i=T.V[a],T.sub[a<<1]\n        while~i:\n\
    \            T._p(i)\n            if not(b:=T.K[i]<l):\n                if~(j:=T.sub[i<<1|1]):ac=T.op(T.A[j],ac)\n\
    \                ac=T.op(T.V[i],ac)\n            i=T.sub[i<<1|b]\n        # right\
    \ subtreap\n        i=T.sub[a<<1|1]\n        while~i:\n            T._p(i)\n \
    \           if b:=T.K[i]<r:\n                if~(j:=T.sub[i<<1]):ac=T.op(ac,T.A[j])\n\
    \                ac=T.op(ac,T.V[i])\n            i=T.sub[i<<1|b]\n        return\
    \ ac\n    def all_prod(T):return T.A[T.r]\n    def __getitem__(T,k):\n       \
    \ if isinstance(k,int):return T.get(k)\n        elif isinstance(k,slice):return\
    \ T.prod(k.start,k.stop)\n    @classmethod\n    def reserve(cls,sz):super(TreapMonoid,cls).reserve(sz);reserve(cls.A,sz+1)\n\
    \    def _u(T,i):\n        T.A[i]=T.V[i]\n        if~(l:=T.sub[i<<1]):T.A[i]=T.op(T.A[l],T.A[i])\n\
    \        if~(r:=T.sub[i<<1|1]):T.A[i]=T.op(T.A[i],T.A[r])\n    def _v(T,i=None):\n\
    \        if i is None:\n            assert T.all_prod() == (ac := T._v(i) if ~(i\
    \ := T.sub[T.r<<1]) else T.e)\n            return ac\n        T._p(i);ac = T.V[i]\n\
    \        if ~(l:=T.sub[i<<1]):\n            assert T.P[i] <= T.P[l]\n        \
    \    assert T.K[l] <= T.K[i]\n            ac = T.op(T._v(l), ac)\n        if ~(r:=T.sub[i<<1|1]):\n\
    \            assert T.P[i] <= T.P[r]\n            assert T.K[i] <= T.K[r]\n  \
    \          ac = T.op(ac, T._v(r))\n        assert T.A[i] == ac\n        return\
    \ ac\n\nclass BSTSized(BSTUpdates):\n    K,sz,sub,st=[-1],[0,0],[-1,-1],[]\n \
    \   def _nr(T):T.sz.append(0);T.sz.append(0);return super()._nr()\n    def _nn(T,k):T.sz.append(0);T.sz.append(0);return\
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
    \            T.rev[i]=0\n    @classmethod\n    def reserve(cls,sz):super().reserve(sz);reserve(cls.rev,sz+1)\n\
    \nclass BSTReversible(BSTImplicit):\n    K,rev,sz,sub,st=None,[0],[0,0],[-1,-1],[]\n\
    \    def _nr(T):T.rev.append(0);return super()._nr()\n    def _nn(T,k):T.rev.append(0);return\
    \ super()._nn(k)\n    def _p(T,i):\n        if T.rev[i]:\n            T.sub[l],T.sub[r],T.sz[l],T.sz[r]=T.sub[r:=i<<1|1],T.sub[l:=i<<1],T.sz[r],T.sz[l]\n\
    \            if~(l:=T.sub[l]):T.rev[l]^=1\n            if~(r:=T.sub[r]):T.rev[r]^=1\n\
    \            T.rev[i]=0\n    @classmethod\n    def reserve(cls,sz):super().reserve(sz);reserve(cls.rev,sz+1)\n\
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
    \nclass CartesianTreeSized(CartesianTree, BSTSized):\n    K,P,sz,sub,st=[-1],[42],[0,0],[-1,-1],[]\n\
    \    def kth(T,k): return T.P[BSTSized.kth(T,k)]\n    def _nr(T):T.P.append(-1);return\
    \ BSTSized._nr(T)\n    def _nn(T,k,p=-1):T.P.append(p);return BSTSized._nn(T,k)\n\
    \    @classmethod\n    def reserve(cls,sz):BSTSized.reserve.__call__(sz);reserve(cls.P,sz+1)\n\
    \nclass CartesianTreeReversible(CartesianTreeSized,BSTReversible):\n    def _nr(T):T.P.append((T.P[-1]*1103515245+12345)&0x7fffffff);return\
    \ BSTReversible._nr(T)\n    def _nn(T,k,v):T.P.append(v);return BSTReversible._nn(T,k)\n\
    \    def reverse(T,l,r):\n        if l>=r:return\n        lo,hi = l>0,r<len(T)\n\
    \        s = T.r<<1\n        if hi:T._sp(T.sub[s],r,s,1);T._r()\n        if lo:T._sp(T.sub[s],l,0,s);T._r()\n\
    \        T.rev[T.sub[s]]^=1\n        if hi:T._m(s,T.sub[s],T.sub[1]);T._r()\n\
    \        if lo:T._m(s,T.sub[0],T.sub[s]);T._r()\n    @classmethod\n    def reserve(cls,sz):BSTReversible.reserve.__call__(sz);reserve(cls.P,sz+1)\n\
    \nclass CartesianTreeImplicit(CartesianTreeSized,BSTImplicit):\n    K,P,sz,sub,st=None,[42],[0,0],[-1,-1],[]\n\
    \    def _nr(T):T.P.append((T.P[-1]*1103515245+12345)&0x7fffffff);return BSTImplicit._nr(T)\n\
    \    def _nn(T,k,p):T.P.append(p);return BSTImplicit._nn(T,k)\n    def _i(T,s,k,n):\n\
    \        T.st.append(s)\n        while ~k and ~T.sub[s] and T.P[i:=T.sub[s]]<T.P[n]:\n\
    \            T._p(i)\n            if (sz:=T.sz[s:=i<<1])<k:k-=1+sz;s^=1\n    \
    \        T.st.append(s)\n        i,T.sub[s]=T.sub[s],n\n        if~i:T._sp(i,k,n<<1,n<<1|1)\n\
    \    def _sp(T,i,k,l,r):\n        T.st.append(l)\n        if 1<l^r:T.st.append(r)\n\
    \        while~i:\n            T._p(i)\n            if (sz:=T.sz[i<<1])<k:k-=1+sz;T.sub[l]=i;i=T.sub[l:=i<<1|1];T.st.append(l)\n\
    \            else:T.sub[r]=i;i=T.sub[r:=i<<1];T.st.append(r)\n        T.sub[l]=T.sub[r]=-1\n\
    \    def _node_str(T, i): return f\"{T.P[i]}\"\n    @classmethod\n    def reserve(cls,sz):BSTImplicit.reserve.__call__(sz);reserve(cls.P,sz+1)\n\
    \nclass TreapSized(Treap, CartesianTreeSized):\n    K,V,P,sz,sub,st=[-1],[-1],[42],[0,0],[-1,-1],[]\n\
    \    def _nr(T):T.V.append(T.e);return CartesianTreeSized._nr(T)\n    def _nn(T,k,v):T.V.append(v);return\
    \ CartesianTreeSized._nn(T,k,(T.P[-1]*1103515245+12345)&0x7fffffff)\n    def kth(T,k):\
    \ return T.V[BSTSized.kth(T,k)]\n    @classmethod\n    def reserve(cls,sz):CartesianTreeSized.reserve.__call__(sz);reserve(cls.V,sz+1)\n\
    \nclass TreapImplicit(TreapSized,CartesianTreeImplicit):\n    K,V,P,sz,sub,st=None,[-1],[42],[0,0],[-1,-1],[]\n\
    \    def _nr(T):T.V.append(T.e);return CartesianTreeImplicit._nr(T)\n    def _nn(T,k,v):T.V.append(v);return\
    \ CartesianTreeImplicit._nn(T,k,(T.P[-1]*1103515245+12345)&0x7fffffff)\n    def\
    \ set(T,k,v):T._s(T.r<<1,k,v);T._r()\n    def _i(T,s,k,n):\n        T.st.append(s)\n\
    \        while ~k and ~T.sub[s] and T.P[i:=T.sub[s]]<T.P[n]:\n            T._p(i)\n\
    \            if (sz:=T.sz[s:=i<<1])<k:k-=1+sz;s^=1\n            T.st.append(s)\n\
    \        i,T.sub[s]=T.sub[s],n\n        if~i:T._sp(i,k,n<<1,n<<1|1)\n    def _sp(T,i,k,l,r):\n\
    \        T.st.append(l)\n        if 1<l^r:T.st.append(r)\n        while~i:\n \
    \           T._p(i)\n            if (sz:=T.sz[i<<1])<k:k-=1+sz;T.sub[l]=i;i=T.sub[l:=i<<1|1];T.st.append(l)\n\
    \            else:T.sub[r]=i;i=T.sub[r:=i<<1];T.st.append(r)\n        T.sub[l]=T.sub[r]=-1\n\
    \    def _s(T,s,k,v):T.V[i:=T._t(s,k)]=v;T.st.append(i<<1)\n    def _node_str(T,\
    \ i): return f\"{T.V[i]}\"\n    @classmethod\n    def reserve(cls,sz):CartesianTreeImplicit.reserve.__call__(sz);reserve(cls.V,sz+1)\n\
    \nclass TreapReversible(TreapImplicit,CartesianTreeReversible):\n    K,V,P,sz,sub,st=None,[-1],[42],[0,0],[-1,-1],[]\n\
    \    def _nr(T):T.V.append(T.e);return CartesianTreeReversible._nr(T)\n    def\
    \ _nn(T,k,v):T.V.append(v);return CartesianTreeReversible._nn(T,k,(T.P[-1]*1103515245+12345)&0x7fffffff)\n\
    \    @classmethod\n    def reserve(cls,sz):CartesianTreeReversible.reserve.__call__(sz);reserve(cls.V,sz+1)\n\
    \nclass TreapMonoidReversibe(TreapMonoid,TreapReversible):\n    __slots__='op'\n\
    \    K,V,A,P,rev,sz,sub,st=None,[-1],[-1],[42],[0],[0,0],[-1,-1],[]\n    def build(T,V):\n\
    \        if not V: return\n        base, rnd, P = len(T.V), T.P[-1], [0]*(N:=len(V))\n\
    \        for i in range(N): P[i] = rnd = (rnd*1103515245+12345)&0xfffffff\n  \
    \      P.sort()\n        T.V.extend(V); T.A.extend(V)\n        T.P.extend(zeros:=[0]*N);\
    \ T.rev.extend(zeros)\n        T.sz.extend(zeros); T.sz.extend(zeros); T.sub.extend([-1]*(N<<1))\n\
    \        N += base\n        s,i = 2,base\n        while i < N: T.P[i] = P.pop();\
    \ i += s\n        s,hs,i,l = 4,1,base+1,-1\n        while P:\n            while\
    \ i < N:\n                T.P[i] = P.pop()\n                l, r = i<<1,i<<1|1\n\
    \                T.sub[l] = i-hs\n                T.sz[l] = T.sz[(i-hs)<<1]+1+T.sz[(i-hs)<<1|1]\n\
    \                T.A[i] = T.op(T.A[i-hs],T.A[i])\n                if i+hs<N:\n\
    \                    T.sub[r] = i+hs\n                    T.sz[r] = T.sz[(i+hs)<<1]+1+T.sz[(i+hs)<<1|1]\n\
    \                    T.A[i] = T.op(T.A[i],T.A[i+hs])\n                elif i<N-1:\n\
    \                    T.sub[r] = l = i+(1<<((N-1-i).bit_length()-1))\n        \
    \            T.sz[r] = T.sz[l<<1]+1+T.sz[l<<1|1]\n                    T.A[i] =\
    \ T.op(T.A[i],T.A[l])\n                i += s\n            i,s,hs = base+s-1,s<<1,hs<<1\n\
    \        T.sub[T.r<<1] = r = base+hs-1\n        T.sz[T.r<<1] = T.sz[r<<1]+1+T.sz[r<<1|1]\n\
    \        T.A[T.r] = T.A[r]\n\n    def _nr(T):T.A.append(T.e);return TreapReversible._nr(T)\n\
    \    def _nn(T,k,v):T.A.append(v);return TreapReversible._nn(T,k,v)\n    def prod(T,l,r):\n\
    \        # find common ancestor\n        a=T.sub[T.r<<1]\n        while~a:\n \
    \           T._p(a)\n            if l<=(sz:=T.sz[s:=a<<1])<r:break\n         \
    \   if sz<l:l-=1+sz;r-=1+sz;s^=1\n            a=T.sub[s]\n        if a<0:return\
    \ T.e\n        r-=T.sz[a<<1]+1\n        # left subtreap\n        ac,i=T.V[a],T.sub[a<<1]\n\
    \        while~i and ~l:\n            T._p(i)\n            if (sz:=T.sz[s:=i<<1])<l:l-=1+sz;s^=1\n\
    \            else:\n                if~(j:=T.sub[i<<1|1]):ac=T.op(T.A[j],ac)\n\
    \                ac=T.op(T.V[i],ac)\n            i=T.sub[s]\n        # right subtreap\n\
    \        i=T.sub[a<<1|1]\n        while~i and ~r:\n            T._p(i)\n     \
    \       if (sz:=T.sz[s:=i<<1])<r:\n                if~(j:=T.sub[s]):ac=T.op(ac,T.A[j])\n\
    \                ac=T.op(ac,T.V[i])\n                r-=1+sz;s^=1\n          \
    \  i=T.sub[s]\n        return ac\n    @classmethod\n    def reserve(cls,sz):TreapReversible.reserve.__call__(sz);reserve(cls.A,sz+1)\n\
    \    def _u(T,i):\n        T.A[i]=T.V[i]\n        T.sz[s]=T.sz[l<<1]+1+T.sz[l<<1|1]\
    \ if~(l:=T.sub[s:=i<<1]) else 0\n        T.sz[s]=T.sz[r<<1]+1+T.sz[r<<1|1] if~(r:=T.sub[s:=i<<1|1])\
    \ else 0\n        if~(l:=T.sub[i<<1]):T.A[i]=T.op(T.A[l],T.A[i])\n        if~(r:=T.sub[i<<1|1]):T.A[i]=T.op(T.A[i],T.A[r])\n\
    \    # def _node_str(T, i): return f\"{i=} V{T.V[i]} A{T.A[i]} ({T.sz[i<<1]}:{T.sz[i<<1|1]})\"\
    \n    def _node_str(T, i): return f\"{T.V[i]}\"\n\nif __name__ == '__main__':\n\
    \    L = 31\n    T = TreapMonoidReversibe(add, 0)\n    V = [*range(L)]\n    T.build(V)\n\
    \    print(T)\n    # for L in range(2000):\n    #     T = TreapMonoidReversibe(add,\
    \ 0)\n    #     V = [*range(L)]\n    #     T.build(V)\n    #     assert len(T)\
    \ == L, f'{V}\\n{T}'\n\n\nfrom typing import Type, Union, overload\nimport typing\n\
    from collections import deque\nfrom numbers import Number\nfrom types import GenericAlias\
    \ \nfrom typing import Callable, Collection, Iterator, Union\nimport os\nimport\
    \ sys\nfrom io import BytesIO, IOBase\n\n\nclass FastIO(IOBase):\n    BUFSIZE\
    \ = 8192\n    newlines = 0\n\n    def __init__(self, file):\n        self._fd\
    \ = file.fileno()\n        self.buffer = BytesIO()\n        self.writable = \"\
    x\" in file.mode or \"r\" not in file.mode\n        self.write = self.buffer.write\
    \ if self.writable else None\n\n    def read(self):\n        BUFSIZE = self.BUFSIZE\n\
    \        while True:\n            b = os.read(self._fd, max(os.fstat(self._fd).st_size,\
    \ BUFSIZE))\n            if not b: break\n            ptr = self.buffer.tell()\n\
    \            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)\n\
    \        self.newlines = 0\n        return self.buffer.read()\n\n    def readline(self):\n\
    \        BUFSIZE = self.BUFSIZE\n        while self.newlines == 0:\n         \
    \   b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))\n        \
    \    self.newlines = b.count(b\"\\n\") + (not b)\n            ptr = self.buffer.tell()\n\
    \            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)\n\
    \        self.newlines -= 1\n        return self.buffer.readline()\n\n    def\
    \ flush(self):\n        if self.writable:\n            os.write(self._fd, self.buffer.getvalue())\n\
    \            self.buffer.truncate(0), self.buffer.seek(0)\n\n\nclass IOWrapper(IOBase):\n\
    \    stdin: 'IOWrapper' = None\n    stdout: 'IOWrapper' = None\n    \n    def\
    \ __init__(self, file):\n        self.buffer = FastIO(file)\n        self.flush\
    \ = self.buffer.flush\n        self.writable = self.buffer.writable\n\n    def\
    \ write(self, s):\n        return self.buffer.write(s.encode(\"ascii\"))\n   \
    \ \n    def read(self):\n        return self.buffer.read().decode(\"ascii\")\n\
    \    \n    def readline(self):\n        return self.buffer.readline().decode(\"\
    ascii\")\ntry:\n    sys.stdin = IOWrapper.stdin = IOWrapper(sys.stdin)\n    sys.stdout\
    \ = IOWrapper.stdout = IOWrapper(sys.stdout)\nexcept:\n    pass\nfrom typing import\
    \ TypeVar\n_S = TypeVar('S')\n_T = TypeVar('T')\n_U = TypeVar('U')\n_T1 = TypeVar('T1')\n\
    _T2 = TypeVar('T2')\n_T3 = TypeVar('T3')\n_T4 = TypeVar('T4')\n_T5 = TypeVar('T5')\n\
    _T6 = TypeVar('T6')\n\nclass TokenStream(Iterator):\n    stream = IOWrapper.stdin\n\
    \n    def __init__(self):\n        self.queue = deque()\n\n    def __next__(self):\n\
    \        if not self.queue: self.queue.extend(self._line())\n        return self.queue.popleft()\n\
    \    \n    def wait(self):\n        if not self.queue: self.queue.extend(self._line())\n\
    \        while self.queue: yield\n \n    def _line(self):\n        return TokenStream.stream.readline().split()\n\
    \n    def line(self):\n        if self.queue:\n            A = list(self.queue)\n\
    \            self.queue.clear()\n            return A\n        return self._line()\n\
    TokenStream.default = TokenStream()\n\nclass CharStream(TokenStream):\n    def\
    \ _line(self):\n        return TokenStream.stream.readline().rstrip()\nCharStream.default\
    \ = CharStream()\n\nParseFn = Callable[[TokenStream],_T]\nclass Parser:\n    def\
    \ __init__(self, spec: Union[type[_T],_T]):\n        self.parse = Parser.compile(spec)\n\
    \n    def __call__(self, ts: TokenStream) -> _T:\n        return self.parse(ts)\n\
    \    \n    @staticmethod\n    def compile_type(cls: type[_T], args = ()) -> _T:\n\
    \        if issubclass(cls, Parsable):\n            return cls.compile(*args)\n\
    \        elif issubclass(cls, (Number, str)):\n            def parse(ts: TokenStream):\
    \ return cls(next(ts))              \n            return parse\n        elif issubclass(cls,\
    \ tuple):\n            return Parser.compile_tuple(cls, args)\n        elif issubclass(cls,\
    \ Collection):\n            return Parser.compile_collection(cls, args)\n    \
    \    elif callable(cls):\n            def parse(ts: TokenStream):\n          \
    \      return cls(next(ts))              \n            return parse\n        else:\n\
    \            raise NotImplementedError()\n    \n    @staticmethod\n    def compile(spec:\
    \ Union[type[_T],_T]=int) -> ParseFn[_T]:\n        if isinstance(spec, (type,\
    \ GenericAlias)):\n            cls = typing.get_origin(spec) or spec\n       \
    \     args = typing.get_args(spec) or tuple()\n            return Parser.compile_type(cls,\
    \ args)\n        elif isinstance(offset := spec, Number): \n            cls =\
    \ type(spec)  \n            def parse(ts: TokenStream): return cls(next(ts)) +\
    \ offset\n            return parse\n        elif isinstance(args := spec, tuple):\
    \      \n            return Parser.compile_tuple(type(spec), args)\n        elif\
    \ isinstance(args := spec, Collection):\n            return Parser.compile_collection(type(spec),\
    \ args)\n        elif isinstance(fn := spec, Callable): \n            def parse(ts:\
    \ TokenStream): return fn(next(ts))\n            return parse\n        else:\n\
    \            raise NotImplementedError()\n\n    @staticmethod\n    def compile_line(cls:\
    \ _T, spec=int) -> ParseFn[_T]:\n        if spec is int:\n            fn = Parser.compile(spec)\n\
    \            def parse(ts: TokenStream): return cls([int(token) for token in ts.line()])\n\
    \            return parse\n        else:\n            fn = Parser.compile(spec)\n\
    \            def parse(ts: TokenStream): return cls([fn(ts) for _ in ts.wait()])\n\
    \            return parse\n\n    @staticmethod\n    def compile_repeat(cls: _T,\
    \ spec, N) -> ParseFn[_T]:\n        fn = Parser.compile(spec)\n        def parse(ts:\
    \ TokenStream): return cls([fn(ts) for _ in range(N)])\n        return parse\n\
    \n    @staticmethod\n    def compile_children(cls: _T, specs) -> ParseFn[_T]:\n\
    \        fns = tuple((Parser.compile(spec) for spec in specs))\n        def parse(ts:\
    \ TokenStream): return cls([fn(ts) for fn in fns])  \n        return parse\n \
    \           \n    @staticmethod\n    def compile_tuple(cls: type[_T], specs) ->\
    \ ParseFn[_T]:\n        if isinstance(specs, (tuple,list)) and len(specs) == 2\
    \ and specs[1] is ...:\n            return Parser.compile_line(cls, specs[0])\n\
    \        else:\n            return Parser.compile_children(cls, specs)\n\n   \
    \ @staticmethod\n    def compile_collection(cls, specs):\n        if not specs\
    \ or len(specs) == 1 or isinstance(specs, set):\n            return Parser.compile_line(cls,\
    \ *specs)\n        elif (isinstance(specs, (tuple,list)) and len(specs) == 2 and\
    \ isinstance(specs[1], int)):\n            return Parser.compile_repeat(cls, specs[0],\
    \ specs[1])\n        else:\n            raise NotImplementedError()\n\nclass Parsable:\n\
    \    @classmethod\n    def compile(cls):\n        def parser(ts: TokenStream):\
    \ return cls(next(ts))\n        return parser\n    \n    @classmethod\n    def\
    \ __class_getitem__(cls, item):\n        return GenericAlias(cls, item)\n\n@overload\n\
    def read() -> list[int]: ...\n@overload\ndef read(spec: Type[_T], char=False)\
    \ -> _T: ...\n@overload\ndef read(spec: _U, char=False) -> _U: ...\n@overload\n\
    def read(*specs: Type[_T], char=False) -> tuple[_T, ...]: ...\n@overload\ndef\
    \ read(*specs: _U, char=False) -> tuple[_U, ...]: ...\ndef read(*specs: Union[Type[_T],_U],\
    \ char=False):\n    if not char and not specs: return [int(s) for s in TokenStream.default.line()]\n\
    \    parser: _T = Parser.compile(specs[0] if len(specs) == 1 else specs)\n   \
    \ return parser(CharStream.default if char else TokenStream.default)\n\ndef write(*args,\
    \ **kwargs):\n    '''Prints the values to a stream, or to stdout_fast by default.'''\n\
    \    sep, file = kwargs.pop(\"sep\", \" \"), kwargs.pop(\"file\", IOWrapper.stdout)\n\
    \    at_start = True\n    for x in args:\n        if not at_start:\n         \
    \   file.write(sep)\n        file.write(str(x))\n        at_start = False\n  \
    \  file.write(kwargs.pop(\"end\", \"\\n\"))\n    if kwargs.pop(\"flush\", False):\n\
    \        file.flush()\n\nif __name__ == '__main__':\n    main()\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/range_reverse_range_sum\n\
    \nfrom operator import add\n\ndef main():\n    N, Q = read()\n    TreapMonoidReversibe.reserve(1+N+Q)\n\
    \    T = TreapMonoidReversibe(add, 0)\n    T.build(read())\n    for _ in range(Q):\n\
    \        t, l, r = read()\n        if t == 0:\n            T.reverse(l,r)\n  \
    \      else:\n            write(T.prod(l,r))\n\nfrom cp_library.ds.tree.bst.treap_monoid_reversible_cls\
    \ import TreapMonoidReversibe\nfrom cp_library.io.read_fn import read\nfrom cp_library.io.write_fn\
    \ import write\n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - cp_library/ds/tree/bst/treap_monoid_reversible_cls.py
  - cp_library/io/read_fn.py
  - cp_library/io/write_fn.py
  - cp_library/ds/reserve_fn.py
  - cp_library/ds/tree/bst/treap_monoid_cls.py
  - cp_library/ds/tree/bst/treap_reversible_cls.py
  - cp_library/io/parser_cls.py
  - cp_library/io/fast_io_cls.py
  - cp_library/ds/tree/bst/bst_updates_cls.py
  - cp_library/ds/tree/bst/treap_cls.py
  - cp_library/ds/tree/bst/cartesian_tree_reversible_cls.py
  - cp_library/ds/tree/bst/treap_implicit_cls.py
  - cp_library/ds/tree/bst/bst_reversible_cls.py
  - cp_library/ds/tree/bst/cartesian_tree_sized_cls.py
  - cp_library/ds/tree/bst/cartesian_tree_implicit_cls.py
  - cp_library/ds/tree/bst/treap_sized_cls.py
  - cp_library/ds/tree/bst/bst_implicit_cls.py
  - cp_library/ds/tree/bst/bst_sized_cls.py
  - cp_library/ds/tree/bst/cartesian_tree_cls.py
  - cp_library/ds/tree/bst/bst_cls.py
  - cp_library/bit/masks/i64_max_cnst.py
  isVerificationFile: true
  path: test/library-checker/data-structure/range_reverse_range_sum.test.py
  requiredBy: []
  timestamp: '2025-07-20 06:26:01+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library-checker/data-structure/range_reverse_range_sum.test.py
layout: document
redirect_from:
- /verify/test/library-checker/data-structure/range_reverse_range_sum.test.py
- /verify/test/library-checker/data-structure/range_reverse_range_sum.test.py.html
title: test/library-checker/data-structure/range_reverse_range_sum.test.py
---
