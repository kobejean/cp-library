"""
Minimal checksum utilities for benchmark validation.
"""

def update_checksum(current: int, value: int) -> int:
    """Update checksum with a single value."""
    return (current * 31 + value) & 0xFFFFFFFF