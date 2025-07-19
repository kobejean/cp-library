import cp_library.__header__
import cp_library.alg.__header__
import cp_library.alg.iter.__header__

def majority_vote(A: list[int], default = None):
    T = len(A) >> 1
    cnt = val = 0
    for a in A:
        if cnt: cnt += 1 if a == val else -1
        else: cnt, val = 1, a
    return val if cnt and A.count(val) > T else default