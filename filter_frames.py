import os

_CURRENT_SYSTEM_NAME = os.name

_LOCAL_PATH = os.path.dirname(os.path.abspath('main.py'))

if _CURRENT_SYSTEM_NAME == 'nt':
    _FRAMES_PATH = os.path.join(_LOCAL_PATH, "Frames\\")
    _LABELS_PATH = os.path.join(_LOCAL_PATH, "Labels\\")
elif _CURRENT_SYSTEM_NAME == 'posix':
    _FRAMES_PATH = os.path.join(_LOCAL_PATH, "Frames/")
    _LABELS_PATH = os.path.join(_LOCAL_PATH, "Labels/")


def filter_files():
    for file in os.listdir(_FRAMES_PATH):
        found = False
        file_path = os.path.join(_FRAMES_PATH, file)
        file_name = os.path.splitext(file)[0]
        for label_file in os.listdir(_LABELS_PATH):
            label_file_name = os.path.splitext(label_file)[0]
            if label_file_name == file_name:
                found = True
                break
        if not found:
            os.remove(file_path)


def main():
    filter_files()
    return 0


if __name__ == '__main__':
    main()
