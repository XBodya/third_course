import numpy as np
from pprint import pprint
from PIL import Image
from numpy import linalg


def convert_arr_rgb2yuv(_img_size, _rgb_array):
    RGB2YUV_KOEFF = np.array([
        (0.299, 0.5, 0.1687),
        (0.587, -0.4187, -0.3313),
        (0.114, -0.0813, 0.5)
    ])
    RGB2YUV_ADDIT = np.array((0, 128, 128), dtype=np.int32)
    _yuv_array = []
    for x in range(_img_size[1]):
        _yuv_array.append([])
        for y in range(_img_size[0]):
            _rgb_vector = np.array(_rgb_array[y, x], dtype=np.uint8)
            # print(_rgb_vector)
            _yuv_array[x].append(
                list(np.dot(_rgb_vector, RGB2YUV_KOEFF) + RGB2YUV_ADDIT))
    _yuv_array = np.array(_yuv_array, dtype=np.uint8)
    # print(_yuv_array)
    return _yuv_array


def convert_arr_yuv2rgb(_img_size, _yuv_array):
    YUV2RGB_KOEFF = np.array([
        (1, 0, 1.402),
        (1, -0.34414, -0.71414),
        (1, 1.772, 0)
    ]).T
    print(YUV2RGB_KOEFF)
    YUV2RGB_ADDIT = np.array((0, 128, 128), dtype=np.uint8)
    print(YUV2RGB_ADDIT - (0, 0, 0))
    return
    _rgb_array = []
    for x in range(_img_size[1]):
        _rgb_array.append([])
        for y in range(_img_size[0]):
            _yuv_vector = np.array(_yuv_array[y, x], dtype=np.uint8)
            _rgb_array[x].append(
                list(np.dot(YUV2RGB_KOEFF, (_yuv_vector - YUV2RGB_ADDIT))))
    _rgb_array = np.array(_rgb_array, dtype=np.uint8)
    pprint(_rgb_array)
    return _rgb_array


def subsampling(_yuv_array):
    pass


def save2image(_arr, _mode='RGB', _format='png'):
    _image = Image.fromarray(_arr, mode=_mode)
    _image.save(f'new{_mode}.{_format}')
    return _image


def test(rgb_vector):
    RGB2YUV_KOEFF = [
        [0.299, 0.587, 0.114],
        [0.1687, -0.3313, 0.5],
        [0.5, -0.4187, -0.0813]

    ]
    RGB2YUV_ADDIT = [
        [0],
        [128],
        [128]
    ]
    ycrcbK = [
        [1, 0, 1.402],
        [1, -0.34414, -0.71414],
        [1, 1.772, 0]
    ]
    print(linalg.inv(RGB2YUV_KOEFF))
    print(rgb_vector)
    print(np.dot(RGB2YUV_KOEFF, rgb_vector) + RGB2YUV_ADDIT)
    ycrcb_vector = np.dot(RGB2YUV_KOEFF, rgb_vector) + RGB2YUV_ADDIT
    print(np.dot(ycrcbK, (ycrcb_vector - RGB2YUV_ADDIT)))
    print(np.dot(linalg.inv(RGB2YUV_KOEFF), (ycrcb_vector - RGB2YUV_ADDIT)))


if __name__ == '__main__':
    a = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ]
    b = [
        [255], [255], [100]
    ]
    test(b)
