import math

def temp_update(cur_it, max_it):
    temp = math.exp(-cur_it / max_it)
    return temp