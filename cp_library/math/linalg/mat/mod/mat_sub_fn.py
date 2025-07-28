import cp_library.__header__
import cp_library.math.__header__
import cp_library.math.linalg.__header__
import cp_library.math.linalg.mat.__header__
import cp_library.math.linalg.mat.mod.__header__

def mat_sub(A, B, mod): return [[(Ai[j] - Bi[j]) % mod for j in range(len(Ai))] for Ai,Bi in zip(A,B)]