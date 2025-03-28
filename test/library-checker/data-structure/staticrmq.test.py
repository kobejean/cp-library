# verification-helper: PROBLEM https://judge.yosupo.jp/problem/staticrmq

def main():
    N, Q = rd(), rd()
    A = rdl(N)
    st = MinSparseTable(A)
    for _ in range(Q):
        wtn(st.query(rd(),rd()))

from cp_library.ds.min_sparse_table_cls import MinSparseTable
from __pypy__.builders import StringBuilder
import sys
from os import read as os_read, write as os_write
from atexit import register as atexist_register

class Fastio:
    ibuf = bytes()
    pil = pir = 0
    sb = StringBuilder()
    def load(self):
        self.ibuf = self.ibuf[self.pil:]
        self.ibuf += os_read(0, 131072)
        self.pil = 0; self.pir = len(self.ibuf)
    def flush_atexit(self): os_write(1, self.sb.build().encode())
    def flush(self):
        os_write(1, self.sb.build().encode())
        self.sb = StringBuilder()
    def fastin(self):
        if self.pir - self.pil < 64: self.load()
        minus = x = 0
        while self.ibuf[self.pil] < 45: self.pil += 1
        if self.ibuf[self.pil] == 45: minus = 1; self.pil += 1
        while self.ibuf[self.pil] >= 48:
            x = x * 10 + (self.ibuf[self.pil] & 15)
            self.pil += 1
        if minus: return -x
        return x
    def fastin_string(self):
        if self.pir - self.pil < 64: self.load()
        while self.ibuf[self.pil] <= 32: self.pil += 1
        res = bytearray()
        while self.ibuf[self.pil] > 32:
            if self.pir - self.pil < 64: self.load()
            res.append(self.ibuf[self.pil])
            self.pil += 1
        return res
    def fastout(self, x): self.sb.append(str(x))
    def fastoutln(self, x): self.sb.append(str(x)); self.sb.append('\n')
fastio = Fastio()
rd = fastio.fastin; rds = fastio.fastin_string; wt = fastio.fastout; wtn = fastio.fastoutln; flush = fastio.flush
atexist_register(fastio.flush_atexit)
sys.stdin = None; sys.stdout = None
def rdl(n): return [rd() for _ in range(n)]
def wtnl(l): wtn(' '.join(map(str, l)))

if __name__ == '__main__':
    main()
