# verification-helper: PROBLEM https://atcoder.jp/contests/abc202/tasks/abc202_e

from bisect import bisect_left

def main():
    N = read(int)
    U = list(range(1,N))
    V = read(list[-1])
    G = Tree(N, U, V)
    cnt = [[] for _ in range(N)]
    time = 0
    tin, tout = [0]*N, [0]*N
    depth = -1
    for event, u in G.dfs_enter_leave(0):
        match event:
            case DFSEvent.ENTER:
                depth += 1
                tin[u] = time
                cnt[depth].append(time)
            case DFSEvent.LEAVE:
                tout[u] = time
                depth -= 1
        time += 1
    Q = read(int)
    for u,d in read(list[tuple[-1,int],Q]):
        ans = bisect_left(cnt[d], tout[u]) - bisect_left(cnt[d], tin[u])
        write(ans)

    
from cp_library.alg.graph.dfs_options_cls import DFSEvent
from cp_library.alg.tree.fast.tree_cls import Tree
from cp_library.io.read_fn import read
from cp_library.io.write_fn import write

if __name__ == "__main__":
    main()