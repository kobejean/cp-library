
class DisjointSparseTable:
    def __init__(self, op, arr: list):
        self.n = len(arr)
        self.log = (self.n-1).bit_length()
        self.op = op
        self.st = [arr]

        for h in range(1, self.log):
            row = arr.copy()
            half = 1 << h
            for m in range(half, self.n, 2*half):
                l,r = m-half,min(m+half,self.n)
                for j in range(m-1,l,-1): row[j-1] = self.op(row[j-1], row[j])
                for j in range(m,r-1): row[j+1] = self.op(row[j], row[j+1])
            self.st.append(row)

    def query(self, l: int, r: int):
        r -= 1
        if l == r: return self.st[0][l]
        h = (l ^ r).bit_length() - 1
        return self.op(self.st[h][l], self.st[h][r])

    def __repr__(self):
        return '\n'.join(f'{i:<2d} {row}' for i,row in enumerate(self.st))
