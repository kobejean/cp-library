from collections import deque
from typing import Dict, List, Optional

class Trie:
    __slots__ = 'dic', 'parent', 'last', 'count', 'word'

    def __init__(self):
        self.dic: Dict[str, Trie] = {}
        self.parent: Optional[Trie] = None
        self.last: str = ""
        self.count: int = 0
        self.word: bool = False
    
    def add(self, word: str) -> None:
        p = self
        for c in word:
            if c not in p.dic:   
                p.dic[c] = type(self)()
            parent = p
            p = p.dic[c]
            p.parent = parent
            p.last = c
        p.word = True

    def bfs(self) -> List['Trie']:
        output = []
        queue = deque([self])
        while queue:
            p = queue.popleft()
            output.append(p)
            queue.extend(p.dic.values())
        return output
    
    def get_word(self, p: 'Trie') -> str:
        output = []
        curr = p
        while curr != self:
            output.append(curr.last)
            curr = curr.parent
        return "".join(reversed(output))
    
    def find(self, prefix: str) -> 'Trie':
        node = self
        for char in prefix:
            if char not in node.dic:
                return None
            node = node.dic[char]
        return node
    
    def search(self, word: str) -> bool:
        node = self.find(word)
        return node.word if node is not None else False
