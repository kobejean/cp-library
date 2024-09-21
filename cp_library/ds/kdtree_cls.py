import cp_library.ds.__header__

import typing
import random

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
            
            pi = self.partition(l,r,axis, random.randint(l, r))

            parent.children[child] = self.nodes[pi]
 
            if pi < r:
                stack.append((pi + 1, r, depth+1, self.nodes[pi], 1))
            if l < pi:
                stack.append((l, pi - 1, depth+1, self.nodes[pi], 0))
        self.root = root.children[0]

    def __getitem__(self, ranges: typing.Tuple[slice]):
        result = []
        stack = [(self.root, 0)]

        while stack:
            node, depth = stack.pop()
            axis = depth % self.k

            # Check if the current point is within the range
            if all(ranges[i].start <= node.point[i] < ranges[i].stop for i in range(self.k)):
                result.append(node.id)

            # Check right subtree if necessary
            if node.children[1] and node.point[axis] < ranges[axis].stop:
                stack.append((node.children[1], depth + 1))

            # Check left subtree if necessary
            if node.children[0] and ranges[axis].start <= node.point[axis]:
                stack.append((node.children[0], depth + 1))

        return result