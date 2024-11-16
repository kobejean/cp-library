from io import TextIOBase
import cp_library.io.__header__

import sys
import typing
from collections import deque
from numbers import Number
from types import GenericAlias 
from typing import Callable, Collection, Iterator, TypeAlias, TypeVar

class TokenStream(Iterator):
    def __init__(self, stream: TextIOBase = sys.stdin):
        self.queue = deque()
        self.stream = stream

    def __next__(self):
        if not self.queue: self.queue.extend(self.line())
        return self.queue.popleft()
    
    def wait(self):
        if not self.queue: self.queue.extend(self.line())
        while self.queue: yield
        
    def line(self):
        assert not self.queue
        return sys.stdin.readline().split()

    def n_uints(self, n: int, shift = 0, max_digits: int = 20):
        # sync buffers
        tokens: list[str] = []
        while (lim := sys.stdin.buffer.tell() - sys.stdin.tell()) and len(tokens) < n:
            residual_str: str = sys.stdin.readline(lim)
            tokens.extend(residual_str.split())
        
        result = [0] * n
        pos = 0
        
        # Process residual string and check for partial token
        partial = None
        if tokens:
            if not residual_str[-1].isspace():
                partial = tokens.pop()
            for pos, token in enumerate(tokens):
                result[pos] = int(token)+shift
            pos += 1
        # Process remaining data token by token
        stdin_buffer = sys.stdin.buffer
        num = int(partial) if partial else 0
        have_digit = partial is not None

        original_chunk_size = sys.stdin._CHUNK_SIZE
        sys.stdin._CHUNK_SIZE = max(original_chunk_size, max_digits * (n - pos))
        
        while pos < n:
            byte = stdin_buffer.read(1)

            match byte[0]:
                case 10 | 32:
                    if have_digit:
                        result[pos] = num+shift
                        pos += 1
                        num = 0
                        have_digit = False
                case char:  # digit
                    num = (num * 10) + (char - 48)
                    have_digit = True

        if have_digit:
            result[pos] = num+shift
            pos += 1

        sys.stdin._CHUNK_SIZE = original_chunk_size 
        if pos < n:
            raise EOFError(f"Only found {pos} numbers, expected {n}")
            
        return result
    
    def n_ints(self, n: int, shift = 0, max_digits: int = 20):
        # sync buffers
        tokens: list[str] = []
        while (lim := sys.stdin.buffer.tell() - sys.stdin.tell()) and len(tokens) < n:
            residual_str: str = sys.stdin.readline(lim)
            tokens.extend(residual_str.split())
        
        result = [0] * n
        pos = 0
        
        # Process residual string and check for partial token
        partial = None
        if tokens:
            if not residual_str[-1].isspace():
                partial = tokens.pop()
            for pos, token in enumerate(tokens):
                result[pos] = int(token)+shift
            pos += 1
        # Process remaining data token by token
        stdin_buffer = sys.stdin.buffer
        num = abs(int(partial)) if partial else 0
        is_negative = partial and partial.startswith('-')
        have_digit = partial is not None

        original_chunk_size = sys.stdin._CHUNK_SIZE
        sys.stdin._CHUNK_SIZE = max(original_chunk_size, max_digits * (n - pos))
        
        while pos < n:
            byte = stdin_buffer.read(1)

            match byte[0]:
                case 10 | 32:
                    if have_digit:
                        result[pos] = -num+shift if is_negative else num+shift
                        pos += 1
                        num = 0
                        is_negative = False
                        have_digit = False
                case 45:  # minus sign
                    is_negative = True
                case char:  # digit
                    num = (num * 10) + (char - 48)
                    have_digit = True

        if have_digit:
            result[pos] = -num+shift if is_negative else num+shift
            pos += 1

        sys.stdin._CHUNK_SIZE = original_chunk_size 
        if pos < n:
            raise EOFError(f"Only found {pos} numbers, expected {n}")
            
        return result

class CharStream(TokenStream):
    def line(self):
        assert not self.queue
        return next(self.stream).rstrip()
        
T = TypeVar('T')
ParseFn: TypeAlias = Callable[[TokenStream],T]
class Parser:
    def __init__(self, spec: type[T]|T):
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
    def compile(spec: type[T]|T=int) -> ParseFn[T]:
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
        fn = Parser.compile(spec)
        def parse(ts: TokenStream):
            return cls(fn(ts) for _ in ts.wait())
        return parse
    
    # @staticmethod
    # def compile_n_ints(cls: T, N, shift = int) -> ParseFn[T]:
    #     shift = shift if isinstance(shift, int) else 0
    #     def parse(ts: TokenStream):
    #         return cls(ts.n_ints(N, shift))
    #     return parse

    @staticmethod
    def compile_repeat(cls: T, spec, N) -> ParseFn[T]:
        fn = Parser.compile(spec)
        def parse(ts: TokenStream):
            return cls(fn(ts) for _ in range(N))
        return parse

    @staticmethod
    def compile_children(cls: T, specs) -> ParseFn[T]:
        fns = tuple(Parser.compile(spec) for spec in specs)
        def parse(ts: TokenStream):
            return cls(fn(ts) for fn in fns)  
        return parse

    @staticmethod
    def compile_tuple(cls: type[T], specs) -> ParseFn[T]:
        match specs:
            case [spec, end] if end is ...:
                return Parser.compile_line(cls, spec)
            case specs:   
                return Parser.compile_children(cls, specs)
    
    @staticmethod
    def compile_collection(cls, specs):
        match specs:
            case [ ] | [_] | set():
                return Parser.compile_line(cls, *specs)
            case [spec, int() as N]:
                # if issubclass(spec, int) or isinstance(spec, int):
                #     return Parser.compile_n_ints(cls, N, spec)
                return Parser.compile_repeat(cls, spec, N)
            case _:
                raise NotImplementedError()

        
class Parsable:
    @classmethod
    def compile(cls):
        def parser(ts: TokenStream):
            return cls(next(ts))
        return parser