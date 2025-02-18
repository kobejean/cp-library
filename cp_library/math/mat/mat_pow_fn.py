import cp_library.math.__header__

def mat_pow(A,K):
    R = A if K & 1 else mat_id(len(A))
    for i in range(1,K.bit_length()):
        A = mat_mul(A,A) 
        if K >> i & 1: R = mat_mul(R,A) 
    return R 

from cp_library.math.mat.mat_mul_fn import mat_mul
from cp_library.math.mat.mat_id_fn import mat_id