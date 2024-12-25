import cp_library.math.fps.__header__

from cp_library.math.fps.fps_deriv_fn import fps_deriv
from cp_library.math.fps.fps_integ_fn import fps_integ
from cp_library.math.fps.fps_inv_fn import fps_inv

def fps_log(P: list) -> list:
    fntt, ifntt = mint.ntt.fntt, mint.ntt.ifntt
    return fps_integ(mint.ntt.conv(fps_deriv(P), fps_inv(P), len(P)-1))

from cp_library.math.mod.mint_ntt_cls import mint