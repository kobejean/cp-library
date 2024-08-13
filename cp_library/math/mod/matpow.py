from cp_library.math.mod.matmul import mat_mul
from cp_library.math.mod.matid import mat_id

def mat_pow(A,K,mod):
    N = len(A)
    ret = A if K & 1 else mat_id(N)
    for i in range(1,K.bit_length()):
        A = mat_mul(A,A,mod) 
        if K >> i & 1:
            ret = mat_mul(ret,A,mod) 
    return ret 
