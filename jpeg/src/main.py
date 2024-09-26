from PIL import Image
from funcs.tools import *

"""
in: *.png
out: *.jpeg

"""


def test(_pixels=None):
    pixels = [
        [(54, 54, 54), (232, 23, 93), (71, 71, 71), (168, 167, 167)],
        [(204, 82, 122), (54, 54, 54), (168, 167, 167), (232, 23, 93)],
        [(71, 71, 71), (168, 167, 167), (54, 54, 54), (204, 82, 122)],
        [(168, 167, 167), (204, 82, 122), (232, 23, 93), (54, 54, 54)]
    ]
    pixels = pixels if _pixels is None else _pixels
    # Convert the pixels into an array using numpy
    array = np.array(pixels, dtype=np.uint8)
    pprint(array)
    # new_image = Image.fromarray(array)
    # new_image.save('new.png')


def main(filename='test', typef='png'):
    try:
        img = Image.open(f"{filename}.{typef}")
    except FileNotFoundError:
        print(f"{filename}.{typef} file not found.")
        return
    rgb_array = img.convert("RGB").load()
    # test()
    yuv_img = save2image(convert_arr_rgb2yuv(
        img.size, rgb_array), _mode='YCbCr', _format='jpg')
    # rgb_img = save2image(convert_arr_yuv2rgb(
    #     yuv_img.size, yuv_img.load()), _mode='RGB', _format='png')
    # print(yuv_img.load())
    # convert_arr_yuv2rgb(yuv_img.size, yuv_img.load())


if __name__ == '__main__':
    main(filename='C:\\Users\\BOGDAN\\my_gits\\third_course\\jpeg\\src\\imgs\\test4')
