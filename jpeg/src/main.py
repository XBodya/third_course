from PIL import Image
from funcs.tools import *

"""
in: *.png
out: *.jpeg

"""


def test():
    pixels = [
        [(54, 54, 54), (232, 23, 93), (71, 71, 71), (168, 167, 167)],
        [(204, 82, 122), (54, 54, 54), (168, 167, 167), (232, 23, 93)],
        [(71, 71, 71), (168, 167, 167), (54, 54, 54), (204, 82, 122)],
        [(168, 167, 167), (204, 82, 122), (232, 23, 93), (54, 54, 54)]
    ]

    # Convert the pixels into an array using numpy
    array = np.array(pixels, dtype=np.uint8)
    pprint(array)
    new_image = Image.fromarray(array)
    new_image.save('new.png')


def main(filename='test', typef='png'):
    try:
        img = Image.open(f"{filename}.{typef}")
    except FileNotFoundError:
        print(f"{filename}.{typef} file not found.")
        return
    rgb_array = img.convert("RGB").load()
    test()
    # new_img = save_from_arr2image(convert_arr_rgb2yuv(img.size, rgb_array))
    # new_img.save("MYIMAGE.jpg")


if __name__ == '__main__':
    main(filename='C:\\Users\\BOGDAN\my_gits\\third_course\\jpeg\\src\\imgs\\test2')
