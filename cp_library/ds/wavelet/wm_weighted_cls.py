import cp_library.__header__
import cp_library.ds.__header__
import cp_library.ds.wavelet.__header__
from cp_library.ds.wavelet.wm_static_cls import WMStatic

class WMWeighted(WMStatic):
    class Level(WMStatic.Level):
        def __init__(L,N:int,H:int):super().__init__(N,H);L.W=[0]*(N+1)
        def build(L,W:list[int]):
            super().build()
            for i,w in enumerate(W):L.W[i+1]=L.W[i]+w
        def sum(L,l:int,r:int):return L.W[r]-L.W[l]
    def __init__(wm, A:list[int],W:list[int],Amax:int=None):wm._build(A,W,[0]*len(A),[0]*len(A),max(A,default=0)if Amax is None else Amax)
    def _build(wm,A,W,nA,nW,Amax):wm.N,wm.H=len(A),Amax.bit_length();wm._build_base(W);wm._build_levels(A,W,nA,nW)
    def _build_base(wm, W):
        wm.W = [0]*(wm.N+1)
        for i,w in enumerate(W): wm.W[i+1] = wm.W[i]+w
    def _build_levels(wm, A, W, nA, nW):
        wm.up = [wm.Level(wm.N, H) for H in range(wm.H)]; wm.down = wm.up[::-1]
        for L in wm.down:
            x,y,i=-1,wm.N-1,wm.N
            while i:y-=A[i:=i-1]>>L.H&1
            for i,a in enumerate(A):
                if a>>L.H&1:nA[y:=y+1],nW[y]=a,W[i];L.set1(i)
                else:nA[x:=x+1],nW[x]=a,W[i]
            A,nA,W,nW=nA,A,nW,W;L.build(W)
    def sum_range(wm,l:int,r:int):return wm._sum_range(l,r) if l<r else 0
    def sum_at(wm,y:int,l:int,r:int):return wm._sum_rect(y,y+1,l,r) if l<r else 0
    def sum_below(wm,u:int,l:int,r:int):return wm._sum_below(u,l,r) if l<r else 0
    def sum_above(wm,d:int,l:int,r:int):return wm._sum_above(d,l,r) if l<r else 0
    def sum_between(wm,d:int,u:int,l:int,r:int):return wm._sum_rect(d,u,l,r)if l<r and d<u else 0
    def sum_corner(wm,r:int,u:int):return wm.sum_below(u,0,r) if 0<r else 0
    def sum_rect(wm,l:int,d:int,r:int,u:int):return wm._sum_rect(d,u,l,r)if l<r and d<u else 0
    def _sum_range(wm,l,r):return wm.W[r]-wm.W[l]
    def _sum_below(wm,u,l,r):
        if u<=0:return 0
        elif wm.H<u.bit_length():return wm._sum_range(l,r)
        sum = 0
        for L in wm.down:
            l,r=l-(l1:=L.count1(l)),r-(r1:=L.count1(r))
            if u>>L.H&1:sum+=L.sum(l,r);l,r=L.T0+l1,L.T0+r1
        return sum
    def _sum_above(wm,d,l,r):
        if d<=0:return wm._sum_range(l,r)
        elif wm.H<d.bit_length():return 0
        sum,d=0,d-1
        for L in wm.down:
            l0,r0=l-(l:=L.T0+L.count1(l)),r-(r:=L.T0+L.count1(r))
            if d>>L.H&1==0:sum+=L.sum(l,r);l,r=L.T0+l0,L.T0+r0
        return sum
    def _sum_rect(wm,d,u,l,r):
        if u<=0 or wm.H<d.bit_length():return 0
        elif d<=0:return wm._sum_below(u,l,r)
        elif wm.H<u.bit_length():return wm._sum_above(d,l,r)
        same,sum,d=1,0,d-1
        for L in wm.down:
            db,ub,l,r=d>>L.H&1,u>>L.H&1,l-(l1:=L.count1(l)),r-(r1:=L.count1(r))
            if same:
                if db!=ub:same,dl,dr,l,r=0,l,r,L.T0+l1,L.T0+r1
                elif db:l,r=L.T0+l1,L.T0+r1
            else:
                if ub:sum+=L.sum(l,r);l,r=L.T0+l1,L.T0+r1
                dl0,dr0=dl-(dl:=L.T0+L.count1(dl)),dr-(dr:=L.T0+L.count1(dr))
                if not db:sum+=L.sum(dl,dr);dl,dr=L.T0+dl0,L.T0+dr0
        return sum