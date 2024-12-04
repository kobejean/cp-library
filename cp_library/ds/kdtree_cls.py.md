---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/dsl_2_c_kdtree.test.py
    title: test/dsl_2_c_kdtree.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2578\n             https://kobejean.github.io/cp-library               \n'''\n\
    \nimport typing\nimport random\n\nclass KDTreeNode:\n    __slots__ = ['id', 'point',\
    \ 'children']\n    \n    def __init__(self, id, point, children):\n        self.id\
    \ = id\n        self.point = point\n        self.children = children\n\nclass\
    \ KDTree:\n    __slots__ = ['k', 'nodes', 'root']\n\n    def __init__(self, points):\n\
    \        self.k = len(points[0])\n        self.build_tree(points)\n\n    def median_of_three(self,\
    \ l, r, axis):\n        m = (l + r) // 2\n        a, b, c = self.nodes[l].point[axis],\
    \ self.nodes[m].point[axis], self.nodes[r].point[axis]\n        if a <= b <= c\
    \ or c <= b <= a:\n            return m\n        if b <= a <= c or c <= a <= b:\n\
    \            return l\n        return r\n\n    def partition(self, l, r, axis,\
    \ pi):\n        nodes = self.nodes\n        nodes[pi], nodes[r] = nodes[r], nodes[pi]\n\
    \        pi = l\n        pivot = nodes[r].point[axis]\n        for j in range(l,\
    \ r):\n            v = nodes[j].point[axis]\n            if v < pivot or (v ==\
    \ pivot and j&1):\n                nodes[pi], nodes[j] = nodes[j], nodes[pi]\n\
    \                pi += 1\n        nodes[pi], nodes[r] = nodes[r], nodes[pi]\n\
    \        return pi\n\n    def build_tree(self, points):\n        self.nodes =\
    \ [KDTreeNode(id, point, [None,None]) for id,point in enumerate(points)]\n   \
    \     root = KDTreeNode(-1, None, [None])\n        stack = [(0, len(points)-1,\
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
    \ + 1))\n\n        return result\n"
  code: "import cp_library.ds.__header__\n\nimport typing\nimport random\n\nclass\
    \ KDTreeNode:\n    __slots__ = ['id', 'point', 'children']\n    \n    def __init__(self,\
    \ id, point, children):\n        self.id = id\n        self.point = point\n  \
    \      self.children = children\n\nclass KDTree:\n    __slots__ = ['k', 'nodes',\
    \ 'root']\n\n    def __init__(self, points):\n        self.k = len(points[0])\n\
    \        self.build_tree(points)\n\n    def median_of_three(self, l, r, axis):\n\
    \        m = (l + r) // 2\n        a, b, c = self.nodes[l].point[axis], self.nodes[m].point[axis],\
    \ self.nodes[r].point[axis]\n        if a <= b <= c or c <= b <= a:\n        \
    \    return m\n        if b <= a <= c or c <= a <= b:\n            return l\n\
    \        return r\n\n    def partition(self, l, r, axis, pi):\n        nodes =\
    \ self.nodes\n        nodes[pi], nodes[r] = nodes[r], nodes[pi]\n        pi =\
    \ l\n        pivot = nodes[r].point[axis]\n        for j in range(l, r):\n   \
    \         v = nodes[j].point[axis]\n            if v < pivot or (v == pivot and\
    \ j&1):\n                nodes[pi], nodes[j] = nodes[j], nodes[pi]\n         \
    \       pi += 1\n        nodes[pi], nodes[r] = nodes[r], nodes[pi]\n        return\
    \ pi\n\n    def build_tree(self, points):\n        self.nodes = [KDTreeNode(id,\
    \ point, [None,None]) for id,point in enumerate(points)]\n        root = KDTreeNode(-1,\
    \ None, [None])\n        stack = [(0, len(points)-1, 0, root, 0)]\n\n        while\
    \ stack:\n            l, r, depth, parent, child = stack.pop()\n            axis\
    \ = depth % self.k\n            \n            pi = self.partition(l,r,axis, random.randint(l,\
    \ r))\n\n            parent.children[child] = self.nodes[pi]\n \n            if\
    \ pi < r:\n                stack.append((pi + 1, r, depth+1, self.nodes[pi], 1))\n\
    \            if l < pi:\n                stack.append((l, pi - 1, depth+1, self.nodes[pi],\
    \ 0))\n        self.root = root.children[0]\n\n    def __getitem__(self, ranges:\
    \ typing.Tuple[slice]):\n        result = []\n        stack = [(self.root, 0)]\n\
    \n        while stack:\n            node, depth = stack.pop()\n            axis\
    \ = depth % self.k\n\n            # Check if the current point is within the range\n\
    \            if all(ranges[i].start <= node.point[i] < ranges[i].stop for i in\
    \ range(self.k)):\n                result.append(node.id)\n\n            # Check\
    \ right subtree if necessary\n            if node.children[1] and node.point[axis]\
    \ < ranges[axis].stop:\n                stack.append((node.children[1], depth\
    \ + 1))\n\n            # Check left subtree if necessary\n            if node.children[0]\
    \ and ranges[axis].start <= node.point[axis]:\n                stack.append((node.children[0],\
    \ depth + 1))\n\n        return result"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/ds/kdtree_cls.py
  requiredBy: []
  timestamp: '2024-12-05 05:25:23+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/dsl_2_c_kdtree.test.py
documentation_of: cp_library/ds/kdtree_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/kdtree_cls.py
- /library/cp_library/ds/kdtree_cls.py.html
title: cp_library/ds/kdtree_cls.py
---
