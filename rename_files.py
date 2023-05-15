import os
import shutil
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
import warnings

warnings.simplefilter("ignore")

_CURRENT_SYSTEM_NAME = os.name

_LOCAL_PATH = os.path.dirname(os.path.abspath('main.py'))

_CLASS_ID = {'rock': 0, 'tree': 1, 'car_parts': 2, 'car_wheel': 3, 'snow': 4,
             'bird': 5}

if _CURRENT_SYSTEM_NAME == 'nt':
    _FRAMES_PATH = os.path.join(_LOCAL_PATH, "Frames\\")
    _LABELS_PATH = os.path.join(_LOCAL_PATH, "Labels\\")
elif _CURRENT_SYSTEM_NAME == 'posix':
    _FRAMES_PATH = os.path.join(_LOCAL_PATH, "Frames/")
    _LABELS_PATH = os.path.join(_LOCAL_PATH, "Labels/")

# Parse command line arguments
parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
parser.add_argument("-c", "--category", default="0",
                    help="Category from 0 to 5")
parser.add_argument("-i", "--index", default="1",
                    help="Index")
args = vars(parser.parse_args())

_CATEGORY = int(args["category"])
_INDEX_ARG = int(args["index"])

_DESTINATION_FRAMES_PATH = os.path.join(_LOCAL_PATH, 'newFrames')
_DESTINATION_LABELS_PATH = os.path.join(_LOCAL_PATH, 'newLabels')


def iterate_files():
    file_index = _INDEX_ARG
    for file in os.listdir(_FRAMES_PATH):
        frame_file_path = os.path.join(_FRAMES_PATH, file)
        frame_file_name = os.path.splitext(file)[0]
        frame_file_extension = os.path.splitext(file)[1]
        # TODO: implement search algorithm
        for label_file in os.listdir(_LABELS_PATH):
            label_file_path = os.path.join(_LABELS_PATH, label_file)
            label_file_name = os.path.splitext(label_file)[0]
            label_file_extension = os.path.splitext(label_file)[1]
            if label_file_name == frame_file_name:
                try:
                    category_name = list(_CLASS_ID.keys())[
                        list(_CLASS_ID.values()).index(_CATEGORY)]
                except:
                    print("Wrong category")

                frame_new_name = '{}_{}{}'.format(file_index, category_name,
                                                  frame_file_extension)
                label_new_name = '{}_{}{}'.format(file_index, category_name,
                                                  label_file_extension)

                label_new_path = os.path.join(_DESTINATION_LABELS_PATH,
                                              label_new_name)
                frame_new_path = os.path.join(_DESTINATION_FRAMES_PATH,
                                              frame_new_name)

                shutil.copy(frame_file_path, frame_new_path)
                shutil.copy(label_file_path, label_new_path)

                file_index += 1


def create_new_directory():
    try:
        os.makedirs(_DESTINATION_FRAMES_PATH, exist_ok=True)
        os.makedirs(_DESTINATION_LABELS_PATH, exist_ok=True)
        print("Directory created successfully")
    except OSError as error:
        print("Directory can not be created")


def main():
    create_new_directory()
    iterate_files()
    return 0


if __name__ == '__main__':
    main()
