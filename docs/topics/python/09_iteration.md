---
title: Iteration
image: python.png
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

Python provides two main types of loops: `for` and `while` loops.

## 1. `for` Loops

A `for` loop is sometimes call **a counted loop** because, simply, it repeats a set number of times effectively counting as it goes.  For this we need to provide a starting value and a stopping value:

```py
for i in range(1,11):
    print(i)
```

Using the `range()` function we specify the start value as $1$ and the stop value as $11$.  Why $11$?  This may seem confusing at first but it means that when the control variable, `i`, has the value $11$ the loop will end and the following `print()` statement will noy be executed.

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

## 2. Nested `for` Loops

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

## 3. `while` Loops

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

## Questions

{{ get_questions(page.title)}}

## Programming Tasks

{{ get_programming_tasks(page.title)}}