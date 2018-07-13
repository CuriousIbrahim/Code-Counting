from language import get_languages
from util import get_file_extension, count_lines_of_code
import logging


class LanguagesController:

    def __init__(self):
        self.languages = get_languages()
        self.used = {}


    def get_used_language(self, lang):
        return self.used[lang]

    """If the file is of an extension (ex: .java, .py), it will add it to the a separate dictionary and start counting 
    its lines"""

    def check(self, file):

        logging.info('Checking', file)

        ext = get_file_extension(file)
        logging.info('\t', file, 'is of', ext, 'extension')
        if ext in self.used:
            logging.info('\t', file, 'is already in used')
            self._add_file_and_count_lines(file, ext)
        elif ext in self.languages:
            logging.info('\t', file, 'is not in used, adding it')
            lang = self.languages[ext]
            self.used[ext] = lang
            self._add_file_and_count_lines(file, ext)

    def _add_file_and_count_lines(self, file, ext):

        count = count_lines_of_code(file)
        self.used[ext].add_lines(count)
        self.used[ext].add_file()

    def results(self):
        result = ''

        added = []

        for l in self.used:

            temp = str(self.used[l])

            if temp not in added:
                result += temp + '\n'
                added.append(temp)

        return result

    def total_lines(self):

        total = 0

        for l in self.used:
            total += self.used[l].lines_of_code

        return total

    def total_files(self):

        total = 0

        for l in self.used:
            total += self.used[l].files

        return total
