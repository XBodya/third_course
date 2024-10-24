import unittest
import tools
from PIL import Image
import numpy as np


def is_clr(color):
    return 0 <= color <= 255


class ConvertationTest():
    def test_rgb2ycbcr(self):
        for i in range(256):
            for j in range(256):
                for k in range(256):
                    res = tools.convert_pixel_rgb2ycbcr((i, j, k))
                    self.assertTrue(is_clr(res[0]) and is_clr(
                        res[1]) and is_clr(res[2]))
                    inv = tools.convert_pixel_ycbcr2rgb(res)
                    self.assertTrue(is_clr(inv[0]) and is_clr(
                        inv[1]) and is_clr(inv[2]))
                    # self.assertEqual(inv[0], i)
                    # self.assertEqual(inv[1], j)
                    # self.assertEqual(inv[2], k)


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


class DctTest(unittest.TestCase):
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


if __name__ == '__main__':
    # unittest.main()
    # DctTest().dct_test1()
    DctTest().main()
