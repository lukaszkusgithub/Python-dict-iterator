import os

_CURRENT_SYSTEM_NAME = os.name

_LOCAL_PATH = os.path.dirname(os.path.abspath('main.py'))

if _CURRENT_SYSTEM_NAME == 'nt':
    frames = os.path.join(_LOCAL_PATH, "frames\\")
    labels = os.path.join(_LOCAL_PATH, "labels\\")
elif _CURRENT_SYSTEM_NAME == 'posix':
    frames = os.path.join(_LOCAL_PATH, "frames/")
    labels = os.path.join(_LOCAL_PATH, "labels/")


def iterate_files():
    for file in os.listdir(frames):
        found = False
        file_path = os.path.join(frames, file)
        file_name = os.path.splitext(file)[0]
        for label_file in os.listdir(labels):
            label_file_name = os.path.splitext(label_file)[0]
            if label_file_name == file_name:
                found = True
        if not found:
            os.remove(file_path)


def main():
    iterate_files()
    return 0


if __name__ == '__main__':
    main()
