'''
  You must see with eyes unclouded by hate.  See the good in    
  that which is evil, and the evil in that which is good.       
  Pledge yourself to neither side, but vow instead to preserve  
  the balance that exists between the two. - Hayao Miyazaki     
╺━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╸
                     Submitted by: kobejean                     
'''
# verification-helper: PROBLEM https://atcoder.jp/contests/abc294/tasks/abc294_g



def main():
    N = read(int)
    T = read(TreeWeighted[N])

    hld = HeavyLightDecomposition(T)
    W = [hld.weights[i] for i in hld.order]
    bit = BinaryIndexTree(W)

    Q = read(int)
    for query in read(list[tuple[int, int, int], Q]):
        match query:
            case 1, i, w:
                i -= 1  # Convert to 0-based index
                u, v, _ = T.E[i]
                # Find child node in edge (u, v)
                if hld.par[u] == v:
                    node = u
                else:
                    node = v
                idx = hld.pos[node]
                bit.set(idx, w)
            case 2, u, v:
                u, v = u - 1, v - 1
                ans = sum(bit.range_sum(l,r) for l,r in hld.path(u,v, True))
                print(ans)

from cp_library.ds.bit_cls import BinaryIndexTree
from cp_library.alg.tree.tree_weighted_cls import TreeWeighted
from cp_library.alg.tree.heavy_light_decomposition_cls import HeavyLightDecomposition
from cp_library.io.read_specs_fn import read

if __name__ == "__main__":
    main()