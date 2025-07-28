import cp_library.__header__
import cp_library.alg.__header__
import cp_library.alg.graph.__header__
import cp_library.alg.graph.csr.__header__
from cp_library.alg.graph.csr.graph_base_cls import GraphBase

class GridGraphBase(GraphBase):
    def __init__(G, H, W, M, S, U, V, deg, La, Ra, Ua, Va, Ea,
            dirs: list = [(-1,0),(0,1),(1,0),(0,-1)]):
        super().__init__(H*W, M, U, V, deg, La, Ra, Ua, Va, Ea)
        G.W, G.H, G.dirs = W, H, dirs
        G.S: list[str] = S
        G.dirs: list[tuple[int,int]] = dirs

    def vertex(G, key: tuple[int,int] | int):
        if isinstance(key, tuple): i,j = key; return i*G.W+j
        else: return key
    
    def check_bounds(G, i, j, v):
        return 0 <= i < G.H and 0 <= j < G.W
    
    is_valid = check_bounds
    
    @classmethod
    def compile(cls, H: int, W: int, *args):
        def parse(io: IOBase):
            S = ''.join(io.readchars() for _ in range(H))
            return cls(H, W, S, *args)
        return parse
from cp_library.io.parser_cls import IOBase