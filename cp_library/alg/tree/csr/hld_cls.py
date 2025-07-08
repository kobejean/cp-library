import cp_library.__header__
import cp_library.alg.__header__
import cp_library.alg.tree.__header__
import cp_library.alg.tree.csr.__header__
from cp_library.alg.tree.csr.hld_base_cls import HLDBase

class HLD(HLDBase):

    def path_query(hld, u, v, query_fn, edge=False):
        while hld.head[u] != hld.head[v]:
            if hld.depth[hld.head[u]] < hld.depth[hld.head[v]]:
                query_fn(hld.tin[hld.head[v]], hld.tin[v]+1)
                v = hld.up[v]
            else:
                query_fn(hld.tin[hld.head[u]], hld.tin[u]+1)
                u = hld.up[u]

        if hld.depth[u] < hld.depth[v]:
            query_fn(hld.tin[u]+edge, hld.tin[v]+1)
        else:
            query_fn(hld.tin[v]+edge, hld.tin[u]+1)
