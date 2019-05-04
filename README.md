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
python3 code_counting '<directory of your choice>'
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
Ibrahims-MacBook-Pro:Code-Counting Ibrahim$ python3 code_counting '/Users/Ibrahim/Documents/My Documents/Projects'
INFO:root:Exploring /Users/Ibrahim/Documents/My Documents/Projects
INFO:root:Exploring finished
INFO:root:Checking 62244 files

==============================================

Language: Python, 5348 lines of code in 139 files
Language: XML, 67290 lines of code in 587 files
Language: HTML, 77093 lines of code in 311 files
Language: Java, 7468 lines of code in 90 files
Language: Text, 17078 lines of code in 154 files
Language: INI, 170 lines of code in 13 files
Language: Gradle, 124 lines of code in 7 files
Language: Batch File, 336 lines of code in 4 files
Language: Markdown, 831316 lines of code in 4994 files
Language: JavaScript, 4416746 lines of code in 35602 files
Language: JSON, 835484 lines of code in 5664 files
Language: YAML, 9705 lines of code in 536 files
Language: TypesScript, 84834 lines of code in 223 files
Language: C/C++/Objective-C, 22130 lines of code in 65 files
Language: Emacs Lisp, 18 lines of code in 3 files
Language: CSS, 28324 lines of code in 68 files
Language: PHP, 1 line of code in 1 file
Language: Shell, 254 lines of code in 14 files
Language: Scala, 363 lines of code in 6 files
Language: Matab, 75 lines of code in 1 file
Language: Less, 12204 lines of code in 123 files
Language: SCSS, 1832 lines of code in 33 files

21.072 seconds to process 6418193 lines of code across 48638 files with an average of 131.96 lines of code per file
```


## Interesting Behaviour

Code-Counting does not count any lines after the last line in a file. Even if there is space after the last line 
in a text editor, Code-Counting will not read it. This was discovered through the unit tests.

## Todo 

- ~~Switch to pytest for unit testing~~
- ~~Add test that goes through every file in 'test-code' directory~~
- Make test code files and tests for the following languages:
    - ~~Javascript~~
    - ~~HTML~~
    - ~~CSS~~
    - C/C++
    - C#
- Add functionality to allow user to ignore specific directories and files

## Supported Languages to Detect

- Java
- Python 
- C/C++/Objective-C
- Javascript
- HTML
- CSS
- C#
- Ruby
- Shell
- Groovy
- XML
- JSON
- Markdown
- Scala
- Perl
- PHP
- Swift
- TypeScript
- YAML
- Text
- Go
- Clojure
- Rust
- Assembly
- Kotlin
- Gradle
- INI
- Emacs
- INI
- Emacs Lisp
- TeX
- Visual Basic
- Basic
- Factor
- ChucK
- SQL
- Elixir
- Haskell
- Haxe
- Dart
- Jupyter Notebook
- Mathematica
- R
- Lua
- SCSS
- Sass
- Less
- Matlab
