---
title: Tuples
image: python.png
filename: '_data/python_questions.json'
---

![](../../assets/images/topics/{{image}}){width="100"; align=right}

# {{ title}}

!!! note "Objectives"
    - Differentiate between tuples and lists in Python, emphasizing the immutability of tuples.
    - Recognize the use of tuples to group related data together.
    - Learn how to create tuples
    - Access elements in a tuple using indexing, similar to lists.
    - Understand 0-based indexing and the slicing operator for tuples.
    - Identify scenarios where tuples are useful, especially when dealing with collections of related data that should not change.
    - Apply relational operators to tuples, which compare elements in a pairwise manner.

Similar to a list, a tuple is a sequence of values which can be of any type and are indexed by integers.  The key difference however is that a tuple is **immutable** meaning their contents cannot be changed after creation.  Tuples are typically used to group related data together.


## Example 12

```python hl_lines="3 6 9 12 15 18"
# Example program with tuples
climate_info = ("Sunny", 25, 45)
print("Original climate info:", climate_info)

weather = climate_info[0]
print("Weather:", weather)

temperature = climate_info[1]
print("Temperature:", temperature)

humidity = climate_info[2]
print("Humidity:", humidity)

sub_tuple = climate_info[1:]
print("Sub-tuple:", sub_tuple)

comparison = (25, 45) == (25, 45)
print("Comparison result:", comparison)
```

Using the example code above, predict the output for the following:

- What will be printed for the original climate info (line 3)?
- What will the weather, temperature, and humidity variables contain (lines 6, 9 and 12)?
- What will be printed for the sub-tuple (line 15)?
- What will the comparison result be (line 18)?

Copy the code into a Python environment and run the program.  Were you right?

## Creating Tuples

You create a tuple by enclosing a comma-separated sequence of elements within parentheses `()`.

```python
climate_info = ("Sunny", 25, 45)
```

Alternatively a tuple can be created by calling the function `tuple()`:

```py
empty_tuple = tuple()           # -> an empty tuple
my_tuple = tuple("sunny")       # -> ('s','u','n','n','y')
```

The `tuple()` function takes only one argument, so best to think of it as converting another type into a tuple type.  As in the example above that takes the string "apple" and returns a tuple with the elements of that string.  

Similarly, if we give `tuple()` a list:

```py
my_tuple = tuple([1,2,3])
print(my_tuple)             # -> (1,2,3)
```

## Accessing Elements

Elements in a tuple are accessed using indexing, just like in lists. Python uses 0-based indexing.

```python
first_element = climate_info[0]  # Access the first element -> "sunny"
```

The slicing operator will also work on tuples:

```py
my_tuple = ('s','u','n','n','y')
print(my_tuple[1:4])                # -> ('u','n','n')
```

But, if you try to modify any element in a tuple you will get an error:

```py
my_tuple = ('s','u','n','n','y')
my_tuple[0] = 'S'                   # -> TypeError: 'tuple' object does not support item assignment
```

## Use Cases

Tuples are useful when you have a collection of related data **that should not change**. For example, coordinates (x, y), date and time (year, month, day, hour, minute), and more.

## Comparing tuples

Relational operators can be applied to tuples.  They start by comparing the first element of each tuple and then move to the second and so on:

```py
>>> (3, 7, 9) < (3, 6, 8)
False
>>> (2, 8, 100) < (20, 8, 200)
True
```

## Tuple assignment

There is a unique Python feature that can be used as a tuple can be on the left of an assignment statement.  This is easier to show in an example than explain!

```py
>>> a = ['Hello', 'World']
>>> (b, c) = a   # the brackets are optional but make the tuple assignment clearer
>>> b
'Hello'
>>> c
'World'
```

A neat use of this feature is to swap the values of two variables:

```py
>>> b, c = c, b
>>> b
'World'
>>> c
'Hello'
```

We can go further and use it, for example to split an email address into the username and domain:

```py
>>> email = 'peter.davies@gmail.com'
>>> username, domain = email.split('@')
>>> username
'peter.davies'
>>> domain
'gmail.com'
```

## Dictionaries and tuples

Recall the example for the section on dictionaries:

```py
for n in climate_data.items():
    print(n)            
```

The output is:

```py
('temperature', 22)
('humidity', 45)
('wind-_speed', 15)
```

If we call the `items()` function on our dictionary, it returns a list of tuples as `dict_items()`.  Each item in the list is a **tuple** with key value pairs:

```py
>>> climate_data = {'temperature': 22, 'humidity': 45, 'wind-_speed': 15, 'rainfall': 37}
>>> climate_data.items()
dict_items([('temperature', 22), ('humidity', 45), ('wind-_speed', 15), ('rainfall', 37)])
```

It helps to first convert the in-built `dict_items()` form to a list:

```py
>>> c = list(climate_data.items())
>>> c
[('temperature', 22), ('humidity', 45), ('wind-_speed', 15), ('rainfall', 37)]
```

As this is now a list of tuples, they can be sorted.

Similarly, we saw the following used when looking at dictionaries:

```py
# Iterating through key-value pairs
for key, value in climate_data.items():
    print(key, value)

# output:
# temperature 22
# humidity 45
# wind-_speed 15
```

The `key` and `value` here is a tuple (without the brackets, as brackets are optional).

## Tuples as return values

Another neat feature of the Python tuple is when we might want to return more than one value from a function.  Consider the following example:

```py
def get_name_and_age():
    name = "Alice"
    age = 25
    return name, age

result = get_name_and_age()
print(result)  # Output: ('Alice', 25)
```

The function `get_name_and_age()` returns a tuple containing two values: the `name` and `age`. The caller of the function can then unpack the tuple into separate variables or use it as-is:

```py
name, age = get_name_and_age()
print(name)  # Output: 'Alice'
print(age)   # Output: 25
```

## Activity

Modify the example program to make the following changes:

1. Attempt to change an element in the tuple.  What happens?
2. Create a new tuple with updated values.
3. Combine tuples to form a new tuple.
4. Iterate through the tuple and print each element.

## Climate Quest Project

![](../../assets/images/climate-quest.png){align=left width="200"}

Throughout this topic we'll be working on a large scale project: **Climate Quest**.  In this project a player embarks on a journey to combat the effects of climate change by making decisions that impact the environment. Each choice affects the outcome of the game, emphasizing the importance of individual actions in addressing climate change.

**There is no additional task for tuples for the Climate Quest project.  USe the time to continue the refactoring exercise from the previous task.**

## Questions

{{ show_questions(page.title, page.meta.filename) }}

## Programming Tasks

{{ get_programming_tasks(page.title)}}