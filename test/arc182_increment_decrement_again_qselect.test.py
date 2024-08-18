# verification-helper: PROBLEM https://atcoder.jp/contests/arc182/tasks/arc182_d

from cp_library.alg.divcon.qselect import kth_element

def rint(shift=0, base=10):
    return [int(x, base) + shift for x in input().split()]

N, M = rint()
A = rint()
B = rint()

if M == 2:
    print(0 if A == B else -1)
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
median = kth_element([c-a for a,c in zip(A,C)], N//2)
ans = float('inf')
for i in range(median//M,median//M+2):
    now=0
    for j in range(N):
        now+=abs(A[j]+i*M-C[j])
    ans=min(ans,now)
print(ans)