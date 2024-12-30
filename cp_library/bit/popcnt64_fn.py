import cp_library.bit.__header__

def popcnt64(x):
    x = ((x >> 1)  & 0x5555555555555555) + (x & 0x5555555555555555)
    x = ((x >> 2)  & 0x3333333333333333) + (x & 0x3333333333333333)
    x = ((x >> 4)  & 0x0f0f0f0f0f0f0f0f) + (x & 0x0f0f0f0f0f0f0f0f)
    x = ((x >> 8)  & 0x00ff00ff00ff00ff) + (x & 0x00ff00ff00ff00ff)
    x = ((x >> 16) & 0x0000ffff0000ffff) + (x & 0x0000ffff0000ffff)
    x = ((x >> 32) & 0x00000000ffffffff) + (x & 0x00000000ffffffff)
    return x
