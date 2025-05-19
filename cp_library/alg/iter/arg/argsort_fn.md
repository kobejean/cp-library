---
title: argsort
documentation_of: //cp_library/alg/iter/arg/argsort_fn.py
---

## Description

`argsort` returns the indices that would sort an array, using a highly optimized bit-packing approach that's particularly efficient when run with PyPy.

## Usage

```python
from cp_library.alg.iter.arg.argsort_fn import argsort

# Ascending sort indices
indices = argsort(array)

# Descending sort indices
indices = argsort(array, reverse=True)
```

## Implementation Details

The function uses bit-packing to combine array values with their indices before sorting:

```python
def argsort(A: list[int], reverse=False):
    s, m = pack_sm(len(A))
    if reverse:
        I = [a<<s|m^i for i,a in enumerate(A)]
        I.sort(reverse=True)
        for i,ai in enumerate(I): I[i] = m^ai&m
    else:
        I = [a<<s|i for i,a in enumerate(A)]
        I.sort()
        for i,ai in enumerate(I): I[i] = ai&m
    return I
```

This approach requires only a single sorting operation, with no costly key functions or multiple passes.

## Compatibility with Negative Numbers

Despite using bit operations, `argsort` correctly handles negative integers. This works because Python's left shift operation preserves the relative ordering of numbers, and the bit masking cleanly extracts just the index portion.

## PyPy Performance Advantage

The implementation excels when run with PyPy due to:

1. **Optimized Integer Lists**: PyPy uses specialized storage for homogeneous integer arrays
2. **Efficient JIT Compilation**: Bit operations (`<<`, `|`, `&`) are highly optimized
3. **Fast Sorting**: PyPy's `list.sort()` is particularly efficient for homogeneous types

## Performance Comparison

![Argsort Benchmark Results]({{ site.baseurl }}/static/media/argsort_benchmarks.png)

As the benchmark shows, `argsort` significantly outperforms alternatives:
- ~3-4x faster than `argsort_by_key`
- ~10x faster than `argsort_by_tuple` for large arrays

## Alternative Implementations

For reference, here are the slower but more intuitive alternatives:

```python
def argsort_by_key(A, reverse=False):
    I = [*range(len(A))]
    I.sort(key=A.__getitem__, reverse=reverse)
    return I

def argsort_by_tuple(A, reverse=False):
    I = [(a,i) for i,a in enumerate(A)]
    I.sort(reverse=reverse)
    return [i for _,i in I]
```

These implementations perform poorly compared to `argsort` primarily due to:
- Function call overhead with the key-based approach
- Memory allocation overhead for creating tuples
- Less effective JIT optimization by PyPy
