from population import *
from fitness import *
from problems.objective import sphere

def snake_optimizer(population_size, lower_bound, upper_bound, max_it, cur_it, dimensions):
    population = initialize_population(population_size, dimensions, lower_bound, upper_bound)

    males, females = split_population(population)

    while cur_it < max_it:
        cur_it += 1
        best_fitnessm, best_fitnessf = evaluate_each_group(males, females, sphere)
        print(f"Iteration {cur_it}: Males: {males}, Females: {females}, Best Male Fitness: {best_fitnessm}, Best Female Fitness: {best_fitnessf}")
    

