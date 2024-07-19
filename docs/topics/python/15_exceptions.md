---
title: Exceptions
image: python.png
---

![](../../assets/images/topics/{{image}}){width="100"; align=right}

# {{ title}}

!!! note "Objectives"

    - Define exceptions as events that occur during program execution, disrupting the normal flow.
    - Recognize common reasons for exceptions, such as invalid input, file not found, and division by zero.
    - Identify specific types of exceptions in Python, including `ValueError`, `TypeError`, `IndexError`, `NameError`, and `ZeroDivisionError`.
    - Understand the circumstances that lead to each type of exception.
    - Describe the structure of a `try...except` block and its role in managing exceptions.
    - Demonstrate how to catch and handle exceptions using generic and specific `except` blocks.

## What are Exceptions?

* Exceptions are events that occur during the execution of a program, which disrupt the normal flow of the program.  
* They can be caused by various reasons such as invalid input, file not found, division by zero, etc.

Consider the following example of calculating the area of a circle.  

```py
radius = int(input("Enter circle radius: ))
area = 3.14 * radius**2
print(area)
```

In a sample run of the program the user enters a `float`, which would seem to be a reasonable value from the user's perspective (the prompt does not specify an `integer` or a `float`).

```py
Enter circle radius: 2.4
Traceback (most recent call last):
  File "c:\Users\dell touch\Documents\GitHub\pythonprogramming\docs\test.py", line 1, in <module>
    radius = int(input("Enter circle radius: "))
ValueError: invalid literal for int() with base 10: '2.4'
```

The program has crashed with an exception error: `ValueError: : invalid literal for int() with base 10: '2.4'`.  Exceptions are bad and we should want to avoid them.

Good programming practice is to consider such situations and provide a strategy for handling such data.  Here, it would be trivial to use the `float()` function rather than `int()`, but what if the user entered a `string`?  We would still get the `ValueError` exception.

Python provides  way of dealing with these exception errors so the program can continue or exit gracefully known as a `try .. except` block.

## Types of Exception

### ValueError

We saw this type of exception in the previous example.  The value error is **raised** when an operation or a function receives an argument of the correct type but with an inappropriate value.  Typically when trying to convert a string to an integer or float, but the string doesn't represent a valid number or using an argument that is out of the acceptable range for a function or method.

### TypeError

A `TypeError` is raised when an operation or function is applied to an object of inappropriate type.  For example, trying to add an integer to a string, using the wrong number of arguments when calling a function, or trying to call a function on an object (such as a list) that does not support that function.

E.g.

```python
x = 5 + "2"         # Raises a TypeError because you can't add an int to a str.
result = len(42)    # Raises a TypeError because you can't find the length of an int.
```

### IndexError

An `IndexError` occurs when you attempt to access an element at an index that is not valid for the given sequence or collection. It's a common error when working with lists, tuples, strings, or similar data structures in Python. 

E.g.

```python
my_list = [1, 2, 3]
print(my_list[5])  # Raises an IndexError because there is no element at index 5.

my_string = "hello"
print(my_string[10])  # Raises an IndexError because there is no character at index 10.

empty_list = []
print(empty_list[0])  # Raises an IndexError because the list is empty.
```

### NameError

A `NameError` occurs when Python encounters a name (identifier for a variable, function, or module) that it cannot find, it's often caused by typos, incorrect variable names etc..

E.g.

```python
print(variable_name)  # Raises a NameError if 'variable_name' is not defined.

def my_function():
    print(x)  # Raises a NameError if 'x' is not defined globally.

import math
print(math.pi)  # No NameError because 'math' module is imported.

print(non_existent_module.some_function())  # Raises a NameError if 'non_existent_module' doesn't exist.
```

### ZeroDivisionError

As the name implies, when we try to divide by $0$ this exception will be raised.

## Handling Exceptions

To handle these exceptions we use `try .. except`.  For example, using the area of a circle problem from earlier:

```python
try:
    radius = float(input("Enter circle radius: "))
    area = 3.14 * radius**2
    print(area)
except:
    print("Please enter a valid number: ")

```

* The `try` block contains the code that might raise an exception.
* The `except` block contains the code to handle the exception when it occurs.

Catching the exception in this way gives us a chance to fix the problem with the input, try again or exit gracefully.
 
In the example the `except` block was generic, i.e. it would catch anything.  It is usually better to specify the type of exception we're trying to catch as it helps with debugging.  For example, to catch an `IndexError`:

```python
try:
    students = ["Alice", "Bob", "Carol"]
    print(students[3])
except IndexError:
    print("There is no index with that value")
```

Here the type of error we want to catch is specified.

The types of error can be provided as a tuple:

```python
try:
    # code that may raise an exception
except IndexError, ValueError, TypeError:
    # code to handle the exception raised
```

Or provide multiple `except` blocks:

```python
try:
    # Code that may raise an exception
except ExceptionType1:
    # Code to handle ExceptionType1
except ExceptionType2:
    # Code to handle ExceptionType2
```

## The `finally` Block

The `try ... except` block can also take a `finally` section.  This is used to execute code regardless of whether an exception was raised or not. It is often used for cleanup tasks, like closing files or releasing resources.

## Raising an exception

Sometimes we need to raise an exception when there is a potential issue that needs to be handled, perhaps not covered by any of the exceptions seen thus far.  For example, the age of a student will be within a certain range (depending on their phase of study).  e.e. a secondary school student would normally be between 11 and 18 years old.  Should the user provide an age outside of that range we can raise an exception to handle that data.

The syntax to use is:

```python
raise ExceptionType("Error message")
```

We can create our own `ExceptionType`.  This involves creating a class in Python.  Classes are covered in a later section (and are beyond the requirements for GCSE) but the following illustrates the principle:

```python
class AgeError(Exception):
    pass

try:
    age = int(input("Enter your age: "))
    if age < 11 or age > 18:
        raise AgeError("Invalid age entered!")
    else:
        print("Age is valid.")
except AgeError as e:
    print(f"Error: {e}")
```

We can also raise an exception for a built-in exception.  E.g. in a temperature conversion program we might ask the user for the units, either a `C` or an `F` (for Celcius and Fahrenheit), we can raise an exception if the value entered is not correct:

```python
if unit == "C":
    converted_temperature = (temperature * 9/5) + 32
    converted_unit = "Fahrenheit"
elif unit == "F":
    converted_temperature = (temperature - 32) * 5/9
    converted_unit = "Celsius"
else:
    # Handle invalid unit
    raise ValueError(f"Invalid unit '{unit}' entered.")
```

## Questions

{{ get_questions(page.title)}}

1. What are exceptions in Python?
2. What is the purpose of the `try...except` block?
3. What is the purpose of the `finally` block?
4. How do you handle multiple exceptions in Python?
5. Which exception is raised when dividing by zero?
6. Why is the `finally` block useful in file operations?
7. When do you use the `try...except` block in your code?
8. What is the difference between `except ExceptionType` and `except` without specifying an exception type?
9. What happens if an exception is not handled in Python?
10. Explain with an example how you would handle an `IndexError` using `try...except`.

## Programming Tasks

{{ get_programming_tasks(page.title)}}