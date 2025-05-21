import cp_library.__header__
import cp_library.ds.__header__
from cp_library.ds.reserve_fn import reserve
import cp_library.ds.tree.__header__
import cp_library.ds.tree.bst.__header__
from cp_library.ds.tree.bst.treap_cls import Treap

class TreapMonoid(Treap):
    __slots__ = 'op', 'e'
    K, V, A, P, sub, st = [-1], [-1], [-1], [42], [-1, -1], []
    def __init__(T, op, e = -1): T.op = op; super().__init__(e)
    def _new_tree(T): return T.__class__(T.op, T.e)
    def _new_node(T, key, val): T.A.append(val); return super()._new_node(key, val)

    def prod(T, l: int, r: int):
        # find common ancestor
        a = T.sub[T.root<<1]
        while ~a and not l <= T.K[a] < r: a = T.sub[a<<1|(T.K[a]<l)]
        if a < 0: return T.e
        # left subtreap
        acc, i = T.V[a], T.sub[a<<1]
        while ~i:
            if not (b:=T.K[i]<l):
                if ~T.sub[i<<1|1]: acc = T.op(T.A[T.sub[i<<1|1]], acc)
                acc = T.op(T.V[i], acc)
            i = T.sub[i<<1|b]
        # right subtreap
        i = T.sub[a<<1|1]
        while ~i:
            if b:=T.K[i]<r:
                if ~T.sub[i<<1]: acc = T.op(acc, T.A[T.sub[i<<1]])
                acc = T.op(acc, T.V[i])
            i = T.sub[i<<1|b]
        return acc

    def all_prod(T): return T.A[T.root]
    
    def __getitem__(T, key):
        if isinstance(key, int): return T.get(key)
        elif isinstance(key, slice): return T.prod(key.start, key.stop)
    
    @classmethod
    def reserve(cls, hint: int): super(TreapMonoid, cls).reserve(hint); reserve(cls.A, hint+1)
    
    def _repair(T):
        while T.st:
            T.A[id] = T.V[id := T.st.pop()]
            if ~(l := T.sub[id << 1]): T.A[id] = T.op(T.A[l], T.A[id])
            if ~(r := T.sub[id<<1|1]): T.A[id] = T.op(T.A[id], T.A[r])
        assert id == T.root

    def _validate(T, id = None):
        if id is None:
            assert T.all_prod() == (acc := T._validate(id) if ~(id := T.sub[T.root<<1]) else T.e)
            return acc
        acc = T.V[id]
        if ~(l:=T.sub[id<<1]):
            assert T.P[id] <= T.P[l]
            assert T.K[l] <= T.K[id]
            acc = T.op(T._validate(l), acc)
        if ~(r:=T.sub[id<<1|1]):
            assert T.P[id] <= T.P[r]
            assert T.K[id] <= T.K[r]
            acc = T.op(acc, T._validate(r))
        assert T.A[id] == acc
        return acc