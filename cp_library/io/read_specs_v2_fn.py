'''
                      cp_library by: kobejean                       
╺━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╸
                  A₀B₀A₁B₁A₂B₂A₃B₃A₄B₄A₅B₅A₆B₆A₇B₇              
                 ┏┿━┿━┿━┿━┿━┿━┿━┿━┿━┿━┿━┿━┿━┿━┿━┿━┓             
                 ┃├∧┤ ├∧┤ ├∧┤ ├∧┤ ├∧┤ ├∧┤ ├∧┤ ├∧┤ ┃             
        (RCA₈)   ┃└│⊕┐└│⊕┐└│⊕┐└│⊕┐└│⊕┐└│⊕┐└│⊕┐└│⊕┐┃             
                 ┃┌││⊕┌││⊕┌││⊕┌││⊕┌││⊕┌││⊕┌││⊕┌││⊕┃             
               C'╂│∨∧┴│∨∧┴│∨∧┴│∨∧┴│∨∧┴│∨∧┴│∨∧┴│∨∧┴╂C            
                 ┗┿━━━┿━━━┿━━━┿━━━┿━━━┿━━━┿━━━┿━━━┛             
                  S₀  S₁  S₂  S₃  S₄  S₅  S₆  S₇                
╺━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╸
'''
import typing

T = typing.TypeVar('T')
def read(spec: typing.Type[T]=[int]) -> T:
    def stream():
        while True: yield input()
    return parse_stream(stream(), spec)

def parse_stream(stream, spec: typing.Type[T]) -> T:
    from collections import deque
    from numbers import Number
    from typing import Collection, Callable

    def parse_tuple(cls, specs):
        match specs:
            case [spec, elip] if elip is ...:
                return cls(parse_line(spec))
            case specs:
                return cls(map(parse_spec, specs))

    def parse_collection(cls, specs):
        match specs:
            case [ ] | [_]:
                return cls(parse_line(*specs))
            case [spec, int() as n]:
                return cls(parse_spec(spec) for _ in range(n))
            case _:
                raise NotImplementedError(f"No spec definition for {specs}")

    def parse_spec(spec = int):
        match spec, type(spec):
            case int() as offset, cls:
                return cls(next_token()) + offset
            case (tuple(specs), cls) | (TupleSpec(cls, specs), _):
                return parse_tuple(cls, specs)
            case (list(specs), cls) | (CollectionSpec(cls, specs), _):
                return parse_collection(cls, specs)
            case cls, _:
                return cls(next_token())

    def parse_line(spec=int):
        if not queue: queue.extend(next_line())
        while queue: yield parse_spec(spec)
        
    def next_token():
        if not queue: queue.extend(next_line())
        return queue.popleft()
    
    def next_line():
        return next(stream).split()
    
    queue = deque(next_line()) 

    class TypeMatch(type):
        __match_args__ = ('__origin__', '__args__')
        def __instancecheck__(cls, other):
            match other:
                case type(__origin__=origin):
                    return issubclass(origin, cls.cls)
                case _:
                    return False 
    class CollectionSpec(metaclass=TypeMatch): cls = Collection
    class TupleSpec(metaclass=TypeMatch): cls = tuple

    return parse_spec(spec)

