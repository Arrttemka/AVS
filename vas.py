import numpy as np
import time


def generate_system(size, seed=42):
    np.random.seed(seed)

    coeff_matrix = np.random.randint(-10, 10, size=(size, size))
    rhs_vector = np.random.randint(-10, 10, size=size)

    return coeff_matrix, rhs_vector


def solve_system(matrix, vector):
    det_A = np.linalg.det(matrix)

    if det_A == 0:
        return None  # система не имеет единственного решения

    n = len(vector)
    solutions = []

    start_time = time.time()

    for i in range(n):
        temp_matrix = matrix.copy()
        temp_matrix[:, i] = vector
        det_i = np.linalg.det(temp_matrix)
        x_i = det_i / det_A
        solutions.append(x_i)

    end_time = time.time()

    return solutions, end_time - start_time


def solve_system_multiple_times(num_iterations, size):
    total_time_elapsed = 0

    for iteration in range(1, num_iterations + 1):
        # Генерируем систему с фиксированным зерном
        coeff_matrix, rhs_vector = generate_system(size, seed=42)

        # Решаем систему уравнений и измеряем время
        _, time_elapsed = solve_system(coeff_matrix, rhs_vector)

        total_time_elapsed += time_elapsed

    print(
        f"\nОбщее время, затраченное на {num_iterations} итераций для системы размером {size}x{size}: {total_time_elapsed} сек.")


# Получаем количество раз и размер системы, которое пользователь хочет использовать
num_iterations = int(input("Введите количество раз решения системы: "))
system_size = 10
solve_system_multiple_times(num_iterations, system_size)
