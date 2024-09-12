---
title: Strings
image: python.png
filename: '_data/python_questions.json'
---

![](../../assets/images/topics/{{image}}){width="100"; align=right}

# {{ title }}

!!! note "Objectives"
    - Understand the nature and importance of strings as a fundamental data type in Python.
    - Know how to create, manipulate, and format strings using various techniques.
    - Be aware of common string methods and their applications.
    - Know how to effectively index, slice, and find the length of strings.
    - Understand the concept of string immutability.
    - Gain practical experience through programming tasks related to strings.


Earlier we saw how Python works with **variables** and the data stored in the variable will be of a particular type of data i.e. integers (whole numbers), reals (numbers with a fractional part), characters (e.g. 'a', '5') and boolean (either true or false).  In this section we look at **strings**.

A string is a list of characters, a character being anything that you type on the keyboard in one keystroke e.g. a letter, a number or a symbol, including ++space++.

## Example 3:

Read the following program, and predict what the program will do.  

```python hl_lines="4 7 10 13 16 19"
greeting = "Hello, "
name = "Alice"
full_greeting = greeting + name
print("Full Greeting:", full_greeting)

shout = full_greeting.upper()
print("Shout:", shout)

whisper = full_greeting.lower()
print("Whisper:", whisper)

length = len(full_greeting)
print("Length of Full Greeting:", length)

first_letter = name[0]
print("First Letter of Name:", first_letter)

sliced_name = name[1:4]
print("Sliced Name:", sliced_name)
```

Pay particular attention to the highlighted lines.  What will be displayed on the screen when these lines are executed?

??? hint "Answers"

  - Full Greeting: Hello  Alice 
  - Shout: HELLO, ALICE 
  - Whisper: hello, alice 
  - Length of Full Greeting: 12 
  - First Letter of Name: 
  - A Sliced Name: lic

Copy the code and paste into a code editor and run the code to compare your predictions with the actual results.

## What are Strings?

- In Python, a **string** is a data type used to represent text.
- Text can be anything from a single character to a whole paragraph.
- Strings are a fundamental data type in programming and are used extensively in real-world applications.
- A string is a **list of characters**

## Creating Strings

- Strings are created by enclosing text in either single quotes (`'`) or double quotes (`"`).
- For example:
  - `'Hello, World!'`
  - `"Python is fun"`

!!! warning
    The type of quotation mark used must be consistent e.g. `'Hello, World!"` is incorrect, the quotes do not match 

- to include a quotation mark within a string, use the other one!  For example:

```python
message = "I don't like Mondays!"
```

## String Operations

Two of the operators we saw being used as mathematical operators are repurposed when applied to string operands:

### Concatenation

- You can combine two or more strings using the **concatenation operator** (`+`).
- Example:
  
  - `'Hello' + ' ' + 'World'` results in `'Hello World'`.

### Repetition

- You can repeat a string multiple times using the **repetition operator** (`*`).
- Example:
  - `'Python' * 3` results in `'PythonPythonPython'`.


## String Methods

- Python provides many built-in **string methods** that allow you to manipulate and work with strings effectively.
- Some common string methods include `upper()`, `lower()`, `len()`, `strip()`, `split()`, and `replace()`.
- Example:
  - `"Python".upper()` results in `'PYTHON'`.
- When using these do not forget the brackets after the method name, these are function calls and must have the brackets
- To find characters in a string, use the `find()` method.  This returns the index of the first occurrence of that character.  
- For example:
  
```python
course = "Python for beginners"
course.find('P')                    # returns 0
course.find('for')                  # returns 7
course.find('Beg')                  # returns -1, it is case sensitive
```
- To replace a character, or a sequence of characters use `replace()` e.g. `course.replace('Python', 'Java')`
- To check for the existence of characters in a string, use `print('Python' in course)`.  This method will returns a boolean value and line `find()` is case-sensitive.

## String Indexing

- Each character in a string has a unique **index** starting from `0`.
- You can access individual characters in a string using square brackets and the index.
- Example:
  - `"Python"[0]` returns `'P'`.
  - `"Python"[2]` returns `'t'`.

## String Slicing

- **String slicing** allows you to extract a portion of a string.
- It is done by specifying a **range** of indices inside square brackets.
- For example:

```py exec="on" source="console"
course = "Python"
print(course[0])            # 'P'
print(course[-1])           # 'n'
print(course[0:3])          # 'Pyt' nb. does not print course[3] the 4th char
print(course[0:])           # all the characters!
```

## String Length

- You can find the length of a string using the `len()` function.
- Example:
  - `len("Hello, World!")` returns `13`.

## Escape Characters

- Some characters have special meanings in strings, such as newline (`\n`) and tab (`\t`).
- To include these characters in a string, you need to use **escape sequences**.
- Example:
  - `"Hello\nWorld"` creates a string with a newline character.

## Multiline Strings

- You can create multiline strings by enclosing them in triple quotes (`'''` or `"""`).
- Useful for long text or preserving the formatting of text.
- Example:
  
```py
multiline_text = '''
This is a multiline
string in Python.
'''
```

## Printing strings

Python provides three different ways to print the contents of the string to the screen:

Compare the following:

```python
first = "Imran"
second = "Khalisa"
print(first + second)       # concatenation operator
print(first, second)        # comma operator, inserts a space between items
print(f"{first} {second}")  # f-string
```

It makes little different which you choose to use but notice the concatenation operator does not insert a space between items being printed.

## String Immutability

- Strings in Python are **immutable**, which means their values cannot be changed after creation.
- Any operation that seems to modify a string actually creates a new string.
- Example:
  - `text = "Hello"`
  - `new_text = text + ", World!"`

**Activity** 

Modify the given example by:

- Changing the variable values and observe the output.
- Adding more string manipulations using different methods.
- Experimenting with slicing to extract different parts of the string.

## Climate Quest Project

![](../../assets/images/climate-quest.png){align=left width="200"}

Throughout this topic we'll be working on a large scale project: **Climate Quest**.  In this project a player embarks on a journey to combat the effects of climate change by making decisions that impact the environment. Each choice affects the outcome of the game, emphasizing the importance of individual actions in addressing climate change.

[Go to task 3 - String Handling](./climate_quest/task_3.md){:class=md-button}




## Questions

{{ show_questions(page.title, page.meta.filename) }}

## Programming Tasks

{{ get_programming_tasks(page.title)}}