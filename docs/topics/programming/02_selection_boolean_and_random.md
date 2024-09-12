---
title: Selection, Boolean and Random
image: programming.jpg
filename: '_data/data_questions.json'
---

![](../../assets/images/topics/{{image}}){width="100"; align=right}

# {{ title}}

This content should also be familiar from the programming with Python topic but we need to see how this concept is described using pseudocode.

## Selection

Recall that each line of code in a program will be executed one after the other in **sequence** unless we change the **flow of control** by introducing a construct such as **selection** or **iteration**.

With a selection statement the next statement to be executed will be dependent on some condition:

```
// in pseudocode
age = 15
if age > 17 then
    print("You are old enough to drive")
else
    print("You are not old enough to drive")
endif
```

The **condition**, `age > 17` is a boolean expression.  It will evaluate to either `True` or `False`.  In this example, `age = 15`, so the program will execute the `print()` statement that belongs to the `else` part of the selection block.

The `if` statement can provide a number of alternative branches:

```
if age > 18 then
    print("You may be at university")
elif age > 16 then
    print("You may be doing your A Levels")
elif age > 14 then
    print("You will be doing your GCSEs")
elif age > 11 then
    print("You will be at secondary school")
else
    print("You will be at primary school")
endif
```

### Nested if statements

Another `if` statement can appear inside another one:

```
if age <= 16 then
    if day == 'Tuesday' then
        print("20% Discount is available")
    else
        print("10% Discount is available")
    endif
else
    print("Full price only")
endif
```

### Switch/Case statement

Multiple `if ... elif ... elif .. endif``` statements can sometimes be hard to follow and the`switch ... case`` statement block can make this easier to read and maintain:


```
option = int(input("Enter an option: "))

switch option:
    case 1:
        print("You selected the first option")
    case 2:
        print("You selected the second option")
    case 3:
        print("You selected the third option")
    default:
        print("You made an invalid choice")
endswitch
```

Depending on the value entered by the user, the code will either take the first, second or third option.  If none of these is recognised, it will `default` to the final alternative.

## Boolean Expressions

A number of operators are available for boolean expressions:

| Operator | Description | Example | Result |
|:---------:|-------------|:-------:|:------:|
| `==` | Equal to | `7 == 7` | True |
| `!=` | Not Equal to | `7 != 6` | True |
| `>` | Greater than | `7 > 6` | True |
| `<` | Less than | `7 < 6` | False |
| `>=` | Greater than or equal to | `7 >= 7` | True |
| `<=` | Less than or equal to | `7 <= 7` | True |

!!! warning

    Pay attention to the "is equal to" operator ( == ), it's two equal signs. It’s easy to mistake it for the assignment operator ( = ).  It helps to read the assignment operator as e.g. "age is assigned the value 17" for `age = 17`; and "is age equal to 17?" for `age == 17`.

These are also known as the **comparison operators**

## Complex Boolean Expressions

Boolean expressions can be joined together using `AND`, `OR` and `NOT`.

```
if age > 16 AND age < 18 then
    print("You can claim a student discount")
endif
```

