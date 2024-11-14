import numpy as np
from numpy import linalg

convertation_matrix_rgb2ycbcr = np.array([
    [0.29900,  0.58700,   0.11400],
    [-0.16874, -0.33126,  0.50000],
    [0.50000, -0.41869, -0.08131]
], dtype=np.float64).T

convertation_vector = np.array([
    [0],
    [128],
    [128]
], dtype=int).T

convertation_matrix_ycbcr2rgb = np.array([
    [1, 0, 1.402],
    [1, -0.34414, -0.71414],
    [1, 1.77200, 0]
], dtype=np.float64).T

convertation_matrix_inv_rgb2ycbcr = linalg.inv(convertation_matrix_rgb2ycbcr)

matrix_of_quantization = np.zeros((8, 8), dtype=int)

zigzag_way = [0, 1, 8, 16, 9, 2, 3, 10, 17, 24, 32, 25, 18, 11, 4, 5, 12, 19, 26, 33,
              40, 48, 41, 34, 27, 20, 13, 6, 7, 14, 21, 28, 35, 42, 49, 56, 57, 50,
              43, 36, 29, 22, 15, 23, 30, 37, 44, 51, 58, 59, 52, 45, 38, 31, 39,
              46, 53, 60, 61, 54, 47, 55, 62, 63]

convertation_int_matrix_rgb2ycbcr = np.array([
    [77, 150, 29],
    [-43, -84, 127],
    [127, -106, -21]
], dtype=int).T

inv_convertation_int_matrix_rgb2ycbcr = linalg.inv(
    convertation_int_matrix_rgb2ycbcr)

if __name__ == '__main__':
    print(linalg.inv(convertation_matrix_rgb2ycbcr))
