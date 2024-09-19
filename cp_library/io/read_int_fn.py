import cp_library.io.__init__

def read(shift=0, base=10):
    return [int(s, base) + shift for s in input().split()]
