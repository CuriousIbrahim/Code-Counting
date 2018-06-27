

"""
Language class, contains name of language as well as the language's extension. Example: Java .java; HTML .html
"""

class Language:
    name = ''
    extension = []

    def __init__(self, name, extension):
        self.name = name
        self.extension = extension


