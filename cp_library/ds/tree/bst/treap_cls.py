import cp_library.__header__
import cp_library.ds.__header__
from cp_library.ds.reserve_fn import reserve
import cp_library.ds.tree.__header__
import cp_library.ds.tree.bst.__header__
from cp_library.ds.tree.bst.bst_cls import BST
from cp_library.ds.tree.bst.cartesian_tree_cls import CartesianTree

class Treap(CartesianTree):
    __slots__='e'
    K,V,P,sub,st=[-1],[-1],[42],[-1,-1],[]
    def __init__(T,e=-1):T.e=e;super().__init__()
    def _nt(T):return T.__class__(T.e)
    def _nr(T):T.V.append(T.e);return super()._nr()
    def _nn(T,k,v):T.V.append(v);return super()._nn(k,(T.P[-1]*1103515245+12345)&0x7fffffff)
    def insert(T,k,v):return super().insert(k,v)
    def get(T,k):return T.V[BST.get(T,k)]
    def pop(T,k):return T.V[BST.pop(T,k)]
    def set(T,k,v):T._s(T.r<<1,k,v);T._r()
    def __setitem__(T,k,v):T.set(k,v)
    def _s(T,s,k,v):
        if ~(i:=T._t(s,k)):T.V[i]=v;T.st.append(i<<1)
        else:
            n=T._nn(k,v)
            while T.P[n]<T.P[i:=T.st[-1]>>1]:T._p(T.st.pop())
            T._p(i)
            i,T.sub[s]=T.sub[s:=i<<1|(i!=T.r and T.K[i]<k)],n
            if~i:T._sp(i,k,n<<1,n<<1|1)
    def _node_str(T, i): return f"{T.K[i]}:{T.V[i]}"
    @classmethod
    def reserve(cls,hint):super(Treap,cls).reserve(hint);reserve(cls.V,hint+1)