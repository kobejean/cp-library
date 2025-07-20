"""
Command-line interface for the benchmark framework.
"""

import argparse
import sys
from typing import List, Optional
from dataclasses import dataclass


@dataclass
class CLIConfig:
    """Configuration parsed from command line arguments"""
    profile_mode: bool = False
    operation: Optional[str] = None
    size: Optional[int] = None
    implementation: Optional[str] = None


class BenchmarkCLI:
    """Command-line interface handler"""
    
    def __init__(self, name: str, operations: List[str], sizes: List[int]):
        self.name = name
        self.operations = operations
        self.sizes = sizes
    
    def parse_args(self) -> CLIConfig:
        """Parse command line arguments"""
        parser = argparse.ArgumentParser(
            description=f"Benchmark {self.name} with optional profiling mode",
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog="""
Examples:
  # Normal benchmark mode (all operations and sizes)
  python benchmark.py
  
  # Normal mode with specific operation
  python benchmark.py --operation access
  
  # Normal mode with specific size
  python benchmark.py --size 1000
  
  # Normal mode with specific operation and size
  python benchmark.py --operation access --size 100
  
  # Profile specific operation and implementation
  python benchmark.py --profile --operation random_access --implementation grid
  
  # Profile with specific size
  python benchmark.py --profile --size 1000000
"""
        )
        
        parser.add_argument('--profile', action='store_true',
                          help='Run in profiling mode (minimal overhead for profilers)')
        parser.add_argument('--operation', type=str, 
                          help=f'Filter to specific operation. Options: {", ".join(self.operations)}')
        parser.add_argument('--size', type=int,
                          help=f'Filter to specific size. Options: {", ".join(map(str, self.sizes))}')
        parser.add_argument('--implementation', type=str,
                          help='Specific implementation (profile mode only)')
        
        args = parser.parse_args()
        
        return CLIConfig(
            profile_mode=args.profile,
            operation=args.operation,
            size=args.size,
            implementation=args.implementation
        )
    
    def validate_args(self, config: CLIConfig) -> None:
        """Validate command line arguments"""
        if config.operation and config.operation not in self.operations:
            print(f"Error: Unknown operation '{config.operation}'")
            print(f"Available operations: {', '.join(self.operations)}")
            sys.exit(1)
        
        if config.size and config.size not in self.sizes:
            print(f"Error: Unknown size '{config.size}'")
            print(f"Available sizes: {', '.join(map(str, self.sizes))}")
            sys.exit(1)