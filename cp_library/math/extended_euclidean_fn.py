import cp_library.math.__header__

def extended_euclidean(a, b):
    match a, b:
        case 0,0: return 0, 1, 0
        case _,0: return 1, 0, a
        case 0,_: return 0, 1, b
        case _:
            x,y,r,s = 1,0,0,1
            while b:
                q, c = divmod(a,b)
                a, b, r, s, x, y = b, c, x - q*r, y - q*s, r, s
            return x, y, a
