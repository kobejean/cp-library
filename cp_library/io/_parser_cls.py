
from math import inf
from numbers import Number
from typing import Collection, Iterable, Iterator
import typing

from cp_library.io.parsable_cls import Parsable

class Parser:
    def __init__(self, fn, *children):
        if isinstance(fn, Parser):
            raise
        self.unpack = True
        self.fn, self.children = fn, children
        if len(children) == 1 and isinstance(children[0], Iterable):
            self.children = children[0]
            self.unpack = False
        self.stride = sum((c.stride for c in self.children if isinstance(c,Parser)))
        if not children:
            self.stride = 1
        print(self.fn, self.stride, self.children)


    def __call__(self, s):
        if not self.children:
            return self.fn(s.token())
        else:
            nargs = tuple(c(s) if isinstance(c,Parser) else c for c in self.children)
            return self.fn(*nargs) if self.unpack else self.fn(nargs)
        
    @staticmethod
    def compile(spec):

        def compile_tuple(cls, specs):
            match specs:
                case [spec, end] if end is ...:
                    return LineParser(cls, Parser.compile(spec))
                case specs:
                    children = tuple(Parser.compile(spec) for spec in specs)               
                    return Parser(cls, children)
                
        def compile_collection(cls, specs) -> list:
            match specs:
                case [ ] | [_] | set():
                    return LineParser(cls, Parser.compile(*specs))
                case [spec, int() as n]: 
                    elm = Parser.compile(spec)
                    return Parser(cls, tuple(elm for _ in range(n)))
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
        elif args := match_spec(spec, tuple):      
            return compile_tuple(*args)
        elif args := match_spec(spec, Collection): 
            return compile_collection(*args)
        elif issubclass(cls := type(offset := spec), Number):         
            return Parser(lambda s: cls(s) + offset)
        elif callable(cls := spec):
            return Parser(cls)
        else:
            raise NotImplementedError()
        
class LineParser(Parser):
    def __init__(self, fn, child):
        super().__init__(fn,child)
        self.stride = inf

    def __call__(self, s):
        if not self.children:
            return self.fn(s.line())
        elif isinstance(c := self.children[-1], Parser):
            batches, extra = divmod(s.rem(), c.stride)
            assert extra == 0
            args = (*self.children[:-1], *(c(s) for _ in range(batches)))
            return self.fn(args)
        raise NotImplementedError()

class TokenStream:
    def __init__(self, stream: Iterator[str]):
        self.stream = stream
        self.tokens = []
        self.pos = 0

    def fetch(self):
        if self.pos >= len(self.tokens):
            self.pos = 0
            self.tokens = next(self.stream).rstrip().split()

    def token(self):
        self.fetch()
        token = self.tokens[self.pos]
        self.pos += 1
        return token
    
    def line(self):
        self.fetch()
        line = self.tokens[self.pos:]
        self.pos = len(self.tokens)
        return line
    
    def rem(self):
        self.fetch()
        return len(self.tokens) - self.pos
