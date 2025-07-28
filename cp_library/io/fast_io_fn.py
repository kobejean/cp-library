import cp_library.__header__
import cp_library.io.__header__
import cp_library.io.__header__
from cp_library.io.io_cls import IO
def rd(): return IO.stdin.readints()
def rds(): return IO.stdin.__next__()
def rdl(n): return IO.stdin.readintsinto(elist(n))
def wt(s): IO.stdout.write(s)
def wtn(s): IO.stdout.write(f'{s}\n')
def wtnl(l): IO.stdout.write(' '.join(map(str, l)))
from cp_library.ds.list.elist_fn import elist