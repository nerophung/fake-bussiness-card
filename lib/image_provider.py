import os
import random
import glob
from PIL import Image
from lib.config import settings


class ImageProvider:

    def __init__(self, list_fields):
        self.__list_fields = list_fields
        self.__background_dir = settings.BACKGROUND_DIR
        self.__image_dir = settings.IMAGE_DIR
        self.__image_fields = settings.IMAGE_FIELDS
        self.__image_colors = settings.IMAGE_COLOR

    def get_image_paths(self, number_records):
        list_image_paths = dict()
        for image_color in self.__image_colors:
            list_images = dict()
            for field_name in self.__image_fields:
                field_image_dir = os.path.join(self.__image_dir, image_color, field_name)
                image_names = glob.glob('{}/*/*/*.png'.format(field_image_dir))
                list_images[field_name] = random.choices(image_names, k=number_records)
            list_image_paths[image_color] = list_images
        return list_image_paths

    def get_background(self, background_color, vertical_card=False):
        background_dir_path = os.path.join(
            self.__background_dir, background_color)

        background_image_path = random.choice(os.listdir(background_dir_path))

        background_image = Image.open(os.path.join(
            background_dir_path, background_image_path))

        if vertical_card:
            background_image = background_image.rotate(random.choice([0, 90]), expand=True)

        background_image = background_image.convert('RGBA')

        return background_image
