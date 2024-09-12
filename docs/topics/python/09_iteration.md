---
title: Iteration
image: python.png
filename: '_data/python_questions.json'
---

![](../../assets/images/topics/{{image}}){width="100"; align=right}

# {{ title}}

!!! note "Objectives"

    - Define iteration in programming and its importance.
    - Recognize the concept of loops as a fundamental element of iteration.
    - Differentiate between for and while loops in Python.
    - Explain when to use a for loop and when to use a while loop.
    - Describe the purpose of the `range()` function in for loops.
    - Illustrate the use of for loops to iterate over sequences like lists, tuples, and strings.
    - Explain the concept of nested for loops, and demonstrate the use of nested for loops with examples.
    - Understand the structure of a while loop in Python.
    - Compare and contrast for loops and while loops.

Iteration is a fundamental concept in programming that allows you to execute a block of code repeatedly. Think of "iteration" is a word that simply means "loop", doing something over and over again.  

Iteration allows certain sections of our program to be repeated.  We just have to be careful not repeat these statements for ever!

Consider, if wanted to print a list of all values between 1 and 10 we could do the following:

```py
print(1)
print(2)
print(3)
print(4)
print(5)
# etc..
```

Clearly this gets tedious and the loop constructs in Python makes this so much easier.

## Example 7

```python hl_lines="3 8"

# Example program with for and while loops
print("Counting using for loop:")
for i in range(1, 6):
    print(i)

print("\nCounting using while loop:")
count = 1
while count < 6:
    print(count)
    count += 1
```

Predict what the output of the program will be for the following:

- What will be printed by the `for` loop?
- What will be printed by the `while` loop?

Run the program in a Python environment and compare the actual output with your predictions.

Python provides two main types of loops: `for` and `while` loops.

## The `for` loop

A `for` loop is sometimes call **a counted loop** because, simply, it repeats a set number of times effectively counting as it goes.  For this we need to provide a starting value and a stopping value:

```py
for i in range(1,11):
    print(i)            # print values from 1 to 10
```

The `range()` function generates a sequence of numbers.  In this example, the `range()` function has two arguments, the first is the start value, $1$, the second is the stop value, $11$.  Why $11$?  This may seem confusing at first but it means that when the control variable, `i`, has the value $11$ the loop will end and the following `print()` statement will not be executed.

There are two variations on the `range()` function:

- `for i in range(10)`: only the stop value has been specified.  The start value defaults to $0$.
- `for i in range(1,20,2)`: an additional parameter, a skip value.  Here `i` will start with $1$ and when the loop is repeated the skip value is added making $3$ and the $5$ and so on.

A `for` loop can also used to iterate over a sequence (such as a list, tuple, string) and execute a block of code for each item in the sequence.

!!! note 

    We've not yet met lists but they are useful when we have a collection of items that share a common name e.g. `colours = ["red", "brown", "white", "black]`.  A `for` loop is excellent for moving over each of the items in the list.

```python
colours = ["red", "brown", "white", "black"]
for item in colours:
    print(item)
```

A `string` is actually a list of characters.  Try the following code in your IDE:

```py
phrase = "Hello, World!"
for ch in phrase:
    print(ch)
```

## Nested `for` Loops

A loop can be placed inside another loop:

```py
for i in range(0,2):
    for j in range(1,3):
        print(i, j)
```

This will output:

```py
0 1
0 2
1 1
1 2
```

Check that you understand why this output is as it is.

## The `while` Loop

Python offers an alternative construct for iteration, the **conditional** loop.  This uses the keyboard `while` and the code in this loop will execute as long as a specified condition is `True`.  It can be a little more tricky to handle than the `for` loop as we, the programmer, have to control how many times the loop will execute.  

```python
i = 1
while i <= 10:
    print(i)
    i = i + 1
```

- We need to give the control variable an initial value, `i = 1`.
- The condition is checked using a relational operator against our desired stop value.
- The control variable needs to be updated in the body of the loop

The `for` loop and the `while` loop are interchangeable, it matters little which you use as long you keep the logic correct.  Sometimes it is just a matter of personal preference.

!!! note 

    The `while` loop is also known as a **top-tested loop** as the condition is placed at the top of the loop and if that condition is not satisfied  it may never be executed.  An alternative form is the `do ... while` or `repeat ... until` loops.  These are bottom-tested loop constructs.  the condition comes at the bottom of the loop so the code in the loop will be executed at least once.  Python does not have a bottom-tested loop but you will encounter it in other programming languages.

## Examples

### Example 1: `for` Loop
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")
```

### Example 2: `while` Loop
```python
count = 1
while count <= 5:
    print(f"Count: {count}")
    count += 1
```

## Activity

Using the following program, amend the code to:

- change the range of the multiplication table
- iterate over a list of numbers rather than a string
- use a while loop to count from 1 through to 5
- amend the while loop to print all the even numbers between 1 and 100

```python
# Modified example with nested loops and sequence iteration
print("Multiplication table using nested for loops:")
for i in range(1, 4):
    for j in range(1, 4):
        print(i * j, end=' ')
    print()

print("\nIterating over a string with for loop:")
text = "Python"
for char in text:
    print(char)

print("\nCounting down using while loop:")
count = 5
while count > 0:
    print(count)
    count -= 1
```
## Climate Quest Project

![](../../assets/images/climate-quest.png){align=left width="200"}

Throughout this topic we'll be working on a large scale project: **Climate Quest**.  In this project a player embarks on a journey to combat the effects of climate change by making decisions that impact the environment. Each choice affects the outcome of the game, emphasizing the importance of individual actions in addressing climate change.

[Go to task 7 - Iteration](./climate_quest/task_7.md){:class=md-button}

## Summary

[Cheat sheet for iteration (and selection)](../../files/beginners_python_cheat_sheet_pcc_if_while.pdf){:class=md-button}[^source]

[^source]: [https://ehmatthes.github.io/pcc_3e/cheat_sheets/(https://ehmatthes.github.io/pcc_3e/cheat_sheets/)]

## Questions

{{ show_questions(page.title, page.meta.filename) }}

## Programming Tasks

{{ get_programming_tasks(page.title)}}