import os
import tempfile
import subprocess
import base64
import zlib
from cffi import FFI

# Embed your C source code as a string
C_SOURCE = '''
#include <stdio.h>

int add(int a, int b) {
    return a + b;
}

int fibonacci(int n) {
    if (n <= 1) return n;
    return fibonacci(n-1) + fibonacci(n-2);
}
'''

def compile_c_code(source_code):
    with tempfile.TemporaryDirectory() as tmpdir:
        source_path = os.path.join(tmpdir, "source.c")
        with open(source_path, "w") as f:
            f.write(source_code)
        
        lib_path = os.path.join(tmpdir, "lib.so")
        compile_command = f"gcc -shared -fPIC -O3 -o {lib_path} {source_path}"
        
        try:
            subprocess.run(compile_command, shell=True, check=True, stderr=subprocess.PIPE)
        except subprocess.CalledProcessError as e:
            print(f"Compilation failed: {e.stderr.decode()}")
            return None

        with open(lib_path, "rb") as f:
            return f.read()

def compress_and_encode_library(lib_data):
    compressed_data = zlib.compress(lib_data, level=9)  # Highest compression level
    return base64.b64encode(compressed_data).decode()

def decode_and_decompress_library(encoded_data):
    compressed_data = base64.b64decode(encoded_data)
    return zlib.decompress(compressed_data)

def load_library(lib_data):
    fd, path = tempfile.mkstemp(suffix='.so')
    try:
        with os.fdopen(fd, 'wb') as tmp:
            tmp.write(lib_data)
        
        ffi = FFI()
        ffi.cdef('''
            int add(int a, int b);
            int fibonacci(int n);
        ''')
        
        return ffi.dlopen(path)
    except Exception as e:
        print(f"Error loading library: {e}")
        return None
    finally:
        os.unlink(path)

def main():
    # Compile the C code
    lib_data = compile_c_code(C_SOURCE)
    if lib_data is None:
        return 1

    # Compress, encode, and print the library data
    encoded_lib = compress_and_encode_library(lib_data)
    print("Compressed and base64 encoded library:")
    print(encoded_lib)
    print(f"\nEncoded length: {len(encoded_lib)} characters")
    print("\nYou can copy this encoded string and use it in your script.")

    # For demonstration, we'll decode, decompress, and load the library
    decoded_lib_data = decode_and_decompress_library(encoded_lib)
    lib = load_library(decoded_lib_data)
    if lib is None:
        return 1

    # Use the compiled C functions
    result_add = lib.add(2, 3)
    print(f"\nResult of 2 + 3 = {result_add}")

    result_fib = lib.fibonacci(10)
    print(f"10th Fibonacci number = {result_fib}")

    return 0

if __name__ == "__main__":
    exit(main())
