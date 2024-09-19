import cp_library.alg.__init__

from cp_library.io.parsable_cls import Parsable

class DiGraphWeighted(list, Parsable):
    def __init__(self, N, edges=[]):
        super().__init__(([] for _ in range(N)))
        for u,v,w in edges:
            self[u].append((w,v))

    @classmethod
    def parse(cls, parse_spec, N, M, I=-1):
        return cls(N, parse_spec(list[tuple[I,I,int], M]))
