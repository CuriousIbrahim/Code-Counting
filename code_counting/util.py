import logging
import os


def get_file_extension(file):
    file = file.split('.')

    extension = '.' + file[len(file)-1]

    return extension


def count_lines_of_code(file):
    count = 0

    with open(file, encoding='ISO-8859-1') as f:
        for _ in f:
            count += 1

    logging.debug('{} contains {} lines of code'.format(file, count))

    return count


def explore_folder(root, files):

    # If root is not a folder, add it to the files list
    # Base case
    if not os.path.isdir(root):
        logging.debug('\tAdd {} to files list'.format(root))
        files.append(root)
        return files

    # If root is a folder, explore the folder and call itself (explore_folder function)
    # Recursive case
    elif os.path.isdir(root):
        logging.debug('\t{} is a dir, expanding:'.format(root))
        for f in os.listdir(root):
            logging.debug('\tExploring {}'.format(f))
            explore_folder(os.path.join(root, f), files)

        return files
