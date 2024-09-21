import cp_library.math.mod.__header__

def mat_add(A, B, mod):
    return [[(Ai[j] + Bi[j]) % mod for j in range(len(Ai))] for Ai,Bi in zip(A,B)]
