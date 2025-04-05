import cp_library.__header__
import cp_library.ds.__header__
import cp_library.ds.heap.__header__

class IntervalHeap:
    def __init__(heap, arr: list):
        heap._d = arr
        for k in range(len(arr)): heap._up(k)

    def push(heap, item):
        heap._d.append(item)
        heap._up(len(heap._d)-1)

    def pop_min(heap):
        item = heap._d.pop()
        if heap._d: item, heap._d[0] = heap._d[0], item; heap._down(0)
        return item

    def pop_max(heap):
        item = heap._d.pop()
        if len(heap._d) >= 2: item, heap._d[1] = heap._d[1], item; heap._down(1)
        return item

    def _up(heap, k):
        v = heap._d[k]
        if k&1 and heap._d[k] < heap._d[k-1]: heap._d[k] = heap._d[k-1]; k ^= 1
        while 0 <= (p := (k>>1)-1&~1) and v < heap._d[p]: heap._d[k], k = heap._d[p], p
        while 0 <= (p := (k>>1)-1|1) and heap._d[p] < v: heap._d[k], k = heap._d[p], p
        heap._d[k] = v

    def _down(heap, k):
        n, v, rt = len(d := heap._d)-2, d[k], k
        if k & 1: # max heap
            c = 2*k+1
            while c < n and v < d[c := c+2 if d[c] < d[c+2] else c]: d[k], k, c = d[c], c, c<<1|1
            if c < n+2 and v < d[c]: d[k], k = d[c], c
            d[k] = v
            if v < d[k-1]:
                d[k] = d[k-1]; k ^= 1
                while rt <= (p := (k>>1)-1&~1) and v < d[p]: d[k], k = d[p], p
                d[k] = v
        else: # min heap
            c = (k+1)<<1
            while c < n and d[c := c+2 if d[c+2] < d[c] else c] < v: d[k], k, c = d[c], c, (c+1)<<1
            if c < n+2 and d[c] < v: d[k], k = d[c], c
            d[k] = v
            if k+1 < n+2 and d[k+1] < d[k]:
                d[k] = d[k+1]; k ^= 1
                while rt <= (p := (k>>1)-1|1) and d[p] < v: d[k], k = d[p], p
                d[k] = v