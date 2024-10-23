import unittest
import tools


def is_clr(color):
    return 0 <= color <= 255


class ConvertationTest(unittest.TestCase):
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


if __name__ == '__main__':
    unittest.main()
