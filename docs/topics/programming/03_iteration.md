---
title: Iteration
image: programming.jpg
filename: '_data/data_questions.json'
---

![](../../assets/images/topics/{{image}}){width="100"; align=right}

# {{ title}}

There are three main **programming constructs**, that is, three main building blocks we use to construct algorithms:

- sequence
- selection
- iteration

In **sequence** the code statements are executed one after another; in **selection** a choice is made based on a boolean expression to determine which statement, or block of statements, will be executed; in **iteration** statements will repeat until a condition is met.

There are three types of iteration statements:

- the `for ... next` loop
- the `while ... endwhile` loop, and
- the `do ... until` loop

!!! note
    Python only has the first two, there is no `do ... while` loop in Python

## `for` loop

The `for ... next' loop will repeat a set number of times.  It is sometimes known as the **counted loop**.  The code sets up a counter and it will count up from a start value to a stop value.  When that stop value has been reached the loop will end.

```
sum = 0
for count = 1 to 10
    sum = sum + count
next i
print(sum)
```

On each iteration of the loop the value if `count` is incremented, and the value of count on that loop is added to our accumulator, `sum`.  When `count` reaches 10 the loop ends and the value if `sum` is printed to the screen.

## `while ... endwhile` loop

This loop is used `while` a given condition is `True`.  The same loop can be expressed in this was:

```
sum = 0
count = 1
while count <= 10
    sum = sum + count
    count = count + 1
endwhile
print(sum)
```

The functionality is identical to the `for` loop, though the syntax used is different.

The `while` loop is also known as a **top-tested loop**.  The condition for entering the loop is placed at the top, all the while this condition remains `True` the loop will run.

Unlike the `for` loop, we have to manage the `count` variable, firstly by giving it a start value, and then changing that value as part of the loop.

If we did not change the value of `count` inside the loop it would just keep on running - an **inifinite loop**.

## `do ... until` loop

The `do ... until` loop is also known as a **bottom-tested loop**, the condition is placed at the bottom.

The same algorithm can be expressed using this form:

```
sum = 0
count = 1
do
    sum = sum + count
    count = count + 1
until count == 10
print(sum)
```

It does not matter what the start value of `count` is in this loop, the loop will *always* be executed at least once.  Consider what happens if we assign 11 to `count` in line 2.  What will be output?  If we did the same thing with the `while ... endwhile` loop, what would be the output?

