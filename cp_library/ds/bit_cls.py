import cp_library.ds.__header__

class BinaryIndexTree:
    def __init__(self, v: int|list):
        if isinstance(v, int):
            self.data, self.size = [0]*v, v
        else:
            self.build(v)

    def build(self, data):
        self.data, self.size = data, len(data)
        for i in range(self.size):
            r = i|(i+1)
            if r < self.size: 
                self.data[r] += self.data[i]

    def add(self, i: int, x: object) -> None:
        assert 0 <= i <= self.size
        i += 1
        while i <= self.size:
            self.data[i-1], i = self.data[i-1] + x, i+(i&-i)

    def pref_sum(self, i: int):
        assert 0 <= i <= self.size
        s = 0
        while i > 0:
            s, i = s+self.data[i-1], i-(i&-i)
        return s
    
    def range_sum(self, l: int, r: int):
        assert 0 <= l <= r <= self.size
        m = l&r if l.bit_length() == r.bit_length() else 0
        s = 0
        while l > m:
            s, l = s-self.data[l-1], l-(l&-l)
        while r > m:
            s, r = s+self.data[r-1], r-(r&-r)
        return s