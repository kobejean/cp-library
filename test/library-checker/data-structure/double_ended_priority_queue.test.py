# verification-helper: PROBLEM https://judge.yosupo.jp/problem/double_ended_priority_queue

def main():
    N, Q = rd()
    S = rdl(N)
    reserve(S, N+Q)
    heap = IntervalHeap(S)

    for _ in range(Q):
        t = rd()
        if t[0] == 0: heap.push(t[1])
        elif t[0] == 1: wtn(heap.pop_min())
        else: wtn(heap.pop_max())

from cp_library.ds.heap.interval_heap_cls import IntervalHeap
from cp_library.ds.list.reserve_fn import reserve
from cp_library.io.fast_io_fn import rd, rdl, wtn

if __name__ == '__main__':
    main()
