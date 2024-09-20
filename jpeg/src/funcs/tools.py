import numpy as np
from pprint import pprint
from PIL import Image


def convert_arr_rgb2yuv(_img_size, _rgb_array):
    pprint(_rgb_array)
    RGB2YUV_KOEFF = np.array((
        (0.299, 0.5, 0.1687),
        (0.587, -0.4187, -0.3313),
        (0.114, -0.0813, 0.5)
    ))
    RGB2YUV_ADDIT = np.array((0, 128, 128))
    _yuv_array = [[]] * _img_size[0]
    for x in range(_img_size[0]):
        for y in range(_img_size[1]):
            _rgb_vector = np.array(_rgb_array[x, y], dtype=np.uint8)
            _yuv_array[x].append(tuple(np.array(
                np.dot(_rgb_vector, RGB2YUV_KOEFF) + RGB2YUV_ADDIT, dtype=np.uint8)))
    # pprint(_yuv_array)
    return _yuv_array


def subsampling(_yuv_array):
    pass


def save_from_arr2image(_arr):
    return Image.fromarray(_arr, mode='YCbCr')
