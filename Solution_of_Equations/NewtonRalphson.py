from common.calculation_tools import critical_range_finder, eval_equation
import sympy as sp
import random


def iterator_function(x_initial, equation, iter_count=0, max_iter=100):

    dy = eval_diff_equation(equation, x_initial)

    if abs(dy) < 1e-14:
        raise ValueError("Derivative too close to zero.")

    y = eval_equation(equation, x_initial)

    x = x_initial - y / dy

    y_new = eval_equation(equation, x)

    if abs(y_new) < 1e-12:
        return x, y_new

    if iter_count >= max_iter:
        return x, y_new

    return iterator_function(x, equation, iter_count+1, max_iter)


def eval_diff_equation(equation, x_val):
    x = sp.Symbol('x')
    diff_equation = sp.diff(equation, x)
    return diff_equation.subs(x, x_val)


def solution_finder(equation):
    roots = []
    
    critical_ranges = critical_range_finder(equation)


    for range in critical_ranges:
        x_begin = range[0][0]
        x_end = range[1][0]

        x_initial = random.uniform(x_begin, x_end)

        x_new, y_new = iterator_function(x_initial, equation) 
        roots.append((x_new, y_new))


    roots.append((x_new, y_new))

    print(roots)

    return roots
