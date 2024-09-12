---
title: Variables
image: python.png
filename: '_data/python_questions.json'
---

![](../../assets/images/topics/{{image}}){width="100"; align=right}

# {{ title }}

!!! note  "Objectives"
    - Understand the concept of variables and their role in programming.
    - Grasp the dynamic typing system in Python.
    - Follow Python's naming conventions when naming variables.
    - Learn how to display output using the print() function.
    - Know how to obtain and process user input.
    - How to check the data type of a variable.
    - Definition of a constant and how to use with Python
    - Gain practical experience by completing programming tasks related to variables and user input.

In the previous section we set up the Python environment and our IDE for writing Python programs.  Here we'll run through one of the key features for all programming languages, **variables** and **constants**.

## What is a program?

A program, in the context of computers and technology, is like a set of instructions that tells a computer what to do. It's a bit like giving directions to a friend, but instead of telling your friend how to get from one place to another, you're telling the computer how to perform specific tasks.

Imagine you have a robot, and you want that robot to make you a sandwich. You can't just tell the robot, "Make me a sandwich." The robot needs step-by-step instructions, like:

1. Go to the kitchen.
2. Open the refrigerator.
3. Take out the bread, cheese, and lettuce.
4. Put two slices of bread on a plate.
5. Put some cheese and lettuce on one slice of bread.
6. Put the other slice of bread on top.
7. Close the sandwich.
8. Bring it to me.

Each of these steps is like a line of code in a program. A program is a collection of these instructions that a computer can understand and follow to complete a specific task. The computer reads and executes these instructions in order, just like our robot friend follows the steps to make a sandwich. It's the language computers understand to perform the tasks we want them to do.

The syntax of the instructions will differ between programming languages but essentially all have the following components:

- **Input**: Get data from the keyboard, a file, the network, or some other device.
- **Output**: Display data on the screen, save it in a file, send it over the network, etc.
- **Mathematical and logical operators**: To perform basic mathematical operations like addition and multiplication and logical operations such as AND, OR and NOT.
- **conditional execution**: Check for certain conditions and run the appropriate code.
- **Repetition**: Perform some action repeatedly, usually with some variation.

Every program you've ever run will be made up of these type of instructions and these will be explored in this and subsequent sections.

## Example 1:

```python
# Example 1
name = "Alice"
age = 21
PI = 3.14

print("Name:", name)
print("Age:", age)
print("PI:", PI)

user_input = input("Enter something: ")
print("You entered:", user_input)
print("Data type of user input:", type(user_input))
```

Read the code and predict what will happen when we run this program, in particular:

- line 1: What will be stored in the variable `name`?
- line 6: What do you think `print("Age:", age)` will display?
- line 9: What will happen when the program reaches this line?"
- line 11: What is the purpose of `type(user_input)`?

Copy the code into your text editor, run the code to see if your were right!

## Variables

In the example program, line 1 assigns the value "Alice" to a **variable** named `name`.

A variable is a foundational concept for all programming languages.  It is a container, or a label, used to store data in our programs.  Lines 2 and 3 assign further variables named `age` and `pi`.

During the course of a program it is likely the value of that data item will change, it varies, hence it is known as a __variable__.

```python hl_lines="2 3 4"
# Example 1
name = "Alice"
age = 21
PI = 3.14

print("Name:", name)
print("Age:", age)
print("PI:", PI)

user_input = input("Enter something: ")
print("You entered:", user_input)
print("Data type of user input:", type(user_input))
```
The opening lines of our program assigns data to three different variables, they contain a different **type** of data:

| line | identifier | value | type |
|------|------------|-------|------|
|  1   |  `name`     | "Alice" | string |
| 2    |  `age`      | 21 | integer |
| 3     | `PI`      | 3.14 | float |

Python knows about four primitive types of data:

- **Int**eger: whole numbers, positive and negative
- **Float**ing point numbers: a real number with a decimal point and fractional component
- **Bool**ean: either true or false
- **Str**ing: any set of characters

!!! note "Comments"
    A comment is text in your code that will be ignored by the Python interpreter. Comments can be on a single line when preceded by the `#` symbol:
    
    ```py
    # This is a comment, and will be ignored by the interpreter
    ```

It's important to recognise the difference between these different **data-types**.  In some programming languages you have to declare the type of data that is expected in a variable, this is known as **static data typing**, and it is fixed before the code is compiled.  For example in C# you would declare these variables as:

```cs
string name = "Simon";
int age = 34;
bool plays_piano = true;
float hourly_rate = 34.99;
```

Python takes a different approach.  It is a **dynamically typed** language.  This means the value assigned to the variable will determine the data type for that variable as the program is running.  So the data type of the variable is determined by the value it holds.

### Identifiers

The names, or **identifiers**, for each helps to describe the data they each contain.  We could have named them as follows:

```py
a = "Alice"
b = 21
c = 3.14
```

But, the name `a` does not tell the reader anything about the data being stored in the variablae named `a`.  The name given to the variable should be descriptive of the item of data contained there so it makes sense when you, or others, read your code.  This makes the code easier to read and understand.

!!! tip 
    When giving a name to a variable, think carefully about what to use.  Make if descriptive of the data being stored in the variable.

There are guidelines/rules for naming variables but for now remember they must not start with a digit, nor can they use another term used as a __keyword__ in the language.  Python allows for underscores to be used in variable names e.g. `is_student` but **not** the hyphen e.g. `is-student`.  

Finally, variable names are case-sensitive, so `age` is different to `Age`.

!!! info "Python Keywords"
    **Python keywords** 

    `and`, `as`, `assert`, `break`, `class`, `continue`, `def`, `del`, `elif`, `else`, `except`, `finally`, `for`, `from`, `global`, `if`, `import`, `in`, `is`, `lambda`, `nonlocal`, `not`, `or`, `pass`, `raise`, `return`, `try`, `while`, `with`, `yield`.  
    
    None of these can be used as the name for a variable. To see the latest set of keyboards enter ```print(keyword.kwlist)``` in the interactive environment.

### Naming style for variables

Python has a style for naming of variables.  When an identifier is made up of multiple words separate each word with an underscore:

```py
is_student = True
cumulative_sum_of_numbers = 50
```

!!! info
    This naming style is called "snake-case".  There is extensive documentation for how to write Python code, a style guide known as **PEP8**.  You can read about PEP8 here [https://pep8.org](https://pep8.org)

Values are assigned to variables using the **assignment operator**: `=`, as shown in the examples above.  Variables can be re-assigned with new values thus their value can change during the course of the program.  This is why they are called variables.

```python hl_lines="5"
# Example 1
name = "Alice"
age = 21
PI = 3.14
name = "Imran"  # the value of name has been changed
```

Note the assignment operator: `=`.  It's important not to confuse this with the mathematical symbol for "equals".  Try to get into the habit when reading code and encountering e.g. ```age = 42``` to say "age *is assigned* the value 42".  Also make sure you get it the right way round, ```42 = age``` will not work!

## Simple Output

```python hl_lines="6 7 8"
# Example 1
name = "Alice"
age = 21
PI = 3.14

print("Name:", name)
print("Age:", age)
print("PI:", PI)

user_input = input("Enter something: ")
print("You entered:", user_input)
print("Data type of user input:", type(user_input))
```

To get data displayed on the screen we use the `print()` function.  On it's own this command will just print a new empty line, but elements, or more formally **arguments**, can be placed inside the brackets.  These arguments will then be displayed on the screen.  

Having declared and initialised the three variables, we make successive calls to `print()` passing in a different variable each time to display the values of each variable.

## Getting input from the user

```python hl_lines="10"
# Example 1
name = "Alice"
age = 21
PI = 3.14

print("Name:", name)
print("Age:", age)
print("PI:", PI)

user_input = input("Enter something: ")
print("You entered:", user_input)
print("Data type of user input:", type(user_input))
```

Assigning data to a variable can be hard-coded in your program or obtained externally such as a user entering data at the keyboard.

To get data from our user we call the `input()` function, line 11

This function displays the string in brackets and waits for user to type something, this is then assigned to a variable, here named `user_input`.

### All data entered from the keyboard is a string

The data type of the input from the keyboard will always be a string so if we need that data to behave as a integer, a float or some other type then it will need to be **cast** to that type using the appropriate function.  For example, the following will generate an error as we are trying to subtract $1$ from the string entered by the user.  You cannot subtract $1$ from, say, "15"!

~~~~~py
age = input('Enter you age: ")
age = age - 1                   # this generates an error!
~~~~~

Instead, we have to **cast** it to an integer:

~~~~~py
age = input("Enter your age: ")
age = int(age)
age = age - 1
~~~~~

This will work, though it can be shortened by wrapping the `int()` function around the `input()`:

~~~~~py
age = int(input("Enter your age: "))
age = age + 1
~~~~~

- To convert the input to a float i.e. a number with a decimal point such as $3.14$, use the `float()` function.

- To convert a numeric value to a string using the `str()` function,

### Checking the data type

```python hl_lines="12"
# Example 1
name = "Alice"
age = 21
PI = 3.14

print("Name:", name)
print("Age:", age)
print("PI:", PI)

user_input = input("Enter something: ")
print("You entered:", user_input)
print("Data type of user input:", type(user_input))
```

If you want to check the type of data held by a variable we can use the `type()` function:

In line 12 we print to the screen the data type of `user_input`.  It will, of course, be a string.

## Constants

```python hl_lines="4"
# Example 1
name = "Alice"
age = 21
PI = 3.14

print("Name:", name)
print("Age:", age)
print("PI:", PI)

user_input = input("Enter something: ")
print("You entered:", user_input)
print("Data type of user input:", type(user_input))
```

The data on line 4, for the value of pi ($\pi$) should not be changed.  It's value should remain the same.  We call it a **constant**.

Like a variable a **constant** is a name given to an item of data.  The difference is the value of that item should not change throughout the course of the program.  

!!! warning
    Unlike other programming languages Python does not have a strict syntax for constants - this is unfortunate.  To get round this we simply declare our constants using upper case identifiers.  Yes, you might make a mistake and inadvertently reassign that constant value but if you stick to the convention it should be obvious that the data item is to be treated as a constant value rather than a variable.

## Formal vs natural languages

When we think of a language we probably think of the language people speak be that English, French or arabic etc..  These are known as **natural languages**, no-one sat down and designed the language, they have evolved naturally over time (and are continuing to evolve).

A **formal language** is a language that has been designed by people to be used in specific circumstances e.g. mathematical expressions and notation or chemical symbols to denote the molecular structure of different chemicals.  Similarly programming languages in computer science.  

These formal languages have a strict syntax relating to the **tokens** of the language and how they can be organised.  For example, in mathematical notation $4 + 7 = 11$ combines five tokens of the language into a meaningful expression.  By contrast, $4 += 7$ does not!  The tokens might be valid but the rules do not permit one operator to follow another in this way.  It is a **syntax error**.

## The Python interpreter

Python is an **interpreted language**.  This means it does not produce a separate executable file but works its way through your code file and executing it on the fly.  

!!! Warning "The Python Interpreter"

    How Python works through the code you write and produces the output is a complicated process and not required for the GCSE - you might like to return to this section at another time.  But, do remember Python is an **interpreted language**.

First, Python (the interpreter) will analyse your code and check it for any syntax errors and make sure the rules for indentation have been followed correctly.  It carries out a **lexical analysis** and the divides the source code into a number of **tokens** which are passed to the **parser** which generates the **Abstract Syntax Tree** (AST). The AST is converted into **byte codes** which can then be saved to a file with a `.pyc` extension.

Next, the Python interpreter will launch its **Python Virtual Machine** (PVM) which converts the byte codes into the binary data required by the target computer.  This way, your Python code will run on Windows, Linux or MacOS.

Some programming languages will, by default, produce a compiled executable which, on Windows, will be a file with the `.exe` extension.  This means you can create your program and distribute the `.exe` for another user to run.  This file will only be compatible for the target platform e.g. Windows, or MacOS.  To distribute your Python program you need to provide the code and your user will have to have Python installed on their machine to run your code.

## Climate Quest Project

![](../../assets/images/climate-quest.png){align=left width="200"}

Throughout this topic we'll be working on a large scale project: **Climate Quest**.  In this project a player embarks on a journey to combat the effects of climate change by making decisions that impact the environment. Each choice affects the outcome of the game, emphasizing the importance of individual actions in addressing climate change.

[Go to task 1 - Declaring variables](./climate_quest/task_1.md){:class=md-button}

## Questions

{{ show_questions(page.title, page.meta.filename) }}


## Extra Programming Tasks

{{ get_programming_tasks(page.title)}}
<!-- ## Questions

1. What is a variable, and why is it important in programming?

2. Explain the difference between a variable and a constant.

3. Python is a dynamically typed language. What does this mean in terms of variable declaration and data types?

4. What are the four primitive data types in Python mentioned in the notes?

5. What are the rules for naming variables in Python?

6. Why is it essential to choose descriptive variable names in your code?

7. What is the purpose of casting in Python, and how is it done?

8. How can you check the data type of a variable in Python?

9. What is the Pythonic style for naming variables with multiple words?

10. What is PEP8, and why is it important in Python programming?
 -->
