import cp_library.misc.__header__

import sys
sys.setrecursionlimit(10**6)
import pypyjit
pypyjit.set_param("max_unroll_recursion=-1")
