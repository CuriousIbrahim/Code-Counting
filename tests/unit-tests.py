import os
from code_counting.lang_controller import LanguagesController
from code_counting.util import explore_folder


CURRENT_PATH = os.path.dirname(os.path.realpath(__file__))

TEST_CODE_DIR = 'test-code/'

JAVA_FILE = os.path.join(TEST_CODE_DIR, 'Person.java')
PYTHON_FILE = os.path.join(TEST_CODE_DIR, 'Person.py')
HTML_FILE = os.path.join(TEST_CODE_DIR, 'test.html')
CSS_FILE = os.path.join(TEST_CODE_DIR, 'test.css')

JAVA_LINE_COUNT = 39
PYTHON_LINE_COUNT = 16
HTML_LINE_COUNT = 29
CSS_LINE_COUNT = 9

TEST_CODE_DIR_LINE_COUNT = JAVA_LINE_COUNT + PYTHON_LINE_COUNT + HTML_LINE_COUNT + CSS_LINE_COUNT


def get_line_count(file, language_extension):
    lang_controller = LanguagesController()

    path = os.path.join(CURRENT_PATH, file)

    lang_controller.check(path)

    result = lang_controller.get_used_language(language_extension).lines_of_code

    return result


def test_java_line_count():

    assert get_line_count(JAVA_FILE, '.java') == JAVA_LINE_COUNT


def test_python_line_count():

    assert get_line_count(PYTHON_FILE, '.py') == PYTHON_LINE_COUNT


def test_html_line_count():

    assert get_line_count(HTML_FILE, '.html') == HTML_LINE_COUNT


def test_css_line_count():

    assert get_line_count(CSS_FILE, '.css') == CSS_LINE_COUNT


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





