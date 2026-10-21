import numpy as np
from algorithms.snake_optimizer import snake_optimizer
from algorithms.fitness import evaluate_group
from problems.objective import sphere

if __name__ == "__main__":
    population_size = 50
    dimensions = 5
    max_it = 100
    cur_it = 0
    cap = 1
    lower_bound = np.full(dimensions, cap * -1)
    upper_bound = np.full(dimensions, cap)


    resultado = snake_optimizer(
        population_size,
        lower_bound,
        upper_bound,
        max_it,
        cur_it,
        dimensions)

    best_population = resultado
    for array in best_population:
        print(array)
    fitness = evaluate_group(best_population, sphere)

    print(fitness)
    best_fitness = np.min(fitness)
    print(best_fitness)
    
    np.savetxt("./results/resultado.txt", best_population, fmt="%.8f", delimiter=";")