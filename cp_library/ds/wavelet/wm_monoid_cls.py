from abc import abstractmethod
import cp_library.__header__
import cp_library.ds.__header__
import cp_library.ds.wavelet.__header__
from cp_library.ds.wavelet.wm_static_cls import WMStatic

class WMMonoid(WMStatic):
    def __init__(wm,op,e,A:list[int],W:list[int],Amax:int=None):wm._build(op,e,A,W,[0]*len(A),[0]*len(A),max(A,default=0)if Amax is None else Amax)
    def _build(wm,op,e,A,W,nA,nW,Amax):wm.N,wm.H,wm.op,wm.e=len(A),Amax.bit_length(),op,e;wm._build_base(W);wm._build_levels(A,W,nA,nW)
    @abstractmethod
    def _build_base(wm,W):...
    @abstractmethod
    def _build_level(wm,L,W):...
    def _build_levels(wm,A,W,nA,nW):
        wm.up=[wm.Level(wm.N,H)for H in range(wm.H)];wm.down=wm.up[::-1]
        for L in wm.down:
            x,y,i=-1,wm.N-1,wm.N
            while i:y-=A[i:=i-1]>>L.H&1
            for i,a in enumerate(A):
                if a>>L.H&1:nA[y:=y+1],nW[y]=a,W[i];L.set1(i)
                else:nA[x:=x+1],nW[x]=a,W[i]
            A,nA,W,nW=nA,A,nW,W;wm._build_level(L,W)
    def prod_range(wm,l:int,r:int):return wm._prod_range(l,r)if l<r else wm.e
    def prod_at(wm,y:int,l:int,r:int):return wm._prod_rect(y,y+1,l,r)if l<r else wm.e
    def prod_below(wm,u:int,l:int,r:int):return wm._prod_below(u,l,r)if l<r else wm.e
    def prod_above(wm,d:int,l:int,r:int):return wm._prod_above(d,l,r)if l<r else wm.e
    def prod_between(wm,d:int,u:int,l:int,r:int):return wm._prod_rect(d,u,l,r)if l<r and d<u else wm.e
    def prod_corner(wm,r:int,u:int):return wm._prod_below(u,0,r)if 0<r else wm.e
    def prod_rect(wm,l:int,d:int,r:int,u:int):return wm._prod_rect(d,u,l,r)if l<r and d<u else wm.e
    @abstractmethod
    def _prod_range(wm,l,r):...
    def _prod_below(wm,u,l,r):
        if u<=0:return wm.e
        elif wm.H<u.bit_length():return wm._prod_range(l,r)
        prod=wm.e
        for L in wm.down:
            l,r=l-(l1:=L.count1(l)),r-(r1:=L.count1(r))
            if u>>L.H&1:prod=wm.op(prod,L.prod(l,r));l,r=L.T0+l1,L.T0+r1
        return prod
    def _prod_above(wm,d,l,r):
        if d<=0: return wm._prod_range(l, r)
        elif d.bit_length() > wm.H: return wm.e
        prod, d = wm.e, d-1
        for L in wm.down:
            l0,r0=l-(l:=L.T0+L.count1(l)),r-(r:=L.T0+L.count1(r))
            if d>>L.H&1==0:prod=wm.op(L.prod(l,r),prod);l,r=L.T0+l0,L.T0+r0
        return prod
    def _prod_rect(wm,d,u,l,r):
        if u<=0 or wm.H<d.bit_length():return wm.e
        elif d<=0:return wm._prod_below(u,l,r)
        elif wm.H<u.bit_length():return wm._prod_above(d,l,r)
        same,prod,d=1,wm.e,d-1
        for L in wm.down:
            db,ub,l,r=d>>L.H&1,u>>L.H&1,l-(l1:=L.count1(l)),r-(r1:=L.count1(r))
            if same:
                if db!=ub:same,dl,dr,l,r=0,l,r,L.T0+l1,L.T0+r1
                elif db:l,r=L.T0+l1,L.T0+r1
            else:
                if ub:prod=wm.op(prod,L.prod(l,r));l,r=L.T0+l1,L.T0+r1
                dl0,dr0=dl-(dl:=L.T0+L.count1(dl)),dr-(dr:=L.T0+L.count1(dr))
                if not db:prod=wm.op(L.prod(dl,dr),prod);dl,dr=L.T0+dl0,L.T0+dr0
        return prod