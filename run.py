import argparse
from lib.controller import FBCController

parser = argparse.ArgumentParser()
parser.add_argument('--number_of_records', type=int, required=True)
parser.add_argument('--number_of_images', type=int, required=True)
parser.add_argument('--vertical_card', type=bool, default=False)

if __name__ == '__main__':
    args = parser.parse_args()
    num_of_records = args.number_of_records
    num_of_images = args.number_of_images
    vertical_card = args.vertical_card
    controller = FBCController()
    controller.generate(number_of_records=num_of_records, num_of_images=num_of_images, vertical_card=vertical_card)