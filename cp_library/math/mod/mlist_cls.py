from cp_library.math.mod.mint_ntt_cls import mint

class mlist:
    def __init__(lst, data): lst.data = [0]*data if isinstance(data, int) else [int(x) for x in data]
    @staticmethod
    def from_raw(data: list[int]):
        (lst := mlist.__new__(mlist)).data = data
        return lst
    def __getitem__(lst, i) -> mint: return mint(lst.data[i])
    def __setitem__(lst, i, x): lst.data[i] = int(x)
    def __len__(lst): return len(lst.data)
    def conv(A, B, N):
        A = A.data
        B = B.data if hasattr(B, 'data') else B
        return mlist.from_raw(mint.ntt.conv(A, B, N))