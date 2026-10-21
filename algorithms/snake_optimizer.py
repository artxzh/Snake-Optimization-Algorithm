import numpy as np

from .behavior import (
    combat_update,
    food_update,
    local_exploration_update,
    reproduction_update,
    random_exploration_update,
    temp_update,
)
from .fitness import evaluate_each_group
from .oscillation import (
    combat_equation_female,
    combat_equation_male,
    food_equation_female,
    food_equation_male,
    mating_equation_female,
    mating_equation_male,
)
from .population import initialize_population, split_population
from problems.objective import sphere


def snake_optimizer(
    population_size,
    lower_bound,
    upper_bound,
    max_it,
    cur_it,
    dimensions,
    objective_function=sphere,
    *,
    c1=0.5,
    c2=0.005,
    c3=0.7,
):
    population = initialize_population(
        population_size,
        dimensions,
        lower_bound,
        upper_bound,
    )

    males, females = split_population(population)

    while cur_it < max_it:
        cur_it += 1
        male_fitness, female_fitness = evaluate_each_group(
            males,
            females,
            objective_function,
        )

        temp = temp_update(cur_it, max_it)
        food = food_update(c1, cur_it, max_it)

        if food < 0.25:
            population = random_exploration_update(
                lower_bound,
                upper_bound,
                males,
                females,
                c2,
                food_equation_male,
                food_equation_female,
                male_fitness,
                female_fitness,
            )
        else:
            if temp > 0.6:
                population = local_exploration_update(
                    males,
                    females,
                    male_fitness,
                    female_fitness,
                    lower_bound,
                    upper_bound,
                    c3,
                    temp,
                )
            else:
                random_value = np.random.uniform(0, 1)
                if random_value < 0.5:
                    population = combat_update(
                        males,
                        females,
                        male_fitness,
                        female_fitness,
                        lower_bound,
                        upper_bound,
                        c3,
                        food,
                        combat_equation_male,
                        combat_equation_female,
                    )
                else:
                    population = reproduction_update(
                        males,
                        females,
                        male_fitness,
                        female_fitness,
                        lower_bound,
                        upper_bound,
                        c3,
                        food,
                        mating_equation_male,
                        mating_equation_female,
                    )

        males, females = split_population(population)

    return population
