import math

import numpy as np

def oscillation_factor_c2(iteration, max_iterations):
    progress = iteration / max_iterations

    return abs(
        np.exp(-progress * np.pi * 1.5)
        * np.cos(3 * 6 * progress * np.pi)
    )

def oscillation_exploration_factor_male(rand_male, ith_male, evaluate):
    fitness__random_male = evaluate(rand_male)
    fitness_ith_male = evaluate(ith_male)
    result  = math.exp(-fitness__random_male / fitness_ith_male)
    return result

def oscillation_exploration_factor_female(rand_female, ith_female, evaluate):
    fitness__random_female = evaluate(rand_female)
    fitness_ith_female = evaluate(ith_female)
    result  = math.exp(-fitness__random_female / fitness_ith_female)
    return result