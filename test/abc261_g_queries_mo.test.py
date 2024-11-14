# verification-helper: PROBLEM https://atcoder.jp/contests/abc293/tasks/abc293_g


def main():
    N, Q = read()
    A = read()
    queries = read(QueriesMoOps[Q, N])
    
    # State for counting triples
    cnt = [0]*200001        
    triples = 0           
    ans = [0]*Q
    
    for op in queries:
        match op:
            case (MoOp.ADD_RIGHT | MoOp.ADD_LEFT, start, stop, step):
                for i in range(start, stop, step):
                    v = A[i]
                    c = cnt[v] 
                    triples += c*(c-1)  
                    cnt[v] += 1   
            case (MoOp.REMOVE_RIGHT | MoOp.REMOVE_LEFT, start, stop, step):
                for i in range(start, stop, step):
                    v = A[i]
                    cnt[v] -= 1       
                    c = cnt[v]      
                    triples -= c*(c-1)    
            case (MoOp.ANSWER, i, _, _):
                ans[i] = triples >> 1
    
    print(*ans, sep='\n')

from cp_library.ds.queries_cls import QueriesMoOps, MoOp
from cp_library.io.read_specs_fn import read

if __name__ == "__main__":
    main()