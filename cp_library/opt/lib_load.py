ENCODED_BINARY = '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'
import os
import tempfile
import base64
import zlib
from cffi import FFI

def compress_and_encode_library(lib_data):
    compressed_data = zlib.compress(lib_data, level=9)
    return base64.b64encode(compressed_data).decode()

def decode_and_decompress_library(encoded_data):
    compressed_data = base64.b64decode(encoded_data)
    return zlib.decompress(compressed_data)

def load_library(lib_data, ffi_instance):
    fd, path = tempfile.mkstemp(suffix='.so')
    try:
        with os.fdopen(fd, 'wb') as tmp:
            tmp.write(lib_data)
        
        return ffi_instance.dlopen(path)
    except Exception as e:
        # print(f"Error loading library: {e}")
        return None
    finally:
        os.unlink(path)

ffi = FFI()
ffi.cdef('''
    int64_t mod_inv(int64_t a, int64_t mod);
''')
decoded_lib_data = decode_and_decompress_library(ENCODED_BINARY)
lib = load_library(decoded_lib_data, ffi)

def mod_inv(a, mod):
    if inv := lib.mod_inv(a, mod):
        return inv
    raise ValueError("No inverse!")

def test(a, mod):
    x = mod_inv(a, mod)
    y = pow(a,-1,mod)
    assert x == y