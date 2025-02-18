import cp_library.math.mod.__header__

def mat_pow(A,K,mod):
    N = len(A)
    ret = A if K & 1 else mat_id(N)
    for i in range(1,K.bit_length()):
        A = mat_mul(A,A,mod) 
        if K >> i & 1:
            ret = mat_mul(ret,A,mod) 
    return ret 

from cp_library.math.mat.mod.mat_mul_fn import mat_mul
from cp_library.math.mat.mat_id_fn import mat_id