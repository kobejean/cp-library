
from __pypy__ import strategy
A = [False]*10
print(strategy(A))

    Va, La, Ra, I = G.Va, G.La, G.Ra, G.La[:]
    G.state, G.stack = state, stack = u8a(G.N), elist(G.N)
    for s in G.starts(s):
        if state[s]: continue
        stack.append(s)
        # DOWN ROOT
        while stack:
            if state[u := stack[-1]] == 0:
                state[u] = 1
                # ENTER NODE
            if (i := I[u]) < Ra[u]:
                I[u] += 1
                if (s := state[v := Va[i]]) == 0:
                    stack.append(v)
                    # DOWN/TREE EDGE
                elif s == 1:
                    # BACK EDGE
                    pass
                elif s == 2:
                    # CROSS EDGE
                    pass
            else:
                stack.pop()
                state[u] = 2
                # UNCOMMENT IF BACKTRACKING
                # state[u], I[u] = 0, La[u]

                # LEAVE NODE
                if stack:
                    # UP/TREE EDGE
                    # v = stack[-1]
                    pass
        # UP ROOT