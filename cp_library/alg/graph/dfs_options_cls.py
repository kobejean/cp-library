import cp_library.alg.graph.__header__

from enum import auto, IntFlag, IntEnum

class DFSFlags(IntFlag):
    ENTER = auto()
    DOWN = auto()
    BACK = auto()
    CROSS = auto()
    LEAVE = auto()
    UP = auto()
    MAXDEPTH = auto()

    RETURN_PARENTS = auto()
    RETURN_DEPTHS = auto()
    BACKTRACK = auto()
    CONNECT_ROOTS = auto()

    # Common combinations
    ALL_EDGES = DOWN | BACK | CROSS
    EULER_TOUR = DOWN | UP
    INTERVAL = ENTER | LEAVE
    TOPDOWN = DOWN | CONNECT_ROOTS
    BOTTOMUP = UP | CONNECT_ROOTS
    RETURN_ALL = RETURN_PARENTS | RETURN_DEPTHS

class DFSEvent(IntEnum):
    ENTER = DFSFlags.ENTER 
    DOWN = DFSFlags.DOWN 
    BACK = DFSFlags.BACK 
    CROSS = DFSFlags.CROSS 
    LEAVE = DFSFlags.LEAVE 
    UP = DFSFlags.UP 
    MAXDEPTH = DFSFlags.MAXDEPTH
    
