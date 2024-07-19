---
title: Dictionaries
image: python.png
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

A dictionary is similar to a list but rather than using integers to index the elements in the list the indices can be of any type.  In other programming languages the dictionary might be known as a **map** or an **associative array**.  Think od a conventional English to French dictionary, if your want to know the French word for say 'house', your would look up in the dictionary for the item (key) 'house', the read back the French equivalent (value) as 'la maison'.  The notion of the key being associated with, or mapped to, a value is the essence of how the dictionary operates.

## Dictionary Basics

* A dictionary is defined using curly braces `{}` or the `dict()` constructor.
* Each item in a dictionary consists of a key and its corresponding value, separated by a colon `:`.
* Keys are unique within a dictionary, and they must be immutable objects (e.g., strings, numbers, or tuples).
* Values can be of any data type, including numbers, strings, lists, other dictionaries, and more.
* Some similarity to an array, but the index used will be the **key** rather than a numerical position

## Creating a Dictionary

```python
# Creating an empty dictionary
empty_dict = {}

# Creating a dictionary with key-value pairs
student = {"name": "John", "age": 25, "grade": "A"}
```

We can also use the function `dict()`, which creates an empty dictionary:

```py
french_english_dictionary = dict()
print(french_english_dictionary)         # => {}
```

Note the output from the `print()` statement: `{}`.  The curly braces signify the data type as being a dictionary.

## Accessing Values

* You can access the values in a dictionary by specifying the key in square brackets `[]`.
* If the key is not found, it raises a `KeyError`.

```python
# Accessing values
print(student["name"])  # Output: "John"
```

Recall the similarity with an array, we might have an array of students but these are 'keyed' by their position e.g.`student[0]`.  For the dictionary we use the identifier for the key, here being "name" in the square brackets.

## Modifying and Adding Entries

* You can modify the value associated with a key or add new key-value pairs to an existing dictionary.

```python
# Modifying values
student["age"] = 26

# Adding a new key-value pair
student["city"] = "New York"
```

When adding elements to a dictionary the order is not known, the dictionary is not automatically sorted.  However, this is not that significant as we use the key to access the associated element and the key must be unique.  If the key does not exist in the dictionary we get a `KeyValueError` returned as an exception.

## Dictionary Methods and Functions

* Python provides several built-in methods and functions to work with dictionaries, such as `keys()`, `values()`, `items()`, `get()`, `pop()`, and more.
* These methods allow you to retrieve keys, values, key-value pairs, and manipulate dictionary contents.

```python
# Getting keys and values
keys = student.keys()
values = student.values()

# Getting key-value pairs
items = student.items()
```

The return type from the `keys()` and `values()` functions are of type `dict_keys()` and `dict_values` respectively.  To make them a little easier to handle it is recommended to convert them to a list first:

```py
keys = list(student.keys())
values = list(student.values())
print(keys)                     # -> ['name', 'age', 'grade']
print(values)                   # -> ['John', 25, 'A']
```

In addition functions such as `len()` can be used to return the number of items in the dictionary.

## Iterating Through a Dictionary

* You can iterate through a dictionary using a `for` loop, which by default iterates over keys.
* The `in` operator can be applied which works on the keys in the dictionary

```python
# Iterating through keys
for key in student:
    print(key, student[key])

# Iterating through key-value pairs
for key, value in student.items():
    print(key, value)
```

!!! note 

    The algorithm used by the `in` operator if different for lists and dictionaries.  For a list it uses a linear search and thus the search time is dependent on the length of the list.  For the dictionary it uses a hash table which means it takes the same amount of time for any item irrespective of the number of items in the dictionary.

You might also try:

```py
for n in student.items():
    print(n)            
```

The output is:

```terminal
('name', 'John')
('age', 25)
('grade', 'A')
```

These are **tuples** and will be looked at in a later section.

## Checking for Key Existence

* You can use the `in` keyword or the `get()` method to check if a key exists in a dictionary.

```python
# Checking for key existence
if "name" in student:
    print("Name exists:", student["name"])

# Using get() to check for key existence
grade = student.get("grade", "Not found")
```

!!! note 

    - Dictionaries are unordered collections, which means the order of key-value pairs may not be preserved in older versions of Python (prior to 3.7).  
    - Starting from Python 3.7+, dictionaries maintain the insertion order of items.


### Example

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

## Questions

{{ get_questions(page.title)}}

1. What is the fundamental difference between a list and a dictionary in Python?
2. Explain the purpose of keys in a dictionary and why they must be unique.
3. How do you create an empty dictionary in Python using both curly braces and the `dict()` constructor?
4. Can you have a dictionary with keys of different data types? Explain with an example.
5. What happens if you try to access a key that does not exist in a dictionary?
6. How can you modify the value associated with a specific key in a dictionary?
7. Describe how you can add a new key-value pair to an existing dictionary.
8. What is the purpose of the `keys()`, `values()`, and `items()` methods in Python dictionaries?
9. Explain how the `in` operator works when checking for key existence in a dictionary.
10. How does Python handle the order of key-value pairs in dictionaries starting from Python 3.7?


## Programming Tasks

{{ get_programming_tasks(page.title)}}