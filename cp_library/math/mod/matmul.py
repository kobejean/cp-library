def matmul(A,B,mod):
    assert len(A[0]) == len(B)
    N = len(A)
    M = len(B)
    ret = [[0]*M for _ in range(N)] 
    for i,reti in enumerate(ret):
        for k,a_ik in enumerate(A[i]):
            for j,b_kj in enumerate(B[k]):
                reti[j] = (reti[j] + a_ik*b_kj) % mod  

    return ret 