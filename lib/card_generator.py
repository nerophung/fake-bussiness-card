import os
import random
import numpy as np
import uuid
import imutils
from pascal_voc_writer import Writer
from collections import OrderedDict
from PIL import Image
from lib import IMAGE_PROVIDER
from lib.config import settings


class CardGenerator:

    def __init__(self):
        self.__image_provider = IMAGE_PROVIDER
        self.__background_options = settings.BACKGROUND_OPTIONS
        self.__log_dir = os.path.join(settings.LOG_DIR, 'images')
        self.__log_xml_dir = os.path.join(settings.LOG_DIR, 'xml')
        os.makedirs(self.__log_dir, exist_ok=True)
        os.makedirs(self.__log_xml_dir, exist_ok=True)

    def paste_image(self, card_image, list_images, writer_xml, xml_path):
        card_width, card_height = card_image.size
        padding_width, padding_height = int(0.1 * card_width), int(0.25 * card_height)
        field_images = list(list_images.items())
        random.shuffle(field_images)
        list_images = OrderedDict(field_images)
        for field_name in list_images:
            image = list_images[field_name]
            if field_name == 'name':
                image = imutils.resize(np.array(image), height=98)
            else:
                image = imutils.resize(np.array(image), height=32)
            height, width, _ = image.shape
            if width > 0.8 * card_width:
                image = imutils.resize(image, width=int(0.7 * card_width))
                height, width, _ = image.shape
            range_width = card_width - padding_width * 2 - width
            range_height = int(0.05 * card_height)
            print(field_name)
            print('card_width: ', card_width)
            print('padding_width: ', padding_width)
            print('width: ', width)
            list_x_min = [pos for pos in range(0, range_width)]
            list_y_min = [pos for pos in range(0, range_height)]
            x_min = padding_width + random.choice(list_x_min)
            y_min = padding_height + random.choice(list_y_min)
            pos = (x_min, y_min)
            image = Image.fromarray(image).convert('RGBA')
            card_image.paste(image, pos, image)
            writer_xml.addObject('text', x_min, y_min, x_min + width, y_min + height)
            padding_height = height + y_min
        writer_xml.save(xml_path)
        return card_image

    def get_images_by_color(self, list_image_paths, background_color):
        list_images = dict()

        for field_name in list_image_paths[background_color]:
            image = Image.open(random.choice(list_image_paths[background_color][field_name])).convert('RGBA')
            list_images[field_name] = image

        return list_images

    def generate_card(self, list_image_paths, vertical_card=False):

        image_name = str(uuid.uuid4())

        image_save_path = os.path.join(self.__log_dir, image_name + '.png')

        xml_path = os.path.join(self.__log_xml_dir, image_name + '.xml')

        background_color = random.choice(self.__background_options)

        card_image = self.__image_provider.get_background(
            background_color=background_color, vertical_card=vertical_card)

        width, height = card_image.size

        writer = Writer(image_save_path, width, height)

        list_images = self.get_images_by_color(list_image_paths, background_color)

        card_image = self.paste_image(card_image=card_image, list_images=list_images, writer_xml=writer, xml_path=xml_path)

        card_image.convert('RGBA').save(image_save_path, 'PNG')
