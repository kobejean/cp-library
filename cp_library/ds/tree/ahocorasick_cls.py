import cp_library.__header__
from typing import Optional
from collections import Counter, deque
import cp_library.ds.__header__
import cp_library.ds.tree.__header__
from cp_library.ds.tree.trie_cls import Trie
from cp_library.ds.que.que_cls import Que

class AhoCorasick(Trie):
    __slots__ = 'failed', 'freq'

    def __init__(T):
        super().__init__()
        T.failed: Optional['AhoCorasick'] = None
        T.freq: int = 0

    def build(T):
        order: list[AhoCorasick] = T.bfs()
        for node in order:
            now: AhoCorasick = node.par
            chr = node.chr
            while now.failed:
                if chr in now.failed.sub:
                    node.failed = now.failed.sub[chr]
                    break
                now = now.failed
            else:
                node.failed = T
        T.failed = T
        return order

    def freq_table(T, text: str) -> Counter[str, int]:
        order = T.build()
        order.reverse()
        node: AhoCorasick = T
        for chr in text:
            while node != T and chr not in node.sub:
                node = node.failed
            node = node.sub.get(chr, T)
            node.freq += 1

        output = Counter()
        for node in order:
            node.failed.freq += node.freq
            if node.word:
                output[str(node)] = node.freq
        return output

    def bfs(T) -> list['Trie']:
        order, que = [], Que([T])
        while que:
            order.extend(sub := que.pop().sub.values())
            que.extend(sub)
        return order
