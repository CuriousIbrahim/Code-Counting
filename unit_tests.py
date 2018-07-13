import unittest
import os
from lang_controller import LanguagesController

CURRENT_PATH = os.path.dirname(os.path.realpath(__file__))

class TestLanguageController(unittest.TestCase):

    def test_java_line_count(self):
        lang_controller = LanguagesController()

        path = os.path.join(CURRENT_PATH, 'test-code/Person.java')

        lang_controller.check(path)

        result = lang_controller.get_used_language('.java').lines_of_code

        self.assertEqual(result, 39)

    def test_python_line_count(self):
        lang_controller = LanguagesController()

        path = os.path.join(CURRENT_PATH, 'test-code/Person.py')

        lang_controller.check(path)

        result = lang_controller.get_used_language('.py').lines_of_code

        self.assertEqual(result, 16)


if __name__ == '__main__':
    unittest.main()