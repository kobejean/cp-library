import cp_library.__header__
from __pypy__.builders import StringBuilder
import cp_library.io.__header__
from cp_library.io.io_cls import IO

class IOBytes(IO):
    def __init__(io, file):
        io.file = file
        io.f = -1
        io.sz = io.BUFSIZE
        io.B, io.O, io.S = bytearray(), [], StringBuilder()
        io.V = memoryview(io.B)
        io.l = io.p = 0
        io.char = False
        io.st, io.ist = [], []
        io.writable, io.encoding, io.errors = True, 'ascii', 'ignore'
    def readbytes(io, sz): return io.file.read(sz)