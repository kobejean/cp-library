# verification-helper: PROBLEM https://atcoder.jp/contests/abc293/tasks/abc293_g


def main():
    N, Q = read(tuple[int, ...])
    A = read(list[int])
    mo = read(TripletQueries[Q, N])
    
    print(*mo.solve(A), sep='\n')

from cp_library.alg.dp.mo_cls import Mo
from cp_library.io.read_specs_fn import read

class TripletQueries(Mo):
    cnt = [0]*200001      
    pairs = [0]*200001    
    triples = 0
    A: list[int] = None

    def add(self, i):
        v = self.A[i]
        self.triples += self.pairs[v]    
        self.pairs[v] += self.cnt[v]     
        self.cnt[v] += 1 
    
    def remove(self, i):
        v = self.A[i]
        self.cnt[v] -= 1 
        self.pairs[v] -= self.cnt[v]     
        self.triples -= self.pairs[v]   

    def answer(self, i, l, r):
        return self.triples 
    
    def solve(self, A):
        self.A = A
        return super().solve()

if __name__ == "__main__":
    main()