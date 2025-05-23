import cp_library.__header__
import cp_library.ds.__header__
from cp_library.ds.reserve_fn import reserve
import cp_library.ds.tree.__header__
import cp_library.ds.tree.bst.__header__
from cp_library.ds.tree.bst.bst_implicit_cls import BSTImplicit

class BSTReversible(BSTImplicit):
    K,rev,sz,sub,st=None,[0],[0,0],[-1,-1],[]
    def _nr(T):T.rev.append(0);return super()._nr()
    def _nn(T,k):T.rev.append(0);return super()._nn(k)
    def _p(T,i):
        if T.rev[i]:
            T.sub[l],T.sub[r],T.sz[l],T.sz[r]=T.sub[r:=i<<1|1],T.sub[l:=i<<1],T.sz[r],T.sz[l]
            if~(l:=T.sub[l]):T.rev[l]^=1
            if~(r:=T.sub[r]):T.rev[r]^=1
            T.rev[i]=0
    @classmethod
    def reserve(cls,sz):super().reserve(sz);reserve(cls.rev,sz+1)