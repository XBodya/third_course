import numpy as np
import numpy.linalg as linalg
import matplotlib.pyplot as plt
from pprint import pprint

LEFT = 0.5
RIGHT = 1.5
Y_LIM_UP, Y_LIM_DOWN = 0.25, 0

n = int(input())
matrix_divided_diff = np.zeros((n + 1, n + 2), dtype=np.float32)


def my_func(x):
    return (1 + abs(np.log(x))) / (1 + 25 * x * x)


def get_coef_for_m1(nodes, i, j):
    mul = 1
    for k in range(j):
        mul *= nodes[i]-nodes[k]
    return mul


def get_newton_coefs_1(nodes, n):
    M = []
    #   print(M)
    for i in range(n + 1):
        M.append([0] * (n + 1))
        for j in range(n + 1):
            if j == 0:
                M[i][0] = 1
            elif j > i:
                M[i][j] = 0
            else:
                M[i][j] = get_coef_for_m1(nodes, i, j)
    # print(*M, sep='\n')
    M = np.array(M, dtype=np.float32)
    B = np.array(list(map(my_func, nodes[:])))
    RES = linalg.solve(M, B)
    # pprint(M)
    # pprint(RES)
    return RES


def get_divided_diff(start, end):
    global matrix_divided_diff
    # print(f"Start: {start}, End: {end}", matrix_divided_diff[start][end - 1], matrix_divided_diff[start + 1][end],
    #      matrix_divided_diff[start][0], matrix_divided_diff[end][0])
    return (matrix_divided_diff[start][end - 1] - matrix_divided_diff[start + 1][end - 1]) / (matrix_divided_diff[start][0] - matrix_divided_diff[start + end - 1][0])


def calc_coef_by_matr_divided_diff(nodes, n):
    global matrix_divided_diff
    for i in range(n + 1):
        matrix_divided_diff[i][0] = nodes[i]
        matrix_divided_diff[i][1] = my_func(nodes[i])
    for i in range(2, n + 2):
        for j in range(n - i + 2):
            matrix_divided_diff[j][i] = get_divided_diff(j, i)
            # matrix_divided_diff[j][i] = 1
            # print(j, i)
            # get_divided_diff(j, i)
    return matrix_divided_diff.copy()


def calc_divided_diff_by_formula(nodes, n, m):
    _sum = 0
    for i in range(n - m, n + 1):
        _mul = my_func(nodes[i])
        for j in range(n - m, n + 1):
            if i != j:
                _mul *= (1 / (nodes[i] - nodes[j]))
        _sum += _mul
    return _sum


def calc_coef_divdiff_v3(nodes, n):
    KOEFFS = []
    for k in range(n + 1):
        KOEFFS.append(calc_divided_diff_by_formula(nodes, k, k))
    return KOEFFS


def newton_polynomial(koeffs, nodes, x):
    deg_plus_1 = len(koeffs)
    result = 0
    for i in range(deg_plus_1):
        _mul = koeffs[i]
        for j in range(i):
            _mul *= (x - nodes[j])
        result += _mul
    return result


def main(n):
    a = np.linspace(LEFT, RIGHT, n+1)
    a_2 = np.linspace(LEFT, RIGHT, 2*n+1)
    v1 = get_newton_coefs_1(a, n)
    v2 = calc_coef_by_matr_divided_diff(a, n)
    v3 = calc_coef_divdiff_v3(a, n)
    print(v1)
    print(v2)
    print(v3)
    print(my_func(1))
    print(newton_polynomial(v1, a, 0.78))
    fig, ax = plt.subplots(figsize=(20, 9))
    ax.plot(a_2, list(map(lambda x: my_func(x), a_2)), color='r',
            linewidth=2, label='функция')

    ax.plot(a_2, list(map(lambda x: newton_polynomial(v2[0][1:], a, x), a_2)),
            '--', linewidth=2, label='интерполяция способ 2',
            color='b')
    ax.plot(a, list(map(lambda x: newton_polynomial(v2[0][1:], a, x), a)), 'ro',
            linewidth=6,
            color='m')
    ax.set_xlabel('x label')
    ax.set_ylabel('y label')
    plt.grid()
    plt.ylim(Y_LIM_DOWN, Y_LIM_UP)
    plt.legend()
    plt.show()



main(n)
