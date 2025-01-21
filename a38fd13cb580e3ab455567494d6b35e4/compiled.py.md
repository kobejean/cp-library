---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "#!/Users/kobejean/miniforge3/envs/atcoder/bin/pypy\n\"\"\"This is\
    \ a helper script to run the target Python code.\n\nWe need this script to set\
    \ PYTHONPATH portably. The env command, quoting something, etc. are not portable\
    \ or difficult to implement.\n\"\"\"\n\nimport os\nimport sys\n\n# arguments\n\
    path = '/Users/kobejean/Developer/GitHub/cp-library/test/agc038_b_sliding_min_max.test.py'\n\
    basedir = '/Users/kobejean/Developer/GitHub/cp-library'\n\n# run test/agc038_b_sliding_min_max.test.py\n\
    env = dict(os.environ)\nif \"PYTHONPATH\" in env:\n    env[\"PYTHONPATH\"] = basedir\
    \ + os.pathsep + env[\"PYTHONPATH\"] \nelse:\n    env[\"PYTHONPATH\"] = basedir\
    \  # set `PYTHONPATH` to import files relative to the root directory\nos.execve(sys.executable,\
    \ [sys.executable, path], env=env)  # use `os.execve` to avoid making an unnecessary\
    \ parent process\n"
  code: "#!/Users/kobejean/miniforge3/envs/atcoder/bin/pypy\n\"\"\"This is a helper\
    \ script to run the target Python code.\n\nWe need this script to set PYTHONPATH\
    \ portably. The env command, quoting something, etc. are not portable or difficult\
    \ to implement.\n\"\"\"\n\nimport os\nimport sys\n\n# arguments\npath = '/Users/kobejean/Developer/GitHub/cp-library/test/agc038_b_sliding_min_max.test.py'\n\
    basedir = '/Users/kobejean/Developer/GitHub/cp-library'\n\n# run test/agc038_b_sliding_min_max.test.py\n\
    env = dict(os.environ)\nif \"PYTHONPATH\" in env:\n    env[\"PYTHONPATH\"] = basedir\
    \ + os.pathsep + env[\"PYTHONPATH\"] \nelse:\n    env[\"PYTHONPATH\"] = basedir\
    \  # set `PYTHONPATH` to import files relative to the root directory\nos.execve(sys.executable,\
    \ [sys.executable, path], env=env)  # use `os.execve` to avoid making an unnecessary\
    \ parent process\n"
  dependsOn: []
  isVerificationFile: false
  path: a38fd13cb580e3ab455567494d6b35e4/compiled.py
  requiredBy: []
  timestamp: '2025-01-21 21:57:07+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: a38fd13cb580e3ab455567494d6b35e4/compiled.py
layout: document
redirect_from:
- /library/a38fd13cb580e3ab455567494d6b35e4/compiled.py
- /library/a38fd13cb580e3ab455567494d6b35e4/compiled.py.html
title: a38fd13cb580e3ab455567494d6b35e4/compiled.py
---
