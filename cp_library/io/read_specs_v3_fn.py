
'''
╺━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╸
                 Competitive Programming Library                 
╺━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╸
'''
import sys
from numbers import Number
from collections import deque
from typing import Iterator, Type, TypeVar, Collection
import typing

T = TypeVar('T')
def read(spec: Type[T]=[int]) -> T:
    return parse_stream(sys.stdin, spec)

def parse_stream(stream: Iterator[str], spec: Type[T]) -> T:
    def parse_tuple(cls, specs):
        match specs:
            case [spec, end] if end is ...: 
                return cls(parse_line(spec))
            case specs:                     
                return cls(map(parse_spec, specs))

    def parse_collection(cls, specs):
        match specs:
            case [ ] | [_]:          
                return cls(parse_line(*specs))
            case [spec, int() as n]: 
                return cls(parse_spec(spec) for _ in range(n))

    def parse_spec(spec = int):
        if issubclass(cls := type(offset := spec), Number):         
            return cls(next_token()) + offset
        elif args := match_spec(spec, tuple):      
            return parse_tuple(*args)
        elif args := match_spec(spec, Collection): 
            return parse_collection(*args)
        elif callable(cls := spec):                  
            return cls(next_token())

    def parse_line(spec=int):
        if not queue: queue.extend(next_line())
        while queue: yield parse_spec(spec)
        
    def next_token():
        if not queue: queue.extend(next_line())
        return queue.popleft()
    
    def next_line():
        return next(stream).rstrip().split()
    
    def match_spec(spec, types):
        if issubclass(cls := type(specs := spec), types):
            return cls, specs
        elif (isinstance(spec, type) and 
             (specs := typing.get_args(spec)) and 
             issubclass(cls := typing.get_origin(spec), types)):
            return cls, specs
        
    queue = deque(next_line()) 
    return parse_spec(spec)
