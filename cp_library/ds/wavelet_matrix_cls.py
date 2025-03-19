import cp_library.ds.__header__
from bisect import bisect_left
import heapq
from bitarray import bitarray

class WaveletMatrix:

    class Level(bitarray):
        def select(self, bit: int, k: int) -> int:
            def key(i):
                return self.count(bit, 0, i+1)
            index = bisect_left(range(len(self)), k+1, key=key)
            return -1 if index >= len(self) else index

    def __init__(self, data: list[int]):
        self.n = len(data)
        self.height = max(data).bit_length()
        self.rows = []
        self.start = dict()

        for h in range(self.height - 1, -1, -1):
            bits = WaveletMatrix.Level(self.n)
            left, right = [], []

            for i, num in enumerate(data):
                if num >> h & 1:
                    bits[i] = 1
                    right.append(num)
                else:
                    bits[i] = 0
                    left.append(num)

            self.rows.append((h,bits))
            data = left + right
        
        for i in range(self.n-1,-1,-1):
            self.start[data[i]] = i 
    
    def access(self, i: int) -> int:
        if i < 0 or i >= self.n:
            raise IndexError("Index out of range")

        val = 0
        for _, row in self.rows:
            bit, val = row[i], (val << 1) | row[i]
            i = row.count(bit, 0, i) + row.count(0)*bit

        return val

    def count(self, val: int, i: int) -> int:
        if i <= 0 or val not in self.start: return 0

        for h, row in self.rows:
            bit = val >> h & 1
            i = row.count(bit, 0, i) + row.count(0)*bit

        return i - self.start[val]
         
    def select(self, val: int, k: int) -> int:
        '''
        Find the 0-indexed position of the `k+1`-th occurance of `val`.
        '''
        if k < 0 or val not in self.start:
            return -1
        
        idx = self.start[val]+k
        for h, row in reversed(self.rows):
            bit = val >> h & 1
            idx = row.select(bit, idx - row.count(0)*bit)
            if idx == -1: return -1

        return idx

    def quantile(self, l: int, r: int, k: int) -> int:
        '''
        Find the k-th smallest element in the range [l, r).
        k is 0-indexed, so k=0 returns the minimum element in the range.
        '''
        if r > self.n or l >= r or k >= r - l:
            return -1

        val = 0
        for _, row in self.rows:
            cnt0lr = row.count(0, l, r)
            bit = 0 if k < cnt0lr else 1
            if bit:
                k -= cnt0lr
                cnt0l = row.count(0, l)
                l += cnt0l         # add 0s in [l,N)
                r += cnt0l+cnt0lr  # add 0s in [l,N)
            else:
                l = row.count(0, 0, l) # 0s in [0,l)
                r = l+cnt0lr           # 0s in [0,r)
            val = (val << 1) | bit
        return val

    def topk(self, l: int, r: int, k: int) -> list[tuple[int, int]]:
        '''
        Find the k most frequent elements in the range [l, r).
        
        :param l: start of the range (inclusive)
        :param r: end of the range (exclusive)
        :param k: number of top elements to return
        :return: list of (value, frequency) pairs, sorted by frequency (descending), then by value (descending)
        '''
        if r > self.n or l >= r or k <= 0:
            return []

        heap = []
        
        def dfs(l: int, r: int, depth: int, val: int):
            if l >= r:
                return
            
            if depth == self.height:
                count = r - l
                heapq.heappush(heap, (-count, -val, val, count))
                return

            h, row = self.rows[depth]
            cnt0 = row.count(0, l, r)
            cnt1 = r - l - cnt0

            # Process 1-bits (larger values) first
            if cnt1 > 0:
                next_l = row.count(0, 0, l) + row.count(0)
                next_r = next_l + cnt1
                dfs(next_l, next_r, depth + 1, val | (1 << (self.height - depth - 1)))

            # Then process 0-bits
            if cnt0 > 0:
                next_l = row.count(0, 0, l)
                next_r = next_l + cnt0
                dfs(next_l, next_r, depth + 1, val)

        dfs(l, r, 0, 0)
        
        result = []
        while heap and len(result) < k:
            _, _, val, count = heapq.heappop(heap)
            result.append((val, count))
        
        return result
