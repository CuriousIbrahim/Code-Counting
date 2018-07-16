# Code-Counting

Code Counting, written in Python 3 will explore a given directory and will:
1. Detect the languages in the given directory (ex. Java, HTML, Python, etc.)
2. For each detected language, will:
    1. Print lines of code
    2. Number of files
3. Will finally print:
    1. Time to process
    2. Total lines of code in given directory
    3. Total files (this only includes the detected languages)
    4. An average lines of code per file 

## Installation and Use

Requirements:
* Git
* Python 3

Git clone first:
```buildoutcfg
git clone https://github.com/CuriousIbrahim/Code-Counting
```

then to use:
```buildoutcfg
cd Code-Counting/
python3 code_counting <directory of your choice>
```

### Running tests

Requirement(s):
- [pytest](https://github.com/pytest-dev/pytest)

To install pytest, run the following command:
```buildoutcfg
pip3 install pytest
```

To run the written tests, run the following command:
```buildoutcfg
py.test
```

## Example

```buildoutcfg
Ibrahims-MacBook-Pro:Code-Counting Ibrahim$ python3 code_counting /Users/Ibrahim/Documents/My\ Documents/Projects/
INFO:root:Starting program!
INFO:root:Exploring /Users/Ibrahim/Documents/My Documents/Projects/
INFO:root:Exploring finished
INFO:root:Checking 62500 files

==============================================

Language: Python. 5293 lines of code in 139 files
Language: HTML. 77093 lines of code in 311 files
Language: Java. 7468 lines of code in 90 files
Language: Javascript. 4416738 lines of code in 35601 files
Language: C/C++. 22130 lines of code in 65 files
Language: CSS. 28324 lines of code in 68 files

14.826189279556274 seconds to process 4579176 lines of code across 36339 files with an average of 126.01271361347312 lines of code per file
```


## Supported Languages

- Java
- Python 
- C/C++
- Javascript
- HTML
- CSS
- C#

## Interesting Behaviour

Code-Counting does not count any lines after the last line in a file. Even if there is space after the last line 
in a text editor, Code-Counting will not read it. This was discovered through the unit tests.

## Todo 

- ~~Switch to pytest for unit testing~~
- ~~Add test that goes through every file in 'test-code' directory~~
- Make test code files and tests for the following languages:
    - Javascript
    - ~~HTML~~
    - ~~CSS~~
    - C/C++
    - C#