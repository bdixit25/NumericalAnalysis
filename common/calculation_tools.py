import math
import numpy as np
from itertools import pairwise


def eval_equation(equation, x = None):
    try:
        return eval(equation) 
    except:
        print("You must provide the value at which th equation has to be evaluated.")


def eval_equation(equation, x = None):
    try:
        return eval(equation) 
    except:
        print("You must provide the value at which th equation has to be evaluated.")


# Simple function to find the values of the given function in a given range
def value_finder(equation, start = -1000, stop = 1000, step = 0.1):
    x_values = np.arange(start, stop, step)
    y_values = []

    for x in x_values:
        y_val = eval_equation(equation, x)
        y_values.append(y_val)

    val_list = list(zip(x_values, y_values))
    return val_list 

# Function to find the ranges where roots might exist
def critical_range_finder(equation):
    critical_ranges = []
    values = value_finder(equation)

    for a, b in pairwise(values):
        if a[1]*b[1] < 0:
            critical_ranges.append((a, b))
    return critical_ranges
