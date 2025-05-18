import cp_library.__header__
import cp_library.ds.__header__
import cp_library.ds.wavelet.__header__
from cp_library.ds.wavelet.wm_bit_cls import WMBIT
from cp_library.ds.wavelet.wm_weighted_compressed_cls import WMWeightedCompressed

class WMBITCompressed(WMBIT,WMWeightedCompressed):pass