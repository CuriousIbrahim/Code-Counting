import os
import time
import sys

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

    return files


def count_lines_of_code(file):
    count = 0

    with open(file, encoding='ISO-8859-1') as f:
        for line in file:
            count += 1

    return count


def main(root):
    start = time.time()

    explore_folder(root)

    total = 0

    for f in files:
        total += count_lines_of_code(f)

    print('There are {} lines of code in {} files. This took {} to process'.format(
        total, len(files), time.time() - start
    ))


if __name__ == '__main__':
    root = sys.argv[1]
    main(root)
