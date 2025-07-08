import cp_library.__header__
import cp_library.perf.__header__
import random
from abc import ABC, abstractmethod
from typing import Any, List, Dict
import math

class DataGenerator(ABC):
    """Base class for test data generators"""
    
    @abstractmethod
    def generate(self, **params) -> Any:
        """Generate test data based on parameters"""
        pass

class RandomArrayGenerator(DataGenerator):
    """Generate random integer arrays"""
    
    def __init__(self, min_val: int = 1, max_val: int = None):
        self.min_val = min_val
        self.max_val = max_val
    
    def generate(self, size: int, **params) -> List[int]:
        max_val = self.max_val if self.max_val is not None else size
        return [random.randint(self.min_val, max_val) for _ in range(size)]

class SortedArrayGenerator(DataGenerator):
    """Generate sorted arrays"""
    
    def __init__(self, reverse: bool = False, step: int = 1):
        self.reverse = reverse
        self.step = step
    
    def generate(self, size: int, **params) -> List[int]:
        arr = list(range(0, size * self.step, self.step))
        if self.reverse:
            arr.reverse()
        return arr

class DuplicatesArrayGenerator(DataGenerator):
    """Generate arrays with many duplicate values"""
    
    def __init__(self, num_unique: int = 10):
        self.num_unique = num_unique
    
    def generate(self, size: int, **params) -> List[int]:
        return [random.randint(1, self.num_unique) for _ in range(size)]

class DistributionArrayGenerator(DataGenerator):
    """Generate arrays following specific distributions"""
    
    def __init__(self, distribution: str = 'uniform'):
        self.distribution = distribution
    
    def generate(self, size: int, **params) -> List[int]:
        if self.distribution == 'normal':
            mean = params.get('mean', size // 2)
            std = params.get('std', size // 10)
            return [int(random.gauss(mean, std)) for _ in range(size)]
        
        elif self.distribution == 'exponential':
            rate = params.get('rate', 1.0 / (size // 10))
            return [int(random.expovariate(rate)) for _ in range(size)]
        
        elif self.distribution == 'power':
            alpha = params.get('alpha', 2.0)
            return [int(random.paretovariate(alpha) * size // 10) for _ in range(size)]
        
        elif self.distribution == 'bimodal':
            # Mix of two normal distributions
            mean1 = size // 3
            mean2 = 2 * size // 3
            std = size // 20
            return [
                int(random.gauss(mean1 if i % 2 == 0 else mean2, std))
                for i in range(size)
            ]
        
        else:  # uniform
            return RandomArrayGenerator().generate(size)

class PermutationGenerator(DataGenerator):
    """Generate permutations"""
    
    def generate(self, size: int, **params) -> List[int]:
        arr = list(range(size))
        random.shuffle(arr)
        return arr

class PlateauArrayGenerator(DataGenerator):
    """Generate arrays with plateaus (consecutive equal values)"""
    
    def __init__(self, num_plateaus: int = 5):
        self.num_plateaus = num_plateaus
    
    def generate(self, size: int, **params) -> List[int]:
        plateau_size = size // self.num_plateaus
        arr = []
        for i in range(self.num_plateaus):
            value = i * 100
            arr.extend([value] * plateau_size)
        
        # Fill remaining with last value
        while len(arr) < size:
            arr.append((self.num_plateaus - 1) * 100)
        
        return arr[:size]

class SawtoothArrayGenerator(DataGenerator):
    """Generate sawtooth pattern arrays"""
    
    def __init__(self, period: int = 10):
        self.period = period
    
    def generate(self, size: int, **params) -> List[int]:
        return [i % self.period for i in range(size)]

class AlmostSortedArrayGenerator(DataGenerator):
    """Generate almost sorted arrays with some inversions"""
    
    def __init__(self, inversion_rate: float = 0.05):
        self.inversion_rate = inversion_rate
    
    def generate(self, size: int, **params) -> List[int]:
        arr = list(range(size))
        num_swaps = int(size * self.inversion_rate)
        
        for _ in range(num_swaps):
            i = random.randint(0, size - 1)
            j = random.randint(0, size - 1)
            arr[i], arr[j] = arr[j], arr[i]
        
        return arr

# Factory function for easy generator creation
def create_generator(generator_type: str, **kwargs) -> DataGenerator:
    """Create a data generator by type name"""
    generators = {
        'random': RandomArrayGenerator,
        'sorted': SortedArrayGenerator,
        'reverse': lambda: SortedArrayGenerator(reverse=True),
        'duplicates': DuplicatesArrayGenerator,
        'distribution': DistributionArrayGenerator,
        'permutation': PermutationGenerator,
        'plateau': PlateauArrayGenerator,
        'sawtooth': SawtoothArrayGenerator,
        'almost_sorted': AlmostSortedArrayGenerator,
    }
    
    if generator_type in generators:
        gen_class = generators[generator_type]
        if callable(gen_class) and not isinstance(gen_class, type):
            return gen_class()
        return gen_class(**kwargs)
    else:
        raise ValueError(f"Unknown generator type: {generator_type}")