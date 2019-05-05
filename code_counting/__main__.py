import time
import sys
import logging
import os

# Yea, I don't know either. If I don't do it, python starts informing me that lang_controller is not a module
CURRENT_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

sys.path.append(CURRENT_PATH)

from code_counting.lang_controller import LanguagesController
from code_counting.util import explore_folder

# logging.getLogger().setLevel(logging.INFO)


def main(root):
    logging.debug('Constructing LanguageController object')
    controller = LanguagesController()
    logging.debug('Successfully constructed LanguageController object')

    start = time.time()

    logging.info('Exploring {}'.format(root))
    files = explore_folder(root, [])
    logging.info('Exploring finished')

    logging.info('Checking {} files'.format(len(files)))

    for f in files:
        controller.check(f)

    print('\n==============================================\n')

    print(controller.results())

    if controller.total_files() != 0:
        print('{} seconds to process {} lines of code across {} files with an average of {} lines of code per '
              'file'.format(round(time.time() - start, 3), controller.total_lines(), controller.total_files(),
                            (round(controller.total_lines() / controller.total_files(), 2))))
    else:
        print('{} seconds to process {} lines of code across {} files.'.format(round(time.time() - start, 3),
                                                                               controller.total_lines(),
                                                                               controller.total_files()))


if __name__ == '__main__':
    logging.info('Starting program!')

    root = ''

    debug = False

    root = sys.argv[1]

    try:
        if sys.argv[2] == '-d':
            debug = True
    except:
        None


    if debug:
        logging.basicConfig(filename='code-counting.log',
                            filemode='w', level=logging.DEBUG)
        logging.getLogger().debug('Debug mode ON')
    else:
        logging.getLogger().setLevel(logging.INFO)

    main(root)
