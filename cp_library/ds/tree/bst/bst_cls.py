import cp_library.__header__
from cp_library.bit.masks.i64_max_cnst import i64_max
import cp_library.ds.__header__
from cp_library.ds.reserve_fn import reserve
import cp_library.ds.tree.__header__
import cp_library.ds.tree.bst.__header__

class BST:
    __slots__ = 'r'
    K,sub,st=[-1],[-1,-1],[]
    def __init__(T):T.r=T._nr()
    def _nt(T):return T.__class__()
    def _nr(T):r=len(T.K);T.K.append(i64_max);T.sub.append(-1);T.sub.append(-1);return r
    def _nn(T,k):n=len(T.K);T.K.append(k);T.sub.append(-1);T.sub.append(-1);return n
    def insert(T,k):T._i(T.r<<1,k,n:=T._nn(k));T._r();return n
    def get(T,k):
        if~(i:=T._f(T.r<<1,k)):return i
        raise KeyError
    def pop(T,k):
        if ~(i:=T._t(T.r<<1,k)):T._d(i,T.st[-1]);T._r();return i
        else:T.st.clear();raise KeyError
    def __delitem__(T,k):
        if~(i:=T._t(T.r<<1,k)):T._d(i,T.st[-1]);T._r()
        else:T.st.clear();raise KeyError
    def __contains__(T,k):return 0<=T._f(T.r<<1,k)
    def _f(T,s,k):
        i = T.sub[s]
        while~i and T.K[i]!=k:T._p(i);i=T.sub[i<<1|(T.K[i]<k)]
        return i
    def _t(T,s,k):
        T.st.append(s)
        while~(i:=T.sub[s])and T.K[i]!=k:T._p(i);T.st.append(s:=i<<1|(T.K[i]<k))
        return i
    def _i(T,s,k,n):
        T.st.append(s)
        while ~T.sub[s]:T._p(i:=T.sub[s]);T.st.append(s:=i<<1|(T.K[i]<k))
        i,T.sub[s]=T.sub[s],n
    def _d(T,i,s): raise NotImplemented
    def _r(T):T.st.clear()
    def _p(T,i): pass
    @classmethod
    def reserve(cls,sz):sz+=1;reserve(cls.K,sz);reserve(cls.sub,sz<<1);reserve(cls.st,sz.bit_length()<<1)
    def _node_str(T, i): return f"{T.K[i]}"

    def __str__(T):
        def rec(i, pre="", is_right=False):
            if i == -1: return ""
            ret = "";T._p(i)
            if ~(r:=T.sub[i<<1|1]):ret+=rec(r,pre+("   "if is_right else"│  "),True)
            ret+=pre+("┌─ "if is_right else"└─ ")+T._node_str(i)+"\n"
            if ~(l:=T.sub[i<<1]):ret+=rec(l,pre+("   "if not is_right else"│  "),False)
            return ret
        return rec(T.sub[T.r<<1]).rstrip()

class BSTUpdates(BST):
    def _u(T,i): pass
    def _r(T):
        while T.st:T._u(T.st.pop()>>1)

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

class BSTImplicit(BSTSized):
    K,sz,sub,st=None,[0,0],[-1,-1],[]
    def _nr(T):r=len(T.sz)>>1;T.sz.append(0);T.sz.append(0);T.sub.append(-1);T.sub.append(-1);return r
    def _nn(T,k):n=len(T.sz)>>1;T.sz.append(0);T.sz.append(0);T.sub.append(-1);T.sub.append(-1);return n
    def pop(T,k):
        if 0<=k<len(T):T._d(i:=T._kt(T.r<<1,k),T.st[-1]);T._r();return i
        else:raise KeyError
    def __contains__(T,k):raise NotImplemented
    def __delitem__(T,k):
        if 0<=k<len(T):T._d(T._kt(T.r<<1,k),T.st[-1]);T._r()
        else:raise KeyError
    def _f(T,s,k):return T._k(s,k)
    def _t(T,s,k):return T._kt(s,k)
    def _i(T,s,k,n):T.sub[T._kt(s,k)]=n
    @classmethod
    def reserve(cls,sz):sz+=1;reserve(cls.st,sz.bit_length()<<1);reserve(cls.sz,sz<<1);reserve(cls.sub,sz<<1)

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