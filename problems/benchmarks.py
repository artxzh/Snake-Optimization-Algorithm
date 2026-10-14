import numpy as np

def rastrigin(solution):
    x = np.asarray(solution)

    return 10 * len(x) + np.sum(
        x**2 - 10 * np.cos(2 * np.pi * x)
    )