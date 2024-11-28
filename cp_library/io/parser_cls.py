import sys
import cp_library.io.__header__

import typing
from collections import deque
from numbers import Number
from types import GenericAlias 
from typing import Callable, Collection, Iterator, TypeVar, Union
from cp_library.io.fast_io_cls import IOWrapper


class TokenStream(Iterator):
    stream = IOWrapper.stdin

    def __init__(self):
        self.queue = deque()

    def __next__(self):
        if not self.queue: self.queue.extend(self.line())
        return self.queue.popleft()
    
    def wait(self):
        if not self.queue: self.queue.extend(self.line())
        while self.queue: yield
        
    def line(self):
        return TokenStream.stream.readline().split()

class CharStream(TokenStream):
    def line(self):
        assert not self.queue
        return next(TokenStream.stream).rstrip()
        
T = TypeVar('T')
ParseFn = Callable[[TokenStream],T]
class Parser:
    def __init__(self, spec: Union[type[T],T]):
        self.parse = Parser.compile(spec)

    def __call__(self, ts: TokenStream) -> T:
        return self.parse(ts)
    
    @staticmethod
    def compile_type(cls: type[T], args = ()) -> T:
        if issubclass(cls, Parsable):
            return cls.compile(*args)
        elif issubclass(cls, (Number, str)):
            def parse(ts: TokenStream):
                return cls(next(ts))              
            return parse
        elif issubclass(cls, tuple):
            return Parser.compile_tuple(cls, args)
        elif issubclass(cls, Collection):
            return Parser.compile_collection(cls, args)
        elif callable(cls):
            def parse(ts: TokenStream):
                return cls(next(ts))              
            return parse
        else:
            raise NotImplementedError()
    
    @staticmethod
    def compile(spec: Union[type[T],T]=int) -> ParseFn[T]:
        if isinstance(spec, (type, GenericAlias)):
            cls = typing.get_origin(spec) or spec
            args = typing.get_args(spec) or tuple()
            return Parser.compile_type(cls, args)
        elif isinstance(offset := spec, Number): 
            cls = type(spec)  
            def parse(ts: TokenStream):
                return cls(next(ts)) + offset
            return parse
        elif isinstance(args := spec, tuple):      
            return Parser.compile_tuple(type(spec), args)
        elif isinstance(args := spec, Collection):  
            return Parser.compile_collection(type(spec), args)
        else:
            raise NotImplementedError()
    
    @staticmethod
    def compile_line(cls: T, spec=int) -> ParseFn[T]:
        if spec is int:
            fn = Parser.compile(spec)
            def parse(ts: TokenStream):
                return cls((int(token) for token in ts.line()))
            return parse
        else:
            fn = Parser.compile(spec)
            def parse(ts: TokenStream):
                return cls((fn(ts) for _ in ts.wait()))
            return parse

    @staticmethod
    def compile_repeat(cls: T, spec, N) -> ParseFn[T]:
        fn = Parser.compile(spec)
        def parse(ts: TokenStream):
            return cls((fn(ts) for _ in range(N)))
        return parse

    @staticmethod
    def compile_children(cls: T, specs) -> ParseFn[T]:
        fns = tuple((Parser.compile(spec) for spec in specs))
        def parse(ts: TokenStream):
            return cls((fn(ts) for fn in fns))  
        return parse
            
    @staticmethod
    def compile_tuple(cls: type[T], specs) -> ParseFn[T]:
        if isinstance(specs, (tuple,list)) and len(specs) == 2 and specs[1] is ...:
            return Parser.compile_line(cls, specs[0])
        else:
            return Parser.compile_children(cls, specs)

    @staticmethod
    def compile_collection(cls, specs):
        if not specs or len(specs) == 1 or isinstance(specs, set):
            return Parser.compile_line(cls, *specs)
        elif (isinstance(specs, (tuple,list)) and len(specs) == 2 
            and isinstance(specs[1], int)):
            return Parser.compile_repeat(cls, specs[0], specs[1])
        else:
            raise NotImplementedError()

class Parsable:
    @classmethod
    def compile(cls):
        def parser(ts: TokenStream):
            return cls(next(ts))
        return parser