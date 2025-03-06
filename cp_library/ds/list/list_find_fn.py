import sys
import cp_library.ds.list.__header__

def list_find(lst: list, value, start = 0, stop = sys.maxsize):
    try:
        return lst.index(value, start, stop)
    except:
        return -1