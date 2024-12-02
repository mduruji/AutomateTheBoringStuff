"""
Selective Copy
Write a program that walks through a folder tree and searches for files with a certain file
extension (such as .pdf or .jpg).
Copy these files from whatever location they are in to a new folder.
"""

from pathlib import Path as path
import shutil
import os
import fnmatch

p = path('/Users/Michael/downloads')


def selective_copy(filepath):
    for folders, subfolders, filenames in os.walk(filepath):
        pattern = "*.pdf"
        destination = filepath / "tmp"
        if not destination.is_dir():
            os.mkdir(destination)

        for filename in filenames:
            if fnmatch.fnmatch(filename, pattern):
                if not (destination/filename).is_file():
                    shutil.copy(filepath/filename, destination)
                    print(f"{filename} has been successfully moved to {destination}")


selective_copy(p)
