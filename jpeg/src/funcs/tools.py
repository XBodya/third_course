import numpy as np
from pprint import pprint
from PIL import Image
from numpy import linalg
from typing import Tuple, List
from math import pi
import itertools

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

matrix_of_quantization = np.zeros((8, 8), dtype=int)


def init_matrix_of_q(_quality_factor):
    for i in range(8):
        for j in range(8):
            matrix_of_quantization[i][j] = 1 + (i * j) * _quality_factor
    print(matrix_of_quantization)


matrix_of_quantization_for_y = np.array([
    [16, 11, 10, 16, 24, 40, 51, 61],
    [12, 12, 14, 19, 26, 58, 60, 55],
    [14, 13, 16, 24, 40, 57, 69, 56],
    [14, 17, 22, 29, 51, 87, 80, 62],
    [18, 22, 37, 56, 68, 109, 103, 77],
    [24, 35, 55, 64, 81, 104, 113, 92],
    [49, 64, 78, 87, 103, 121, 120, 101],
    [72, 92, 95, 98, 112, 100, 103, 99]
])

matrix_of_quantization_for_c = np.array([
    [17, 18, 24, 47, 99, 99, 99, 99],
    [18, 21, 26, 66, 99, 99, 99, 99],
    [24, 26, 56, 99, 99, 99, 99, 99],
    [47, 66, 99, 99, 99, 99, 99, 99],
    [99, 99, 99, 99, 99, 99, 99, 99],
    [99, 99, 99, 99, 99, 99, 99, 99],
    [99, 99, 99, 99, 99, 99, 99, 99],
    [99, 99, 99, 99, 99, 99, 99, 99]
])

test_eye = np.eye(5)

matrix_of_dct = np.zeros((8, 8), dtype=np.float64)

for i in range(8):
    for j in range(8):
        if i == 0:
            matrix_of_dct[i][j] = (1 / (2 * np.sqrt(2)))
        elif i > 0:
            matrix_of_dct[i][j] = 0.5 * np.cos(((2*j + 1) * i * pi) / 16)

transposed_matrix_of_dct = matrix_of_dct.T

inv_matrix_of_dct = linalg.inv(matrix_of_dct)

inv_transposed_matrix_of_dct = linalg.inv(transposed_matrix_of_dct)

zigzag_way = [0, 1, 8, 16, 9, 2, 3, 10, 17, 24, 32, 25, 18, 11, 4, 5, 12, 19, 26, 33,
              40, 48, 41, 34, 27, 20, 13, 6, 7, 14, 21, 28, 35, 42, 49, 56, 57, 50,
              43, 36, 29, 22, 15, 23, 30, 37, 44, 51, 58, 59, 52, 45, 38, 31, 39,
              46, 53, 60, 61, 54, 47, 55, 62, 63]


def fix_image_size_for_jpeg(_pixels_arr, size):
    need_cols = (8 - (size[0] % 8)) if size[0] % 8 else 0
    need_rows = (8 - (size[1] % 8)) if size[1] % 8 else 0
    # print(need_cols, need_rows)
    # print(size)
    if not need_cols and not need_rows:
        return
    new_pixels_arr = np.zeros(
        (size[0] + need_cols, size[1] + need_rows, 3), dtype=int)
    # for i in range(need_rows):
    for i in range(size[0] + need_cols):
        for j in range(size[1] + need_rows):
            if i < size[0] and j < size[1]:
                new_pixels_arr[i][j] = convert_pixel_rgb2ycbcr(
                    tuple(_pixels_arr[i][j]))
            elif i < size[0] and j >= size[1]:
                new_pixels_arr[i][j] = convert_pixel_rgb2ycbcr(
                    tuple(new_pixels_arr[i][size[1] - 1]))
            else:
                new_pixels_arr[i][j] = convert_pixel_rgb2ycbcr(tuple(
                    new_pixels_arr[size[0] - 1][j]))
    return new_pixels_arr


def convert_pixel_rgb2ycbcr(_pixel_rgb: Tuple[int, int, int]) -> Tuple[int, int, int]:
    # return np.dot(_pixel_rgb, convertation_matrix_rgb2ycbcr) + convertation_vector_rgb2ycbcr
    return (int(0.299 * _pixel_rgb[0] + 0.587 * _pixel_rgb[1] + 0.114 * _pixel_rgb[2]),
            int(128 + (-0.168736) *
                _pixel_rgb[0] - 0.3313 * _pixel_rgb[1] + 0.5 * _pixel_rgb[2]),
            int(128 + 0.5 * _pixel_rgb[0] - 0.4187 * _pixel_rgb[1] - 0.0813 * _pixel_rgb[2]))


def convert_pixel_ycbcr2rgb(_pixel_ycbcr: Tuple[int, int, int]) -> Tuple[int, int, int]:
    # return np.dot((_pixel_ycbcr - convertation_vector_rgb2ycbcr), convertation_matrix_ycbcr2rgb)
    return (
        int(_pixel_ycbcr[0] + 1.402 * (_pixel_ycbcr[2] - 128)),
        int(_pixel_ycbcr[0] - 0.34414 *
            (_pixel_ycbcr[1] - 128) - 0.71414 * (_pixel_ycbcr[2] - 128)),
        int(_pixel_ycbcr[0] + 1.772 * (_pixel_ycbcr[1] - 128))
    )


def subsampling(_pixel_arr):
    pass


def inv_subsampling(_pixel_arr):
    pass


def discrete_cosine_transform(_pixels_arr) -> None:
    # test_case = [
    #     [40, 24, 15, 19, 28, 24, 19, 15],
    #     [38, 34, 35, 35, 31, 28, 27, 29],
    #     [40, 47, 49, 40, 33, 29, 32, 43],
    #     [42, 49, 50, 39, 34, 30, 32, 46],
    #     [40, 47, 46, 35, 31, 32, 35, 43],
    #     [38, 43, 42, 31, 27, 27, 28, 33],
    #     [39, 33, 25, 17, 14, 15, 19, 26],
    #     [29, 16,  6,  1, -4,  0,  7, 18]
    # ]
   #  _pixels_arr = test_case
    # _test_arr = np.zeros((8, 8), dtype=np.float64)
    # for i in range(8):
    #     for j in range(8):
    #         tmp = 0
    #         for x in range(8):
    #             for y in range(8):
    #                 tmp +=

    return np.round(np.dot(matrix_of_dct, np.dot(_pixels_arr, transposed_matrix_of_dct))).astype(int)


def inv_discrete_cosine_transform(_pixel_arr):
    return np.round(np.dot(np.dot(transposed_matrix_of_dct, _pixel_arr), matrix_of_dct)).astype(int)


def quantization(_pixel_arr, __matrix_of_quantization=matrix_of_quantization_for_y):
    return np.round(_pixel_arr / __matrix_of_quantization).astype(int)


def inv_quantization(_pixel_arr, __matrix_of_quantization=matrix_of_quantization_for_c):
    return np.round(_pixel_arr * __matrix_of_quantization).astype(int)


def RLE(_pixel_arr):
    message = [str(int(_pixel_arr[i // 8][i % 8])) for i in zigzag_way]
    encoded_string = []
    i = 0
    while (i <= len(message) - 1):
        count = 1
        ch = message[i]
        j = i
        while (j < len(message) - 1):
            if (message[j] == message[j + 1]):
                count = count + 1
                j = j + 1
            else:
                break
        encoded_string.append((count, int(ch)))
        i = j + 1
    return encoded_string


def inv_RLE(_rle_array):
    rle_elements = []
    for i, j in _rle_array:
        for k in range(i):
            rle_elements.append(j)
    matrix_peace = np.zeros((8, 8), dtype=int)
    for i in range(64):
        matrix_peace[zigzag_way[i] // 8][zigzag_way[i] % 8] = rle_elements[i]
    return matrix_peace


def divide_on_blocks(_pixel_array, size):
    blocks = []
    img_w, img_h = size[0], size[1]
    for i in range(0, img_w, 8):
        for j in range(0, img_h, 8):
            blocks.append(_pixel_array[i:i+8][j:j+8])
    return blocks


def encode_jpeg(quality_factor, path_to_image, out='filename.myjpeg'):
    init_matrix_of_q(_quality_factor=quality_factor)
    print(matrix_of_quantization)
    # main_image = Image.open(path_to_image).convert('RGB')
    # _pixel_array = np.asarray(main_image)
    # _fixed_pixel_array = fix_image_size_for_jpeg(
    #     _pixel_array, (main_image.size)[::-1])
    # _blocks = divide_on_blocks(_fixed_pixel_array, (len(
    #     _fixed_pixel_array), len(_fixed_pixel_array[0])))
    # Y = [block[:, :, 0] for block in _blocks]
    # Cb = [block[:, :, 1] for block in _blocks]
    # Cr = [block[:, :, 2] for block in _blocks]
    # # print(Y)
    # # print(Cr)
    # # print(Cb)
    # # print(_blocks)
    # try:
    #     Y_dct = [discrete_cosine_transform(_Y) for _Y in Y]
    #     Cb_dct = [discrete_cosine_transform(_Cb) for _Cb in Cb]
    #     Cr_dct = [discrete_cosine_transform(_Cr) for _Cr in Cr]
    # except:
    #     print(len(Y_dct[-1]))
    # # print(Y_dct)
    # # print(Cr_dct)
    # # print(Cb_dct)
    # Y_quan = [quantization(_Y) for _Y in Y_dct]
    # Cb_quan = [quantization(
    #     _Cb, __matrix_of_quantization=matrix_of_quantization_for_c) for _Cb in Cb_dct]
    # Cr_quan = [quantization(
    #     _Cr, __matrix_of_quantization=matrix_of_quantization_for_c) for _Cr in Cr_dct]
    # # print(Y_quan)
    # # print(Cr_quan)
    # # print(Cb_quan)
    # Y_rle = [RLE(_Y) for _Y in Y_quan]
    # Cb_rle = [RLE(_Cb) for _Cb in Cb_quan]
    # Cr_rle = [RLE(_Cr) for _Cr in Cr_quan]
    # # print(Y_rle, Cr_rle, Cb_rle, file='kek.txt')
    # # with open('kek.txt', 'w') as file:
    # #     file.write(f"{Y_rle}\n{Cr_rle}\n{Cb_rle}")


if __name__ == '__main__':
    # print(matrix_of_dct)
    # print(discrete_cosine_transform([]))
    # print((test_eye * 5) / (test_eye * 5))
    # print(np.dot(inv_matrix_of_dct, matrix_of_dct))
    # print(inv_transposed_matrix_of_dct)

    pass
