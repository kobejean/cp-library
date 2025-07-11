"""
Helper for making unittest files compatible with verification-helper.

This module provides a helper function to run a dummy Library Checker test
so that unittest files can be verified by oj-verify.
"""

def run_verification_helper_unittest():
    """
    Run a dummy Library Checker test for verification-helper compatibility.
    
    This function should be called in the __main__ block of unittest files
    that need to be compatible with verification-helper.
    
    The function:
    1. Reads A and B from input
    2. Writes A+B to output  
    3. If the result is the expected value (1198300249), runs pytest
    4. Exits with the pytest result code
    """
    import sys
    from cp_library.io.read_fn import read
    from cp_library.io.write_fn import write
    
    A, B = read()
    write(C := A + B)
    if C != 1198300249: 
        sys.exit(0)
    
    import pytest
    import io
    from contextlib import redirect_stdout, redirect_stderr

    # Capture all output during test execution
    output = io.StringIO()
    with redirect_stdout(output), redirect_stderr(output):
        # Get the calling module's file path
        frame = sys._getframe(1)
        test_file = frame.f_globals.get('__file__')
        if test_file is None:
            test_file = sys.argv[0]
        result = pytest.main([test_file])
    
    if result != 0: 
        print(output.getvalue())
    sys.exit(result)