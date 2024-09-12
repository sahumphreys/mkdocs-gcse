---
title: Tracing an algorithm
image: algorithms.jpg
filename: '_data/algorithms_questions.json'
---

![](../../assets/images/topics/{{image}}){width="100"; align=right}

# {{ title}}

!!! note "Objectives"

    -  to identify where inputs, processing and outputs are taking place within an algorithm
    -  know how, and be able to, construct a trace table to illustrate how the value of variables are changing during the execution of an algorithm

Often, when writing and implementing our algorithms using code, we do not get the results we are expecting.  We get an error.  There may be different types of errors.

## Types of error

**Syntax Errors**

Syntax errors are related to the structure or grammar of the code and occur when the programmer violates the rules of the programming language.  They are picked up by the compiler or interpreter during the compilation phase.  Typically these might include missing semicolons, mismatched parentheses, or typos in keywords. The program won't run until all syntax errors are fixed.

**Logic Errors**

Logic errors occur when the program's logic is flawed, leading to incorrect results or unexpected behavior. The code may run without producing any error messages, but the output is not what was intended.  Logic errors are usually discovered during testing and debugging phases and may involve tracing the code and analyzing the output to identify discrepancies.  The program runs, but it does not produce the expected or desired results.

**Runtime Errors**

Runtime errors occur during the execution of a program, they are not detected by the compiler but emerge when the program is running.  They are usually  identified by error messages displayed during program execution and typically might include division by zero, accessing an out-of-bounds array element, or using an undefined variable.  When that happens the execution of the program is interrupted or terminated.
  
## Tracing an algorithm

Tracing an algorithm can help track down i.e. **debug** logic errors, and runtime errors.  Let's first look at the process and principles then use the technique on code that does have a logic error that needs to be corrected.

!!! note
     A trace table can also be used to determine the purpose of the algorithm

We'll start with the binary search algorithm from the previous section:

```python
def binary_search(items, target):
    low = 0
    high = len(items) - 1

    while low <= high:
        mid = (low + high) // 2  # Calculate the middle index

        if items[mid] == target:
            return mid  # Element found, return its index
        elif items[mid] < target:
            low = mid + 1  # Discard the left half
        else:
            high = mid - 1  # Discard the right half

    return -1  # Element not found
```

Our list of items will be: `sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`, and our `target` will be $7$.

When tracing we play the role of the computer keeping a record of the **variables** and how they are being changed during the execution of the function.  Proceed cautiously, do not try to second guess what you *think* might be happening, do not look forward just take it line by line.  It can help to cover up any lines of code not being considered, analyse that one line, note the variables and any change of state, before moving on to the next line.

Our function has a number of important variables.  Make these the columns of a table:

| target |  low  | high  |  mid  | items[mid] | output |
| :----: | :---: | :---: | :---: | :--------: | :----: |
|        |       |       |       |            |        |

We know our target is 7 and lines 2-3 of our function can be entered quite easily into our table:

| target |  low  | high  |  mid  | items[mid] | output |
| :----: | :---: | :---: | :---: | :--------: | :----: |
|   7    |   0   |   9   |       |            |        |

Moving down our code, line 5 is `True` as 0 is less than 9, so we proceed to the next line and note the value iof `mid`, then check the value at `items[mid]`:

| target |  low  | high  |  mid  | items[mid] | output |
| :----: | :---: | :---: | :---: | :--------: | :----: |
|   7    |   0   |   9   |   4   |     5      |        |

Line 8, we've  not found the target value in this position, the value is less than our target so we need to adjust the `low` value:

| target |  low  | high  |  mid  | items[mid] | output |
| :----: | :---: | :---: | :---: | :--------: | :----: |
|   7    |   0   |   9   |   4   |     5      |        |
|        |   5   |       |       |            |        |

!!! note
     You do not need to repeat the values for `target`, `high`, `mid` etc..  It is assumed these have not changed - which, of course, they haven't.

We return to the top of the loop and repeat.  

Line 5 is still `True` and we can progress to work out the value for `mid` (line 6) and then get the value for `items[mid]`:

| target |  low  | high  |  mid  | items[mid] | output |
| :----: | :---: | :---: | :---: | :--------: | :----: |
|   7    |   0   |   9   |   4   |     5      |        |
|        |   5   |       |   7   |     8      |        |

It's not our `target` value, but it is higher than our target so we use line 13 to adjust the value if `high`:

| target |  low  | high  |  mid  | items[mid] | output |
| :----: | :---: | :---: | :---: | :--------: | :----: |
|   7    |   0   |   9   |   4   |     5      |        |
|        |   5   |       |   7   |     8      |        |
|        |       |   6   |       |            |        |

Returning to the top of the loop again, `low <= high`  is still `True` so we update the value if `mid` and get the value of `items[mid]` as before:

| target |  low  | high  |  mid  | items[mid] | output |
| :----: | :---: | :---: | :---: | :--------: | :----: |
|   7    |   0   |   9   |   4   |     5      |        |
|        |   5   |       |   7   |     8      |        |
|        |       |   6   |       |            |        |
|        |       |       |   5   |     6      |        |

It's *still* not our target value so we continue.  The value is less than the target so we update the value of `low`:

| target |  low  | high  |  mid  | items[mid] | output |
| :----: | :---: | :---: | :---: | :--------: | :----: |
|   7    |   0   |   9   |   4   |     5      |        |
|        |   5   |       |   7   |     8      |        |
|        |       |   6   |       |            |        |
|        |       |       |   5   |     6      |        |
|        |   6   |       |       |            |        |

Returning to the top of the loop again, it evaluates to `True` and we proceed as before to the next line to get the value of `mid` and the corresponding item in the list:

| target |  low  | high  |  mid  | items[mid] | output |
| :----: | :---: | :---: | :---: | :--------: | :----: |
|   7    |   0   |   9   |   4   |     5      |        |
|        |   5   |       |   7   |     8      |        |
|        |       |   6   |       |            |        |
|        |       |       |   5   |     6      |        |
|        |   6   |       |       |            |        |
|        |       |       |   6   |     7      |        |

Now the `target` is the same as `items[mid]` and on line 9 we can return the value iof `mid` from our function and we are done.


## Questions

{{ show_questions(page.title, page.meta.filename) }}
