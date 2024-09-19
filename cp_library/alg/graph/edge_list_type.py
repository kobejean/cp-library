import cp_library.alg.graph.__init__
from typing import TypeAlias, TypeVar

M = TypeVar('M', int, None)
I = TypeVar('I', int, None)
EdgeList: TypeAlias = list[tuple[I,I], M]