import cp_library.__header__
import cp_library.ds.__header__
from cp_library.ds.list.reserve_fn import reserve
import cp_library.ds.tree.__header__
import cp_library.ds.tree.bst.__header__
from cp_library.ds.tree.bst.bst_updates_cls import BSTUpdates

class BSTSized(BSTUpdates):
    K,sz,sub,st=[-1],[0,0],[-1,-1],[]
    def _nr(T):T.sz.append(0);T.sz.append(0);return super()._nr()
    def _nn(T,k):T.sz.append(0);T.sz.append(0);return super()._nn(k)
    def kth(T,k):
        if 0<=k<len(T):return T._k(T.r<<1,k)
        raise KeyError
    def __len__(T):return T.sz[T.r<<1]
    def _k(T,s,k):
        while ~k:
            T._p(T.sub[s])
            if (sz:=T.sz[s:=T.sub[s]<<1])<=k:k-=1+sz;s^=1
        return s>>1
    def _kt(T,s,k):
        while ~k:
            T._p(T.sub[s]);T.st.append(s)
            if (sz:=T.sz[s:=T.sub[s]<<1])<=k:k-=1+sz;s^=1
        return s>>1
    def _u(T,i):
        T.sz[s]=T.sz[l<<1]+1+T.sz[l<<1|1] if~(l:=T.sub[s:=i<<1]) else 0
        T.sz[s]=T.sz[r<<1]+1+T.sz[r<<1|1] if~(r:=T.sub[s:=i<<1|1]) else 0
    @classmethod
    def reserve(cls,sz):super().reserve(sz);reserve(cls.sz,(sz+1)<<1)