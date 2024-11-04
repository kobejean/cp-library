# verification-helper: PROBLEM https://atcoder.jp/contests/abc184/tasks/abc184_f


from bisect import bisect_left

def solve(N, T, A):
    if N <= 5:
        A = sorted(subset_sum(A))
        return max_lim(A, T)
    else:
        mid = N//2
        B = sorted(subset_sum(A[mid:]))
        C = sorted(subset_sum(A[:mid]))
        ans = 0
        for b in B:
            if b > T: break
            ans = max(ans, max_lim(C, T-b)+b)
        return ans
    
def max_lim(X, lim):
    pi = bisect_left(X, lim+1)-1
    if 0 <= pi < len(X):
        return X[pi]
    return 0

def main():
    N, T = read(tuple[int, ...])
    A = sorted(read(list[int, N]))
    ans = solve(N, T, A)
    print(ans)
    

from cp_library.io.read_specs_fn import read
from cp_library.math.subset_sum_fn import subset_sum

if __name__ == "__main__":
    main()