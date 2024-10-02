import time
import random
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Import your sieve classes
from cp_library.math.table.sieve_cls import Sieve
from cp_library.math.table.linear_sieve_cls import LinearSieve
from cp_library.math.table.linear_sieve_cnts_cls import LinearSieveCounts

def benchmark_construction(Ns):
    sieve_classes = [
        ('LinearSieveCounts', LinearSieveCounts),
        ('LinearSieve', LinearSieve),
        ('Sieve', Sieve)
    ]
    construction_results = []

    for N in Ns:
        sieves = {}
        for name, cls in sieve_classes:
            print(f"Constructing {name} with N = {N}")
            start_time = time.perf_counter()
            sieve = cls(N)
            total_time = time.perf_counter() - start_time
            sieves[name] = sieve
            construction_results.append({'Sieve': name, 'ConstructionTime': total_time, 'N': N})
        yield N, sieves, construction_results[-len(sieve_classes):]  # Return only the latest results

def warm_up_methods(sieves, test_numbers, warm_up_runs=3):
    print("\nWarming up methods...")
    for _ in range(warm_up_runs):
        for sieve_name, sieve in sieves.items():
            for method_name in ['factor_cnts', 'factors']:
                method = getattr(sieve, method_name)
                for num in test_numbers[:100]:  # Use a subset for warm-up
                    method(num)
    print("Warm-up completed.\n")

def benchmark_methods(sieves, test_numbers, N, warm_up_runs=3):
    timings = []
    num_numbers = len(test_numbers)

    # Warm-up phase
    warm_up_methods(sieves, test_numbers, warm_up_runs)

    for sieve_name, sieve in sieves.items():
        for method_name in ['factor_cnts', 'factors']:
            method = getattr(sieve, method_name)
            print(f"Benchmarking {sieve_name}.{method_name} with N = {N}")
            start_time = time.perf_counter()
            for num in test_numbers:
                method(num)
            total_time = time.perf_counter() - start_time
            avg_time = total_time / num_numbers
            timings.append({
                'Sieve': sieve_name,
                'Method': method_name,
                'AvgTimePerNumber': avg_time,
                'N': N
            })

    return timings

def verify_correctness(sieves, test_numbers):
    correct = True
    for num in test_numbers:
        factors_results = []
        factor_cnts_results = []
        for sieve_name, sieve in sieves.items():
            factors_results.append((sieve_name, sieve.factors(num)))
            factor_cnts_results.append((sieve_name, sorted(sieve.factor_cnts(num))))
        # Check if all factors results are the same
        factors_set = set(tuple(res[1]) for res in factors_results)
        if len(factors_set) > 1:
            print(f"Mismatch in factors for number {num}")
            for name, res in factors_results:
                print(f"{name}: {res}")
            correct = False
            break
        # Check if all factor_cnts results are the same
        factor_cnts_set = set(tuple(res[1]) for res in factor_cnts_results)
        if len(factor_cnts_set) > 1:
            print(f"Mismatch in factor_cnts for number {num}")
            for name, res in factor_cnts_results:
                print(f"{name}: {res}")
            correct = False
            break
    if correct:
        print("All methods produce correct results.")
    return correct

def benchmark_specific_cases(sieves, N, repetitions=50, warm_up_runs=3):
    # Benchmarking factorials and powers of 2
    factorial_numbers = []
    max_i = 20  # Adjust as needed for more factorials
    for i in range(1, max_i + 1):
        fact = math.factorial(i)
        if fact >= N:
            break
        factorial_numbers.append(fact)
    
    # Extend the list by repeating numbers to increase sample size
    factorial_numbers *= repetitions  # Repeat the list 'repetitions' times
    random.shuffle(factorial_numbers)  # Shuffle to randomize the order

    powers_of_two = [1 << k for k in range(1, int(math.log2(N)) + 1)]
    powers_of_two *= repetitions  # Repeat the list 'repetitions' times
    random.shuffle(powers_of_two)  # Shuffle to randomize the order

    specific_cases_results = []

    # Warm-up phase
    warm_up_methods(sieves, factorial_numbers + powers_of_two, warm_up_runs)

    for case_name, numbers in [('Factorials', factorial_numbers), ('PowersOfTwo', powers_of_two)]:
        num_numbers = len(numbers)
        for sieve_name, sieve in sieves.items():
            if num_numbers == 0:
                continue  # Skip if no numbers to test
            print(f"Benchmarking {sieve_name} on {case_name} with N = {N}")
            method = sieve.factor_cnts
            start_time = time.perf_counter()
            for num in numbers:
                method(num)
            total_time = time.perf_counter() - start_time
            avg_time = total_time / num_numbers
            specific_cases_results.append({
                'Case': case_name,
                'Sieve': sieve_name,
                'AvgTimePerNumber': avg_time,
                'NumNumbers': num_numbers,
                'N': N
            })
    return specific_cases_results

def plot_results(construction_df, methods_df, specific_cases_df):
    # Plot construction times
    plt.figure(figsize=(10, 6))
    for sieve in construction_df['Sieve'].unique():
        sieve_data = construction_df[construction_df['Sieve'] == sieve]
        sieve_data = sieve_data.sort_values('N')  # Ensure data is sorted by N
        plt.plot(sieve_data['N'], sieve_data['ConstructionTime'], marker='o', label=sieve)
    plt.xlabel('N')
    plt.ylabel('Construction Time (s)')
    plt.title('Sieve Construction Time')
    plt.legend()
    plt.xscale('log')
    plt.yscale('log')
    plt.grid(True)
    plt.show()

    # Plot method average times per number
    for method in methods_df['Method'].unique():
        plt.figure(figsize=(10, 6))
        for sieve in methods_df['Sieve'].unique():
            sieve_data = methods_df[(methods_df['Sieve'] == sieve) & (methods_df['Method'] == method)]
            sieve_data = sieve_data.sort_values('N')  # Ensure data is sorted by N
            plt.plot(sieve_data['N'], sieve_data['AvgTimePerNumber'], marker='o', label=sieve)
        plt.xlabel('N')
        plt.ylabel('Average Time per Number (s)')
        plt.title(f'Method {method} Average Time per Number')
        plt.legend()
        plt.xscale('log')
        plt.yscale('log')
        plt.grid(True)
        plt.show()

    # Compute and plot percentage speedup for methods
    baseline_sieve = 'Sieve'  # Set the baseline sieve
    for method in methods_df['Method'].unique():
        plt.figure(figsize=(10, 6))
        # Get the baseline timings
        baseline_data = methods_df[(methods_df['Sieve'] == baseline_sieve) & (methods_df['Method'] == method)]
        baseline_data = baseline_data[['N', 'AvgTimePerNumber']].set_index('N')
        for sieve in methods_df['Sieve'].unique():
            if sieve == baseline_sieve:
                continue
            sieve_data = methods_df[(methods_df['Sieve'] == sieve) & (methods_df['Method'] == method)]
            sieve_data = sieve_data[['N', 'AvgTimePerNumber']].set_index('N')
            # Align data on N
            combined = baseline_data.join(sieve_data, lsuffix='_baseline', rsuffix='_other', how='inner')
            # Compute percentage speedup
            combined['PercentSpeedup'] = ((combined['AvgTimePerNumber_baseline'] - combined['AvgTimePerNumber_other']) / combined['AvgTimePerNumber_baseline']) * 100
            combined = combined.reset_index()
            combined = combined.sort_values('N')
            plt.plot(combined['N'], combined['PercentSpeedup'], marker='o', label=sieve)
        plt.xlabel('N')
        plt.ylabel('Percentage Speedup (%)')
        plt.title(f'Method {method} Percentage Speedup over {baseline_sieve}')
        plt.legend()
        plt.xscale('log')
        plt.grid(True)
        plt.show()

    # Compute and plot percentage speedup for specific cases
    for case in specific_cases_df['Case'].unique():
        plt.figure(figsize=(10, 6))
        # Get the baseline timings
        baseline_data = specific_cases_df[(specific_cases_df['Sieve'] == baseline_sieve) & (specific_cases_df['Case'] == case)]
        baseline_data = baseline_data[['N', 'AvgTimePerNumber']].set_index('N')
        for sieve in specific_cases_df['Sieve'].unique():
            if sieve == baseline_sieve:
                continue
            sieve_data = specific_cases_df[(specific_cases_df['Sieve'] == sieve) & (specific_cases_df['Case'] == case)]
            sieve_data = sieve_data[['N', 'AvgTimePerNumber']].set_index('N')
            # Align data on N
            combined = baseline_data.join(sieve_data, lsuffix='_baseline', rsuffix='_other', how='inner')
            # Compute percentage speedup
            combined['PercentSpeedup'] = ((combined['AvgTimePerNumber_baseline'] - combined['AvgTimePerNumber_other']) / combined['AvgTimePerNumber_baseline']) * 100
            combined = combined.reset_index()
            combined = combined.sort_values('N')
            plt.plot(combined['N'], combined['PercentSpeedup'], marker='o', label=sieve)
        plt.xlabel('N')
        plt.ylabel('Percentage Speedup (%)')
        plt.title(f'{case} Percentage Speedup over {baseline_sieve}')
        plt.legend()
        plt.xscale('log')
        plt.grid(True)
        plt.show()

    # Compute and plot percentage speedup for construction times
    plt.figure(figsize=(10, 6))
    # Get the baseline timings
    baseline_data = construction_df[construction_df['Sieve'] == baseline_sieve]
    baseline_data = baseline_data[['N', 'ConstructionTime']].set_index('N')
    for sieve in construction_df['Sieve'].unique():
        if sieve == baseline_sieve:
            continue
        sieve_data = construction_df[construction_df['Sieve'] == sieve]
        sieve_data = sieve_data[['N', 'ConstructionTime']].set_index('N')
        # Align data on N
        combined = baseline_data.join(sieve_data, lsuffix='_baseline', rsuffix='_other', how='inner')
        # Compute percentage speedup
        combined['PercentSpeedup'] = ((combined['ConstructionTime_baseline'] - combined['ConstructionTime_other']) / combined['ConstructionTime_baseline']) * 100
        combined = combined.reset_index()
        combined = combined.sort_values('N')
        plt.plot(combined['N'], combined['PercentSpeedup'], marker='o', label=sieve)
    plt.xlabel('N')
    plt.ylabel('Percentage Speedup (%)')
    plt.title(f'Construction Time Percentage Speedup over {baseline_sieve}')
    plt.legend()
    plt.xscale('log')
    plt.grid(True)
    plt.show()

def main():
    # Create a finer list of N values, ranging from 1e5 to 1e8 with more steps
    Ns = [int(N) for N in np.logspace(5, 8, num=30)]  # 30 steps from 1e5 to 1e8
    num_tests = 20000  # Increased number of random numbers to test methods on

    construction_results = []
    method_results = []
    specific_cases_results = []

    for N_data in benchmark_construction(Ns):
        N, sieves, construction_timings = N_data
        construction_results.extend(construction_timings)

        # Generate random test numbers
        test_numbers = [random.randint(2, N - 1) for _ in range(num_tests)]

        method_timings = benchmark_methods(sieves, test_numbers, N, warm_up_runs=3)
        method_results.extend(method_timings)

        print(f"\nVerifying correctness of methods for N = {N}...")
        verify_correctness(sieves, test_numbers[:100])  # Check correctness for first 100 numbers

        specific_case_timings = benchmark_specific_cases(sieves, N, repetitions=50, warm_up_runs=3)
        specific_cases_results.extend(specific_case_timings)

    # Convert results to DataFrames
    construction_df = pd.DataFrame(construction_results)
    methods_df = pd.DataFrame(method_results)
    specific_cases_df = pd.DataFrame(specific_cases_results)

    # Plotting
    plot_results(construction_df, methods_df, specific_cases_df)

if __name__ == "__main__":
    main()