import time
import numpy as np
import multiprocessing
from functools import partial

def generate_fixed_system(size):
    np.random.seed(42)  # Фиксируем seed для воспроизводимости
    A = np.random.rand(size, size)
    B = np.random.rand(size)
    return A, B

def solve_system_cramer(A, B, num_cores=1):
    start_time = time.time()

    det_A = np.linalg.det(A)
    if abs(det_A) < 1e-10:
        raise ValueError("Determinant is close to zero, system may not have a unique solution")

    def solve_cramer_single_column(i, A, B):
        Ai = A.copy()
        Ai[:, i] = B
        det_Ai = np.linalg.det(Ai)
        if abs(det_Ai) < 1e-10:
            return np.nan
        return det_Ai / det_A

    pool = multiprocessing.Pool(processes=num_cores)
    partial_solve = partial(solve_cramer_single_column, A=A, B=B)
    solutions = pool.map(partial_solve, range(len(B)))
    pool.close()
    pool.join()

    end_time = time.time()
    execution_time = end_time - start_time

    return solutions, execution_time

def main():
    sizes = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    num_cores = int(input("Введите количество ядер CPU для использования: "))

    for size in sizes:
        A, B = generate_fixed_system(size)
        try:
            solutions, execution_time = solve_system_cramer(A, B, num_cores)
            print(f"System size: {size}, Execution time: {execution_time} seconds, Solutions: {solutions}")
        except ValueError as e:
            print(f"System size: {size}, Error: {e}")

if __name__ == "__main__":
    main()
