import cp_library.__header__
import cp_library.ds.__header__
from cp_library.ds.reserve_fn import reserve
import cp_library.ds.tree.__header__
import cp_library.ds.tree.bst.__header__
from cp_library.ds.tree.bst.cartesian_tree_implicit_cls import CartesianTreeImplicit
from cp_library.ds.tree.bst.treap_sized_cls import TreapSized

class TreapImplicit(TreapSized,CartesianTreeImplicit):
    K,V,P,sz,sub,st=None,[-1],[42],[0,0],[-1,-1],[]
    def _nr(T):T.V.append(T.e);return CartesianTreeImplicit._nr(T)
    def _nn(T,k,v):T.V.append(v);return CartesianTreeImplicit._nn(T,k,(T.P[-1]*1103515245+12345)&0x7fffffff)
    def set(T,k,v):T._s(T.r<<1,k,v);T._r()
    def _i(T,s,k,n):
        T.st.append(s)
        while ~k and ~T.sub[s] and T.P[i:=T.sub[s]]<T.P[n]:
            T._p(i)
            if (sz:=T.sz[s:=i<<1])<k:k-=1+sz;s^=1
            T.st.append(s)
        i,T.sub[s]=T.sub[s],n
        if~i:T._sp(i,k,n<<1,n<<1|1)
    def _sp(T,i,k,l,r):
        T.st.append(l)
        if 1<l^r:T.st.append(r)
        while~i:
            T._p(i)
            if (sz:=T.sz[i<<1])<k:k-=1+sz;T.sub[l]=i;i=T.sub[l:=i<<1|1];T.st.append(l)
            else:T.sub[r]=i;i=T.sub[r:=i<<1];T.st.append(r)
        T.sub[l]=T.sub[r]=-1
    def _s(T,s,k,v):T.V[i:=T._t(s,k)]=v;T.st.append(i<<1)
    def _node_str(T, i): return f"{T.V[i]}"
    @classmethod
    def reserve(cls,sz):CartesianTreeImplicit.reserve.__call__(sz);reserve(cls.V,sz+1)