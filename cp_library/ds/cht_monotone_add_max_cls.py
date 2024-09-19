import cp_library.ds.__init__

from bisect import bisect_left

class CHTMonotoneAddMax:
    def __init__(self):
        self.hull = []

    def insert(self, m: int, b: int) -> None:
        # Remove lines with greater or equal slopes (maintaining monotonicity)
        while self.hull and self.hull[-1][0] >= m:
            self.hull.pop()

        def is_obsolete():
            (m1, b1), (m2, b2) = self.hull[-2], self.hull[-1]
            return (b - b1) * (m1 - m2) <= (b2 - b1) * (m1 - m)
        
        # Remove lines that are no longer part of the lower envelope
        while len(self.hull) >= 2 and is_obsolete():
            self.hull.pop()
        
        self.hull.append((m, b))

    def max(self, x: int) -> int:
        def eval(i):
            m, b = self.hull[i]
            return m * x + b
        def key(i):
            m1, b1 = self.hull[i]
            m2, b2 = self.hull[i+1]
            return (m1-m2)*x + (b1-b2)
        return eval(bisect_left(range(len(self.hull) - 1), 0, key=key))