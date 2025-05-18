import cp_library.__header__
import cp_library.math.__header__
import cp_library.math.mod.__header__
def lemire_precompute(d,bits=32):s=bits<<1;m=(1<<s)-1;a=(m+d)//d;return a,s,m
def lemire_divmod(x,d,a,s):q=(a*x)>>s;r=x-q*d;return q,r
def lemire_div(x,a,s):return(a*x)>>s
def lemire_mod(x,d,a,s,m):return(((a*x)&m)*d)>>s
def lemire_divisibility(x,a,m):return((a*x)&m)<a