import cp_library.io.__header__
from cp_library.io.write_fn import write

def bye(*args, **kwargs):
    write(*args, **kwargs)
    exit(0)