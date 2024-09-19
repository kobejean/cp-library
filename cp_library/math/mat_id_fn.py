import cp_library.math.__init__

def mat_id(N):
    return [[int(i==j) for j in range(N)] for i in range(N)]
