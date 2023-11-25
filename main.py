import numpy as np
import time
import multiprocessing

def generate_test_values(equations):
    np.random.seed(42)
    coefficients = np.random.uniform(1, 100, size=(equations, equations))
    constants = np.random.uniform(1, 100, size=(equations, 1))

    # Дополнительные случайные коэффициенты и константы
    additional_coefficients = np.random.rand(equations, equations)
    additional_constants = np.random.rand(equations, 1)

    coefficients += additional_coefficients
    constants += additional_constants

    return coefficients, constants

def solve_system_partial(args):
    coefficients, constants, index = args
    matrix = coefficients.copy()
    matrix[:, index] = constants.flatten()
    logdet_i = np.linalg.slogdet(matrix)[1]
    return logdet_i

def solve_system(coefficients, constants, num_cores):
    logdet_A = np.linalg.slogdet(coefficients)[1]

    if np.isinf(logdet_A):
        raise ValueError("Determinant of the coefficient matrix is zero. The system may have no solution or infinite solutions.")

    pool = multiprocessing.Pool(processes=num_cores)
    results = pool.map_async(solve_system_partial, [(coefficients, constants, i) for i in range(coefficients.shape[1])])
    pool.close()
    pool.join()

    logdet_solutions = results.get()

    # Сложим логарифмы, чтобы избежать переполнения
    logdet_solutions_sum = np.sum(logdet_solutions)

    # Вернемся к обычному масштабу
    det_A = np.exp(logdet_A + logdet_solutions_sum)

    solutions = [np.exp(logdet_i) / det_A for logdet_i in logdet_solutions]

    return solutions

def main():
    equations = int(input("Введите количество уравнений: "))
    num_solves = int(input("Введите количество раз для решения системы: "))
    num_cores = int(input("Введите количество ядер для расчетов: "))

    total_time = 0.0
    for _ in range(num_solves):
        coefficients, constants = generate_test_values(equations)

        start_time = time.time()

        # Решение каждого уравнения происходит параллельно
        solutions = solve_system(coefficients, constants, num_cores)

        end_time = time.time()
        total_time += (end_time - start_time)

    average_time = total_time / num_solves
    print(f"Среднее время выполнения одного уравнения: {average_time} секунд")
    print(f"Общее время выполнения для {num_solves} уравнений: {total_time} секунд")

if __name__ == "__main__":
    main()
