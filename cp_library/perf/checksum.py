"""
Checksum utilities for benchmark validation.
Provides consistent ways to compute checksums across benchmarks.
"""

def update_checksum(current: int, value: int) -> int:
    """Update checksum with a single value using hash-like function."""
    return (current * 31 + value) & 0xFFFFFFFF