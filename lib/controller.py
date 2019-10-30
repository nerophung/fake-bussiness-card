from tqdm import tqdm
from lib.card_generator import CardGenerator
from lib import IMAGE_PROVIDER

class FBCController:

    def __init__(self):
        self.__card_generator = CardGenerator()
        self.__image_provider = IMAGE_PROVIDER

    def generate(self, number_of_records, num_of_images, vertical_card=False):
        list_image_paths = self.__image_provider.get_image_paths(number_records=number_of_records)
        for _ in tqdm(range(num_of_images)):
            self.__card_generator.generate_card(list_image_paths=list_image_paths, vertical_card=vertical_card)
