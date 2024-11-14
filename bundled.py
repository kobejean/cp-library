# verification-helper: PROBLEM https://atcoder.jp/contests/dp/tasks/dp_v


def main():
    N, M = read(tuple[int, ...])
    T = read(Tree[N])



    def merge(a,b):
        return a*b%M

    def add_node(v,res):
        return (res+1)%M
    
    e = 1
    dp = [[e]*len(T[v]) for v in range(N)]
    ans = [e]*N
    pid = [0]*N
    
    def suffix_list(A: list):
        N = len(A)
        suf = A[:] + [e]
        for i in range(N, 0, -1):
            suf[i-1] = merge(suf[i-1], suf[i]) 
        return suf

    order = T.dfs_topdown(0, True)
    # up
    for p, u in reversed(order):
        up = dp[u]
        for c,v in enumerate(T[u]):
            if v == p:
                pid[u] = c
            else:
                up[c] = add_node(u, ans[v])
                ans[u] = merge(ans[u], up[c])
    # down        
    for p, u in order:
        up = dp[u]
        suf, pre = suffix_list(up), e
        for i,v in enumerate(T[u]):
            if v != p:
                dp[v][pid[v]] = add_node(v, merge(suf[i+1], pre))
            pre = merge(pre, up[i])
        ans[u] = pre

    # print(*ans, sep='\n')
    write_int(ans, sep='\n')

from array import array
from math import ceil, log10
import os

def write_int(numbers, sep = ' '):
    sep = ord(sep)
    # Convert to array for memory efficiency and faster processing
    arr = array('i', numbers) 
    extreme = max(1,abs(max(numbers)), abs(min(numbers)))
    chars_per_num = ceil(log10(extreme)) + 2
    # Pre-calculate approximate buffer size (assume ~10 chars per number plus spaces)
    buffer = bytearray(len(arr) * chars_per_num)
    
    # Track position in buffer
    pos = 0
    
    # Convert numbers to bytes and add to buffer
    for num in arr:
        # Convert integer to string bytes
        s = str(num).encode('ascii')
        # Copy bytes to buffer
        buffer[pos:pos + len(s)] = s
        buffer[pos + len(s)] = sep  # ASCII space
        pos += len(s) + 1
    
    # Write completed buffer to stdout
    os.write(1, memoryview(buffer)[:pos-1])  # Exclude trailing space
    os.write(1, b'\n')  # Add final newline



'''
╺━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╸
             https://kobejean.github.io/cp-library               
'''



import sys
import typing
from collections import deque
from numbers import Number
from types import GenericAlias 
from typing import Callable, Collection, Iterator, TypeAlias, TypeVar

# class TokenStream(Iterator):
#     def __init__(self, stream = sys.stdin):
#         self.stream = stream
#         self.queue = deque()

#     def __next__(self):
#         if not self.queue: self.queue.extend(self.line())
#         return self.queue.popleft()
    
#     def wait(self):
#         if not self.queue: self.queue.extend(self.line())
#         while self.queue: yield
        
#     def line(self):
#         assert not self.queue
#         return next(self.stream).rstrip().split()

from typing import Iterator, List


class TokenStream(Iterator):
    stream = sys.stdin.buffer
    buffer = bytearray()
    pos = 0
    
    def __init__(self, chunk_size=8192):
        self.queue = deque()
        self.chunk_size = chunk_size
        
    def __next__(self) -> str:
        if not self.queue:
            while True:
                if TokenStream.pos >= len(self.buffer):
                    if not self._read_chunk():
                        raise StopIteration
                
                while TokenStream.pos < len(self.buffer):
                    start = TokenStream.pos
                    while (TokenStream.pos < len(self.buffer) and 
                           self.buffer[TokenStream.pos] not in (32, 10)):  # b' \n'
                        TokenStream.pos += 1
                    if start != TokenStream.pos:
                        return self.buffer[start:TokenStream.pos].decode()
                    TokenStream.pos += 1  # skip delimiter
                    
        return self.queue.popleft()
    
    def wait(self):
        if not self.queue:
            self.queue.extend(self.line())
        while self.queue:
            yield
            
    def line(self) -> List[str]:
        """Reads exactly one line and returns its tokens"""
        assert not self.queue
        line = bytearray()
        
        while True:
            if TokenStream.pos >= len(self.buffer):
                if not self._read_chunk():
                    if not line:
                        raise StopIteration
                    return line.decode().split()
            
            end = TokenStream.pos
            while end < len(self.buffer) and self.buffer[end] != 10:  # \n
                end += 1
                
            if end < len(self.buffer):  # found newline
                line.extend(self.buffer[TokenStream.pos:end])
                TokenStream.pos = end + 1
                return line.decode().split()
            
            # no newline found, append entire remainder and read more
            line.extend(self.buffer[TokenStream.pos:])
            TokenStream.pos = len(self.buffer)
    
    def int_line(self) -> array:
        """Returns the next line as an array of integers"""
        result = array('i')
        current = 0
        
        while True:
            if TokenStream.pos >= len(self.buffer):
                if not self._read_chunk():
                    if current > 0:
                        result.append(current)
                    return result
            
            b = self.buffer[TokenStream.pos]
            TokenStream.pos += 1
            
            if b >= 48:  # ASCII '0'
                current = current * 10 + (b - 48)
            elif b == 32:  # space
                result.append(current)
                current = 0
            elif b == 10:  # newline
                if current > 0 or not result:  # handle trailing number or empty line
                    result.append(current)
                return result

    def int_n(self, n: int) -> array:
        """Returns exactly n integers or raises StopIteration"""
        result = array('i', [0]) * n
        num_count = 0
        current = 0
        
        while num_count < n:
            if TokenStream.pos >= len(self.buffer):
                if not self._read_chunk():
                    if current > 0 and num_count < n:
                        result[num_count] = current
                        num_count += 1
                    break
            
            b = self.buffer[TokenStream.pos]
            TokenStream.pos += 1
            
            if b >= 48:  # ASCII '0'
                current = current * 10 + (b - 48)
            elif b in (32, 10):  # space or newline
                result[num_count] = current
                num_count += 1
                current = 0
                if num_count >= n:
                    break
        
        if num_count < n:
            raise StopIteration
        return result
    
    def _read_chunk(self) -> bool:
        """Read a chunk of data into buffer, return True if data was read"""
        if TokenStream.pos > 0:
            # Remove processed data
            del self.buffer[:TokenStream.pos]
            TokenStream.pos = 0
            
        chunk = TokenStream.stream.read(self.chunk_size)
        if not chunk:
            return False
        self.buffer.extend(chunk)
        return True
sys.stdin._CHUNK_SIZE = 1 << 24
# print(sys.stdin._CHUNK_SIZE)
# class TokenStream(Iterator):
#     def __init__(self, stream = sys.stdin):
#         self.stream = stream
#         self.queue = deque()

#     def __next__(self):
#         if not self.queue: self.queue.extend(self.line())
#         return self.queue.popleft()
    
#     def wait(self):
#         if not self.queue: self.queue.extend(self.line())
#         while self.queue: yield
        
#     def line(self):
#         assert not self.queue
#         return next(self.stream).rstrip().split()

class CharStream(TokenStream):
    def line(self):
        assert not self.queue
        return next(self.stream).rstrip()
        
T = TypeVar('T')
ParseFn: TypeAlias = Callable[[TokenStream],T]
class Parser:
    def __init__(self, spec: type[T]|T):
        self.parse = Parser.compile(spec)

    def __call__(self, ts: TokenStream) -> T:
        return self.parse(ts)
    
    @staticmethod
    def compile_type(cls: type[T], args = ()) -> T:
        if issubclass(cls, Parsable):
            return cls.compile(*args)
        elif issubclass(cls, (Number, str)):
            def parse(ts: TokenStream):
                return cls(next(ts))              
            return parse
        elif issubclass(cls, tuple):
            return Parser.compile_tuple(cls, args)
        elif issubclass(cls, Collection):
            return Parser.compile_collection(cls, args)
        elif callable(cls):
            def parse(ts: TokenStream):
                return cls(next(ts))              
            return parse
        else:
            raise NotImplementedError()
    
    @staticmethod
    def compile(spec: type[T]|T=int) -> ParseFn[T]:
        if isinstance(spec, (type, GenericAlias)):
            cls = typing.get_origin(spec) or spec
            args = typing.get_args(spec) or tuple()
            return Parser.compile_type(cls, args)
        elif isinstance(offset := spec, Number): 
            cls = type(spec)  
            def parse(ts: TokenStream):
                return cls(next(ts)) + offset
            return parse
        elif isinstance(args := spec, tuple):      
            return Parser.compile_tuple(type(spec), args)
        elif isinstance(args := spec, Collection):  
            return Parser.compile_collection(type(spec), args)
        else:
            raise NotImplementedError()
    
    @staticmethod
    def compile_line(cls: T, spec=int) -> ParseFn[T]:
        fn = Parser.compile(spec)
        def parse(ts: TokenStream):
            return cls(fn(ts) for _ in ts.wait())
        return parse

    @staticmethod
    def compile_repeat(cls: T, spec, N) -> ParseFn[T]:
        fn = Parser.compile(spec)
        def parse(ts: TokenStream):
            return cls(fn(ts) for _ in range(N))
        return parse

    @staticmethod
    def compile_children(cls: T, specs) -> ParseFn[T]:
        fns = tuple(Parser.compile(spec) for spec in specs)
        def parse(ts: TokenStream):
            return cls(fn(ts) for fn in fns)  
        return parse

    @staticmethod
    def compile_tuple(cls: type[T], specs) -> ParseFn[T]:
        match specs:
            case [spec, end] if end is ...:
                return Parser.compile_line(cls, spec)
            case specs:   
                return Parser.compile_children(cls, specs)
    
    @staticmethod
    def compile_collection(cls, specs):
        match specs:
            case [ ] | [_] | set():
                return Parser.compile_line(cls, *specs)
            case [spec, int() as n]:
                return Parser.compile_repeat(cls, spec, n)
            case _:
                raise NotImplementedError()

        
class Parsable:
    @classmethod
    def compile(cls):
        def parser(ts: TokenStream):
            return cls(next(ts))
        return parser

class Edge(tuple, Parsable):
    @classmethod
    def compile(cls, I=-1):
        def parse(ts: TokenStream):
            u,v = ts.line()
            return cls((int(u)+I,int(v)+I))
        return parse

from enum import auto, IntFlag, IntEnum

class DFSFlags(IntFlag):
    ENTER = auto()
    DOWN = auto()
    BACK = auto()
    CROSS = auto()
    LEAVE = auto()
    UP = auto()
    MAXDEPTH = auto()

    RETURN_PARENTS = auto()
    RETURN_DEPTHS = auto()
    BACKTRACK = auto()
    CONNECT_ROOTS = auto()

    # Common combinations
    ALL_EDGES = DOWN | BACK | CROSS
    EULER_TOUR = DOWN | UP
    INTERVAL = ENTER | LEAVE
    TOPDOWN = DOWN | CONNECT_ROOTS
    BOTTOMUP = UP | CONNECT_ROOTS
    RETURN_ALL = RETURN_PARENTS | RETURN_DEPTHS

class DFSEvent(IntEnum):
    ENTER = DFSFlags.ENTER 
    DOWN = DFSFlags.DOWN 
    BACK = DFSFlags.BACK 
    CROSS = DFSFlags.CROSS 
    LEAVE = DFSFlags.LEAVE 
    UP = DFSFlags.UP 
    MAXDEPTH = DFSFlags.MAXDEPTH
    
try:
    from __pypy__ import newlist_hint
except:
    def newlist_hint(hint):
        return []
    
def elist(est_len: int) -> list:
    return newlist_hint(est_len)
from typing import Iterable, overload
from math import inf

class GraphProtocol(list, Parsable):
    def __init__(G, N: int, E: list = None, adj: Iterable = None):
        G.N = N
        if E is not None:
            G.M, G.E = len(E), E
        if adj is not None:
            super().__init__(adj)

    def neighbors(G, v: int) -> Iterable[int]:
        return G[v]
    
    def edge_ids(G) -> list[list[int]]: ...

    @overload
    def distance(G) -> list[list[int]]: ...
    @overload
    def distance(G, s: int = 0) -> list[int]: ...
    @overload
    def distance(G, s: int, g: int) -> int: ...
    def distance(G, s = None, g = None):
        match s, g:
            case None, None:
                return G.floyd_warshall()
            case s, None:
                return G.bfs(s)
            case s, g:
                return G.bfs(s, g)

    @overload
    def bfs(G, s: int|list = 0) -> list[int]: ...
    @overload
    def bfs(G, s: int|list, g: int) -> int: ...
    def bfs(G, s = 0, g = None):
        D = [inf for _ in range(G.N)]
        q = deque([s] if isinstance(s, int) else s)
        for u in q: D[u] = 0
        while q:
            nd = D[u := q.popleft()]+1
            if u == g: return D[u]
            for v in G.neighbors(u):
                if nd < D[v]:
                    D[v] = nd
                    q.append(v)
        return D if g is None else inf    
    
    
    def floyd_warshall(G) -> list[list[int]]:
        D = [[inf]*G.N for _ in range(G.N)]

        for u in G:
            D[u][u] = 0
            for v in G.neighbors(u):
                D[u][v] = 1
        
        for k, Dk in enumerate(D):
            for Di in D:
                for j in range(G.N):
                    Di[j] = min(Di[j], Di[k]+Dk[j])
        return D
    
    
    def find_cycle(G, s = 0, vis = None, par = None):
        N = G.N
        vis = vis or [0] * N
        par = par or [-1] * N
        if vis[s]: return None
        vis[s] = 1
        stack = [(True, s)]
        while stack:
            forw, v = stack.pop()
            if forw:
                stack.append((False, v))
                vis[v] = 1
                for u in G.neighbors(v):
                    if vis[u] == 1 and u != par[v]:
                        # Cycle detected
                        cyc = [u]
                        vis[u] = 2
                        while v != u:
                            cyc.append(v)
                            vis[v] = 2
                            v = par[v]
                        return cyc
                    elif vis[u] == 0:
                        par[u] = v
                        stack.append((True, u))
            else:
                vis[v] = 2
        return None
    
    def bridges(G):
        tin = [-1] * G.N
        low = [-1] * G.N
        par = [-1] * G.N
        vis = [0] * G.N
        in_edge = [-1] * G.N

        Eid = G.edge_ids()
        time = 0
        bridges = []
        stack = list(range(G.N))
        while stack:
            v = stack.pop()
            p = par[v]
            match vis[v]:
                case 0:
                    vis[v] = 1
                    tin[v] = low[v] = time
                    time += 1
                    stack.append(v)
                    for i, child in enumerate(G.neighbors(v)):
                        if child == p:
                            continue
                        match vis[child]:
                            case 0:
                                # Tree edge - recurse
                                par[child] = v
                                in_edge[child] = Eid[v][i]
                                stack.append(child)
                            case 1:
                                # Back edge - update low-link value
                                low[v] = min(low[v], tin[child])
                case 1:
                    vis[v] = 2
                    if p != -1:
                        low[p] = min(low[p], low[v])
                        if low[v] > tin[p]:
                            bridges.append(in_edge[v])
                
        return bridges

    def articulation_points(G):
        """
        Find articulation points in an undirected graph using DFS events.
        Returns a boolean list that is True for indices where the vertex is an articulation point.
        """
        N = G.N
        order = [-1] * N
        low = [-1] * N
        par = [-1] * N
        state = [0] * N
        children = [0] * N
        ap = [False] * N
        time = 0
        stack = list(range(N))

        while stack:
            v = stack.pop()
            p = par[v]
            if state[v] == 0:
                state[v] = 1
                order[v] = low[v] = time
                time += 1
            
                stack.append(v)
                for child in G[v]:
                    if order[child] == -1:
                        par[child] = v
                        stack.append(child)
                    elif child != p:
                        low[v] = min(low[v], order[child])
                if p != -1:
                    children[p] += 1
            elif state[v] == 1:
                state[v] = 2
                ap[v] |= p == -1 and children[v] > 1
                if p != -1:
                    low[p] = min(low[p], low[v])
                    ap[p] |= par[p] != -1 and low[v] >= order[p]

        return ap
    
    def dfs_events(G, flags: DFSFlags, s: int|list|None = None, max_depth: int|None = None):
        match flags:
            case DFSFlags.INTERVAL:
                if max_depth is None:
                    return G.dfs_enter_leave(s)
            case DFSFlags.DOWN|DFSFlags.TOPDOWN:
                edges = G.dfs_topdown(s, DFSFlags.CONNECT_ROOTS in flags)
                return [(DFSEvent.DOWN, p, u) for p,u in edges]
            case DFSFlags.UP|DFSFlags.BOTTOMUP:
                edges = G.dfs_bottomup(s, DFSFlags.CONNECT_ROOTS in flags)
                return [(DFSEvent.UP, p, u) for p,u in edges]
            case flags if flags & DFSFlags.BACKTRACK:
                return G.dfs_backtrack(s)
        state = [0] * G.N
        child = [0] * G.N
        stack = [0] * G.N
        if flags & DFSFlags.RETURN_PARENTS:
            parents = [-1] * G.N
        if flags & DFSFlags.RETURN_DEPTHS:
            depths = [-1] * G.N

        events = []
        for s in G.starts(s):
            stack[depth := 0] = s
            if (DFSFlags.DOWN|DFSFlags.CONNECT_ROOTS) in flags:
                events.append((DFSEvent.DOWN,-1,s))
            while depth != -1:
                u = stack[depth]
                
                if not state[u]:
                    state[u] = 1
                    if flags & DFSFlags.ENTER:
                        events.append((DFSEvent.ENTER, u))
                    if flags & DFSFlags.RETURN_DEPTHS:
                        depths[u] = depth
                
                if (c := child[u]) < len(G[u]):
                    child[u] += 1
                    match state[v := G[u][c]]:
                        case 0:  # Unvisited
                            if max_depth is None or depth <= max_depth:
                                if flags & DFSFlags.DOWN:
                                    events.append((DFSEvent.DOWN, u, v))
                                stack[depth := depth+1] = v
                                if flags & DFSFlags.RETURN_PARENTS:
                                    parents[v] = u
                        case 1:  # In progress
                            if flags & DFSFlags.BACK:
                                events.append((DFSEvent.BACK, u, v))
                        case 2:  # Completed
                            if flags & DFSFlags.CROSS:
                                events.append((DFSEvent.CROSS, u, v))
                else:
                    depth -= 1
                    state[u] = 0 if DFSFlags.BACKTRACK in flags else 2
                    if flags & DFSFlags.LEAVE:
                        events.append((DFSEvent.LEAVE, u))
                    if depth != -1 and flags & DFSFlags.UP:
                        events.append((DFSEvent.UP, stack[depth], u))
            if (DFSFlags.UP|DFSFlags.CONNECT_ROOTS) in flags:
                events.append((DFSEvent.UP,-1,s))
        ret = tuple((events,)) if DFSFlags.RETURN_ALL & flags else events
        if DFSFlags.RETURN_PARENTS in flags:
            ret += (parents,)
        if DFSFlags.RETURN_DEPTHS in flags:
            ret += (depths,)
        return ret

    def dfs_backtrack(G, flags: DFSFlags, s: int|list = None, max_depth: int|None = None):
        stack_depth = (max_depth+1 if max_depth is not None else G.N)
        stack = [0]*stack_depth
        child = [0]*stack_depth
        state = [0]*G.N
        events: list[tuple[DFSEvent, int]|tuple[DFSEvent, int, int]] = []

        for s in G.starts(s):
            if state[s]: continue
            state[s] = 1
            stack[depth := 0] = s
            if DFSFlags.DOWN|DFSFlags.CONNECT_ROOTS in flags:
                events.append((DFSEvent.DOWN,-1,s))
            while depth != -1:
                u = stack[depth]
                if state[u] == 1:
                    state[u] = 2
                    if DFSFlags.ENTER in flags:
                        events.append((DFSEvent.ENTER,u))
                    if max_depth is not None and depth >= max_depth:
                        child[depth] = len(G[u])
                        if DFSFlags.MAXDEPTH in flags:
                            events.append((DFSEvent.MAXDEPTH,u))

                if (c := child[depth]) < len(G[u]):
                    child[depth] += 1
                    if state[v := G[u][c]]:
                        if DFSFlags.BACK in flags:
                            events.append((DFSEvent.BACK,u,v))
                        continue
                    state[v] = 1
                    if DFSFlags.DOWN in flags:
                        events.append((DFSEvent.DOWN,u,v))
                    stack[depth := depth+1] = v
                else:
                    state[u] = 0
                    if DFSFlags.LEAVE in flags:
                        events.append((DFSEvent.LEAVE,u))
                    child[depth] = 0
                    depth -= 1
                    if depth and DFSFlags.UP in flags:
                        events.append((DFSEvent.UP, stack[depth], u))
            if DFSFlags.UP|DFSFlags.CONNECT_ROOTS in flags:
                events.append((DFSEvent.UP,-1,s))
        return events
    
    def dfs_enter_leave(G, s: int|list[int]|None = None):
        stack: list[int] = [0]*(G.N+1)
        state = [0]*G.N
        events: list[tuple[DFSEvent, int]] = []

        for s in G.starts(s):
            if state[s]: continue
            state[s] = True
            stack[idx := 1] = s
            while idx:
                u = stack[idx], idx
                if state[u] == 1:
                    events.append((DFSEvent.ENTER,u))
                    for v in G[u]:
                        if state[v]: continue
                        state[v] = 1
                        stack[idx := idx+1] = v
                else:
                    events.append((DFSEvent.LEAVE,u))
                    idx -= 1

        return events
    
    def dfs_topdown(G, s: int|list[int]|None = None, connect_roots = False):
        '''Returns list of (u,v) representing u->v edges in order of top down discovery'''
        stack: list[int] = elist(G.N)
        vis = [False]*G.N
        edges: list[tuple[int,int]] = elist(G.N)

        for s in G.starts(s):
            if vis[s]: continue
            if connect_roots:
                edges.append((-1,s))
            vis[s] = True
            stack.append(s)
            while stack:
                u = stack.pop()
                for v in G[u]:
                    if vis[v]: continue
                    vis[v] = True
                    edges.append((u,v))
                    stack.append(v)
        return edges


    # def dfs_topdown(G, s: int|list[int]|None = None, connect_roots = False):
    #     '''Returns list of (u,v) representing u->v edges in order of top down discovery'''
    #     stack = [0] * G.N
    #     vis: list[bool] = [False]*G.N
    #     edges: list[tuple[int,int]] = []

    #     for s in G.starts(s):
    #         if vis[s]: continue
    #         if connect_roots:
    #             edges.append((-1,s))
    #         vis[s] = True
    #         stack[idx := 0] = s
    #         while idx != -1:
    #             u, idx = stack[idx], idx-1
    #             for v in G[u]:
    #                 if vis[v]: continue
    #                 vis[v] = True
    #                 edges.append((u,v))
    #                 stack[idx := idx+1] = v 

    #     return edges
    
    def dfs_topdown_indexed(G, s: int|list[int]|None = None, connect_roots = False):
        '''Returns list of (u,v) representing u->v edges in order of top down discovery'''
        stack = [0] * G.N
        vis: list[bool] = [False]*G.N
        edges: list[tuple[int,int,int]] = []

        for r,s in enumerate(G.starts(s)):
            if vis[s]: continue
            if connect_roots:
                edges.append((r,-1,s))
            vis[s] = True
            stack[idx := 0] = s
            while idx != -1:
                u, idx = stack[idx], idx-1
                for c,v in enumerate(G[u]):
                    if vis[v]: continue
                    vis[v] = True
                    edges.append((c,u,v))
                    stack[idx := idx+1] = v 

        return edges
    
    def dfs_bottomup(G, s: int|list[int]|None = None, connect_roots = False):
        '''Returns list of (p,u) representing p->u edges in bottom up order'''
        edges = G.dfs_topdown(s, connect_roots)
        edges.reverse()
        return edges
    
    def starts(G, v: int|list[int]|None) -> Iterable:
        match v:
            case int(v): return (v,)
            case None: return range(G.N)
            case V: return V

    @classmethod
    def compile(cls, N: int, M: int, E):
        edge = Parser.compile(E)
        def parse(ts: TokenStream):
            return cls(N, [edge(ts) for _ in range(M)])
        return parse
    

class Graph(GraphProtocol):
    def __init__(G, N: int, E: list[Edge]=[]):
        super().__init__(N, E, ([] for _ in range(N)))
        for u,v in G.E:
            G[u].append(v)
            G[v].append(u)

    def edge_ids(G) -> list[list[int]]:
        Eid = [[] for _ in range(G.N)]
        for e,(u,v) in enumerate(G.E):
            Eid[u].append(e)
            Eid[v].append(e)
        return Eid

    @classmethod
    def compile(cls, N: int, M: int, E: type|int = Edge[-1]):
        if isinstance(E, int): E = Edge[E]
        return super().compile(N, M, E)

from typing import overload, Literal
from functools import cached_property


from typing import Any, Callable, List

class SparseTable:
    def __init__(self, op: Callable[[Any, Any], Any], arr: List[Any]):
        self.n = len(arr)
        self.log = self.n.bit_length()
        self.op = op
        self.st = [[None] * (self.n-(1<<i)+1) for i in range(self.log)]
        self.st[0] = arr[:]
        
        for i in range(self.log-1):
            row, d = self.st[i], 1<<i
            for j in range(len(self.st[i+1])):
                self.st[i+1][j] = op(row[j], row[j+d])

    def query(self, l: int, r: int) -> Any:
        k = (r-l).bit_length()-1
        return self.op(self.st[k][l], self.st[k][r-(1<<k)])
    
    def __repr__(self) -> str:
        return '\n'.join(f'{i:<2d} {row}' for i,row in enumerate(self.st))

class BinaryIndexTree:
    def __init__(self, v: int|list):
        if isinstance(v, int):
            self.data, self.size = [0]*v, v
        else:
            self.build(v)

    def build(self, data):
        self.data, self.size = data, len(data)
        for i in range(self.size):
            if (r := i|(i+1)) < self.size: 
                self.data[r] += self.data[i]

    def get(self, i: int):
        assert 0 <= i < self.size
        s = self.data[i]
        z = i&(i+1)
        for _ in range((i^z).bit_count()):
            s, i = s-self.data[i-1], i-(i&-i)
        return s
    
    def set(self, i: int, x: int):
        self.add(i, x-self.get(i))
        
    def add(self, i: int, x: int) -> None:
        assert 0 <= i <= self.size
        i += 1
        data, size = self.data, self.size
        while i <= size:
            data[i-1], i = data[i-1] + x, i+(i&-i)

    def pref_sum(self, i: int):
        assert 0 <= i <= self.size
        s = 0
        data = self.data
        for _ in range(i.bit_count()):
            s, i = s+data[i-1], i-(i&-i)
        return s
    
    def range_sum(self, l: int, r: int):
        return self.pref_sum(r) - self.pref_sum(l)

class LCATable(SparseTable):
    def __init__(self, T, root = 0):
        self.start = [-1] * len(T)
        self.end = [-1] * len(T)
        self.euler = []
        self.depth = []
        
        # Iterative DFS
        stack = [(root, -1, 0)]
        while stack:
            u, p, d = stack.pop()
            
            if self.start[u] == -1:
                self.start[u] = len(self.euler)
                
                for v in reversed(T[u]):
                    if v != p:
                        stack.append((u, p, d))
                        stack.append((v, u, d+1))
                        
            self.euler.append(u)
            self.depth.append(d)
            self.end[u] = len(self.euler)
        super().__init__(min, list(zip(self.depth, self.euler)))

    def query(self, u, v) -> tuple[int,int]:
        l, r = min(self.start[u], self.start[v]), max(self.start[u], self.start[v])+1
        d, a = super().query(l, r)
        return a, d
    
    def distance(self, u, v) -> int:
        l, r = min(self.start[u], self.start[v]), max(self.start[u], self.start[v])+1
        d, _ = super().query(l, r)
        return self.depth[l] + self.depth[r] - 2*d
        

class TreeProtocol(GraphProtocol):

    @cached_property
    def lca(T):
        return LCATable(T)
    
    @overload
    def diameter(T) -> int: ...
    @overload
    def diameter(T, endpoints: Literal[True]) -> tuple[int,int,int]: ...
    def diameter(T, endpoints = False):
        _, s = max((d,v) for v,d in enumerate(T.dfs(0)))
        diam, g = max((d,v) for v,d in enumerate(T.dfs(s)))
        return (diam, s, g) if endpoints else diam
    
    @overload
    def distance(T) -> list[list[int]]: ...
    @overload
    def distance(T, s: int = 0) -> list[int]: ...
    @overload
    def distance(T, s: int, g: int) -> int: ...
    def distance(T, s = None, g = None):
        match s, g:
            case None, None:
                return [T.dfs(u) for u in range(T.N)]
            case s, g:
                return T.dfs(s, g)
            
    @overload
    def dfs(T, s: int = 0) -> list[int]: ...
    @overload
    def dfs(T, s: int, g: int) -> int: ...
    def dfs(T, s = 0, g = None):
        D = [inf for _ in range(T.N)]
        D[s] = 0
        state = [True for _ in range(T.N)]
        stack = [s]

        while stack:
            u = stack.pop()
            if u == g: return D[u]
            state[u] = False
            for v in T[u]:
                if state[v]:
                    D[v] = D[u]+1
                    stack.append(v)
        return D if g is None else inf 


    def dfs_events(G, opts: DFSFlags, s: int = 0):         
        events = []
        # stack = deque([(s,-1)], maxlen=G.N)
        stack = [(s,-1)]
        adj = [None]*G.N


        while stack:
            u, p = stack[-1]
            
            if adj[u] is None:
                adj[u] = iter(G.neighbors(u))
                if DFSFlags.ENTER in opts:
                    events.append((DFSEvent.ENTER, u))
            
            if (v := next(adj[u], None)) is not None:
                if v == p:
                    if DFSFlags.BACK in opts:
                        events.append((DFSEvent.BACK, u, v))
                else:
                    if DFSFlags.DOWN in opts:
                        events.append((DFSEvent.DOWN, u, v))
                    stack.append((v,u))
            else:
                stack.pop()

                if DFSFlags.LEAVE in opts:
                    events.append((DFSEvent.LEAVE, u))
                if p != -1 and DFSFlags.UP in opts:
                    events.append((DFSEvent.UP, u, p))
        return events


class Tree(Graph, TreeProtocol):

    @classmethod
    def compile(cls, N: int):

        def parse(ts: TokenStream):
            T = cls.__new__(cls)
            list.__init__(T, (elist(4) for _ in range(N)))
            
            V = ts.int_n(2*(N-1))
            
            for i in range(N-1):
                x, y = V[i<<1]-1, V[(i<<1)+1]-1
                T[x].append(y)
                T[y].append(x)

            T.N = N
            T.M = N-1
            return T

        return parse
    
def read_ints(count, maxdigits=10):
    """
    Read integers by collecting and decoding all input first, then processing
    """
    result = array('i', [0]*count)
    num_count = 0
    
    # First peek to find newline
    peek = sys.stdin.buffer.peek()
    nl_pos = peek.find(b'\n')
    if nl_pos != -1:
        # Read exactly up to and including newline
        first_line = sys.stdin.buffer.read(nl_pos + 1)
        print(f"First line was: {first_line}", sys.stdin.line_buffering)
    
    # Get all remaining buffered content from readline
    buffered = []
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        buffered.append(line)  # readline already returns str
    
    # Combine all into a single string for processing
    all_input =  ''.join(buffered) + first_line.decode('utf-8')
    
    # Now process all numbers from the combined string
    current = 0
    for c in all_input:
        if c >= '0' and c <= '9':
            current = current * 10 + (ord(c) - ord('0'))
        elif c in (' ', '\n'):
            result[num_count] = current
            num_count += 1
            current = 0
            if num_count >= count:
                return result
    
    # If we still need more numbers, continue with os.read
    if num_count < count:
        buffer = bytearray()
        pos = 0
        
        while num_count < count:
            if pos >= len(buffer):
                chunk = os.read(0, 8192)
                if not chunk:
                    if current > 0:
                        result[num_count] = current
                        num_count += 1
                    break
                buffer.extend(chunk)
                
            b = buffer[pos]
            pos += 1
            
            if b >= 48:  # ASCII '0'
                current = current * 10 + (b - 48)
            elif b in (32, 10):  # space or newline
                result[num_count] = current
                num_count += 1
                current = 0
                if num_count >= count:
                    break
    
    return result[:num_count]

from typing import Type, TypeVar, overload

T = TypeVar('T')
@overload
def read(spec: int|None) -> list[int]: ...
@overload
def read(spec: Type[T]|T, char=False) -> T: ...
def read(spec: Type[T]|T=None, char=False):
    match spec, char:
        case None, False:
            return list(map(int, input().split()))
        case int(offset), False:
            return [int(s)+offset for s in input().split()]
        case _, _:
            if char:
                stream = CharStream()
            else:
                stream = TokenStream()
            parser: T = Parser.compile(spec)
            return parser(stream)

if __name__ == '__main__':
    main()
