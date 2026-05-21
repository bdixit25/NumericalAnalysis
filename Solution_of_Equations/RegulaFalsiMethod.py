from common.calculation_tools import critical_range_finder, eval_equation


def iterator_function(x1, y1, x2, y2, equation, iter_count = 0, max_iter = 100):
    x = (x2*y1 - x1*y2)/(y1 - y2)
    y = eval_equation(equation, x)

    if iter_count == max_iter:
        return x, y

    return iterator_function(x, y, x2, y2, equation, iter_count+1)
    

def solution_finder(equation):
    roots = []

    critical_ranges = critical_range_finder(equation)
    print(f"critical_ranges = {critical_ranges}")

    for range in critical_ranges:
        x_begin = range[0][0]
        x_end = range[1][0]

        x_new, y_new = iterator_function(x_begin, eval_equation(equation, x_begin), x_end, eval_equation(equation, x_end), equation)
        roots.append((x_new, y_new))
    
    print(roots)
    return roots

if __name__ == '__main__':
    solution_finder(equation)
    
