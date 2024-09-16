from heapq import _heapify_max as heapify_max, _heappop_max as heappop_max, _siftdown_max as heapsiftdown_max

def heappush_max(heap, item):
    """Push item onto heap, maintaining the heap invariant."""
    heap.append(item)
    heapsiftdown_max(heap, 0, len(heap)-1)