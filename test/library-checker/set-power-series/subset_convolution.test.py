# verification-helper: PROBLEM https://judge.yosupo.jp/problem/subset_convolution

def main():
    mod = 998244353
    n = rd()
    a = rdl(1 << n)
    b = rdl(1 << n)
    wtnl(subset_conv(a, b, n, mod))

from cp_library.math.conv.mod.subset_conv_fn import subset_conv

from atexit import register
from os import read, write
import sys
from __pypy__ import builders
class Fastio:
    ibuf = bytes()
    pil = pir = 0
    sb = builders.StringBuilder()
    def load(self):
        self.ibuf = self.ibuf[self.pil:]
        self.ibuf += read(0, 131072)
        self.pil = 0; self.pir = len(self.ibuf)
    def flush(self): write(1, self.sb.build().encode())
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
    def fastout(self, x): self.sb.append(str(x))
    def fastoutln(self, x): self.sb.append(str(x)); self.sb.append('\n')
fastio = Fastio()
rd = fastio.fastin; wt = fastio.fastout; wtn = fastio.fastoutln; flush = fastio.flush
register(flush)
sys.stdin = None; sys.stdout = None
def rdl(n): return [rd() for _ in range(n)]
def wtnl(l): wtn(' '.join(map(str, l)))

main()