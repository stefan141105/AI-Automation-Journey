# CS50P Week 0 (Functions & Variables)

## Functions
A **function** is an action that lets you do something in a program.

## Arguments
An **Argument** is an input to a function that somehow influences its behaviour.

## Side effects
A **side effect** is something a function does besides returning a value, such as printing text on a screen.

## print() 
'print ()' is a function used to display output on the screen.

## Bugs
A **bug** is a natural part of coding. It represents a problem/mistake in the code. It can take a lot of forms.

## input() 
'input ()' allows users to type information into the program.

## Return Values
A **return value** is a value that a function sends back after it finishes its work.

## Variables
A **variable** can store values such as numbers, text or even images or videos. They work as a container for some values inside of a computer/program.

## Comments
**Comments** are notes to yourself in your code. In python the symbol '#' is used for writting a comment which will be completly ignored by the computer when running the program.

## Pseudocode
A **pseudocode** is not one specific language. It is a human language such as English which you use to express your thoughts algorithmically and methodically.

## Parameters
A **parameter** is a name inside a function that waits to receive a value. The difference between an argument and a parameter is that one is an actual value you give and the other is a placeholder.

## Strings
A **string** is text in Python, usually written inside quotation marks. 

## Methods
A **method** is a function that belongs to a type of value, such as a string.

For example:
'name.strip()'

## .strip()
'.strip()' removes any extra spaces from the beginning and end of a string

## .title()
'.title()' capitalizes the first letter of each word in a string just like a title.

## .capitalize() 
'.capitalize()' capitalizes the first letter in a string.

## f-strings
An **f-string** allows you to put variables directly inside a string using '{}' 

Example:

print(f"hello, {name}")

## sep=
'sep=' controls what is placed between multiple values inside print().

Example: 
'print ("A","B","C", sep="-")

Output:
A-B-C

## end=
'end=' controls what is printed at the end of a print() statement.

By default, 'print()' ends with a new line.

Example:
print("Hello", end=" ")
print("World")

Output:
Hello World

## split()
A 'split()' breaks a string into smaller parts and returns them as a list.

By default, it splits wherever there is a space.

Example:
name = Stefan Voicu
parts = name.split()

Result:
["Stefan", "Voicu"]

## int
Python does support **interegs** (int). 

## int()
'int()' transforms the default data type (str) to integers.

For example:

x = "1"
y = "2"

z = x + y

print (z) => the result will be 12 as the default data is str rather than int.

When using int():

z = int(x) + int(y)

print (z) => the result will be 3 as the program will recognise x and y as integers.

## float
**Float** is a data type which represents numbers with decimal points.

## float()
'float()' transforms the data type into floating pint values (values with decimal places).

## def 
This means defining your own function so basically creating functions to improve efficiency of the code/program

## scope
This refers to a variable only existing in the context in which you defined it.

## '='
'=' is the assignment operator. It gives value to a variable.

## '+'
'+' can add numbers together or join strings togerher.

## pow()
'pow()' raises a number to a power.s

## Week 0 Reflection

**Easiest:** 
One of the easiest part of this week is understanding VS code and how to navigate through the programm. Also i feel like it is easy to understand different kind of funtions such as print (), or input(), int() etc.

**Hardest:** 
Implementing new functions from the python library (where you find different functions and codes for python). Hard for me to understand those. Also i feel like there is a blank in arguments and parameters and i feel like i do not fully understand their purpose.

**Still unclear:**
Still don't understand how 'sep =' and 'end ='. I do not understand how to use them. I have tried once to use 'sep =' but it did not work and did not understand why.
