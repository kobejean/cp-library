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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 101, in bundle\n    return bundler.update(path)\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python_bundle.py\"\
    , line 154, in update\n    self.process_file(path)\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python_bundle.py\"\
    , line 23, in process_file\n    tree = ast.parse(source)\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/ast.py\"\
    , line 50, in parse\n    return compile(source, filename, mode, flags,\n  File\
    \ \"<unknown>\", line 6\n    Va, La, Ra, I = G.Va, G.La, G.Ra, G.La[:]\nIndentationError:\
    \ unexpected indent\n"
  code: "\nfrom __pypy__ import strategy\nA = [False]*10\nprint(strategy(A))\n\n \
    \   Va, La, Ra, I = G.Va, G.La, G.Ra, G.La[:]\n    G.state, G.stack = state, stack\
    \ = u8a(G.N), elist(G.N)\n    for s in G.starts(s):\n        if state[s]: continue\n\
    \        stack.append(s)\n        # DOWN ROOT\n        while stack:\n        \
    \    if state[u := stack[-1]] == 0:\n                state[u] = 1\n          \
    \      # ENTER NODE\n            if (i := I[u]) < Ra[u]:\n                I[u]\
    \ += 1\n                if (s := state[v := Va[i]]) == 0:\n                  \
    \  stack.append(v)\n                    # DOWN/TREE EDGE\n                elif\
    \ s == 1:\n                    # BACK EDGE\n                    pass\n       \
    \         elif s == 2:\n                    # CROSS EDGE\n                   \
    \ pass\n            else:\n                stack.pop()\n                state[u]\
    \ = 2\n                # UNCOMMENT IF BACKTRACKING\n                # state[u],\
    \ I[u] = 0, La[u]\n\n                # LEAVE NODE\n                if stack:\n\
    \                    # UP/TREE EDGE\n                    # v = stack[-1]\n   \
    \                 pass\n        # UP ROOT"
  dependsOn: []
  isVerificationFile: false
  path: play.py
  requiredBy: []
  timestamp: '2024-12-29 16:20:36+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: play.py
layout: document
redirect_from:
- /library/play.py
- /library/play.py.html
title: play.py
---
