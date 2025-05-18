import cp_library.__header__
import cp_library.ds.__header__
import cp_library.ds.wavelet.__header__
from cp_library.ds.wavelet.wm_segtree_compressed_cls import WMSegTreeCompressed
from cp_library.ds.wavelet.wm_monoid_points_cls import WMMonoidPoints

class WMSegTreePoints(WMSegTreeCompressed,WMMonoidPoints):
    def set(wm,i:int,w:int):super().set(wm.I[i],w)
    def get(wm,i:int):super().get(wm.I[i])