from solver import generate_system, solve_system
import time
from multiprocessing import Pool

def solve_system_multiple_times(num_iterations, size):
    systems = [generate_system(size, seed=42) for _ in range(num_iterations)]

    start_time = time.time()

    with Pool() as pool:
        results = list(pool.imap_unordered(solve_system, systems))

    total_time_elapsed = time.time() - start_time

    print(
        f"\nОбщее время, затраченное на {num_iterations} итераций для системы размером {size}x{size}: {total_time_elapsed} сек.")

if __name__ == "__main__":
    num_iterations = int(input("Введите количество раз решения системы: "))
    system_size = 50
    solve_system_multiple_times(num_iterations, system_size)
