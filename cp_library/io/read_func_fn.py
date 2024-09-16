
def read(func=0, /, *a, **k):
    if callable(func): return [func(s, *a, **k) for s in input().split()]
    return [int(s, *a, **k)+func for s in input().split()]
