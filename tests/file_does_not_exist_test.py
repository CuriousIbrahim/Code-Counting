import os

from .constants import CURRENT_PATH

from code_counting.lang_controller import LanguagesController


def test_a_file_that_does_not_exist():
    lang_controller = LanguagesController()

    path = os.path.join(CURRENT_PATH, 'does_not_exist.java')

    lang_controller.check(path)

    result = lang_controller.get_used_language('java')

    assert result is None


def test_a_file_does_not_exist_line_count():
    lang_controller = LanguagesController()

    path = os.path.join(CURRENT_PATH, 'does_not_exist.java')

    lang_controller.check(path)

    assert lang_controller.total_lines() == 0


def test_a_file_does_not_exist_file_count():
    lang_controller = LanguagesController()

    path = os.path.join(CURRENT_PATH, 'does_not_exist.java')

    lang_controller.check(path)

    assert lang_controller.total_files() == 0
