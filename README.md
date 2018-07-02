# Code-Counting

Code Counting, written in Python 3 will explore a given root directory and print out:
* Number of files that were counted
* Total lines of code
* Total time to process

## Current Known Bugs

- For C and C++ projects, Code Counting might print multiple lines for the language C and C++ and they all contain the 
exact same amount of lines of code and number of files. They are the same object but tracking different file 
extensions (.h, .cpp, .c, ...)