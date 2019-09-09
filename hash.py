# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from os import listdir, getcwd
from os.path import isfile, join, normpath, basename
import hashlib

#getting files from the current directory
def get_files():
    path = normpath(getcwd())
    print(path)
    return [join(path, f) for f in listdir(path) if isfile(join(path, f))]

#generating hashes for all the files
def get_hashes():
    files = get_files()
    list_of_hashes = []
    for each_file in files:
        hash = hashlib.md5()
        with open(each_file, "rb") as f:
            for block in iter(lambda: f.read(4096), b""):# Read and update hash in chunks/blocks of 4K(usefull for large files)
                hash.update(block)
        list_of_hashes.append('Filename: {}\tHash: {}\n'.format(basename(each_file), hash.hexdigest()))
        print(list_of_hashes)
    return list_of_hashes

#writing hashes to a hash_list
def write_hashes():
    hashes = get_hashes()
    with open('hash_list.txt', 'w') as f:
        for md5_hash in hashes:
            f.write(md5_hash)


if __name__ == '__main__':
    write_hashes()