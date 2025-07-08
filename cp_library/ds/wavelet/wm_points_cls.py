import cp_library.__header__
from cp_library.alg.divcon.bisect_left_fn import bisect_left
from cp_library.alg.iter.rank.rank_fn import rank
import cp_library.ds.__header__
import cp_library.ds.wavelet.__header__
from cp_library.ds.wavelet.wm_compressed_cls import WMCompressed

class WMPoints(WMCompressed):
    def __init__(wm,X,Y):
        wm.I,wm.X=rank(X,distinct=True);A,wm.Y=rank(Y);nA=[0]*len(Y)
        for i,j in enumerate(wm.I):nA[j]=A[i]
        wm._build(nA,A,len(wm.Y)-1)
    def _lidx(wm,x):return bisect_left(wm.X,x,0,len(wm.X))
    def __getitem__(wm,i):return super().__getitem__(wm.I[i])
    def kth(wm,k,l,r):return super().kth(k,wm._lidx(l),wm._lidx(r))
    def select(wm,y,k,l=0,r=-1):return super().select(y,k,wm._lidx(l),wm._lidx(r))
    def rank_range(wm,y,l,r):return super().rank_range(y,wm._lidx(l),wm._lidx(r))
    def count_at(wm,y,l,r):return super().count_at(y,wm._lidx(l),wm._lidx(r))
    def count_below(wm,u,l,r):return super().count_below(u,wm._lidx(l),wm._lidx(r))
    def count_between(wm,d,u,l,r):return super().count_between(d,u,wm._lidx(l),wm._lidx(r))
    def prev_val(wm,u,l,r):return super().prev_val(u,wm._lidx(l),wm._lidx(r))
    def next_val(wm,d,l,r):return super().next_val(d,wm._lidx(l),wm._lidx(r))