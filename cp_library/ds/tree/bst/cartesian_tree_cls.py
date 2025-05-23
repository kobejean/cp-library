import cp_library.__header__
import cp_library.ds.__header__
from cp_library.ds.reserve_fn import reserve
import cp_library.ds.tree.__header__
import cp_library.ds.tree.bst.__header__
from cp_library.ds.tree.bst.bst_cls import BST, BSTSized, BSTImplicit, BSTReversible

class CartesianTree(BST):
    K,P,sub,st=[-1],[42],[-1,-1],[]
    def _nr(T):T.P.append(-1);return super()._nr()
    def _nn(T,k,p=-1):T.P.append(p);return super()._nn(k)
    def get(T,k):return T.P[BST.get(T,k)]
    def pop(T,k):return T.P[BST.pop(T,k)]
    def split(T,k):S=T._nt();T._sp(T.sub[T.r<<1],k,S.r<<1,T.r<<1);T._r();return S,T
    def insert(T,k,p):T._i(T.r<<1,k,n:=T._nn(k,p));T._r();return n
    def __getitem__(T,k):return T.get(k)
    def _i(T,s,k,n):
        T.st.append(s)
        while~T.sub[s]and T.P[i:=T.sub[s]]<T.P[n]:T._p(i);T.st.append(s:=i<<1|(T.K[i]<k))
        i,T.sub[s]=T.sub[s],n
        if~i:T._sp(i,k,n<<1,n<<1|1)
    def _sp(T,i,k,l,r):
        T.st.append(l)
        if 1<l^r:T.st.append(r)
        while~i:
            T._p(i)
            if T.K[i]<k:T.sub[l]=i;i=T.sub[l:=i<<1|1];T.st.append(l)
            else:T.sub[r]=i;i=T.sub[r:=i<<1];T.st.append(r)
        T.sub[l]=T.sub[r]=-1
    def _m(T,s,l,r):
        T.st.append(s)
        while~l and~r:
            if T.P[l]<T.P[r]:T._p(l);T.sub[s]=l;l=T.sub[s:=l<<1|1]
            else:T._p(r);T.sub[s]=r;r=T.sub[s:=r<<1]
            T.st.append(s)
        T.sub[s]=l if~l else r
    def _d(T,i,s):T._p(i);T._m(s,T.sub[i<<1],T.sub[i<<1|1])
    @classmethod
    def reserve(cls,sz):super(CartesianTree,cls).reserve(sz);reserve(cls.P,sz+1)

class CartesianTreeSized(CartesianTree, BSTSized):
    K,P,sz,sub,st=[-1],[42],[0,0],[-1,-1],[]
    def kth(T,k): return T.P[BSTSized.kth(T,k)]

class CartesianTreeImplicit(CartesianTreeSized,BSTImplicit):
    K,P,sz,sub,st=None,[42],[0,0],[-1,-1],[]
    def _nr(T):T.P.append((T.P[-1]*1103515245+12345)&0x7fffffff);return BSTImplicit._nr(T)
    def _nn(T,k,p):T.P.append(p);return BSTImplicit._nn(T,k)
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

    def _node_str(T, i): return f"{T.P[i]}"

class CartesianTreeReversible(CartesianTreeSized,BSTReversible):
    def _nr(T):T.P.append((T.P[-1]*1103515245+12345)&0x7fffffff);return BSTReversible._nr(T)
    def _nn(T,k,v):T.P.append(v);return BSTReversible._nn(T,k)
    def reverse(T,l,r):
        if l>=r:return
        lo,hi = l>0,r<len(T)
        s = T.r<<1
        if hi:T._sp(T.sub[s],r,s,1);T._r()
        if lo:T._sp(T.sub[s],l,0,s);T._r()
        T.rev[T.sub[s]]^=1
        if hi:T._m(s,T.sub[s],T.sub[1]);T._r()
        if lo:T._m(s,T.sub[0],T.sub[s]);T._r()