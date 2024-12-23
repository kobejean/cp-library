import cp_library.math.mod.__header__
from cp_library.math.mod.mint_cls import mint
from cp_library.math.nt.ntt_cls import NTT

class mint(mint):
    ntt: NTT

    @classmethod
    def set_mod(cls, mod: int):
        super().set_mod(mod)
        cls.ntt = NTT(mod)
