import os

from .constants import CURRENT_PATH, TEST_CODE_DIR, TEST_CODE_DIR_LINE_COUNT

from code_counting.lang_controller import LanguagesController
from code_counting.util import explore_folder


# Get line count for the entire test-code/ dir
def test_the_test_code_dir_line_count():
    print(CURRENT_PATH)

    lang_controller = LanguagesController()

    files = explore_folder(os.path.join(CURRENT_PATH, TEST_CODE_DIR), [])

    for file in files:
        lang_controller.check(file)

    assert lang_controller.total_lines() == TEST_CODE_DIR_LINE_COUNT


def test_the_test_code_dir_file_count():
    lang_controller = LanguagesController()

    print(os.path.join(CURRENT_PATH, TEST_CODE_DIR))

    files = explore_folder(os.path.join(CURRENT_PATH, TEST_CODE_DIR), [])

    for file in files:
        lang_controller.check(file)

    assert lang_controller.total_files() == 4
