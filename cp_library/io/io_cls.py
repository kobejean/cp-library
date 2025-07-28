import cp_library.__header__
from os import read as os_read, write as os_write, fstat as os_fstat
import sys
from __pypy__.builders import StringBuilder
from cp_library.alg.dp.max2_fn import max2
import cp_library.io.__header__
from cp_library.io.io_base_cls import IOBase

class IO(IOBase):
    BUFSIZE = 1 << 16; stdin: 'IO'; stdout: 'IO'
    __slots__ = 'f', 'file', 'B', 'O', 'V', 'S', 'l', 'p', 'char', 'sz', 'st', 'ist', 'writable', 'encoding', 'errors'
    def __init__(io, file):
        io.file = file
        try: io.f = file.fileno(); io.sz, io.writable = max2(io.BUFSIZE, os_fstat(io.f).st_size), ('x' in file.mode or 'r' not in file.mode)
        except: io.f, io.sz, io.writable = -1, io.BUFSIZE, False
        io.B, io.O, io.S = bytearray(), [], StringBuilder(); io.V = memoryview(io.B); io.l = io.p = 0
        io.char, io.st, io.ist, io.encoding, io.errors = False, [], [], 'ascii', 'ignore'
    def _dec(io, l, r): return io.V[l:r].tobytes().decode(io.encoding, io.errors)
    def readbytes(io, sz): return os_read(io.f, sz)
    def load(io):
        while io.l >= len(io.O):
            if not (b := io.readbytes(io.sz)):
                if io.O[-1] < len(io.B): io.O.append(len(io.B))
                break
            pos = len(io.B); io.B.extend(b)
            while ~(pos := io.B.find(b'\n', pos)): io.O.append(pos := pos+1)
    def __next__(io):
        if io.char: return io.readchar()
        else: return io.readtoken()
    def readchar(io):
        io.load(); r = io.O[io.l]
        c = chr(io.B[io.p])
        if io.p >= r-1: io.p = r; io.l += 1
        else: io.p += 1
        return c
    def write(io, s: str): io.S.append(s)
    def readline(io): io.load(); l, io.p = io.p, io.O[io.l]; io.l += 1; return io._dec(l, io.p)
    def readtoken(io):
        io.load(); r = io.O[io.l]
        if ~(p := io.B.find(b' ', io.p, r)): s = io._dec(io.p, p); io.p = p+1
        else: s = io._dec(io.p, r-1); io.p = r; io.l += 1
        return s
    def readtokens(io): io.st.clear(); return io.readtokensinto(io.st)
    def readints(io): io.ist.clear(); return io.readintsinto(io.ist)
    def readdigits(io): io.ist.clear(); return io.readdigitsinto(io.ist)
    def readnums(io): io.ist.clear(); return io.readnumsinto(io.ist)
    def readchars(io): io.load(); l, io.p = io.p, io.O[io.l]; io.l += 1; return io._dec(l, io.p-1)
    def readinto(io, lst):
        if io.char: return io.readcharsinto(lst)
        else: return io.readtokensinto(lst)
    def readcharsinto(io, lst): lst.extend(io.readchars()); return lst
    def readtokensinto(io, lst): 
        io.load(); r = io.O[io.l]
        while ~(p := io.B.find(b' ', io.p, r)): lst.append(io._dec(io.p, p)); io.p = p+1
        lst.append(io._dec(io.p, r-1)); io.p = r; io.l += 1; return lst
    def readintsinto(io, lst):
        io.load(); r = io.O[io.l]
        while io.p < r:
            while io.p < r and io.B[io.p] <= 32: io.p += 1
            if io.p >= r: break
            minus = x = 0
            if io.B[io.p] == 45: minus = 1; io.p += 1
            while io.p < r and io.B[io.p] >= 48:
                x = x * 10 + (io.B[io.p] & 15); io.p += 1
            lst.append(-x if minus else x)
            if io.p < r and io.B[io.p] == 32: io.p += 1
        io.l += 1; return lst
    def readdigitsinto(io, lst):
        io.load(); r = io.O[io.l]
        while io.p < r and io.B[io.p] > 32:
            if io.B[io.p] >= 48 and io.B[io.p] <= 57:
                lst.append(io.B[io.p] & 15)
            io.p += 1
        if io.p < r and io.B[io.p] == 10: io.p = r; io.l += 1
        return lst
    def readnumsinto(io, lst):
        if io.char: return io.readdigitsinto(lst)
        else: return io.readintsinto(lst)
    def line(io): io.st.clear(); return io.readinto(io.st)
    def wait(io):
        io.load(); r = io.O[io.l]
        while io.p < r: yield
    def flush(io):
        if io.writable: os_write(io.f, io.S.build().encode(io.encoding, io.errors)); io.S = StringBuilder()
sys.stdin = IO.stdin = IO(sys.stdin); sys.stdout = IO.stdout = IO(sys.stdout)
