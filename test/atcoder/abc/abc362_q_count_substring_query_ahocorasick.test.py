# verification-helper: PROBLEM https://atcoder.jp/contests/abc362/tasks/abc362_g

def main():
    S = read(str)
    Q = read(int)
    ac = AhoCorasick()
    queries = []
    for _ in range(Q):
        T = input()
        ac.add(T)
        queries.append(T)

    freq_dict = ac.count_freq(S)
    for query in queries:
        write(freq_dict.get(query, 0))

from cp_library.io.read_fn import read
from cp_library.io.write_fn import write
from cp_library.ds.tree.ahocorasick_cls import AhoCorasick

if __name__ == '__main__':
    main()