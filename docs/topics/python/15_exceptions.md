---
title: Exceptions
image: python.png
filename: '_data/python_questions.json'
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

## Example 13

```python hl_lines="10-12"
def divide_numbers(a, b):
    return a / b

def get_element(lst, index):
    return lst[index]

def convert_to_int(value):
    return int(value)

print(divide_numbers(10, 0))
print(get_element([1, 2, 3], 5))
print(convert_to_int("abc"))
```

Using the example code above, predict the output for the following:

- What will happen when dividing 10 by 0, line 10?
- What do you think will occur when trying to access an index that doesn’t exist, line 11?
- What will happen when trying to convert the given string to an integer, line 12?

Copy and paste the code into a Python environment, run the code and check your predictions against the actual results.

In each case an error occurred, these errors are so extreme the program cannot continue and it crashes out with an error message:

- In the first instance we're trying to divide by zero, which triggers the **ZeroDivisionError** exception
- Then we try to access an item in a list using an index value that does nor exist, triggering an **IndexError** exception
- Finally, `abc` cannot be converted into an integer thus triggering a **ValueError**

There are other types of exceptions that can occur including **NameError** and **TypeError**.  You can find others [here](https://docs.python.org/3/library/exceptions.html#concrete-exceptions)

These errors are known as **exceptions** and to avoid the error, and program crashing out, we need to insert code that handles these exceptions.

## Handling exceptions

In Python, `the try...except...finally` block is a powerful construct used for exception handling, allowing a program to handle errors gracefully and ensure that important cleanup actions are always executed. 

- The `try` block contains the code that may trigger, or **raise** an exception
- The `except` block allows you to catch and manage specific or general exceptions that occur. 
- The `finally` block, which is optional, runs regardless of whether an exception was raised or not, making it ideal for tasks like closing files or releasing resources. This ensures that necessary final actions, such as closing a file or cleaning up resources, are always performed, even if an error occurs during the execution of the try block.
  
For example, in the `divide_numbers()` function, we can check for the divisor being passed in.  Should it be a $0$ the error can be handled:

```python
def divide_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None
    finally:
        print("Execution of divide_numbers() completed.")
```

- Line 3: the function will attempt to return the result of dividing `a` by `b`.  If this raises an exception control is then passed to ...
- ... Line 4: which prints a helpful message and returns from the function
- Line 7: this is optional and here just provides a message acknowledging safe completion of the function

## Activity

Following this pattern, modify the following code to capture an exceptions that might be raised in our example program:

```python
def divide_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None

def get_element(lst, index):
    # insert a try..except block to catch and handle an out-of-range index.
    return lst[index]

def convert_to_int(value):
    # insert a try..except block to manage invalid string-to-integer conversions.
    return int(value)

print(divide_numbers(10, 2))
print(divide_numbers(10, 0))
print(get_element([1, 2, 3], 5))
print(convert_to_int("abc"))
print(convert_to_int("123"))
```

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

## Generic Exceptions

The following is valid:

```python
def divide_numbers(a, b):
    try:
        return a / b
    except:
        print("Error: Division by zero is not allowed.")
        return None

```

* The `try` block contains the code that might raise an exception.
* The `except` block contains the code to handle the exception when it occurs.

In the example the `except` block was generic, i.e. it would catch anything.  It is usually better to specify the type of exception we're trying to catch as it helps with debugging.  

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

Sometimes we need to raise an exception when there is a potential issue that needs to be handled, perhaps not covered by any of the exceptions seen thus far.  For example, the age of a student will be within a certain range (depending on their phase of study).  e.g. a secondary school student would normally be between 11 and 18 years old.  Should the user provide an age outside of that range we can raise an exception to handle that data.

The syntax to use is:

```python
raise ExceptionType("Error message")
```

We can create our own `ExceptionType`.  This involves creating a class in Python.  Classes are beyond the requirements for GCSE, but the following illustrates the principle:

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

## Climate Quest Project

![](../../assets/images/climate-quest.png){align=left width="200"}

Throughout this topic we'll be working on a large scale project: **Climate Quest**.  In this project a player embarks on a journey to combat the effects of climate change by making decisions that impact the environment. Each choice affects the outcome of the game, emphasizing the importance of individual actions in addressing climate change.

**There is no additional task for the Climate Quest project.  Use the time to continue working on your game**

## Summary

[Cheat sheet for exceptions (and files)](../../files/beginners_python_cheat_sheet_pcc_files_exceptions.pdf){:class=md-button}[^source]

[^source]: [https://ehmatthes.github.io/pcc_3e/cheat_sheets/(https://ehmatthes.github.io/pcc_3e/cheat_sheets/)]

## Questions

{{ show_questions(page.title, page.meta.filename) }}

## Programming Tasks

{{ get_programming_tasks(page.title)}}