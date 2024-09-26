import numpy as np
from pprint import pprint
from PIL import Image
from numpy import linalg

convertation_matrix_rgb2ycbcr = np.array([
    [0.299, 0.587, 0.114],
    [0.1687, -0.3313, 0.5],
    [0.5, -0.4187, -0.0813]
], dtype=np.float32)

convertation_matrix_ycbcr2rgb = np.array([
    
])

def fix_image_size_for_jpeg(_pixels_arr):
    pass


def convert_pixel_rgb2ycbcr(_pixel):
    pass


if __name__ == '__main__':
    print(linalg.inv(convertation_matrix_rgb2ycbcr))
