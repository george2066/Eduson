"""ОШИБКА В КОДЕ!!!"""


"""
Задача по ускорению работы программы с большими вычислительными нагрузками.

Для работы программы нужно изображение image.JPG, которое нужно разместить вместе с программой.
Любая фотография с телефона или интернета подойдет. Лучше использовать довольно большое изображение.

Попробуйте применить ProcessPoolExecutor для ускорения работы программы.
"""

from time import monotonic
from PIL import Image, ImageFilter  # pip install pillow
import os


def calc_new_size(original_size, target_max_size):
    original_width, original_height = original_size
    original_ratio = original_width / original_height  
    if original_width > original_height:
        new_width = target_max_size # 13
        new_height = int(new_width / original_ratio) # 4
    else:
        new_height = target_max_size[1] # 4
        new_width = int(new_height * original_ratio) # 6
    return new_width, new_height 


def process_image(image, target_max_size, target_path):
    image_size = image.size
    new_size = calc_new_size(image_size, target_max_size)
    resized_image_with_edges = image.resize(new_size).filter(ImageFilter.ModeFilter(5))  # cpu intensive
    file_name = f'resized_image_{target_max_size}.jpg'
    resized_image_with_edges.save(os.path.join(target_path, file_name))  # I/O task


if __name__ == '__main__':
    start = monotonic()

    image = Image.open('workbooks/python/projects/image.jpg')

    target_max_sizes = [500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500]

    target_path = os.path.join(os.getcwd(), 'resized_images')

    for target_max_size in target_max_sizes:
        process_image(image, target_max_size, target_path)

    duration = monotonic() - start
    print(f'It took {duration:0.2f} secs')