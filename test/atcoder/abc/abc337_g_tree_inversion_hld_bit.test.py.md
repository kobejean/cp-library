---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/dp/chmin_fn.py
    title: cp_library/alg/dp/chmin_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/dp/max2_fn.py
    title: cp_library/alg/dp/max2_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/csr/graph_base_cls.py
    title: cp_library/alg/graph/csr/graph_base_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/csr/graph_cls.py
    title: cp_library/alg/graph/csr/graph_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/dfs_options_cls.py
    title: cp_library/alg/graph/dfs_options_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/iter/presum_fn.py
    title: cp_library/alg/iter/presum_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/csr/hld_base_cls.py
    title: cp_library/alg/tree/csr/hld_base_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/csr/hld_bit_cls.py
    title: cp_library/alg/tree/csr/hld_bit_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/csr/tree_base_cls.py
    title: cp_library/alg/tree/csr/tree_base_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/csr/tree_cls.py
    title: cp_library/alg/tree/csr/tree_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/masks/i32_max_cnst.py
    title: cp_library/bit/masks/i32_max_cnst.py
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/masks/u32_max_cnst.py
    title: cp_library/bit/masks/u32_max_cnst.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/array/i32f_fn.py
    title: cp_library/ds/array/i32f_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/array/u32f_fn.py
    title: cp_library/ds/array/u32f_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/array/u8f_fn.py
    title: cp_library/ds/array/u8f_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/list/elist_fn.py
    title: cp_library/ds/list/elist_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/list/list_find_fn.py
    title: cp_library/ds/list/list_find_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/packet_list_cls.py
    title: cp_library/ds/packet_list_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/que/que_cls.py
    title: cp_library/ds/que/que_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/bit/bit_cls.py
    title: cp_library/ds/tree/bit/bit_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/view/view_cls.py
    title: cp_library/ds/view/view_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/io_base_cls.py
    title: cp_library/io/io_base_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/io_cls.py
    title: cp_library/io/io_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/parsable_cls.py
    title: cp_library/io/parsable_cls.py
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
    PROBLEM: https://atcoder.jp/contests/abc337/tasks/abc337_g
    links:
    - https://atcoder.jp/contests/abc337/tasks/abc337_g
  bundledCode: "# verification-helper: PROBLEM https://atcoder.jp/contests/abc337/tasks/abc337_g\n\
    \ndef main():\n    N = read(int)\n    T = read(Tree[N])\n    hld, ans = HLDBIT(T,\
    \ [0]*N), [0]*(N+1)\n\n    def range_add(l,r,x):\n        ans[l] += x\n      \
    \  ans[r] -= x\n\n    for u in range(N):\n        l,r = hld.subtree_range(u)\n\
    \        range_add(l,r,u-hld.subtree_query(u))\n        for i in T.range(u):\n\
    \            if i != hld.back[u]:\n                l,r = hld.subtree_range(T.Va[i])\n\
    \                cnt = hld.subtree_query(T.Va[i])\n                range_add(0,l,cnt)\n\
    \                range_add(r,N,cnt)\n        hld.add(u,1)\n    ans = presum(ans)\n\
    \    ans = [ans[i] for i in hld.tin]\n    write(*ans)\n\n'''\n\u257A\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\n             https://kobejean.github.io/cp-library\
    \               \n'''\n\n\n\nfrom math import inf\nfrom typing import Callable,\
    \ Literal, Union, overload\n\nfrom typing import Generic\nfrom typing import TypeVar\n\
    _S = TypeVar('S'); _T = TypeVar('T'); _U = TypeVar('U'); _T1 = TypeVar('T1');\
    \ _T2 = TypeVar('T2'); _T3 = TypeVar('T3'); _T4 = TypeVar('T4'); _T5 = TypeVar('T5');\
    \ _T6 = TypeVar('T6')\n\n\nimport sys\n\ndef list_find(lst: list, value, start\
    \ = 0, stop = sys.maxsize):\n    try:\n        return lst.index(value, start,\
    \ stop)\n    except:\n        return -1\n\n\nclass view(Generic[_T]):\n    __slots__\
    \ = 'A', 'l', 'r'\n    def __init__(V, A: list[_T], l: int = 0, r: int = 0): V.A,\
    \ V.l, V.r = A, l, r\n    def __len__(V): return V.r - V.l\n    def __getitem__(V,\
    \ i: int): \n        if 0 <= i < V.r - V.l: return V.A[V.l+i]\n        else: raise\
    \ IndexError\n    def __setitem__(V, i: int, v: _T): V.A[V.l+i] = v\n    def __contains__(V,\
    \ v: _T): return list_find(V.A, v, V.l, V.r) != -1\n    def set_range(V, l: int,\
    \ r: int): V.l, V.r = l, r\n    def index(V, v: _T): return V.A.index(v, V.l,\
    \ V.r) - V.l\n    def reverse(V):\n        l, r = V.l, V.r-1\n        while l\
    \ < r: V.A[l], V.A[r] = V.A[r], V.A[l]; l += 1; r -= 1\n    def sort(V, /, *args,\
    \ **kwargs):\n        A = V.A[V.l:V.r]; A.sort(*args, **kwargs)\n        for i,a\
    \ in enumerate(A,V.l): V.A[i] = a\n    def pop(V): V.r -= 1; return V.A[V.r]\n\
    \    def append(V, v: _T): V.A[V.r] = v; V.r += 1\n    def popleft(V): V.l +=\
    \ 1; return V.A[V.l-1]\n    def appendleft(V, v: _T): V.l -= 1; V.A[V.l] = v;\
    \ \n    def validate(V): return 0 <= V.l <= V.r <= len(V.A)\nfrom typing import\
    \ Callable, Sequence, Union, overload\nfrom types import GenericAlias\n\n\nclass\
    \ Parsable:\n    @classmethod\n    def compile(cls):\n        def parser(io: 'IOBase'):\
    \ return cls(next(io))\n        return parser\n    @classmethod\n    def __class_getitem__(cls,\
    \ item): return GenericAlias(cls, item)\n\n\ndef chmin(dp, i, v):\n    if ch:=dp[i]>v:dp[i]=v\n\
    \    return ch\n\n\nfrom enum import auto, IntFlag, IntEnum\n\nclass DFSFlags(IntFlag):\n\
    \    ENTER = auto()\n    DOWN = auto()\n    BACK = auto()\n    CROSS = auto()\n\
    \    LEAVE = auto()\n    UP = auto()\n    MAXDEPTH = auto()\n\n    RETURN_PARENTS\
    \ = auto()\n    RETURN_DEPTHS = auto()\n    BACKTRACK = auto()\n    CONNECT_ROOTS\
    \ = auto()\n\n    # Common combinations\n    ALL_EDGES = DOWN | BACK | CROSS\n\
    \    EULER_TOUR = DOWN | UP\n    INTERVAL = ENTER | LEAVE\n    TOPDOWN = DOWN\
    \ | CONNECT_ROOTS\n    BOTTOMUP = UP | CONNECT_ROOTS\n    RETURN_ALL = RETURN_PARENTS\
    \ | RETURN_DEPTHS\n\nclass DFSEvent(IntEnum):\n    ENTER = DFSFlags.ENTER \n \
    \   DOWN = DFSFlags.DOWN \n    BACK = DFSFlags.BACK \n    CROSS = DFSFlags.CROSS\
    \ \n    LEAVE = DFSFlags.LEAVE \n    UP = DFSFlags.UP \n    MAXDEPTH = DFSFlags.MAXDEPTH\n\
    \    \n\nclass GraphBase(Parsable):\n    def __init__(G, N: int, M: int, U: list[int],\
    \ V: list[int], \n                 deg: list[int], La: list[int], Ra: list[int],\n\
    \                 Ua: list[int], Va: list[int], Ea: list[int], twin: list[int]\
    \ = None):\n        G.N = N\n        '''The number of vertices.'''\n        G.M\
    \ = M\n        '''The number of edges.'''\n        G.U = U\n        '''A list\
    \ of source vertices in the original edge list.'''\n        G.V = V\n        '''A\
    \ list of destination vertices in the original edge list.'''\n        G.deg =\
    \ deg\n        '''deg[u] is the out degree of vertex u.'''\n        G.La = La\n\
    \        '''La[u] stores the start index of the list of adjacent vertices from\
    \ u.'''\n        G.Ra = Ra\n        '''Ra[u] stores the stop index of the list\
    \ of adjacent vertices from u.'''\n        G.Ua = Ua\n        '''Ua[i] = u for\
    \ La[u] <= i < Ra[u], useful for backtracking.'''\n        G.Va = Va\n       \
    \ '''Va[i] lists adjacent vertices to u for La[u] <= i < Ra[u].'''\n        G.Ea\
    \ = Ea\n        '''Ea[i] lists the edge ids that start from u for La[u] <= i <\
    \ Ra[u].\n        For undirected graphs, edge ids in range M<= e <2*M are edges\
    \ from V[e-M] -> U[e-M].\n        '''\n        G.twin = twin if twin is not None\
    \ else range(len(Ua))\n        '''twin[i] in undirected graphs stores index j\
    \ of the same edge but with u and v swapped.'''\n        G.st: list[int] = None\n\
    \        G.order: list[int] = None\n        G.vis: list[int] = None\n        G.back:\
    \ list[int] = None\n        G.tin: list[int] = None\n    \n    def clear(G):\n\
    \        G.vis = G.back = G.tin = None\n\n    def prep_vis(G):\n        if G.vis\
    \ is None: G.vis = u8f(G.N)\n        return G.vis\n    \n    def prep_st(G):\n\
    \        if G.st is None: G.st = elist(G.N)\n        else: G.st.clear()\n    \
    \    return G.st\n    \n    def prep_order(G):\n        if G.order is None: G.order\
    \ = elist(G.N)\n        else: G.order.clear()\n        return G.order\n    \n\
    \    def prep_back(G):\n        if G.back is None: G.back = i32f(G.N, -2)\n  \
    \      return G.back\n    \n    def prep_tin(G):\n        if G.tin is None: G.tin\
    \ = i32f(G.N, -1)\n        return G.tin\n    \n    def _remove(G, a: int):\n \
    \       G.deg[u := G.Ua[a]] -= 1\n        G.Ra[u] = (r := G.Ra[u]-1)\n       \
    \ G.Ua[a], G.Va[a], G.Ea[a] = G.Ua[r], G.Va[r], G.Ea[r]\n        G.twin[a], G.twin[r]\
    \ = G.twin[r], G.twin[a]\n        G.twin[G.twin[a]] = a\n        G.twin[G.twin[r]]\
    \ = r\n\n    def remove(G, a: int):\n        b = G.twin[a]; G._remove(a)\n   \
    \     if a != b: G._remove(b)\n\n    def __len__(G) -> int: return G.N\n    def\
    \ __getitem__(G, u): return view(G.Va, G.La[u], G.Ra[u])\n    def range(G, u):\
    \ return range(G.La[u],G.Ra[u])\n    \n    @overload\n    def distance(G) -> list[list[int]]:\
    \ ...\n    @overload\n    def distance(G, s: int = 0) -> list[int]: ...\n    @overload\n\
    \    def distance(G, s: int, g: int) -> int: ...\n    def distance(G, s = None,\
    \ g = None):\n        if s == None: return G.floyd_warshall()\n        else: return\
    \ G.bfs(s, g)\n\n    def recover_path(G, s, t):\n        Ua, back, vertices =\
    \ G.Ua, G.back, u32f(1, v := t)\n        while v != s: vertices.append(v := Ua[back[v]])\n\
    \        return vertices\n    \n    def recover_path_edge_ids(G, s, t):\n    \
    \    Ea, Ua, back, edges, v = G.Ea, G.Ua, G.back, u32f(0), t\n        while v\
    \ != s: edges.append(Ea[i := back[v]]), (v := Ua[i])\n        return edges\n\n\
    \    def shortest_path(G, s: int, t: int):\n        if G.distance(s, t) >= inf:\
    \ return None\n        vertices = G.recover_path(s, t)\n        vertices.reverse()\n\
    \        return vertices\n    \n    def shortest_path_edge_ids(G, s: int, t: int):\n\
    \        if G.distance(s, t) >= inf: return None\n        edges = G.recover_path_edge_ids(s,\
    \ t)\n        edges.reverse()\n        return edges\n    \n    @overload\n   \
    \ def bfs(G, s: Union[int,list] = 0) -> list[int]: ...\n    @overload\n    def\
    \ bfs(G, s: Union[int,list], g: int) -> int: ...\n    def bfs(G, s: int = 0, g:\
    \ int = None):\n        S, Va, back, D = G.starts(s), G.Va, i32f(N := G.N, -1),\
    \ [inf]*N\n        G.back, G.D = back, D\n        for u in S: D[u] = 0\n     \
    \   que = Que(S)\n        while que:\n            nd = D[u := que.pop()]+1\n \
    \           if u == g: return nd-1\n            for i in G.range(u):\n       \
    \         if chmin(D, v := Va[i], nd): back[v] = i; que.push(v)\n        return\
    \ D if g is None else inf \n\n    def floyd_warshall(G) -> list[list[int]]:\n\
    \        G.D = D = [[inf]*G.N for _ in range(G.N)]\n        for u in range(G.N):\
    \ D[u][u] = 0\n        for i in range(len(G.Ua)): D[G.Ua[i]][G.Va[i]] = 1\n  \
    \      for k, Dk in enumerate(D):\n            for Di in D:\n                if\
    \ (Dik := Di[k]) == inf: continue\n                for j in range(G.N):\n    \
    \                chmin(Di, j, Dik+Dk[j])\n        return D\n\n    def find_cycle_indices(G,\
    \ s: Union[int, None] = None):\n        Ea, Ua, Va, vis, back = G.Ea, G. Ua, G.Va,\
    \ u8f(N := G.N), u32f(N, i32_max)\n        G.vis, G.back, st = vis, back, elist(N)\n\
    \        for s in G.starts(s):\n            if vis[s]: continue\n            st.append(s)\n\
    \            while st:\n                if not vis[u := st.pop()]:\n         \
    \           st.append(u)\n                    vis[u], pe = 1, Ea[j] if (j := back[u])\
    \ != i32_max else i32_max\n                    for i in G.range(u):\n        \
    \                if not vis[v := Va[i]]:\n                            back[v]\
    \ = i\n                            st.append(v)\n                        elif\
    \ vis[v] == 1 and pe != Ea[i]:\n                            I = u32f(1,i)\n  \
    \                          while v != u: I.append(i := back[u]), (u := Ua[i])\n\
    \                            I.reverse()\n                            return I\n\
    \                else:\n                    vis[u] = 2\n        # check for self\
    \ loops\n        for i in range(len(Ua)):\n            if Ua[i] == Va[i]:\n  \
    \              return u32f(1,i)\n    \n    def find_cycle(G, s: Union[int, None]\
    \ = None):\n        if I := G.find_cycle_indices(s): return [G.Ua[i] for i in\
    \ I]\n    \n    def find_cycle_edge_ids(G, s: Union[int, None] = None):\n    \
    \    if I := G.find_cycle_indices(s): return [G.Ea[i] for i in I]\n\n    def find_minimal_cycle(G,\
    \ s=0):\n        D, par, que, Va = u32f(N := G.N, u32_max), i32f(N, -1), Que([s]),\
    \ G.Va\n        D[s] = 0\n        while que:\n            for i in G.range(u :=\
    \ que.pop()):\n                if (v := Va[i]) == s:  # Found cycle back to start\n\
    \                    cycle = [u]\n                    while u != s: cycle.append(u\
    \ := par[u])\n                    return cycle\n                if D[v] < u32_max:\
    \ continue\n                D[v], par[v] = D[u]+1, u; que.push(v)\n\n    def dfs_topo(G,\
    \ s: Union[int,list] = None) -> list[int]:\n        '''Returns lists of indices\
    \ i where Ua[i] -> Va[i] are edges in order of top down discovery'''\n       \
    \ vis, st, order = G.prep_vis(), G.prep_st(), G.prep_order()\n        for s in\
    \ G.starts(s):\n            if vis[s]: continue\n            vis[s] = 1; st.append(s)\
    \ \n            while st:\n                for i in G.range(st.pop()):\n     \
    \               if vis[v := G.Va[i]]: continue\n                    vis[v] = 1;\
    \ order.append(i); st.append(v)\n        return order\n\n    def dfs(G, s: Union[int,list]\
    \ = None, /, \n            backtrack = False,\n            max_depth = None,\n\
    \            enter_fn: Callable[[int],None] = None,\n            leave_fn: Callable[[int],None]\
    \ = None,\n            max_depth_fn: Callable[[int],None] = None,\n          \
    \  down_fn: Callable[[int,int,int],None] = None,\n            back_fn: Callable[[int,int,int],None]\
    \ = None,\n            forward_fn: Callable[[int,int,int],None] = None,\n    \
    \        cross_fn: Callable[[int,int,int],None] = None,\n            up_fn: Callable[[int,int,int],None]\
    \ = None):\n        I, time, vis, st, back, tin = G.La[:], -1, G.prep_vis(), G.prep_st(),\
    \ G.prep_back(), G.prep_tin()\n        for s in G.starts(s):\n            if vis[s]:\
    \ continue\n            back[s], tin[s] = -1, (time := time+1); st.append(s)\n\
    \            while st:\n                if vis[u := st[-1]] == 0:\n          \
    \          vis[u] = 1\n                    if enter_fn: enter_fn(u)\n        \
    \            if max_depth is not None and len(st) > max_depth:\n             \
    \           I[u] = G.Ra[u]\n                        if max_depth_fn: max_depth_fn(u)\n\
    \                if (i := I[u]) < G.Ra[u]:\n                    I[u] += 1\n  \
    \                  if (s := vis[v := G.Va[i]]) == 0:\n                       \
    \ back[v], tin[v] = i, (time := time+1); st.append(v)\n                      \
    \  if down_fn: down_fn(u,v,i)\n                    elif back_fn and s == 1 and\
    \ back[u] != G.twin[i]: back_fn(u,v,i)\n                    elif (cross_fn or\
    \ forward_fn) and s == 2:\n                        if forward_fn and tin[u] <\
    \ tin[v]: forward_fn(u,v,i)\n                        elif cross_fn: cross_fn(u,v,i)\n\
    \                else:\n                    vis[u] = 2; st.pop()\n           \
    \         if backtrack: vis[u], I[u] = 0, G.La[u]\n                    if leave_fn:\
    \ leave_fn(u)\n                    if up_fn and st: up_fn(u, st[-1], back[u])\n\
    \    \n    def dfs_enter_leave(G, s: Union[int,list[int],None] = None) -> Sequence[tuple[DFSEvent,int]]:\n\
    \        N, I = G.N, G.La[:]\n        st, back, plst = elist(N), i32f(N,-2), PacketList(order\
    \ := elist(2*N), N-1)\n        G.back, ENTER, LEAVE = back, int(DFSEvent.ENTER)\
    \ << plst.shift, int(DFSEvent.LEAVE) << plst.shift\n        for s in G.starts(s):\n\
    \            if back[s] >= -1: continue\n            back[s] = -1\n          \
    \  order.append(ENTER | s), st.append(s)\n            while st:\n            \
    \    if (i := I[u := st[-1]]) < G.Ra[u]:\n                    I[u] += 1\n    \
    \                if back[v := G.Va[i]] >= -1: continue\n                    back[v]\
    \ = i; order.append(ENTER | v); st.append(v)\n                else:\n        \
    \            order.append(LEAVE | u); st.pop()\n        return plst\n    \n  \
    \  def starts(G, s: Union[int,list[int],None] = None) -> list[int]:\n        if\
    \ isinstance(s, int): return [s]\n        elif s is None: return range(G.N)\n\
    \        elif isinstance(s, list): return s\n        else: return list(s)\n\n\
    \    @classmethod\n    def compile(cls, N: int, M: int, shift: int = -1):\n  \
    \      def parse(io: IOBase):\n            U, V = u32f(M), u32f(M)\n         \
    \   for i in range(M): u, v = io.readints(); U[i], V[i] = u+shift, v+shift\n \
    \           return cls(N, U, V)\n        return parse\n\n\nu32_max = (1<<32)-1\n\
    i32_max = (1<<31)-1\n\nfrom array import array\ndef u8f(N: int, elm: int = 0):\
    \      return array('B', (elm,))*N  # unsigned char\ndef u32f(N: int, elm: int\
    \ = 0):     return array('I', (elm,))*N  # unsigned int\ndef i32f(N: int, elm:\
    \ int = 0):     return array('i', (elm,))*N  # signed int\n\ndef elist(est_len:\
    \ int) -> list: ...\ntry:\n    from __pypy__ import newlist_hint\nexcept:\n  \
    \  def newlist_hint(hint):\n        return []\nelist = newlist_hint\n    \n\n\
    class PacketList(Sequence[tuple[int,int]]):\n    def __init__(lst, A: list[int],\
    \ max1: int):\n        lst.A = A\n        lst.mask = (1 << (shift := (max1).bit_length()))\
    \ - 1\n        lst.shift = shift\n    def __len__(lst): return lst.A.__len__()\n\
    \    def __contains__(lst, x: tuple[int,int]): return lst.A.__contains__(x[0]\
    \ << lst.shift | x[1])\n    def __getitem__(lst, key) -> tuple[int,int]:\n   \
    \     x = lst.A[key]\n        return x >> lst.shift, x & lst.mask\n\n\nclass Que:\n\
    \    def __init__(que, v = None): que.q = elist(v) if isinstance(v, int) else\
    \ list(v) if v else []; que.h = 0\n    def push(que, item): que.q.append(item)\n\
    \    def pop(que): que.h = (h := que.h) + 1; return que.q[h]\n    def extend(que,\
    \ items): que.q.extend(items)\n    def __getitem__(que, i: int): return que.q[que.h+i]\n\
    \    def __setitem__(que, i: int, v): que.q[que.h+i] = v\n    def __len__(que):\
    \ return que.q.__len__() - que.h\n    def __hash__(que): return hash(tuple(que.q[que.h:]))\n\
    \nclass IOBase:\n    @property\n    def char(io) -> bool: ...\n    @property\n\
    \    def writable(io) -> bool: ...\n    def __next__(io) -> str: ...\n    def\
    \ write(io, s: str) -> None: ...\n    def readline(io) -> str: ...\n    def readtoken(io)\
    \ -> str: ...\n    def readtokens(io) -> list[str]: ...\n    def readints(io)\
    \ -> list[int]: ...\n    def readdigits(io) -> list[int]: ...\n    def readnums(io)\
    \ -> list[int]: ...\n    def readchar(io) -> str: ...\n    def readchars(io) ->\
    \ str: ...\n    def readinto(io, lst: list[str]) -> list[str]: ...\n    def readcharsinto(io,\
    \ lst: list[str]) -> list[str]: ...\n    def readtokensinto(io, lst: list[str])\
    \ -> list[str]: ...\n    def readintsinto(io, lst: list[int]) -> list[int]: ...\n\
    \    def readdigitsinto(io, lst: list[int]) -> list[int]: ...\n    def readnumsinto(io,\
    \ lst: list[int]) -> list[int]: ...\n    def wait(io): ...\n    def flush(io)\
    \ -> None: ...\n    def line(io) -> list[str]: ...\n\nclass TreeBase(GraphBase):\n\
    \    @overload\n    def distance(T) -> list[list[int]]: ...\n    @overload\n \
    \   def distance(T, s: int = 0) -> list[int]: ...\n    @overload\n    def distance(T,\
    \ s: int, g: int) -> int: ...\n    def distance(T, s = None, g = None):\n    \
    \    if s == None:\n            return [T.dfs_distance(u) for u in range(T.N)]\n\
    \        else:\n            return T.dfs_distance(s, g)\n\n    @overload\n   \
    \ def diameter(T) -> int: ...\n    @overload\n    def diameter(T, endpoints: Literal[True])\
    \ -> tuple[int,int,int]: ...\n    def diameter(T, endpoints = False):\n      \
    \  mask = (1 << (shift := T.N.bit_length())) - 1\n        s = max(d << shift |\
    \ v for v,d in enumerate(T.distance(0))) & mask\n        dg = max(d << shift |\
    \ v for v,d in enumerate(T.distance(s))) \n        diam, g = dg >> shift, dg &\
    \ mask\n        return (diam, s, g) if endpoints else diam\n    \n    def dfs_distance(T,\
    \ s: int, g: Union[int,None] = None):\n        st, Va = elist(N := T.N), T.Va\n\
    \        T.D, T.back = D, back = [inf]*N, i32f(N, -1)\n        D[s] = 0\n    \
    \    st.append(s)\n        while st:\n            nd = D[u := st.pop()]+1\n  \
    \          if u == g: return nd-1\n            for i in T.range(u):\n        \
    \        if nd < D[v := Va[i]]:\n                    D[v], back[v] = nd, i\n \
    \                   st.append(v)\n        return D if g is None else inf\n\n \
    \   def rerooting_dp(T, e: _T, \n                     merge: Callable[[_T,_T],_T],\
    \ \n                     edge_op: Callable[[_T,int,int,int],_T] = lambda s,i,p,u:s,\n\
    \                     s: int = 0):\n        La, Ua, Va = T.La, T.Ua, T.Va\n  \
    \      order, dp, suf, I = T.dfs_topo(s), [e]*T.N, [e]*len(Ua), T.Ra[:]\n    \
    \    # up\n        for i in order[::-1]:\n            u,v = Ua[i], Va[i]\n   \
    \         # subtree v finished up pass, store value to accumulate for u\n    \
    \        dp[v] = new = edge_op(dp[v], i, u, v)\n            dp[u] = merge(dp[u],\
    \ new)\n            # suffix accumulation\n            if (c:=I[u]-1) > La[u]:\
    \ suf[c-1] = merge(suf[c], new)\n            I[u] = c\n        # down\n      \
    \  dp[s] = e # at this point dp stores values to be merged in parent\n       \
    \ for i in order:\n            u,v = Ua[i], Va[i]\n            dp[u] = merge(pre\
    \ := dp[u], dp[v])\n            dp[v] = edge_op(merge(suf[I[u]], pre), i, v, u)\n\
    \            I[u] += 1\n        return dp\n    \n    def euler_tour(T, s = 0):\n\
    \        N, Va = len(T), T.Va\n        tin, tout, par, back = [-1]*N,[-1]*N,[-1]*N,[0]*N\n\
    \        order, delta = elist(2*N), elist(2*N)\n        \n        st = elist(N);\
    \ st.append(s)\n        while st:\n            p = par[u := st.pop()]\n      \
    \      if tin[u] == -1:\n                tin[u] = len(order)\n               \
    \ for i in T.range(u):\n                    if (v := Va[i]) != p:\n          \
    \              par[v], back[v] = u, i\n                        st.append(u); st.append(v)\n\
    \                delta.append(1)\n            else:\n                delta.append(-1)\n\
    \            \n            order.append(u)\n            tout[u] = len(order)\n\
    \        delta[0] = delta[-1] = 0\n        T.tin, T.tout, T.par, T.back = tin,\
    \ tout, par, back\n        T.order, T.delta = order, delta\n\n    @classmethod\n\
    \    def compile(cls, N: int, shift: int = -1):\n        return GraphBase.compile.__func__(cls,\
    \ N, N-1, shift)\n    \n\nclass HLDBase:\n    def __init__(hld, T: TreeBase, r=0):\n\
    \        hld.N, hld.T = len(T), T\n        N, time, Va = T.N, 0, T.Va\n      \
    \  tin, tout, size = [0]*N, [0]*N, [1]*N+[0]\n        back, heavy, head = [-1]*N,\
    \ [-1]*N, [r]*N\n        depth, order, vis = [0]*N, [0]*N, [0]*N\n        st =\
    \ elist(N); st.append(r)\n        while st:\n            if (s := vis[v := st.pop()])\
    \ == 0: # dfs down\n                vis[v], j = 1, back[v]; st.append(v)\n   \
    \             for i in T.range(v):\n                    if i != j:\n         \
    \               depth[c := Va[i]], back[c] = depth[v]+1, T.twin[i]; st.append(c)\n\
    \            elif s == 1: # dfs up\n                l, j = -1, back[v]\n     \
    \           for i in T.range(v):\n                    if i != j:\n           \
    \             size[v] += size[c := Va[i]]\n                        if size[c]\
    \ > size[l]: l = c\n                heavy[v] = l\n                if j == -1:\
    \ vis[v] = 2; st.append(v)\n\n            elif s == 2: # decompose down\n    \
    \            h, l, j = head[v], heavy[v], back[v]\n                tin[v], order[time],\
    \ vis[v] = time, v, 3\n                time += 1; st.append(v)\n             \
    \   for i in T.range(v):\n                    if i != j and (c := Va[i]) != l:\n\
    \                        head[c], vis[c] = c, 2; st.append(c)\n              \
    \  if l != -1: head[l], vis[l] = h, 2; st.append(l)\n\n            elif s == 3:\
    \ # decompose up\n                tout[v] = time\n        hld.up = [-1]*N\n  \
    \      for u,h in enumerate(head):\n            if (j := back[h]) != -1:\n   \
    \             hld.up[u] = T.Va[j]\n\n        hld.size, hld.depth = size, depth\n\
    \        hld.order, hld.tin, hld.tout = order, tin, tout\n        hld.heavy, hld.head,\
    \ hld.back = heavy, head, back\n\n    def subtree_range(hld, v):\n        return\
    \ hld.tin[v], hld.tout[v]\n\n\nclass HLDBIT(HLDBase):\n    def __init__(hld, T:\
    \ TreeBase, A: list[int], r=0):\n        super().__init__(T, r)\n        if len(A)\
    \ == T.N:\n            hld.bit = BIT([A[u] for u in hld.order])\n            hld.edge_queries\
    \ = False\n            hld.ptr = hld.tin\n        elif len(A) == T.M:\n      \
    \      hld.bit = BIT([A[T.Ea[i]] if (i := hld.back[u]) >= 0 else 0 for u in hld.order])\n\
    \            hld.edge_queries = True\n            hld.ptr = [0]*T.M\n        \
    \    for i in hld.back:\n                if i == -1: continue\n              \
    \  hld.ptr[T.Ea[i]] = hld.tin[T.Ua[i]]\n    \n    def add(hld, u: int, x: int):\n\
    \        hld.bit.add(hld.ptr[u], x)\n        \n    def get(hld, u: int):\n   \
    \     return hld.bit.get(hld.ptr[u])\n    __getitem__ = get\n\n    def set(hld,\
    \ u: int, x: int):\n        hld.bit.set(hld.ptr[u], x)\n    __setitem__ = set\n\
    \n    def subtree_range(hld, u):\n        return hld.tin[u]+hld.edge_queries,\
    \ hld.tout[u]\n\n    def subtree_query(hld, u):\n        l, r = hld.subtree_range(u)\n\
    \        return hld.bit.sum_range(l, r)\n\n    def path_query(hld, u, v):\n  \
    \      us = uv = 0\n        while hld.head[u] != hld.head[v]:\n            if\
    \ hld.depth[hld.head[u]] < hld.depth[hld.head[v]]:\n                uv += hld.bit.sum_range(hld.tin[hld.head[v]],\
    \ hld.tin[v]+1)\n                v = hld.up[v]\n            else:\n          \
    \      us += hld.bit.sum_range(hld.tin[hld.head[u]], hld.tin[u]+1)\n         \
    \       u = hld.up[u]\n\n        if hld.depth[u] < hld.depth[v]:\n           \
    \ return us+hld.bit.sum_range(hld.tin[u]+hld.edge_queries, hld.tin[v]+1)+uv\n\
    \        else:\n            return us+hld.bit.sum_range(hld.tin[v]+hld.edge_queries,\
    \ hld.tin[u]+1)+uv\n\n\n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2578\n            \u250F\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2513            \n            \u2503         \
    \                           7 \u2503            \n            \u2517\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u252F\u2501\u251B           \
    \ \n            \u250F\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2513                 \u2502\
    \              \n            \u2503                3 \u2503\u25C4\u2500\u2500\u2500\
    \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\
    \u2524              \n            \u2517\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u252F\u2501\u251B     \
    \            \u2502              \n            \u250F\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2513       \u2502  \u250F\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2513       \u2502              \n            \u2503      1 \u2503\
    \u25C4\u2500\u2500\u2500\u2500\u2500\u2500\u2524  \u2503      5 \u2503\u25C4\u2500\
    \u2500\u2500\u2500\u2500\u2500\u2524              \n            \u2517\u2501\u2501\
    \u2501\u2501\u2501\u2501\u252F\u2501\u251B       \u2502  \u2517\u2501\u2501\u2501\
    \u2501\u2501\u2501\u252F\u2501\u251B       \u2502              \n            \u250F\
    \u2501\u2501\u2501\u2513  \u2502  \u250F\u2501\u2501\u2501\u2513  \u2502  \u250F\
    \u2501\u2501\u2501\u2513  \u2502  \u250F\u2501\u2501\u2501\u2513  \u2502     \
    \         \n            \u2503 0 \u2503\u25C4\u2500\u2524  \u2503 2 \u2503\u25C4\
    \u2500\u2524  \u2503 4 \u2503\u25C4\u2500\u2524  \u2503 6 \u2503\u25C4\u2500\u2524\
    \              \n            \u2517\u2501\u252F\u2501\u251B  \u2502  \u2517\u2501\
    \u252F\u2501\u251B  \u2502  \u2517\u2501\u252F\u2501\u251B  \u2502  \u2517\u2501\
    \u252F\u2501\u251B  \u2502              \n              \u2502    \u2502    \u2502\
    \    \u2502    \u2502    \u2502    \u2502    \u2502              \n          \
    \    \u25BC    \u25BC    \u25BC    \u25BC    \u25BC    \u25BC    \u25BC    \u25BC\
    \              \n            \u250F\u2501\u2501\u2501\u2513\u250F\u2501\u2501\u2501\
    \u2513\u250F\u2501\u2501\u2501\u2513\u250F\u2501\u2501\u2501\u2513\u250F\u2501\
    \u2501\u2501\u2513\u250F\u2501\u2501\u2501\u2513\u250F\u2501\u2501\u2501\u2513\
    \u250F\u2501\u2501\u2501\u2513            \n            \u2503 0 \u2503\u2503\
    \ 1 \u2503\u2503 2 \u2503\u2503 3 \u2503\u2503 4 \u2503\u2503 5 \u2503\u2503 6\
    \ \u2503\u2503 7 \u2503            \n            \u2517\u2501\u2501\u2501\u251B\
    \u2517\u2501\u2501\u2501\u251B\u2517\u2501\u2501\u2501\u251B\u2517\u2501\u2501\
    \u2501\u251B\u2517\u2501\u2501\u2501\u251B\u2517\u2501\u2501\u2501\u251B\u2517\
    \u2501\u2501\u2501\u251B\u2517\u2501\u2501\u2501\u251B            \n\u257A\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\n           Data\
    \ Structure - Tree - Binary Index Tree            \n'''\n\nclass BIT:\n    def\
    \ __init__(bit, v):\n        if isinstance(v, int): bit._d, bit._n = [0]*v, v\n\
    \        else: bit.build(v)\n        bit._lb = 1<<bit._n.bit_length()\n\n    def\
    \ build(bit, data):\n        bit._d, bit._n = data, len(data)\n        for i in\
    \ range(bit._n):\n            if (r := i|i+1) < bit._n: bit._d[r] += bit._d[i]\n\
    \n    def add(bit, i, x):\n        while i < bit._n: bit._d[i] += x; i |= i+1\n\
    \n    def sum(bit, n: int) -> int:\n        s = 0\n        while n: s, n = s+bit._d[n-1],\
    \ n&n-1\n        return s\n\n    def sum_range(bit, l, r):\n        s = 0\n  \
    \      while r: s, r = s+bit._d[r-1], r&r-1\n        while l: s, l = s-bit._d[l-1],\
    \ l&l-1\n        return s\n\n    def __len__(bit) -> int:\n        return bit._n\n\
    \    \n    def __getitem__(bit, i: int) -> int:\n        s, l = bit._d[i], i&(i+1)\n\
    \        while l != i: s, i = s-bit._d[i-1], i-(i&-i)\n        return s\n    get\
    \ = __getitem__\n    \n    def __setitem__(bit, i: int, x: int) -> None: bit.add(i,\
    \ x-bit[i])\n    set = __setitem__\n\n    def prelist(bit) -> list[int]:\n   \
    \     pre = [0]+bit._d\n        for i in range(bit._n+1): pre[i] += pre[i&i-1]\n\
    \        return pre\n\n    def bisect_left(bit, v) -> int:\n        return bit.bisect_right(v-1)\
    \ if v>0 else -1\n    \n    def bisect_right(bit, v, key=None) -> int:\n     \
    \   i = s = 0; m = bit._lb\n        if key:\n            while m := m>>1:\n  \
    \              if (ni := m|i) <= bit._n and key(ns:=s+bit._d[ni-1]) <= v: s, i\
    \ = ns, ni\n        else:\n            while m := m>>1:\n                if (ni\
    \ := m|i) <= bit._n and (ns:=s+bit._d[ni-1]) <= v: s, i = ns, ni\n        return\
    \ i\n\n\nclass Graph(GraphBase):\n    def __init__(G, N: int, U: list[int], V:\
    \ list[int]):\n        M, Ma, deg = len(U), 0, u32f(N)\n        for e in range(M\
    \ := len(U)):\n            distinct = (u := U[e]) != (v := V[e])\n           \
    \ deg[u] += 1; deg[v] += distinct; Ma += 1+distinct\n        twin, Ea, Ua, Va,\
    \ La, Ra, i = i32f(Ma), i32f(Ma), u32f(Ma), u32f(Ma), u32f(N), u32f(N), 0\n  \
    \      for u in range(N): La[u] = Ra[u] = i; i = i+deg[u]\n        for e in range(M):\n\
    \            i, j = Ra[u := U[e]], Ra[v := V[e]]\n            Ra[u], Ua[i], Va[i],\
    \ Ea[i], twin[i] = i+1, u, v, e, j\n            if i == j: continue\n        \
    \    Ra[v], Ua[j], Va[j], Ea[j], twin[j] = j+1, v, u, e, i\n        super().__init__(N,\
    \ M, U, V, deg, La, Ra, Ua, Va, Ea, twin)\n\nclass Tree(TreeBase, Graph):\n  \
    \  pass\n\nfrom typing import Type, Union, overload\n\n@overload\ndef read() ->\
    \ list[int]: ...\n@overload\ndef read(spec: Type[_T], char=False) -> _T: ...\n\
    @overload\ndef read(spec: _U, char=False) -> _U: ...\n@overload\ndef read(*specs:\
    \ Type[_T], char=False) -> tuple[_T, ...]: ...\n@overload\ndef read(*specs: _U,\
    \ char=False) -> tuple[_U, ...]: ...\ndef read(*specs: Union[Type[_T],_T], char=False):\n\
    \    IO.stdin.char = char\n    if not specs: return IO.stdin.readnumsinto([])\n\
    \    parser: _T = Parser.compile(specs[0] if len(specs) == 1 else specs)\n   \
    \ return parser(IO.stdin)\nfrom os import read as os_read, write as os_write,\
    \ fstat as os_fstat\nfrom __pypy__.builders import StringBuilder\n\ndef max2(a,\
    \ b): return a if a > b else b\n\nclass IO(IOBase):\n    BUFSIZE = 1 << 16; stdin:\
    \ 'IO'; stdout: 'IO'\n    __slots__ = 'f', 'file', 'B', 'O', 'V', 'S', 'l', 'p',\
    \ 'char', 'sz', 'st', 'ist', 'writable', 'encoding', 'errors'\n    def __init__(io,\
    \ file):\n        io.file = file\n        try: io.f = file.fileno(); io.sz, io.writable\
    \ = max2(io.BUFSIZE, os_fstat(io.f).st_size), ('x' in file.mode or 'r' not in\
    \ file.mode)\n        except: io.f, io.sz, io.writable = -1, io.BUFSIZE, False\n\
    \        io.B, io.O, io.S = bytearray(), [], StringBuilder(); io.V = memoryview(io.B);\
    \ io.l = io.p = 0\n        io.char, io.st, io.ist, io.encoding, io.errors = False,\
    \ [], [], 'ascii', 'ignore'\n    def _dec(io, l, r): return io.V[l:r].tobytes().decode(io.encoding,\
    \ io.errors)\n    def readbytes(io, sz): return os_read(io.f, sz)\n    def load(io):\n\
    \        while io.l >= len(io.O):\n            if not (b := io.readbytes(io.sz)):\n\
    \                if io.O[-1] < len(io.B): io.O.append(len(io.B))\n           \
    \     break\n            pos = len(io.B); io.B.extend(b)\n            while ~(pos\
    \ := io.B.find(b'\\n', pos)): io.O.append(pos := pos+1)\n    def __next__(io):\n\
    \        if io.char: return io.readchar()\n        else: return io.readtoken()\n\
    \    def readchar(io):\n        io.load(); r = io.O[io.l]\n        c = chr(io.B[io.p])\n\
    \        if io.p >= r-1: io.p = r; io.l += 1\n        else: io.p += 1\n      \
    \  return c\n    def write(io, s: str): io.S.append(s)\n    def readline(io):\
    \ io.load(); l, io.p = io.p, io.O[io.l]; io.l += 1; return io._dec(l, io.p)\n\
    \    def readtoken(io):\n        io.load(); r = io.O[io.l]\n        if ~(p :=\
    \ io.B.find(b' ', io.p, r)): s = io._dec(io.p, p); io.p = p+1\n        else: s\
    \ = io._dec(io.p, r-1); io.p = r; io.l += 1\n        return s\n    def readtokens(io):\
    \ io.st.clear(); return io.readtokensinto(io.st)\n    def readints(io): io.ist.clear();\
    \ return io.readintsinto(io.ist)\n    def readdigits(io): io.ist.clear(); return\
    \ io.readdigitsinto(io.ist)\n    def readnums(io): io.ist.clear(); return io.readnumsinto(io.ist)\n\
    \    def readchars(io): io.load(); l, io.p = io.p, io.O[io.l]; io.l += 1; return\
    \ io._dec(l, io.p-1)\n    def readinto(io, lst):\n        if io.char: return io.readcharsinto(lst)\n\
    \        else: return io.readtokensinto(lst)\n    def readcharsinto(io, lst):\
    \ lst.extend(io.readchars()); return lst\n    def readtokensinto(io, lst): \n\
    \        io.load(); r = io.O[io.l]\n        while ~(p := io.B.find(b' ', io.p,\
    \ r)): lst.append(io._dec(io.p, p)); io.p = p+1\n        lst.append(io._dec(io.p,\
    \ r-1)); io.p = r; io.l += 1; return lst\n    def _readint(io, r):\n        while\
    \ io.p < r and io.B[io.p] <= 32: io.p += 1\n        if io.p >= r: return None\n\
    \        minus = x = 0\n        if io.B[io.p] == 45: minus = 1; io.p += 1\n  \
    \      while io.p < r and io.B[io.p] >= 48: x = x * 10 + (io.B[io.p] & 15); io.p\
    \ += 1\n        io.p += 1\n        return -x if minus else x\n    def readintsinto(io,\
    \ lst):\n        io.load(); r = io.O[io.l]\n        while io.p < r and (x := io._readint(r))\
    \ is not None: lst.append(x)\n        io.l += 1; return lst\n    def _readdigit(io):\
    \ d = io.B[io.p] & 15; io.p += 1; return d\n    def readdigitsinto(io, lst):\n\
    \        io.load(); r = io.O[io.l]\n        while io.p < r and io.B[io.p] > 32:\
    \ lst.append(io._readdigit())\n        if io.B[io.p] == 10: io.l += 1\n      \
    \  io.p += 1\n        return lst\n    def readnumsinto(io, lst):\n        if io.char:\
    \ return io.readdigitsinto(lst)\n        else: return io.readintsinto(lst)\n \
    \   def line(io): io.st.clear(); return io.readinto(io.st)\n    def wait(io):\n\
    \        io.load(); r = io.O[io.l]\n        while io.p < r: yield\n    def flush(io):\n\
    \        if io.writable: os_write(io.f, io.S.build().encode(io.encoding, io.errors));\
    \ io.S = StringBuilder()\nsys.stdin = IO.stdin = IO(sys.stdin); sys.stdout = IO.stdout\
    \ = IO(sys.stdout)\nimport typing\nfrom numbers import Number\nfrom typing import\
    \ Callable, Collection\n\nclass Parser:\n    def __init__(self, spec):  self.parse\
    \ = Parser.compile(spec)\n    def __call__(self, io: IOBase): return self.parse(io)\n\
    \    @staticmethod\n    def compile_type(cls, args = ()):\n        if issubclass(cls,\
    \ Parsable): return cls.compile(*args)\n        elif issubclass(cls, (Number,\
    \ str)):\n            def parse(io: IOBase): return cls(next(io))            \
    \  \n            return parse\n        elif issubclass(cls, tuple): return Parser.compile_tuple(cls,\
    \ args)\n        elif issubclass(cls, Collection): return Parser.compile_collection(cls,\
    \ args)\n        elif callable(cls):\n            def parse(io: IOBase): return\
    \ cls(next(io))              \n            return parse\n        else: raise NotImplementedError()\n\
    \    @staticmethod\n    def compile(spec=int):\n        if isinstance(spec, (type,\
    \ GenericAlias)):\n            cls, args = typing.get_origin(spec) or spec, typing.get_args(spec)\
    \ or tuple()\n            return Parser.compile_type(cls, args)\n        elif\
    \ isinstance(offset := spec, Number): \n            cls = type(spec)  \n     \
    \       def parse(io: IOBase): return cls(next(io)) + offset\n            return\
    \ parse\n        elif isinstance(args := spec, tuple): return Parser.compile_tuple(type(spec),\
    \ args)\n        elif isinstance(args := spec, Collection): return Parser.compile_collection(type(spec),\
    \ args)\n        elif isinstance(fn := spec, Callable): \n            def parse(io:\
    \ IOBase): return fn(next(io))\n            return parse\n        else: raise\
    \ NotImplementedError()\n    @staticmethod\n    def compile_line(cls, spec=int):\n\
    \        if spec is int:\n            def parse(io: IOBase): return cls(io.readnums())\n\
    \        elif spec is str:\n            def parse(io: IOBase): return cls(io.line())\n\
    \        else:\n            fn = Parser.compile(spec)\n            def parse(io:\
    \ IOBase): return cls((fn(io) for _ in io.wait()))\n        return parse\n   \
    \ @staticmethod\n    def compile_repeat(cls, spec, N):\n        fn = Parser.compile(spec)\n\
    \        def parse(io: IOBase): return cls([fn(io) for _ in range(N)])\n     \
    \   return parse\n    @staticmethod\n    def compile_children(cls, specs):\n \
    \       fns = tuple((Parser.compile(spec) for spec in specs))\n        def parse(io:\
    \ IOBase): return cls([fn(io) for fn in fns])  \n        return parse\n    @staticmethod\n\
    \    def compile_tuple(cls, specs):\n        if isinstance(specs, (tuple,list))\
    \ and len(specs) == 2 and specs[1] is ...: return Parser.compile_line(cls, specs[0])\n\
    \        else: return Parser.compile_children(cls, specs)\n    @staticmethod\n\
    \    def compile_collection(cls, specs):\n        if not specs or len(specs) ==\
    \ 1 or isinstance(specs, set):\n            return Parser.compile_line(cls, *specs)\n\
    \        elif (isinstance(specs, (tuple,list)) and len(specs) == 2 and isinstance(specs[1],\
    \ int)):\n            return Parser.compile_repeat(cls, specs[0], specs[1])\n\
    \        else:\n            raise NotImplementedError()\n\ndef write(*args, **kwargs):\n\
    \    '''Prints the values to a stream, or to stdout_fast by default.'''\n    sep,\
    \ file = kwargs.pop(\"sep\", \" \"), kwargs.pop(\"file\", IO.stdout)\n    at_start\
    \ = True\n    for x in args:\n        if not at_start:\n            file.write(sep)\n\
    \        file.write(str(x))\n        at_start = False\n    file.write(kwargs.pop(\"\
    end\", \"\\n\"))\n    if kwargs.pop(\"flush\", False):\n        file.flush()\n\
    import operator\nfrom itertools import accumulate\nfrom typing import Callable,\
    \ Iterable\n\n\ndef presum(iter: Iterable[_T], func: Callable[[_T,_T],_T] = None,\
    \ initial: _T = None, step = 1) -> list[_T]:\n    if step == 1:\n        return\
    \ list(accumulate(iter, func, initial=initial))\n    else:\n        assert step\
    \ >= 2\n        if func is None:\n            func = operator.add\n        A =\
    \ list(iter)\n        if initial is not None:\n            A = [initial] + A\n\
    \        for i in range(step,len(A)):\n            A[i] = func(A[i], A[i-step])\n\
    \        return A\n\nif __name__ == \"__main__\":\n    main()\n"
  code: "# verification-helper: PROBLEM https://atcoder.jp/contests/abc337/tasks/abc337_g\n\
    \ndef main():\n    N = read(int)\n    T = read(Tree[N])\n    hld, ans = HLDBIT(T,\
    \ [0]*N), [0]*(N+1)\n\n    def range_add(l,r,x):\n        ans[l] += x\n      \
    \  ans[r] -= x\n\n    for u in range(N):\n        l,r = hld.subtree_range(u)\n\
    \        range_add(l,r,u-hld.subtree_query(u))\n        for i in T.range(u):\n\
    \            if i != hld.back[u]:\n                l,r = hld.subtree_range(T.Va[i])\n\
    \                cnt = hld.subtree_query(T.Va[i])\n                range_add(0,l,cnt)\n\
    \                range_add(r,N,cnt)\n        hld.add(u,1)\n    ans = presum(ans)\n\
    \    ans = [ans[i] for i in hld.tin]\n    write(*ans)\n\nfrom cp_library.alg.tree.csr.hld_bit_cls\
    \ import HLDBIT\nfrom cp_library.alg.tree.csr.tree_cls import Tree\nfrom cp_library.io.read_fn\
    \ import read\nfrom cp_library.io.write_fn import write\nfrom cp_library.alg.iter.presum_fn\
    \ import presum\n\nif __name__ == \"__main__\":\n    main()"
  dependsOn:
  - cp_library/alg/tree/csr/hld_bit_cls.py
  - cp_library/alg/tree/csr/tree_cls.py
  - cp_library/io/read_fn.py
  - cp_library/io/write_fn.py
  - cp_library/alg/iter/presum_fn.py
  - cp_library/alg/tree/csr/hld_base_cls.py
  - cp_library/alg/tree/csr/tree_base_cls.py
  - cp_library/ds/tree/bit/bit_cls.py
  - cp_library/alg/graph/csr/graph_cls.py
  - cp_library/io/io_cls.py
  - cp_library/io/parser_cls.py
  - cp_library/ds/list/elist_fn.py
  - cp_library/alg/graph/csr/graph_base_cls.py
  - cp_library/ds/array/i32f_fn.py
  - cp_library/ds/array/u32f_fn.py
  - cp_library/io/io_base_cls.py
  - cp_library/io/parsable_cls.py
  - cp_library/alg/dp/max2_fn.py
  - cp_library/ds/view/view_cls.py
  - cp_library/alg/dp/chmin_fn.py
  - cp_library/alg/graph/dfs_options_cls.py
  - cp_library/bit/masks/u32_max_cnst.py
  - cp_library/bit/masks/i32_max_cnst.py
  - cp_library/ds/array/u8f_fn.py
  - cp_library/ds/packet_list_cls.py
  - cp_library/ds/que/que_cls.py
  - cp_library/ds/list/list_find_fn.py
  isVerificationFile: true
  path: test/atcoder/abc/abc337_g_tree_inversion_hld_bit.test.py
  requiredBy: []
  timestamp: '2025-07-28 19:59:52+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/atcoder/abc/abc337_g_tree_inversion_hld_bit.test.py
layout: document
redirect_from:
- /verify/test/atcoder/abc/abc337_g_tree_inversion_hld_bit.test.py
- /verify/test/atcoder/abc/abc337_g_tree_inversion_hld_bit.test.py.html
title: test/atcoder/abc/abc337_g_tree_inversion_hld_bit.test.py
---
