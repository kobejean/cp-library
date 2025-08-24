from __pypy__ import bytebuffer, newlist_hint, list_get_physical_size, resizelist_hint
import gc
gc.disable()

# A = newlist_hint(1000000000_0000)
A = newlist_hint(1000000000_00)
for _ in range(1000000000): A.append(100)
print(list_get_physical_size(A))
A.pop()
print(list_get_physical_size(A))
A.append(100)
print(list_get_physical_size(A))
