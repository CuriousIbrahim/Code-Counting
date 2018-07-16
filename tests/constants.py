import os

CURRENT_PATH = os.path.dirname(os.path.realpath(__file__))

TEST_CODE_DIR = 'test-code/'

JAVA_FILE = os.path.join(TEST_CODE_DIR, 'Person.java')
PYTHON_FILE = os.path.join(TEST_CODE_DIR, 'Person.py')
HTML_FILE = os.path.join(TEST_CODE_DIR, 'test.html')
CSS_FILE = os.path.join(TEST_CODE_DIR, 'test.css')

JAVA_LINE_COUNT = 39
PYTHON_LINE_COUNT = 16
HTML_LINE_COUNT = 29
CSS_LINE_COUNT = 9

TEST_CODE_DIR_LINE_COUNT = JAVA_LINE_COUNT + PYTHON_LINE_COUNT + HTML_LINE_COUNT + CSS_LINE_COUNT
