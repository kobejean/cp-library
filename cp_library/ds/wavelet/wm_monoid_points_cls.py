import cp_library.__header__
from cp_library.alg.iter.rank.rank_fn import rank
import cp_library.ds.__header__
import cp_library.ds.wavelet.__header__
from cp_library.ds.wavelet.wm_monoid_compressed_cls import WMMonoidCompressed
from cp_library.ds.wavelet.wm_points_cls import WMPoints

class WMMonoidPoints(WMMonoidCompressed,WMPoints):
    def __init__(wm,op,e,X:list[int],Y:list[int],W:list[int]):
        wm.I,wm.X=rank(X,distinct=True);A,wm.Y=rank(Y);nA,nW=[0]*(N:=len(A)),[0]*N
        for i,j in enumerate(wm.I):nA[j],nW[j]=A[i],W[i]
        wm._build(op,e,nA,nW,A,W,len(wm.Y)-1)
    def prod_range(wm,l,r):return super().prod_range(wm._lidx(l),wm._lidx(r))
    def prod_at(wm,y,l,r):return super().prod_at(y,wm._lidx(l),wm._lidx(r))
    def prod_below(wm,u,l,r):return super().prod_below(u,wm._lidx(l),wm._lidx(r))
    def prod_between(wm,d,u,l,r):return super().prod_between(d,u,wm._lidx(l),wm._lidx(r))
    def prod_corner(wm,r,u):return super().prod_corner(wm._lidx(r),u)
    def prod_rect(wm,l,d,r,u):return super().prod_rect(wm._lidx(l),d,wm._lidx(r),u)