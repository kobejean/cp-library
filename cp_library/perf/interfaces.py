"""
Interfaces for the benchmark framework following SOLID principles.
"""

from abc import ABC, abstractmethod
from typing import Any, Callable, Dict, List, Optional, Union
from dataclasses import dataclass


@dataclass
class BenchmarkResult:
    """Immutable benchmark result value object"""
    operation: str
    size: int
    implementation: str
    time_ms: float
    correct: bool
    error: Optional[str] = None


class TimerInterface(ABC):
    """Interface for timing implementations"""
    
    @abstractmethod
    def measure_time(self, func: Callable, data: Any, setup_func: Callable = None) -> tuple[Any, float]:
        """Measure execution time of a function"""
        pass


class PlotRenderer(ABC):
    """Interface for plot rendering implementations"""
    
    @abstractmethod
    def can_render(self) -> bool:
        """Check if this renderer is available"""
        pass
    
    @abstractmethod
    def create_plots(self, results: List[BenchmarkResult], config: Any) -> None:
        """Create plots from benchmark results"""
        pass


class ResultValidator(ABC):
    """Interface for result validation strategies"""
    
    @abstractmethod
    def validate(self, expected: Any, actual: Any) -> bool:
        """Validate benchmark result"""
        pass


class DataGenerator(ABC):
    """Interface for data generation strategies"""
    
    @abstractmethod
    def generate(self, size: int, operation: str) -> Any:
        """Generate test data for given size and operation"""
        pass


class OutputManager(ABC):
    """Interface for output management"""
    
    @abstractmethod
    def save_results(self, results: List[BenchmarkResult], config: Any) -> None:
        """Save benchmark results"""
        pass


class BenchmarkRegistry(ABC):
    """Interface for benchmark component registration"""
    
    @abstractmethod
    def register_implementation(self, name: str, func: Callable, operations: List[str]) -> None:
        """Register a benchmark implementation"""
        pass
    
    @abstractmethod
    def register_data_generator(self, name: str, generator: DataGenerator) -> None:
        """Register a data generator"""
        pass
    
    @abstractmethod
    def register_validator(self, operation: str, validator: ResultValidator) -> None:
        """Register a result validator"""
        pass
    
    @abstractmethod
    def register_setup(self, name: str, setup_func: Callable, operations: List[str]) -> None:
        """Register a setup function"""
        pass


class BenchmarkOrchestrator(ABC):
    """Interface for benchmark execution orchestration"""
    
    @abstractmethod
    def run_benchmarks(self, operations: List[str], sizes: List[int]) -> List[BenchmarkResult]:
        """Execute benchmarks and return results"""
        pass