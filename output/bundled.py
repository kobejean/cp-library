# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/2/DSL_2_C
import typing
import random
from collections import deque


class KDTreeNode:
    __slots__ = ['id', 'point', 'children']
    
    def __init__(self, id, point, children):
        self.id = id
        self.point = point
        self.children = children

class KDTree:
    __slots__ = ['k', 'nodes', 'root']

    def __init__(self, points):
        self.k = len(points[0])
        self.build_tree(points)

    def median_of_three(self, l, r, axis):
        m = (l + r) // 2
        a, b, c = self.nodes[l].point[axis], self.nodes[m].point[axis], self.nodes[r].point[axis]
        if a <= b <= c or c <= b <= a:
            return m
        if b <= a <= c or c <= a <= b:
            return l
        return r

    def partition(self, l, r, axis, pi):
        nodes = self.nodes
        nodes[pi], nodes[r] = nodes[r], nodes[pi]
        pi = l
        pivot = nodes[r].point[axis]
        for j in range(l, r):
            v = nodes[j].point[axis]
            if v < pivot or (v == pivot and j&1):
                nodes[pi], nodes[j] = nodes[j], nodes[pi]
                pi += 1
        nodes[pi], nodes[r] = nodes[r], nodes[pi]
        return pi

    def build_tree(self, points):
        self.nodes = [KDTreeNode(id, point, [None,None]) for id,point in enumerate(points)]
        root = KDTreeNode(-1, None, [None])
        stack = [(0, len(points)-1, 0, root, 0)]

        while stack:
            l, r, depth, parent, child = stack.pop()
            axis = depth % self.k
            # pi = self.partition(l,r,axis, self.median_of_three(l, r, axis))
            pi = self.partition(l,r,axis, random.randint(l, r))
            # if depth < 5:
            #     m = (l+r)//2
            #     thresh = 3*(m-l)//4
            #     if abs(pi - m) > thresh:
            #         ll, rr = (l, pi-1) if pi > m else (pi+1, r)
            #         pi = self.partition(ll, rr, axis, random.randint(ll, rr))

            parent.children[child] = self.nodes[pi]
 
            if pi < r:
                stack.append((pi + 1, r, depth+1, self.nodes[pi], 1))
            if l < pi:
                stack.append((l, pi - 1, depth+1, self.nodes[pi], 0))
        self.root = root.children[0]

    def __getitem__(self, ranges: typing.Tuple[slice]):
        result = []
        stack = deque([(self.root, 0)])
        # stack = []

        while stack:
            node, axis = stack.pop()
            axis = axis if axis < self.k else 0

            # Check if the current point is within the range
            if all(r.start <= p < r.stop for p, r in zip(node.point, ranges)):
                result.append(node.id)

            # Check right subtree if necessary
            if node.children[1] and node.point[axis] < ranges[axis].stop:
                stack.append((node.children[1], axis + 1))

            # Check left subtree if necessary
            if node.children[0] and ranges[axis].start <= node.point[axis]:
                stack.append((node.children[0], axis + 1))

        return result

def rint(shift=0, base=10):
    return [int(x, base) + shift for x in input().split()]

N, = rint()
pts = [rint() for _ in range(N)]

kdtree = KDTree(pts)

Q, = rint()
for _ in range(Q):
    sx,tx,sy,ty = rint()
    tx += 1
    ty += 1
    ans = sorted(kdtree[sx:tx,sy:ty]) + ['']
    print(*ans, sep='\n')
