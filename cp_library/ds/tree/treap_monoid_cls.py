import cp_library.__header__
import cp_library.ds.__header__
from cp_library.ds.reserve_fn import reserve
import cp_library.ds.tree.__header__

class TreapMonoid:
    __slots__ = 'key', 'val', 'acc', 'prior', 'sub', 'e', 'op', 'rand', 'st1', 'st2'
    def __init__(T, e, op):
        T.key = [-1]
        T.val = [e]
        T.acc = [e]
        T.prior = [42]
        T.sub = [-1, -1]
        T.e = e
        T.op = op
        T.st1, T.st2 = [], []

    def reserve(T, hint: int):
        hint += 1
        reserve(T.key, hint)
        reserve(T.val, hint)
        reserve(T.acc, hint)
        reserve(T.prior, hint)
        reserve(T.sub, hint << 1)

    def new_node(T, key, value, left = -1, right = -1):
        id = len(T.key)
        T.key.append(key)
        T.val.append(value)
        T.acc.append(value)
        T.prior.append((T.prior[-1] * 1103515245 + 12345) & 0x7fffffff)
        T.sub.append(left); T.sub.append(right)
        return id
    
    def update(T, id):
        T.acc[id] = T.val[id]
        if (l := T.sub[id << 1]) >= 0:
            T.acc[id] = T.op(T.acc[l], T.acc[id])
        if (r := T.sub[id<<1|1]) >= 0:
            T.acc[id] = T.op(T.acc[id], T.acc[r])

    def split(T, id, key, l, r):
        while True:
            if id < 0: T.sub[l] = T.sub[r] = -1; break
            if T.key[id] < key:
                m = id << 1 | 1
                T.st1.append((id, l))
                id, l, r = T.sub[m], m, r
            else:
                m = id << 1
                T.st1.append((id, r))
                id, l, r = T.sub[m], l, m
        while T.st1:
            id, sid = T.st1.pop()
            T.sub[sid] = id
            T.update(id)
        # if id < 0: T.sub[l] = T.sub[r] = -1; return
        # elif T.key[id] < key:
        #     m = id << 1 | 1
        #     T.split(T.sub[m], key, m, r); T.sub[l] = id
        # else:
        #     m = id << 1
        #     T.split(T.sub[m], key, l, m); T.sub[r] = id
        # T.update(id)

    def insert(T, sid, nid):
        while True:
            if T.sub[sid] < 0:
                T.sub[sid] = nid; break
            elif T.prior[nid] < T.prior[id := T.sub[sid]]:
                T.split(id, T.key[nid], nid<<1, nid<<1|1); T.sub[sid] = nid; T.update(nid); break
            else:
                T.st2.append(id)
                sid, nid = id << 1 | (T.key[id] < T.key[nid]), nid
        while T.st2:
            T.update(T.st2.pop())

        # if T.sub[sid] < 0: T.sub[sid] = nid
        # elif T.prior[nid] < T.prior[id := T.sub[sid]]:
        #     T.split(id, T.key[nid], nid<<1, nid<<1|1); T.sub[sid] = nid; T.update(nid)
        # else:
        #     T.insert(id << 1 | (T.key[id] < T.key[nid]), nid); T.update(id)

    def add(T, key, value):
        T.insert(0, T.new_node(key, value))

    def all_prod(T):
        return T.acc[T.sub[0]] if T.sub[0] >= 0 else T.e
