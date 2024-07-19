---
title: Functions
image: python.png
---

![](../../assets/images/topics/{{image}}){width="100"; align=right}

# {{ title }}

!!! note "Objectives"

    - Understand the concept of functions and procedures in Python.
    - Learn why functions are useful in programming.
    - Discover when and how to use functions.
    - Understand the roles of arguments and parameters in functions.
    - Practice writing and using functions with simple examples.

Most problems we encounter can be broken down in to a series of steps.  Earlier we saw the following series of steps to make a sandwich:

- Go to the kitchen.
- Open the refrigerator.
- Take out the bread, cheese, and lettuce.
- Put two slices of bread on a plate.
- Put some cheese and lettuce on one slice of bread.
- Put the other slice of bread on top.
- Close the sandwich.
- Bring it to me.

Here's we've **decomposed** the larger problem into a series of smaller problems each can be tackled on their own but when put together will result in a sandwich being made (hopefully).

Thinking of something we might want to compute, lets' take the simple example of calculating the area of a rectangle.  There might be three steps, or sub-problems, to solve before we have a working program:

- Get the length and the height values from the user
- Multiply those two values together to get the area
- Print the result to the screen

You could even break the first step into two steps, one for the length and one for the height.

Thus our main program might read as:

```py
def get_value():
    # function to get a value from the user

def calculate_area(length, height):
    # function to calculate the area of a rectangle

def print_result(result):
    # function to display the result to the screen

length = get_value()
height = get_value()
area = calculate_area(length, height)
print_result(area)
```

The term **main program** was used here.  Some languages specify the entry point for their programs to be in a function called `main()`.  We can replicate that behaviour here:

```py
def get_value():
    # function to get a value from the user

def calculate_area(length, height):
    # function to calculate the area of a rectangle

def print_result(result):
    # function to display the result to the screen

def main():
    length = get_value()
    height = get_value()
    area = calculate_area(length, height)
    print_result(area)

main()
```

We've decomposed our problem into a series of smaller, reusable, blocks of code that is responsible for a specific task. Our code follows a logical pattern and each section is more manageable and better organised.

The key steps of our algorithm are now in a `main()` function which is called as the entry point for our program.

Having determined this overall structure for our program we can then focus on each part in turn.  It's much easier to work on a small section of code like this rather than trying to tackle the whole thing in one go!  It also helps when/if we have errors.  It should be more obvious where the error is occurring, i.e. in which function, when following this approach rather than having to look through many lines of code.

So, using functions is a good thing, they provide many key benefits:

- **Modularity:** Divide your code into smaller, self-contained modules (functions) for easier development and debugging.
- **Reusability:** Write code once and use it multiple times, reducing duplication.
- **Readability:** Functions make code more understandable and concise.
- **Maintenance:** Changes are easier to implement and test within a function.

## Defining Functions

To create a function in Python, we use the `def` keyword, followed by the function name, pair of parentheses, `()`, followed by a colon, `:`. 

For example:

```python
def my_function():
    # Function body
    pass
```

!!! note

    The keyword `pass` is a statement that does not do anything.  It is useful when scaffolding code as in the previous example.  We know we want a function that calculates the area of a rectangle but are either unsure of how to complete this function or want to return to it later so we enter `pass`.  Our main program will still call that function but nothing will happen.

Similar to the naming of variables and constants, the name we give to our function should be self-documenting.  `calculate_area()` seems ok here, though we might want to be even more explicit as name it is `calculate_rectangle_area()` to distinguish it from another similar function such as `calculate_triangle_area()` or `calculate-circle_area()`.  It might take some more typing but will result in your code being easier to read and maintain.

The syntax required can be summarised as:

- **Function Name**: Descriptive and meaningful (follow naming conventions), the identifier for the function
- **Parentheses**: Used to pass arguments (inputs) to the function.
- **Colon**: Indicates the beginning of the function body.
- **Indentation**: All code inside the function must be indented.
- **Statement(s)**: The body of the function, statements that get executed every time the function is called.

## Procedures vs Functions

Look at how our functions are called in the main program:

```py
def main():
    length = get_value()
    height = get_value()
    area = calculate_area(length, height)
    print_result(area)
```

The statements in the first three lines are assignment statements.  An item of data is being returned from that block of code.  The fourth line is different, `print_result(area)` is a **procedure**.  `get_value()` and `calculate_area()` are **functions**.

What's the difference?  **Functions return a value, procedures do not**.

!!! warning

    This is not strictly true in Python, as a procedure will always return `None` when it is called, but we generally ignore this and it is not used.


To return a value from a function we use the `return` statement.  Here's how it might be used for our `get_value()` function:

~~~~~py
def get_value():
    print("Enter a value: ")    # prompt for a value
    value = int(input())        # cast the input to an integer
    return value                # return the input back to the main program
~~~~~

Similarly to calculate the area of the rectangle, the result is being returned:

~~~~~py
def calculate_area(length, height):
    return length * height
~~~~~

That return value needs to be stored somewhere, yes, in a variable: `area = calculate_area(length, height)`.

## Function Parameters and Arguments

In our `calculate_rectangle()` function we put the names of two variables inside the brackets:

~~~~~py
def calculate_area(length, height):
    pass
~~~~~

These variables are known as the **parameters** to the function.  In order to do this calculation we need to know the length and height of the rectangle. When this function is called Python will create two new variables called `length` and `height` and use them during the course of the function.  Once the function ends, these variables are destroyed.

In our `main()` program we called this function as `area = calculate_area(length, height)`.  Here we are passing two **arguments** to our function, the length and the height.  In this instance the identifiers used happen to be the same but we could have used different terms as the parameters and the program would still work:

~~~~~python
def calculate_area(rec_length, rec_height):
    return rec_length * rec_height)

length = 10
height = 5
area = calculate_area(length, height)
print(area)
~~~~~

![](../../assets/images/python/parameters.png)

Remember:

- **Parameters:** Variables declared in the function header.
- **Arguments:** Values passed to the function when it's called.

## Calling a function

To **call** a function we enter the name for the function and any arguments that need to be passed to the function from another part of our program.  The function call must come after the function definition in Python.

~~~~~python
def calculate_area(rec_length, rec_height):     # function definition
    return rec_length * rec_height)

length = 10
height = 5
area = calculate_area(length, height)           # function call
print(area)
~~~~~

## Default parameters

Consider the following example:

~~~~~python
def greet(name, message="Hello"):
    print(f"{message} {name})
~~~~~

Python allows for functions (and procedures) to have default arguments.  The procedure `greet()` can now be called with only one argument:

~~~~~python
greet("Sally")          # "Hello Sally"
~~~~~

Or we can override the default parameter replacing the default message with one of our own:

~~~~~python
greet("Sally", "Hi")    # "Hi Sally"
~~~~~

## Why bother with functions?

It can be a lot of trouble to organise your code into these blocks, functions, so why bother?  There are a number of good reasons:

- Providing a name for a group of statements that are responsible for a task will make the program easier to read and debug
- Using functions can eliminate the need to duplicate code.  One of the guiding rules of good programming style is the acronym **DRY**.  This stands for **Don't Repeat Yourself**
- With a long program decomposed into smaller chunks it becomes easier to locate where there might be a bug.  It can also be easier to start with a high level description (even as code) and then progressively break each of these down into as many functions as might be required.
- Well designed functions can be used in other programs.  Once its written and tested you can use it elsewhere.

## Keyword parameters

When you call a function, you usually pass values as arguments in the same order as the function's parameters are defined. However, sometimes it's more convenient to specify which argument corresponds to which parameter by using their names. These are called **keyword parameters**.

Let's say we have our simple function that calculates the area of a rectangle, we can call this function using keyword parameters:

~~~~~python
area = calculate_area(length=5, width=10)
~~~~~

The names of the parameters are explicitly mentioned with their values.  It makes the code more readable, especially when you have a function that takes in several arguments.  If the keyword parameter is used the order of the variables do not matter.

## Summary

Functions are fundamental to programming in Python. They promote code organization, reusability, and readability. As you continue your programming journey, you'll find that functions become an essential tool for solving complex problems efficiently.

## Questions

{{ get_questions(page.title)}}

## Programming Tasks

{{ get_programming_tasks(page.title)}}