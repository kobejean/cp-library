import cp_library.__header__
import cp_library.ds.__header__
from cp_library.ds.reserve_fn import reserve
import cp_library.ds.tree.__header__
import cp_library.ds.tree.bst.__header__
from cp_library.ds.tree.bst.bst_cls import BST
from cp_library.ds.tree.bst.cartesian_tree_cls import CartesianTree

class Treap(CartesianTree):
    K, V, P, sub, st = [-1], [-1], [42], [-1, -1], []

    def __init__(T, e = 0):
        T.e = e
        T.root = T._new_node(-1, e)
        T.P[T.root] = -1
        
    def _new_tree(T): return T.__class__(T.e)

    def _new_node(T, key, val):
        T.V.append(val)
        return super()._new_node(key, (T.P[-1] * 1103515245 + 12345) & 0x7fffffff)

    def insert(T, key, val): return super().insert(key, val)
    
    def get(T, key): return T.V[id] if ~(id:=T._find(key)) else T.e
    
    def set(T, key, val): T.set_node(key, val); T._repair()

    def pop(T, key): return T.V[BST.pop(T, key)]

    def __setitem__(T, key, val): T.set(key, val)
    
    def set_node(T, key, val):
        if ~(id:=T._trace(key)): T.V[id] = val; T.st.append(id)
        else:
            nid = T._new_node(key, val)
            while T.P[nid]<T.P[id:=T.st[-1]]: T.st.pop()
            id, T.sub[sid] = T.sub[sid := id<<1|(id!=T.root and T.K[id]<key)], nid
            if ~id: T.st.append(nid); T._split(id, key, nid<<1, nid<<1|1)

    @classmethod
    def reserve(cls, hint: int): super(Treap, cls).reserve(hint); reserve(cls.V, hint+1)