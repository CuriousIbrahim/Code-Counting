import os


FILE_EXTENSIONS = ['.java', '.py', '.c', '.cpp', '.h', '.js']

files = []

def check_if_file_is_of_extension(file):

    for e in FILE_EXTENSIONS:
        if e in file:
            return True

    return False

