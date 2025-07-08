# verification-helper: PROBLEM https://atcoder.jp/contests/abc202/tasks/abc202_e


from bisect import bisect_left

def main():
    N = read(int)
    P = read(list[-1])
    U, V = [], []
    for u,p in enumerate(P, start=1):
        U.append(p); V.append(u)
    cnt = [[] for _ in range(N)]
    T = Tree(N, U, V)
    depth = [0]*N
    for i in T.dfs_topdown():
        p, u = T.Ua[i], T.Va[i]
        depth[u] = depth[p]+1
    time = 0
    tin = [0]*N
    tout = [0]*N
    
    for t, u in T.dfs_enter_leave(0):
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
from cp_library.alg.tree.fast.tree_cls import Tree
from cp_library.io.read_fn import read
from cp_library.io.write_fn import write

if __name__ == "__main__":
    main()