import cp_library.io.__init__

from cp_library.io.read_specs_fn import read

def read_edges(M, i0=1):
    return read(list[tuple[-i0,-i0], M])
