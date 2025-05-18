import cp_library.__header__
from cp_library.alg.iter.cmpr.coord_compress_fn import coord_compress
import cp_library.ds.__header__
import cp_library.ds.wavelet.__header__
from cp_library.ds.wavelet.wm_group_cls import WMGroup
from cp_library.ds.wavelet.wm_monoid_compressed_cls import WMMonoidCompressed

class WMGroupCompressed(WMGroup,WMMonoidCompressed):
    def __init__(wm,op,e,diff,A:list[int],W:list):A,wm.Y=coord_compress(A);WMGroup.__init__(wm,op,e,diff,A,W,len(wm.Y)-1)