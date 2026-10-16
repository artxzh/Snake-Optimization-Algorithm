import math
import random
import numpy as np
from utils.bounds import clip_bounds

def temp_update(cur_it, max_it):
    temp = math.exp(-cur_it / max_it)
    return temp

def food_update(c1, cur_it, max_it):
    food = c1 * math.exp(cur_it - max_it / max_it)
    return food

def random_exploration_update(lb, ub, males, females, c2, food_function_male, food_function_female, fitness_male, fitness_female):
    new_males = males.copy()
    new_females = females.copy()

    for i in range(len(males)):
        random_index = random.randint(0, len(males) - 1)

        current_fitness = fitness_male[i]
        random_fitness = fitness_male[random_index]

        var = food_function_male(current_fitness, random_fitness)
        r = np.random.uniform(0, 1, size=males.shape[1])
        sign = random.choice([-1, 1])

        new_position = (
            males[random_index]
            + sign * c2 * var * ((ub - lb) * r + lb)
        )

        new_males[i] = clip_bounds(new_position, lb, ub)

    for i in range(len(females)):
        random_index = random.randint(0, len(females) - 1)

        current_fitness = fitness_female[i]
        random_fitness = fitness_female[random_index]

        var = food_function_female(current_fitness, random_fitness)
        r = np.random.uniform(0, 1, size=females.shape[1])
        sign = random.choice([-1, 1])

        new_position = (
            females[random_index]
            + sign * c2 * var * ((ub - lb) * r + lb)
        )

        new_females[i] = clip_bounds(new_position, lb, ub)

    new_population = np.concatenate((new_males, new_females), axis=0)

    return new_population

def local_exploration_update(males, females, fitness_male, fitness_female, c3, temp):
    new_males = males.copy()
    new_females = females.copy()

    for i in range(len(males)):
        best_male_index = np.argmin(fitness_male)
        sing = random.choice([-1, 1])
        r = np.random.uniform(0, 1, size=males.shape[1])
        new_position = (
            males[best_male_index]
            + sing * c3 * temp * r * (males[best_male_index] - males[i])
        )

        new_males[i] = clip_bounds(new_position, lb, ub)

    for i in range(len(females)):
        best_female_index = np.argmin(fitness_female)
        sing = random.choice([-1, 1])
        r = np.random.uniform(0, 1, size=females.shape[1])
        new_position = (
            females[best_female_index]
            + sing * c3 * temp * r * (females[best_female_index] - females[i])
        )

        new_females[i] = clip_bounds(new_position, lb, ub)

    return np.concatenate((new_males, new_females), axis=0)

def combat_mode_update(males, females, fitness_male, fitness_female, c3, food_factor, combat_function_male, combat_function_female):
    new_males = males.copy()
    new_females = females.copy()

    for i in range(len(males)):
        best_female_index = np.argmin(fitness_female)
        r = np.random.uniform(0, 1, size=males.shape[1])
        combat_factor = combat_function_male(fitness_male[best_female_index], fitness_male[i])
        new_position = (
            males[i] + c3 * combat_factor * r * (food_factor * fitness_female[best_female_index] - males[i])
        )

        new_males[i] = clip_bounds(new_position, lb, ub)

    for i in range(len(females)):
        best_male_index = np.argmin(fitness_male)
        r = np.random.uniform(0, 1, size=females.shape[1])
        combat_factor = combat_function_female(fitness_female[best_male_index], fitness_female[i])
        new_position = (
            females[i] + c3 * combat_factor * r * (food_factor * fitness_male[best_male_index] - females[i])
        )

        new_females[i] = clip_bounds(new_position, lb, ub)

    return np.concatenate((new_males, new_females), axis=0)