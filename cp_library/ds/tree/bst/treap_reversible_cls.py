import cp_library.__header__
import cp_library.ds.__header__
from cp_library.ds.reserve_fn import reserve
import cp_library.ds.tree.__header__
import cp_library.ds.tree.bst.__header__
from cp_library.ds.tree.bst.cartesian_tree_reversible_cls import CartesianTreeReversible
from cp_library.ds.tree.bst.treap_implicit_cls import TreapImplicit

class TreapReversible(TreapImplicit,CartesianTreeReversible):
    K,V,P,sz,sub,st=None,[-1],[42],[0,0],[-1,-1],[]
    def _nr(T):T.V.append(T.e);return CartesianTreeReversible._nr(T)
    def _nn(T,k,v):T.V.append(v);return CartesianTreeReversible._nn(T,k,(T.P[-1]*1103515245+12345)&0x7fffffff)
    @classmethod
    def reserve(cls,sz):CartesianTreeReversible.reserve.__call__(sz);reserve(cls.V,sz+1)