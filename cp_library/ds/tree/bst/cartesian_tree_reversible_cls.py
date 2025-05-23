import cp_library.__header__
import cp_library.ds.__header__
from cp_library.ds.reserve_fn import reserve
import cp_library.ds.tree.__header__
import cp_library.ds.tree.bst.__header__
from cp_library.ds.tree.bst.bst_reversible_cls import BSTReversible
from cp_library.ds.tree.bst.cartesian_tree_sized_cls import CartesianTreeSized

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
    @classmethod
    def reserve(cls,sz):BSTReversible.reserve.__call__(sz);reserve(cls.P,sz+1)