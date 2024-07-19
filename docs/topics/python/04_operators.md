---
title: Operators
image: python.png
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

We can get familiar with these using the interactive environment:

```py
>>> 3 + 4
7
>>> 3 * 4
12
>>> 3 * 4 - 2
10
>>> 3 / 4
0.75
```

Note the order of precedence in the third example (line 5), multiplication is carried out before subtraction, as we might expect.  Also note the answer to the fourth example (line 7), we provided two integers but the result was given as a real number.

There is an alternative division operator for when we want to carry out integer division:

```py
>>> 7 // 2 
3
```
Here the answer is given as an integer, not a real number as we used the integer division operator `//`.  `2` divides into `7` `3` times leaving `1` as the remainder.  If we needed to grab that remainder, we'd use the modulo operator, `%`:

```py
>>> 7 % 2
1
```

If we think of an example of wanting to know how many hours and minutes for a movie that lasts 138 minutes.  We can get the hours by using the integer division operator: `hours = minutes // 60`.  This automatically rounds down.  We can get the remainder too: `remainder = minutes - (hours * 60)`.  But this is the same as using the modulo operator: `remainder = minutes % 60`.

It is also really useful when checking if one divides equally into another.  For example: `if x % 2 == 0`, then we know if the number (`x`) is odd or even.

There is also the exponent operator, `**`:

```py
>>> 2**4
16
```

This is $2^4$ giving the result $16$ as we would expect.

### Augmented assignment operators

A nice shortcut, or syntactic sugar are:

```py
>>> x = 6
>>> x += 1          # the same as x = x + 3
>>> x
7
>>> x *= 2          # the same as x = x * 2
14
```

It does not matter which you prefer to use but the shorter form takes a little less typing.

### Operator precedence

There should be no surprises here, at least initially:

- exponentiation
- multiplication or division
- addition or subtraction

As in maths any brackets take priority, so these can be used to alter the order of precedence

## Logical operators

Logical operators in Python allow us to perform logical operations on one or more **Boolean** values (`True` or `False`). These operators are used to make decisions and control the flow of a program based on those conditions. They are often referred to as Boolean operators.

Python provides three main logical operators:

1. **AND (`and`):** The `and` operator combines two operands or expressions and returns `True` if both operands/expressions are true; otherwise, it returns `False`.

2. **OR (`or`):** The `or` operator combines two operands or expressions and returns `True` if at least one of the operands is true; it returns `False` only if both operands are false.

3. **NOT (`not`):** The `not` operator returns the opposite Boolean value of the operand or expression. If the operand is `True`, `not` makes it `False`, and vice versa.

For example:


| Example         | T/F   | Reason                                                                           |
| --------------- | ----- | -------------------------------------------------------------------------------- |
| $3>6$ and $4<5$ | False | The expression 3 > 6 is false so the whole expression will return `False`        |
| $3>6$ or $4<5$  | True  | One of the conditions is true, 4 < 5, so the whole expression will return `True` |
| not $3>6$       | True  | 3<6 returns `False`, so the `not` will flip this result and so return `True`     |


### Logical Operator Examples

Let's explore these logical operators with some examples, you can try these in the interactive environment:

#### 1. AND Operator (`and`)

The `and` operator returns True only if both conditions are True.

```py
>>> x = True
>>> y = False
>>> x and y
False
```

#### 2. OR Operator (`or`)

The `or` operator returns True if at least one condition is True.

```py
>>> a = True
>>> b = False
>>> a or b
True
```

#### 3. NOT Operator (`not`)

The `not` operator negates the Boolean value.

```py
>>> p = True
>>> not p
False
```

### Combining Logical Operators

You can combine logical operators to create more complex conditions:

```python
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

- **Boolean Algebra:** In mathematical and engineering applications involving Boolean algebra.

We will consider each of these use cases in later sections.

## Comparison operators

Comparison operators in Python are used to compare two values or expressions and produce Boolean results (`True` or `False`). These operators allow you to check conditions and make decisions based on the results of these comparisons. Python provides several comparison operators:

1. **Equal to (`==`):** Checks if two values are equal.

2. **Not equal to (`!=`):** Checks if two values are not equal.

3. **Greater than (`>`):** Checks if one value is greater than another.

4. **Less than (`<`):** Checks if one value is less than another.

5. **Greater than or equal to (`>=`):** Checks if one value is greater than or equal to another.

6. **Less than or equal to (`<=`):** Checks if one value is less than or equal to another.

### Comparison Operator Examples

Let's explore these comparison operators with some examples, again use the interactive environment to check the results:

#### 1. Equal to (`==`)

The `==` operator checks if two values are equal.

```py
>>> x = 5
>>> y = 5
>>> x == y
True
```

#### 2. Not equal to (`!=`)

The `!=` operator checks if two values are not equal.

```py
>>> a = 10
>>> b = 20
>>> a != b
True
```

#### 3. Greater than (`>`)

The `>` operator checks if one value is greater than another.

```py
>>> m = 30
>>> n = 15
>>> m > n
True
```

#### 4. Less than (`<`)

The `<` operator checks if one value is less than another.

```terminal
>>> p = 25
>>> q = 50
>>> p < q
True
```

#### 5. Greater than or equal to (`>=`)

The `>=` operator checks if one value is greater than or equal to another.

```py
>>> alpha = 100
>>> beta = 100
>>> alpha >= beta  
True
```

#### 6. Less than or equal to (`<=`)

The `<=` operator checks if one value is less than or equal to another.

```py
>>> gamma = 75
>>> delta = 100
>>>  gamma <= delta
True
```

### Combining Comparison Operators

You can combine comparison operators to create complex conditions:

```python
age = 25

if age >= 18 and age <= 65:
    print("You are eligible to vote and of working age.")
```

In this example, the `and` operator is used to check if the age is both greater than or equal to 18 and less than or equal to 65.

### Common Use Cases

Comparison operators are commonly used in programming for various purposes, such as:

- **Conditional Statements:** To make decisions and control program flow using `if`, `elif`, and `else` statements.

- **Loop Control:** To control the execution of loops, such as `while` and `for` loops.

- **Sorting and Filtering:** To sort data and filter it based on specific conditions.

- **Searching and Validation:** To search for specific values in data and validate user input.

## Questions

{{ get_questions(page.title)}}

## Programming Tasks

{{ get_programming_tasks(page.title)}}