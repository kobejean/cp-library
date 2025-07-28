import cp_library.__header__
import cp_library.ds.__header__
import cp_library.ds.heap.__header__
from cp_library.ds.heap.heapsiftup_fn import heapsiftup

def heapify(x: list):
    for i in reversed(range(len(x)//2)): heapsiftup(x, i)