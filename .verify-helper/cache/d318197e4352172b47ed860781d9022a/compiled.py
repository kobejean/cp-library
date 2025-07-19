#!/Users/kobejean/miniforge3/bin/python3.12
"""This is a helper script to run the target Python code.

We need this script to set PYTHONPATH portably. The env command, quoting something, etc. are not portable or difficult to implement.
"""

import os
import sys

# arguments
path = '/Users/kobejean/Developer/GitHub/cp-library/test/atcoder/abc/abc249_f_min_k_heap.test.py'
basedir = '/Users/kobejean/Developer/GitHub/cp-library'

# run test/atcoder/abc/abc249_f_min_k_heap.test.py
env = dict(os.environ)
if "PYTHONPATH" in env:
    env["PYTHONPATH"] = basedir + os.pathsep + env["PYTHONPATH"] 
else:
    env["PYTHONPATH"] = basedir  # set `PYTHONPATH` to import files relative to the root directory
os.execve(sys.executable, [sys.executable, path], env=env)  # use `os.execve` to avoid making an unnecessary parent process
