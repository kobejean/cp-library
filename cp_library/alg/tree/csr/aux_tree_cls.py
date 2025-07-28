import cp_library.__header__
from cp_library.io.parser_cls import IOBase

import cp_library.alg.__header__
import cp_library.alg.tree.__header__
from cp_library.alg.tree.lca_table_iterative_cls import LCATable

import cp_library.alg.tree.csr.__header__
from cp_library.alg.tree.csr.tree_weighted_cls import TreeWeighted
from cp_library.alg.tree.csr.aux_tree_base_cls import AuxTreeBase

class AuxTree(AuxTreeBase, TreeWeighted):

    def __init__(T, N, U, V, root=0):
        TreeWeighted.__init__(T, N, U, V, [1]*len(U))
        AuxTreeBase.__init__(T, LCATable(T, root))

    @classmethod
    def compile(cls, N: int, shift: int = -1, root=0):
        def parse(io: IOBase):
            U, V = u32f(N-1), u32f(N-1)
            for i in range(N-1):
                u, v = io.readints()
                U[i], V[i] = u+shift, v+shift
            return cls(N, U, V, root)
        return parse
from cp_library.ds.array.u32f_fn import u32f