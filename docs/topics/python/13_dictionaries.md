---
title: Dictionaries
image: python.png
filename: '_data/python_questions.json'
---

![](../../assets/images/topics/{{image}}){width="100"; align=right}

# {{ title}}

!!! note "Objectives"
    - Differentiate between dictionaries and lists in Python, emphasizing the key-value pair structure of dictionaries.
    - Define a dictionary using curly braces {} or the dict() constructor.
    - Understand the uniqueness and immutability of keys in a dictionary.
    - Create an empty dictionary using curly braces and the dict() constructor.
    - Initialize a dictionary with key-value pairs using identifiers and colons.
    - Access values in a dictionary by specifying the key in square brackets.
    - Use built-in methods such as keys(), values(), and items() to retrieve information from dictionaries.

A dictionary is similar to a list but rather than using integers to index the elements in the list the indices can be of any type.  In other programming languages the dictionary might be known as a **map** or an **associative array**.  Think od a conventional English to French dictionary, if you want to know the French word for say 'house', your would look up in the dictionary for the item (key) 'house', the read back the French equivalent (value) as 'la maison'.  The notion of the key being associated with, or mapped to, a value is the essence of how the dictionary operates.


## Example 11

```python hl_lines="7 10 13 19-21"
# Example program with a dictionary
climate_data = {
    "temperature": 22,
    "humidity": 45,
    "wind_speed": 15
}
print("Original climate data:", climate_data)

temp = climate_data["temperature"]
print("Temperature:", temp)

climate_data["temperature"] = 25
print("Updated climate data:", climate_data)

keys = climate_data.keys()
values = climate_data.values()
items = climate_data.items()

print("Keys:", keys)
print("Values:", values)
print("Items:", items)
```

Predict the output of the program for the highlighted lines in the example program:

- What will be printed for the original climate data?
- What will the temperature variable contain?
- How will the climate data look after updating the temperature?
- What will be printed for keys, values, and items?

Run the program in a Python environment to confirm or correct your predictions

## Dictionary Basics

* A dictionary is defined using curly braces `{}` or the `dict()` constructor.
* Each item in a dictionary consists of a **key** and its corresponding **value**, separated by a colon `:`.
* Keys are unique within a dictionary, and they must be immutable objects (e.g., strings, numbers, or tuples).
* Values can be of any data type, including numbers, strings, lists, other dictionaries, and more.
* Some similarity to a list, but the index used will be the **key** rather than a numerical position

## Creating a Dictionary

```python
# Creating an empty dictionary
empty_dict = {}

# Creating a dictionary with key-value pairs
climate_data = {
    "temperature": 22,
    "humidity": 45,
    "wind_speed": 15
}
```

We can also use the function `dict()`, which creates an empty dictionary:

```py
climate_data = dict()
print(climate_data)         # => {}
```

Note the output from the `print()` statement: `{}`.  The curly braces signify the data type as being a dictionary.

## Accessing Values

* You can access the values in a dictionary by specifying the key in square brackets `[]`.
* If the key is not found, it raises a `KeyError`.

```python
# Accessing values
print(climate_data["temperature"])  # Output: 22
```

Recall the similarity with a list, we could have used a list to hold the climate data but this data would be 'keyed' by their position in the list e.g.`climate_data[0]`.  For the dictionary we use the identifier for the key, here being "temperature" in the square brackets.  Using the identifier makes the code easier to read.

## Modifying and Adding Entries

* You can modify the value associated with a key or add new key-value pairs to an existing dictionary.

```python
# Modifying values
climate_data["humidity"] = 41

# Adding a new key-value pair
climate_data["rainfall"] = 37
```

!!! note

    When adding elements to a dictionary the order is not known, the dictionary is not automatically sorted.  However, this is not that significant as we use the key to access the associated element and the key must be unique.  If the key does not exist in the dictionary we get a `KeyValueError` returned as an exception.

## Dictionary Methods and Functions

* Python provides several built-in methods and functions to work with dictionaries, such as `keys()`, `values()`, `items()`, `get()`, `pop()`, and more.
* These methods allow you to retrieve keys, values, key-value pairs, and manipulate dictionary contents.

```python
# Getting keys and values
keys = climate_data.keys()
values = climate_data.values()

# Getting key-value pairs
items = climate_data.items()
```

The return type from the `keys()` and `values()` functions are of type `dict_keys()` and `dict_values` respectively.  To make them a little easier to handle it is recommended to convert them to a list first:

```py
keys = list(climate_data.keys())
values = list(climate_data.values())
print(keys)                     # -> ['temperature', 'humidity', 'wind-_speed']
print(values)                   # -> [22, 45, 15]
```

In addition functions such as `len()` can be used to return the number of items in the dictionary.

```py
print(len(climate_data))        # -> 3
```

## Iterating Through a Dictionary

* You can iterate through a dictionary using a `for` loop, which by default iterates over keys.
* The `in` operator can be applied which works on the keys in the dictionary

```python
# Iterating through a dictionary using the key
for key in climate_data:
    print(key, climate_data[key])

# Iterating through key-value pairs
for key, value in student.items():
    print(key, value)
```

!!! note 

    The algorithm used by the `in` operator is different for lists and dictionaries.  For a list it uses a linear search and thus the search time is dependent on the length of the list.  For the dictionary it uses a hash table which means it takes the same amount of time for any item irrespective of the number of items in the dictionary.

You might also try:

```py
for n in climate_data.items():
    print(n)            
```

The output is:

```terminal
('temperature', 22)
('humidity', 45)
('wind-_speed', 15)
```

These are **tuples** and will be looked at in a later section.

## Checking for Key Existence

You can use the `in` keyword or the `get()` method to check if a key exists in a dictionary.

```python hl_lines="6"
# Checking for key existence
if "humidity" in climate_data:
    print("Humidity:", climate_data["humidity"])

# Using get() to check for key existence
rainfall = climate_data.get("rainfall", "Not found")
```

For line 6, there is no key for "rainfall" in the original dictionary therefore the variable `rainfall` will be assigned "Not found".  If it was present in the dictionary the variable would contain the key's value.

!!! note 

    - Dictionaries are unordered collections, which means the order of key-value pairs may not be preserved in older versions of Python (prior to 3.7).  
    - Starting from Python 3.7+, dictionaries maintain the insertion order of items.

## Activity

Using the example code, make the following changes:

1. Add a new key-value pair for precipitation
2. Remove a key-value pair
3. Update an existing value
4. Iterate through the dictionary and print each key-value pair

Copy the following into your Python environment and modify the code as indicated by the comments.

```py
# Modified example with dictionary manipulations
climate_data = {
    "temperature": 22,
    "humidity": 45,
    "wind_speed": 15
}

# Q1: Add a new key-value pair for precipitation
# Answer: 

print("Climate data after adding precipitation:", climate_data)

# Q2: Remove a key-value pair
# Answer: 

print("Climate data after removing humidity:", climate_data)

# Q3: Update an existing value
# Answer:

print("Climate data after updating wind_speed:", climate_data)

# Q4: Iterate through the dictionary and print each key-value pair
# Answer:
```

## Further Example

```python
# Creating a dictionary to store information about a book
book = {
    "title": "Python Crash Course",
    "author": "Eric Matthes",
    "pages": 544,
    "year": 2015
}

# Accessing and printing book details
print("Title:", book["title"])
print("Author:", book["author"])
print("Pages:", book["pages"])
print("Year:", book["year"])
```

## Climate Quest Project

![](../../assets/images/climate-quest.png){align=left width="200"}

Throughout this topic we'll be working on a large scale project: **Climate Quest**.  In this project a player embarks on a journey to combat the effects of climate change by making decisions that impact the environment. Each choice affects the outcome of the game, emphasizing the importance of individual actions in addressing climate change.

[Go to task 10 - Dictionaries](./climate_quest/task_10.md){:class=md-button}

## Summary

[Cheat sheet for dictionaries](../../files/beginners_python_cheat_sheet_pcc_dictionaries.pdf){:class=md-button} [^source]

[^source]: [https://ehmatthes.github.io/pcc_3e/cheat_sheets/](https://ehmatthes.github.io/pcc_3e/cheat_sheets/)

## Questions

{{ show_questions(page.title, page.meta.filename) }}

## Programming Tasks

{{ get_programming_tasks(page.title)}}