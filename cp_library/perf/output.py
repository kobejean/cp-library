"""
Output management for benchmark results.
"""

import json
import time
from pathlib import Path
from typing import List, Any
from cp_library.perf.interfaces import OutputManager, BenchmarkResult


class JSONOutputManager(OutputManager):
    """Output manager that saves results to JSON files"""
    
    def __init__(self, output_dir: str = "./output/benchmark_results"):
        self.output_dir = Path(output_dir)
    
    def save_results(self, results: List[BenchmarkResult], config: Any) -> None:
        """Save benchmark results to JSON"""
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # Convert results to dictionaries for JSON serialization
        results_dict = [
            {
                'operation': r.operation,
                'size': r.size,
                'implementation': r.implementation,
                'time_ms': r.time_ms,
                'correct': r.correct,
                'error': r.error
            }
            for r in results
        ]
        
        # Use config name if available, otherwise default name
        name = getattr(config, 'name', 'benchmark') if config else 'benchmark'
        filename = self.output_dir / f"{name}_{int(time.time())}.json"
        
        with open(filename, 'w') as f:
            json.dump(results_dict, f, indent=2)
        
        print(f"\nResults saved to {filename}")


class NoOpOutputManager(OutputManager):
    """Output manager that does nothing (for testing or when output is disabled)"""
    
    def save_results(self, results: List[BenchmarkResult], config: Any) -> None:
        """No-op implementation"""
        pass