# verification-helper: PROBLEM https://atcoder.jp/contests/arc182/tasks/arc182_d

def main():
    N, M = read()
    A = read()
    B = read()

    if M == 2:
        write(0 if A == B else -1)
        exit()

    def rel(x,y):
        return max(-1,min(x-y,1))

    C = [B[0]]

    for i in range(1,N):
        c = C[-1] - C[-1]%M + B[i]
        for Ci in range(c-M,c+2*M,M):
            if rel(A[i-1],A[i]) == rel(C[-1],Ci) and abs(C[-1]-Ci)<M:
                C.append(Ci)
                break
    median = qselect([c-a for a,c in zip(A,C)], N//2)
    ans = inf
    for i in range(median//M,median//M+2):
        now=0
        for j in range(N):
            now+=abs(A[j]+i*M-C[j])
        ans=min(ans,now)
    write(ans)

from math import inf
from cp_library.alg.divcon.qselect_fn import qselect
from cp_library.io.read_int_fn import read
from cp_library.io.write_fn import write
    
if __name__ == '__main__':
    main()