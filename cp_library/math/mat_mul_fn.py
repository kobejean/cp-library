import cp_library.math.__init__

def mat_mul(A,B):
    assert len(A[0]) == len(B)
    R = [[0]*len(B[0]) for _ in range(len(A))] 
    for i,Ri in enumerate(R):
        for k,Aik in enumerate(A[i]):
            for j,Bkj in enumerate(B[k]):
                Ri[j] = Bkj*Aik + Ri[j]  
    return R 
