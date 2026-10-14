import numpy as np

def initialize_population(
    population_size,
    lower_bound,
    upper_bound,
    rng
):

    return rng.uniform(
        lower_bound,
        upper_bound,
        size = (population_size, len(lower_bound))
    )
