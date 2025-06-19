from cp_library.math.mod.mint_cls import mint

class mintlist:
    def __init__(lst, data): lst.data = [0]*data if isinstance(data, int) else [int(x) for x in data]
    def __getitem__(lst, i): return mint(lst.data[i])
    def __setitem__(lst, i, x): lst.data[i] = int(x)