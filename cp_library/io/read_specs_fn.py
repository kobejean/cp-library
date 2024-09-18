def read(*specs):
    return [*parse(input().split(), *specs)]

def parse(strs, *specs):
    def spec_def(spec):
        match spec:
            case int() as offset:
                return lambda s: int(s) + offset
            case func, *args if callable(func):
                return lambda s: func(s,*args)
            case func if callable(func):
                return func
    strs, funcs = iter(strs), map(spec_def, specs or (int,))
    for func in funcs: yield func(next(strs))
    yield from map(func, strs)