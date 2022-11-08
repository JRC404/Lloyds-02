# Python Introduction

## Topics

* Fundamentals
    * Key features of Python
    * Variables / Constants
    * Conditions
    * Loops
    * Data Structures
    * Functions / Methods
* Object-oriented programming

```python
# test.py
print("hello, world.")
```

## VSCode Help

* shift alt up / down -> create a copy of the line above or below
* alt up / down -> move the line up or down
* ctrl ' -> will show and hide the terminal
* right click new file... examples/example.py -> this will create a folder called examples and a file called example.py inside
* alt z -> line wrapping
* ctrl / -> will create / delete a comment on a line
* (https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf)[Windows VSCode Shortcuts]

### Key Features of Python

* Case sensitive

```python
firstName = "Jacob"
FirstName = "Jacob"
firstname = "Jacob"
first_name = "Jacob"
```

#### Comments in Python 
* Comments are lines of code / thoughts that are ignored by the file / interpreter when it is executed
```python
# My first comment
print("Hello, World")
```

#### Whitespace is crucial in Python 
* Python reads whitespace as a break or indent and will run into issues if whitespace isn't used properly
```python
favourite_number = 4
if favourite_number < 5:
    print("Excellent. Less than 5")

if favourite_number < 5:
print("Excellent. Less than 5")
```

#### Naming conventions in Software Development

* Camel Casing
    * each word except the first starts with a capital letter
    * eachWordExceptTheFirstStartsWithACapitalLetter
    * eachwordexceptthefirststartswithacapitalletter
* Pascal Casing
    * Each word including the first starts with a capital letter
    * EachWordIncludingTheFirstStartsWithACapitalLetter
* Snake Casing (Python)
    * Each word is lower case and split by underscores
    * each_word_is_lower_case_and_split_by_underscores

## Variables

* Variables are a storage place for our values that we want to store in our program
* Variables can change
* Variables have a type

### Data Types

* Numerical Data Types
    * int -> whole number 0-9, both positive and negative
        * 1
        * 123456
    * float -> decimal number / floating point number
        * 0.145
        * 2.456
        * 8.1
        * 3.0
* String Data Types:
    * string
        * "anything inside of the quotes is a string"
        * "12" -> string NOT a number
        * "HIYA"
        * "©"
        * Anything on this list: https://www.fileformat.info/info/charset/UTF-8/list.htm
* Boolean Data Types:
    * True
    * False

## Bash

```
> ls -> list the files / folders inside of the directory we are in
> pwd -> print working directory
> directory is a folder
> cd Documents -> take us into the document folder
> clear -> clears the screeen of the bash window
> mkdir TestLloyds -> will create a TestLloyds folder
> Try and avoid spaces in Folder Names
> cd TestLloyds
> touch index.py -> create a file called index.py
> touch hello.py test.py -> create two files at once
> mkdir notes test
> cd notes
> cd .. -> takes us back one level (a folder backwards)
> cd ../.. -> takes us back two levels
> rm test.py -> removes the file test.py
> touch moveMe.py
> mv moveMe.py notes/
> cd notes
> mv moveMe.py ../test
> cd ../test
> pwd
> mv moveMe.py moved.py -> renamed the file moveMe to moved
> rm -r folderName
```

```
* Please create a folder called "Challenge" that has two files and a directory inside it:
    * directory: 
        * randomFolder
    * files: 
        * test.py
        * file.py

* Continue:
    * Rename test.py to myPythonFile.py
    * move file.py to the "randomFolder" directory

* Continue: 
    * Delete myPythonFile.py
```

## Conditionals

* If statements are logical statements that are based on a condition
* If statements can be one condition long or 1000 conditions long
* If statements can contain the following keywords:
    * if
    * elif (else if)
    * else

```python
my_age = 95

if my_age < 18:
    print("You are not allowed in the club.")
elif my_age <= 23:
    print("You are eligible for the Young Person discount.")
elif my_age <= 60:
    print("Full price as you are middle aged.")
elif my_age <= 65:
    print("Senior discount applied for you.")
elif my_age <= 100:
    print("You get in for free. Well done.")
else:
    print("You are too old. Sorreh.")
```

## Operators

### Arithmetic

* +, -, /, *, %

* 10 % 3 = 1
* 11 % 3 = 2
* 12 % 3 = 0
* 16 % 5 = 1

### Conditional / Comparison

* <, >, <= , >=, ==, !=
* < Less than
* > Greater than
* <= Less than OR equal to
* >= Greater than or equal to
* == Equal to
* != Not equal to

### Assignment

* = left is now equal to the right
* += left is equal to itself plus the right
* -= left is equal to itself minus the right
* *= left is equal to itself times the right
* /= left is equal to itself divided by the right

### Logical

* and - the left and the right are both true
```python
my_number = 8
if(my_number < 10 and my_number > 5) # true
if(my_number < 10 and my_number < 5) # false
```
* or - the left OR the right is true... can be both!
```python 
if(my_number < 10 or my_number > 5) # true
if(my_number < 10 or my_number < 5) # true
if(my_number < 6 or my_number < 5) # false
if(my_number < 10 or my_number == 8) # true
if(my_number == 10 or my_number == 8) # true
if(my_number == 10 or my_number == 15) # false
```
* not - reverse the result... if it's true originally... make it false
```python
my_number = 8
if(not(my_number < 10 and my_number > 5)) # false
if(not(my_number < 10 and my_number < 5)) # true

```

**XOR is not in Python BUT**
* XOR - exclusive OR... the left OR the right is TRUE but not both