import cp_library.__header__
import cp_library.ds.__header__
from cp_library.ds.list.reserve_fn import reserve
import cp_library.ds.tree.__header__
import cp_library.ds.tree.bst.__header__
from cp_library.ds.tree.bst.bst_sized_cls import BSTSized
from cp_library.ds.tree.bst.cartesian_tree_sized_cls import CartesianTreeSized
from cp_library.ds.tree.bst.treap_cls import Treap

class TreapSized(Treap, CartesianTreeSized):
    K,V,P,sz,sub,st=[-1],[-1],[42],[0,0],[-1,-1],[]
    def _nr(T):T.V.append(T.e);return CartesianTreeSized._nr(T)
    def _nn(T,k,v):T.V.append(v);return CartesianTreeSized._nn(T,k,(T.P[-1]*1103515245+12345)&0x7fffffff)
    def kth(T,k): return T.V[BSTSized.kth(T,k)]
    @classmethod
    def reserve(cls,sz):CartesianTreeSized.reserve.__call__(sz);reserve(cls.V,sz+1)