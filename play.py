from cffi import FFI
from enum import IntEnum
from math import isqrt

class MoOp(IntEnum):
    ADD_LEFT = 0
    REMOVE_LEFT = 1
    ADD_RIGHT = 2
    REMOVE_RIGHT = 3
    ANSWER = 4

ffi = FFI()

ffi.cdef("""
    void process_queries(unsigned long long* ops, int* op_count,
                        unsigned long long* queries, int Q, int N,
                        int qbits, int nbits);
""")

lib = ffi.verify("""
    #include <stdlib.h>
    #include <math.h>
    
    static inline int decode_i(unsigned long long bits, int qbits) {
        return bits & ((1ULL << qbits) - 1);
    }
    
    static inline int decode_l(unsigned long long bits, int qbits, int nbits) {
        return (bits >> qbits) & ((1ULL << nbits) - 1);
    }
    
    static inline int decode_r(unsigned long long bits, int qbits, int nbits) {
        return bits >> (qbits + nbits);
    }
    
    static inline unsigned long long encode_op(unsigned char op, int a, int b, int c) {
        // Ensure op is only using 3 bits (0-7)
        unsigned long long result = ((unsigned long long)(op & 7) << 61);
        // Use 20 bits each for a, b
        result |= ((unsigned long long)(a & 0xFFFFF) << 41);
        result |= ((unsigned long long)(b & 0xFFFFF) << 21);
        // Handle c specially for negative numbers
        if (c < 0) {
            result |= (1ULL << 20);  // Set sign bit
            result |= (unsigned long long)((-c) & 0xFFFFF);
        } else {
            result |= (unsigned long long)(c & 0xFFFFF);
        }
        return result;
    }
    
    static int g_qbits;
    static int g_nbits;
    static int g_block_size;
    
    static int compare_queries(const void* a, const void* b) {
        unsigned long long qa = *(const unsigned long long*)a;
        unsigned long long qb = *(const unsigned long long*)b;
        
        int l_a = decode_l(qa, g_qbits, g_nbits);
        int l_b = decode_l(qb, g_qbits, g_nbits);
        
        int block_a = l_a / g_block_size;
        int block_b = l_b / g_block_size;
        
        if (block_a != block_b) 
            return block_a - block_b;
        
        int r_a = decode_r(qa, g_qbits, g_nbits);
        int r_b = decode_r(qb, g_qbits, g_nbits);
        
        return (block_a & 1) ? (r_b - r_a) : (r_a - r_b);
    }
    
    void process_queries(unsigned long long* ops, int* op_count,
                        unsigned long long* queries, int Q, int N,
                        int qbits, int nbits) {
        g_qbits = qbits;
        g_nbits = nbits;
        g_block_size = (int)sqrt(N);
        
        qsort(queries, Q, sizeof(unsigned long long), compare_queries);
        
        int nl = 0, nr = 0;
        int op_idx = 0;
        
        for (int q = 0; q < Q; q++) {
            unsigned long long query = queries[q];
            int i = decode_i(query, qbits);
            int l = decode_l(query, qbits, nbits);
            int r = decode_r(query, qbits, nbits);
            
            if (l < nl) {
                ops[op_idx++] = encode_op(0, nl - 1, l - 1, -1);  // ADD_LEFT
            } 
            else if (l > nl) {
                ops[op_idx++] = encode_op(1, nl, l, 1);  // REMOVE_LEFT
            }
            
            if (r > nr) {
                ops[op_idx++] = encode_op(2, nr, r, 1);  // ADD_RIGHT
            }
            else if (r < nr) {
                ops[op_idx++] = encode_op(3, nr - 1, r - 1, -1);  // REMOVE_RIGHT
            }
            
            ops[op_idx++] = encode_op(4, i, l, r);  // ANSWER
            
            nl = l;
            nr = r;
        }
        
        *op_count = op_idx;
    }
""",  extra_compile_args=['-O3', '-march=native', '-ffast-math'], extra_link_args=['-O3'])

class MoAlgorithm:
    def encode(self, i, l, r):
        return (((r << self.nbits) + l) << self.qbits) + i
    
    def decode_op(self, encoded):
        op = (encoded >> 61) & 7  # Get 3 bits for op
        a = (encoded >> 41) & 0xFFFFF  # Get 20 bits for a
        b = (encoded >> 21) & 0xFFFFF  # Get 20 bits for b
        c = encoded & 0xFFFFF  # Get value bits
        sign = (encoded >> 20) & 1  # Get sign bit
        if sign:
            c = -c
        return MoOp(op), a, b, c

    def __init__(self, queries: list[tuple[int, int]], N: int):
        Q = len(queries)
        self.qbits = Q.bit_length()
        self.nbits = N.bit_length()
        
        # Encode queries
        encoded_queries = [self.encode(i, l, r) for i, (l, r) in enumerate(queries)]
        
        # Prepare C arrays
        query_arr = ffi.new("unsigned long long[]", encoded_queries)
        max_ops = 3 * Q
        op_arr = ffi.new("unsigned long long[]", max_ops)
        op_count = ffi.new("int*", 0)
        
        # Process queries and generate operations
        lib.process_queries(op_arr, op_count, query_arr, Q, N, 
                          self.qbits, self.nbits)
        
        # Convert to Python list and decode operations
        self.ops = []
        for i in range(op_count[0]):
            self.ops.append(self.decode_op(op_arr[i]))

# Test and debug
def test():
    queries = [(0, 3), (1, 4), (2, 5), (0, 2), (3, 5), (2, 3)]
    N = 6
    
    mo = MoAlgorithm(queries, N)
    
    print("Generated Operations:")
    for op in mo.ops:
        print(op)

if __name__ == "__main__":
    test()