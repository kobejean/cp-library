import cp_library.__header__
from cp_library.alg.iter.cmpr.coord_compress_fn import coord_compress
import cp_library.ds.__header__
import cp_library.ds.wavelet.__header__
from cp_library.ds.wavelet.wm_bit_compressed_cls import WMBITCompressed
from cp_library.ds.wavelet.wm_weighted_points_cls import WMWeightedPoints

class WMBITPoints(WMBITCompressed, WMWeightedPoints):
    def __init__(wm, X: list[int], Y: list[int], W: list[int]):
        wm.I,wm.X=coord_compress(X,distinct=True);A,wm.Y=coord_compress(Y);nA,nW=[0]*(N:=len(A)),[0]*N
        for i,j in enumerate(wm.I):nA[j],nW[j]=A[i],W[i]
        super()._build(nA,nW,A,W,len(wm.Y)-1)
    def add(wm,i:int,w:int):super().add(wm.I[i],w)