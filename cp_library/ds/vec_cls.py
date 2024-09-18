import typing
from cp_library.ds.vec_op_mixin import VecOpMixin

class vec(tuple, VecOpMixin):
    def __new__(cls, *args):
        if len(args) == 1 and isinstance(args[0], typing.Iterable):
            return super().__new__(cls, args[0])
        return super().__new__(cls, args)
