import cp_library.__header__
import cp_library.ds.__header__
from cp_library.ds.reserve_fn import reserve
import cp_library.ds.tree.__header__
import cp_library.ds.tree.bst.__header__
from cp_library.ds.tree.bst.bst_sized_cls import BSTSized
from cp_library.ds.tree.bst.cartesian_tree_cls import CartesianTree

class CartesianTreeSized(CartesianTree, BSTSized):
    K,P,sz,sub,st=[-1],[42],[0,0],[-1,-1],[]
    def kth(T,k): return T.P[BSTSized.kth(T,k)]
    def _nr(T):T.P.append(-1);return BSTSized._nr(T)
    def _nn(T,k,p=-1):T.P.append(p);return BSTSized._nn(T,k)
    @classmethod
    def reserve(cls,sz):BSTSized.reserve.__call__(sz);reserve(cls.P,sz+1)