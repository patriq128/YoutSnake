import os
import hashlib
import random

def file_hash(path):
    hasher = hashlib.md5()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            hasher.update(chunk)
    return hasher.hexdigest()

def remove_duplicates(folder):
    hashes = {}
    for root, _, files in os.walk(folder):
        for file in files:
            path = os.path.join(root, file)
            h = file_hash(path)
            if h in hashes:
                to_delete = random.choice([hashes[h], path])
                to_keep = path if to_delete == hashes[h] else hashes[h]
                os.remove(to_delete)
                print(f"Deleted: {to_delete}")
                print(f"Kept: {to_keep}")
                hashes[h] = to_keep
            else:
                hashes[h] = path

folder = input("Enter the path to the folder: ")
remove_duplicates(folder)
