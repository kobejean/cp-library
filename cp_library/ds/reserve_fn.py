import cp_library.ds.__header__

def reserve(A: list, est_len: int) -> None: ...
try:
    from __pypy__ import resizelist_hint
except:
    def resizelist_hint(A: list, est_len: int):
        pass
reserve = resizelist_hint