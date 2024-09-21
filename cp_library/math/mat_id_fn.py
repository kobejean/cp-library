import cp_library.math.__header__

def mat_id(N):
    return [[int(i==j) for j in range(N)] for i in range(N)]
