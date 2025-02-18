# verification-helper: PROBLEM https://judge.yosupo.jp/problem/bitwise_and_convolution

def main():
    N = rd()
    A = rdl(1 << N)
    B = rdl(1 << N)
    wtnl(and_conv(A, B, N, 998244353))

from cp_library.math.and_conv_fast_fn import and_conv
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

if __name__ == '__main__':
    main()
