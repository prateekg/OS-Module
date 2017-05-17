#if top = "/"; it will delete all your memory in the disk
#os.path.join return a path from the dirpath to the name of the file or directory in the dirpath
#os.walk returns a 3-tuple (dirpath, dirnames, filenames) where [dirnames - list of subdirectories in dirpath] and [filenames - list of names of non-directory filenames in dirpath]
#os.unlink(path) is similar function to os.remove(path) which deletes(removes) the file path
#os.rmdir(path) removes(deletes) the directory path. "Raise OSError if directory is non-empty"
#os.removedirs(path) removes the directories recursively. "Raise OSError if directory is non-empty"

import os
for root, dirs, files in os.walk(top, topdown=False):
    for name in files:
        os.remove(os.path.join(root, name))
    for name in dirs:
        os.rmdir(os.path.join(root, name))
