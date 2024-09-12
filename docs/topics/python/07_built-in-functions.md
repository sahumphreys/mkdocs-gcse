---
title: Built in functions
image: python.png
filename: '_data/python_questions.json'
---

![](../../assets/images/topics/{{image}}){width="100"; align=right}

# {{ title }}

!!! note "Objectives"

    - Understand the concept of built-in functions in Python.
    - Learn how to use some commonly used built-in functions for math, strings, and basic input/output.
    - Explore the purpose and usage of functions like `print()`, `len()`, `input()`, and more.

As well as creating our own functions Python comes with a wide range of built-in functions that perform various tasks, making programming easier and more efficient. These functions are part of Python's standard library and can be used without the need for additional installations.

There are a whole host of other functions available to us that can be either `import`ed to our program e.g. the `random` library, or installed e.g. the `pandas` library.  We'll consider this approach in a later section

## Example 5

```python hl_lines="2 6 10 13 16 20"
print("Welcome to the Built-in Functions Lesson!")
user_name = input("Enter your name: ")
print("Hello,", user_name)

sample_string = "Climate"
string_length = len(sample_string)
print("The length of the string is:", string_length)

value = input("Enter a whole number: ")
print(type(value))

value_int = int(value)
print(type(value))

number = -7.25
abs_number = abs(number)
print("The absolute value is:", abs_number)

decimal_number = 3.14159
rounded_number = round(decimal_number, 2)
print("The rounded value is:", rounded_number)
```

Before running this code, read it and predict what you think will be displayed for the following:

- line 2: What will `input("Enter your name: ")` do?
- line 6: What does the `len` function return for the string 'Climate'?
- line 10 and 13: what will be output from the `type()` function in both cases?
- line 16: What will be the result of `abs(-7.25)`?
- line 20: What will `round(3.14159, 2)` return?
  

Run the program in a Python environment and compare the actual output with your predictions.

## Commonly Used Built-In Functions 

| Function | Description | Example | Output |
|----------|-------------|---------|--------|
| `print()` |We have seen this used in previous sections. The `print()` function is used to display information on the screen. It can print text, variables, and the result of expressions. |`print("Welcome")`| "Welcome"|
| `len()` | The `len()` function returns the length of a string. It counts the number of characters in the string. |`len("Hello")`| 5 |
|`input()` | The `input()` function allows user input. It waits for the user to enter data and returns it as a string. || |
|`int()` | used for data type conversion. `int()` converts a value to an integer | ||
| `float()` | used for data type conversion. `float()` converts a value to an real number |||
|`str()` | The `str()` function converts other data types to strings |||
|`max()`| used to find the maximum value among a set of values|||
| `min()`|used to find the minimum value among a set of values. |||
|`abs()` |The `abs()` function returns the absolute value of a number. |||
|`round()`|The `round()` function rounds a floating-point number to the nearest integer |||
| `str.upper()`| Converts characters in `str` variable to upper case |||
|`str.lower()`| Converts characters in `str` variable to lower case |||
| `chr()` | `chr()` converts an ASCII code (integer) to a character |||
| `ord()` |`ord()` converts a character to its ASCII integer code |||

## Activity

Copy and paste the following code into a code editor, before running the code read it and predict what you think the output will be.  Then make changes to the code as indicated below.

```python
print("Welcome to the Modified Built-in Functions Lesson!")
age = int(input("Enter your age: "))
print("You are", age, "years old.")

another_string = "Environmental Science"
string_upper = another_string.upper()
string_lower = another_string.lower()
print("Uppercase:", string_upper)
print("Lowercase:", string_lower)

float_number = float(input("Enter a decimal number: "))
rounded_float = round(float_number)
print("Rounded number:", rounded_float)

negative_number = int(input("Enter a negative integer: "))
absolute_value = abs(negative_number)
print("Absolute value:", absolute_value)
```
Make the following changes:

  - Change the string and observe the output of the `upper()` and `lower()` methods.
  - Input a decimal number and see the rounded result.
  - Input a negative integer and see the absolute value.

## Climate Quest Project

![](../../assets/images/climate-quest.png){align=left width="200"}

Throughout this topic we'll be working on a large scale project: **Climate Quest**.  In this project a player embarks on a journey to combat the effects of climate change by making decisions that impact the environment. Each choice affects the outcome of the game, emphasizing the importance of individual actions in addressing climate change.

[Go to task 5 - Built-in Functions](./climate_quest/task_5.md){:class=md-button}

## Questions

{{ show_questions(page.title, page.meta.filename) }}

## Programming Tasks

{{ get_programming_tasks(page.title)}}

