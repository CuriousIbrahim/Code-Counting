import os

CURRENT_PATH = os.path.dirname(os.path.realpath(__file__))

TEST_CODE_DIR = 'test-code/'

JAVA_FILE = os.path.join(TEST_CODE_DIR, 'Person.java')
PYTHON_FILE = os.path.join(TEST_CODE_DIR, 'Person.py')
HTML_FILE = os.path.join(TEST_CODE_DIR, 'test.html')
CSS_FILE = os.path.join(TEST_CODE_DIR, 'test.css')
JAVASCRIPT_FILE = os.path.join(TEST_CODE_DIR, 'test.js')

JAVA_LINE_COUNT = 39
PYTHON_LINE_COUNT = 16
HTML_LINE_COUNT = 29
CSS_LINE_COUNT = 9
JAVASCRIPT_FILE_COUNT = 8

TEST_CODE_DIR_LINE_COUNT = JAVA_LINE_COUNT + PYTHON_LINE_COUNT + HTML_LINE_COUNT + CSS_LINE_COUNT + \
                           JAVASCRIPT_FILE_COUNT

TEST_CODE_DIR_FILE_COUNT = 5
