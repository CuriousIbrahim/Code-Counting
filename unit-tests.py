import pytest
import os
from lang_controller import LanguagesController

CURRENT_PATH = os.path.dirname(os.path.realpath(__file__))

TEST_CODE_DIR = 'test-code/'

JAVA_FILE = os.path.join(TEST_CODE_DIR, 'Person.java')
PYTHON_FILE = os.path.join(TEST_CODE_DIR, 'Person.py')
HTML_FILE = os.path.join(TEST_CODE_DIR, 'test.html')
CSS_FILE = os.path.join(TEST_CODE_DIR, 'test.css')


def get_line_count(file, language_extension):
    lang_controller = LanguagesController()

    path = os.path.join(CURRENT_PATH, file)

    lang_controller.check(path)

    result = lang_controller.get_used_language(language_extension).lines_of_code

    return result


def test_java_line_count():

    assert get_line_count(JAVA_FILE, '.java') == 39


def test_python_line_count():

    assert get_line_count(PYTHON_FILE, '.py') == 16


def test_html_line_count():

    assert get_line_count(HTML_FILE, '.html') == 29


def test_css_line_count():

    assert get_line_count(CSS_FILE, '.css') == 9


