# verification-helper: PROBLEM https://atcoder.jp/contests/abc202/tasks/abc202_e


from bisect import bisect_left

def main():
    N = read(int)
    P = read(list[-1])
    E = []
    for u,p in enumerate(P, start=1):
        E.append((p,u))

    cnt = [[] for _ in range(N)]

    G = Tree(N, E)
    depth = [0]*N
    for p,u in G.dfs_topdown():
        depth[u] = depth[p]+1
    time = 0
    tin = [0]*N
    tout = [0]*N
    
    for t, u in G.dfs_enter_leave(0):
        match t:
            case DFSEvent.ENTER:
                tin[u] = time
                cnt[depth[u]].append(time)
            case DFSEvent.LEAVE:
                tout[u] = time
        time += 1
    Q = read(int)
    for u,d in read(list[tuple[-1,int],Q]):
        ans = bisect_left(cnt[d], tout[u]) - bisect_left(cnt[d], tin[u])
        write(ans)

    
from cp_library.alg.graph.dfs_options_cls import DFSEvent
from cp_library.alg.tree.tree_cls import Tree
from cp_library.io.read_fn import read
from cp_library.io.write_fn import write

if __name__ == "__main__":
    main()