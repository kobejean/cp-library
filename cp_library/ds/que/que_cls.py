import cp_library.ds.__header__
import cp_library.ds.que.__header__

class Que:
    def __init__(que, v = None): que.q = elist(v) if isinstance(v, int) else list(v) if v else []; que.h = 0
    def push(que, item): que.q.append(item)
    def pop(que): que.h = (h := que.h) + 1; return que.q[h]
    def extend(que, items): que.q.extend(items)
    def __getitem__(que, i: int): return que.q[que.h+i]
    def __len__(que): return que.q.__len__() - que.h
from cp_library.ds.elist_fn import elist