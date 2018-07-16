from .constants import *

from code_counting.lang_controller import LanguagesController


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
