from cp_library.alg.dp.max2_fn import max2
import cp_library.__header__
import cp_library.bit.__header__
import cp_library.bit.pack.__header__

class Packer:
    def __init__(P, mx: int):
        P.s = mx.bit_length()
        P.m = (1 << P.s) - 1
    def enc(P, a: int, b: int): return a << P.s | b
    def dec(P, x: int) -> tuple[int, int]: return x >> P.s, x & P.m
    def enumerate(P, A, reverse=False): P.ienumerate(A:=A.copy(), reverse); return A
    def ienumerate(P, A, reverse=False):
        if reverse:
            for i,a in enumerate(A): A[i] = P.enc(-a, i)
        else:
            for i,a in enumerate(A): A[i] = P.enc(a, i)
    def indices(P, A: list[int]): P.iindices(A:=A.copy()); return A
    def iindices(P, A):
        for i,a in enumerate(A): A[i] = P.m&a

class Packer3:
    def __init__(P, mxb: int, mxc: int):
        bb, bc = mxb.bit_length(), mxc.bit_length()
        P.mc, P.mb, P.sb, P.sa = (1<<bc)-1, (1<<bb)-1, bc, bc+bb
    def enc(P, a: int, b: int, c: int): return a << P.sa | b << P.sb | c
    def dec(P, x: int) -> tuple[int, int, int]: return x >> P.sa, (x >> P.sb) & P.mb, x & P.mc
    def enumerate(P, A, N, reverse=False): 
        V, k = [0]*N, 0
        if reverse:
            for i,Ai in enumerate(A):
                for j, a in enumerate(Ai):V[k]=P.enc(-a, i, j);k+=1
        else:
            for i,Ai in enumerate(A):
                for j, a in enumerate(Ai):V[k]=P.enc(a, i, j);k+=1
        return V

def argsort(A: list[int], reverse=False):
    P = Packer(len(I := A.copy())-1); P.ienumerate(I, reverse); I.sort(); P.iindices(I)
    return I
def iargsort(A: list[int], reverse=False):
    P = Packer(len(I := A)-1); P.ienumerate(I, reverse); I.sort(); P.iindices(I)
    return I

def argsort_multi(*A: list[int], reverse=False):
    P = Packer((N:=len(A[0]))-1); I, J, s, m = [0]*N, [*range(N)], P.s, P.m
    V = P.enumerate(A[-1], reverse); V.sort()
    if reverse:
        for B in A[-2::-1]:
            for i,v in enumerate(V):V[i],I[i]=-B[j:=J[v&m]]<<s|i,j
            I,J=J,I;V.sort()
    else:
        for B in A[-2::-1]:
            for i,v in enumerate(V):V[i],I[i]=B[j:=J[v&m]]<<s|i,j
            I,J=J,I;V.sort()
    for i,v in enumerate(V):I[i]=J[v&m]
    return I

def coord_compress(A: list[int], distinct = False):
    if not A: return [], []
    P = Packer((N:=len(A))-1); R, V = [0]*N, P.enumerate(A); V.sort()
    if distinct:
        for r, ai in enumerate(V): a, i = P.dec(ai); R[i], V[r] = r, a
    else:
        r, p = -1, V[-1]+1 # set p to unique value to trigger `if a != p` on first elm
        for ai in V:
            a, i = P.dec(ai)
            if a != p: V[r:=r+1] = p = a
            R[i] = r
        del V[r+1:]
    return R, V

def irank(A: list[int], distinct = False):
    P = Packer(len(A)-1)
    V = P.enumerate(A); V.sort()
    if distinct:
        for r, ai in enumerate(V): a, i = P.dec(ai); A[i], V[r] = r, a
    else:
        r = p = -1
        for ai in V:
            a, i = P.dec(ai)
            if a!=p: V[r:=r+1] = p = a
            A[i] = r
        del V[r+1:]
    return V

def irank_multi(*A: list[int], distinct = False):
    N = mxj = 0
    for Ai in A: N += len(Ai); mxj = max2(mxj, len(Ai))
    P = Packer3(len(A)-1, mxj); V = P.enumerate(A, N); V.sort();r=p=-1
    if distinct:
        for r,aij in enumerate(V):a,i,j=P.dec(aij);A[i][j],V[r]=r,a
    else:
        for aij in V:
            a,i,j=P.dec(aij)
            if a!=p:V[r:=r+1]=p=a
            A[i][j]=r
        del V[r+1:]
    return V

A = [4, 1, 7, 4, 6, 4, 3]
B = [4, 1, 1, 2, 1, 3, 1]
C = [8, 3, -9, -1, 0, 5, -1]
# print(argsort(A))
# print(argsort(A, True))
# print(argsort_multi(A, B))
# print(argsort_multi(A, B, reverse=True))
# print(C, coord_compress(C))
# print(C, coord_compress(C, True))
print(A, B, C)
print(irank_multi(A, B, C))
# print(irank_multi(A, B, C, distinct=True))
print(A, B, C)

import time
import random

def extended_benchmark_irank_methods():
    """Extended benchmark with larger datasets and more diverse test cases"""
    
    # Larger test cases
    test_cases = [
        # Very large datasets
        ("Very large random", [random.randint(1, 100000) for _ in range(50000)]),
        ("Huge random", [random.randint(1, 1000000) for _ in range(100000)]),
        
        # Large sorted datasets
        ("Very large sorted", list(range(50000))),
        ("Huge sorted", list(range(100000))),
        
        # Pathological cases
        ("Large mostly duplicates", [random.randint(1, 100) for _ in range(50000)]),
        ("Huge few values", [random.randint(1, 10) for _ in range(100000)]),
        
        # Real-world-like distributions
        ("Normal distribution", [int(random.gauss(5000, 1000)) for _ in range(50000)]),
        ("Exponential-like", [int(random.expovariate(0.001)) for _ in range(50000)]),
        
        # Edge cases with larger data
        ("Large alternating", [i if i % 2 == 0 else 100000 - i for i in range(50000)]),
        ("Large plateau", [1000] * 25000 + [2000] * 25000),
    ]
    
    print(f"{'Test Case':<25} {'Size':<8} {'irank (ms)':<12} {'multi (ms)':<12} {'Ratio':<8} {'Speedup':<8} {'Correct':<8}")
    print("-" * 90)
    
    for test_name, test_data in test_cases:
        # Test both distinct=False and distinct=True
        for distinct in [False, True]:
            suffix = " (distinct)" if distinct else ""
            
            try:
                # Benchmark irank (fewer iterations for large data)
                iterations = max(1, 50 // (len(test_data) // 1000))  # Adjust iterations based on size
                
                start = time.perf_counter()
                for _ in range(iterations):
                    result1 = irank(test_data.copy(), distinct=distinct)
                time1 = (time.perf_counter() - start) * 1000 / iterations  # Convert to ms per iteration
                
                # Benchmark irank_multi
                start = time.perf_counter()
                for _ in range(iterations):
                    result2 = irank_multi(test_data.copy(), distinct=distinct)
                time2 = (time.perf_counter() - start) * 1000 / iterations  # Convert to ms per iteration
                
                # Check correctness
                correct = result1 == result2
                ratio = time2 / time1 if time1 > 0 else float('inf')
                speedup = "irank" if ratio > 1 else "multi" if ratio < 1 else "tie"
                
                print(f"{test_name + suffix:<25} {len(test_data):<8} {time1:<12.3f} {time2:<12.3f} {ratio:<8.2f} {speedup:<8} {'✓' if correct else '✗':<8}")
                
            except Exception as e:
                print(f"{test_name + suffix:<25} {len(test_data):<8} {'ERROR':<12} {'ERROR':<12} {'N/A':<8} {'N/A':<8} {'✗':<8}")
                print(f"  Error: {e}")

def memory_usage_test():
    """Test memory usage patterns"""
    print("\nMemory Usage Test (approximate):")
    print("Note: This is a rough estimate based on data size")
    
    sizes = [10000, 50000, 100000, 500000]
    
    print(f"{'Size':<10} {'Input (MB)':<12} {'Est. Peak (MB)':<15}")
    print("-" * 40)
    
    for size in sizes:
        # Rough memory estimates
        input_mb = size * 8 / (1024 * 1024)  # Assuming 8 bytes per integer
        peak_mb = input_mb * 3  # Rough estimate for peak usage during ranking
        
        print(f"{size:<10} {input_mb:<12.2f} {peak_mb:<15.2f}")

def scaling_analysis():
    """Analyze how performance scales with input size"""
    print("\nScaling Analysis:")
    
    sizes = [100, 500, 1000, 5000, 10000, 25000, 50000, 100000, 1000000, 10000000]
    
    print(f"{'Size':<8} {'irank (ms)':<12} {'multi (ms)':<12} {'irank/n':<12} {'multi/n':<12}")
    print("-" * 60)
    
    for size in sizes:
        test_data = [random.randint(1, size) for _ in range(size)]
        
        # Single iteration for scaling test
        start = time.perf_counter()
        irank(test_data, distinct=False)
        time1 = (time.perf_counter() - start) * 1000
        
        start = time.perf_counter()
        irank_multi(test_data, distinct=False)
        time2 = (time.perf_counter() - start) * 1000
        
        time_per_n1 = time1 / size
        time_per_n2 = time2 / size
        
        print(f"{size:<8} {time1:<12.3f} {time2:<12.3f} {time_per_n1:<12.6f} {time_per_n2:<12.6f}")

if __name__ == "__main__":
    # Note: You'll need to define irank and irank_multi functions before running
    print("Extended Benchmark Suite for irank methods")
    print("=" * 50)
    
    try:
        extended_benchmark_irank_methods()
        memory_usage_test()
        scaling_analysis()
    except NameError:
        print("Error: irank and irank_multi functions not defined.")
        print("Please define these functions before running the benchmark.")