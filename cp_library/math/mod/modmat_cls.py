import cp_library.math.mod.__init__
from typing import Union, List, Tuple
from cp_library.math.mod.mint_cls import mint

class ModMat:
    __slots__ = 'data', 'R', 'C'

    def __init__(self, data: List[Union[int,mint]]):
        self.data, self.R, self.C = data, len(data), len(data[0])
    
    @classmethod
    def identity(cls, N) -> 'ModMat': return ModMat([[int(i==j) for j in range(N)] for i in range(N)])
    
    @classmethod
    def zeros(cls, R, C) -> 'ModMat': return ModMat([[0]*C for _ in range(R)])

    def inv(self) -> 'ModMat':
        assert self.R != self.C
        
        N = self.R
        A = [row[:] for row in self.data]
        I = [[int(i==j) for j in range(N)] for i in range(N)]
        
        for i in range(N):
            if A[i][i] == 0:
                for j in range(i+1, N):
                    if A[j][i] != 0:
                        A[i], A[j] = A[j], A[i]
                        I[i], I[j] = I[j], I[i]
                        break
                else:
                    raise ValueError("Matrix is not invertible")
            
            inv = pow(A[i][i], -1, mint.mod)
            for j in range(N):
                A[i][j] = (A[i][j] * inv) % mint.mod
                I[i][j] = (I[i][j] * inv) % mint.mod
            
            for j in range(N):
                if i != j:
                    factor = A[j][i]
                    for k in range(N):
                        A[j][k] = (A[j][k] - factor * A[i][k]) % mint.mod
                        I[j][k] = (I[j][k] - factor * I[i][k]) % mint.mod
        
        return ModMat(I)
    
    def T(self) -> 'ModMat': return ModMat(list(map(list,zip(*self.data))))

    def elem_wise(self, func, other):
        if isinstance(other, ModMat):
            return ModMat([[func(a,b) for a,b in zip(Ai,Bi)] for Ai,Bi in zip(self.data,other.data)])
        elif isinstance(other, int):
            return ModMat([[func(a,other) for a in Ai] for Ai in self.data])
        else:
            return NotImplemented
        
    def __str__(self): return '\n'.join(' '.join(map(str,row)) for row in self.data)
    def __iter__(self): return self.data
    def __copy__(self): return ModMat([row[:] for row in self.data])
    def copy(self): return ModMat([row[:] for row in self.data])
    def __add__(self, other): return self.elem_wise(lambda a,b: (a+b) % mint.mod, other)
    def __radd__(self, other): return self.__add__(other)
    def __sub__(self, other): return self.elem_wise(lambda a,b: (a-b) % mint.mod, other)
    def __rsub__(self, other): return self.__sub__(other)
    def __mul__(self, other): return self.elem_wise(lambda a,b: (a*b) % mint.mod, other)
    def __rmul__(self, other): return self.__mul__(other)
    def __truediv__(self, other): return self.elem_wise(lambda a,b: a*pow(b,-1,mint.mod) % mint.mod, other)
    def __rtruediv__(self, other): return self.elem_wise(lambda a,b: pow(a,-1,mint.mod)*b % mint.mod, other)
    
    def __matmul__(self, other: 'ModMat'):
        assert self.C == other.R
        R = [[0]*other.C for _ in range(self.R)]
        for i,Ri in enumerate(R):
            for k,Aik in enumerate(self.data[i]):
                for j,Bkj in enumerate(other.data[k]):
                    Ri[j] = (Ri[j] + Aik*Bkj) % mint.mod
        return ModMat(R)
    
    def __pow__(self, K):
        assert isinstance(K,int)
        assert self.R == self.C
        A = self.copy()
        R = A if K & 1 else ModMat.identity(self.R)
        for i in range(1,K.bit_length()):
            A @= A 
            if K >> i & 1:
                R @= A 
        return R
    
    def __getitem__(self, key: Union[int, Tuple[int, int], slice, Tuple[slice, slice]]):
        if isinstance(key, int):
            return self.data[key]
        elif isinstance(key, tuple):
            if len(key) == 2:
                if all(isinstance(k, int) for k in key):
                    return mint(self.data[key[0]][key[1]])
                elif all(isinstance(k, slice) for k in key):
                    return ModMat([[self.data[i][j] for j in range(*key[1].indices(self.C))] 
                                   for i in range(*key[0].indices(self.R))])
            raise IndexError("Invalid index")
        elif isinstance(key, slice):
            return ModMat([row[:] for row in self.data[key]])
        raise IndexError("Invalid index")

    def __setitem__(self, key: Union[Tuple[int, int], slice, Tuple[slice, slice]], value):
        if isinstance(key, tuple):
            if len(key) == 2:
                if all(isinstance(k, int) for k in key):
                    self.data[key[0]][key[1]] = value % mint.mod
                elif all(isinstance(k, slice) for k in key):
                    if isinstance(value, ModMat):
                        for i, row in enumerate(range(*key[0].indices(self.R))):
                            for j, col in enumerate(range(*key[1].indices(self.C))):
                                self.data[row][col] = value.data[i][j] % mint.mod
                    else:
                        for row in range(*key[0].indices(self.R)):
                            for col in range(*key[1].indices(self.C)):
                                self.data[row][col] = value % mint.mod
                else:
                    raise IndexError("Invalid index")
            else:
                raise IndexError("Invalid index")
        elif isinstance(key, slice):
            if isinstance(value, ModMat):
                for i, row in enumerate(range(*key.indices(self.R))):
                    self.data[row] = [v % mint.mod for v in value.data[i]]
            else:
                for row in range(*key.indices(self.R)):
                    self.data[row] = [value % mint.mod] * self.C
        else:
            raise IndexError("Invalid index")

    def __delitem__(self, key: Union[int, slice]):
        if isinstance(key, (int, slice)):
            del self.data[key]
            self.R = len(self.data)
            if self.R == 0:
                self.C = 0
        else:
            raise IndexError("Invalid index")

    