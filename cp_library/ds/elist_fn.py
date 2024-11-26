import cp_library.ds.__header__

def elist(est_len: int) -> list: ...
try:
    from __pypy__ import newlist_hint
except:
    def newlist_hint(hint):
        return []
elist = newlist_hint
    