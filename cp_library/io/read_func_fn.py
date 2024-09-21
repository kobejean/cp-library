import cp_library.io.__header__

def read(func=0, /):
    if callable(func): return [func(s) for s in input().split()]
    return [int(s)+func for s in input().split()]
