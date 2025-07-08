import cp_library.__header__
from cp_library.io.parser_cls import TokenStream

import cp_library.alg.__header__
import cp_library.alg.tree.__header__
from cp_library.alg.tree.lca_table_weighted_iterative_cls import LCATableWeighted

import cp_library.alg.tree.csr.__header__
from cp_library.alg.tree.csr.tree_weighted_cls import TreeWeighted
from cp_library.alg.tree.csr.aux_tree_base_cls import AuxTreeBase

class AuxTreeWeighted(AuxTreeBase, TreeWeighted):

    def __init__(T, N, U, V, W, root=0):
        TreeWeighted.__init__(T, N, U, V, W)
        AuxTreeBase.__init__(T, LCATableWeighted(T, root))

    @classmethod
    def compile(cls, N: int, shift: int = -1, root=0):
        M = N-1
        def parse(ts: TokenStream):
            U, V, W = u32f(M), u32f(M), [0]*M
            for i in range(M):
                u, v, w = ts._line()
                U[i], V[i], W[i] = int(u)+shift, int(v)+shift, int(w)
            return cls(N, U, V, W, root)
        return parse
from cp_library.ds.array.u32f_fn import u32f