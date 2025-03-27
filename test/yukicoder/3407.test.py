# verification-helper: PROBLEM https://yukicoder.me/problems/3407

def main():
    N = read(int)
    T = read(AuxTreeWeighted[N,0])
    Q = read(int)
    for _ in range(Q):
        k, *X = read() 
        V, post = T.tree(X)
        ans = sum(T.Wa[i] for i in post)
        write(ans)
    

from cp_library.alg.tree.fast.aux_tree_weighted_cls import AuxTreeWeighted
from cp_library.io.read_fn import read
from cp_library.io.write_fn import write

if __name__ == '__main__':
    main()
