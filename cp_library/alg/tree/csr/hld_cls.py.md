---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/dp/chmin_fn.py
    title: cp_library/alg/dp/chmin_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/csr/graph_base_cls.py
    title: cp_library/alg/graph/csr/graph_base_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/dfs_options_cls.py
    title: cp_library/alg/graph/dfs_options_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/csr/hld_base_cls.py
    title: cp_library/alg/tree/csr/hld_base_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/csr/tree_base_cls.py
    title: cp_library/alg/tree/csr/tree_base_cls.py
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
    path: cp_library/ds/view/view_cls.py
    title: cp_library/ds/view/view_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/io_base_cls.py
    title: cp_library/io/io_base_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/parsable_cls.py
    title: cp_library/io/parsable_cls.py
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/csr/hld_weighted_cls.py
    title: cp_library/alg/tree/csr/hld_weighted_cls.py
  - icon: ':warning:'
    path: test/library-checker/tree/vertex_add_path_sum_hld.test copy.py
    title: test/library-checker/tree/vertex_add_path_sum_hld.test copy.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/atcoder/abc/abc294_g_fast_tree_hld.test.py
    title: test/atcoder/abc/abc294_g_fast_tree_hld.test.py
  - icon: ':heavy_check_mark:'
    path: test/atcoder/abc/abc337_g_tree_inversion_hld_fast.test.py
    title: test/atcoder/abc/abc337_g_tree_inversion_hld_fast.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/tree/vertex_add_path_sum_hld.test.py
    title: test/library-checker/tree/vertex_add_path_sum_hld.test.py
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
    \n\n\nfrom math import inf\nfrom typing import Callable, Literal, Union, overload\n\
    \nfrom typing import Generic\nfrom typing import TypeVar\n_S = TypeVar('S'); _T\
    \ = TypeVar('T'); _U = TypeVar('U'); _T1 = TypeVar('T1'); _T2 = TypeVar('T2');\
    \ _T3 = TypeVar('T3'); _T4 = TypeVar('T4'); _T5 = TypeVar('T5'); _T6 = TypeVar('T6')\n\
    \n\nimport sys\n\ndef list_find(lst: list, value, start = 0, stop = sys.maxsize):\n\
    \    try:\n        return lst.index(value, start, stop)\n    except:\n       \
    \ return -1\n\n\nclass view(Generic[_T]):\n    __slots__ = 'A', 'l', 'r'\n   \
    \ def __init__(V, A: list[_T], l: int = 0, r: int = 0): V.A, V.l, V.r = A, l,\
    \ r\n    def __len__(V): return V.r - V.l\n    def __getitem__(V, i: int): \n\
    \        if 0 <= i < V.r - V.l: return V.A[V.l+i]\n        else: raise IndexError\n\
    \    def __setitem__(V, i: int, v: _T): V.A[V.l+i] = v\n    def __contains__(V,\
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
    \ hld.tin[v], hld.tout[v]\n\n\nclass HLD(HLDBase):\n\n    def path_query(hld,\
    \ u, v, query_fn, edge=False):\n        while hld.head[u] != hld.head[v]:\n  \
    \          if hld.depth[hld.head[u]] < hld.depth[hld.head[v]]:\n             \
    \   query_fn(hld.tin[hld.head[v]], hld.tin[v]+1)\n                v = hld.up[v]\n\
    \            else:\n                query_fn(hld.tin[hld.head[u]], hld.tin[u]+1)\n\
    \                u = hld.up[u]\n\n        if hld.depth[u] < hld.depth[v]:\n  \
    \          query_fn(hld.tin[u]+edge, hld.tin[v]+1)\n        else:\n          \
    \  query_fn(hld.tin[v]+edge, hld.tin[u]+1)\n"
  code: "import cp_library.__header__\nimport cp_library.alg.__header__\nimport cp_library.alg.tree.__header__\n\
    import cp_library.alg.tree.csr.__header__\nfrom cp_library.alg.tree.csr.hld_base_cls\
    \ import HLDBase\n\nclass HLD(HLDBase):\n\n    def path_query(hld, u, v, query_fn,\
    \ edge=False):\n        while hld.head[u] != hld.head[v]:\n            if hld.depth[hld.head[u]]\
    \ < hld.depth[hld.head[v]]:\n                query_fn(hld.tin[hld.head[v]], hld.tin[v]+1)\n\
    \                v = hld.up[v]\n            else:\n                query_fn(hld.tin[hld.head[u]],\
    \ hld.tin[u]+1)\n                u = hld.up[u]\n\n        if hld.depth[u] < hld.depth[v]:\n\
    \            query_fn(hld.tin[u]+edge, hld.tin[v]+1)\n        else:\n        \
    \    query_fn(hld.tin[v]+edge, hld.tin[u]+1)\n"
  dependsOn:
  - cp_library/alg/tree/csr/hld_base_cls.py
  - cp_library/alg/tree/csr/tree_base_cls.py
  - cp_library/ds/list/elist_fn.py
  - cp_library/alg/graph/csr/graph_base_cls.py
  - cp_library/ds/array/i32f_fn.py
  - cp_library/ds/view/view_cls.py
  - cp_library/io/parsable_cls.py
  - cp_library/alg/dp/chmin_fn.py
  - cp_library/alg/graph/dfs_options_cls.py
  - cp_library/bit/masks/u32_max_cnst.py
  - cp_library/bit/masks/i32_max_cnst.py
  - cp_library/ds/array/u8f_fn.py
  - cp_library/ds/array/u32f_fn.py
  - cp_library/ds/packet_list_cls.py
  - cp_library/ds/que/que_cls.py
  - cp_library/io/io_base_cls.py
  - cp_library/ds/list/list_find_fn.py
  isVerificationFile: false
  path: cp_library/alg/tree/csr/hld_cls.py
  requiredBy:
  - test/library-checker/tree/vertex_add_path_sum_hld.test copy.py
  - cp_library/alg/tree/csr/hld_weighted_cls.py
  timestamp: '2025-07-28 14:17:34+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library-checker/tree/vertex_add_path_sum_hld.test.py
  - test/atcoder/abc/abc294_g_fast_tree_hld.test.py
  - test/atcoder/abc/abc337_g_tree_inversion_hld_fast.test.py
documentation_of: cp_library/alg/tree/csr/hld_cls.py
layout: document
redirect_from:
- /library/cp_library/alg/tree/csr/hld_cls.py
- /library/cp_library/alg/tree/csr/hld_cls.py.html
title: cp_library/alg/tree/csr/hld_cls.py
---
