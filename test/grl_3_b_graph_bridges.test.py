# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/all/GRL_3_B

def main():
    N, M = read()
    G = read(Graph[N,M,0])
    E = [(min(u,v), max(u,v)) for u,v in G.E]
    B = sorted([E[e] for e in G.bridges()])
    for s,t in B:
        write(s,t)

from cp_library.alg.graph.graph_cls import Graph
from cp_library.io.read_fn import read
from cp_library.io.write_fn import write

if __name__ == '__main__':
    main()