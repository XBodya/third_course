import unittest
import tools
from PIL import Image
import numpy as np


def is_clr(color):
    return 0 <= color <= 255


def is_pixel(vector):
    return is_clr(vector[0]) and is_clr(vector[1]) and is_clr(vector[2])


class ConvertationTest():
    def test_rgb2ycbcr(self):
        for i in range(256):
            for j in range(256):
                for k in range(256):
                    rgb = (i, j, k)
                    ycbcr1 = tools.matrix_convert_pixel_rgb2ycbcr(rgb)
                    # ycbcr1 = tools.convert_pixel_rgb2ycbcr(rgb)
                    # self.assertTrue(is_pixel(ycbcr1))
                    inv_rgb = tools.matrix_convert_pixel_ycbcr2rgb(ycbcr1)

                    print(
                        f"(r, g, b):{rgb} -> (y, cb, cr): {ycbcr1} -> (r, g, b): {inv_rgb}")

    def test_ycbcr2rgb(self):
        for i in range(256):
            for j in range(256):
                for k in range(256):
                    rgb = (i, j, k)
                    ycbcr = tools.convert_pixel_rgb2ycbcr(rgb)
                    _rgb = tools.convert_pixel_ycbcr2rgb(ycbcr)
                    # self.assertEqual(rgb, _rgb)


_test_case = [
    [140, 144, 147, 140, 140, 155, 179, 175],
    [144, 152, 140, 147, 140, 148, 167, 179],
    [152, 155, 136, 167, 163, 162, 152, 172],
    [168, 145, 156, 160, 152, 155, 136, 160],
    [162, 148, 156, 148, 140, 136, 147, 162],
    [147, 167, 140, 155, 155, 140, 136, 162],
    [136, 156, 123, 167, 162, 144, 140, 147],
    [148, 155, 136, 155, 152, 147, 147, 136]
]


class DctTest():
    def dct_test1(self):
        www = tools.discrete_cosine_transform(_test_case)
        print(www)
        yyy = tools.quantization(www)
        yyy1 = tools.inv_quantization(yyy)
        print(yyy)
        print(yyy1)
        # qqq = tools.RLE(yyy)
        # print(qqq)
        # print(tools.inv_RLE(qqq))
        www1 = tools.inv_discrete_cosine_transform(www)
        print(www1)

    def main(self):
        img = Image.open('jpeg\\src\\imgs\\test2.png').convert('RGB')
        arr = np.asarray(img)
        # print(arr)
        # print(len(arr), len(arr[0]))
        # print(img.size)
        new_arr = tools.fix_image_size_for_jpeg(arr, (img.size)[::-1])
        # print(new_arr)
        new_img = Image.fromarray(new_arr.astype(np.uint8))
        # print(new_arr)
        new_img.save('my_image.png')
        # print(len(new_arr), len(new_arr[0]))
        blocks = tools.divide_on_blocks(
            new_arr, (len(new_arr), len(new_arr[0])))
        print(len(blocks))
        # print(blocks)

    def test_encode(self):
        tools.encode_jpeg('.\\jpeg\\src\\imgs\\test2.png')


class QuantizationTC(unittest.TestCase):
    def test1(self):
        tools.encode_jpeg(1, "")
        print(tools.matrix_of_quantization)


class MyTests():
    def __init__(self, filename):
        # self.test_convertation_rgb_ycbcr_rgb(filename)
        # test_case = [[i for j in range(8)] for i in range(8)]
        # self.test_subsampling(test_case)
        self.test_combine_color_channels()
        # self.test_subsampling_on_image()

    def test_convertation_rgb_ycbcr_rgb(self, filename):
        current_image = Image.open(filename).convert("RGB")
        image_plot = np.asarray(current_image)
        image_shape = image_plot.shape
        new_image_plot = np.zeros(image_shape)
        for y_i in range(image_shape[0]):
            for x_i in range(image_shape[1]):
                ycbcr = tools.matrix_convert_pixel_rgb2ycbcr(
                    image_plot[y_i][x_i])
                new_rgb = tools.matrix_convert_pixel_ycbcr2rgb(ycbcr)
                new_image_plot[y_i][x_i] = tools.fix_pixel(new_rgb)
                # print(1 if tuple(new_image_plot[y_i][x_i]) != tuple(
                #     image_plot[y_i][x_i]) else 0)
        tools.save_image_fromarray(
            new_image_plot, f"jpeg_results\\convtest{filename}")

    def test_subsampling(self, test_array):
        print("TEST SUBSAMPLING")
        print("BEFORE")
        print(np.array(test_array))
        print("AFTER")
        tools.subsampling(test_array)
        print(np.array(test_array))

    def test_combine_color_channels(self):
        y = np.array([
            [0, 1, 2]
        ])
        cb = [
            [12, 125, 25]
        ]
        cr = [
            [35, 241, 12]
        ]
        print(tools.combine_color_channels(y, cb, cr))

    def test_subsampling_on_image(filename):
        pass


if __name__ == '__main__':
    # unittest.main()
    # DctTest().dct_test1()
    # DctTest().test_encode()
    # ConvertationTest().test_rgb2ycbcr()
    MyTests("my_image.png")
