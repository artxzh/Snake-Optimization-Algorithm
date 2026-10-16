import numpy as np
from algorithms.snake_optimizer import snake_optimizer
from algorithms.fitness import evaluate_group
from problems.objective import sphere

if __name__ == "__main__":
    population_size = 50
    lower_bound = -100
    upper_bound = 100
    max_it = 1000
    cur_it = 0
    dimensions = 30

    resultado = snake_optimizer(
        population_size,
        lower_bound,
        upper_bound,
        max_it,
        cur_it,
        dimensions)

    best_population, _, _ = resultado

    matriz = best_population[0]          # população final (50 x 30)
    
    fitness = evaluate_group(matriz, sphere)   # vetor (50,), um valor por indivíduo

    idx_melhor = np.argmin(fitness)      # sphere é minimização
    melhor_individuo = matriz[idx_melhor]
    melhor_fitness = fitness[idx_melhor]
     # Matriz completa (50 x 30) em texto
    np.savetxt("./results/resultado.txt", best_population, fmt="%.8f", delimiter=";")

    print("Best Population:", best_population)
    print("Melhor índice:", idx_melhor)
    print("Melhor fitness:", melhor_fitness)