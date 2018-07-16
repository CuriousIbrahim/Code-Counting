import time
import sys
import logging

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

    print('{} seconds to process {} lines of code across {} files with an average of {} lines of code per '
          'file'.format(str(time.time() - start), controller.total_lines(), controller.total_files(),
                        (controller.total_lines() / controller.total_files())))


if __name__ == '__main__':
    logging.info('Starting program!')

    root = ''

    for index, item in enumerate(sys.argv[1:]):
        if index != (len(sys.argv) - 2):
            root += item + ' '
        else:
            root += item

    main(root)
