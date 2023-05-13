# Python-dict-iterator
 A simple program to take every x files from a folder and copy them to a new folder

## Usage
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
### changing the path from where the iterated files are located
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
