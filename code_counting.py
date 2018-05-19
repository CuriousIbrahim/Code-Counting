import os

FILE_EXTENSIONS = ['.java', '.py', '.c', '.cpp', '.h', '.js']

files = []


def check_if_file_is_of_extension(file):

    for e in FILE_EXTENSIONS:
        if e in file:
            return True

    return False


def explore_folder(root):

    if not os.path.isdir(root) and check_if_file_is_of_extension(root):
        files.append(root)

    if os.path.isdir(root):

        for f in os.listdir(root):
            explore_folder(os.path.join(root, f))
