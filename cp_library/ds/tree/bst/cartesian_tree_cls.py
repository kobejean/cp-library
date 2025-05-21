import cp_library.__header__
import cp_library.ds.__header__
from cp_library.ds.reserve_fn import reserve
import cp_library.ds.tree.__header__
import cp_library.ds.tree.bst.__header__
from cp_library.ds.tree.bst.bst_cls import BST

class CartesianTree(BST):
    K, P, sub, st = [-1], [42], [-1, -1], []

    def _new_node(T, key, prior = -1): T.P.append(prior); return super()._new_node(key)

    def get(T, key):
        if ~(id:=T._find(key)): return T.P[id]
        raise KeyError

    def split(T, key):
        S = T._new_tree(); T.st.append(T.root); T.st.append(S.root); 
        T._split(T.sub[T.root<<1], key, S.root<<1, T.root<<1); T._repair()
        return S, T

    def insert(T, key, prior):
        T.st.append(T.root); T._insert(T.root<<1, nid := T._new_node(key, prior)); T._repair()
        return nid

    def pop(T, key): return T.P[super().pop(key)]

    def __getitem__(T, key): return T.get(key)

    def _insert(T, sid, nid):
        while ~T.sub[sid] and T.P[id:=T.sub[sid]]<T.P[nid]: T.st.append(id); sid=id<<1|(T.K[id]<T.K[nid])
        id, T.sub[sid] = T.sub[sid], nid
        if ~id: T.st.append(nid); T._split(id, T.K[nid], nid<<1, nid<<1|1)

    def _split(T, id, key, l, r):
        while ~id:
            T.st.append(id)
            if T.K[id] < key: T.sub[l] = id; id = T.sub[l := id<<1|1]
            else: T.sub[r] = id; id = T.sub[r := id<<1]
        T.sub[l] = T.sub[r] = -1

    def _merge(T, sid, l, r):
        T.st.append(sid>>1)
        while ~l and ~r:
            if T.P[l]<T.P[r]: T.st.append(l); T.sub[sid] = l; l = T.sub[sid:=l<<1|1]
            else: T.st.append(r); T.sub[sid] = r; r = T.sub[sid:=r<<1]
        T.sub[sid] = l if ~l else r

    def _del(T, id):
        pid = T.st[-1]
        T._merge(pid<<1|(pid!=T.root and T.K[pid]<T.K[id]), T.sub[id<<1], T.sub[id<<1|1])

    @classmethod
    def reserve(cls, hint: int): super(CartesianTree, cls).reserve(hint); reserve(cls.P, hint+1)