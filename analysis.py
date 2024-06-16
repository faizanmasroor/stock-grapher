import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# Pass in a np.array to return a np.array, s.t. each value represents the original value's percentage growth from the
# prior value
def growth_arr(arr: np.array) -> np.array:
    return_arr = np.zeros(len(arr))
    for idx in range(1, len(arr)):
        prev = arr[idx-1]
        curr = arr[idx]
        ptg_growth = 100 * (curr - prev) / prev
        return_arr[idx] = ptg_growth
    return return_arr
