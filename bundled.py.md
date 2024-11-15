---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    PROBLEM: https://atcoder.jp/contests/dp/tasks/dp_v
    links:
    - https://atcoder.jp/contests/dp/tasks/dp_v
    - https://kobejean.github.io/cp-library
  bundledCode: "# verification-helper: PROBLEM https://atcoder.jp/contests/dp/tasks/dp_v\n\
    \n\ndef main():\n    N, M = read(tuple[int, ...])\n    T = read(Tree[N])\n\n\n\
    \n    def merge(a,b):\n        return a*b%M\n\n    def add_node(v,res):\n    \
    \    return (res+1)%M\n    \n    e = 1\n    dp = [[e]*len(T[v]) for v in range(N)]\n\
    \    ans = [e]*N\n    pid = [0]*N\n    \n    def suffix_list(A: list):\n     \
    \   N = len(A)\n        suf = A[:] + [e]\n        for i in range(N, 0, -1):\n\
    \            suf[i-1] = merge(suf[i-1], suf[i]) \n        return suf\n\n    order\
    \ = T.dfs_topdown(0, True)\n    # up\n    for p, u in reversed(order):\n     \
    \   up = dp[u]\n        for c,v in enumerate(T[u]):\n            if v == p:\n\
    \                pid[u] = c\n            else:\n                up[c] = add_node(u,\
    \ ans[v])\n                ans[u] = merge(ans[u], up[c])\n    # down        \n\
    \    for p, u in order:\n        up = dp[u]\n        suf, pre = suffix_list(up),\
    \ e\n        for i,v in enumerate(T[u]):\n            if v != p:\n           \
    \     dp[v][pid[v]] = add_node(v, merge(suf[i+1], pre))\n            pre = merge(pre,\
    \ up[i])\n        ans[u] = pre\n\n    # print(*ans, sep='\\n')\n    write_int(ans,\
    \ sep='\\n')\n\nfrom array import array\nfrom math import ceil, log10\nimport\
    \ os\n\ndef write_int(numbers, sep = ' '):\n    sep = ord(sep)\n    # Convert\
    \ to array for memory efficiency and faster processing\n    arr = array('i', numbers)\
    \ \n    extreme = max(1,abs(max(numbers)), abs(min(numbers)))\n    chars_per_num\
    \ = ceil(log10(extreme)) + 2\n    # Pre-calculate approximate buffer size (assume\
    \ ~10 chars per number plus spaces)\n    buffer = bytearray(len(arr) * chars_per_num)\n\
    \    \n    # Track position in buffer\n    pos = 0\n    \n    # Convert numbers\
    \ to bytes and add to buffer\n    for num in arr:\n        # Convert integer to\
    \ string bytes\n        s = str(num).encode('ascii')\n        # Copy bytes to\
    \ buffer\n        buffer[pos:pos + len(s)] = s\n        buffer[pos + len(s)] =\
    \ sep  # ASCII space\n        pos += len(s) + 1\n    \n    # Write completed buffer\
    \ to stdout\n    os.write(1, memoryview(buffer)[:pos-1])  # Exclude trailing space\n\
    \    os.write(1, b'\\n')  # Add final newline\n\n\n\n'''\n\u257A\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\n             https://kobejean.github.io/cp-library\
    \               \n'''\n\n\n\nimport sys\nimport typing\nfrom collections import\
    \ deque\nfrom numbers import Number\nfrom types import GenericAlias \nfrom typing\
    \ import Callable, Collection, Iterator, TypeAlias, TypeVar\n\n# class TokenStream(Iterator):\n\
    #     def __init__(self, stream = sys.stdin):\n#         self.stream = stream\n\
    #         self.queue = deque()\n\n#     def __next__(self):\n#         if not\
    \ self.queue: self.queue.extend(self.line())\n#         return self.queue.popleft()\n\
    \    \n#     def wait(self):\n#         if not self.queue: self.queue.extend(self.line())\n\
    #         while self.queue: yield\n        \n#     def line(self):\n#        \
    \ assert not self.queue\n#         return next(self.stream).rstrip().split()\n\
    \nfrom typing import Iterator, List\n\n\nclass TokenStream(Iterator):\n    stream\
    \ = sys.stdin.buffer\n    buffer = bytearray()\n    pos = 0\n    \n    def __init__(self,\
    \ chunk_size=8192):\n        self.queue = deque()\n        self.chunk_size = chunk_size\n\
    \        \n    def __next__(self) -> str:\n        if not self.queue:\n      \
    \      while True:\n                if TokenStream.pos >= len(self.buffer):\n\
    \                    if not self._read_chunk():\n                        raise\
    \ StopIteration\n                \n                while TokenStream.pos < len(self.buffer):\n\
    \                    start = TokenStream.pos\n                    while (TokenStream.pos\
    \ < len(self.buffer) and \n                           self.buffer[TokenStream.pos]\
    \ not in (32, 10)):  # b' \\n'\n                        TokenStream.pos += 1\n\
    \                    if start != TokenStream.pos:\n                        return\
    \ self.buffer[start:TokenStream.pos].decode()\n                    TokenStream.pos\
    \ += 1  # skip delimiter\n                    \n        return self.queue.popleft()\n\
    \    \n    def wait(self):\n        if not self.queue:\n            self.queue.extend(self.line())\n\
    \        while self.queue:\n            yield\n            \n    def line(self)\
    \ -> List[str]:\n        \"\"\"Reads exactly one line and returns its tokens\"\
    \"\"\n        assert not self.queue\n        line = bytearray()\n        \n  \
    \      while True:\n            if TokenStream.pos >= len(self.buffer):\n    \
    \            if not self._read_chunk():\n                    if not line:\n  \
    \                      raise StopIteration\n                    return line.decode().split()\n\
    \            \n            end = TokenStream.pos\n            while end < len(self.buffer)\
    \ and self.buffer[end] != 10:  # \\n\n                end += 1\n             \
    \   \n            if end < len(self.buffer):  # found newline\n              \
    \  line.extend(self.buffer[TokenStream.pos:end])\n                TokenStream.pos\
    \ = end + 1\n                return line.decode().split()\n            \n    \
    \        # no newline found, append entire remainder and read more\n         \
    \   line.extend(self.buffer[TokenStream.pos:])\n            TokenStream.pos =\
    \ len(self.buffer)\n    \n    def int_line(self) -> array:\n        \"\"\"Returns\
    \ the next line as an array of integers\"\"\"\n        result = array('i')\n \
    \       current = 0\n        \n        while True:\n            if TokenStream.pos\
    \ >= len(self.buffer):\n                if not self._read_chunk():\n         \
    \           if current > 0:\n                        result.append(current)\n\
    \                    return result\n            \n            b = self.buffer[TokenStream.pos]\n\
    \            TokenStream.pos += 1\n            \n            if b >= 48:  # ASCII\
    \ '0'\n                current = current * 10 + (b - 48)\n            elif b ==\
    \ 32:  # space\n                result.append(current)\n                current\
    \ = 0\n            elif b == 10:  # newline\n                if current > 0 or\
    \ not result:  # handle trailing number or empty line\n                    result.append(current)\n\
    \                return result\n\n    def int_n(self, n: int) -> array:\n    \
    \    \"\"\"Returns exactly n integers or raises StopIteration\"\"\"\n        result\
    \ = array('i', [0]) * n\n        num_count = 0\n        current = 0\n        \n\
    \        while num_count < n:\n            if TokenStream.pos >= len(self.buffer):\n\
    \                if not self._read_chunk():\n                    if current >\
    \ 0 and num_count < n:\n                        result[num_count] = current\n\
    \                        num_count += 1\n                    break\n         \
    \   \n            b = self.buffer[TokenStream.pos]\n            TokenStream.pos\
    \ += 1\n            \n            if b >= 48:  # ASCII '0'\n                current\
    \ = current * 10 + (b - 48)\n            elif b in (32, 10):  # space or newline\n\
    \                result[num_count] = current\n                num_count += 1\n\
    \                current = 0\n                if num_count >= n:\n           \
    \         break\n        \n        if num_count < n:\n            raise StopIteration\n\
    \        return result\n    \n    def _read_chunk(self) -> bool:\n        \"\"\
    \"Read a chunk of data into buffer, return True if data was read\"\"\"\n     \
    \   if TokenStream.pos > 0:\n            # Remove processed data\n           \
    \ del self.buffer[:TokenStream.pos]\n            TokenStream.pos = 0\n       \
    \     \n        chunk = TokenStream.stream.read(self.chunk_size)\n        if not\
    \ chunk:\n            return False\n        self.buffer.extend(chunk)\n      \
    \  return True\nsys.stdin._CHUNK_SIZE = 1 << 24\n# print(sys.stdin._CHUNK_SIZE)\n\
    # class TokenStream(Iterator):\n#     def __init__(self, stream = sys.stdin):\n\
    #         self.stream = stream\n#         self.queue = deque()\n\n#     def __next__(self):\n\
    #         if not self.queue: self.queue.extend(self.line())\n#         return\
    \ self.queue.popleft()\n    \n#     def wait(self):\n#         if not self.queue:\
    \ self.queue.extend(self.line())\n#         while self.queue: yield\n        \n\
    #     def line(self):\n#         assert not self.queue\n#         return next(self.stream).rstrip().split()\n\
    \nclass CharStream(TokenStream):\n    def line(self):\n        assert not self.queue\n\
    \        return next(self.stream).rstrip()\n        \nT = TypeVar('T')\nParseFn:\
    \ TypeAlias = Callable[[TokenStream],T]\nclass Parser:\n    def __init__(self,\
    \ spec: type[T]|T):\n        self.parse = Parser.compile(spec)\n\n    def __call__(self,\
    \ ts: TokenStream) -> T:\n        return self.parse(ts)\n    \n    @staticmethod\n\
    \    def compile_type(cls: type[T], args = ()) -> T:\n        if issubclass(cls,\
    \ Parsable):\n            return cls.compile(*args)\n        elif issubclass(cls,\
    \ (Number, str)):\n            def parse(ts: TokenStream):\n                return\
    \ cls(next(ts))              \n            return parse\n        elif issubclass(cls,\
    \ tuple):\n            return Parser.compile_tuple(cls, args)\n        elif issubclass(cls,\
    \ Collection):\n            return Parser.compile_collection(cls, args)\n    \
    \    elif callable(cls):\n            def parse(ts: TokenStream):\n          \
    \      return cls(next(ts))              \n            return parse\n        else:\n\
    \            raise NotImplementedError()\n    \n    @staticmethod\n    def compile(spec:\
    \ type[T]|T=int) -> ParseFn[T]:\n        if isinstance(spec, (type, GenericAlias)):\n\
    \            cls = typing.get_origin(spec) or spec\n            args = typing.get_args(spec)\
    \ or tuple()\n            return Parser.compile_type(cls, args)\n        elif\
    \ isinstance(offset := spec, Number): \n            cls = type(spec)  \n     \
    \       def parse(ts: TokenStream):\n                return cls(next(ts)) + offset\n\
    \            return parse\n        elif isinstance(args := spec, tuple):     \
    \ \n            return Parser.compile_tuple(type(spec), args)\n        elif isinstance(args\
    \ := spec, Collection):  \n            return Parser.compile_collection(type(spec),\
    \ args)\n        else:\n            raise NotImplementedError()\n    \n    @staticmethod\n\
    \    def compile_line(cls: T, spec=int) -> ParseFn[T]:\n        fn = Parser.compile(spec)\n\
    \        def parse(ts: TokenStream):\n            return cls(fn(ts) for _ in ts.wait())\n\
    \        return parse\n\n    @staticmethod\n    def compile_repeat(cls: T, spec,\
    \ N) -> ParseFn[T]:\n        fn = Parser.compile(spec)\n        def parse(ts:\
    \ TokenStream):\n            return cls(fn(ts) for _ in range(N))\n        return\
    \ parse\n\n    @staticmethod\n    def compile_children(cls: T, specs) -> ParseFn[T]:\n\
    \        fns = tuple(Parser.compile(spec) for spec in specs)\n        def parse(ts:\
    \ TokenStream):\n            return cls(fn(ts) for fn in fns)  \n        return\
    \ parse\n\n    @staticmethod\n    def compile_tuple(cls: type[T], specs) -> ParseFn[T]:\n\
    \        match specs:\n            case [spec, end] if end is ...:\n         \
    \       return Parser.compile_line(cls, spec)\n            case specs:   \n  \
    \              return Parser.compile_children(cls, specs)\n    \n    @staticmethod\n\
    \    def compile_collection(cls, specs):\n        match specs:\n            case\
    \ [ ] | [_] | set():\n                return Parser.compile_line(cls, *specs)\n\
    \            case [spec, int() as n]:\n                return Parser.compile_repeat(cls,\
    \ spec, n)\n            case _:\n                raise NotImplementedError()\n\
    \n        \nclass Parsable:\n    @classmethod\n    def compile(cls):\n       \
    \ def parser(ts: TokenStream):\n            return cls(next(ts))\n        return\
    \ parser\n\nclass Edge(tuple, Parsable):\n    @classmethod\n    def compile(cls,\
    \ I=-1):\n        def parse(ts: TokenStream):\n            u,v = ts.line()\n \
    \           return cls((int(u)+I,int(v)+I))\n        return parse\n\nfrom enum\
    \ import auto, IntFlag, IntEnum\n\nclass DFSFlags(IntFlag):\n    ENTER = auto()\n\
    \    DOWN = auto()\n    BACK = auto()\n    CROSS = auto()\n    LEAVE = auto()\n\
    \    UP = auto()\n    MAXDEPTH = auto()\n\n    RETURN_PARENTS = auto()\n    RETURN_DEPTHS\
    \ = auto()\n    BACKTRACK = auto()\n    CONNECT_ROOTS = auto()\n\n    # Common\
    \ combinations\n    ALL_EDGES = DOWN | BACK | CROSS\n    EULER_TOUR = DOWN | UP\n\
    \    INTERVAL = ENTER | LEAVE\n    TOPDOWN = DOWN | CONNECT_ROOTS\n    BOTTOMUP\
    \ = UP | CONNECT_ROOTS\n    RETURN_ALL = RETURN_PARENTS | RETURN_DEPTHS\n\nclass\
    \ DFSEvent(IntEnum):\n    ENTER = DFSFlags.ENTER \n    DOWN = DFSFlags.DOWN \n\
    \    BACK = DFSFlags.BACK \n    CROSS = DFSFlags.CROSS \n    LEAVE = DFSFlags.LEAVE\
    \ \n    UP = DFSFlags.UP \n    MAXDEPTH = DFSFlags.MAXDEPTH\n    \ntry:\n    from\
    \ __pypy__ import newlist_hint\nexcept:\n    def newlist_hint(hint):\n       \
    \ return []\n    \ndef elist(est_len: int) -> list:\n    return newlist_hint(est_len)\n\
    from typing import Iterable, overload\nfrom math import inf\n\nclass GraphProtocol(list,\
    \ Parsable):\n    def __init__(G, N: int, E: list = None, adj: Iterable = None):\n\
    \        G.N = N\n        if E is not None:\n            G.M, G.E = len(E), E\n\
    \        if adj is not None:\n            super().__init__(adj)\n\n    def neighbors(G,\
    \ v: int) -> Iterable[int]:\n        return G[v]\n    \n    def edge_ids(G) ->\
    \ list[list[int]]: ...\n\n    @overload\n    def distance(G) -> list[list[int]]:\
    \ ...\n    @overload\n    def distance(G, s: int = 0) -> list[int]: ...\n    @overload\n\
    \    def distance(G, s: int, g: int) -> int: ...\n    def distance(G, s = None,\
    \ g = None):\n        match s, g:\n            case None, None:\n            \
    \    return G.floyd_warshall()\n            case s, None:\n                return\
    \ G.bfs(s)\n            case s, g:\n                return G.bfs(s, g)\n\n   \
    \ @overload\n    def bfs(G, s: int|list = 0) -> list[int]: ...\n    @overload\n\
    \    def bfs(G, s: int|list, g: int) -> int: ...\n    def bfs(G, s = 0, g = None):\n\
    \        D = [inf for _ in range(G.N)]\n        q = deque([s] if isinstance(s,\
    \ int) else s)\n        for u in q: D[u] = 0\n        while q:\n            nd\
    \ = D[u := q.popleft()]+1\n            if u == g: return D[u]\n            for\
    \ v in G.neighbors(u):\n                if nd < D[v]:\n                    D[v]\
    \ = nd\n                    q.append(v)\n        return D if g is None else inf\
    \    \n    \n    \n    def floyd_warshall(G) -> list[list[int]]:\n        D =\
    \ [[inf]*G.N for _ in range(G.N)]\n\n        for u in G:\n            D[u][u]\
    \ = 0\n            for v in G.neighbors(u):\n                D[u][v] = 1\n   \
    \     \n        for k, Dk in enumerate(D):\n            for Di in D:\n       \
    \         for j in range(G.N):\n                    Di[j] = min(Di[j], Di[k]+Dk[j])\n\
    \        return D\n    \n    \n    def find_cycle(G, s = 0, vis = None, par =\
    \ None):\n        N = G.N\n        vis = vis or [0] * N\n        par = par or\
    \ [-1] * N\n        if vis[s]: return None\n        vis[s] = 1\n        stack\
    \ = [(True, s)]\n        while stack:\n            forw, v = stack.pop()\n   \
    \         if forw:\n                stack.append((False, v))\n               \
    \ vis[v] = 1\n                for u in G.neighbors(v):\n                    if\
    \ vis[u] == 1 and u != par[v]:\n                        # Cycle detected\n   \
    \                     cyc = [u]\n                        vis[u] = 2\n        \
    \                while v != u:\n                            cyc.append(v)\n  \
    \                          vis[v] = 2\n                            v = par[v]\n\
    \                        return cyc\n                    elif vis[u] == 0:\n \
    \                       par[u] = v\n                        stack.append((True,\
    \ u))\n            else:\n                vis[v] = 2\n        return None\n  \
    \  \n    def bridges(G):\n        tin = [-1] * G.N\n        low = [-1] * G.N\n\
    \        par = [-1] * G.N\n        vis = [0] * G.N\n        in_edge = [-1] * G.N\n\
    \n        Eid = G.edge_ids()\n        time = 0\n        bridges = []\n       \
    \ stack = list(range(G.N))\n        while stack:\n            v = stack.pop()\n\
    \            p = par[v]\n            match vis[v]:\n                case 0:\n\
    \                    vis[v] = 1\n                    tin[v] = low[v] = time\n\
    \                    time += 1\n                    stack.append(v)\n        \
    \            for i, child in enumerate(G.neighbors(v)):\n                    \
    \    if child == p:\n                            continue\n                  \
    \      match vis[child]:\n                            case 0:\n              \
    \                  # Tree edge - recurse\n                                par[child]\
    \ = v\n                                in_edge[child] = Eid[v][i]\n          \
    \                      stack.append(child)\n                            case 1:\n\
    \                                # Back edge - update low-link value\n       \
    \                         low[v] = min(low[v], tin[child])\n                case\
    \ 1:\n                    vis[v] = 2\n                    if p != -1:\n      \
    \                  low[p] = min(low[p], low[v])\n                        if low[v]\
    \ > tin[p]:\n                            bridges.append(in_edge[v])\n        \
    \        \n        return bridges\n\n    def articulation_points(G):\n       \
    \ \"\"\"\n        Find articulation points in an undirected graph using DFS events.\n\
    \        Returns a boolean list that is True for indices where the vertex is an\
    \ articulation point.\n        \"\"\"\n        N = G.N\n        order = [-1] *\
    \ N\n        low = [-1] * N\n        par = [-1] * N\n        state = [0] * N\n\
    \        children = [0] * N\n        ap = [False] * N\n        time = 0\n    \
    \    stack = list(range(N))\n\n        while stack:\n            v = stack.pop()\n\
    \            p = par[v]\n            if state[v] == 0:\n                state[v]\
    \ = 1\n                order[v] = low[v] = time\n                time += 1\n \
    \           \n                stack.append(v)\n                for child in G[v]:\n\
    \                    if order[child] == -1:\n                        par[child]\
    \ = v\n                        stack.append(child)\n                    elif child\
    \ != p:\n                        low[v] = min(low[v], order[child])\n        \
    \        if p != -1:\n                    children[p] += 1\n            elif state[v]\
    \ == 1:\n                state[v] = 2\n                ap[v] |= p == -1 and children[v]\
    \ > 1\n                if p != -1:\n                    low[p] = min(low[p], low[v])\n\
    \                    ap[p] |= par[p] != -1 and low[v] >= order[p]\n\n        return\
    \ ap\n    \n    def dfs_events(G, flags: DFSFlags, s: int|list|None = None, max_depth:\
    \ int|None = None):\n        match flags:\n            case DFSFlags.INTERVAL:\n\
    \                if max_depth is None:\n                    return G.dfs_enter_leave(s)\n\
    \            case DFSFlags.DOWN|DFSFlags.TOPDOWN:\n                edges = G.dfs_topdown(s,\
    \ DFSFlags.CONNECT_ROOTS in flags)\n                return [(DFSEvent.DOWN, p,\
    \ u) for p,u in edges]\n            case DFSFlags.UP|DFSFlags.BOTTOMUP:\n    \
    \            edges = G.dfs_bottomup(s, DFSFlags.CONNECT_ROOTS in flags)\n    \
    \            return [(DFSEvent.UP, p, u) for p,u in edges]\n            case flags\
    \ if flags & DFSFlags.BACKTRACK:\n                return G.dfs_backtrack(s)\n\
    \        state = [0] * G.N\n        child = [0] * G.N\n        stack = [0] * G.N\n\
    \        if flags & DFSFlags.RETURN_PARENTS:\n            parents = [-1] * G.N\n\
    \        if flags & DFSFlags.RETURN_DEPTHS:\n            depths = [-1] * G.N\n\
    \n        events = []\n        for s in G.starts(s):\n            stack[depth\
    \ := 0] = s\n            if (DFSFlags.DOWN|DFSFlags.CONNECT_ROOTS) in flags:\n\
    \                events.append((DFSEvent.DOWN,-1,s))\n            while depth\
    \ != -1:\n                u = stack[depth]\n                \n               \
    \ if not state[u]:\n                    state[u] = 1\n                    if flags\
    \ & DFSFlags.ENTER:\n                        events.append((DFSEvent.ENTER, u))\n\
    \                    if flags & DFSFlags.RETURN_DEPTHS:\n                    \
    \    depths[u] = depth\n                \n                if (c := child[u]) <\
    \ len(G[u]):\n                    child[u] += 1\n                    match state[v\
    \ := G[u][c]]:\n                        case 0:  # Unvisited\n               \
    \             if max_depth is None or depth <= max_depth:\n                  \
    \              if flags & DFSFlags.DOWN:\n                                   \
    \ events.append((DFSEvent.DOWN, u, v))\n                                stack[depth\
    \ := depth+1] = v\n                                if flags & DFSFlags.RETURN_PARENTS:\n\
    \                                    parents[v] = u\n                        case\
    \ 1:  # In progress\n                            if flags & DFSFlags.BACK:\n \
    \                               events.append((DFSEvent.BACK, u, v))\n       \
    \                 case 2:  # Completed\n                            if flags &\
    \ DFSFlags.CROSS:\n                                events.append((DFSEvent.CROSS,\
    \ u, v))\n                else:\n                    depth -= 1\n            \
    \        state[u] = 0 if DFSFlags.BACKTRACK in flags else 2\n                \
    \    if flags & DFSFlags.LEAVE:\n                        events.append((DFSEvent.LEAVE,\
    \ u))\n                    if depth != -1 and flags & DFSFlags.UP:\n         \
    \               events.append((DFSEvent.UP, stack[depth], u))\n            if\
    \ (DFSFlags.UP|DFSFlags.CONNECT_ROOTS) in flags:\n                events.append((DFSEvent.UP,-1,s))\n\
    \        ret = tuple((events,)) if DFSFlags.RETURN_ALL & flags else events\n \
    \       if DFSFlags.RETURN_PARENTS in flags:\n            ret += (parents,)\n\
    \        if DFSFlags.RETURN_DEPTHS in flags:\n            ret += (depths,)\n \
    \       return ret\n\n    def dfs_backtrack(G, flags: DFSFlags, s: int|list =\
    \ None, max_depth: int|None = None):\n        stack_depth = (max_depth+1 if max_depth\
    \ is not None else G.N)\n        stack = [0]*stack_depth\n        child = [0]*stack_depth\n\
    \        state = [0]*G.N\n        events: list[tuple[DFSEvent, int]|tuple[DFSEvent,\
    \ int, int]] = []\n\n        for s in G.starts(s):\n            if state[s]: continue\n\
    \            state[s] = 1\n            stack[depth := 0] = s\n            if DFSFlags.DOWN|DFSFlags.CONNECT_ROOTS\
    \ in flags:\n                events.append((DFSEvent.DOWN,-1,s))\n           \
    \ while depth != -1:\n                u = stack[depth]\n                if state[u]\
    \ == 1:\n                    state[u] = 2\n                    if DFSFlags.ENTER\
    \ in flags:\n                        events.append((DFSEvent.ENTER,u))\n     \
    \               if max_depth is not None and depth >= max_depth:\n           \
    \             child[depth] = len(G[u])\n                        if DFSFlags.MAXDEPTH\
    \ in flags:\n                            events.append((DFSEvent.MAXDEPTH,u))\n\
    \n                if (c := child[depth]) < len(G[u]):\n                    child[depth]\
    \ += 1\n                    if state[v := G[u][c]]:\n                        if\
    \ DFSFlags.BACK in flags:\n                            events.append((DFSEvent.BACK,u,v))\n\
    \                        continue\n                    state[v] = 1\n        \
    \            if DFSFlags.DOWN in flags:\n                        events.append((DFSEvent.DOWN,u,v))\n\
    \                    stack[depth := depth+1] = v\n                else:\n    \
    \                state[u] = 0\n                    if DFSFlags.LEAVE in flags:\n\
    \                        events.append((DFSEvent.LEAVE,u))\n                 \
    \   child[depth] = 0\n                    depth -= 1\n                    if depth\
    \ and DFSFlags.UP in flags:\n                        events.append((DFSEvent.UP,\
    \ stack[depth], u))\n            if DFSFlags.UP|DFSFlags.CONNECT_ROOTS in flags:\n\
    \                events.append((DFSEvent.UP,-1,s))\n        return events\n  \
    \  \n    def dfs_enter_leave(G, s: int|list[int]|None = None):\n        stack:\
    \ list[int] = [0]*(G.N+1)\n        state = [0]*G.N\n        events: list[tuple[DFSEvent,\
    \ int]] = []\n\n        for s in G.starts(s):\n            if state[s]: continue\n\
    \            state[s] = True\n            stack[idx := 1] = s\n            while\
    \ idx:\n                u = stack[idx], idx\n                if state[u] == 1:\n\
    \                    events.append((DFSEvent.ENTER,u))\n                    for\
    \ v in G[u]:\n                        if state[v]: continue\n                \
    \        state[v] = 1\n                        stack[idx := idx+1] = v\n     \
    \           else:\n                    events.append((DFSEvent.LEAVE,u))\n   \
    \                 idx -= 1\n\n        return events\n    \n    def dfs_topdown(G,\
    \ s: int|list[int]|None = None, connect_roots = False):\n        '''Returns list\
    \ of (u,v) representing u->v edges in order of top down discovery'''\n       \
    \ stack: list[int] = elist(G.N)\n        vis = [False]*G.N\n        edges: list[tuple[int,int]]\
    \ = elist(G.N)\n\n        for s in G.starts(s):\n            if vis[s]: continue\n\
    \            if connect_roots:\n                edges.append((-1,s))\n       \
    \     vis[s] = True\n            stack.append(s)\n            while stack:\n \
    \               u = stack.pop()\n                for v in G[u]:\n            \
    \        if vis[v]: continue\n                    vis[v] = True\n            \
    \        edges.append((u,v))\n                    stack.append(v)\n        return\
    \ edges\n\n\n    # def dfs_topdown(G, s: int|list[int]|None = None, connect_roots\
    \ = False):\n    #     '''Returns list of (u,v) representing u->v edges in order\
    \ of top down discovery'''\n    #     stack = [0] * G.N\n    #     vis: list[bool]\
    \ = [False]*G.N\n    #     edges: list[tuple[int,int]] = []\n\n    #     for s\
    \ in G.starts(s):\n    #         if vis[s]: continue\n    #         if connect_roots:\n\
    \    #             edges.append((-1,s))\n    #         vis[s] = True\n    #  \
    \       stack[idx := 0] = s\n    #         while idx != -1:\n    #           \
    \  u, idx = stack[idx], idx-1\n    #             for v in G[u]:\n    #       \
    \          if vis[v]: continue\n    #                 vis[v] = True\n    #   \
    \              edges.append((u,v))\n    #                 stack[idx := idx+1]\
    \ = v \n\n    #     return edges\n    \n    def dfs_topdown_indexed(G, s: int|list[int]|None\
    \ = None, connect_roots = False):\n        '''Returns list of (u,v) representing\
    \ u->v edges in order of top down discovery'''\n        stack = [0] * G.N\n  \
    \      vis: list[bool] = [False]*G.N\n        edges: list[tuple[int,int,int]]\
    \ = []\n\n        for r,s in enumerate(G.starts(s)):\n            if vis[s]: continue\n\
    \            if connect_roots:\n                edges.append((r,-1,s))\n     \
    \       vis[s] = True\n            stack[idx := 0] = s\n            while idx\
    \ != -1:\n                u, idx = stack[idx], idx-1\n                for c,v\
    \ in enumerate(G[u]):\n                    if vis[v]: continue\n             \
    \       vis[v] = True\n                    edges.append((c,u,v))\n           \
    \         stack[idx := idx+1] = v \n\n        return edges\n    \n    def dfs_bottomup(G,\
    \ s: int|list[int]|None = None, connect_roots = False):\n        '''Returns list\
    \ of (p,u) representing p->u edges in bottom up order'''\n        edges = G.dfs_topdown(s,\
    \ connect_roots)\n        edges.reverse()\n        return edges\n    \n    def\
    \ starts(G, v: int|list[int]|None) -> Iterable:\n        match v:\n          \
    \  case int(v): return (v,)\n            case None: return range(G.N)\n      \
    \      case V: return V\n\n    @classmethod\n    def compile(cls, N: int, M: int,\
    \ E):\n        edge = Parser.compile(E)\n        def parse(ts: TokenStream):\n\
    \            return cls(N, [edge(ts) for _ in range(M)])\n        return parse\n\
    \    \n\nclass Graph(GraphProtocol):\n    def __init__(G, N: int, E: list[Edge]=[]):\n\
    \        super().__init__(N, E, ([] for _ in range(N)))\n        for u,v in G.E:\n\
    \            G[u].append(v)\n            G[v].append(u)\n\n    def edge_ids(G)\
    \ -> list[list[int]]:\n        Eid = [[] for _ in range(G.N)]\n        for e,(u,v)\
    \ in enumerate(G.E):\n            Eid[u].append(e)\n            Eid[v].append(e)\n\
    \        return Eid\n\n    @classmethod\n    def compile(cls, N: int, M: int,\
    \ E: type|int = Edge[-1]):\n        if isinstance(E, int): E = Edge[E]\n     \
    \   return super().compile(N, M, E)\n\nfrom typing import overload, Literal\n\
    from functools import cached_property\n\n\nfrom typing import Any, Callable, List\n\
    \nclass SparseTable:\n    def __init__(self, op: Callable[[Any, Any], Any], arr:\
    \ List[Any]):\n        self.n = len(arr)\n        self.log = self.n.bit_length()\n\
    \        self.op = op\n        self.st = [[None] * (self.n-(1<<i)+1) for i in\
    \ range(self.log)]\n        self.st[0] = arr[:]\n        \n        for i in range(self.log-1):\n\
    \            row, d = self.st[i], 1<<i\n            for j in range(len(self.st[i+1])):\n\
    \                self.st[i+1][j] = op(row[j], row[j+d])\n\n    def query(self,\
    \ l: int, r: int) -> Any:\n        k = (r-l).bit_length()-1\n        return self.op(self.st[k][l],\
    \ self.st[k][r-(1<<k)])\n    \n    def __repr__(self) -> str:\n        return\
    \ '\\n'.join(f'{i:<2d} {row}' for i,row in enumerate(self.st))\n\nclass BinaryIndexTree:\n\
    \    def __init__(self, v: int|list):\n        if isinstance(v, int):\n      \
    \      self.data, self.size = [0]*v, v\n        else:\n            self.build(v)\n\
    \n    def build(self, data):\n        self.data, self.size = data, len(data)\n\
    \        for i in range(self.size):\n            if (r := i|(i+1)) < self.size:\
    \ \n                self.data[r] += self.data[i]\n\n    def get(self, i: int):\n\
    \        assert 0 <= i < self.size\n        s = self.data[i]\n        z = i&(i+1)\n\
    \        for _ in range((i^z).bit_count()):\n            s, i = s-self.data[i-1],\
    \ i-(i&-i)\n        return s\n    \n    def set(self, i: int, x: int):\n     \
    \   self.add(i, x-self.get(i))\n        \n    def add(self, i: int, x: int) ->\
    \ None:\n        assert 0 <= i <= self.size\n        i += 1\n        data, size\
    \ = self.data, self.size\n        while i <= size:\n            data[i-1], i =\
    \ data[i-1] + x, i+(i&-i)\n\n    def pref_sum(self, i: int):\n        assert 0\
    \ <= i <= self.size\n        s = 0\n        data = self.data\n        for _ in\
    \ range(i.bit_count()):\n            s, i = s+data[i-1], i-(i&-i)\n        return\
    \ s\n    \n    def range_sum(self, l: int, r: int):\n        return self.pref_sum(r)\
    \ - self.pref_sum(l)\n\nclass LCATable(SparseTable):\n    def __init__(self, T,\
    \ root = 0):\n        self.start = [-1] * len(T)\n        self.end = [-1] * len(T)\n\
    \        self.euler = []\n        self.depth = []\n        \n        # Iterative\
    \ DFS\n        stack = [(root, -1, 0)]\n        while stack:\n            u, p,\
    \ d = stack.pop()\n            \n            if self.start[u] == -1:\n       \
    \         self.start[u] = len(self.euler)\n                \n                for\
    \ v in reversed(T[u]):\n                    if v != p:\n                     \
    \   stack.append((u, p, d))\n                        stack.append((v, u, d+1))\n\
    \                        \n            self.euler.append(u)\n            self.depth.append(d)\n\
    \            self.end[u] = len(self.euler)\n        super().__init__(min, list(zip(self.depth,\
    \ self.euler)))\n\n    def query(self, u, v) -> tuple[int,int]:\n        l, r\
    \ = min(self.start[u], self.start[v]), max(self.start[u], self.start[v])+1\n \
    \       d, a = super().query(l, r)\n        return a, d\n    \n    def distance(self,\
    \ u, v) -> int:\n        l, r = min(self.start[u], self.start[v]), max(self.start[u],\
    \ self.start[v])+1\n        d, _ = super().query(l, r)\n        return self.depth[l]\
    \ + self.depth[r] - 2*d\n        \n\nclass TreeProtocol(GraphProtocol):\n\n  \
    \  @cached_property\n    def lca(T):\n        return LCATable(T)\n    \n    @overload\n\
    \    def diameter(T) -> int: ...\n    @overload\n    def diameter(T, endpoints:\
    \ Literal[True]) -> tuple[int,int,int]: ...\n    def diameter(T, endpoints = False):\n\
    \        _, s = max((d,v) for v,d in enumerate(T.dfs(0)))\n        diam, g = max((d,v)\
    \ for v,d in enumerate(T.dfs(s)))\n        return (diam, s, g) if endpoints else\
    \ diam\n    \n    @overload\n    def distance(T) -> list[list[int]]: ...\n   \
    \ @overload\n    def distance(T, s: int = 0) -> list[int]: ...\n    @overload\n\
    \    def distance(T, s: int, g: int) -> int: ...\n    def distance(T, s = None,\
    \ g = None):\n        match s, g:\n            case None, None:\n            \
    \    return [T.dfs(u) for u in range(T.N)]\n            case s, g:\n         \
    \       return T.dfs(s, g)\n            \n    @overload\n    def dfs(T, s: int\
    \ = 0) -> list[int]: ...\n    @overload\n    def dfs(T, s: int, g: int) -> int:\
    \ ...\n    def dfs(T, s = 0, g = None):\n        D = [inf for _ in range(T.N)]\n\
    \        D[s] = 0\n        state = [True for _ in range(T.N)]\n        stack =\
    \ [s]\n\n        while stack:\n            u = stack.pop()\n            if u ==\
    \ g: return D[u]\n            state[u] = False\n            for v in T[u]:\n \
    \               if state[v]:\n                    D[v] = D[u]+1\n            \
    \        stack.append(v)\n        return D if g is None else inf \n\n\n    def\
    \ dfs_events(G, opts: DFSFlags, s: int = 0):         \n        events = []\n \
    \       # stack = deque([(s,-1)], maxlen=G.N)\n        stack = [(s,-1)]\n    \
    \    adj = [None]*G.N\n\n\n        while stack:\n            u, p = stack[-1]\n\
    \            \n            if adj[u] is None:\n                adj[u] = iter(G.neighbors(u))\n\
    \                if DFSFlags.ENTER in opts:\n                    events.append((DFSEvent.ENTER,\
    \ u))\n            \n            if (v := next(adj[u], None)) is not None:\n \
    \               if v == p:\n                    if DFSFlags.BACK in opts:\n  \
    \                      events.append((DFSEvent.BACK, u, v))\n                else:\n\
    \                    if DFSFlags.DOWN in opts:\n                        events.append((DFSEvent.DOWN,\
    \ u, v))\n                    stack.append((v,u))\n            else:\n       \
    \         stack.pop()\n\n                if DFSFlags.LEAVE in opts:\n        \
    \            events.append((DFSEvent.LEAVE, u))\n                if p != -1 and\
    \ DFSFlags.UP in opts:\n                    events.append((DFSEvent.UP, u, p))\n\
    \        return events\n\n\nclass Tree(Graph, TreeProtocol):\n\n    @classmethod\n\
    \    def compile(cls, N: int):\n\n        def parse(ts: TokenStream):\n      \
    \      T = cls.__new__(cls)\n            list.__init__(T, (elist(4) for _ in range(N)))\n\
    \            \n            V = ts.int_n(2*(N-1))\n            \n            for\
    \ i in range(N-1):\n                x, y = V[i<<1]-1, V[(i<<1)+1]-1\n        \
    \        T[x].append(y)\n                T[y].append(x)\n\n            T.N = N\n\
    \            T.M = N-1\n            return T\n\n        return parse\n    \ndef\
    \ read_ints(count, maxdigits=10):\n    \"\"\"\n    Read integers by collecting\
    \ and decoding all input first, then processing\n    \"\"\"\n    result = array('i',\
    \ [0]*count)\n    num_count = 0\n    \n    # First peek to find newline\n    peek\
    \ = sys.stdin.buffer.peek()\n    nl_pos = peek.find(b'\\n')\n    if nl_pos !=\
    \ -1:\n        # Read exactly up to and including newline\n        first_line\
    \ = sys.stdin.buffer.read(nl_pos + 1)\n        print(f\"First line was: {first_line}\"\
    , sys.stdin.line_buffering)\n    \n    # Get all remaining buffered content from\
    \ readline\n    buffered = []\n    while True:\n        line = sys.stdin.readline()\n\
    \        if not line:\n            break\n        buffered.append(line)  # readline\
    \ already returns str\n    \n    # Combine all into a single string for processing\n\
    \    all_input =  ''.join(buffered) + first_line.decode('utf-8')\n    \n    #\
    \ Now process all numbers from the combined string\n    current = 0\n    for c\
    \ in all_input:\n        if c >= '0' and c <= '9':\n            current = current\
    \ * 10 + (ord(c) - ord('0'))\n        elif c in (' ', '\\n'):\n            result[num_count]\
    \ = current\n            num_count += 1\n            current = 0\n           \
    \ if num_count >= count:\n                return result\n    \n    # If we still\
    \ need more numbers, continue with os.read\n    if num_count < count:\n      \
    \  buffer = bytearray()\n        pos = 0\n        \n        while num_count <\
    \ count:\n            if pos >= len(buffer):\n                chunk = os.read(0,\
    \ 8192)\n                if not chunk:\n                    if current > 0:\n\
    \                        result[num_count] = current\n                       \
    \ num_count += 1\n                    break\n                buffer.extend(chunk)\n\
    \                \n            b = buffer[pos]\n            pos += 1\n       \
    \     \n            if b >= 48:  # ASCII '0'\n                current = current\
    \ * 10 + (b - 48)\n            elif b in (32, 10):  # space or newline\n     \
    \           result[num_count] = current\n                num_count += 1\n    \
    \            current = 0\n                if num_count >= count:\n           \
    \         break\n    \n    return result[:num_count]\n\nfrom typing import Type,\
    \ TypeVar, overload\n\nT = TypeVar('T')\n@overload\ndef read(spec: int|None) ->\
    \ list[int]: ...\n@overload\ndef read(spec: Type[T]|T, char=False) -> T: ...\n\
    def read(spec: Type[T]|T=None, char=False):\n    match spec, char:\n        case\
    \ None, False:\n            return list(map(int, input().split()))\n        case\
    \ int(offset), False:\n            return [int(s)+offset for s in input().split()]\n\
    \        case _, _:\n            if char:\n                stream = CharStream()\n\
    \            else:\n                stream = TokenStream()\n            parser:\
    \ T = Parser.compile(spec)\n            return parser(stream)\n\nif __name__ ==\
    \ '__main__':\n    main()\n"
  code: "# verification-helper: PROBLEM https://atcoder.jp/contests/dp/tasks/dp_v\n\
    \n\ndef main():\n    N, M = read(tuple[int, ...])\n    T = read(Tree[N])\n\n\n\
    \n    def merge(a,b):\n        return a*b%M\n\n    def add_node(v,res):\n    \
    \    return (res+1)%M\n    \n    e = 1\n    dp = [[e]*len(T[v]) for v in range(N)]\n\
    \    ans = [e]*N\n    pid = [0]*N\n    \n    def suffix_list(A: list):\n     \
    \   N = len(A)\n        suf = A[:] + [e]\n        for i in range(N, 0, -1):\n\
    \            suf[i-1] = merge(suf[i-1], suf[i]) \n        return suf\n\n    order\
    \ = T.dfs_topdown(0, True)\n    # up\n    for p, u in reversed(order):\n     \
    \   up = dp[u]\n        for c,v in enumerate(T[u]):\n            if v == p:\n\
    \                pid[u] = c\n            else:\n                up[c] = add_node(u,\
    \ ans[v])\n                ans[u] = merge(ans[u], up[c])\n    # down        \n\
    \    for p, u in order:\n        up = dp[u]\n        suf, pre = suffix_list(up),\
    \ e\n        for i,v in enumerate(T[u]):\n            if v != p:\n           \
    \     dp[v][pid[v]] = add_node(v, merge(suf[i+1], pre))\n            pre = merge(pre,\
    \ up[i])\n        ans[u] = pre\n\n    # print(*ans, sep='\\n')\n    write_int(ans,\
    \ sep='\\n')\n\nfrom array import array\nfrom math import ceil, log10\nimport\
    \ os\n\ndef write_int(numbers, sep = ' '):\n    sep = ord(sep)\n    # Convert\
    \ to array for memory efficiency and faster processing\n    arr = array('i', numbers)\
    \ \n    extreme = max(1,abs(max(numbers)), abs(min(numbers)))\n    chars_per_num\
    \ = ceil(log10(extreme)) + 2\n    # Pre-calculate approximate buffer size (assume\
    \ ~10 chars per number plus spaces)\n    buffer = bytearray(len(arr) * chars_per_num)\n\
    \    \n    # Track position in buffer\n    pos = 0\n    \n    # Convert numbers\
    \ to bytes and add to buffer\n    for num in arr:\n        # Convert integer to\
    \ string bytes\n        s = str(num).encode('ascii')\n        # Copy bytes to\
    \ buffer\n        buffer[pos:pos + len(s)] = s\n        buffer[pos + len(s)] =\
    \ sep  # ASCII space\n        pos += len(s) + 1\n    \n    # Write completed buffer\
    \ to stdout\n    os.write(1, memoryview(buffer)[:pos-1])  # Exclude trailing space\n\
    \    os.write(1, b'\\n')  # Add final newline\n\n\n\n'''\n\u257A\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\n             https://kobejean.github.io/cp-library\
    \               \n'''\n\n\n\nimport sys\nimport typing\nfrom collections import\
    \ deque\nfrom numbers import Number\nfrom types import GenericAlias \nfrom typing\
    \ import Callable, Collection, Iterator, TypeAlias, TypeVar\n\n# class TokenStream(Iterator):\n\
    #     def __init__(self, stream = sys.stdin):\n#         self.stream = stream\n\
    #         self.queue = deque()\n\n#     def __next__(self):\n#         if not\
    \ self.queue: self.queue.extend(self.line())\n#         return self.queue.popleft()\n\
    \    \n#     def wait(self):\n#         if not self.queue: self.queue.extend(self.line())\n\
    #         while self.queue: yield\n        \n#     def line(self):\n#        \
    \ assert not self.queue\n#         return next(self.stream).rstrip().split()\n\
    \nfrom typing import Iterator, List\n\n\nclass TokenStream(Iterator):\n    stream\
    \ = sys.stdin.buffer\n    buffer = bytearray()\n    pos = 0\n    \n    def __init__(self,\
    \ chunk_size=8192):\n        self.queue = deque()\n        self.chunk_size = chunk_size\n\
    \        \n    def __next__(self) -> str:\n        if not self.queue:\n      \
    \      while True:\n                if TokenStream.pos >= len(self.buffer):\n\
    \                    if not self._read_chunk():\n                        raise\
    \ StopIteration\n                \n                while TokenStream.pos < len(self.buffer):\n\
    \                    start = TokenStream.pos\n                    while (TokenStream.pos\
    \ < len(self.buffer) and \n                           self.buffer[TokenStream.pos]\
    \ not in (32, 10)):  # b' \\n'\n                        TokenStream.pos += 1\n\
    \                    if start != TokenStream.pos:\n                        return\
    \ self.buffer[start:TokenStream.pos].decode()\n                    TokenStream.pos\
    \ += 1  # skip delimiter\n                    \n        return self.queue.popleft()\n\
    \    \n    def wait(self):\n        if not self.queue:\n            self.queue.extend(self.line())\n\
    \        while self.queue:\n            yield\n            \n    def line(self)\
    \ -> List[str]:\n        \"\"\"Reads exactly one line and returns its tokens\"\
    \"\"\n        assert not self.queue\n        line = bytearray()\n        \n  \
    \      while True:\n            if TokenStream.pos >= len(self.buffer):\n    \
    \            if not self._read_chunk():\n                    if not line:\n  \
    \                      raise StopIteration\n                    return line.decode().split()\n\
    \            \n            end = TokenStream.pos\n            while end < len(self.buffer)\
    \ and self.buffer[end] != 10:  # \\n\n                end += 1\n             \
    \   \n            if end < len(self.buffer):  # found newline\n              \
    \  line.extend(self.buffer[TokenStream.pos:end])\n                TokenStream.pos\
    \ = end + 1\n                return line.decode().split()\n            \n    \
    \        # no newline found, append entire remainder and read more\n         \
    \   line.extend(self.buffer[TokenStream.pos:])\n            TokenStream.pos =\
    \ len(self.buffer)\n    \n    def int_line(self) -> array:\n        \"\"\"Returns\
    \ the next line as an array of integers\"\"\"\n        result = array('i')\n \
    \       current = 0\n        \n        while True:\n            if TokenStream.pos\
    \ >= len(self.buffer):\n                if not self._read_chunk():\n         \
    \           if current > 0:\n                        result.append(current)\n\
    \                    return result\n            \n            b = self.buffer[TokenStream.pos]\n\
    \            TokenStream.pos += 1\n            \n            if b >= 48:  # ASCII\
    \ '0'\n                current = current * 10 + (b - 48)\n            elif b ==\
    \ 32:  # space\n                result.append(current)\n                current\
    \ = 0\n            elif b == 10:  # newline\n                if current > 0 or\
    \ not result:  # handle trailing number or empty line\n                    result.append(current)\n\
    \                return result\n\n    def int_n(self, n: int) -> array:\n    \
    \    \"\"\"Returns exactly n integers or raises StopIteration\"\"\"\n        result\
    \ = array('i', [0]) * n\n        num_count = 0\n        current = 0\n        \n\
    \        while num_count < n:\n            if TokenStream.pos >= len(self.buffer):\n\
    \                if not self._read_chunk():\n                    if current >\
    \ 0 and num_count < n:\n                        result[num_count] = current\n\
    \                        num_count += 1\n                    break\n         \
    \   \n            b = self.buffer[TokenStream.pos]\n            TokenStream.pos\
    \ += 1\n            \n            if b >= 48:  # ASCII '0'\n                current\
    \ = current * 10 + (b - 48)\n            elif b in (32, 10):  # space or newline\n\
    \                result[num_count] = current\n                num_count += 1\n\
    \                current = 0\n                if num_count >= n:\n           \
    \         break\n        \n        if num_count < n:\n            raise StopIteration\n\
    \        return result\n    \n    def _read_chunk(self) -> bool:\n        \"\"\
    \"Read a chunk of data into buffer, return True if data was read\"\"\"\n     \
    \   if TokenStream.pos > 0:\n            # Remove processed data\n           \
    \ del self.buffer[:TokenStream.pos]\n            TokenStream.pos = 0\n       \
    \     \n        chunk = TokenStream.stream.read(self.chunk_size)\n        if not\
    \ chunk:\n            return False\n        self.buffer.extend(chunk)\n      \
    \  return True\nsys.stdin._CHUNK_SIZE = 1 << 24\n# print(sys.stdin._CHUNK_SIZE)\n\
    # class TokenStream(Iterator):\n#     def __init__(self, stream = sys.stdin):\n\
    #         self.stream = stream\n#         self.queue = deque()\n\n#     def __next__(self):\n\
    #         if not self.queue: self.queue.extend(self.line())\n#         return\
    \ self.queue.popleft()\n    \n#     def wait(self):\n#         if not self.queue:\
    \ self.queue.extend(self.line())\n#         while self.queue: yield\n        \n\
    #     def line(self):\n#         assert not self.queue\n#         return next(self.stream).rstrip().split()\n\
    \nclass CharStream(TokenStream):\n    def line(self):\n        assert not self.queue\n\
    \        return next(self.stream).rstrip()\n        \nT = TypeVar('T')\nParseFn:\
    \ TypeAlias = Callable[[TokenStream],T]\nclass Parser:\n    def __init__(self,\
    \ spec: type[T]|T):\n        self.parse = Parser.compile(spec)\n\n    def __call__(self,\
    \ ts: TokenStream) -> T:\n        return self.parse(ts)\n    \n    @staticmethod\n\
    \    def compile_type(cls: type[T], args = ()) -> T:\n        if issubclass(cls,\
    \ Parsable):\n            return cls.compile(*args)\n        elif issubclass(cls,\
    \ (Number, str)):\n            def parse(ts: TokenStream):\n                return\
    \ cls(next(ts))              \n            return parse\n        elif issubclass(cls,\
    \ tuple):\n            return Parser.compile_tuple(cls, args)\n        elif issubclass(cls,\
    \ Collection):\n            return Parser.compile_collection(cls, args)\n    \
    \    elif callable(cls):\n            def parse(ts: TokenStream):\n          \
    \      return cls(next(ts))              \n            return parse\n        else:\n\
    \            raise NotImplementedError()\n    \n    @staticmethod\n    def compile(spec:\
    \ type[T]|T=int) -> ParseFn[T]:\n        if isinstance(spec, (type, GenericAlias)):\n\
    \            cls = typing.get_origin(spec) or spec\n            args = typing.get_args(spec)\
    \ or tuple()\n            return Parser.compile_type(cls, args)\n        elif\
    \ isinstance(offset := spec, Number): \n            cls = type(spec)  \n     \
    \       def parse(ts: TokenStream):\n                return cls(next(ts)) + offset\n\
    \            return parse\n        elif isinstance(args := spec, tuple):     \
    \ \n            return Parser.compile_tuple(type(spec), args)\n        elif isinstance(args\
    \ := spec, Collection):  \n            return Parser.compile_collection(type(spec),\
    \ args)\n        else:\n            raise NotImplementedError()\n    \n    @staticmethod\n\
    \    def compile_line(cls: T, spec=int) -> ParseFn[T]:\n        fn = Parser.compile(spec)\n\
    \        def parse(ts: TokenStream):\n            return cls(fn(ts) for _ in ts.wait())\n\
    \        return parse\n\n    @staticmethod\n    def compile_repeat(cls: T, spec,\
    \ N) -> ParseFn[T]:\n        fn = Parser.compile(spec)\n        def parse(ts:\
    \ TokenStream):\n            return cls(fn(ts) for _ in range(N))\n        return\
    \ parse\n\n    @staticmethod\n    def compile_children(cls: T, specs) -> ParseFn[T]:\n\
    \        fns = tuple(Parser.compile(spec) for spec in specs)\n        def parse(ts:\
    \ TokenStream):\n            return cls(fn(ts) for fn in fns)  \n        return\
    \ parse\n\n    @staticmethod\n    def compile_tuple(cls: type[T], specs) -> ParseFn[T]:\n\
    \        match specs:\n            case [spec, end] if end is ...:\n         \
    \       return Parser.compile_line(cls, spec)\n            case specs:   \n  \
    \              return Parser.compile_children(cls, specs)\n    \n    @staticmethod\n\
    \    def compile_collection(cls, specs):\n        match specs:\n            case\
    \ [ ] | [_] | set():\n                return Parser.compile_line(cls, *specs)\n\
    \            case [spec, int() as n]:\n                return Parser.compile_repeat(cls,\
    \ spec, n)\n            case _:\n                raise NotImplementedError()\n\
    \n        \nclass Parsable:\n    @classmethod\n    def compile(cls):\n       \
    \ def parser(ts: TokenStream):\n            return cls(next(ts))\n        return\
    \ parser\n\nclass Edge(tuple, Parsable):\n    @classmethod\n    def compile(cls,\
    \ I=-1):\n        def parse(ts: TokenStream):\n            u,v = ts.line()\n \
    \           return cls((int(u)+I,int(v)+I))\n        return parse\n\nfrom enum\
    \ import auto, IntFlag, IntEnum\n\nclass DFSFlags(IntFlag):\n    ENTER = auto()\n\
    \    DOWN = auto()\n    BACK = auto()\n    CROSS = auto()\n    LEAVE = auto()\n\
    \    UP = auto()\n    MAXDEPTH = auto()\n\n    RETURN_PARENTS = auto()\n    RETURN_DEPTHS\
    \ = auto()\n    BACKTRACK = auto()\n    CONNECT_ROOTS = auto()\n\n    # Common\
    \ combinations\n    ALL_EDGES = DOWN | BACK | CROSS\n    EULER_TOUR = DOWN | UP\n\
    \    INTERVAL = ENTER | LEAVE\n    TOPDOWN = DOWN | CONNECT_ROOTS\n    BOTTOMUP\
    \ = UP | CONNECT_ROOTS\n    RETURN_ALL = RETURN_PARENTS | RETURN_DEPTHS\n\nclass\
    \ DFSEvent(IntEnum):\n    ENTER = DFSFlags.ENTER \n    DOWN = DFSFlags.DOWN \n\
    \    BACK = DFSFlags.BACK \n    CROSS = DFSFlags.CROSS \n    LEAVE = DFSFlags.LEAVE\
    \ \n    UP = DFSFlags.UP \n    MAXDEPTH = DFSFlags.MAXDEPTH\n    \ntry:\n    from\
    \ __pypy__ import newlist_hint\nexcept:\n    def newlist_hint(hint):\n       \
    \ return []\n    \ndef elist(est_len: int) -> list:\n    return newlist_hint(est_len)\n\
    from typing import Iterable, overload\nfrom math import inf\n\nclass GraphProtocol(list,\
    \ Parsable):\n    def __init__(G, N: int, E: list = None, adj: Iterable = None):\n\
    \        G.N = N\n        if E is not None:\n            G.M, G.E = len(E), E\n\
    \        if adj is not None:\n            super().__init__(adj)\n\n    def neighbors(G,\
    \ v: int) -> Iterable[int]:\n        return G[v]\n    \n    def edge_ids(G) ->\
    \ list[list[int]]: ...\n\n    @overload\n    def distance(G) -> list[list[int]]:\
    \ ...\n    @overload\n    def distance(G, s: int = 0) -> list[int]: ...\n    @overload\n\
    \    def distance(G, s: int, g: int) -> int: ...\n    def distance(G, s = None,\
    \ g = None):\n        match s, g:\n            case None, None:\n            \
    \    return G.floyd_warshall()\n            case s, None:\n                return\
    \ G.bfs(s)\n            case s, g:\n                return G.bfs(s, g)\n\n   \
    \ @overload\n    def bfs(G, s: int|list = 0) -> list[int]: ...\n    @overload\n\
    \    def bfs(G, s: int|list, g: int) -> int: ...\n    def bfs(G, s = 0, g = None):\n\
    \        D = [inf for _ in range(G.N)]\n        q = deque([s] if isinstance(s,\
    \ int) else s)\n        for u in q: D[u] = 0\n        while q:\n            nd\
    \ = D[u := q.popleft()]+1\n            if u == g: return D[u]\n            for\
    \ v in G.neighbors(u):\n                if nd < D[v]:\n                    D[v]\
    \ = nd\n                    q.append(v)\n        return D if g is None else inf\
    \    \n    \n    \n    def floyd_warshall(G) -> list[list[int]]:\n        D =\
    \ [[inf]*G.N for _ in range(G.N)]\n\n        for u in G:\n            D[u][u]\
    \ = 0\n            for v in G.neighbors(u):\n                D[u][v] = 1\n   \
    \     \n        for k, Dk in enumerate(D):\n            for Di in D:\n       \
    \         for j in range(G.N):\n                    Di[j] = min(Di[j], Di[k]+Dk[j])\n\
    \        return D\n    \n    \n    def find_cycle(G, s = 0, vis = None, par =\
    \ None):\n        N = G.N\n        vis = vis or [0] * N\n        par = par or\
    \ [-1] * N\n        if vis[s]: return None\n        vis[s] = 1\n        stack\
    \ = [(True, s)]\n        while stack:\n            forw, v = stack.pop()\n   \
    \         if forw:\n                stack.append((False, v))\n               \
    \ vis[v] = 1\n                for u in G.neighbors(v):\n                    if\
    \ vis[u] == 1 and u != par[v]:\n                        # Cycle detected\n   \
    \                     cyc = [u]\n                        vis[u] = 2\n        \
    \                while v != u:\n                            cyc.append(v)\n  \
    \                          vis[v] = 2\n                            v = par[v]\n\
    \                        return cyc\n                    elif vis[u] == 0:\n \
    \                       par[u] = v\n                        stack.append((True,\
    \ u))\n            else:\n                vis[v] = 2\n        return None\n  \
    \  \n    def bridges(G):\n        tin = [-1] * G.N\n        low = [-1] * G.N\n\
    \        par = [-1] * G.N\n        vis = [0] * G.N\n        in_edge = [-1] * G.N\n\
    \n        Eid = G.edge_ids()\n        time = 0\n        bridges = []\n       \
    \ stack = list(range(G.N))\n        while stack:\n            v = stack.pop()\n\
    \            p = par[v]\n            match vis[v]:\n                case 0:\n\
    \                    vis[v] = 1\n                    tin[v] = low[v] = time\n\
    \                    time += 1\n                    stack.append(v)\n        \
    \            for i, child in enumerate(G.neighbors(v)):\n                    \
    \    if child == p:\n                            continue\n                  \
    \      match vis[child]:\n                            case 0:\n              \
    \                  # Tree edge - recurse\n                                par[child]\
    \ = v\n                                in_edge[child] = Eid[v][i]\n          \
    \                      stack.append(child)\n                            case 1:\n\
    \                                # Back edge - update low-link value\n       \
    \                         low[v] = min(low[v], tin[child])\n                case\
    \ 1:\n                    vis[v] = 2\n                    if p != -1:\n      \
    \                  low[p] = min(low[p], low[v])\n                        if low[v]\
    \ > tin[p]:\n                            bridges.append(in_edge[v])\n        \
    \        \n        return bridges\n\n    def articulation_points(G):\n       \
    \ \"\"\"\n        Find articulation points in an undirected graph using DFS events.\n\
    \        Returns a boolean list that is True for indices where the vertex is an\
    \ articulation point.\n        \"\"\"\n        N = G.N\n        order = [-1] *\
    \ N\n        low = [-1] * N\n        par = [-1] * N\n        state = [0] * N\n\
    \        children = [0] * N\n        ap = [False] * N\n        time = 0\n    \
    \    stack = list(range(N))\n\n        while stack:\n            v = stack.pop()\n\
    \            p = par[v]\n            if state[v] == 0:\n                state[v]\
    \ = 1\n                order[v] = low[v] = time\n                time += 1\n \
    \           \n                stack.append(v)\n                for child in G[v]:\n\
    \                    if order[child] == -1:\n                        par[child]\
    \ = v\n                        stack.append(child)\n                    elif child\
    \ != p:\n                        low[v] = min(low[v], order[child])\n        \
    \        if p != -1:\n                    children[p] += 1\n            elif state[v]\
    \ == 1:\n                state[v] = 2\n                ap[v] |= p == -1 and children[v]\
    \ > 1\n                if p != -1:\n                    low[p] = min(low[p], low[v])\n\
    \                    ap[p] |= par[p] != -1 and low[v] >= order[p]\n\n        return\
    \ ap\n    \n    def dfs_events(G, flags: DFSFlags, s: int|list|None = None, max_depth:\
    \ int|None = None):\n        match flags:\n            case DFSFlags.INTERVAL:\n\
    \                if max_depth is None:\n                    return G.dfs_enter_leave(s)\n\
    \            case DFSFlags.DOWN|DFSFlags.TOPDOWN:\n                edges = G.dfs_topdown(s,\
    \ DFSFlags.CONNECT_ROOTS in flags)\n                return [(DFSEvent.DOWN, p,\
    \ u) for p,u in edges]\n            case DFSFlags.UP|DFSFlags.BOTTOMUP:\n    \
    \            edges = G.dfs_bottomup(s, DFSFlags.CONNECT_ROOTS in flags)\n    \
    \            return [(DFSEvent.UP, p, u) for p,u in edges]\n            case flags\
    \ if flags & DFSFlags.BACKTRACK:\n                return G.dfs_backtrack(s)\n\
    \        state = [0] * G.N\n        child = [0] * G.N\n        stack = [0] * G.N\n\
    \        if flags & DFSFlags.RETURN_PARENTS:\n            parents = [-1] * G.N\n\
    \        if flags & DFSFlags.RETURN_DEPTHS:\n            depths = [-1] * G.N\n\
    \n        events = []\n        for s in G.starts(s):\n            stack[depth\
    \ := 0] = s\n            if (DFSFlags.DOWN|DFSFlags.CONNECT_ROOTS) in flags:\n\
    \                events.append((DFSEvent.DOWN,-1,s))\n            while depth\
    \ != -1:\n                u = stack[depth]\n                \n               \
    \ if not state[u]:\n                    state[u] = 1\n                    if flags\
    \ & DFSFlags.ENTER:\n                        events.append((DFSEvent.ENTER, u))\n\
    \                    if flags & DFSFlags.RETURN_DEPTHS:\n                    \
    \    depths[u] = depth\n                \n                if (c := child[u]) <\
    \ len(G[u]):\n                    child[u] += 1\n                    match state[v\
    \ := G[u][c]]:\n                        case 0:  # Unvisited\n               \
    \             if max_depth is None or depth <= max_depth:\n                  \
    \              if flags & DFSFlags.DOWN:\n                                   \
    \ events.append((DFSEvent.DOWN, u, v))\n                                stack[depth\
    \ := depth+1] = v\n                                if flags & DFSFlags.RETURN_PARENTS:\n\
    \                                    parents[v] = u\n                        case\
    \ 1:  # In progress\n                            if flags & DFSFlags.BACK:\n \
    \                               events.append((DFSEvent.BACK, u, v))\n       \
    \                 case 2:  # Completed\n                            if flags &\
    \ DFSFlags.CROSS:\n                                events.append((DFSEvent.CROSS,\
    \ u, v))\n                else:\n                    depth -= 1\n            \
    \        state[u] = 0 if DFSFlags.BACKTRACK in flags else 2\n                \
    \    if flags & DFSFlags.LEAVE:\n                        events.append((DFSEvent.LEAVE,\
    \ u))\n                    if depth != -1 and flags & DFSFlags.UP:\n         \
    \               events.append((DFSEvent.UP, stack[depth], u))\n            if\
    \ (DFSFlags.UP|DFSFlags.CONNECT_ROOTS) in flags:\n                events.append((DFSEvent.UP,-1,s))\n\
    \        ret = tuple((events,)) if DFSFlags.RETURN_ALL & flags else events\n \
    \       if DFSFlags.RETURN_PARENTS in flags:\n            ret += (parents,)\n\
    \        if DFSFlags.RETURN_DEPTHS in flags:\n            ret += (depths,)\n \
    \       return ret\n\n    def dfs_backtrack(G, flags: DFSFlags, s: int|list =\
    \ None, max_depth: int|None = None):\n        stack_depth = (max_depth+1 if max_depth\
    \ is not None else G.N)\n        stack = [0]*stack_depth\n        child = [0]*stack_depth\n\
    \        state = [0]*G.N\n        events: list[tuple[DFSEvent, int]|tuple[DFSEvent,\
    \ int, int]] = []\n\n        for s in G.starts(s):\n            if state[s]: continue\n\
    \            state[s] = 1\n            stack[depth := 0] = s\n            if DFSFlags.DOWN|DFSFlags.CONNECT_ROOTS\
    \ in flags:\n                events.append((DFSEvent.DOWN,-1,s))\n           \
    \ while depth != -1:\n                u = stack[depth]\n                if state[u]\
    \ == 1:\n                    state[u] = 2\n                    if DFSFlags.ENTER\
    \ in flags:\n                        events.append((DFSEvent.ENTER,u))\n     \
    \               if max_depth is not None and depth >= max_depth:\n           \
    \             child[depth] = len(G[u])\n                        if DFSFlags.MAXDEPTH\
    \ in flags:\n                            events.append((DFSEvent.MAXDEPTH,u))\n\
    \n                if (c := child[depth]) < len(G[u]):\n                    child[depth]\
    \ += 1\n                    if state[v := G[u][c]]:\n                        if\
    \ DFSFlags.BACK in flags:\n                            events.append((DFSEvent.BACK,u,v))\n\
    \                        continue\n                    state[v] = 1\n        \
    \            if DFSFlags.DOWN in flags:\n                        events.append((DFSEvent.DOWN,u,v))\n\
    \                    stack[depth := depth+1] = v\n                else:\n    \
    \                state[u] = 0\n                    if DFSFlags.LEAVE in flags:\n\
    \                        events.append((DFSEvent.LEAVE,u))\n                 \
    \   child[depth] = 0\n                    depth -= 1\n                    if depth\
    \ and DFSFlags.UP in flags:\n                        events.append((DFSEvent.UP,\
    \ stack[depth], u))\n            if DFSFlags.UP|DFSFlags.CONNECT_ROOTS in flags:\n\
    \                events.append((DFSEvent.UP,-1,s))\n        return events\n  \
    \  \n    def dfs_enter_leave(G, s: int|list[int]|None = None):\n        stack:\
    \ list[int] = [0]*(G.N+1)\n        state = [0]*G.N\n        events: list[tuple[DFSEvent,\
    \ int]] = []\n\n        for s in G.starts(s):\n            if state[s]: continue\n\
    \            state[s] = True\n            stack[idx := 1] = s\n            while\
    \ idx:\n                u = stack[idx], idx\n                if state[u] == 1:\n\
    \                    events.append((DFSEvent.ENTER,u))\n                    for\
    \ v in G[u]:\n                        if state[v]: continue\n                \
    \        state[v] = 1\n                        stack[idx := idx+1] = v\n     \
    \           else:\n                    events.append((DFSEvent.LEAVE,u))\n   \
    \                 idx -= 1\n\n        return events\n    \n    def dfs_topdown(G,\
    \ s: int|list[int]|None = None, connect_roots = False):\n        '''Returns list\
    \ of (u,v) representing u->v edges in order of top down discovery'''\n       \
    \ stack: list[int] = elist(G.N)\n        vis = [False]*G.N\n        edges: list[tuple[int,int]]\
    \ = elist(G.N)\n\n        for s in G.starts(s):\n            if vis[s]: continue\n\
    \            if connect_roots:\n                edges.append((-1,s))\n       \
    \     vis[s] = True\n            stack.append(s)\n            while stack:\n \
    \               u = stack.pop()\n                for v in G[u]:\n            \
    \        if vis[v]: continue\n                    vis[v] = True\n            \
    \        edges.append((u,v))\n                    stack.append(v)\n        return\
    \ edges\n\n\n    # def dfs_topdown(G, s: int|list[int]|None = None, connect_roots\
    \ = False):\n    #     '''Returns list of (u,v) representing u->v edges in order\
    \ of top down discovery'''\n    #     stack = [0] * G.N\n    #     vis: list[bool]\
    \ = [False]*G.N\n    #     edges: list[tuple[int,int]] = []\n\n    #     for s\
    \ in G.starts(s):\n    #         if vis[s]: continue\n    #         if connect_roots:\n\
    \    #             edges.append((-1,s))\n    #         vis[s] = True\n    #  \
    \       stack[idx := 0] = s\n    #         while idx != -1:\n    #           \
    \  u, idx = stack[idx], idx-1\n    #             for v in G[u]:\n    #       \
    \          if vis[v]: continue\n    #                 vis[v] = True\n    #   \
    \              edges.append((u,v))\n    #                 stack[idx := idx+1]\
    \ = v \n\n    #     return edges\n    \n    def dfs_topdown_indexed(G, s: int|list[int]|None\
    \ = None, connect_roots = False):\n        '''Returns list of (u,v) representing\
    \ u->v edges in order of top down discovery'''\n        stack = [0] * G.N\n  \
    \      vis: list[bool] = [False]*G.N\n        edges: list[tuple[int,int,int]]\
    \ = []\n\n        for r,s in enumerate(G.starts(s)):\n            if vis[s]: continue\n\
    \            if connect_roots:\n                edges.append((r,-1,s))\n     \
    \       vis[s] = True\n            stack[idx := 0] = s\n            while idx\
    \ != -1:\n                u, idx = stack[idx], idx-1\n                for c,v\
    \ in enumerate(G[u]):\n                    if vis[v]: continue\n             \
    \       vis[v] = True\n                    edges.append((c,u,v))\n           \
    \         stack[idx := idx+1] = v \n\n        return edges\n    \n    def dfs_bottomup(G,\
    \ s: int|list[int]|None = None, connect_roots = False):\n        '''Returns list\
    \ of (p,u) representing p->u edges in bottom up order'''\n        edges = G.dfs_topdown(s,\
    \ connect_roots)\n        edges.reverse()\n        return edges\n    \n    def\
    \ starts(G, v: int|list[int]|None) -> Iterable:\n        match v:\n          \
    \  case int(v): return (v,)\n            case None: return range(G.N)\n      \
    \      case V: return V\n\n    @classmethod\n    def compile(cls, N: int, M: int,\
    \ E):\n        edge = Parser.compile(E)\n        def parse(ts: TokenStream):\n\
    \            return cls(N, [edge(ts) for _ in range(M)])\n        return parse\n\
    \    \n\nclass Graph(GraphProtocol):\n    def __init__(G, N: int, E: list[Edge]=[]):\n\
    \        super().__init__(N, E, ([] for _ in range(N)))\n        for u,v in G.E:\n\
    \            G[u].append(v)\n            G[v].append(u)\n\n    def edge_ids(G)\
    \ -> list[list[int]]:\n        Eid = [[] for _ in range(G.N)]\n        for e,(u,v)\
    \ in enumerate(G.E):\n            Eid[u].append(e)\n            Eid[v].append(e)\n\
    \        return Eid\n\n    @classmethod\n    def compile(cls, N: int, M: int,\
    \ E: type|int = Edge[-1]):\n        if isinstance(E, int): E = Edge[E]\n     \
    \   return super().compile(N, M, E)\n\nfrom typing import overload, Literal\n\
    from functools import cached_property\n\n\nfrom typing import Any, Callable, List\n\
    \nclass SparseTable:\n    def __init__(self, op: Callable[[Any, Any], Any], arr:\
    \ List[Any]):\n        self.n = len(arr)\n        self.log = self.n.bit_length()\n\
    \        self.op = op\n        self.st = [[None] * (self.n-(1<<i)+1) for i in\
    \ range(self.log)]\n        self.st[0] = arr[:]\n        \n        for i in range(self.log-1):\n\
    \            row, d = self.st[i], 1<<i\n            for j in range(len(self.st[i+1])):\n\
    \                self.st[i+1][j] = op(row[j], row[j+d])\n\n    def query(self,\
    \ l: int, r: int) -> Any:\n        k = (r-l).bit_length()-1\n        return self.op(self.st[k][l],\
    \ self.st[k][r-(1<<k)])\n    \n    def __repr__(self) -> str:\n        return\
    \ '\\n'.join(f'{i:<2d} {row}' for i,row in enumerate(self.st))\n\nclass BinaryIndexTree:\n\
    \    def __init__(self, v: int|list):\n        if isinstance(v, int):\n      \
    \      self.data, self.size = [0]*v, v\n        else:\n            self.build(v)\n\
    \n    def build(self, data):\n        self.data, self.size = data, len(data)\n\
    \        for i in range(self.size):\n            if (r := i|(i+1)) < self.size:\
    \ \n                self.data[r] += self.data[i]\n\n    def get(self, i: int):\n\
    \        assert 0 <= i < self.size\n        s = self.data[i]\n        z = i&(i+1)\n\
    \        for _ in range((i^z).bit_count()):\n            s, i = s-self.data[i-1],\
    \ i-(i&-i)\n        return s\n    \n    def set(self, i: int, x: int):\n     \
    \   self.add(i, x-self.get(i))\n        \n    def add(self, i: int, x: int) ->\
    \ None:\n        assert 0 <= i <= self.size\n        i += 1\n        data, size\
    \ = self.data, self.size\n        while i <= size:\n            data[i-1], i =\
    \ data[i-1] + x, i+(i&-i)\n\n    def pref_sum(self, i: int):\n        assert 0\
    \ <= i <= self.size\n        s = 0\n        data = self.data\n        for _ in\
    \ range(i.bit_count()):\n            s, i = s+data[i-1], i-(i&-i)\n        return\
    \ s\n    \n    def range_sum(self, l: int, r: int):\n        return self.pref_sum(r)\
    \ - self.pref_sum(l)\n\nclass LCATable(SparseTable):\n    def __init__(self, T,\
    \ root = 0):\n        self.start = [-1] * len(T)\n        self.end = [-1] * len(T)\n\
    \        self.euler = []\n        self.depth = []\n        \n        # Iterative\
    \ DFS\n        stack = [(root, -1, 0)]\n        while stack:\n            u, p,\
    \ d = stack.pop()\n            \n            if self.start[u] == -1:\n       \
    \         self.start[u] = len(self.euler)\n                \n                for\
    \ v in reversed(T[u]):\n                    if v != p:\n                     \
    \   stack.append((u, p, d))\n                        stack.append((v, u, d+1))\n\
    \                        \n            self.euler.append(u)\n            self.depth.append(d)\n\
    \            self.end[u] = len(self.euler)\n        super().__init__(min, list(zip(self.depth,\
    \ self.euler)))\n\n    def query(self, u, v) -> tuple[int,int]:\n        l, r\
    \ = min(self.start[u], self.start[v]), max(self.start[u], self.start[v])+1\n \
    \       d, a = super().query(l, r)\n        return a, d\n    \n    def distance(self,\
    \ u, v) -> int:\n        l, r = min(self.start[u], self.start[v]), max(self.start[u],\
    \ self.start[v])+1\n        d, _ = super().query(l, r)\n        return self.depth[l]\
    \ + self.depth[r] - 2*d\n        \n\nclass TreeProtocol(GraphProtocol):\n\n  \
    \  @cached_property\n    def lca(T):\n        return LCATable(T)\n    \n    @overload\n\
    \    def diameter(T) -> int: ...\n    @overload\n    def diameter(T, endpoints:\
    \ Literal[True]) -> tuple[int,int,int]: ...\n    def diameter(T, endpoints = False):\n\
    \        _, s = max((d,v) for v,d in enumerate(T.dfs(0)))\n        diam, g = max((d,v)\
    \ for v,d in enumerate(T.dfs(s)))\n        return (diam, s, g) if endpoints else\
    \ diam\n    \n    @overload\n    def distance(T) -> list[list[int]]: ...\n   \
    \ @overload\n    def distance(T, s: int = 0) -> list[int]: ...\n    @overload\n\
    \    def distance(T, s: int, g: int) -> int: ...\n    def distance(T, s = None,\
    \ g = None):\n        match s, g:\n            case None, None:\n            \
    \    return [T.dfs(u) for u in range(T.N)]\n            case s, g:\n         \
    \       return T.dfs(s, g)\n            \n    @overload\n    def dfs(T, s: int\
    \ = 0) -> list[int]: ...\n    @overload\n    def dfs(T, s: int, g: int) -> int:\
    \ ...\n    def dfs(T, s = 0, g = None):\n        D = [inf for _ in range(T.N)]\n\
    \        D[s] = 0\n        state = [True for _ in range(T.N)]\n        stack =\
    \ [s]\n\n        while stack:\n            u = stack.pop()\n            if u ==\
    \ g: return D[u]\n            state[u] = False\n            for v in T[u]:\n \
    \               if state[v]:\n                    D[v] = D[u]+1\n            \
    \        stack.append(v)\n        return D if g is None else inf \n\n\n    def\
    \ dfs_events(G, opts: DFSFlags, s: int = 0):         \n        events = []\n \
    \       # stack = deque([(s,-1)], maxlen=G.N)\n        stack = [(s,-1)]\n    \
    \    adj = [None]*G.N\n\n\n        while stack:\n            u, p = stack[-1]\n\
    \            \n            if adj[u] is None:\n                adj[u] = iter(G.neighbors(u))\n\
    \                if DFSFlags.ENTER in opts:\n                    events.append((DFSEvent.ENTER,\
    \ u))\n            \n            if (v := next(adj[u], None)) is not None:\n \
    \               if v == p:\n                    if DFSFlags.BACK in opts:\n  \
    \                      events.append((DFSEvent.BACK, u, v))\n                else:\n\
    \                    if DFSFlags.DOWN in opts:\n                        events.append((DFSEvent.DOWN,\
    \ u, v))\n                    stack.append((v,u))\n            else:\n       \
    \         stack.pop()\n\n                if DFSFlags.LEAVE in opts:\n        \
    \            events.append((DFSEvent.LEAVE, u))\n                if p != -1 and\
    \ DFSFlags.UP in opts:\n                    events.append((DFSEvent.UP, u, p))\n\
    \        return events\n\n\nclass Tree(Graph, TreeProtocol):\n\n    @classmethod\n\
    \    def compile(cls, N: int):\n\n        def parse(ts: TokenStream):\n      \
    \      T = cls.__new__(cls)\n            list.__init__(T, (elist(4) for _ in range(N)))\n\
    \            \n            V = ts.int_n(2*(N-1))\n            \n            for\
    \ i in range(N-1):\n                x, y = V[i<<1]-1, V[(i<<1)+1]-1\n        \
    \        T[x].append(y)\n                T[y].append(x)\n\n            T.N = N\n\
    \            T.M = N-1\n            return T\n\n        return parse\n    \ndef\
    \ read_ints(count, maxdigits=10):\n    \"\"\"\n    Read integers by collecting\
    \ and decoding all input first, then processing\n    \"\"\"\n    result = array('i',\
    \ [0]*count)\n    num_count = 0\n    \n    # First peek to find newline\n    peek\
    \ = sys.stdin.buffer.peek()\n    nl_pos = peek.find(b'\\n')\n    if nl_pos !=\
    \ -1:\n        # Read exactly up to and including newline\n        first_line\
    \ = sys.stdin.buffer.read(nl_pos + 1)\n        print(f\"First line was: {first_line}\"\
    , sys.stdin.line_buffering)\n    \n    # Get all remaining buffered content from\
    \ readline\n    buffered = []\n    while True:\n        line = sys.stdin.readline()\n\
    \        if not line:\n            break\n        buffered.append(line)  # readline\
    \ already returns str\n    \n    # Combine all into a single string for processing\n\
    \    all_input =  ''.join(buffered) + first_line.decode('utf-8')\n    \n    #\
    \ Now process all numbers from the combined string\n    current = 0\n    for c\
    \ in all_input:\n        if c >= '0' and c <= '9':\n            current = current\
    \ * 10 + (ord(c) - ord('0'))\n        elif c in (' ', '\\n'):\n            result[num_count]\
    \ = current\n            num_count += 1\n            current = 0\n           \
    \ if num_count >= count:\n                return result\n    \n    # If we still\
    \ need more numbers, continue with os.read\n    if num_count < count:\n      \
    \  buffer = bytearray()\n        pos = 0\n        \n        while num_count <\
    \ count:\n            if pos >= len(buffer):\n                chunk = os.read(0,\
    \ 8192)\n                if not chunk:\n                    if current > 0:\n\
    \                        result[num_count] = current\n                       \
    \ num_count += 1\n                    break\n                buffer.extend(chunk)\n\
    \                \n            b = buffer[pos]\n            pos += 1\n       \
    \     \n            if b >= 48:  # ASCII '0'\n                current = current\
    \ * 10 + (b - 48)\n            elif b in (32, 10):  # space or newline\n     \
    \           result[num_count] = current\n                num_count += 1\n    \
    \            current = 0\n                if num_count >= count:\n           \
    \         break\n    \n    return result[:num_count]\n\nfrom typing import Type,\
    \ TypeVar, overload\n\nT = TypeVar('T')\n@overload\ndef read(spec: int|None) ->\
    \ list[int]: ...\n@overload\ndef read(spec: Type[T]|T, char=False) -> T: ...\n\
    def read(spec: Type[T]|T=None, char=False):\n    match spec, char:\n        case\
    \ None, False:\n            return list(map(int, input().split()))\n        case\
    \ int(offset), False:\n            return [int(s)+offset for s in input().split()]\n\
    \        case _, _:\n            if char:\n                stream = CharStream()\n\
    \            else:\n                stream = TokenStream()\n            parser:\
    \ T = Parser.compile(spec)\n            return parser(stream)\n\nif __name__ ==\
    \ '__main__':\n    main()\n"
  dependsOn: []
  isVerificationFile: false
  path: bundled.py
  requiredBy: []
  timestamp: '2024-11-16 03:24:02+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: bundled.py
layout: document
redirect_from:
- /library/bundled.py
- /library/bundled.py.html
title: bundled.py
---
