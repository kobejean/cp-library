# verification-helper: PROBLEM https://atcoder.jp/contests/abc293/tasks/abc293_g


def main():
    N, Q = read()
    A = read(list[int])
    ops, *opands = read(QueriesMoOps[Q, N])
    
    # State for counting triples
    cnt = [0]*200001        
    triples = 0           
    ans = [0]*Q
    
    for j in range(len(ops)):
        if ops[j] in MoOp.ADD:
            for i in range(opands[0][j], opands[1][j], opands[2][j]):
                v = A[i]
                c = cnt[v] 
                triples += c*(c-1)  
                cnt[v] += 1   
        elif ops[j] in MoOp.REMOVE:
            for i in range(opands[0][j], opands[1][j], opands[2][j]):
                v = A[i]
                cnt[v] -= 1       
                c = cnt[v]      
                triples -= c*(c-1)    
        else:
            i = opands[0][j]
            ans[i] = triples >> 1
    
    write(*ans, sep='\n')

from cp_library.ds.queries_mo_ops_cls import QueriesMoOps, MoOp
from cp_library.io.read_fn import read
from cp_library.io.write_fn import write

if __name__ == "__main__":
    main()