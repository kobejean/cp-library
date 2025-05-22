import random
import cp_library.__header__
import cp_library.ds.__header__
from cp_library.ds.reserve_fn import reserve
import cp_library.ds.tree.__header__
import cp_library.ds.tree.bst.__header__
from cp_library.ds.tree.bst.bst_cls import BST, BSTSized, BSTImplicit
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
    def set(T,k,v):T._s(k,v);T._r()
    def __setitem__(T,k,v):T.set(k,v)
    def _s(T,k,v):
        if ~(i:=T._t(k)):T.V[i]=v;T.st.append(i<<1)
        else:
            n=T._nn(k,v)
            while T.P[n]<T.P[i:=T.st[-1]>>1]:T.st.pop()
            i,T.sub[s]=T.sub[s:=i<<1|(i!=T.r and T.K[i]<k)],n
            if~i:T.st.append(n<<1);T._sp(i,k,n<<1,n<<1|1)
    def _node_str(T, i): return f"{T.K[i]}:{T.V[i]}"
    @classmethod
    def reserve(cls,hint):super(Treap,cls).reserve(hint);reserve(cls.V,hint+1)

class TreapSized(Treap, BSTSized):
    K,V,P,sub,st=[-1],[-1],[42],[-1,-1],[]
    def kth(T,k): return T.V[super().kth(k)]

class TreapImplicit(TreapSized,BSTImplicit):
    K,V,P,sub,st=None,[-1],[42],[-1,-1],[]
    def _nr(T):T.P.append((T.P[-1]*1103515245+12345)&0x7fffffff);return BSTImplicit._nr(T)
    def _nn(T,k,v):T.P.append((T.P[-1]*1103515245+12345)&0x7fffffff);return BSTImplicit._nn(T,k,v)
    def set(T,k,v):T._s(k,v);T._r()
    def _i(T,s,k,n):
        while ~k and ~T.sub[s] and T.P[i:=T.sub[s]]<T.P[n]:
            T.st.append(i<<1)
            if (sz:=T.sz[s:=i<<1])<k:k-=1+sz;s^=1
        i,T.sub[s]=T.sub[s],n
        if~i:T.st.append(n<<1);T._sp(i,k,n<<1,n<<1|1)
    def _sp(T,i,k,l,r):
        while~i:
            T.st.append(i<<1)
            if (sz:=T.sz[i<<1])<k:k-=1+sz;T.sub[l]=i;i=T.sub[l:=i<<1|1]
            else:T.sub[r]=i;i=T.sub[r:=i<<1]
        T.sub[l]=T.sub[r]=-1
    def _s(T,k,v):T.V[i:=T._t(k)]=v;T.st.append(i<<1)
    # def _m(T,s,l,r):
    #     T.st.append(s>>1)
    #     while~l and~r:
    #         if T.P[l]<T.P[r]:T.st.append(l);T.sub[s]=l;l=T.sub[s:=l<<1|1]
    #         else:T.st.append(r);T.sub[s]=r;r=T.sub[s:=r<<1]
    #     T.sub[s]=l if~l else r
    # def _d(T,i):p=T.st[-1];T._m(p<<1|(p!=T.r and T.K[p]<T.K[i]),T.sub[i<<1],T.sub[i<<1|1])

    def _node_str(T, i): return f"{T.V[i]}"
if __name__ == '__main__':
    T = TreapSized()
    L = 5
    for i in range(L):
        T[i] = i*10
    for i in range(L):
        assert T.kth(i) == i*10
    A = [T.kth(i) for i in range(L)]
    print(A)
    print(T)

    T = TreapImplicit()
    random.shuffle(A)
    for i,a in enumerate(A):
        T.insert(i,a)
    print(A)
    print(T)
    T.insert(4,3)
    print(T)
