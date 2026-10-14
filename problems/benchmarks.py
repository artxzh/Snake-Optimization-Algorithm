import numpy as np

def rastrigin(solution):
    x = np.asarray(solution)

    return 10 * len(x) + np.sum(
        x**2 - 10 * np.cos(2 * np.pi * x)
    )

def rosenbrock(solution):
    x = np.asarray(solution)

    return np.sum(
        100 * (x[1:] - x[:-1] ** 2) ** 2 + 
        (x[:-1] - 1) ** 2
    )