import cp_library.__header__
import cp_library.ds.__header__
from cp_library.ds.reserve_fn import reserve
import cp_library.ds.tree.__header__
import cp_library.ds.tree.bst.__header__
from cp_library.ds.tree.bst.bst_cls import BST

class CartesianTree(BST):
    K,P,sub,st=[-1],[42],[-1,-1],[]
    def _nr(T):T.P.append(-1);return super()._nr()
    def _nn(T,k,p=-1):T.P.append(p);return super()._nn(k)
    def get(T,k):return T.P[BST.get(T,k)]
    def pop(T,k):return T.P[BST.pop(T,k)]
    def split(T,k):S=T._nt();T.st.append(T.r<<1);T.st.append(S.r<<1);T._sp(T.sub[T.r<<1],k,S.r<<1,T.r<<1);T._r();return S,T
    def insert(T,k,p):T.st.append(T.r<<1);T._i(T.r<<1,k,n:=T._nn(k,p));T._r();return n
    def __getitem__(T,k):return T.get(k)
    def _i(T,s,k,n):
        while~T.sub[s]and T.P[i:=T.sub[s]]<T.P[n]:T.st.append(i<<1);s=i<<1|(T.K[i]<k)
        i,T.sub[s]=T.sub[s],n
        if~i:T.st.append(n<<1);T._sp(i,k,n<<1,n<<1|1)
    def _sp(T,i,k,l,r):
        while~i:
            T.st.append(i<<1)
            if T.K[i]<k:T.sub[l]=i;i=T.sub[l:=i<<1|1]
            else:T.sub[r]=i;i=T.sub[r:=i<<1]
        T.sub[l]=T.sub[r]=-1
    def _m(T,s,l,r):
        T.st.append(s)
        while~l and~r:
            if T.P[l]<T.P[r]:T.st.append(l<<1);T.sub[s]=l;l=T.sub[s:=l<<1|1]
            else:T.st.append(r<<1);T.sub[s]=r;r=T.sub[s:=r<<1]
        T.sub[s]=l if~l else r
    def _d(T,k,i):p=T.st[-1]>>1;T._m(p<<1|(p!=T.r and T.K[p]<k),T.sub[i<<1],T.sub[i<<1|1])
    @classmethod
    def reserve(cls,sz):super(CartesianTree,cls).reserve(sz);reserve(cls.P,sz+1)