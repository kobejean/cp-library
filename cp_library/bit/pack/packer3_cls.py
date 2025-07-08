import cp_library.__header__
import cp_library.bit.__header__
import cp_library.bit.pack.__header__

class Packer3:
    def __init__(P, mxb: int, mxc: int):
        bb, bc = mxb.bit_length(), mxc.bit_length()
        P.mc, P.mb, P.sb, P.sa = (1<<bc)-1, (1<<bb)-1, bc, bc+bb
    def enc(P, a: int, b: int, c: int): return a << P.sa | b << P.sb | c
    def dec(P, x: int) -> tuple[int, int, int]: return x >> P.sa, (x >> P.sb) & P.mb, x & P.mc
    def enumerate(P, A, N, reverse=False): 
        V, k = [0]*N, 0
        if reverse:
            for i,Ai in enumerate(A):
                for j, a in enumerate(Ai):V[k]=P.enc(-a, i, j);k+=1
        else:
            for i,Ai in enumerate(A):
                for j, a in enumerate(Ai):V[k]=P.enc(a, i, j);k+=1
        return V