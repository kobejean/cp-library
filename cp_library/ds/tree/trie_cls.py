import cp_library.__header__
from typing import Optional
import cp_library.ds.__header__
import cp_library.ds.tree.__header__

class Trie:
    __slots__ = 'sub', 'par', 'chr', 'cnt', 'word'

    def __init__(T):
        T.sub: dict[str, Trie] = {}
        T.par: Optional[Trie] = None
        T.chr: str = ""
        T.cnt: int = 0
        T.word: bool = False

    def add(T, word: str):
        (node := T).cnt += 1
        for chr in word:
            if chr not in node.sub: node.sub[chr] = T.__class__()
            par, node = node, node.sub[chr]; node.par, node.chr = par, chr
            node.cnt += 1
        node.word = True

    def remove(T, word: str):
        assert (node := T.find(word)) and node.cnt >= 1
        if node.cnt == 1 and node.par: del node.par.sub[node.chr]
        while node: node.cnt -= 1; node = node.par
    
    def discard(T, word: str):
        if node := T.find(word):
            if node.par: del node.par.sub[node.chr]
            cnt = node.cnt
            while node: node.cnt -= cnt; node = node.par

    def find(T, prefix: str, full = True) -> Optional['Trie']:
        node = T
        for chr in prefix:
            if chr not in node.sub: return None if full else node
            node = node.sub[chr]
        return node
    
    def __contains__(T, word: str) -> bool:
        return node.word if (node := T.find(word)) is not None else False

    def __len__(T): return T.cnt

    def __str__(T) -> str:
        ret, node = [], T
        while node.par: ret.append(node.chr); node = node.par
        ret.reverse()
        return "".join(ret)
    
