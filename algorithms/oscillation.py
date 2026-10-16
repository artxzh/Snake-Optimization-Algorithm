import math

import numpy as np

def oscillation_factor_c2(iteration, max_iterations):
    progress = iteration / max_iterations

    return abs(
        np.exp(-progress * np.pi * 1.5)
        * np.cos(3 * 6 * progress * np.pi)
    )

def food_equation_male(rand_male, ith_male):
    result  = math.exp(-rand_male / ith_male)
    return result

def food_equation_female(rand_female, ith_female):
    result  = math.exp(-rand_female / ith_female)
    return result