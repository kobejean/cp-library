# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/1/ITP1_1_A

import pytest
import io

class TestIOBytes:
    def test_initialization(self):
        """Test basic initialization of IO class"""
        buffer = io.BytesIO(b"test\n")
        test_io = IOBytes(buffer)
        
        assert test_io.char == False
        assert test_io.l == 0
        assert test_io.p == 0
        assert test_io.st == []
        assert test_io.ist == []

    def test_readtoken(self):
        """Test readtoken method"""
        buffer = io.BytesIO(b"hello world test\n")
        test_io = IOBytes(buffer)
        
        assert test_io.readtoken() == "hello"
        assert test_io.readtoken() == "world"
        assert test_io.readtoken() == "test"

    def test_readtokens(self):
        """Test readtokens method"""
        buffer = io.BytesIO(b"hello world test\n")
        test_io = IOBytes(buffer)
        
        tokens = test_io.readtokens()
        assert tokens == ["hello", "world", "test"]

    def test_readints(self):
        """Test readints method"""
        buffer = io.BytesIO(b"10 -20 300 -4000\n")
        test_io = IOBytes(buffer)
        
        ints = test_io.readints()
        assert ints == [10, -20, 300, -4000]

    def test_readints_single_line(self):
        """Test readints with various integer formats"""
        buffer = io.BytesIO(b"0 1 -1 42 -999 1000000\n")
        test_io = IOBytes(buffer)
        
        ints = test_io.readints()
        assert ints == [0, 1, -1, 42, -999, 1000000]

    def test_readdigits_char_mode(self):
        """Test readdigits method in char mode"""
        buffer = io.BytesIO(b"12345\n")
        test_io = IOBytes(buffer)
        test_io.char = True
        
        digits = test_io.readdigits()
        assert digits == [1, 2, 3, 4, 5]

    def test_readdigits_mixed_chars(self):
        """Test readdigits with mixed characters"""
        buffer = io.BytesIO(b"1a2b3c\n")
        test_io = IOBytes(buffer)
        test_io.char = True
        
        digits = test_io.readdigits()
        assert digits == [1, 2, 3]

    def test_readnums_token_mode(self):
        """Test readnums in token mode (should use readints)"""
        buffer = io.BytesIO(b"10 -20 300\n")
        test_io = IOBytes(buffer)
        test_io.char = False
        
        nums = test_io.readnums()
        assert nums == [10, -20, 300]

    def test_readnums_char_mode(self):
        """Test readnums in char mode (should use readdigits)"""
        buffer = io.BytesIO(b"12345\n")
        test_io = IOBytes(buffer)
        test_io.char = True
        
        nums = test_io.readnums()
        assert nums == [1, 2, 3, 4, 5]

    def test_readchar(self):
        """Test readchar method"""
        buffer = io.BytesIO(b"abc\n")
        test_io = IOBytes(buffer)
        test_io.char = True
        
        assert test_io.readchar() == "a"
        assert test_io.readchar() == "b"
        assert test_io.readchar() == "c"

    def test_readchars(self):
        """Test readchars method"""
        buffer = io.BytesIO(b"hello\n")
        test_io = IOBytes(buffer)
        test_io.char = True
        
        chars = test_io.readchars()
        assert chars == "hello"

    def test_readline(self):
        """Test readline method"""
        buffer = io.BytesIO(b"first line\nsecond line\n")
        test_io = IOBytes(buffer)
        
        assert test_io.readline() == "first line\n"
        assert test_io.readline() == "second line\n"

    def test_readinto_token_mode(self):
        """Test readinto in token mode"""
        buffer = io.BytesIO(b"hello world\n")
        test_io = IOBytes(buffer)
        test_io.char = False
        
        lst = []
        result = test_io.readinto(lst)
        assert result == ["hello", "world"]
        assert lst == ["hello", "world"]

    def test_readinto_char_mode(self):
        """Test readinto in char mode"""
        buffer = io.BytesIO(b"hello\n")
        test_io = IOBytes(buffer)
        test_io.char = True
        
        lst = []
        result = test_io.readinto(lst)
        assert "".join(result) == "hello"
        assert "".join(lst) == "hello"
        assert result == ['h', 'e', 'l', 'l', 'o']
        assert lst == ['h', 'e', 'l', 'l', 'o']

    def test_readtokensinto(self):
        """Test readtokensinto method"""
        buffer = io.BytesIO(b"one two three\n")
        test_io = IOBytes(buffer)
        
        lst = ["existing"]
        result = test_io.readtokensinto(lst)
        assert result == ["existing", "one", "two", "three"]
        assert lst == ["existing", "one", "two", "three"]

    def test_readintsinto(self):
        """Test readintsinto method"""
        buffer = io.BytesIO(b"10 -20 30\n")
        test_io = IOBytes(buffer)
        
        lst = [99]
        result = test_io.readintsinto(lst)
        assert result == [99, 10, -20, 30]
        assert lst == [99, 10, -20, 30]

    def test_readdigitsinto(self):
        """Test readdigitsinto method"""
        buffer = io.BytesIO(b"123a45\n")
        test_io = IOBytes(buffer)
        
        lst = [9]
        result = test_io.readdigitsinto(lst)
        assert result == [9, 1, 2, 3, 4, 5]
        assert lst == [9, 1, 2, 3, 4, 5]

    def test_readnumsinto_token_mode(self):
        """Test readnumsinto in token mode"""
        buffer = io.BytesIO(b"10 -20 30\n")
        test_io = IOBytes(buffer)
        test_io.char = False
        
        lst = []
        result = test_io.readnumsinto(lst)
        assert result == [10, -20, 30]
        assert lst == [10, -20, 30]

    def test_readnumsinto_char_mode(self):
        """Test readnumsinto in char mode"""
        buffer = io.BytesIO(b"12345\n")
        test_io = IOBytes(buffer)
        test_io.char = True
        
        lst = []
        result = test_io.readnumsinto(lst)
        assert result == [1, 2, 3, 4, 5]
        assert lst == [1, 2, 3, 4, 5]

    def test_line_token_mode(self):
        """Test line method in token mode"""
        buffer = io.BytesIO(b"hello world test\n")
        test_io = IOBytes(buffer)
        test_io.char = False
        
        line_data = test_io.line()
        assert line_data == ["hello", "world", "test"]

    def test_line_char_mode(self):
        """Test line method in char mode"""
        buffer = io.BytesIO(b"hello\n")
        test_io = IOBytes(buffer)
        test_io.char = True
        
        line_data = test_io.line()
        assert "".join(line_data) == "hello"
        assert line_data == ['h', 'e', 'l', 'l', 'o']
        assert len(line_data) == 5

    def test_next_token_mode(self):
        """Test __next__ method in token mode"""
        buffer = io.BytesIO(b"hello world\n")
        test_io = IOBytes(buffer)
        test_io.char = False
        
        assert next(test_io) == "hello"
        assert next(test_io) == "world"

    def test_next_char_mode(self):
        """Test __next__ method in char mode"""
        buffer = io.BytesIO(b"abc\n")
        test_io = IOBytes(buffer)
        test_io.char = True
        
        assert next(test_io) == "a"
        assert next(test_io) == "b"
        assert next(test_io) == "c"

    def test_multiline_tokens(self):
        """Test reading tokens across multiple lines"""
        buffer = io.BytesIO(b"line1 data\nline2 more\n")
        test_io = IOBytes(buffer)
        
        # First line
        tokens1 = test_io.readtokens()
        assert tokens1 == ["line1", "data"]
        
        # Second line
        tokens2 = test_io.readtokens()
        assert tokens2 == ["line2", "more"]

    def test_multiline_ints(self):
        """Test reading integers across multiple lines"""
        buffer = io.BytesIO(b"10 20\n30 40\n")
        test_io = IOBytes(buffer)
        
        # First line
        ints1 = test_io.readints()
        assert ints1 == [10, 20]
        
        # Second line  
        ints2 = test_io.readints()
        assert ints2 == [30, 40]

    def test_empty_line(self):
        """Test handling empty lines"""
        buffer = io.BytesIO(b"\n")
        test_io = IOBytes(buffer)
        
        tokens = test_io.readtokens()
        assert tokens == [""]

    def test_single_integer(self):
        """Test reading single integer"""
        buffer = io.BytesIO(b"42\n")
        test_io = IOBytes(buffer)
        
        ints = test_io.readints()
        assert ints == [42]

    def test_single_digit(self):
        """Test reading single digit in char mode"""
        buffer = io.BytesIO(b"7\n")
        test_io = IOBytes(buffer)
        test_io.char = True
        
        digits = test_io.readdigits()
        assert digits == [7]

    def test_zero_handling(self):
        """Test proper handling of zero values"""
        buffer = io.BytesIO(b"0 00 000\n")
        test_io = IOBytes(buffer)
        
        ints = test_io.readints()
        assert ints == [0, 0, 0]

    def test_negative_zero(self):
        """Test handling of negative zero"""
        buffer = io.BytesIO(b"-0\n")
        test_io = IOBytes(buffer)
        
        ints = test_io.readints()
        assert ints == [0]

    def test_large_numbers(self):
        """Test handling of large numbers"""
        buffer = io.BytesIO(b"1000000000 -1000000000\n")
        test_io = IOBytes(buffer)
        
        ints = test_io.readints()
        assert ints == [1000000000, -1000000000]

    def test_digits_with_linebreak(self):
        """Test digits reading stops at linebreak and advances line"""
        buffer = io.BytesIO(b"123\n456\n")
        test_io = IOBytes(buffer)
        test_io.char = True
        
        # First line digits
        digits1 = test_io.readdigits()
        assert digits1 == [1, 2, 3]
        
        # Second line digits 
        digits2 = test_io.readdigits()
        assert digits2 == [4, 5, 6]

    def test_mixed_whitespace(self):
        """Test handling various whitespace characters"""
        buffer = io.BytesIO(b"10  20   30\n")
        test_io = IOBytes(buffer)
        
        ints = test_io.readints()
        assert ints == [10, 20, 30]

    def test_char_mode_individual_access(self):
        """Test individual character access in char mode"""
        buffer = io.BytesIO(b"abc123\n")
        test_io = IOBytes(buffer)
        test_io.char = True
        
        line_data = test_io.line()
        assert line_data[0] == 'a'
        assert line_data[1] == 'b' 
        assert line_data[2] == 'c'
        assert line_data[3] == '1'
        assert line_data[4] == '2'
        assert line_data[5] == '3'
        assert len(line_data) == 6

    def test_char_mode_readcharsinto_individual(self):
        """Test readcharsinto individual character behavior"""
        buffer = io.BytesIO(b"test\n")
        test_io = IOBytes(buffer)
        
        lst = ['start']
        result = test_io.readcharsinto(lst)
        # readcharsinto extends with string characters
        assert lst == ['start', 't', 'e', 's', 't']
        assert result == ['start', 't', 'e', 's', 't']

from cp_library.io.io_bytes_cls import IOBytes

if __name__ == '__main__':
    from cp_library.test.unittest_helper import run_verification_helper_unittest
    run_verification_helper_unittest()