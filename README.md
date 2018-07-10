# Code-Counting

Code Counting, written in Python 3 will explore a given root directory and print out:
* Each language that was detected, and for each language that was detected:
    * THe lines of code
    * Files 
* And finally will state amount taken, total lines code, total files, and the average lines of code per file

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
Ibrahims-MacBook-Pro:Code-Counting Ibrahim$ python3 code-counting.py /Users/Ibrahim/Documents/My Documents/Projects
Language: Python. 11557 lines of code in 124 files
Language: HTML. 38123 lines of code in 308 files
Language: Java. 9620 lines of code in 83 files
Language: Javascript. 4693509 lines of code in 35544 files
Language: C/C++. 7293 lines of code in 65 files
Language: CSS. 7855 lines of code in 66 files

5.451298236846924 seconds to process 4775250 lines of code across 36255 files with an average of 131.7128671907323 lines of code per file
```


## Supported Languages

- Java
- Python 
- C/C++
- Javascript
- HTML
- CSS
- C#

## Current Known Bugs

- ~~For C and C++ projects, Code Counting might print multiple lines for the language C and C++ and they all contain the 
exact same amount of lines of code and number of files. They are the same object but tracking different file 
extensions (.h, .cpp, .c, ...)~~ - Fixed on July 2, 2018