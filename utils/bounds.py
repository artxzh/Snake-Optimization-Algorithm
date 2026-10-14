import numpy as np

def clip_bounds(position, lower_bound, upper_bound):
    return np.clip(
        position,
        lower_bound,
        upper_bound
    )