
def read(*specs: tuple[type]):
    S = input().split()
    return [func(s) for func, s in io_specs(specs, S)]

def io_specs(specs, S):
    def shift(shift):
        return lambda s: int(s) + shift
    def spec_func(spec):
        return shift(spec) if isinstance(spec, int) else spec
    if len(specs) > 1:
        return zip(map(spec_func, specs), S)
    func = spec_func(specs[0] if specs else int)
    return ((func, s) for s in S)
