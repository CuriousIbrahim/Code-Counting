from code_counting.language import get_languages
from code_counting.util import get_file_extension, count_lines_of_code
import logging
import os


class LanguagesController:

    def __init__(self):
        self.languages = get_languages()
        self.used = {}


    def get_used_language(self, lang):
        if lang in self.used:
            return self.used[lang]
        return None

    """If the file is of an extension (ex: .java, .py), it will add it to the a separate dictionary and start counting 
    its lines"""

    def check(self, file):

        ext = get_file_extension(file)
        if ext in self.languages:
            logging.debug('\t{} is of {} extension'.format(file, ext))

        if ext in self.used:
            logging.debug('\t{} is already in used'.format(file))
            self._add_file_and_count_lines(file, ext)
        elif ext in self.languages:
            logging.debug('\t{} is not in used, adding it'.format(file))
            lang = self.languages[ext]
            self.used[ext] = lang
            self._add_file_and_count_lines(file, ext)
        else:
            logging.debug('/t{} is not any of the known extensions'.format(file))

    def _add_file_and_count_lines(self, file, ext):
        if os.path.isfile(file):
            count = count_lines_of_code(file)
            self.used[ext].add_lines(count)
            self.used[ext].add_file()

    def results(self):
        result = ''

        added = []

        for l in self.used:

            temp = str(self.used[l])

            if self.used[l].name not in added:
                result += temp + '\n'
                added.append(self.used[l].name)

        return result

    def total_lines(self):

        total = 0

        added = []

        for l in self.used:
            if self.used[l].name not in added:
                total += self.used[l].lines_of_code
                added.append(self.used[l].name)

        return total

    def total_files(self):

        total = 0

        added = []

        for l in self.used:
            if self.used[l].name not in added:
                total += self.used[l].files
                added.append(self.used[l].name)

        return total
