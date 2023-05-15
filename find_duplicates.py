# Importing Libraries
import os
import hashlib
from filecmp import cmp
import argparse
import os
import hashlib
from collections import defaultdict
from pathlib import Path
from typing import Iterator, Iterable, NamedTuple

CHUNK_SIZE = 4 * 1024 * 1024

_CURRENT_SYSTEM_NAME = os.name

_LOCAL_PATH = os.path.dirname(os.path.abspath('main.py'))

if _CURRENT_SYSTEM_NAME == 'nt':
    _FRAMES_PATH = os.path.join(_LOCAL_PATH, "Frames\\")
    _LABELS_PATH = os.path.join(_LOCAL_PATH, "Labels\\")
elif _CURRENT_SYSTEM_NAME == 'posix':
    _FRAMES_PATH = os.path.join(_LOCAL_PATH, "Frames/")
    _LABELS_PATH = os.path.join(_LOCAL_PATH, "Labels/")


class HashedFile(NamedTuple):
    size: int
    path: Path
    md5_hash: bytes

    def __str__(self) -> str:
        return str(self.path)

    @classmethod
    def load(cls, root: Path, name: str) -> 'HashedFile':
        path = root / name

        md5_hash = hashlib.md5()
        with path.open('rb') as f:
            for chunk in iter(lambda: f.read(CHUNK_SIZE), b''):
                md5_hash.update(chunk)

        return cls(path.stat().st_size, path, md5_hash.digest())


def file_listing(directory: str) -> Iterator[HashedFile]:
    for root, dirs, files in os.walk(directory):
        root_path = Path(root)
        for name in files:
            yield HashedFile.load(root_path, name)


def find_duplicates(files: Iterable[HashedFile]) -> Iterator[list[HashedFile]]:
    duplicates = defaultdict(list)
    for file in files:
        duplicates[file.size, file.md5_hash].append(file)

    for (size, md5_hash), dupe_files in duplicates.items():
        if len(dupe_files) > 1:
            print(f'Size: {size} bytes, MD5: {md5_hash.hex()}')
            for i, file in enumerate(dupe_files, 1):
                print(f'{i:4}. {file}')
            yield dupe_files


def delete_duplicates(duplicate_groups: Iterable[list[HashedFile]]) -> Iterator[int]:
    for files in duplicate_groups:
        for file in files:
            print(f'   Deleting {file}')
            file.path.unlink()
            yield file.size


def main() -> None:
    # directory = file_listing(_FRAMES_PATH)
    directory = file_listing(_LABELS_PATH)

    duplicates = find_duplicates(directory)

    bytes_removed = sum(delete_duplicates(duplicates))
    print(f'\nTotal freed up space: {bytes_removed} bytes')



if __name__ == '__main__':
    main()