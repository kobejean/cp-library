import cp_library.__header__
import sys
import cp_library.vis.__header__

def debug(*args, **kwargs):
    if debug.on:
        kwargs.setdefault('file', sys.stderr)
        print(*args, **kwargs)
debug.on = False