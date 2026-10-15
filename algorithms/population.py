import numpy as np

def initialize_population(
    population_size,
    dimensions,
    lower_bound,
    upper_bound
):
    population = np.random.uniform(
        lower_bound,
        upper_bound,
        size=(population_size, dimensions)
    )
    return population

def split_population(population):
    midpoint = len(population) // 2
    males = population[:midpoint]
    females = population[midpoint:]

    return males, females