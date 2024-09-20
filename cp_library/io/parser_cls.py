import cp_library.io.__init__

import sys
import typing
from collections import deque
from numbers import Number
from typing import Callable, Collection, Iterator, TypeVar

class TokenStream(Iterator):
    def __init__(self, stream = sys.stdin):
        self.stream = stream
        self.queue = deque()

    def __next__(self):
        if not self.queue: self.queue.extend(self.line())
        return self.queue.popleft()
    
    def wait(self):
        if not self.queue: self.queue.extend(self.line())
        while self.queue: yield
        
    def line(self):
        assert not self.queue
        return next(self.stream).rstrip().split()
    
        
T = TypeVar('T')
class Parser:
    def __init__(self, spec: type[T]|T):
        self.parse = Parser.compile(spec)

    def __call__(self, ts: TokenStream) -> T:
        return self.parse(ts)

    @staticmethod
    def compile(spec: type[T]|T=int) -> Callable[[TokenStream],T]:
            
        def compile_tuple(cls, specs):
            match specs:
                case [spec, end] if end is ...: 
                    fn = Parser.compile(spec) 
                    return lambda ts: cls(fn(ts) for _ in ts.wait())
                case specs:
                    fns = tuple(Parser.compile(spec) for spec in specs)               
                    return lambda ts: cls(fn(ts) for fn in fns)

        def compile_collection(cls, specs) -> list:
            match specs:
                case [ ] | [_] | set():   
                    fn = Parser.compile(*specs)       
                    return lambda ts: cls(fn(ts) for _ in ts.wait())
                case [spec, int() as n]: 
                    fn = Parser.compile(spec)
                    return lambda ts: cls(fn(ts) for _ in range(n))
                case _:
                    raise NotImplementedError()
        
        def match_spec(spec, types):
            if issubclass(cls := type(specs := spec), types):
                return cls, specs
            elif (isinstance(spec, type) and 
                issubclass(cls := typing.get_origin(spec) or spec, types)):
                return cls, (typing.get_args(spec) or tuple())
            
        if args := match_spec(spec, Parsable):
            cls, args = args
            return cls.compile(*args)
        elif issubclass(cls := type(offset := spec), Number):         
            return lambda ts: cls(next(ts)) + offset
        elif args := match_spec(spec, tuple):      
            return compile_tuple(*args)
        elif args := match_spec(spec, Collection): 
            return compile_collection(*args)
        elif callable(cls := spec):                  
            return lambda ts: cls(next(ts))
        else:
            raise NotImplementedError()
        
class Parsable:
    @classmethod
    def compile(cls):
        return lambda ts: cls(next(ts))