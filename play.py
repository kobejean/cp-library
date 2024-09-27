
class BinaryIndexTree:
    def __init__(self, v: int|list):
        if isinstance(v, int):
            self.data, self.size = [0]*v, v
        else:
            self.build(v)

    def build(self, data):
        self.data, self.size = data, len(data)
        for i in range(self.size):
            if (r := i|(i+1)) < self.size: 
                self.data[r] += self.data[i]

    def get(self, i: int):
        assert 0 <= i < self.size
        s = self.data[i]
        z = i&(i+1)
        for _ in range((i^z).bit_count()):
            s, i = s-self.data[i-1], i-(i&-i)
        return s
    
    def set(self, i: int, x: int):
        self.add(i, x-self.get(i))
        
    def add(self, i: int, x: object) -> None:
        assert 0 <= i <= self.size
        i += 1
        while i <= self.size:
            self.data[i-1], i = self.data[i-1] + x, i+(i&-i)

    def pref_sum(self, i: int):
        assert 0 <= i <= self.size
        s = 0
        for _ in range(i.bit_count()):
            s, i = s+self.data[i-1], i-(i&-i)
        return s
    
    def range_sum(self, l: int, r: int):
        return self.pref_sum(r) - self.pref_sum(l)

bit = BinaryIndexTree(list(range(100)))
l,r = 5,7
a = bit.pref_sum(r) - bit.pref_sum(l)
b = bit.range_sum(l,r)
print(a, b)
for i in range(100):
    assert bit.range_sum(i,i+1) == bit.get(i)