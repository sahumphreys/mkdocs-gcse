---
title: Tuples
image: python.png
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

## Creating Tuples
You can create a tuple by enclosing a comma-separated sequence of elements within parentheses `()`.

```python
my_tuple = (1, 2, 3, "apple", "banana")
```

Alternatively a tuple can be created by calling the function `tuple()`:

```py
empty_tuple = tuple()           # -> an empty tuple
my_tuple = tuple("apple")       # -> ('a','p','p','l','e')
```

The `tuple()` function takes only one argument, so best to think of it as converting another type into a tuple type.  As in the example above that takes the string "apple" and returns a tuple with teh elements of that string.  Similarly, if we give `tuple()` a list:

```py
my_tuple = tuple([1,2,3])
print(my_tuple)             # -> (1,2,3)
```

## Accessing Elements
Elements in a tuple are accessed using indexing, just like in lists. Python uses 0-based indexing.

```python
first_element = my_tuple[0]  # Access the first element
```

The slicing operator will also work on tuples:

```py
my_tuple = ('a','p','p','l','e')
print(my_tuple[1:4])                # -> ('p','p','l')
```

But, if you try to modify any element in a tuple you will get an error:

```py
my_tuple = ('a','p','p','l','e')
my_tuple[0] = 'A'                   # -> TypeError: 'tuple' object does not support item assignment
```

## Use Cases

Tuples are useful when you have a collection of related data that should not change. For example, coordinates (x, y), date and time (year, month, day, hour, minute), and more.

## Comparing tuples

Relational operators can be applied to tuples.  They start by comparing the first element of each tuple and then move to the second and so on:

```py
>>> (3, 7, 9) < (3, 6, 8)
False
>>> (2, 8, 100) < (20, 8, 200)
True
```

## Tuple assignment

There is a unique Python feature that can be used as a tuple can be on the left of an assignment statement.  Easier to show in an example:

```py
>>> a = ['Hello', 'World']
>>> b,c = a                     # clearer if we used brackets i.e. (b, c) = a
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
for n in student.items():
    print(n)            
```

The output is:

```py
('name', 'John')
('age', 25)
('grade', 'A')
```

If we call the `items()` function on our dictionary, it returns a list of tuples as `dict_items()`.  Each item in the list is a tuple with key value pairs.:

```py
>>> student = {"name": "John", "age": 25, "grade": "A"}
>>> student.items()
dict_items([('name', 'John'), ('age', 25), ('grade', 'A')])
```

It helps to first convert the in-built `dict_items()` form to a list:

```py
>>> s = list(student.items())
>>> s
[('name', 'John'), ('age', 25), ('grade', 'A')]
```

As this is now a list of tuples, they can be sorted.

Similarly, we saw the following used when looking at dictionaries:

```py
# Iterating through key-value pairs
for key, value in student.items():
    print(key, value)
```

The `key` and `value` here is a tuple (without the brackets, as brackets are optional).

## Tuples as return values

Another neat feature of the Python tuple is when we might want to return more than oone value from a function.  Consider the following example:

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

## Questions

{{ get_questions(page.title)}}

1. What is the key difference between a list and a tuple in Python?
2. How do you create a tuple in Python using parentheses?
3. Can you create an empty tuple? If so, how?
4. What is the indexing for the first element in a tuple?
5. What happens if you try to modify an element within a tuple?
6. Explain a use case where tuples are preferred over lists.
7. How are relational operators applied to tuples?
8. What is tuple assignment, and how is it used?
9. Provide an example of using tuple assignment to swap the values of two variables.
10. How can tuples be used to return multiple values from a function in Python?


## Programming Tasks

{{ get_programming_tasks(page.title)}}