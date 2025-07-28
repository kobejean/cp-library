# verification-helper: PROBLEM https://atcoder.jp/contests/abc203/tasks/abc203_e

def main():
    N, M = read(tuple[int, ...])
    # groups and sorts by x value
    XY = read(QueriesGrouped[M])
    
    # currently reacable columns
    S = { N }
    for _,group in XY:
        add = elist(len(group))
        for _,_,y in group:
            if (y-1) in S or (y+1) in S:
                # we can reach pawn on this column
                add.append(y)
        for _,_,y in group:
            # pawn blocks y column
            S.discard(y)
            # we'll add it back in the next loop if reachable
        for y in add:
            S.add(y)

    ans = len(S)
    write(ans)

from cp_library.ds.list.elist_fn import elist
from cp_library.io.read_fn import read
from cp_library.io.write_fn import write
from cp_library.ds.queries_cls import QueriesGrouped

if __name__ == "__main__":
    main()