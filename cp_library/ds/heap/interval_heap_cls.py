import cp_library.__header__
import cp_library.ds.__header__
import cp_library.ds.heap.__header__

class IntervalHeap:
    def __init__(heap, x):
        super().__init__()
        heap._d = x
        for i in range(len(x)): heap._up(0, i, i+1)

    def push(heap, v):
        heap._d.append(v)
        heap._up(0, len(heap._d)-1, len(heap._d))

    def pop_min(heap):
        v = heap._d.pop()
        if heap._d: v, heap._d[0] = heap._d[0], v; heap._up(0, heap._down(0), len(heap._d))
        return v

    def pop_max(heap):
        v = heap._d.pop()
        if len(heap._d) >= 2: v, heap._d[1] = heap._d[1], v; heap._up(1, heap._down(1), len(heap._d))
        return v

    def _up(heap, rt, k, n):
        v = (d := heap._d)[k]
        if k|1 < n and d[k|1] < d[k&~1]: d[k] = d[k^1]; k ^= 1
        while rt <= (p := (k>>1)-1&~1) and v < d[p]: d[k], k = d[p], p
        while rt <= (p := (k>>1)-1|1) and d[p] < v: d[k], k = d[p], p
        d[k] = v

    def _down(heap, k):
        n, v = len(d := heap._d), d[k]
        if k & 1: # max heap
            c = 2*k+1
            while c < n:
                if c+2 < n and d[c] < d[c+2]: c += 2
                if v < d[c]: d[k], k, c = d[c], c, 2*c+1
                else: break
        else: # min heap
            c = 2*k+2
            while c < n:
                if c+2 < n and d[c+2] < d[c]: c += 2
                if d[c] < v: d[k], k, c = d[c], c, 2*c+2
                else: break
        d[k] = v
        return k
