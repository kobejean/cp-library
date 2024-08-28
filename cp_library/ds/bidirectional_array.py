
class BidirectionalArray:
    def __init__(self, e, op, data):
        self.size = len(data)
        self.prefix = [e] + data.copy()
        self.suffix = data.copy() + [e]
        self.e = e
        self.op = op
        for i in range(self.size):
            self.prefix[i+1] = op(self.prefix[i], self.prefix[i+1])
        for i in range(self.size,0,-1):
            self.suffix[i-1] = op(self.suffix[i-1], self.suffix[i])
    def left(self, l): return self.prefix[l]
    def right(self, r): return self.suffix[r]
    def all(self): return self.prefix[-1]
    def out(self, l, r=None):
        r = l+1 if r is None else r
        return self.op(self.prefix[l], self.suffix[r])
    
