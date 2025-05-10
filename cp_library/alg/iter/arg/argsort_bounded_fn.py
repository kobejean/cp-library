import cp_library.alg.iter.__header__

def argsort_bounded(A, mx):
    I, cnt, t = [0]*len(A), [0]*(mx+1), 0
    for a in A: cnt[a] += 1
    for a in range(mx+1): cnt[a], t = t, t+cnt[a]
    for i,a in enumerate(A): I[cnt[a]] = i; cnt[a] += 1
    return I