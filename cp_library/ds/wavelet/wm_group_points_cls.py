import cp_library.__header__
from cp_library.alg.iter.cmpr.coord_compress_fn import coord_compress
import cp_library.ds.__header__
import cp_library.ds.wavelet.__header__
from cp_library.ds.wavelet.wm_group_compressed_cls import WMGroupCompressed
from cp_library.ds.wavelet.wm_monoid_points_cls import WMMonoidPoints

class WMGroupPoints(WMGroupCompressed,WMMonoidPoints):
    def __init__(wm,op,e,diff,X:list[int],Y:list[int],W:list):
        wm.I,wm.X=coord_compress(X,distinct=True);A,wm.Y=coord_compress(Y);nA,nW=[0]*(N:=len(A)),[0]*N
        for i,j in enumerate(wm.I):nA[j],nW[j]=A[i],W[i]
        wm._build(op,e,diff,nA,nW,A,W,len(wm.Y)-1)