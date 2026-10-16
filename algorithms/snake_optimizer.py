from population import *
from fitness import *
from behavior import *
from oscillation import *
from problems.objective import sphere
import math

#Global constants
c1 = 0.5
c3 = 2

def snake_optimizer(population_size, lower_bound, upper_bound, max_it, cur_it, dimensions):
    population = initialize_population(
        population_size,
        dimensions,
        lower_bound,
        upper_bound)

    males, females = split_population(population)

    while cur_it < max_it:
        cur_it += 1
        male_fitness, female_fitness = evaluate_each_group(males, females, sphere)
        
        temp = temp_update(cur_it, max_it)
        food = food_update(0.5, cur_it, max_it)

        if food <0.25:
            c2 = oscillation_factor_c2(cur_it, max_it)
            population = random_exploration_update(
                lower_bound, 
                upper_bound, 
                males, 
                females, 
                c2, 
                food_equation_male,
                food_equation_female, 
                male_fitness,
                female_fitness)
        else:
            if temp > 0.6:
                #Exploração Local
                population = local_exploration_update(
                    males, 
                    females, 
                    male_fitness, 
                    female_fitness, 
                    c3, 
                    temp)
                
            else:
                random = np.random.uniform(0,1)
                if(random < 0.5):
                    #Modo de Combate
                    pass
                else:
                    #Modo de Acasalamento
                    pass
        if cur_it > max_it:
            break
    

