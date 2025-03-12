# verification-helper: PROBLEM https://judge.yosupo.jp/problem/rooted_tree_isomorphism_classification

def main():
    N = rd()
    P = rdl(N-1)
    if all(i == p for i,p in enumerate(P)):
        wtn(N)
        P.append(N-1)
        wtnl(P)
        return

    H = gen(N+1)
    sz = [1]*N
    ans = [1]*N
    for i, p in rev_enumerate(P, 1):
        ans[p] = mul(ans[p], ans[i] + H[sz[i]])
        sz[p] += sz[i]
    ids = { a: i for i, a in enumerate(set(ans)) }
    for i,a in enumerate(ans):
        ans[i] = ids[a]
    wtn(len(ids))
    wtnl(ans)

def mul(a: int, b: int) -> int:
    au, ad = a >> 31, a & 0x7fffffff
    bu, bd = b >> 31, b & 0x7fffffff
    m = ad * bu + au * bd
    mu, md = m >> 30, m & 0x3fffffff
    x = (au*bu<<1) + mu + (md << 31) + ad * bd
    xu, xd = x >> 61, x & 0x1fffffffffffffff
    res = xu + xd
    return res if res < 0x1fffffffffffffff else res - 0x1fffffffffffffff

def gen(N: int):
    seed = randint(0, 0xffffffff)
    H = [0]*N
    for i in range(N):
        seed ^= seed<<13&0xFFFFFFFF
        seed ^= seed>>17&0xFFFFFFFF
        seed ^= seed<<5&0xFFFFFFFF
        H[i] = seed &0xFFFFFFFF
    return H

from cp_library.alg.iter.rev_enumerate_fn import rev_enumerate
from random import randint
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
