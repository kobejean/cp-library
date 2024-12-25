# verification-helper: PROBLEM https://atcoder.jp/contests/abc202/tasks/abc202_e


from bisect import bisect_left

def main():
    N = read(int)
    V = read(list[-1])
    U = list(range(1,N))
    G = Tree(N, U, V)

    depth = [0]*N
    cnt = [[] for _ in range(N)]

    time = 0
    tin = [0]*N
    tout = [0]*N
    
    def down(p,u):
        depth[u] = depth[p]+1

    def enter(u):
        nonlocal time
        tin[u] = time
        cnt[depth[u]].append(time)
        time += 1

    def leave(u):
        nonlocal time
        tout[u] = time
        time += 1

    G.dfs(0, down_fn=down, enter_fn=enter, leave_fn=leave)

    Q = read(int)
    for u,d in read(list[tuple[-1,int],Q]):
        ans = bisect_left(cnt[d], tout[u]) - bisect_left(cnt[d], tin[u])
        write(ans)

from cp_library.alg.tree.fast.tree_cls import Tree
from cp_library.io.read_fn import read
from cp_library.io.write_fn import write

if __name__ == "__main__":
    main()