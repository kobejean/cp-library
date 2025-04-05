import cp_library.ds.__header__
import cp_library.ds.que.__header__

class que01:
    def __init__(self, hint=None):
        if hint: self.q0, self.q1 = elist(hint), elist(hint)
        else: self.q0, self.q1 = [], []
        
    def push0(self, item):
        self.q0.append(item)

    def push1(self, item):
        self.q1.append(item)
    
    def pop(self):
        if self.q0: return self.q0.pop()
        self.q0, self.q1 = self.q1, self.q0
        return self.q0.pop()

    def __len__(self):
        return len(self.q0) + len(self.q1)

from cp_library.ds.elist_fn import elist