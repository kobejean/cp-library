# verification-helper: PROBLEM https://atcoder.jp/contests/abc362/tasks/abc362_g

def main():
    S = read(str)
    Q = read(int)
    A = AhoCorasick()
    queries = []
    for _ in range(Q):
        T = input()
        A.add(T)
        queries.append(T)

    freq_dict = A.freq_table(S)
    for query in queries:
        write(freq_dict[query])

from cp_library.io.read_fn import read
from cp_library.io.write_fn import write
from cp_library.ds.tree.ahocorasick_cls import AhoCorasick

if __name__ == '__main__':
    main()