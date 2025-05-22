import cp_library.__header__
import cp_library.ds.__header__
from cp_library.ds.reserve_fn import reserve
import cp_library.ds.tree.__header__
import cp_library.ds.tree.bst.__header__
from cp_library.ds.tree.bst.bst_cls import BSTUpdates
from cp_library.ds.tree.bst.treap_cls import Treap

class TreapMonoid(Treap, BSTUpdates):
    __slots__='op'
    K,V,A,P,sub,st=[-1],[-1],[-1],[42],[-1,-1],[]
    def __init__(T,op,e=-1):T.op=op;super().__init__(e)
    def _nt(T):return T.__class__(T.op,T.e)
    def _nr(T):T.A.append(T.e);return super()._nr()
    def _nn(T,k,v):T.A.append(v);return super()._nn(k, v)
    def prod(T,l,r):
        # find common ancestor
        a=T.sub[T.r<<1]
        while~a and not l<=T.K[a]<r:a=T.sub[a<<1|(T.K[a]<l)]
        if a<0:return T.e
        # left subtreap
        ac,i=T.V[a],T.sub[a<<1]
        while~i:
            if not(b:=T.K[i]<l):
                if~T.sub[i<<1|1]:ac=T.op(T.A[T.sub[i<<1|1]],ac)
                ac=T.op(T.V[i],ac)
            i=T.sub[i<<1|b]
        # right subtreap
        i=T.sub[a<<1|1]
        while~i:
            if b:=T.K[i]<r:
                if~T.sub[i<<1]:ac=T.op(ac,T.A[T.sub[i<<1]])
                ac=T.op(ac,T.V[i])
            i=T.sub[i<<1|b]
        return ac
    def all_prod(T):return T.A[T.r]
    def __getitem__(T,k):
        if isinstance(k,int):return T.get(k)
        elif isinstance(k,slice):return T.prod(k.start,k.stop)
    @classmethod
    def reserve(cls,sz):super(TreapMonoid,cls).reserve(sz);reserve(cls.A,sz+1)
    def _u(T,i):
        T.A[i]=T.V[i]
        if~(l:=T.sub[i<<1]):T.A[i]=T.op(T.A[l],T.A[i])
        if~(r:=T.sub[i<<1|1]):T.A[i]=T.op(T.A[i],T.A[r])
    def _v(T,i=None):
        if i is None:
            assert T.all_prod() == (ac := T._v(i) if ~(i := T.sub[T.r<<1]) else T.e)
            return ac
        ac = T.V[i]
        if ~(l:=T.sub[i<<1]):
            assert T.P[i] <= T.P[l]
            assert T.K[l] <= T.K[i]
            ac = T.op(T._v(l), ac)
        if ~(r:=T.sub[i<<1|1]):
            assert T.P[i] <= T.P[r]
            assert T.K[i] <= T.K[r]
            ac = T.op(ac, T._v(r))
        assert T.A[i] == ac
        return ac