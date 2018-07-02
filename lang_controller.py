from language import Language, get_languages
from util import get_file_extension, count_lines_of_code


class LanguagesController:

    def __init__(self):
        self.languages = get_languages()
        self.used = {}

    """If the file is of an extension (ex: .java, .py), it will add it to the a seperate dictionary and start counting 
    its lines"""

    def check(self, file):

        ext = get_file_extension(file)

        if ext in self.used:
            self._add_file_and_count_lines(file, ext)
        elif ext in self.languages:

            lang = self.languages[ext]

            self.used[ext] = lang

            self._add_file_and_count_lines(file, ext)

    def _add_file_and_count_lines(self, file, ext):
        count = count_lines_of_code(file)
        self.used[ext].add_lines(count)
        self.used[ext].add_file()

    def results(self):
        result = ''

        for l in self.used:
            result += self.used[l] + '\n'

        return result