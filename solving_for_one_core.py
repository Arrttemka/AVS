import numpy as np
import time

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

def solve_system(coefficients, constants):
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
    size = 100
    num_runs = int(input("Введите количество запусков для одной и той же системы: "))

    # Генерация одной и той же системы уравнений
    system = generate_system(size)

    # Запись системы уравнений в файл
    write_system_to_file("system_equations.txt", system[0], system[1])

    start_time = time.time()
    for i in range(num_runs):
        result = solve_system(system[0], system[1])
    end_time = time.time()

    print(f"\nВремя выполнения: {end_time - start_time:.6f} секунд")

    # Вывод результатов после замера времени


if __name__ == "__main__":
    main()
