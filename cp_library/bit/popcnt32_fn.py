import cp_library.bit.__header__

def popcnt32(x):
    x = ((x >> 1)  & 0x55555555) + (x & 0x55555555)
    x = ((x >> 2)  & 0x33333333) + (x & 0x33333333)
    x = ((x >> 4)  & 0x0f0f0f0f) + (x & 0x0f0f0f0f)
    x = ((x >> 8)  & 0x00ff00ff) + (x & 0x00ff00ff)
    x = ((x >> 16) & 0x0000ffff) + (x & 0x0000ffff)
    return x
if hasattr(int, 'bit_count'):
    popcnt32 = int.bit_count