import numpy as np
from multiprocessing import Pool
import time

def generate_system(size):
    coefficients = np.random.randint(-10, 10, size=(size, size))
    constants = np.random.randint(-10, 10, size=size)
    return coefficients, constants

def determinant(matrix):
    size = len(matrix)
    if size == 1:
        return matrix[0, 0]
    elif size == 2:
        return matrix[0, 0] * matrix[1, 1] - matrix[0, 1] * matrix[1, 0]
    else:
        det = 0
        for i in range(size):
            det += ((-1) ** i) * matrix[0, i] * determinant(np.delete(np.delete(matrix, 0, axis=0), i, axis=1))
        return det

def solve_system(args):
    coefficients, constants = args
    size = len(coefficients)
    det_main = determinant(coefficients)

    solution = []
    for i in range(size):
        temp_matrix = coefficients.copy()
        temp_matrix[:, i] = constants
        det_temp = determinant(temp_matrix)
        solution.append(det_temp / det_main)

    return solution

def main():
    size = 5  # Размерность системы
    num_systems = int(input("Введите количество систем для решения: "))
    num_cores = int(input("Введите количество ядер для выполнения вычислений: "))

    pool = Pool(num_cores)

    systems = [generate_system(size) for _ in range(num_systems)]

    start_time = time.time()

    results = pool.map(solve_system, systems)

    end_time = time.time()

    for i, result in enumerate(results):
        print(f"\nРешение для системы {i + 1}:\n{result}")

    print(f"\nВремя выполнения: {end_time - start_time:.6f} секунд")

if __name__ == "__main__":
    main()
