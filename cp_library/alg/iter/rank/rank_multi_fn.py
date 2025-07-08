import cp_library.__header__
import cp_library.alg.__header__
import cp_library.alg.iter.__header__
import cp_library.alg.iter.rank.__header__
from cp_library.alg.iter.rank.irank_multi_fn import irank

def rank(*A: list[int], distinct = False): return *(R := tuple(Ai.copy() for Ai in A)), irank(*R, distinct)