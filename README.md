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