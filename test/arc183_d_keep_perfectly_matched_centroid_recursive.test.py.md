---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: cp_library/alg/tree/find_centroid_recursive_fn.py
    title: cp_library/alg/tree/find_centroid_recursive_fn.py
  - icon: ':question:'
    path: cp_library/misc/setrecursionlimit.py
    title: cp_library/misc/setrecursionlimit.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    IGNORE: PROBLEM https://atcoder.jp/contests/arc183/tasks/arc183_d
    links:
    - https://atcoder.jp/contests/arc183/tasks/arc183_d
  bundledCode: "# verification-helper: IGNORE PROBLEM https://atcoder.jp/contests/arc183/tasks/arc183_d\n\
    import heapq\n\n\nimport sys\nsys.setrecursionlimit(10**6)\nimport pypyjit\npypyjit.set_param(\"\
    max_unroll_recursion=-1\")\n\ndef find_centroid(T):\n    N = len(T)\n    size\
    \ = [1] * N\n\n    def dfs(u=0, p=None):\n        is_cent = True\n        for\
    \ v in T[u]:\n            if v == p: continue\n            cent = dfs(v, u)\n\
    \            if cent != -1:\n                return cent\n            if size[v]\
    \ > N // 2:\n                is_cent = False\n            size[u] += size[v]\n\
    \        if N - size[u] > N // 2:\n            is_cent = False\n        return\
    \ u if is_cent else -1\n\n    return dfs()\n\ndef rint(shift=0, base=10):\n  \
    \  return [int(x, base) + shift for x in input().split()]\n\n\ndef solve():\n\
    \    size = [0] * N\n    centroid = find_centroid(T)\n    dfs_order = [[] for\
    \ _ in range(N)]\n    matched = (0, -1)\n    heap = []\n\n    def dfs(u, p):\n\
    \        r = u\n        stack = [(u, p, False)]\n        while stack:\n      \
    \      u, p, done = stack.pop()\n            if not done:\n                size[u]\
    \ = 1\n                dfs_order[r].append(u)\n                m = u ^ 1\n   \
    \             stack.append((u, p, True))\n                \n                if\
    \ m != p and m in T[u]:\n                    stack.append((m, u, False))\n\n \
    \               for v in T[u]:\n                    if v == p or m == v:\n   \
    \                     continue\n                    stack.append((v, u, False))\n\
    \            else:\n                for v in T[u]:\n                    if v !=\
    \ p:\n                        size[u] += size[v]\n        \n\n    for v in T[centroid]:\n\
    \        dfs(v, centroid)\n        if centroid ^ 1 == v:\n            matched\
    \ = (-size[v], v)\n        else:\n            heapq.heappush(heap, (-size[v],\
    \ v))\n\n    ops = []\n    while heap:\n        s, v = heapq.heappop(heap)\n \
    \       if dfs_order[v] and dfs_order[matched[1]]:\n            leaf1 = dfs_order[v].pop()\n\
    \            leaf2 = dfs_order[matched[1]].pop()\n            ops.append((leaf1,\
    \ leaf2))\n        else:\n            continue\n        if -matched[0] > 1:\n\
    \            heapq.heappush(heap, (matched[0] + 1, matched[1]))\n        matched\
    \ = (s + 1, v)\n\n    if matched[1] != -1:\n        ops.append((centroid, matched[1]))\n\
    \n    return ops\n\nN, = rint()\nT = [[] for _ in range(N)]\nfor _ in range(N-1):\n\
    \    u, v = rint(-1)\n    T[u].append(v)\n    T[v].append(u)\n\nfor op in solve():\n\
    \    print(op[0] + 1, op[1] + 1)\n"
  code: "# verification-helper: IGNORE PROBLEM https://atcoder.jp/contests/arc183/tasks/arc183_d\n\
    import heapq\n\nfrom cp_library.alg.tree.find_centroid_recursive_fn import find_centroid\n\
    \ndef rint(shift=0, base=10):\n    return [int(x, base) + shift for x in input().split()]\n\
    \n\ndef solve():\n    size = [0] * N\n    centroid = find_centroid(T)\n    dfs_order\
    \ = [[] for _ in range(N)]\n    matched = (0, -1)\n    heap = []\n\n    def dfs(u,\
    \ p):\n        r = u\n        stack = [(u, p, False)]\n        while stack:\n\
    \            u, p, done = stack.pop()\n            if not done:\n            \
    \    size[u] = 1\n                dfs_order[r].append(u)\n                m =\
    \ u ^ 1\n                stack.append((u, p, True))\n                \n      \
    \          if m != p and m in T[u]:\n                    stack.append((m, u, False))\n\
    \n                for v in T[u]:\n                    if v == p or m == v:\n \
    \                       continue\n                    stack.append((v, u, False))\n\
    \            else:\n                for v in T[u]:\n                    if v !=\
    \ p:\n                        size[u] += size[v]\n        \n\n    for v in T[centroid]:\n\
    \        dfs(v, centroid)\n        if centroid ^ 1 == v:\n            matched\
    \ = (-size[v], v)\n        else:\n            heapq.heappush(heap, (-size[v],\
    \ v))\n\n    ops = []\n    while heap:\n        s, v = heapq.heappop(heap)\n \
    \       if dfs_order[v] and dfs_order[matched[1]]:\n            leaf1 = dfs_order[v].pop()\n\
    \            leaf2 = dfs_order[matched[1]].pop()\n            ops.append((leaf1,\
    \ leaf2))\n        else:\n            continue\n        if -matched[0] > 1:\n\
    \            heapq.heappush(heap, (matched[0] + 1, matched[1]))\n        matched\
    \ = (s + 1, v)\n\n    if matched[1] != -1:\n        ops.append((centroid, matched[1]))\n\
    \n    return ops\n\nN, = rint()\nT = [[] for _ in range(N)]\nfor _ in range(N-1):\n\
    \    u, v = rint(-1)\n    T[u].append(v)\n    T[v].append(u)\n\nfor op in solve():\n\
    \    print(op[0] + 1, op[1] + 1)\n"
  dependsOn:
  - cp_library/alg/tree/find_centroid_recursive_fn.py
  - cp_library/misc/setrecursionlimit.py
  isVerificationFile: true
  path: test/arc183_d_keep_perfectly_matched_centroid_recursive.test.py
  requiredBy: []
  timestamp: '2024-08-30 22:41:46+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: test/arc183_d_keep_perfectly_matched_centroid_recursive.test.py
layout: document
redirect_from:
- /verify/test/arc183_d_keep_perfectly_matched_centroid_recursive.test.py
- /verify/test/arc183_d_keep_perfectly_matched_centroid_recursive.test.py.html
title: test/arc183_d_keep_perfectly_matched_centroid_recursive.test.py
---