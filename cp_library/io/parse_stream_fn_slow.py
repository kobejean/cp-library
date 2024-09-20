import cp_library.io.__init__

import typing
from collections import deque
from numbers import Number
from typing import Collection, Iterator, Type, TypeVar

from cp_library.io.parsable_cls import Parsable

T = TypeVar('T')
def parse_stream(stream: Iterator[str], spec: Type[T]|T) -> T:

    def parse_tuple(cls, specs):
        match specs:
            case [spec, end] if end is ...: 
                return cls(parse_line(spec))
            case specs:                     
                return cls(parse_spec(spec) for spec in specs)

    def parse_collection(cls, specs) -> list:
        match specs:
            case [ ] | [_] | set():          
                return cls(parse_line(*specs))
            case [spec, int() as n]: 
                return cls(parse_spec(spec) for _ in range(n))
            case _:
                raise NotImplementedError()

    def parse_spec(spec):
        if args := match_spec(spec, Parsable):
            cls, args = args
            return cls.parse(parse_spec, *args)
        elif args := match_spec(spec, tuple):      
            return parse_tuple(*args)
        elif args := match_spec(spec, Collection): 
            return parse_collection(*args)
        elif issubclass(cls := type(offset := spec), Number):         
            return cls(next_token()) + offset
        elif callable(cls := spec):                  
            return cls(next_token())
        else:
            raise NotImplementedError()

    def next_token():
        if not queue: queue.extend(next_line())
        return queue.popleft()
    
    def parse_line(spec=int):
        if not queue: queue.extend(next_line())
        while queue: yield parse_spec(spec)
        
    def next_line():
        return next(stream).rstrip().split()
    
    def match_spec(spec, types):
        if issubclass(cls := type(specs := spec), types):
            return cls, specs
        elif (isinstance(spec, type) and 
             issubclass(cls := typing.get_origin(spec) or spec, types)):
            return cls, (typing.get_args(spec) or tuple())
        
    queue = deque() 
    return parse_spec(spec)
