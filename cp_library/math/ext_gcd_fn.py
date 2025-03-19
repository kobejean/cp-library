import cp_library.math.__header__

def ext_gcd(a, b):
    ''' Returns (x, y, d) where: ax + by = d = gcd(a,b) '''
    if a and b:
        x,y,r,s = 1,0,0,1
        while b:
            q, c = divmod(a,b)
            a, b, r, s, x, y = b, c, x - q*r, y - q*s, r, s
        return x, y, a
    elif a: return 1, 0, a
    elif b: return 0, 1, b
    else: return 0, 1, 0
