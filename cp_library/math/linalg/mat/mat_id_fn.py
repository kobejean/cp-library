import cp_library.__header__
import cp_library.math.__header__
import cp_library.math.linalg.__header__
import cp_library.math.linalg.mat.__header__

def mat_id(N):
    return [[int(i==j) for j in range(N)] for i in range(N)]