import cp_library.__header__
from cp_library.bit.masks.i64_max_cnst import i64_max
import cp_library.ds.__header__
from cp_library.ds.list.reserve_fn import reserve
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