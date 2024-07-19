---
title: Built-in functions
image: python.png
---

![](../../assets/images/topics/{{image}}){width="100"; align=right}

# {{ title }}

!!! note "Objectives"

    - Understand the concept of built-in functions in Python.
    - Learn how to use some commonly used built-in functions for math, strings, and basic input/output.
    - Explore the purpose and usage of functions like `print()`, `len()`, `input()`, and more.

As well as creating our own functions Python comes with a wide range of built-in functions that perform various tasks, making programming easier and more efficient. These functions are part of Python's standard library and can be used without the need for additional installations.

There are a whole host of other functions available to us that can be either `import`ed to our program e.g. the `random` library, or installed e.g. the `pandas` library.  We'll consider this approach in a later section

## Commonly Used Built-In Functions 

### 1. `print()`

The `print()` function is used to display information on the screen. It can print text, variables, and the result of expressions. 

Example:

```python
print("Hello, World!")
```

### 2. `len()`

The `len()` function returns the length of a string. It counts the number of characters in the string. Example:

```python
text = "Python"
length = len(text)  # length will be 6
```

### 3. `input()`

The `input()` function allows user input. It waits for the user to enter data and returns it as a string. Example:

```python
name = input("Enter your name: ")
```

### 4. `int()`, `float()`

These functions are used for data type conversion. `int()` converts a value to an integer, and `float()` converts it to a floating-point number. Example:

```python
num_str = "42"
num_int = int(num_str)    # num_int will be 42
num_float = float(num_str)  # num_float will be 42.0
```

### 5. `str()`

The `str()` function converts other data types to strings. Example:

```python
num = 42
num_str = str(num)  # num_str will be "42"
```

### 6. `max()` and `min()`

These functions are used to find the maximum and minimum values among a set of values. Example:

```python
a = 5
b = 10
maximum = max(a, b)  # maximum will be 10
minimum = min(a, b)  # minimum will be 5
```

### 7. `abs()`

The `abs()` function returns the absolute value of a number. Example:

```python
num = -5
abs_num = abs(num)  # abs_num will be 5
```

### 8. `round()`

The `round()` function rounds a floating-point number to the nearest integer. Example:

```python
value = 3.7
rounded_value = round(value)  # rounded_value will be 4
```

### 9. `str.upper()` and `str.lower()`

These methods are used to change the case of characters in a string. `str.upper()` converts all characters to uppercase, and `str.lower()` converts them to lowercase. Example:

```python
text = "Python is FUN"
upper_text = text.upper()  # upper_text will be "PYTHON IS FUN"
lower_text = text.lower()  # lower_text will be "python is fun"
```

### 10. `chr()` and `ord()`

These functions deal with character encoding. `chr()` converts an integer to a character, and `ord()` converts a character to its integer representation. Example:

```python
character = 'A'
ascii_value = ord(character)    # ascii_value will be 65
char_from_ascii = chr(65)       # char_from_ascii will be 'A'
```

## Questions

{{ get_questions(page.title)}}

## Programming Tasks

{{ get_programming_tasks(page.title)}}