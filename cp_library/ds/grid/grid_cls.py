from cp_library.io.parser_cls import IOBase, Parsable, Parser
from cp_library.ds.view.view_cls import view
import cp_library.__header__
from typing import Generic, Union
from cp_library.misc.typing import _T
from cp_library.bit.pack.packer_cls import Packer
import cp_library.ds.__header__
import cp_library.ds.grid.__header__

class Grid(Generic[_T], Parsable):
    __slots__ = 'pkr', 'size', 'H', 'W', 'A'
    def __init__(G, H: int, W: int, A: Union[_T, list[_T], list[list[_T]]], pkr = None):
        G.pkr = pkr or Packer(W-1); G.size = H << G.pkr.s; G.H, G.W = H, W
        if isinstance(A, list):
            if isinstance(A[0], list):
                G.A = [A[0][0]]*G.size
                for i in range(H):
                    ii = i << G.pkr.s
                    for j in range(W): G.A[ii|j] = A[i][j]
            elif len(A) < G.size:
                G.A = [A[0]]*G.size
                for i in range(H):
                    ii = i << G.pkr.s
                    for j in range(W): G.A[ii|j] = A[i*W+j]
            else:
                G.A = A
        else:
            G.A = [A] * G.size
    def __len__(G): return G.H
    def __getitem__(G, i: int): 
        if 0 <= i < G.H: return view(G.A, i<<G.pkr.s, (i+1)<<G.pkr.s)
        else: raise IndexError
    def __call__(G, i: int, j: int): return G.A[G.pkr.enc(i,j)]
    def set(G, i: int, j: int, v: _T): G.A[G.pkr.enc(i,j)] = v

    @classmethod
    def compile(cls, H: int, W: int, T: type = int):
        pkr = Packer(W-1); size = H << pkr.s
        if T is int:
            def parse(io: IOBase):
                A = [0]*size
                for i in range(H):
                    for j, a in enumerate(io.readints()): A[pkr.enc(i,j)] = a
                return cls(H, W, A, pkr)
        elif T is str:
            def parse(io: IOBase):
                A = ['']*size
                for i in range(H):
                    for j, s in enumerate(io.line()): A[pkr.enc(i,j)] = s
                return cls(H, W, A, pkr)
        else:
            elm = Parser.compile(T)
            def parse(io: IOBase):
                A = [None]*size
                for i in range(H):
                    for j in range(W): A[pkr.enc(i,j)] = elm(io)
                return cls(H, W, A, pkr)
        return parse
