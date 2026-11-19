from source.task1.extrema import find_extrema
from source.task1.boundary_search import find_boundary_extrema


def print_results(title, results):
    print(f"\n{title}")

    for i, (point, value) in enumerate(results, 1):
        print(f"{i}. x = {point[0]:.6f}, y = {point[1]:.6f}, F = {value:.8f}")

def run_task1():

    inside_min = find_extrema('min')
    inside_max = find_extrema('max')

    boundary_min = find_boundary_extrema('min')
    boundary_max = find_boundary_extrema('max')

    print_results("ВНУТРЕННИЕ МИНИМУМЫ", inside_min)
    print_results("ВНУТРЕННИЕ МАКСИМУМЫ", inside_max)

    print_results("МИНИМУМЫ НА ГРАНИЦЕ", boundary_min)
    print_results("МАКСИМУМЫ НА ГРАНИЦЕ", boundary_max)

    all_min = inside_min + boundary_min
    all_max = inside_max + boundary_max

    global_min_value = min(i[1] for i in all_min)
    global_max_value = max(i[1] for i in all_max)

    global_min = [
        i for i in all_min
        if abs(i[1] - global_min_value) < 10 ** (-6)
    ]

    global_max = [
        i for i in all_max
        if abs(i[1] - global_max_value) < 10 ** (-6)
    ]

    print_results("ГЛОБАЛЬНЫЕ МИНИМУМЫ", global_min)
    print_results("ГЛОБАЛЬНЫЕ МАКСИМУМЫ", global_max)
