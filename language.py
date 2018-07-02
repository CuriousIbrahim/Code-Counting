

"""
Language class, contains name of language as well as the language's extension. Example: Java .java; HTML .html
"""


class Language:

    def __init__(self, name, extension):       # extension has to be a list
        self.name = name

        for index, ext in enumerate(extension):
            if '.' not in ext:
                extension[index] = '.' + ext

        self.extension = extension

    def __str__(self):
        return 'NAME: {} EXTENSION: {}'.format(self.name, self.extension)


LANGUAGES_FILE = 'languages.txt'


def get_languages():

    def parse(data):
        # Split between ';', you would have a list with length 2, index 0 is name while index 1 is extension
        data = data.split(';')

        # Clean name (remove \n)
        data[0].rstrip('\n')

        # There might be multiple extensions for a single language, so split at ','
        data[1] = data[1].split(',')

        # Clean extensions (remove \n)
        for index, line in enumerate(data[1]):
            data[1][index] = line.strip()

        return data

    languages = []

    with open(LANGUAGES_FILE) as f:

        # Skip header row
        next(f)

        for line in f:
            data = parse(line)

            # Create new Language object
            Language(data[0], data[1])

            # For each extension, creates a tuple for the object. The languages list is then converted into a dictionary
            # where each file extension acts as a key which is associated which its Language object as its value.
            # Ex. {'.java': Java (Language Object), '.c' C/C++ (Language Object), '.cpp': C/C++ (Language Object), ...}
            for ext in data[1]:
                languages.append((ext, Language))

    return dict(languages)
