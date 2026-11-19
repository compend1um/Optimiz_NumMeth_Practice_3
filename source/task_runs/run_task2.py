
from source.task2.data_generation import generate_points
from source.task2.data_generation import add_outlier

from source.task2.geometric_median import calculate_arithmetic_mean
from source.task2.geometric_median import calculate_geometric_median


from source.task2.geometric_median import make_f
from source.task2.geometric_median import make_grad

from source.task2.geometric_median import print_result_without_outlier
from source.task2.geometric_median import print_result_with_outlier

from source.task2.geometric_median import compare
from source.task2.geometric_median import plot_results

from source.common.gradient_descent import gradient_descent


def run_task_2(key):

    points = generate_points(50)

    arithmetic_mean_point, arithmetic_mean_value = calculate_arithmetic_mean(points)

    geometric_median_point, geometric_median_value = \
        calculate_geometric_median(points, arithmetic_mean_point)


    points_out = add_outlier(points)

    arithmetic_mean_point_out, arithmetic_mean_value_out = calculate_arithmetic_mean(points_out)

    geometric_median_point_out, geometric_median_value_out = gradient_descent(
        make_f(points_out), make_grad(points_out), arithmetic_mean_point_out, step=0.01, eps=10**(-6)
    )

    if key == "print_results":

        print_result_without_outlier(
            arithmetic_mean_point, arithmetic_mean_value,
            geometric_median_point, geometric_median_value
        )

        print_result_with_outlier(
                arithmetic_mean_point_out, arithmetic_mean_value_out,
                geometric_median_point_out, geometric_median_value_out
        )

        compare(arithmetic_mean_point_out, arithmetic_mean_point,
                    geometric_median_point_out, geometric_median_point)


    elif key == "show_plot":

        plot_results(
            points, points_out,
            arithmetic_mean_point, geometric_median_point,
            arithmetic_mean_point_out, geometric_median_point_out
        )

    else:
        exit("Unknown key")

