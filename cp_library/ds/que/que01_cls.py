import cp_library.ds.__header__
import cp_library.ds.que.__header__

class Que01:
    def __init__(que, hint=None):
        if hint: que.q0, que.q1 = elist(hint), elist(hint)
        else: que.q0, que.q1 = [], []
    def push0(que, item): que.q0.append(item)
    def push1(que, item): que.q1.append(item)
    def pop(que):
        if que.q0: return que.q0.pop()
        que.q0, que.q1 = que.q1, que.q0
        return que.q0.pop()
    def __len__(que): return len(que.q0) + len(que.q1)
from cp_library.ds.list.elist_fn import elist