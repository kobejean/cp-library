import cp_library.io.__header__
import os
import sys
from io import BytesIO, IOBase


class FastIO(IOBase):
    BUFSIZE = 8192
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        BUFSIZE = self.BUFSIZE
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b: break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        BUFSIZE = self.BUFSIZE
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    stdin: 'IOWrapper' = None
    stdout: 'IOWrapper' = None
    
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable

    def write(self, s):
        return self.buffer.write(s.encode("ascii"))
    
    def read(self):
        return self.buffer.read().decode("ascii")
    
    def readline(self):
        return self.buffer.readline().decode("ascii")
try:
    sys.stdin = IOWrapper.stdin = IOWrapper(sys.stdin)
    sys.stdout = IOWrapper.stdout = IOWrapper(sys.stdout)
except:
    pass