import time
import sys
import logging
import os

# Yea, I don't know either. If I don't do it, python starts informing me that lang_controller is not a module
CURRENT_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

sys.path.append(CURRENT_PATH)

from code_counting.lang_controller import LanguagesController
from code_counting.util import explore_folder


def main(root):
    logging.info('Constructing LanguageController object')
    controller = LanguagesController()
    logging.info('Successfully constructed LanguageController object')

    start = time.time()

    logging.info('Exploring', root, ':')
    files = explore_folder(root, [])
    logging.info('Exploring finished')

    for f in files:
        controller.check(f)

    print(controller.results())

    if controller.total_files() != 0:
        print('{} seconds to process {} lines of code across {} files with an average of {} lines of code per '
              'file'.format(str(time.time() - start), controller.total_lines(), controller.total_files(),
                            (controller.total_lines() / controller.total_files())))
    else:
        print('{} seconds to process {} lines of code across {} files.'.format(str(time.time() - start), controller.total_lines(), controller.total_files()))


if __name__ == '__main__':
    logging.info('Starting program!')

    root = ''

    for index, item in enumerate(sys.argv[1:]):
        if index != (len(sys.argv) - 2):
            root += item + ' '
        else:
            root += item

    main(root)
