# verification-helper: PROBLEM https://atcoder.jp/contests/abc202/tasks/abc202_e


from bisect import bisect_left

def main():
    N = read(int)
    U = list(range(1,N))
    V = read(list[-1])
    G = Tree(N, U, V)
    
    depth = [0]*N
    depth[0] = -1
    cnt = [[] for _ in range(N)]
    time = 0
    tin = [0]*N
    tout = [0]*N
    for event, u in G.dfs_enter_leave(0):
        match event:
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