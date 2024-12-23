import cp_library.vis.__header__

def debug(*args, **kwargs):
    if debug.on:
        print(*args, **kwargs)
debug.on = False