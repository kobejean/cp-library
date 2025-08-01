import cp_library.__header__
import cp_library.math.__header__
import cp_library.math.linalg.__header__
import cp_library.math.linalg.mat.__header__
import cp_library.math.linalg.mat.mod.__header__

def mat_pow(A,K,mod):
    N = len(A)
    ret = A if K & 1 else mat_id(N)
    for i in range(1,K.bit_length()):
        A = mat_mul(A,A,mod) 
        if K >> i & 1:
            ret = mat_mul(ret,A,mod) 
    return ret 
from cp_library.math.linalg.mat.mod.mat_mul_fn import mat_mul
from cp_library.math.linalg.mat.mat_id_fn import mat_id