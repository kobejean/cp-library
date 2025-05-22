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
    def _nr(T):i=len(T.K);T.K.append(i64_max);T.sub.append(-1);T.sub.append(-1);return i
    def _nn(T,k):i=len(T.K);T.K.append(k);T.sub.append(-1);T.sub.append(-1);return i
    def insert(T,k):T.st.append(T.r>>1);T._i(T.r<<1,k,n:=T._nn(k));T._r();return n
    def get(T,k):
        if~(i:=T._f(k)):return i
        raise KeyError
    def pop(T,k):
        if ~(i:=T._t(k)):T._d(k,i);T._r();return i
        else:T.st.clear();raise KeyError
    def __delitem__(T,k):
        if~(i:=T._t(k)):T._d(k,i);T._r()
        else:T.st.clear();raise KeyError
    def __contains__(T,k):return 0<=T._f(k)
    def _f(T,k):
        i = T.sub[T.r<<1]
        while~i and T.K[i]!=k:i=T.sub[i<<1|(T.K[i]<k)]
        return i
    def _t(T,k):
        i=T.sub[T.r<<1];T.st.append(T.r<<1)
        while~i and T.K[i]!=k:T.st.append(i<<1);i=T.sub[i<<1|(T.K[i]<k)]
        return i
    def _i(T,s,k,n):
        while ~T.sub[s]:T.st.append((i:=T.sub[s])<<1);s=i<<1|(T.K[i]<k)
        i,T.sub[s]=T.sub[s],n
    def _d(T,k,i): raise NotImplemented
    def _r(T):T.st.clear()
    @classmethod
    def reserve(cls,sz):sz+=1;reserve(cls.K,sz);reserve(cls.sub,sz<<1);reserve(cls.st,sz.bit_length()<<1)
    def _node_str(T, i): return f"{T.K[i]}"

    def __str__(T):
        def rec(i, pre="", is_right=False):
            if i == -1: return ""
            ret = ""
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
        if 0<=k<len(T): return T._k(k)>>1
        raise KeyError
    def __len__(T):return T.sz[T.r<<1]
    def _k(T,k):
        s = T.r<<1
        while ~k:
            if (sz:=T.sz[s:=T.sub[s]<<1])<=k:k-=1+sz;s^=1
        return s
    def _u(T,i):
        T.sz[s]=T.sz[l<<1]+1+T.sz[l<<1|1] if~(l:=T.sub[s:=i<<1]) else 0
        T.sz[s]=T.sz[r<<1]+1+T.sz[r<<1|1] if~(r:=T.sub[s:=i<<1|1]) else 0
    @classmethod
    def reserve(cls,sz):super().reserve(sz);reserve(cls.sz,(sz+1)<<1)

class BSTImplicit(BSTSized):
    K,V,sz,sub,st=None,[-1],[0,0],[-1,-1],[]
    def _nr(T):T.sz.append(0);T.sz.append(0);r=len(T.V);T.V.append(-1);T.sub.append(-1);T.sub.append(-1);return r
    def _nn(T,k,v):T.sz.append(0);T.sz.append(0);n=len(T.V);T.V.append(v);T.sub.append(-1);T.sub.append(-1);return n
    def pop(T,k):
        if 0<=k<len(T):T._d(k,i:=T._kt(k));T._r();return T.V[i]
        else:T.st.clear();raise KeyError
    def __delitem__(T,k):
        if 0<=k<len(T):T._d(k,T._kt(k));T._r()
        else:T.st.clear();raise KeyError
    def _f(T,k):return T._k(k)>>1
    def _kt(T,s,k):
        while ~k:
            T.st.append((i:=T.sub[s])<<1)
            if (sz:=T.sz[s:=i<<1])<=k:k-=1+sz;s^=1
        return s
    def _i(T,s,k,n):T.sub[T._kt(s,k)]=n
    @classmethod
    def reserve(cls,sz):
        sz+=1;reserve(cls.V,sz);reserve(cls.st,sz.bit_length()<<1);reserve(cls.sz,sz<<1);reserve(cls.sub,sz<<1)

class BSTLazy(BSTUpdates):
    def _p(T,i): pass

# class BSTReversible(BSTImplicit, BSTLazy):
#     K,sz,rev,sub,st=[-1],[0],[0],[-1,-1],[]
#     def _nr(T):T.rev.append(0);return super()._nr()
#     def _nn(T,k):T.rev.append(0);return super()._nn(k)
#     def _p(T,i):
#         if T.rev[i]:
#             if~(l:=T.sub[i<<1]):T.rev[l]^=1
#             if~(r:=T.sub[i<<1|1]):T.rev[r]^=1
#             T.rev[i]=0
#     def _k(T,k):
#         s=(i:=T.r)<<1;T._p(i)
#         while 0<k and~T.sub[s]:
#             T._p(i:=T.sub[s]);sz=0
#             if~(l:=T.sub[i<<1|T.rev[i]]) and k<(sz:=T.sz[l]):s=i<<1|T.rev[i];continue
#             k-=1+sz;s^=1
#         if ~k:
#             while ~T.sub[s]:T._p(i:=T.sub[s]);s=i<<1|T.rev[i]
#         return i
#     def reverse(T,l,r):
#         if l>=r:return
#         T.st.append(T.r);T._rev(T.sub[T.r<<1],l,r);T._r()
#     def _rev(T,i,l,r):
#         if~i:
#             T.st.append(i);ls=T._ls(i)
#             if l<=ls and ls<r:T.rev[i]^=1
#             if l<ls:T._rev(T._lc(i),l,min(r,ls))
#             if ls+1<r:T._rev(T._rc(i),max(0,l-ls-1),r-ls-1)
#     @classmethod
#     def reserve(cls,sz):super().reserve(sz);reserve(cls.rev,sz+1)
