import sympy as sp
import numpy as np
import multiprocessing
import time

for zu in range(10):
    # Define the symbol and period
    t = sp.symbols('t')
    T = 2 * sp.pi  # Assuming a period of 2*pi, adjust as needed

    # Define the function to be decomposed
    # Example: f(t) = t for 0 <= t < pi and -t for pi <= t < 2*pi
    f = sp.Piecewise((t, (t >= 0) & (t < sp.pi)), (-t, (t >= sp.pi) & (t < 2 * sp.pi)))


    # Find the Fourier series coefficients
    def calculate_coefficients(n):
        a0 = (1 / T) * sp.integrate(f, (t, 0, T))
        an = (1 / (T / 2)) * sp.integrate(f * sp.cos(n * 2 * sp.pi * t / T), (t, 0, T))
        bn = (1 / (T / 2)) * sp.integrate(f * sp.sin(n * 2 * sp.pi * t / T), (t, 0, T))
        return a0, an, bn


    # Define the number of terms in the series
    N = 500  # Number of terms in the series

    # Create a pool of worker processes
    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())

    # Start measuring time
    start_time = time.time()

    # Calculate Fourier series coefficients in parallel
    results = pool.map(calculate_coefficients, range(1, N + 1))

    # Close the pool and wait for all processes to finish
    pool.close()
    pool.join()

    # Calculate the Fourier series
    a0, an, bn = zip(*results)
    fourier_series = a0[0] / 2
    for i in range(1, N):
        fourier_series += (an[i - 1] * sp.cos(i * 2 * sp.pi * t / T) +
                           bn[i - 1] * sp.sin(i * 2 * sp.pi * t / T))

    # Stop measuring time
    end_time = time.time()

    # Calculate and display the elapsed time
    elapsed_time = end_time - start_time

    # Append the elapsed time to a file
    with open('mt500.txt', 'a') as file:
        file.write(f"Elapsed Time: {elapsed_time:.6f} seconds\n")

for zu in range(10):
    # Define the symbol and period
    t = sp.symbols('t')
    T = 2 * sp.pi  # Assuming a period of 2*pi, adjust as needed

    # Define the function to be decomposed
    # Example: f(t) = t for 0 <= t < pi and -t for pi <= t < 2*pi
    f = sp.Piecewise((t, (t >= 0) & (t < sp.pi)), (-t, (t >= sp.pi) & (t < 2 * sp.pi)))


    # Find the Fourier series coefficients
    def calculate_coefficients(n):
        a0 = (1 / T) * sp.integrate(f, (t, 0, T))
        an = (1 / (T / 2)) * sp.integrate(f * sp.cos(n * 2 * sp.pi * t / T), (t, 0, T))
        bn = (1 / (T / 2)) * sp.integrate(f * sp.sin(n * 2 * sp.pi * t / T), (t, 0, T))
        return a0, an, bn


    # Define the number of terms in the series
    N = 100  # Number of terms in the series

    # Create a pool of worker processes
    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())

    # Start measuring time
    start_time = time.time()

    # Calculate Fourier series coefficients in parallel
    results = pool.map(calculate_coefficients, range(1, N + 1))

    # Close the pool and wait for all processes to finish
    pool.close()
    pool.join()

    # Calculate the Fourier series
    a0, an, bn = zip(*results)
    fourier_series = a0[0] / 2
    for i in range(1, N):
        fourier_series += (an[i - 1] * sp.cos(i * 2 * sp.pi * t / T) +
                           bn[i - 1] * sp.sin(i * 2 * sp.pi * t / T))

    # Stop measuring time
    end_time = time.time()

    # Calculate and display the elapsed time
    elapsed_time = end_time - start_time

    # Append the elapsed time to a file
    with open('mt100.txt', 'a') as file:
        file.write(f"Elapsed Time: {elapsed_time:.6f} seconds\n")

for zu in range(10):
    # Define the symbol and period
    t = sp.symbols('t')
    n = sp.symbols('n')
    T = 2 * sp.pi  # Assuming a period of 2*pi, adjust as needed

    # Define the function to be decomposed
    # Example: f(t) = t for 0 <= t < pi and -t for pi <= t < 2*pi
    f = sp.Piecewise((t, (t >= 0) & (t < sp.pi)), (-t, (t >= sp.pi) & (t < 2 * sp.pi)))


    # Find the Fourier series coefficients
    def calculate_coefficients(n):
        a0 = (1 / T) * sp.integrate(f, (t, 0, T))
        an = (1 / (T / 2)) * sp.integrate(f * sp.cos(n * 2 * sp.pi * t / T), (t, 0, T))
        bn = (1 / (T / 2)) * sp.integrate(f * sp.sin(n * 2 * sp.pi * t / T), (t, 0, T))
        return a0, an, bn


    # Define the number of terms in the series
    N = 500  # Change N to adjust the number of terms in the series

    start_time = time.time()

    results = [calculate_coefficients(n) for n in range(1, N + 1)]

    # Calculate the Fourier series
    a0, an, bn = zip(*results)
    fourier_series = a0[0] / 2
    for i in range(1, N):
        fourier_series += (an[i - 1] * sp.cos(i * 2 * sp.pi * t / T) +
                           bn[i - 1] * sp.sin(i * 2 * sp.pi * t / T))

    end_time = time.time()

    # Calculate and display the elapsed time
    elapsed_time = end_time - start_time

    # Append the elapsed time to a file
    with open('st500.txt', 'a') as file:
        file.write(f"Elapsed Time: {elapsed_time:.2f} seconds\n")

for zu in range(10):
    # Define the symbol and period
    t = sp.symbols('t')
    n = sp.symbols('n')
    T = 2 * sp.pi  # Assuming a period of 2*pi, adjust as needed

    # Define the function to be decomposed
    # Example: f(t) = t for 0 <= t < pi and -t for pi <= t < 2*pi
    f = sp.Piecewise((t, (t >= 0) & (t < sp.pi)), (-t, (t >= sp.pi) & (t < 2 * sp.pi)))


    # Find the Fourier series coefficients
    def calculate_coefficients(n):
        a0 = (1 / T) * sp.integrate(f, (t, 0, T))
        an = (1 / (T / 2)) * sp.integrate(f * sp.cos(n * 2 * sp.pi * t / T), (t, 0, T))
        bn = (1 / (T / 2)) * sp.integrate(f * sp.sin(n * 2 * sp.pi * t / T), (t, 0, T))
        return a0, an, bn


    # Define the number of terms in the series
    N = 100  # Change N to adjust the number of terms in the series

    start_time = time.time()

    results = [calculate_coefficients(n) for n in range(1, N + 1)]

    # Calculate the Fourier series
    a0, an, bn = zip(*results)
    fourier_series = a0[0] / 2
    for i in range(1, N):
        fourier_series += (an[i - 1] * sp.cos(i * 2 * sp.pi * t / T) +
                           bn[i - 1] * sp.sin(i * 2 * sp.pi * t / T))

    end_time = time.time()

    # Calculate and display the elapsed time
    elapsed_time = end_time - start_time

    # Append the elapsed time to a file
    with open('st100.txt', 'a') as file:
        file.write(f"Elapsed Time: {elapsed_time:.2f} seconds\n")




