import numpy as np
import numpy.linalg as linalg
import matplotlib.pyplot as plt
from pprint import pprint

LEFT = 0.5
RIGHT = 1.5

def function(x):
    return (1 + np.abs(np.log(x))) / (1 + 25 * x * x)

def trapezoid(a, b, n, x, f, g=None):
    nodes = [a] * n
    for i in range(1, n - 1):
        nodes[i] = a + i * ((b - 1) / n)
    nodes[n - 1] = b
    s = 0
    for i in range(n):
        s += f(nodes[i])
    if g == None:
        return (b - a) * (f(nodes[0]) + s * 2 + f(nodes[n - 1])) / 2 * n
    else:
        return (b - a) * ((f(nodes[0]) * g(nodes[0])) + s * 2 + f(nodes[n - 1]) * g(nodes[n - 1])) / 2 * n


def calculate_integral_by_simpson_method(x, f, a, b, N):
    f_x, h = f(x), (b - a) / N
    return h / 3 * (f_x[0] + 4 * np.sum(f_x[1:N:2]) + 2 * np.sum(f_x[2:N - 1:2]) + f_x[-1])

def calculate_integral_by_trapezoid_method(x, f, a, b, N):
    f_x, h = f(x), (b - a) / N
    return h * (0.5 * (f_x[0] + f_x[-1]) + np.sum(f_x[1:-1]))

def scalar(f, g, x, N):
    return trapezoid(LEFT, RIGHT, x, f, N)

def calculate_coefficients_for_polynom(a, b, degree_polynom, N, integrate_method=calculate_integral_by_trapezoid_method):
    matrix_of_system = np.zeros((degree_polynom + 1, degree_polynom + 1))
    joined_vector = np.zeros(degree_polynom + 1)
    if integrate_method is calculate_integral_by_simpson_method:
        N += N % 2
    sample_x = np.linspace(a, b, N + 1)
    for i in range(degree_polynom + 1):
        for j in range(degree_polynom + 1):
            matrix_of_system[i][j] = integrate_method(sample_x, lambda x: np.pow(x, i) * np.pow(x, j), a, b, N)
        joined_vector[i] = integrate_method(sample_x, lambda x: function(x) * np.pow(x, i), a, b, N)
    coefficients = np.linalg.solve(matrix_of_system, joined_vector)
    return coefficients

def calculate_polynom_by_coefficients(x_point, coefficients):
    return sum([coefficients[i] * np.pow(x_point, i) for i in range(len(coefficients))])

def main():
    degree = 10
    N = 10 * (degree + 1) ** 2
    coeffs1 = calculate_coefficients_for_polynom(LEFT, RIGHT, degree, N)
    coeffs2 = calculate_coefficients_for_polynom(LEFT, RIGHT, degree, N, calculate_integral_by_simpson_method)
    sample = np.linspace(LEFT, RIGHT, 1000)
    f_sample = function(sample)
    fig, ax = plt.subplots(figsize=(20, 9))
    ax.plot(sample, f_sample, color='r',
            linewidth=2, label='функция')
    ax.set_xlabel('x label')
    ax.set_ylabel('y label')
    plt.grid()
    # plt.ylim(Y_LIM_DOWN, Y_LIM_UP)
    plt.legend()
    plt.show()

main()