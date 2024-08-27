---
title: PotentializedDSU (generalized with groups)
documentation_of: cp_library/ds/potentialized_dsu.py
---

## Operations

Works with group algebraic structures.

```python
def op(x,y):
    return (x+y)%mod

def inv(x):
    return (-x)%mod

pdsu = PotentializedDSU(op,inv,0,N)

```