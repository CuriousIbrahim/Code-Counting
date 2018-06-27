from language import Language, get_languages


class LanguagesController:

    def __init__(self):
        self.languages = get_languages()

    """If the file is of an extension (ex: .java, .py) then return the Language object for that extension; if the file 
    is not of any extension, then return None"""

    @staticmethod
    def check_file_is_of_extension(self, file):
        for lang in self.languages:
            for ext in lang.extension:
                if ext in file:
                    return lang

        return None
