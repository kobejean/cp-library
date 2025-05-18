# verification-helper: PROBLEM https://atcoder.jp/contests/abc293/tasks/abc293_g


def main():
    N, Q = read(tuple[int, ...])
    A = read(list[int])
    mo = read(TripletQueries[Q, N])
    write(*mo.solve(A), sep='\n')

from cp_library.alg.dp.mo_cls import Mo
from cp_library.io.read_fn import read
from cp_library.io.write_fn import write

class TripletQueries(Mo):
    cnt = [0]*200001      
    pairs = [0]*200001    
    triples = 0
    A: list[int] = None

    def add(mo, i):
        v = mo.A[i]
        mo.triples += mo.pairs[v]    
        mo.pairs[v] += mo.cnt[v]     
        mo.cnt[v] += 1 
    
    def remove(mo, i):
        v = mo.A[i]
        mo.cnt[v] -= 1 
        mo.pairs[v] -= mo.cnt[v]     
        mo.triples -= mo.pairs[v]   

    def answer(mo, i, l, r):
        return mo.triples 
    
    def solve(mo, A):
        mo.A = A
        return super().solve()

if __name__ == "__main__":
    main()