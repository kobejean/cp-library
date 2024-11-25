# verification-helper: PROBLEM https://atcoder.jp/contests/abc203/tasks/abc203_e

def main():
    N, M = read(tuple[int, ...])
    # groups and sorts by x value
    XY = read(list[tuple[int, ...], M])
    XY = sort_groups(XY, 0)
    
    # currently reacable columns
    S = { N }
    for _,group in XY:
        add = elist(len(group))
        for _,y in group:
            if (y-1) in S or (y+1) in S:
                # we can reach pawn on this column
                add.append(y)
        for _,y in group:
            # pawn blocks y column
            S.discard(y)
            # we'll add it back in the next loop if reachable
        for y in add:
            S.add(y)

    ans = len(S)
    print(ans)

from cp_library.ds.elist_fn import elist
from cp_library.io.read_specs_fn import read
from cp_library.alg.iter.sort_groups_fn import sort_groups
if __name__ == "__main__":
    main()