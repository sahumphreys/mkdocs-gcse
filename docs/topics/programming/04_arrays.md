---
title: Arrays
image: programming.jpg
filename: '_data/data_questions.json'
---

![](../../assets/images/topics/{{image}}){width="100"; align=right}

# {{ title}}

When using Python we came across the `list` data structure:

```python
my_shopping_list = ["Milk", "Eggs", "Tomatoes"]
my_values = [1, 6, 87,34, 23]
my_mixed_list = ["Milk", 45, "Flour", 23.99]
my_sub_list = [["Milk", "Eggs"], [45, 3.142]]
```

The list is a fundamental data structure in Python that allows us to store and manage such collections of data, where the collection is gathered under a single identifier or name.  Their contents can be changed during the run of the program, items can be added, changed or removed i.e. they are **mutable**.  

E.g. we have just three of items on our shopping list above.  Each item is in a given position indicated by an integer started at $0$.  So, "Milk" can be referenced by `my_shopping_list[0]` and "Tomatoes" by `my_shopping_list[2]` etc..

**AQA Pseudocode**

Syntax is as above, except the assignment operator that uses `<-`.

**OCR pseudocode**

Syntax is as above

## Array vs List

- The list `my_shopping_list` is a list in Python but more accurately we call it an **array**
- The list `my_mixed_list` is also a list in Python but it is **not** an array.

The difference is due to the data types being used.  All items of data in an array **must** be the same data type.

## 2D Array

An array can have several dimensions.  Suppose we wanted to also store a set os marks achieved by students on a test?

```
marks = [[19, 16, 14, 16], [12, 8, 11, 14], [20, 17, 12, 8]]
```

Here we have the marks achieved by 3 students, each item in the array represent the marks for a student.  These marks are presented as a list.  Think of this as a table with rows and columns:

| test 1 | test 2 | test 3 | test 4 |
| :----: | :----: | :----: | :----: |
|   19   |   16   |   14   |   16   |
|   12   |   8    |   11   |   14   |
|   20   |   17   |   12   |   8    |

To extract and process the items in the 2D array we need two indexes: e.g. `marks[0][1]`, `marks[3][0]`

If wwe wanted to display all the marks as a table, using pseudocode, we might do:

**AQA Pseudocode**

```
FOR student <- 0 to 2
    student_total <- 0
    FOR mark = 0 to 3
        student_total = studentTotal + marks[student][mark]
    ENDFOR
    OUTPUT student_total
ENDFOR
```

**OCR Pseudocode**

```
for student = 1 to 2
    student_total = 0
    for mark = 0 to 3
        student_total = student_total + marks[student,mark]
    next mark
next student
print(student_total)
```

!!! note
    The indices in line 4, uses one set of square brackets with the row, column indices separated by a  comma