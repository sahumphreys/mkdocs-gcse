---
title: Operators
image: python.png
filename: '_data/python_questions.json'
---

![](../../assets/images/topics/{{image}}){width="100"; align=right}

# {{ title }}

!!! note "Objectives"

    - Understand the use and application of the assignment operator
    - Use mathematical operators (+, -, *, /, %, //) for simple calculations
    - Learn how to use the augmented assignment operators
    - Be able to construct expressions, applying operator precedence
    - Understand and use logical operators (and, or, not) in Python.
    - Understand the role and use of comparison Operators (==, !=, >, <, >=, <=)
    - Build expressions combining logical and comparison operators
    - Apply parentheses to modify the evaluation order of logical expressions.


In this section we will look at the different **operators** we can use when programming with Python.  An operator is a character, or characters that will carry out a function on its operands.

The concept will be familiar from using basic arithmetic operators such as `+` or `-` to add two numbers together or subtract two numbers.  The `+` is known as an operator, and the numbers being added are the operands.

Programming languages have a number of types of operators:

- **Mathematical operators**
- **comparison operators**
- **logical operators**

One other is the **assignment operator** (`=`) that we used in the previous section.

## Example 2

Review the following program:

```python hl_lines="4 7 10 13 16"
a = 10
b = 5
result = a + b * 2
print("Result 1:", result)

result = (a + b) * 2
print("Result 2:", result)

result = a // b
print("Result 3:", result)

is_greater = a > b
print("Is a greater than b?", is_greater)

logical_test = (a > b) and (a < 20)
print("Logical test:", logical_test)
```

Here there are a number of these operators being used.  Read the code and predict what will be printed to the screen when the highlighted lines are executed.

??? hint "Answers"
   
    - Result 1: 20 
    - Result 2: 30 
    - Result 3: 2 
    - Is a greater than b? True 
    - Logical test: True

Copy the code and paste into a code editor and run the code to compare your predictions with the actual results.

Compare lines 4 and lines 7.  Why is the result different?

The following sections summarise the behaviour of each type of operator that we use when programming.

## Assignment Operator

We've already seen this being used.  It is the equals sign, `=`, but as we noted before we read it as "is assigned to".  

We can practice its use with the interactive environment:

```py
>>> name = "Simon"
>>> age = 42
```

When reading this code say: "Simon is as assigned to the variable `name`"  and "42 is assigned to the variable `age`".  The computer will then store this value in its memory and they can then be referred to by using their name, or **identifier**:

```py
>>> print(name, age)
Simon 42
```

## Mathematical operators

The mathematical operators are the same we have in maths, noting the use of `/` for division and `*` for multiplication:

- Addition: `+`
- Subtraction: `-`
- Division: `/`
- Multiplication: `*`

| Operator | Description | Example | Result |
|:---------:|-------------|:-------:|:------:|
| + | Addition | `7 + 3`  | 10 |
| - | Subtraction | `7 - 3` | 4 |
| - | Multiplication | `7 * 3` | 21 |
| / | Division | `7 / 3` | 2.33333.. |

!!! note 

    When two integers are divided, the result is a real (floating point number)

There is also a pair of integer division operators: 

| Operator | Description | Example | Result |
|:---------:|-------------|:-------:|:------:|
| // | Floor division | `7 // 3`  | 2 |
| % | Modulo (Remainder) | `7 % 3` | 1 |

Try both of these in the interactive environment to confirm results.

If we think of an example of wanting to know how many hours and minutes for a movie that lasts 138 minutes.  We can get the hours by using the integer division operator: `hours = minutes // 60`.  This automatically rounds down.  We can get the remainder too: `remainder = minutes - (hours * 60)`.  But this is the same as using the modulo operator: `remainder = minutes % 60`.

The modulo operator is also really useful when checking if one divides equally into another.  For example: `if x % 2 == 0`, then we know if the number (`x`) is odd or even.

Finally, exponent operator, `**`:

| Operator | Description | Example | Result |
|:---------:|-------------|:-------:|:------:|
| ** | Exponent | `7 ** 3`  | 343 |

### Augmented assignment operators

The following expression is often used where the value of a variable is being incremented by a given amount:

```py
x = x + 1
```

Here we can use a shorthand form (sometimes called syntactic sugar):

```py
x += 1              # the same as x = x + 1
```

Any of the mathematical operators can be used in this way.

```python
# Initial assignment
x = 10
print(x)            # output: 10
 
# Augmented assignment operator: subtraction
x -= 2
print(x)            # output: 8
 
# Augmented assignment operator: multiplication
x *= 3
print(x)            # output: 24
```
It does not matter which you prefer to use but the shorter form takes a little less typing.

### Operator precedence

There should be no surprises here, at least initially:

- exponentiation
- multiplication or division
- addition or subtraction

As in maths any brackets take priority, so these can be used to alter the order of precedence

## Comparison operators

Comparison operators in Python are used to compare two values or expressions and produce Boolean results (`True` or `False`). These operators allow you to check conditions and make decisions based on the results of these comparisons. They are usually used as part of selection and iteration structures which we'll meet later.

Python provides several comparison operators:


| Operator | Description | Example | Result |
|:---------:|-------------|:-------:|:------:|
| `==` | Equal to | `7 == 7` | True |
| `!=` | Not Equal to | `7 != 6` | True |
| `>` | Greater than | `7 > 6` | True |
| `<` | Less than | `7 < 6` | False |
| `>=` | Greater than or equal to | `7 >= 7` | True |
| `<=` | Less than or equal to | `7 <= 7` | True |

!!! warning

    Pay attention to the "is equal to" operator ( == ), it's two equal signs. It’s easy to mistake it for the assignment operator ( = ).  It helps to read the assignment operator as e.g. "age is assigned the value 18" for `age = 18`; and "is age equal to 18" for `age == 18`.

## Logical operators

Logical operators in Python allow us to combine logical operations on one or more **Boolean** values (`True` or `False`). These operators are used to make decisions and control the flow of a program based on those conditions. They are often referred to as Boolean operators.

Python provides three main logical operators:

| Operator | Description | Example | Result |
|:---------:|-------------|:-------:|:------:|
| `and` | Returns `True` only if **all** the boolean values are true | (7 > 6) and (4 < 8)| True|
| `or` | Returns `True` if **at least one** of the boolean values are true | (10 < 20) or (10 < 5)| True |
| `not` | Returns `True` if the value is false; returns `False if the value is true| not(7 > 6) | False|

### Logical Operator Examples

Let's explore these logical operators with some examples, you can try these in the interactive environment:

**1. AND Operator (`and`)**

The `and` operator returns True only if both conditions are True.

```py
>>> x = True
>>> y = False
>>> x and y
False
```

**2. OR Operator (`or`)**

The `or` operator returns True if at least one condition is True.

```py
>>> a = True
>>> b = False
>>> a or b
True
```

**3. NOT Operator (`not`)**

The `not` operator negates the Boolean value.

```py
>>> p = True
>>> not p
False
```

### Combining Logical Operators

You can combine logical operators to create more complex conditions:

```python exec="on" source="material-block"
age = 25
is_student = False

if age >= 18 and not is_student:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
```

In this example, the `and` operator is used to check if the age is greater than or equal to 18, and the `not` operator is used to check if the person is not a student.

### Precedence of Logical Operators

Logical operators have a specific order of precedence: `not` has the highest precedence, followed by `and`, and then `or`. You can use parentheses to change the order of evaluation if needed.

```python
result = (True or False) and (not True)
```

### Common Use Cases

Logical operators are commonly used in programming for various purposes, such as:

- **Conditional Statements:** To make decisions and control the flow of a program using `if`, `elif`, and `else` statements.
- **Loop Control:** To control the execution of loops, such as `while` and `for` loops.
- **Filtering Data:** To filter data based on specific conditions.
- **Searching and Validation:** To search for specific values in data and validate user input.


## Climate Quest Project

![](../../assets/images/climate-quest.png){align=left width="200"}

Throughout this topic we'll be working on a large scale project: **Climate Quest**.  In this project a player embarks on a journey to combat the effects of climate change by making decisions that impact the environment. Each choice affects the outcome of the game, emphasizing the importance of individual actions in addressing climate change.

[Go to task 2 - Using Operators](./climate_quest/task_2.md){:class=md-button}

## Questions

{{ show_questions(page.title, page.meta.filename) }}


## Programming Tasks

{{ get_programming_tasks(page.title)}}