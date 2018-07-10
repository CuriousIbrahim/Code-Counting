import os
import time
import sys
from lang_controller import LanguagesController
import logging

files = []


def explore_folder(root):

    if not os.path.isdir(root):
        logging.info('\tAdd', root, 'to files list')
        files.append(root)

    if os.path.isdir(root):

        for f in os.listdir(root):
            explore_folder(os.path.join(root, f))

    return files


def main(root):
    logging.info('Constructing LanguageController object')
    controller = LanguagesController()
    logging.info('Successfully constructed LanguageController object')

    start = time.time()

    logging.info('Exploring', root, ':')
    explore_folder(root)
    logging.info('Exploring finished')

    for f in files:
        controller.check(f)

    print(controller.results())

    print('{} seconds to process {} lines of code across {} files with an average of {} lines of code per '
          'file'.format(str(time.time() - start), controller.total_lines(), controller.total_files(),
                        (controller.total_lines() / controller.total_files())))


if __name__ == '__main__':
    logging.info('Starting program!')
    root = sys.argv[1]
    main(root)