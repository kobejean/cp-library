import cp_library.io.__header__

def write(*args, **kwargs):
    '''Prints the values to a stream, or to stdout_fast by default.'''
    sep, file = kwargs.pop("sep", " "), kwargs.pop("file", IO.stdout)
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        file.write(str(x))
        at_start = False
    file.write(kwargs.pop("end", "\n"))
    if kwargs.pop("flush", False):
        file.flush()
from cp_library.io.io_cls import IO