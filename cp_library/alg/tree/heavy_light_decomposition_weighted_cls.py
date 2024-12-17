import cp_library.alg.tree.__header__
from cp_library.alg.tree.heavy_light_decomposition_cls import HLD

class HLDWeighted(HLD):
    def __init__(self, T, r=0):
        super().__init__(T, r)
        self.weights = T.Wpar
