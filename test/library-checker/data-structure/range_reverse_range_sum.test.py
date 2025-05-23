# verification-helper: PROBLEM https://judge.yosupo.jp/problem/range_reverse_range_sum

from operator import add

def main():
    N, Q = read()
    TreapMonoidReversibe.reserve(1+N+Q)
    T = TreapMonoidReversibe(add, 0)
    T.build(read())
    for _ in range(Q):
        t, l, r = read()
        if t == 0:
            T.reverse(l,r)
        else:
            write(T.prod(l,r))

from cp_library.ds.tree.bst.treap_monoid_reversible_cls import TreapMonoidReversibe
from cp_library.io.read_fn import read
from cp_library.io.write_fn import write

if __name__ == '__main__':
    main()
