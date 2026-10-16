import math

import numpy as np

def oscillation_factor_c2(iteration, max_iterations):
    progress = iteration / max_iterations

    return abs(
        np.exp(-progress * np.pi * 1.5)
        * np.cos(3 * 6 * progress * np.pi)
    )

def oscillation_exploration_factor_male(male, female, evaluate):
    fitness_male = evaluate(male)
    fitness_female = evaluate(female)
    result  = math.exp(-fitness_male / fitness_female)
    return result