import cp_library.__header__
import cp_library.ds.__header__
from cp_library.ds.reserve_fn import reserve
import cp_library.ds.tree.__header__
import cp_library.ds.tree.bst.__header__
from cp_library.ds.tree.bst.bst_cls import BSTUpdates
from cp_library.ds.tree.bst.treap_cls import Treap, TreapReversible

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
        while~a and not l<=T.K[a]<r:T._p(a);a=T.sub[a<<1|(T.K[a]<l)]
        if a<0:return T.e
        # left subtreap
        ac,i=T.V[a],T.sub[a<<1]
        while~i:
            T._p(i)
            if not(b:=T.K[i]<l):
                if~(j:=T.sub[i<<1|1]):ac=T.op(T.A[j],ac)
                ac=T.op(T.V[i],ac)
            i=T.sub[i<<1|b]
        # right subtreap
        i=T.sub[a<<1|1]
        while~i:
            T._p(i)
            if b:=T.K[i]<r:
                if~(j:=T.sub[i<<1]):ac=T.op(ac,T.A[j])
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
        T._p(i);ac = T.V[i]
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

class TreapMonoidReversibe(TreapMonoid,TreapReversible):
    __slots__='op'
    K,V,A,P,rev,sz,sub,st=None,[-1],[-1],[42],[0],[0,0],[-1,-1],[]
    def _nr(T):T.A.append(T.e);return TreapReversible._nr(T)
    def _nn(T,k,v):T.A.append(v);return TreapReversible._nn(T,k,v)
    def prod(T,l,r):
        # find common ancestor
        a=T.sub[T.r<<1]
        while~a:
            T._p(a)
            if l<=(sz:=T.sz[s:=a<<1])<r:break
            if sz<l:l-=1+sz;r-=1+sz;s^=1
            a=T.sub[s]
        if a<0:return T.e
        r-=T.sz[a<<1]+1
        # left subtreap
        ac,i=T.V[a],T.sub[a<<1]
        while~i and ~l:
            T._p(i)
            if (sz:=T.sz[s:=i<<1])<l:l-=1+sz;s^=1
            else:
                if~(j:=T.sub[i<<1|1]):ac=T.op(T.A[j],ac)
                ac=T.op(T.V[i],ac)
            i=T.sub[s]
        # right subtreap
        i=T.sub[a<<1|1]
        while~i and ~r:
            T._p(i)
            if (sz:=T.sz[s:=i<<1])<r:
                if~(j:=T.sub[s]):ac=T.op(ac,T.A[j])
                ac=T.op(ac,T.V[i])
                r-=1+sz;s^=1
            i=T.sub[s]
        return ac
    @classmethod
    def reserve(cls,sz):TreapReversible.reserve.__call__(sz);reserve(cls.A,sz+1)
    def _u(T,i):
        T.A[i]=T.V[i]
        T.sz[s]=T.sz[l<<1]+1+T.sz[l<<1|1] if~(l:=T.sub[s:=i<<1]) else 0
        T.sz[s]=T.sz[r<<1]+1+T.sz[r<<1|1] if~(r:=T.sub[s:=i<<1|1]) else 0
        if~(l:=T.sub[i<<1]):T.A[i]=T.op(T.A[l],T.A[i])
        if~(r:=T.sub[i<<1|1]):T.A[i]=T.op(T.A[i],T.A[r])
    def _node_str(T, i): return f"{i=} {T.V[i]}({T.A[i]})"