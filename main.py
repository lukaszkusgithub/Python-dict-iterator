import os
import shutil
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
import warnings
warnings.simplefilter("ignore")

_CURRENT_SYSTEM_NAME = os.name

_LOCAL_PATH = os.path.dirname(os.path.abspath('main.py'))

# Parse command line arguments
parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
parser.add_argument("-n", "--number", default="5",
                    help="Take every {number} frames from the folder")
parser.add_argument("-d", "--destination", default="newFrames",
                    help="Destination diretory to save frames")
if _CURRENT_SYSTEM_NAME == 'nt':
    parser.add_argument("-p", "--path", default="frames\\",
                        help="Path to folder with frames")
elif _CURRENT_SYSTEM_NAME == 'posix':
    parser.add_argument("-p", "--path", default="./frames/",
                        help="Path to folder with frames")
args = vars(parser.parse_args())

# Set up parameters
_NUMBER = int(args["number"])
_DIRECTORY = args["path"]
_NEW_DIRECTORY = os.path.join(_LOCAL_PATH, args["destination"])


def iterate_files():
    for index, filename in enumerate(os.listdir(_DIRECTORY)):
        file = os.path.join(_DIRECTORY, filename)
        if index % _NUMBER == 0:
            if os.path.isfile(file):
                shutil.copy(file, _NEW_DIRECTORY)


def create_new_directory():
    try:
        os.makedirs(_NEW_DIRECTORY, exist_ok=True)
        print("Directory '%s' created successfully" % _NEW_DIRECTORY)
    except OSError as error:
        print("Directory '%s' can not be created" % _NEW_DIRECTORY)



def main():
    create_new_directory()
    iterate_files()
    return 0


if __name__ == '__main__':
    main()
