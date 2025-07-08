import cp_library.__header__
import cp_library.ds.__header__
import cp_library.ds.wavelet.__header__
from cp_library.ds.wavelet.wm_segtree_cls import WMSegTree
from cp_library.ds.wavelet.wm_monoid_compressed_cls import WMMonoidCompressed

class WMSegTreeCompressed(WMSegTree,WMMonoidCompressed):pass