import cp_library.ds.__header__

from heapq import (
    _heapify_max as heapify_max, 
    _heappop_max as heappop_max, 
    _siftdown_max as heapsiftdown_max,
    _siftup_max as heapsiftup_max,
    _siftdown as heapsiftdown,
    _siftup as heapsiftup
)

def heappush_max(heap, item):
    """Push item onto heap, maintaining the heap invariant."""
    heap.append(item)
    heapsiftdown_max(heap, 0, len(heap)-1)

def heapreplace_max(heap, item):
    """Pop and return the current largest value, and add the new item.

    This is more efficient than heappop_max() followed by heappush_max(), and can be
    more appropriate when using a fixed-size heap.  Note that the value
    returned may be larger than item!  That constrains reasonable uses of
    this routine unless written as part of a conditional replacement:

        if item > heap[0]:
            item = heapreplace_max(heap, item)
    """
    returnitem = heap[0]
    heap[0] = item
    heapsiftup_max(heap, 0)
    return returnitem