# verification-helper: PROBLEM https://atcoder.jp/contests/abc184/tasks/abc245_f

def main():
    N, M = read(tuple[int,int])
    G = read(DiGraph[N,M])
    ans = sum(label_cycles(G))
    print(ans)

def label_cycles(G):
    state = [0 for _ in range(G.N)]
    stack = list(range(G.N))
    cyc = [False]*G.N

    while stack:
        u = stack.pop()
        match state[u]:
            case 0:
                stack.append(u)
                for v in G[u]:
                    match state[v]:
                        case 0:
                            stack.append(v)
                        case 1:
                            cyc[v] = True
            case 1:
                cyc[u] = any(cyc[v] for v in G[u])
        state[u] += 1
    return cyc


from cp_library.alg.graph.digraph_cls import DiGraph
from cp_library.io.read_specs_fn import read

if __name__ == "__main__":
    main()