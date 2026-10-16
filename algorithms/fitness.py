import numpy as np

def evaluate_group(group, objective_function):
    fitness = np.array([objective_function(individual) for individual in group])
    return fitness

def evaluate_each_group(males, females, objective_function):
    male_fitness = evaluate_group(males, objective_function)
    female_fitness = evaluate_group(females, objective_function)

    return male_fitness, female_fitness

def best_fitness_index(male_fitness, female_fitness):
    population_fitness = np.concatenate((male_fitness, female_fitness))
    best_index = 0
    for i in range(len(population_fitness)):
        if population_fitness[i] < population_fitness[best_index]:
            best_index = i
    return best_index