import cp_library.math.__header__

from cp_library.math.nt.mod_inv_fn import mod_inv

class NTT:
    def __init__(self, mod = 998244353) -> None:
        self.mod = m = mod
        self.g = g = self.primitive_root(m)
        self.rank2 = rank2 = ((m-1)&(1-m)).bit_length() - 1
        self.root = root = [0] * (rank2 + 1)
        root[rank2] = pow(g, (m - 1) >> rank2, m)
        self.iroot = iroot = [0] * (rank2 + 1)
        iroot[rank2] = pow(root[rank2], m - 2, m)
        for i in range(rank2 - 1, -1, -1):
            root[i] = root[i+1] * root[i+1] % m
            iroot[i] = iroot[i+1] * iroot[i+1] % m
        def rates(s):
            r8,ir8 = [0]*max(0,rank2-s+1), [0]*max(0,rank2-s+1)
            p = ip = 1
            for i in range(rank2-s+1):
                r, ir = root[i+s], iroot[i+s]
                p,ip,r8[i],ir8[i]= p*ir%m,ip*r%m,r*p%m,ir*ip%m
            return r8, ir8
        self.rate2, self.irate2 = rates(2)
        self.rate3, self.irate3 = rates(3)
 
    def primitive_root(self, m):
        if m == 2: return 1
        if m == 167772161: return 3
        if m == 469762049: return 3
        if m == 754974721: return 11
        if m == 998244353: return 3
        divs = [0] * 20
        cnt, divs[0], x = 1, 2, (m - 1) // 2
        while x % 2 == 0: x //= 2
        i=3
        while i*i <= x:
            if x%i == 0:
                divs[cnt],cnt = i,cnt+1
                while x%i==0:x//=i
            i+=2
        if x > 1: divs[cnt],cnt = x,cnt+1
        for g in range(2,m):
            for i in range(cnt):
                if pow(g,(m-1)//divs[i],m)==1:break
            else:return g
    
    def fntt(self, A: list[int]):
        im, r8, m, h = self.root[2],self.rate3,self.mod,(len(A)-1).bit_length()
        for L in range(0,h-1,2):
            p, r = 1<<(h-L-2),1
            for s in range(1 << L):
                r3,of=(r2:=r*r%m)*r%m,s<<(h-L)
                for i in range(p):
                    i3=(i2:=(i1:=(i0:=i+of)+p)+p)+p
                    a0,a1,a2,a3 = A[i0],A[i1]*r,A[i2]*r2,A[i3]*r3
                    a0,a1,a2,a3 = a0+a2,a1+a3,a0-a2,(a1-a3)%m*im
                    A[i0],A[i1],A[i2],A[i3] = (a0+a1)%m,(a0-a1)%m,(a2+a3)%m,(a2-a3)%m
                r=r*r8[(~s&-~s).bit_length()-1]%m
        if h&1:
            r, r8 = 1, self.rate2
            for s in range(1<<(h-1)):
                i1=(i0:=s<<1)+1
                al,ar = A[i0],A[i1]*r%m
                A[i0],A[i1] = (al+ar)%m,(al-ar)%m
                r=r*r8[(~s&-~s).bit_length()-1]%m
        return A
    
    def _ifntt(self, A: list[int]):
        im, r8, m, h = self.iroot[2],self.irate3,self.mod,(len(A)-1).bit_length()
        for L in range(h,1,-2):
            p,r = 1<<(h-L),1
            for s in range(1<<(L-2)):
                r3,of=(r2:=r*r%m)*r%m,s<<(h-L+2)
                for i in range(p):
                    i3=(i2:=(i1:=(i0:=i+of)+p)+p)+p
                    a0,a1,a2,a3 = A[i0],A[i1],A[i2],A[i3]
                    a0,a1,a2,a3 = a0+a1,a2+a3,a0-a1,(a2-a3)*im%m
                    A[i0],A[i1],A[i2],A[i3] = (a0+a1)%m,(a2+a3)*r%m,(a0-a1)*r2%m,(a2-a3)*r3%m
                r=r*r8[(~s&-~s).bit_length()-1]%m
        if h&1:
            for i0 in range(p:=1<<(h-1)):
                al,ar = A[i0],A[i1:=i0+p]
                A[i0],A[i1] = (al+ar)%m,(al-ar)%m
        return A

    def ifntt(self, A: list[int]):
        self._ifntt(A)
        iz = mod_inv(N:=len(A),mod:=self.mod)
        for i in range(N): A[i]=A[i]*iz%mod
        return A
    
    def conv_naive(self, A, B, N):
        n, m, mod = len(A),len(B),self.mod
        C = [0]*N
        if n < m: A,B,n,m = B,A,m,n
        for i,a in enumerate(A):
            for j in range(min(m,N-i)):
                C[ij]=(C[ij:=i+j]+a*B[j])%mod
        return C
    
    def conv_fntt(self, A, B, N):
        n,m,mod=len(A),len(B),self.mod
        z=1<<(n+m-2).bit_length()
        self.fntt(A:=A+[0]*(z-n)), self.fntt(B:=B+[0]*(z-m))
        for i, b in enumerate(B): A[i] = A[i] * b % mod
        self.ifntt(A)
        del A[N:]
        return A
    
    def deconv(self, C, B, N = None):
        n, m = len(C), len(B)
        if N is None: N = n - m + 1
        z = 1 << (n + m - 2).bit_length()
        self.fntt(C := C+[0]*(z-n)), self.fntt(B := B+[0]*(z - m))

        A = [0] * z
        for i in range(z):
            if B[i] == 0:
                raise ValueError("Division by zero in NTT domain - deconvolution not possible")
            b_inv = mod_inv(B[i], self.mod)
            A[i] = (C[i] * b_inv) % self.mod
        
        self.ifntt(A)
        return A[:N]
    
    def conv_half(self, A, Bres):
        mod = self.mod
        self.fntt(A)
        for i, b in enumerate(Bres): A[i] = A[i] * b % mod
        self.ifntt(A)
        return A
    
    def conv(self, A, B, N = None):
        n,m = len(A), len(B)
        N = n+m-1 if N is None else N
        if min(n,m) <= 60: return self.conv_naive(A, B, N)
        return self.conv_fntt(A, B, N)

    def cycle_conv(self, A, B):
        n,m,mod=len(A),len(B),self.mod
        assert n == m
        if n==0:return[]
        con,res=self.conv(A,B),[0]*n
        for i in range(n-1):res[i]=(con[i]+con[i+n])%mod
        res[n-1]=con[n-1]
        return res
