from common.calculation_tools import critical_range_finder, eval_equation



def iterator_function(x1, y1, x2, y2, equation, iter_count = 0, max_iter = 100):
    x = (x1+x2)/2
    y = eval_equation(equation, x)
    
    if abs(y) < 1e-12:
        return x, y

    if iter_count == max_iter:
        return x, y

    if y*y2 < 0:
        return iterator_function(x, y, x2, y2, equation, iter_count+1)
    elif y*y1 < 0: 
        return iterator_function(x1, y1, x, y, equation, iter_count+1)
    else:
        raise ValueError("Bisection method failed: No sign change was found.")



def solution_finder(equation):
    roots = []

    critical_ranges = critical_range_finder(equation)

    for range in critical_ranges:
        x_begin = range[0][0]
        x_end = range[1][0]

        x_new, y_new = iterator_function(x_begin, eval_equation(equation, x_begin), x_end, eval_equation(equation, x_end), equation)
        roots.append((x_new, y_new))
    
    print(roots)
    return roots

if __name__ == '__main__':
    solution_finder(equation)
