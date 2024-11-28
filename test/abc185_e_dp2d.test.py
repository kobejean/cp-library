# verification-helper: PROBLEM https://atcoder.jp/contests/abc185/tasks/abc185_e

def main():
    N, M = read(tuple[int, ...])
    A = read(list[int,N])
    B = read(list[int,M])
    
    dp = DynamicProgramming2D(N+1, M+1)
    dp[0,0] = 0
    
    transitions = [
        Match(1,1,A,B),    # match/mismatch
        Edit(0,1),         # insert
        Edit(1,0),         # delete
    ]
    
    dp.solve(transitions)
    write(dp[N,M])
    

from cp_library.io.read_fn import read
from cp_library.io.write_fn import write
from cp_library.alg.dp.dp2d_cls import DynamicProgramming2D, Transition2D

from dataclasses import dataclass

@dataclass
class Match(Transition2D[int]):
    A: list[int]
    B: list[int]

    def __call__(self, i: int, j: int, src_val: int, dest_val: int) -> int:
        return min(dest_val, src_val + (self.A[i] != self.B[j]))

class Edit(Transition2D[int]):
    def __call__(self, i: int, j: int, src_val: int, dest_val: int) -> int:
        return min(dest_val, src_val + 1)
    
if __name__ == "__main__":
    main()