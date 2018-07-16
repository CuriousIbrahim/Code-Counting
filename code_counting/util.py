import logging
import os


def get_file_extension(file):
    file = file.split('.')

    extension = '.' + file[len(file)-1]

    return extension


def count_lines_of_code(file):
    count = 0

    with open(file, encoding='ISO-8859-1') as f:
        for line in f:
            count += 1

    logging.debug('{} contains {} lines of code'.format(file, count))

    return count


def explore_folder(root, files):

    if not os.path.isdir(root):
        # logging.info('\tAdd', root, 'to files list')
        files.append(root)

    if os.path.isdir(root):
        for f in os.listdir(root):
            explore_folder(os.path.join(root, f), files)

    return files
