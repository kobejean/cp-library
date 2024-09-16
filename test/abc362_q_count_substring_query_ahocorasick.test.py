# verification-helper: PROBLEM https://atcoder.jp/contests/abc362/tasks/abc362_g

def solve():
    S = input()
    Q = int(input())
    ac = AhoCorasick()
    queries = []
    for _ in range(Q):
        T = input()
        ac.add(T)
        queries.append(T)

    freq_dict = ac.count_freq(S)
    return [freq_dict.get(query, 0) for query in queries]

from cp_library.ds.ahocorasick_cls import AhoCorasick

print(*solve(), sep='\n')