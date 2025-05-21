import cp_library.__header__
import cp_library.ds.__header__
from cp_library.ds.reserve_fn import reserve
import cp_library.ds.tree.__header__
import cp_library.ds.tree.bst.__header__

class BST:
    __slots__ = 'root'
    K, sub, st = [-1], [-1, -1], []

    def __init__(T): T.root = T._new_node(-1)

    def _new_tree(T): return T.__class__()

    def _new_node(T, key):
        id = len(T.K); T.K.append(key); T.sub.append(-1); T.sub.append(-1)
        return id

    def insert(T, key):
        T.st.append(T.root); T._insert(T.root<<1, nid := T._new_node(key)); T._repair()
        return nid

    def pop(T, key):
        if ~(id:=T._trace(key)): T._del(id); T._repair(); return id
        else: T.st.clear(); raise KeyError

    def __delitem__(T, key):
        if ~(id:=T._trace(key)): T._del(id); T._repair()
        else: T.st.clear(); raise KeyError

    def __contains__(T, key): return 0 <= T._find(key)

    def _find(T, key):
        id = T.sub[T.root<<1]
        while ~id and T.K[id] != key: id = T.sub[id<<1|(T.K[id]<key)]
        return id

    def _trace(T, key):
        id = T.sub[T.root<<1]; T.st.append(T.root)
        while ~id and T.K[id] != key: T.st.append(id); id = T.sub[id<<1|(T.K[id]<key)]
        return id

    def _insert(T, sid, nid):
        while ~T.sub[sid]: T.st.append(id:=T.sub[sid]); sid=id<<1|(T.K[id]<T.K[nid])
        id, T.sub[sid] = T.sub[sid], nid

    def _del(T, id): raise NotImplemented

    def _repair(T): T.st.clear()

    @classmethod
    def reserve(cls, hint: int):
        hint += 1
        reserve(cls.K, hint); reserve(cls.sub, hint << 1); reserve(cls.st, hint.bit_length() << 1)