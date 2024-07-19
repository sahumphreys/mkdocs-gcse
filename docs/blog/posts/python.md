---
title: Using Sets in Python
date: 2023-10-18
categories:
    - python
---

# {{ title}}

Python has a set data structure built-in.

<!-- more -->

__Declaring a set__

```{.python .numberLines}
mySet = {1.0, "Python", (4, 5, 6)}
print(mySet)
```

Sets do not have duplicates, not can they contain mutable items such as lists, but a set can be formed from a list:

```{.python .numberLines}
# no duplicates, this will output {1, 2, 3, 4}
mySet = {1,1,2,2,2,3,4,4}
print(mySet)

# this line will cause an error as the set contains a list
# eSet = {1, 2, [3, 4]}

# a set can be made, cast, from a list
eSet = set([1, 2, 3])
print(eSet)
```

__Adding elements to a set__

Empty sets are created using the `set()` function on a dictionary with no arguments and elements are added to the set object using the methods `add()` for a single element and `update()` for multiple:

~~~{.python .numberLines}
# declare an empty set
s = {}
# check the data type ...
print(type(s))
s = set()
#check the data type again ..
print(type(s))

# add an element
s.add(42)
print(s)
# add multiple elements
s.update([6, 98])
print(s)
~~~


__Removing elements from a set__

Elements can be removed using either `remove()` which raises an error if the element can not be found, or `discard()`, or to clear all elements use `clear()`.

Python permits set operations as well.

__Set Operations: Union__

Use the "|" operator, or call the `union` method on a set object:

~~~{.python .numberLines}
A = {1, 2, 3}
B = {4, 5, 6}

print{A | B}        # {1, 2, 3, 4, 5, 6}

C = {}              # declare a new set
C = set()
C = A.union(B)      # populate with A union B
~~~

__Set Operations: Intersection__

Use the "&" operator, or call the `intersection` method:

~~~{.python .numberLines}
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A & B)
~~~

__Take it further__

There are a lot of other built in methods and functions for processing sets and you are encouraged to explore further, see for example the following:

- [https://www.python-course.eu/sets_frozensets.php](https://www.python-course.eu/sets_frozensets.php)
- [https://www.python-course.eu/sets_frozensets.php](https://www.python-course.eu/sets_frozensets.php)
- [https://www.programiz.com/python-programming/set](https://www.programiz.com/python-programming/set)
- [https://www.geeksforgeeks.org/sets-in-python/](https://www.geeksforgeeks.org/sets-in-python/)
