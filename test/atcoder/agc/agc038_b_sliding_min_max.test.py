# verification-helper: PROBLEM https://atcoder.jp/contests/agc038/tasks/agc038_b

from cp_library.alg.graph.perm_graph_cls import PermGraph

def main():
    N, K = read(tuple[int,int])
    P = read(PermGraph[N,0])
    win = SlidingMinMax(maxlen=K)
    win.extend(P[:K])
    ans = 1 - (unchanged := len(win.minq) == K)
    for i in range(K,N):
        p = win.popleft()
        win.append(P[i])
        unchanged |= (is_sorted:=len(win.minq) == K)
        ans += not is_sorted and (p > win.min or P[i] < win.max)
        
    ans += unchanged
    write(ans)
    
from cp_library.ds.slidingminmax_cls import SlidingMinMax
from cp_library.io.read_fn import read
from cp_library.io.write_fn import write

if __name__ == "__main__":
    main()