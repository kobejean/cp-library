"""
Benchmark registry implementation following Single Responsibility Principle.
"""

from typing import Callable, Dict, List, Union
from cp_library.perf.interfaces import BenchmarkRegistry, DataGenerator, ResultValidator


class DefaultResultValidator(ResultValidator):
    """Default validator that uses equality comparison"""
    
    def validate(self, expected, actual) -> bool:
        return expected == actual


class FunctionDataGenerator(DataGenerator):
    """Adapter to wrap function-based data generators"""
    
    def __init__(self, func: Callable):
        self.func = func
    
    def generate(self, size: int, operation: str):
        return self.func(size, operation)


class BenchmarkRegistryImpl(BenchmarkRegistry):
    """Implementation of benchmark component registry"""
    
    def __init__(self):
        self.implementations: Dict[str, Dict[str, Callable]] = {}
        self.data_generators: Dict[str, DataGenerator] = {}
        self.validators: Dict[str, ResultValidator] = {}
        self.setups: Dict[str, Dict[str, Callable]] = {}
        
        # Register default validator
        self.default_validator = DefaultResultValidator()
    
    def register_implementation(self, name: str, func: Callable, operations: List[str]) -> None:
        """Register a benchmark implementation"""
        for op in operations:
            if op not in self.implementations:
                self.implementations[op] = {}
            self.implementations[op][name] = func
    
    def register_data_generator(self, name: str, generator: DataGenerator) -> None:
        """Register a data generator"""
        self.data_generators[name] = generator
    
    def register_validator(self, operation: str, validator: ResultValidator) -> None:
        """Register a result validator"""
        self.validators[operation] = validator
    
    def register_setup(self, name: str, setup_func: Callable, operations: List[str]) -> None:
        """Register a setup function"""
        for op in operations:
            if op not in self.setups:
                self.setups[op] = {}
            self.setups[op][name] = setup_func
    
    def get_implementations(self, operation: str) -> Dict[str, Callable]:
        """Get implementations for an operation"""
        return self.implementations.get(operation, {})
    
    def get_data_generator(self, operation: str) -> DataGenerator:
        """Get data generator for an operation"""
        return self.data_generators.get(operation, self.data_generators.get('default'))
    
    def get_validator(self, operation: str) -> ResultValidator:
        """Get validator for an operation"""
        return self.validators.get(operation, self.default_validator)
    
    def get_setup(self, operation: str, implementation: str) -> Callable:
        """Get setup function for operation and implementation"""
        return self.setups.get(operation, {}).get(implementation)
    
    # Decorator methods for backward compatibility
    def data_generator(self, name: str = "default"):
        """Decorator to register data generator function"""
        def decorator(func):
            generator = FunctionDataGenerator(func)
            self.register_data_generator(name, generator)
            return func
        return decorator
    
    def implementation(self, name: str, operations: Union[str, List[str]] = None):
        """Decorator to register implementation function"""
        if operations is None:
            operations = ['default']
        elif isinstance(operations, str):
            operations = [operations]
            
        def decorator(func):
            self.register_implementation(name, func, operations)
            return func
        return decorator
    
    def validator(self, operation: str = "default"):
        """Decorator to register custom validator function"""
        def decorator(func):
            class FunctionValidator(ResultValidator):
                def validate(self, expected, actual) -> bool:
                    return func(expected, actual)
            
            self.register_validator(operation, FunctionValidator())
            return func
        return decorator
    
    def setup(self, name: str, operations: Union[str, List[str]] = None):
        """Decorator to register setup function"""
        if operations is None:
            operations = ['default']
        elif isinstance(operations, str):
            operations = [operations]
            
        def decorator(func):
            self.register_setup(name, func, operations)
            return func
        return decorator