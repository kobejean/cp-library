import cp_library.__header__
from cp_library.alg.iter.rank.rank_fn import rank
import cp_library.ds.__header__
import cp_library.ds.wavelet.__header__
from cp_library.ds.wavelet.wm_weighted_compressed_cls import WMWeightedCompressed
from cp_library.ds.wavelet.wm_points_cls import WMPoints

class WMWeightedPoints(WMWeightedCompressed,WMPoints):
    def __init__(wm,X:list[int],Y:list[int],W:list[int]):
        wm.I,wm.X=rank(X,distinct=True);A,wm.Y=rank(Y);nA,nW=[0]*(N:=len(A)),[0]*N
        for i,j in enumerate(wm.I):nA[j],nW[j]=A[i],W[i]
        wm._build(nA,nW,A,W,len(wm.Y)-1)
    def sum_range(wm,l,r):return super().sum_range(wm._lidx(l),wm._lidx(r))
    def sum_at(wm,y,l,r):return super().sum_at(y,wm._lidx(l),wm._lidx(r))
    def sum_below(wm,u,l,r):return super().sum_below(u,wm._lidx(l),wm._lidx(r))
    def sum_between(wm,d,u,l,r):return super().sum_between(d,u,wm._lidx(l),wm._lidx(r))
    def sum_corner(wm,r,u):return super().sum_corner(wm._lidx(r),u)
    def sum_rect(wm,l,d,r,u):return super().sum_rect(wm._lidx(l),d,wm._lidx(r),u)