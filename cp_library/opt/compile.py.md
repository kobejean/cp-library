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
  bundledCode: "import os\nimport tempfile\nimport subprocess\nimport base64\nimport\
    \ zlib\nfrom cffi import FFI\n\n# Embed your C source code as a string\nC_SOURCE\
    \ = '''\n#include <stdio.h>\n\nint add(int a, int b) {\n    return a + b;\n}\n\
    \nint fibonacci(int n) {\n    if (n <= 1) return n;\n    return fibonacci(n-1)\
    \ + fibonacci(n-2);\n}\n'''\n\ndef compile_c_code(source_code):\n    with tempfile.TemporaryDirectory()\
    \ as tmpdir:\n        source_path = os.path.join(tmpdir, \"source.c\")\n     \
    \   with open(source_path, \"w\") as f:\n            f.write(source_code)\n  \
    \      \n        lib_path = os.path.join(tmpdir, \"lib.so\")\n        compile_command\
    \ = f\"gcc -shared -fPIC -O3 -o {lib_path} {source_path}\"\n        \n       \
    \ try:\n            subprocess.run(compile_command, shell=True, check=True, stderr=subprocess.PIPE)\n\
    \        except subprocess.CalledProcessError as e:\n            print(f\"Compilation\
    \ failed: {e.stderr.decode()}\")\n            return None\n\n        with open(lib_path,\
    \ \"rb\") as f:\n            return f.read()\n\ndef compress_and_encode_library(lib_data):\n\
    \    compressed_data = zlib.compress(lib_data, level=9)  # Highest compression\
    \ level\n    return base64.b64encode(compressed_data).decode()\n\ndef decode_and_decompress_library(encoded_data):\n\
    \    compressed_data = base64.b64decode(encoded_data)\n    return zlib.decompress(compressed_data)\n\
    \ndef load_library(lib_data):\n    fd, path = tempfile.mkstemp(suffix='.so')\n\
    \    try:\n        with os.fdopen(fd, 'wb') as tmp:\n            tmp.write(lib_data)\n\
    \        \n        ffi = FFI()\n        ffi.cdef('''\n            int add(int\
    \ a, int b);\n            int fibonacci(int n);\n        ''')\n        \n    \
    \    return ffi.dlopen(path)\n    except Exception as e:\n        print(f\"Error\
    \ loading library: {e}\")\n        return None\n    finally:\n        os.unlink(path)\n\
    \ndef main():\n    # Compile the C code\n    lib_data = compile_c_code(C_SOURCE)\n\
    \    if lib_data is None:\n        return 1\n\n    # Compress, encode, and print\
    \ the library data\n    encoded_lib = compress_and_encode_library(lib_data)\n\
    \    print(\"Compressed and base64 encoded library:\")\n    print(encoded_lib)\n\
    \    print(f\"\\nEncoded length: {len(encoded_lib)} characters\")\n    print(\"\
    \\nYou can copy this encoded string and use it in your script.\")\n\n    # For\
    \ demonstration, we'll decode, decompress, and load the library\n    decoded_lib_data\
    \ = decode_and_decompress_library(encoded_lib)\n    lib = load_library(decoded_lib_data)\n\
    \    if lib is None:\n        return 1\n\n    # Use the compiled C functions\n\
    \    result_add = lib.add(2, 3)\n    print(f\"\\nResult of 2 + 3 = {result_add}\"\
    )\n\n    result_fib = lib.fibonacci(10)\n    print(f\"10th Fibonacci number =\
    \ {result_fib}\")\n\n    return 0\n\nif __name__ == \"__main__\":\n    exit(main())\n"
  code: "import os\nimport tempfile\nimport subprocess\nimport base64\nimport zlib\n\
    from cffi import FFI\n\n# Embed your C source code as a string\nC_SOURCE = '''\n\
    #include <stdio.h>\n\nint add(int a, int b) {\n    return a + b;\n}\n\nint fibonacci(int\
    \ n) {\n    if (n <= 1) return n;\n    return fibonacci(n-1) + fibonacci(n-2);\n\
    }\n'''\n\ndef compile_c_code(source_code):\n    with tempfile.TemporaryDirectory()\
    \ as tmpdir:\n        source_path = os.path.join(tmpdir, \"source.c\")\n     \
    \   with open(source_path, \"w\") as f:\n            f.write(source_code)\n  \
    \      \n        lib_path = os.path.join(tmpdir, \"lib.so\")\n        compile_command\
    \ = f\"gcc -shared -fPIC -O3 -o {lib_path} {source_path}\"\n        \n       \
    \ try:\n            subprocess.run(compile_command, shell=True, check=True, stderr=subprocess.PIPE)\n\
    \        except subprocess.CalledProcessError as e:\n            print(f\"Compilation\
    \ failed: {e.stderr.decode()}\")\n            return None\n\n        with open(lib_path,\
    \ \"rb\") as f:\n            return f.read()\n\ndef compress_and_encode_library(lib_data):\n\
    \    compressed_data = zlib.compress(lib_data, level=9)  # Highest compression\
    \ level\n    return base64.b64encode(compressed_data).decode()\n\ndef decode_and_decompress_library(encoded_data):\n\
    \    compressed_data = base64.b64decode(encoded_data)\n    return zlib.decompress(compressed_data)\n\
    \ndef load_library(lib_data):\n    fd, path = tempfile.mkstemp(suffix='.so')\n\
    \    try:\n        with os.fdopen(fd, 'wb') as tmp:\n            tmp.write(lib_data)\n\
    \        \n        ffi = FFI()\n        ffi.cdef('''\n            int add(int\
    \ a, int b);\n            int fibonacci(int n);\n        ''')\n        \n    \
    \    return ffi.dlopen(path)\n    except Exception as e:\n        print(f\"Error\
    \ loading library: {e}\")\n        return None\n    finally:\n        os.unlink(path)\n\
    \ndef main():\n    # Compile the C code\n    lib_data = compile_c_code(C_SOURCE)\n\
    \    if lib_data is None:\n        return 1\n\n    # Compress, encode, and print\
    \ the library data\n    encoded_lib = compress_and_encode_library(lib_data)\n\
    \    print(\"Compressed and base64 encoded library:\")\n    print(encoded_lib)\n\
    \    print(f\"\\nEncoded length: {len(encoded_lib)} characters\")\n    print(\"\
    \\nYou can copy this encoded string and use it in your script.\")\n\n    # For\
    \ demonstration, we'll decode, decompress, and load the library\n    decoded_lib_data\
    \ = decode_and_decompress_library(encoded_lib)\n    lib = load_library(decoded_lib_data)\n\
    \    if lib is None:\n        return 1\n\n    # Use the compiled C functions\n\
    \    result_add = lib.add(2, 3)\n    print(f\"\\nResult of 2 + 3 = {result_add}\"\
    )\n\n    result_fib = lib.fibonacci(10)\n    print(f\"10th Fibonacci number =\
    \ {result_fib}\")\n\n    return 0\n\nif __name__ == \"__main__\":\n    exit(main())\n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/opt/compile.py
  requiredBy: []
  timestamp: '2025-07-26 11:14:31+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/opt/compile.py
layout: document
redirect_from:
- /library/cp_library/opt/compile.py
- /library/cp_library/opt/compile.py.html
title: cp_library/opt/compile.py
---
