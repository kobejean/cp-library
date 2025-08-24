import cp_library.__header__
import cp_library.ds.__header__
import cp_library.ds.list.__header__

def elist(hint: int) -> list: ...
try:
    from __pypy__ import newlist_hint
except:
    def newlist_hint(hint): return []
elist = newlist_hint
    