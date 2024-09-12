---
title: 2D Lists
image: python.png
filename: '_data/python_questions.json'
---

![](../../assets/images/topics/{{image}}){width="100"; align=right}

# {{ title}}

!!! note "Objectives"
    - Define what a 2D list is in Python and explain its usefulness in representing tabular data with rows and columns.
    - Recognize the relationship between 2D lists and tables.
    - Demonstrate how to create a 2D list by encapsulating multiple lists within square brackets.
    - Understand the structure of a 2D list with examples.
    - Explain how to access elements in a 2D list using two indices, one for the row and one for the column.
    - Emphasize the need for two indices when working with 2D lists.
    - Use nested loops to iterate through the elements of a 2D list.

The examples thus far have only considered lists of one dimension but we can also create lists that look more like tables, with rows and columns, which give us two dimensions. Each element in a 2D list can be accessed using two indices: one for the row and one for the column.  More dimensions are possible but not recommended as they can get tricky to handle.

## Example 10

```python
# Example program with a 2D list
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Original matrix:")
for row in matrix:
    print(row)

element = matrix[1][2]
print("Element at row 2, column 3:", element)

matrix[0][0] = 10
print("Modified matrix:")
for row in matrix:
    print(row)
```

Predict what the output of the program will be:

- What will be printed for the original matrix?
- What will be the value of the element at row 2, column 3?
- How will the matrix look after modifying the first element?
   
Run the program in a Python environment and check your predictions, were they the same?

## Creating 2D Lists

You can create a 2D list by enclosing multiple lists within square brackets `[]`. Each inner list represents a row in the 2D list.

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

This is a list of lists! Think of it as being organised as a series of rows and columns, like a table.

## Accessing Elements

To access an element in a 2D list, use two indices: one for the row and one for the column. Remember that Python uses 0-based indexing.

```python
element = matrix[row_index][column_index]
```

## Modifying 2D Lists

You can change the values of elements in a 2D list by assigning new values using the indices just as you would with 1D lists but now we need two indices.

```python
matrix[1][2] = 42
```

## Looping Through 2D Lists

You can use nested loops to iterate through the elements of a 2D list.  The outer loop will work through each row, the inner loop will work through the columns in that row.

```python
for row in matrix:
    for element in row:
        # code to process each element
```

## Activity

Using the example program above, copy and paste into a Python IDE and make the following modifications:

- Change element at row 3, column 1 to 11
- Add a new row to the matrix
- Remove the second row

## Example

We've been asked to create a simple address book of our friends with their name, email address and phone number.  Our table of friends might look like this:

| Name    | Phone        | Email                       |
| ------- | ------------ | --------------------------- |
| Alice   | 09876 444555 | alice@example.com           |
| Bob     | 01287 655444 | bob@hotmail.co.uk           |
| Charlie | 09998 666555 | charlie_is_great_@gmail.com |
| Davina  | 06667 543213 | d_khan@myspace.tv           |
| Edward  | 08889 765432 | edward_davies@gmail.com     |

We currently have 5 rows and 3 columns, but will want to add more friends later.

First we initialise our empty table (2D list)

```py
address_book = [][]
```

Or, we could initialise the table with the data we have already:

```py
address_book = [
    ["Alice", "09876 444555","alice@example.com"],
    ["Bob","01287 655444","bob@hotmail.co.uk"],
    ["Charlie","09998 666555","charlie_is_great_@gmail.com"],
    ["Davina","06667 543213","d_khan@myspace.tv"],
    ["Edward","08889 765432","edward_davies@gmail.com"]
]
```

Our program will keep running, presenting us with the menu of options, until we enter quit (one of options):

```py
while True:
    print("\nOptions:")
    print("1. Find friend's information")
    print("2. Add a new friend")
    print("3. Quit")
    
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        # find a friend
    elif choice == "2":
        # add a new friend
    elif choice == "3":
        print("Goodbye")
        break
    else:
        print("Invalid choice.  please enter 1,2 or 3")
```

Let's tackle option 2.  We could create a separate function for this, which would be preferable if we had to consider validation and other factors such as saving and reading from  file etc., but here we're only dealing with three items of data:

```py
# previous code
elif choice == "2":
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    address_book.append([name, phone, email])   # add the list of data as a new row
```

!!! warning

    Be careful with the `append()` operation, we have to append the list and not each individual item of data

Option 1, finding the friend, is suitable for a function.  Here we could write a function that iterates through our table looking for a given name and then return the row when found or an error if not found.  This could then be passed to another function to display.  This would be best practice so that both functions e.g. `find_friend(name)` and `display_friend(friend)` would only be handling one task.  However, here we'll combine the two for simplicity:

```py
# Function to find and display friend information
def find_friend_info(name):
    for friend in address_book:                     # iterate over the list
        if friend[0] == name:
            print(f"Name: {friend[0]}")             # only need 1 index as it's the column we need
            print(f"Phone Number: {friend[1]}")
            print(f"Email: {friend[2]}")
            return
    print(f"{name} not found in your friends list.")
```

In our main program loop we add the call to that function, once we're got the name to find from our user:

```py
# previous code
if choice == "1":
    friend_name = input("Enter the name of your friend: ")
    find_friend_info(friend_name)
# subsequent code
```

## Climate Quest Project

![](../../assets/images/climate-quest.png){align=left width="200"}

Throughout this topic we'll be working on a large scale project: **Climate Quest**.  In this project a player embarks on a journey to combat the effects of climate change by making decisions that impact the environment. Each choice affects the outcome of the game, emphasizing the importance of individual actions in addressing climate change.

[Go to task 9 - 2D Lists](./climate_quest/task_9.md){:class=md-button}

## Questions

{{ show_questions(page.title, page.meta.filename) }}

## Programming Tasks

{{ get_programming_tasks(page.title)}}
