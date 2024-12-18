import cp_library.alg.tree.__header__
from typing import Union
from cp_library.alg.graph.edge_cls import Edge
from cp_library.alg.graph.graph_cls import Graph
from cp_library.alg.tree.tree_proto import TreeProtocol

class Tree(TreeProtocol, Graph):
    @classmethod
    def compile(cls, N: int, E: Union[type,int] = Edge[-1]):
        return Graph.compile.__func__(cls, N, N-1, E)
    
    