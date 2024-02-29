import numpy as np
import time
from multiprocessing import Pool, cpu_count


class LinearSystem:
    def __init__(self, system_size):
        np.random.seed(42)
        self.system_size = system_size
        self.coefficients = None
        self.constants = None


def generate_complex_system(system_size):
    # Создаем более сложную матрицу коэффициентов
    coefficients = np.random.randint(1, 10, size=(system_size, system_size)) * np.random.choice([-1, 1], size=(
        system_size, system_size))

    # Создаем более широкий разброс значений констант
    constants = np.random.uniform(-10, 10, size=system_size)

    return coefficients, constants


def solve_system_cramer(args):
    linear_system, thread_index = args
    det_coefficients = np.linalg.det(linear_system.coefficients)

    if abs(det_coefficients) < 1e-10:
        raise ValueError("Determinant is close to zero, system may be singular.")

    results = np.zeros(linear_system.system_size)
    for i in range(linear_system.system_size):
        temp_matrix = linear_system.coefficients.copy()
        temp_matrix[:, i] = linear_system.constants
        results[i] = np.linalg.det(temp_matrix) / det_coefficients

    return thread_index, results


def main():
    system_size = 99
    num_systems = int(input("Enter the number of systems: "))
    num_iterations = 10  # Укажем количество итераций
    total_time_sum = 0

    for iteration in range(1, num_iterations + 1):

        start_time = time.time()
        # Use multiprocessing to parallelize the solution using all available CPU cores
        pool = Pool(cpu_count())

        # Create a list of LinearSystem instances with more complex coefficients and constants
        systems = [LinearSystem(system_size) for _ in range(num_systems)]
        for sys in systems:
            sys.coefficients, sys.constants = generate_complex_system(system_size)

        # Use Pool.map to solve the systems in parallel
        results_with_index = pool.map(solve_system_cramer, [(sys, idx) for idx, sys in enumerate(systems)])

        # Separate results and thread indices
        thread_indices, results = zip(*results_with_index)

        pool.close()
        pool.join()

        end_time = time.time()
        total_time = end_time - start_time
        total_time_sum += total_time

        print(total_time)

    average_time = total_time_sum / num_iterations
    print(f"\nAverage time for {num_iterations} iterations:", average_time)


if __name__ == "__main__":
    main()
