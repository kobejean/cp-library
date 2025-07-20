"""
Timing and measurement utilities for benchmarks.
Separated from main benchmark class for single responsibility.
"""

import time
from typing import Any, Callable, Tuple
from cp_library.perf.interfaces import TimerInterface
from cp_library.perf.checksum import result_checksum


class BenchmarkTimer(TimerInterface):
    """Handles timing and measurement of benchmark functions"""
    
    def __init__(self, iterations: int = 10, warmup: int = 2):
        self.iterations = iterations
        self.warmup = warmup
    
    def measure_time(self, func: Callable, data: Any, setup_func: Callable = None) -> Tuple[Any, float]:
        """Measure execution time with warmup and optional setup"""
        # Warmup runs
        for _ in range(self.warmup):
            try:
                if setup_func:
                    setup_data = setup_func(data)
                    func(setup_data)
                else:
                    func(data)
            except Exception:
                # If warmup fails, let the main measurement handle the error
                break
        
        # Actual measurement
        start = time.perf_counter()
        for _ in range(self.iterations):
            if setup_func:
                setup_data = setup_func(data)
                result = func(setup_data)
            else:
                result = func(data)
        elapsed_ms = (time.perf_counter() - start) * 1000 / self.iterations
        
        # Calculate checksum after timing with fallback for non-hashable types
        # This reduces overhead during the timed section
        checksum = result_checksum(result)
        
        return checksum, elapsed_ms