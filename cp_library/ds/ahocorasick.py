from typing import Dict, List, Optional
from cp_library.ds.trie import Trie

class AhoCorasick(Trie):
    __slots__ = 'failed',

    def __init__(self):
        super().__init__()
        self.failed: Optional['AhoCorasick'] = None

    def build_fail(self) -> List['AhoCorasick']:
        arr_bfs = self.bfs()
        for p in arr_bfs:
            curr = p.parent
            if curr:
                c = p.last
                while curr.failed:
                    if c in curr.failed.dic:
                        p.failed = curr.failed.dic[c]
                        break
                    curr = curr.failed
                else:
                    p.failed = self
        self.failed = self
        return arr_bfs

    def count_freq(self, text: str) -> Dict[str, int]:
        arr_bfs = self.build_fail()
        p = self
        for c in text:
            while p != self and c not in p.dic:
                p = p.failed
            p = p.dic.get(c, self)
            p.count += 1

        output = {}
        for i in range(len(arr_bfs) - 1, 0, -1):
            p = arr_bfs[i]
            p.failed.count += p.count
            if p.word:
                word = self.get_word(p)
                output[word] = p.count
        return output