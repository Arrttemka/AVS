import numpy as np

def generate_system(size, seed=42):
    np.random.seed(seed)

    coeff_matrix = np.random.randint(-10, 10, size=(size, size))
    rhs_vector = np.random.randint(-10, 10, size=size)

    return coeff_matrix, rhs_vector

def solve_system(args):
    matrix, vector = args
    det_A = np.linalg.det(matrix)

    if det_A == 0:
        return None  # система не имеет единственного решения

    n = len(vector)
    solutions = []

    for i in range(n):
        temp_matrix = matrix.copy()
        temp_matrix[:, i] = vector
        det_i = np.linalg.det(temp_matrix)
        x_i = det_i / det_A
        solutions.append(x_i)

    return solutions
