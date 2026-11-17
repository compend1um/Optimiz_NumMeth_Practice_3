
from source.task2.data_generation import generate_points
from source.task2.data_generation import add_outlier

from source.task2.geometric_median import calculate_arithmetic_mean
from source.task2.geometric_median import calculate_geometric_median


from source.task2.geometric_median import make_f
from source.task2.geometric_median import make_grad

from source.task2.geometric_median import print_result_without_outlier
from source.task2.geometric_median import print_result_with_outlier

from source.common.gradient_descent import gradient_descent



points = generate_points(50)

arithmetic_mean_point, arithmetic_mean_value = calculate_arithmetic_mean(points)

geometric_median_point, geometric_median_value = \
    calculate_geometric_median(points, arithmetic_mean_point)


print_result_without_outlier(
        arithmetic_mean_point, arithmetic_mean_value,
        geometric_median_point, geometric_median_value
)

# outlier

points_out = add_outlier(points)
# print(points_out)

arithmetic_mean_point_out, arithmetic_mean_value_out = calculate_arithmetic_mean(points_out)

# Стартуем из среднего (с выбросом)
geometric_median_point_out, geometric_median_value_out = gradient_descent(
    make_f(points_out), make_grad(points_out), arithmetic_mean_point_out, step=0.1, eps=10**(-4)
)

print_result_with_outlier(
        arithmetic_mean_point_out, arithmetic_mean_value_out,
        geometric_median_point_out, geometric_median_value_out
)


