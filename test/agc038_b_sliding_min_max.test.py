# verification-helper: PROBLEM https://atcoder.jp/contests/agc038/tasks/agc038_b

def main():
    N, K = read(tuple[int,int])
    P = read(list[int])
    win = SlidingMinMax(maxlen=K+1)
    for i in range(K):
        win.append(P[i])
    ans = 1 - (unchanged := len(win.minq) == K)
    for i in range(K,N):
        p = win.popleft()
        win.append(P[i])
        unchanged |= len(win.minq) == K
        if len(win.minq) != K and (p > win.min or P[i] < win.max):
            ans += 1
        
    ans += unchanged
    write(ans)
    
from cp_library.ds.slidingminmax_cls import SlidingMinMax
from cp_library.io.read_fn import read
from cp_library.io.write_fn import write

if __name__ == "__main__":
    main()