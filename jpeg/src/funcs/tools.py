import numpy as np
from pprint import pprint
from PIL import Image
from numpy import linalg
from typing import Tuple, List
from math import pi
from my_consts import *
import itertools


def init_matrix_of_q(_quality_factor):
    for i in range(8):
        for j in range(8):
            matrix_of_quantization[i][j] = 1 + (i * j) * _quality_factor
    print(matrix_of_quantization)


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

# *  JPEG/JFIF YCbCr conversions

#      Y  = R *  0.29900 + G *  0.58700 + B *  0.11400
#      Cb = R * -0.16874 + G * -0.33126 + B *  0.50000 + 128
#      Cr = R *  0.50000 + G * -0.41869 + B * -0.08131 + 128


# def convert_pixel_rgb2ycbcr(_pixel_rgb: Tuple[int, int, int]) -> Tuple[int, int, int]:
#     # return np.dot(_pixel_rgb, convertation_matrix_rgb2ycbcr) + convertation_vector_rgb2ycbcr
#     return (int(np.float64(0.29900) * _pixel_rgb[0] + np.float64(0.58700) * _pixel_rgb[1] + np.float64(0.11400) * _pixel_rgb[2]),
#             int(128 + np.float64(-0.16874) *
#                 _pixel_rgb[0] - np.float64(0.33126) * _pixel_rgb[1] + np.float64(0.50000) * _pixel_rgb[2]),
#             int(128 + np.float64(0.50000) * _pixel_rgb[0] - np.float64(0.41869) * _pixel_rgb[1] - np.float64(0.08131) * _pixel_rgb[2]))


# def convert_pixel_ycbcr2rgb(_pixel_ycbcr: Tuple[int, int, int]) -> Tuple[int, int, int]:
#     # return np.dot((_pixel_ycbcr - convertation_vector_rgb2ycbcr), convertation_matrix_ycbcr2rgb)
#     return (
#         round(_pixel_ycbcr[0] + 1.402 * (_pixel_ycbcr[2] - 128)),
#         round(_pixel_ycbcr[0] - 0.344136 *
#               (_pixel_ycbcr[1] - 128) - 0.714136 * (_pixel_ycbcr[2] - 128)),
#         round(_pixel_ycbcr[0] + 1.772 * (_pixel_ycbcr[1] - 128))
#     )


def matrix_convert_pixel_rgb2ycbcr(_pixel_rgb: Tuple[int, int, int]) -> Tuple[int, int, int]:
    # return np.dot(_pixel_rgb, convertation_matrix_rgb2ycbcr) + convertation_vector_rgb2ycbcr
    return np.round((np.dot(_pixel_rgb, convertation_matrix_rgb2ycbcr) + convertation_vector)[0]).astype(int)


def matrix_convert_pixel_ycbcr2rgb(_pixel_ycbcr: Tuple[int, int, int]) -> Tuple[int, int, int]:
    # return np.dot((_pixel_ycbcr - convertation_vector_rgb2ycbcr), convertation_matrix_ycbcr2rgb)
    return np.round(np.dot((_pixel_ycbcr - convertation_vector), convertation_matrix_ycbcr2rgb)[0]).astype(int)


def subsampling(array_color_channel):
    for i in range(0, len(array_color_channel), 2):
        for j in range(0, len(array_color_channel[0]), 2):
            average_color = array_color_channel[i][j]
            average_color += array_color_channel[i + 1][j]
            average_color += array_color_channel[i][j + 1]
            average_color += array_color_channel[i + 1][j + 1]
            average_color = round(average_color / 4)
            # array_color_channel[i][j] = average_color
            # array_color_channel[i + 1][j] = average_color
            # array_color_channel[i][j + 1] = average_color
            # array_color_channel[i + 1][j + 1] = average_color

            print(f"BLOCK, avg:{average_color}")
            print(array_color_channel[i][j],
                  array_color_channel[i][j + 1])
            print(array_color_channel[i + 1][j],
                  array_color_channel[i + 1][j + 1])

            array_color_channel[i][j] = average_color
            array_color_channel[i + 1][j] = average_color
            array_color_channel[i][j + 1] = average_color
            array_color_channel[i + 1][j + 1] = average_color


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


def quantization(_pixel_arr):
    return np.round(_pixel_arr / matrix_of_quantization).astype(int)


def inv_quantization(_pixel_arr):
    return np.round(_pixel_arr * matrix_of_quantization).astype(int)


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


def save_image_fromarray(parray, filename):
    image_plot = np.array(parray, dtype=np.uint8)
    new_image = Image.fromarray(image_plot)
    new_image.save(filename)


def fix_pixel(pixel: Tuple[int, int, int]) -> Tuple[int, int, int]:
    return (max(min(pixel[0], 255), 0), max(min(pixel[1], 255), 0), max(min(pixel[2], 255), 0))


def combine_color_channels(first, second, third):
    image_plot = np.zeros((first.shape[0], first.shape[1], 3))
    for i in range(first.shape[0]):
        for j in range(first.shape[1]):
            image_plot[i][j] = np.array(
                (first[i][j], second[i][j], third[i][j]), dtype=np.uint8)
    return image_plot


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
    print(convertation_matrix_ycbcr2rgb)
    print(convertation_matrix_rgb2ycbcr)
    print(linalg.inv(convertation_matrix_ycbcr2rgb))
    # print(convert_pixel_rgb2ycbcr((0, 20, 100)))
