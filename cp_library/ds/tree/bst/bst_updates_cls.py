import cp_library.__header__
import cp_library.ds.__header__
import cp_library.ds.tree.__header__
import cp_library.ds.tree.bst.__header__
from cp_library.ds.tree.bst.bst_cls import BST

class BSTUpdates(BST):
    def _u(T,i): pass
    def _r(T):
        while T.st:T._u(T.st.pop()>>1)