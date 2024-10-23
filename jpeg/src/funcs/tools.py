import numpy as np
from pprint import pprint
from PIL import Image
from numpy import linalg
from typing import Tuple, List
from math import pi

convertation_matrix_rgb2ycbcr = np.array([
    [0.299, 0.587, 0.114],
    [0.168736, -0.331254, 0.5],
    [0.5, -0.418688, -0.081312]
], dtype=np.float32).T

convertation_vector_rgb2ycbcr = np.array([
    [0],
    [128],
    [128]
], dtype=np.float32).T

convertation_matrix_ycbcr2rgb = np.array([
    [1, 0, 1.402],
    [1, -0.34414, -0.71414],
    [1, 1.772, 0]
], dtype=np.float32).T

matrix_of_quation = None

matrix_of_dct = np.array([
    [0] * 8,
    [0] * 8,
    [0] * 8,
    [0] * 8,
    [0] * 8,
    [0] * 8,
    [0] * 8,
    [0] * 8
], dtype=float)

for i in range(8):
    for j in range(8):
        if i == 0:
            matrix_of_dct[i][j] = 1
        elif i > 0:
            matrix_of_dct[i][j] = np.sqrt(2) * np.cos((2*j + 1) * i * pi)

transposed_matrix_of_dct = matrix_of_dct.T


def fix_image_size_for_jpeg(_pixels_arr):
    pass


def convert_pixel_rgb2ycbcr(_pixel_rgb: Tuple[int, int, int]) -> Tuple[int, int, int]:
    # return np.dot(_pixel_rgb, convertation_matrix_rgb2ycbcr) + convertation_vector_rgb2ycbcr
    return (round(0.299 * _pixel_rgb[0] + 0.587 * _pixel_rgb[1] + 0.114 * _pixel_rgb[2]),
            round(128 + (-0.168736) *
                  _pixel_rgb[0] - 0.331264 * _pixel_rgb[1] + 0.5 * _pixel_rgb[2]),
            round(128 + 0.5 * _pixel_rgb[0] - 0.418688 * _pixel_rgb[1] - 0.081312 * _pixel_rgb[2]))


def convert_pixel_ycbcr2rgb(_pixel_ycbcr: Tuple[int, int, int]) -> Tuple[int, int, int]:
    # return np.dot((_pixel_ycbcr - convertation_vector_rgb2ycbcr), convertation_matrix_ycbcr2rgb)
    return (
        round(_pixel_ycbcr[0] + 1.402 * (_pixel_ycbcr[2] - 128)),
        round(_pixel_ycbcr[0] - 0.34414 *
              (_pixel_ycbcr[1] - 128) - 0.71414 * (_pixel_ycbcr[2] - 128)),
        round(_pixel_ycbcr[0] + 1.772 * (_pixel_ycbcr[1] - 128))
    )


def subsampling(_pixel_arr):
    pass


def discrete_cosine_transform(_submatrix) -> None:
    test_case = [
        [40, 24, 15, 19, 28, 24, 19, 15],
        [38, 34, 35, 35, 31, 28, 27, 29],
        [40, 47, 49, 40, 33, 29, 32, 43],
        [42, 49, 50, 39, 34, 30, 32, 46],
        [40, 47, 46, 35, 31, 32, 35, 43],
        [38, 43, 42, 31, 27, 27, 28, 33],
        [39, 33, 25, 17, 14, 15, 19, 26],
        [29, 16,  6,  1, -4,  0,  7, 18]
    ]
    _test_result = np.zeros(8)
    # _submatrix = test_case
    result = np.dot(matrix_of_dct, np.dot(
        test_case, transposed_matrix_of_dct))
    print(result)
    print(np.dot(transposed_matrix_of_dct, np.dot(result, matrix_of_dct)))


if __name__ == '__main__':
    # discrete_cosine_transform([])
    print(Image.fromarray(np.array([[(0, 0, 0)]])).convert("YCbCr"))
