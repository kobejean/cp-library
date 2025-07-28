import cp_library.__header__
import cp_library.ds.__header__
from cp_library.ds.list.reserve_fn import reserve
import cp_library.ds.tree.__header__
import cp_library.ds.tree.bst.__header__
from cp_library.ds.tree.bst.treap_monoid_cls import TreapMonoid
from cp_library.ds.tree.bst.treap_reversible_cls import TreapReversible

class TreapMonoidReversibe(TreapMonoid,TreapReversible):
    __slots__='op'
    K,V,A,P,rev,sz,sub,st=None,[-1],[-1],[42],[0],[0,0],[-1,-1],[]
    def build(T,V):
        if not V: return
        base, rnd, P = len(T.V), T.P[-1], [0]*(N:=len(V))
        for i in range(N): P[i] = rnd = (rnd*1103515245+12345)&0xfffffff
        P.sort()
        T.V.extend(V); T.A.extend(V)
        T.P.extend(zeros:=[0]*N); T.rev.extend(zeros)
        T.sz.extend(zeros); T.sz.extend(zeros); T.sub.extend([-1]*(N<<1))
        N += base
        s,i = 2,base
        while i < N: T.P[i] = P.pop(); i += s
        s,hs,i,l = 4,1,base+1,-1
        while P:
            while i < N:
                T.P[i] = P.pop()
                l, r = i<<1,i<<1|1
                T.sub[l] = i-hs
                T.sz[l] = T.sz[(i-hs)<<1]+1+T.sz[(i-hs)<<1|1]
                T.A[i] = T.op(T.A[i-hs],T.A[i])
                if i+hs<N:
                    T.sub[r] = i+hs
                    T.sz[r] = T.sz[(i+hs)<<1]+1+T.sz[(i+hs)<<1|1]
                    T.A[i] = T.op(T.A[i],T.A[i+hs])
                elif i<N-1:
                    T.sub[r] = l = i+(1<<((N-1-i).bit_length()-1))
                    T.sz[r] = T.sz[l<<1]+1+T.sz[l<<1|1]
                    T.A[i] = T.op(T.A[i],T.A[l])
                i += s
            i,s,hs = base+s-1,s<<1,hs<<1
        T.sub[T.r<<1] = r = base+hs-1
        T.sz[T.r<<1] = T.sz[r<<1]+1+T.sz[r<<1|1]
        T.A[T.r] = T.A[r]

    def _nr(T):T.A.append(T.e);return TreapReversible._nr(T)
    def _nn(T,k,v):T.A.append(v);return TreapReversible._nn(T,k,v)
    def prod(T,l,r):
        # find common ancestor
        a=T.sub[T.r<<1]
        while~a:
            T._p(a)
            if l<=(sz:=T.sz[s:=a<<1])<r:break
            if sz<l:l-=1+sz;r-=1+sz;s^=1
            a=T.sub[s]
        if a<0:return T.e
        r-=T.sz[a<<1]+1
        # left subtreap
        ac,i=T.V[a],T.sub[a<<1]
        while~i and ~l:
            T._p(i)
            if (sz:=T.sz[s:=i<<1])<l:l-=1+sz;s^=1
            else:
                if~(j:=T.sub[i<<1|1]):ac=T.op(T.A[j],ac)
                ac=T.op(T.V[i],ac)
            i=T.sub[s]
        # right subtreap
        i=T.sub[a<<1|1]
        while~i and ~r:
            T._p(i)
            if (sz:=T.sz[s:=i<<1])<r:
                if~(j:=T.sub[s]):ac=T.op(ac,T.A[j])
                ac=T.op(ac,T.V[i])
                r-=1+sz;s^=1
            i=T.sub[s]
        return ac
    @classmethod
    def reserve(cls,sz):TreapReversible.reserve.__call__(sz);reserve(cls.A,sz+1)
    def _u(T,i):
        T.A[i]=T.V[i]
        T.sz[s]=T.sz[l<<1]+1+T.sz[l<<1|1] if~(l:=T.sub[s:=i<<1]) else 0
        T.sz[s]=T.sz[r<<1]+1+T.sz[r<<1|1] if~(r:=T.sub[s:=i<<1|1]) else 0
        if~(l:=T.sub[i<<1]):T.A[i]=T.op(T.A[l],T.A[i])
        if~(r:=T.sub[i<<1|1]):T.A[i]=T.op(T.A[i],T.A[r])
    # def _node_str(T, i): return f"{i=} V{T.V[i]} A{T.A[i]} ({T.sz[i<<1]}:{T.sz[i<<1|1]})"
    def _node_str(T, i): return f"{T.V[i]}"

if __name__ == '__main__':
    from operator import add
    L = 31
    T = TreapMonoidReversibe(add, 0)
    V = [*range(L)]
    T.build(V)
    print(T)
    # for L in range(2000):
    #     T = TreapMonoidReversibe(add, 0)
    #     V = [*range(L)]
    #     T.build(V)
    #     assert len(T) == L, f'{V}\n{T}'