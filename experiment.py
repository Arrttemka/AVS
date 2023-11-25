import numpy as np
from multiprocessing import Pool
import time


def generate_system(size):
    np.random.seed(42)  # Зафиксируем seed для воспроизводимости
    coefficients = np.random.randint(-10, 10, size=(size, size))
    constants = np.random.randint(-10, 10, size=size)
    return coefficients, constants


def write_system_to_file(filename, coefficients, constants):
    with open(filename, 'w') as file:
        for i in range(len(coefficients)):
            equation = ' + '.join([f'{coeff} * x{i + 1}' for i, coeff in enumerate(coefficients[i])])
            equation += f' = {constants[i]}'
            file.write(equation + '\n')


def solve_system(args):
    coefficients, constants = args
    size = len(coefficients)

    det_main = np.linalg.det(coefficients)

    solution = []
    for i in range(size):
        temp_matrix = coefficients.copy()
        temp_matrix[:, i] = constants
        det_temp = np.linalg.det(temp_matrix)
        solution.append(det_temp / det_main)

    return solution


def main():
    size = 100  # Размерность системы
    num_runs = int(input("Введите количество запусков для одной и той же системы: "))
    num_cores = int(input("Введите количество ядер для выполнения вычислений: "))

    pool = Pool(num_cores)

    # Генерация одной и той же системы уравнений
    system = generate_system(size)

    # Запись системы уравнений в файл
    write_system_to_file("system_equations.txt", system[0], system[1])

    systems = [system for _ in range(num_runs)]

    start_time = time.time()

    results = pool.map(solve_system, systems)

    end_time = time.time()

    for i, result in enumerate(results):
        print(f"\nРешение для запуска {i + 1}:\n{result}")

    print(f"\nВремя выполнения: {end_time - start_time:.6f} секунд")


if __name__ == "__main__":
    main()
