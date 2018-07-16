# Code-Counting

Code Counting, written in Python 3 will explore a given root directory and will:
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
python3 code-counting <directory of your choice>
```

## Example

```buildoutcfg
Ibrahims-MacBook-Pro:Code-Counting Ibrahim$ python3 code-counting.py /Users/Ibrahim/Documents/My\ Documents/Projects/
Language: Python. 5179 lines of code in 134 files
Language: HTML. 77064 lines of code in 310 files
Language: Java. 7158 lines of code in 86 files
Language: Javascript. 4412072 lines of code in 35544 files
Language: C/C++. 22130 lines of code in 65 files
Language: CSS. 28307 lines of code in 67 files

21.298703908920288 seconds to process 4574040 lines of code across 36271 files with an average of 126.10735849576797 lines of code per file
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
- Add test that goes through every file in 'test-code' directory
- Make test code files for the following languages:
    - Javascript
    - HTML
    - CSS
    - C/C++
    - C#