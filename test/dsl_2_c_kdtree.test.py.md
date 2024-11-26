---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/kdtree_cls.py
    title: cp_library/ds/kdtree_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/read_int_fn.py
    title: cp_library/io/read_int_fn.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/2/DSL_2_C
    links:
    - https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/2/DSL_2_C
  bundledCode: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/2/DSL_2_C\n\
    \ndef main():\n    N, = read()\n    pts = [read() for _ in range(N)]\n\n    kdtree\
    \ = KDTree(pts)\n\n    Q, = read()\n    for _ in range(Q):\n        sx,tx,sy,ty\
    \ = read()\n        tx += 1\n        ty += 1\n        ans = sorted(kdtree[sx:tx,sy:ty])\
    \ + ['']\n        print(*ans, sep='\\n')\n\n'''\n\u257A\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2578\n             https://kobejean.github.io/cp-library\
    \               \n'''\n\nimport typing\nimport random\n\nclass KDTreeNode:\n \
    \   __slots__ = ['id', 'point', 'children']\n    \n    def __init__(self, id,\
    \ point, children):\n        self.id = id\n        self.point = point\n      \
    \  self.children = children\n\nclass KDTree:\n    __slots__ = ['k', 'nodes', 'root']\n\
    \n    def __init__(self, points):\n        self.k = len(points[0])\n        self.build_tree(points)\n\
    \n    def median_of_three(self, l, r, axis):\n        m = (l + r) // 2\n     \
    \   a, b, c = self.nodes[l].point[axis], self.nodes[m].point[axis], self.nodes[r].point[axis]\n\
    \        if a <= b <= c or c <= b <= a:\n            return m\n        if b <=\
    \ a <= c or c <= a <= b:\n            return l\n        return r\n\n    def partition(self,\
    \ l, r, axis, pi):\n        nodes = self.nodes\n        nodes[pi], nodes[r] =\
    \ nodes[r], nodes[pi]\n        pi = l\n        pivot = nodes[r].point[axis]\n\
    \        for j in range(l, r):\n            v = nodes[j].point[axis]\n       \
    \     if v < pivot or (v == pivot and j&1):\n                nodes[pi], nodes[j]\
    \ = nodes[j], nodes[pi]\n                pi += 1\n        nodes[pi], nodes[r]\
    \ = nodes[r], nodes[pi]\n        return pi\n\n    def build_tree(self, points):\n\
    \        self.nodes = [KDTreeNode(id, point, [None,None]) for id,point in enumerate(points)]\n\
    \        root = KDTreeNode(-1, None, [None])\n        stack = [(0, len(points)-1,\
    \ 0, root, 0)]\n\n        while stack:\n            l, r, depth, parent, child\
    \ = stack.pop()\n            axis = depth % self.k\n            \n           \
    \ pi = self.partition(l,r,axis, random.randint(l, r))\n\n            parent.children[child]\
    \ = self.nodes[pi]\n \n            if pi < r:\n                stack.append((pi\
    \ + 1, r, depth+1, self.nodes[pi], 1))\n            if l < pi:\n             \
    \   stack.append((l, pi - 1, depth+1, self.nodes[pi], 0))\n        self.root =\
    \ root.children[0]\n\n    def __getitem__(self, ranges: typing.Tuple[slice]):\n\
    \        result = []\n        stack = [(self.root, 0)]\n\n        while stack:\n\
    \            node, depth = stack.pop()\n            axis = depth % self.k\n\n\
    \            # Check if the current point is within the range\n            if\
    \ all(ranges[i].start <= node.point[i] < ranges[i].stop for i in range(self.k)):\n\
    \                result.append(node.id)\n\n            # Check right subtree if\
    \ necessary\n            if node.children[1] and node.point[axis] < ranges[axis].stop:\n\
    \                stack.append((node.children[1], depth + 1))\n\n            #\
    \ Check left subtree if necessary\n            if node.children[0] and ranges[axis].start\
    \ <= node.point[axis]:\n                stack.append((node.children[0], depth\
    \ + 1))\n\n        return result\n\n\ndef read(shift=0, base=10):\n    return\
    \ [int(s, base) + shift for s in input().split()]\n\nif __name__ == '__main__':\n\
    \    main()\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/2/DSL_2_C\n\
    \ndef main():\n    N, = read()\n    pts = [read() for _ in range(N)]\n\n    kdtree\
    \ = KDTree(pts)\n\n    Q, = read()\n    for _ in range(Q):\n        sx,tx,sy,ty\
    \ = read()\n        tx += 1\n        ty += 1\n        ans = sorted(kdtree[sx:tx,sy:ty])\
    \ + ['']\n        print(*ans, sep='\\n')\n\nfrom cp_library.ds.kdtree_cls import\
    \ KDTree\nfrom cp_library.io.read_int_fn import read\n\nif __name__ == '__main__':\n\
    \    main()"
  dependsOn:
  - cp_library/ds/kdtree_cls.py
  - cp_library/io/read_int_fn.py
  isVerificationFile: true
  path: test/dsl_2_c_kdtree.test.py
  requiredBy: []
  timestamp: '2024-11-26 21:56:46+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/dsl_2_c_kdtree.test.py
layout: document
redirect_from:
- /verify/test/dsl_2_c_kdtree.test.py
- /verify/test/dsl_2_c_kdtree.test.py.html
title: test/dsl_2_c_kdtree.test.py
---
