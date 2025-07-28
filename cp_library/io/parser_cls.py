import cp_library.__header__
import typing
from numbers import Number
from types import GenericAlias 
from typing import Callable, Collection
import cp_library.io.__header__
from cp_library.io.io_base_cls import IOBase
from cp_library.io.parsable_cls import Parsable

class Parser:
    def __init__(self, spec):  self.parse = Parser.compile(spec)
    def __call__(self, io: IOBase): return self.parse(io)
    @staticmethod
    def compile_type(cls, args = ()):
        if issubclass(cls, Parsable): return cls.compile(*args)
        elif issubclass(cls, (Number, str)):
            def parse(io: IOBase): return cls(next(io))              
            return parse
        elif issubclass(cls, tuple): return Parser.compile_tuple(cls, args)
        elif issubclass(cls, Collection): return Parser.compile_collection(cls, args)
        elif callable(cls):
            def parse(io: IOBase): return cls(next(io))              
            return parse
        else: raise NotImplementedError()
    @staticmethod
    def compile(spec=int):
        if isinstance(spec, (type, GenericAlias)):
            cls, args = typing.get_origin(spec) or spec, typing.get_args(spec) or tuple()
            return Parser.compile_type(cls, args)
        elif isinstance(offset := spec, Number): 
            cls = type(spec)  
            def parse(io: IOBase): return cls(next(io)) + offset
            return parse
        elif isinstance(args := spec, tuple): return Parser.compile_tuple(type(spec), args)
        elif isinstance(args := spec, Collection): return Parser.compile_collection(type(spec), args)
        elif isinstance(fn := spec, Callable): 
            def parse(io: IOBase): return fn(next(io))
            return parse
        else: raise NotImplementedError()
    @staticmethod
    def compile_line(cls, spec=int):
        if spec is int:
            def parse(io: IOBase): return cls(io.readnums())
        else:
            fn = Parser.compile(spec)
            def parse(io: IOBase): return cls([fn(io) for _ in io.wait()])
        return parse
    @staticmethod
    def compile_repeat(cls, spec, N):
        fn = Parser.compile(spec)
        def parse(io: IOBase): return cls([fn(io) for _ in range(N)])
        return parse
    @staticmethod
    def compile_children(cls, specs):
        fns = tuple((Parser.compile(spec) for spec in specs))
        def parse(io: IOBase): return cls([fn(io) for fn in fns])  
        return parse
    @staticmethod
    def compile_tuple(cls, specs):
        if isinstance(specs, (tuple,list)) and len(specs) == 2 and specs[1] is ...: return Parser.compile_line(cls, specs[0])
        else: return Parser.compile_children(cls, specs)
    @staticmethod
    def compile_collection(cls, specs):
        if not specs or len(specs) == 1 or isinstance(specs, set):
            return Parser.compile_line(cls, *specs)
        elif (isinstance(specs, (tuple,list)) and len(specs) == 2 and isinstance(specs[1], int)):
            return Parser.compile_repeat(cls, specs[0], specs[1])
        else:
            raise NotImplementedError()