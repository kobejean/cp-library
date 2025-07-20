"""
Checksum utilities for benchmark validation.
Provides consistent ways to compute checksums across benchmarks.
"""

from typing import Any


def update_checksum(current: int, value: int) -> int:
    """Update checksum with a single value using hash-like function."""
    return (current * 31 + value) & 0xFFFFFFFF


def result_checksum(result: Any) -> Any:
    """
    Calculate checksum for benchmark result with fallback for non-hashable types.
    
    This function tries to create a consistent hash for any type of result,
    with intelligent fallbacks for common non-hashable types like lists, sets, and dicts.
    
    Args:
        result: The result to checksum (can be any type)
        
    Returns:
        Hash value if successful, original result if all fallbacks fail
    """
    # Try direct hash first (fastest path for hashable objects)
    try:
        return hash(result)
    except TypeError:
        pass
    
    # Try common fallback conversions for non-hashable types
    try:
        if isinstance(result, dict):
            # Convert dict to sorted tuple of items for consistent ordering
            return hash(tuple(sorted(result.items())))
        elif isinstance(result, set):
            # Convert set to sorted tuple for consistent ordering
            return hash(tuple(sorted(result)))
        elif _is_iterable_not_string(result):
            # Convert other iterables (lists, etc.) to tuple
            return hash(tuple(result))
        elif hasattr(result, '__dict__'):
            # Convert objects with attributes to tuple of sorted items
            return hash(tuple(sorted(result.__dict__.items())))
        else:
            # For other types, convert to string as last resort
            return hash(str(result))
    except (TypeError, RecursionError):
        # If all fallbacks fail, return the original result
        # The validation logic will handle it
        return result


def _is_iterable_not_string(obj: Any) -> bool:
    """
    Check if object is iterable but not a string or bytes.
    
    Uses both __iter__ and __getitem__ checks to catch more iterable types
    while excluding strings and bytes which should be handled differently.
    """
    return (
        (hasattr(obj, '__iter__') or hasattr(obj, '__getitem__')) 
        and not isinstance(obj, (str, bytes))
    )