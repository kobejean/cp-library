try:
    from __pypy__ import newlist_hint
except:
    def newlist_hint(hint):
        return []
    
def elist(est_len: int) -> list:
    return newlist_hint(est_len)