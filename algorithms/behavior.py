import math

def temp_update(cur_it, max_it):
    temp = math.exp(-cur_it / max_it)
    return temp

def food_update(c1, cur_it, max_it):
    food = c1 * math.exp(cur_it - max_it / max_it)
    return food

