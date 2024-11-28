# verification-helper: PROBLEM https://atcoder.jp/contests/abc249/tasks/abc249_f



def main():
    N, K = read(tuple[int, ...])
    ops = read(list[tuple[int, ...], N])
    diff = []
    x = 0
    for t, y in ops:
        match t:
            case 1:
                diff.append(y - x)
                x = y
            case 2:
                diff.append(y)
                x += y

    S = BadOps(K, x)
    if K:
        for i,(t,y) in rev_enumerate(ops):
            match t:
                case 1:
                    S.K -= 1
                    S.added(diff[i])
                    if S.K == 0: break
                case 2:
                    if y < 0:
                        S.push(y)
    write(S.ans)
                

from cp_library.io.read_fn import read
from cp_library.io.write_fn import write
from cp_library.alg.iter.rev_enumerate_fn import rev_enumerate
from cp_library.ds.min_k_heap_cls import MinKHeap

class BadOps(MinKHeap[int]):
    def __init__(self, K: int, x: int):
        super().__init__(K)
        self.x = x
        self.ans = x

    def added(self, y):
        self.x -= y
        self.ans = max(self.ans, self.x)
    
    def removed(self, y):
        self.x += y
        self.ans = max(self.ans, self.x)

if __name__ == "__main__":
    main()