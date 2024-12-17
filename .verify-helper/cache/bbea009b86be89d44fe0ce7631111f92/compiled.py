#!/Users/kobejean/miniforge3/envs/atcoder/bin/pypy
"""This is a helper script to run the target Python code.

We need this script to set PYTHONPATH portably. The env command, quoting something, etc. are not portable or difficult to implement.
"""

import os
import sys

# arguments
path = '/Users/kobejean/Developer/GitHub/cp-library/test/dp_z_cht_monotone_add_min.test.py'
basedir = '/Users/kobejean/Developer/GitHub/cp-library'

# run test/dp_z_cht_monotone_add_min.test.py
env = dict(os.environ)
if "PYTHONPATH" in env:
    env["PYTHONPATH"] = basedir + os.pathsep + env["PYTHONPATH"] 
else:
    env["PYTHONPATH"] = basedir  # set `PYTHONPATH` to import files relative to the root directory
os.execve(sys.executable, [sys.executable, path], env=env)  # use `os.execve` to avoid making an unnecessary parent process
