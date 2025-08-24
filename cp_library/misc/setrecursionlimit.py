import cp_library.__header__
import sys
import pypyjit
import cp_library.misc.__header__

sys.setrecursionlimit(10**6)
pypyjit.set_param("max_unroll_recursion=-1")