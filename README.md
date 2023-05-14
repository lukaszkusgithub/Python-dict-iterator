# Python-dict-iterator
 A simple program to take every x files from a folder and copy them to a new folder, filter folders and rename files.

## Usage to take every x files from a folder
```
python main.py
```

## Arguments
### Changing the file storage path
```
python main.py -d folderName
```
or
```
python main.py --destination folderName
```
### Changing the path from where the iterated files are located
```
python main.py -p folderName
```
or
```
python main.py --path folderName
```
### Change the number with which each file of the video will be taken
```
python main.py -n Integer
```
or
```
python main.py --number Integer
```
## Default settings
The program takes every 5th file from the frames folder and saves it in the newFrames folder
```
number = 5
path = "frames"
destination  = "newFrames"
```
## Example of usage
```
python main.py -p files -d newFiles -n 5
```

## Using a file renaming program
```
python rename_files.py
```

## Arguments
### Changing the category
```
python rename_files.py -c categryIndex
```
or
```
python rename_files.py --category categryIndex
```
### Changing the index
```
python rename_files.py -i Integer
```
or
```
python rename_files.py --index Integer
```
## Default settings
```
category = 1
index  = 1
```
## Example of usage
```
python rename_files.py -c 3 -i 1
```

## Using file filtering
```
python filter_frames.py
```
