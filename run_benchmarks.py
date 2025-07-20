#!/usr/bin/env python3
"""
Performance benchmark runner for cp-library.

This script makes it easy to run all performance benchmarks or specific subsets.
"""

import os
import sys
import argparse
import subprocess
import time
from pathlib import Path
from typing import List, Optional


class BenchmarkRunner:
    """Runner for performance benchmarks"""
    
    def __init__(self):
        self.script_dir = Path(__file__).parent
        self.perf_dir = self.script_dir / "perf"
        self.benchmark_files = self._discover_benchmarks()
    
    def _discover_benchmarks(self) -> List[Path]:
        """Discover all benchmark files in the perf directory"""
        benchmark_files = []
        for file_path in self.perf_dir.glob("*.py"):
            # Skip module files and framework files
            if file_path.name.startswith("__") or file_path.name in {
                "benchmark.py", "interfaces.py", "registry.py", "orchestrator.py", 
                "timing.py", "output.py", "renderers.py", "cli.py", "checksum.py", "plotting.py"
            }:
                continue
            benchmark_files.append(file_path)
        
        return sorted(benchmark_files)
    
    def list_benchmarks(self):
        """List all available benchmarks"""
        print("Available benchmarks:")
        print("=" * 50)
        for i, benchmark in enumerate(self.benchmark_files, 1):
            print(f"{i:2d}. {benchmark.stem}")
    
    def run_benchmark(self, benchmark_file: Path, operation: Optional[str] = None, 
                     size: Optional[int] = None, quiet: bool = False) -> bool:
        """Run a single benchmark file"""
        cmd = ['pypy', str(benchmark_file)]
        
        if operation:
            cmd.extend(["--operation", operation])
        if size:
            cmd.extend(["--size", str(size)])
        
        if not quiet:
            print(f"\n{'='*60}")
            print(f"Running: {benchmark_file.stem}")
            if operation:
                print(f"Operation: {operation}")
            if size:
                print(f"Size: {size}")
            print('='*60)
        
        try:
            result = subprocess.run(
                cmd, 
                cwd=self.script_dir,
                capture_output=quiet,
                text=True,
                timeout=300  # 5 minute timeout per benchmark
            )
            
            if result.returncode == 0:
                if not quiet:
                    print(f"✅ {benchmark_file.stem} completed successfully")
                return True
            else:
                print(f"❌ {benchmark_file.stem} failed with return code {result.returncode}")
                if quiet and result.stderr:
                    print(f"Error: {result.stderr}")
                return False
                
        except subprocess.TimeoutExpired:
            print(f"⏰ {benchmark_file.stem} timed out after 5 minutes")
            return False
        except Exception as e:
            print(f"💥 {benchmark_file.stem} crashed: {e}")
            return False
    
    def run_all(self, operation: Optional[str] = None, size: Optional[int] = None, 
                quiet: bool = False, fast: bool = False):
        """Run all benchmarks"""
        if fast:
            # Fast mode: smaller sizes and fewer iterations
            if not size:
                size = 1000
        
        print(f"Running {len(self.benchmark_files)} benchmarks...")
        if operation:
            print(f"Filtering to operation: {operation}")
        if size:
            print(f"Filtering to size: {size}")
        if fast:
            print("Fast mode: using smaller test sizes")
        
        start_time = time.time()
        successful = 0
        failed = 0
        
        for benchmark in self.benchmark_files:
            success = self.run_benchmark(benchmark, operation, size, quiet)
            if success:
                successful += 1
            else:
                failed += 1
        
        total_time = time.time() - start_time
        
        print(f"\n{'='*60}")
        print(f"BENCHMARK SUMMARY")
        print('='*60)
        print(f"Total benchmarks: {len(self.benchmark_files)}")
        print(f"Successful: {successful}")
        print(f"Failed: {failed}")
        print(f"Total time: {total_time:.1f} seconds")
        
        if failed > 0:
            print(f"\n❌ {failed} benchmarks failed")
            sys.exit(1)
        else:
            print(f"\n✅ All benchmarks completed successfully!")
    
    def run_specific(self, names: List[str], operation: Optional[str] = None, 
                    size: Optional[int] = None, quiet: bool = False):
        """Run specific benchmarks by name"""
        benchmarks_to_run = []
        
        for name in names:
            # Try exact match first
            matching = [b for b in self.benchmark_files if b.stem == name]
            if not matching:
                # Try partial match
                matching = [b for b in self.benchmark_files if name.lower() in b.stem.lower()]
            
            if matching:
                benchmarks_to_run.extend(matching)
            else:
                print(f"❌ No benchmark found matching '{name}'")
                return False
        
        # Remove duplicates while preserving order
        benchmarks_to_run = list(dict.fromkeys(benchmarks_to_run))
        
        print(f"Running {len(benchmarks_to_run)} benchmark(s)...")
        
        successful = 0
        failed = 0
        
        for benchmark in benchmarks_to_run:
            success = self.run_benchmark(benchmark, operation, size, quiet)
            if success:
                successful += 1
            else:
                failed += 1
        
        print(f"\n{'='*40}")
        print(f"Results: {successful} successful, {failed} failed")
        
        return failed == 0


def main():
    parser = argparse.ArgumentParser(
        description="Run performance benchmarks for cp-library",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # List all available benchmarks
  python run_benchmarks.py --list
  
  # Run all benchmarks
  python run_benchmarks.py --all
  
  # Run all benchmarks quickly with smaller sizes
  python run_benchmarks.py --all --fast
  
  # Run specific benchmarks
  python run_benchmarks.py que deque segtree2
  
  # Run benchmarks with specific operation
  python run_benchmarks.py --all --operation construction
  
  # Run benchmarks with specific size
  python run_benchmarks.py --all --size 1000
  
  # Run quietly (less output)
  python run_benchmarks.py --all --quiet
"""
    )
    
    parser.add_argument("benchmarks", nargs="*", 
                       help="Specific benchmark names to run (e.g., 'que', 'segtree2')")
    parser.add_argument("--list", action="store_true",
                       help="List all available benchmarks")
    parser.add_argument("--all", action="store_true",
                       help="Run all benchmarks")
    parser.add_argument("--operation", type=str,
                       help="Filter to specific operation")
    parser.add_argument("--size", type=int,
                       help="Filter to specific size")
    parser.add_argument("--quiet", action="store_true",
                       help="Reduce output (show only summaries)")
    parser.add_argument("--fast", action="store_true",
                       help="Fast mode: use smaller test sizes")
    
    args = parser.parse_args()
    
    runner = BenchmarkRunner()
    
    if args.list:
        runner.list_benchmarks()
    elif args.all:
        runner.run_all(args.operation, args.size, args.quiet, args.fast)
    elif args.benchmarks:
        success = runner.run_specific(args.benchmarks, args.operation, args.size, args.quiet)
        if not success:
            sys.exit(1)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()