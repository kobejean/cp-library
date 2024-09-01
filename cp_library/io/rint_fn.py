def rint(shift=0, base=10):
    return [int(x, base) + shift for x in input().split()]