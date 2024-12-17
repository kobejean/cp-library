# verification-helper: PROBLEM https://atcoder.jp/contests/abc202/tasks/abc202_e


from bisect import bisect_left

def main():
    N = read(int)
    V = read(list[-1])
    U = list(range(1,N))
    G = Tree(N, U, V)
    
    depth = [0]*N
    depth[0] = -1
    cnt = [[] for _ in range(N)]
    time = 0
    tin = [0]*N
    tout = [0]*N
    events, U = G.dfs_enter_leave(0)
    for i in range(len(events)):
        u = U[i]
        match events[i]:
            case DFSEvent.ENTER:
                depth[u] = d = depth[G.par[u]]+1
                tin[u] = time
                cnt[d].append(time)
                time += 1
            case DFSEvent.LEAVE:
                tout[u] = time
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