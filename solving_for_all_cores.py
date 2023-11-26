import numpy as np
import time
from multiprocessing import Pool, cpu_count


def generate_system(size):
    np.random.seed(42)
    coefficients = np.random.randint(-10, 10, size=(size, size))
    constants = np.random.randint(-10, 10, size=size)
    return coefficients, constants


def write_system_to_file(filename, coefficients, constants):
    with open(filename, 'w') as file:
        for i in range(len(coefficients)):
            equation = ' + '.join([f'{coeff} * x{i + 1}' for i, coeff in enumerate(coefficients[i])])
            equation += f' = {constants[i]}'
            file.write(equation + '\n')


def solve_system_parallel(args):
    i, coefficients, constants = args
    temp_matrix = coefficients.copy()
    temp_matrix[:, i] = constants
    det_temp = np.linalg.det(temp_matrix)
    return det_temp


def solve_system(coefficients, constants, pool):
    size = len(coefficients)
    det_main = np.linalg.det(coefficients)

    results = pool.map(solve_system_parallel, [(i, coefficients, constants) for i in range(size)])

    solution = [det_temp / det_main for det_temp in results]
    return solution


def main():
    size = 100
    num_runs = int(input("Введите количество запусков для одной и той же системы: "))

    # Генерация одной и той же системы уравнений
    system = generate_system(size)

    # Запись системы уравнений в файл
    write_system_to_file("system_equations.txt", system[0], system[1])

    # Создание пула процессов
    pool = Pool(processes=cpu_count())

    start_time = time.time()
    for i in range(num_runs):
        result = solve_system(system[0], system[1], pool)
    end_time = time.time()

    # Закрытие пула процессов
    pool.close()
    pool.join()

    print(f"\nВремя выполнения: {end_time - start_time:.6f} секунд")

    # Вывод результатов после замера времени


if __name__ == "__main__":
    main()
