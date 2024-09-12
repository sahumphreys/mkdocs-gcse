---
title: Selection
image: python.png
filename: '_data/python_questions.json'
---

![](../../assets/images/topics/{{image}}){width="100"; align=right}

# {{ title}}

!!! note  "Objectives"

    - To understanding selection in algorithms and code
    - Define the purpose of selection (conditional statements) in programming.
    - Learn the syntax of `if`, `elif`, and `else` statements in Python
    - List and explain the relational operators used in conditions (e.g., ==, !=, >, <, >=, <=).
    - Review examples of Conditional Statements
    - Define the role of the `elif` statement in handling multiple conditions.
    - Differentiate the use of `elif` from `if` and `else`.

## Introduction

As part of our algorithm we will often encounter a moment when a decision needs to be taken, and depending on the outcome of that decision, either `True` or `False`, execute a different statement or set of statements. In Python, we use `if`, `elif` (else if), and `else` statements to implement selection.  We also rely on the relational operators covered earlier i.e. `==`, `!=`, `>` etc..

```python
if True
    do something
else
    do this instead
```

## Example 6

```python
print("Welcome to the Climate Data Analyzer")

temperature = float(input("Enter the temperature in Celsius: "))

if temperature < 0:
    print("It's freezing cold!")
elif temperature >= 0 and temperature <= 20:
    print("The weather is cool.")
elif temperature > 20 and temperature <= 30:
    print("The weather is warm.")
else:
    print("It's hot outside!")
```

Predict what the output of the program will be for these inputs:

- "What will the program print if the temperature is -5?"
- "What will the program print if the temperature is 15?"
- "What will the program print if the temperature is 25?"
- "What will the program print if the temperature is 35?"

Run the program in a Python environment and compare the actual output with your predictions.


## 1. The `if` Statement
The `if` statement allows you to execute a block of code only if a specified condition is true.

```python
if condition:
    # code to execute if condition is true
```

## 2. The `elif` Statement
The `elif` statement is used when you have multiple conditions to check. It is executed if the preceding `if` or `elif` conditions are false and its own condition is true.

```python
if condition1:
    # code to execute if condition1 is true
elif condition2:
    # code to execute if condition2 is true
```

!!! note

    It makes sense to read `elif` as "**else if**"


## 3. The `else` Statement
The `else` statement is used as a fallback option if none of the preceding conditions are true.

```python
if condition:
    # code to execute if condition is true
else:
    # code to execute if condition is false
```

## 4. Conditions

The condition will always be some kind of Boolean expression that evaluates to either `True` or `False` and will use the relational operators we saw earlier:

1. **Equal to (`==`):** Checks if two values are equal.

2. **Not equal to (`!=`):** Checks if two values are not equal.

3. **Greater than (`>`):** Checks if one value is greater than another.

4. **Less than (`<`):** Checks if one value is less than another.

5. **Greater than or equal to (`>=`):** Checks if one value is greater than or equal to another.

6. **Less than or equal to (`<=`):** Checks if one value is less than or equal to another.

These conditions can be further combined using `and`, `or` and `not` to create complex conditional expressions.

## Further Examples

### Example 1: Basic `if` Statement

```python
age = 16
if age >= 18:
    print("You can vote!")
```

### Example 2: `if-elif-else` Statement

```python
score = 85
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("C")
```

## Activity

Using the following program, make the changes suggested:
```python
print("Welcome to the Advanced Climate Data Analyzer")

temperature = float(input("Enter the temperature in Celsius: "))
humidity = int(input("Enter the humidity percentage: "))

if temperature < 0:
    print("It's freezing cold!")
elif temperature >= 0 and temperature <= 20:
    if humidity > 80:
        print("The weather is cool and humid.")
    else:
        print("The weather is cool.")
elif temperature > 20 and temperature <= 30:
    if humidity > 60:
        print("The weather is warm and humid.")
    else:
        print("The weather is warm.")
else:
    if humidity > 40:
        print("It's hot and humid outside!")
    else:
        print("It's hot outside!")
```

- Add a new condition for temperatures above 35 degrees.
- Change the humidity thresholds and observe the different outputs.

## Climate Quest Project

![](../../assets/images/climate-quest.png){align=left width="200"}

Throughout this topic we'll be working on a large scale project: **Climate Quest**.  In this project a player embarks on a journey to combat the effects of climate change by making decisions that impact the environment. Each choice affects the outcome of the game, emphasizing the importance of individual actions in addressing climate change.

[Go to task 6 - Selection](./climate_quest/task_6.md){:class=md-button}

## Summary

[Cheat sheet for selection (and iteration)](../../files/beginners_python_cheat_sheet_pcc_if_while.pdf){:class=md-button}[^source]

[^source]: [https://ehmatthes.github.io/pcc_3e/cheat_sheets/(https://ehmatthes.github.io/pcc_3e/cheat_sheets/)]


## Questions

{{ show_questions(page.title, page.meta.filename) }}

## Programming Tasks

{{ get_programming_tasks(page.title)}}