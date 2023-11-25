import numpy as np
import time
import multiprocessing


def generate_test_values(equations):
    np.random.seed(42)
    coefficients = np.random.randint(1, 10, size=(equations, equations))
    constants = np.random.randint(1, 10, size=(equations, 1))
    return coefficients, constants


def solve_system_partial(args):
    coefficients, constants, index = args
    matrix = coefficients.copy()
    matrix[:, index] = constants.flatten()
    det_i = np.linalg.det(matrix)
    return det_i


def solve_system(coefficients, constants, num_cores):
    det_A = np.linalg.det(coefficients)

    if det_A == 0:
        raise ValueError(
            "Determinant of the coefficient matrix is zero. The system may have no solution or infinite solutions.")

    pool = multiprocessing.Pool(processes=num_cores)
    results = pool.map(solve_system_partial, [(coefficients, constants, i) for i in range(coefficients.shape[1])])
    pool.close()
    pool.join()

    solutions = [result / det_A for result in results]

    return solutions


def main():
    equations = int(input("Введите количество уравнений: "))
    num_cores = int(input("Введите количество ядер для расчетов: "))

    coefficients, constants = generate_test_values(equations)

    start_time = time.time()
    solutions = solve_system(coefficients, constants, num_cores)
    end_time = time.time()

    print(f"Решения системы: {solutions}")
    print(f"Время выполнения: {end_time - start_time} секунд")


if __name__ == "__main__":
    main()
