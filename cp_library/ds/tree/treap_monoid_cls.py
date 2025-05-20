import cp_library.__header__
import cp_library.ds.__header__
from cp_library.ds.reserve_fn import reserve
import cp_library.ds.tree.__header__

class TreapMonoid:
    __slots__ = 'op', 'e', 'root', 'cnt'
    # class attributes
    K, V, A, P = [-1], [-1], [-1], [42]
    par, sub, st = [-1], [-1, -1], []

    def __init__(T, op, e = -1):
        T.op, T.e, T.cnt = op, e, -1
        T.root = T.new_node(-1, e)

    def prod(T, l: int, r: int):
        # find_node common ancestor
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
    
    def insert(T, key, val):
        T.insert_node(T.root<<1, nid := T.new_node(key, val))
        return nid
    
    def split(T, key):
        T.K[0] = key
        T.split_node(T.sub[T.root<<1], 0)
        S = T.__class__(T.op, T.e)
        if ~S.sub[0]: S.attach_node(S.root<<1, T.sub[0])
        if ~T.sub[1]: T.attach_node(T.root<<1, T.sub[1])
        T._repair()
        return S, T
    
    def get(T, key): return T.V[id] if ~(id:=T.find_node(key)) else T.e

    def pop(T, key):
        if ~(id:=T.find_node(key)): T.del_node(id); return T.V[id]
        return T.e

    def __delitem__(T, key):
        if ~(id:=T.find_node(key)): T.del_node(id)
    
    def __setitem__(T, key, val):
        if ~(id:=T.find_node(key)): T.set_node(id, val)
        else: T.insert(key, val)
    
    def __getitem__(T, key):
        if isinstance(key, int): return T.get(key)
        elif isinstance(key, slice): return T.prod(key.start, key.stop)
    
    def __contains__(T, key): return 0 <= T.find_node(key)

    def __len__(T): return T.cnt

    def new_node(T, key, val):
        id = len(T.K)
        T.K.append(key); T.V.append(val); T.A.append(val)
        T.P.append((T.P[-1] * 1103515245 + 12345) & 0x7fffffff)
        T.par.append(-1); T.sub.append(-1); T.sub.append(-1)
        T.cnt += 1
        return id

    def find_node(T, key: int):
        id = T.sub[T.root<<1]
        while ~id and T.K[id] != key: id = T.sub[id<<1|(T.K[id]<key)]
        return id
    
    def insert_node(T, sid, nid):
        while ~T.sub[sid] and T.P[id:=T.sub[sid]]<T.P[nid]:sid=id<<1|(T.K[id]<T.K[nid])
        id = T.sub[sid]; T.attach_node(sid, nid)
        if ~id: T.split_node(id, nid)
        T._repair()
    
    def split_node(T, id, nid):
        l, r = nid<<1, nid<<1|1
        while ~id:
            if T.K[id] < T.K[nid]: T.attach_node(l, id); id = T.sub[l := id<<1|1]
            else: T.attach_node(r, id); id = T.sub[r := id<<1]
        T.st.append(l>>1); T.st.append(r>>1)
        T.sub[l] = T.sub[r] = -1
        T._repair()

    def set_node(T, id: int, val): T.V[id] = val; T._propagate(id)

    def merge_nodes(T, sid: int, l: int, r: int):
        while ~l and ~r:
            if T.P[l]<T.P[r]: T.attach_node(sid, l); l = T.sub[sid := l<<1|1]
            else: T.attach_node(sid, r); r = T.sub[sid := r<<1]
        if ~l: T.attach_node(sid, l)
        elif ~r: T.attach_node(sid, r)
        T._repair()

    def del_node(T, id: int):
        sid, l, r = T.par[id], T.sub[id<<1], T.sub[id<<1|1]
        T.detach_node(id)
        T.merge_nodes(sid, l, r)
        T.cnt -= 1
    
    def detach_node(T, id: int):
        assert ~T.par[id]
        T.st.append(T.par[id]>>1)
        T.sub[T.par[id]] = T.par[id] = -1
    
    def attach_node(T, sid: int, id: int):
        T.st.append(sid>>1)
        T.sub[sid], T.par[id] = id, sid

    @classmethod
    def reserve(cls, hint: int):
        hint += 1
        reserve(cls.K, hint); reserve(cls.V, hint); reserve(cls.A, hint); reserve(cls.P, hint)
        reserve(cls.par, hint); reserve(cls.sub, hint << 1); reserve(cls.st, hint.bit_length() << 1)
    
    def _update(T, id):
        T.A[id] = T.V[id]
        if ~(l := T.sub[id << 1]): T.A[id] = T.op(T.A[l], T.A[id])
        if ~(r := T.sub[id<<1|1]): T.A[id] = T.op(T.A[id], T.A[r])
        
    def _propagate(T, id):
        while ~T.par[id]: T._update(id); id = T.par[id]>>1
        T._update(id)

    def _repair(T):
        if T.st:
            while T.st: T._update(id := T.st.pop())
            if id != T.root: T._propagate(T.par[id]>>1)
    
    def _validate(T, id = None):
        if id is None:
            assert T.all_prod() == (acc := T._validate(id) if ~(id := T.sub[T.root<<1]) else T.e)
            return acc
        assert ~T.par[id]
        assert T.sub[T.par[id]] == id
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
