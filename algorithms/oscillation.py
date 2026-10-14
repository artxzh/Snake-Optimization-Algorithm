import numpy as np

def oscillation_factor(iteration, max_iterations):
    progress = iteration / max_iterations

    return abs(
        np.exp(-progress * np.pi * 1.5)
        * np.cos(3 * 6 * progress * np.pi)
    )