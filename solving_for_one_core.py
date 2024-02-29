import numpy as np
import time

class LinearSystem:
    def __init__(self, system_size):
        np.random.seed(42)
        self.system_size = system_size
        self.coefficients = None
        self.constants = None

def solve_system_cramer(linear_system):
    det_coefficients = np.linalg.det(linear_system.coefficients)

    if abs(det_coefficients) < 1e-10:
        raise ValueError("Determinant is close to zero, system may be singular.")

    results = np.zeros(linear_system.system_size)
    for i in range(linear_system.system_size):
        temp_matrix = linear_system.coefficients.copy()
        temp_matrix[:, i] = linear_system.constants
        results[i] = np.linalg.det(temp_matrix) / det_coefficients

    return results

def main():
    system_size = 99
    num_systems = int(input("Введите количество систем: "))
    num_iterations = 10
    total_time_sum = 0

    for _ in range(num_iterations):
        start_time = time.time()

        # Создаем одну и ту же систему уравнений для решения
        shared_system = LinearSystem(system_size)
        shared_system.coefficients, shared_system.constants = np.random.rand(system_size, system_size), np.random.rand(system_size)

        results = []

        # Решение каждой системы последовательно методом Крамера
        for _ in range(num_systems):
            result = solve_system_cramer(shared_system)
            results.append(result)

        end_time = time.time()
        total_time = end_time - start_time
        total_time_sum += total_time

        print(f"Iteration {_ + 1}, Total time:", total_time)

    average_time = total_time_sum / num_iterations
    print(f"\nAverage time for {num_iterations} iterations:", average_time)

if __name__ == "__main__":
    main()

