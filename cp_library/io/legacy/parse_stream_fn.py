import cp_library.io.__header__

import typing
from collections import deque
from numbers import Number
from typing import Collection, Iterator, Type, TypeVar

from cp_library.io.parsable_cls import Parsable

T = TypeVar('T')
def parse_stream(stream: Iterator[str], spec: Type[T]|T) -> T:

    def parse_tuple(cls, specs):
        if isinstance(specs, list) and len(specs) == 2 and specs[1] is ...:
            return cls(parse_line(specs[0]))
        else:
            return cls(parse_spec(spec) for spec in specs)

    def parse_collection(cls, specs) -> list:
        if not specs or (isinstance(specs, Collection) and len(specs) == 1):
            return cls(parse_line(*specs))
        elif isinstance(specs, Collection) and len(specs) == 2 and isinstance(specs[1], int):
            spec, n = specs
            return cls(parse_spec(spec) for _ in range(n))
        else:
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
