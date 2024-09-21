import cp_library.io.__header__

import typing
from collections import deque
from numbers import Number
from typing import Collection, Iterator, Type, TypeVar

from cp_library.io.parsable_cls import Parsable

T = TypeVar('T')
def parse_stream(stream: Iterator[str], spec: Type[T]|T) -> T:

    def compile(spec=int):
        if args := match_spec(spec, Parsable):
            cls, args = args
            return cls.compile(compile, *args)
        elif args := match_spec(spec, tuple):      
            return compile_tuple(*args)
        elif args := match_spec(spec, Collection): 
            return compile_collection(*args)
        elif issubclass(cls := type(offset := spec), Number):         
            return lambda: cls(next_token()) + offset
        elif callable(cls := spec):                  
            return lambda: cls(next_token())
        else:
            raise NotImplementedError()
        
    def compile_tuple(cls, specs):
        match specs:
            case [spec, end] if end is ...: 
                fn = compile(spec) 
                return lambda: cls(parse_line(fn))
            case specs:
                fns = tuple(compile(spec) for spec in specs)               
                return lambda: cls(fn() for fn in fns)

    def compile_collection(cls, specs) -> list:
        match specs:
            case [ ] | [_] | set():   
                fn = compile(*specs)       
                return lambda: cls(parse_line(fn))
            case [spec, int() as n]: 
                fn = compile(spec)
                return lambda: cls(fn() for _ in range(n))
            case _:
                raise NotImplementedError()

    def next_token():
        if not queue: queue.extend(next_line())
        return queue.popleft()
    
    def parse_line(fn):
        if not queue: queue.extend(next_line())
        while queue: yield fn()
        
    def next_line():
        return next(stream).rstrip().split()
    
    def match_spec(spec, types):
        if issubclass(cls := type(specs := spec), types):
            return cls, specs
        elif (isinstance(spec, type) and 
             issubclass(cls := typing.get_origin(spec) or spec, types)):
            return cls, (typing.get_args(spec) or tuple())
        
    queue = deque() 
    parse = compile(spec)
    return parse()
