---
title: Working with files
image: python.png
filename: '_data/python_questions.json'
---

![](../../assets/images/topics/{{image}}){width="100"; align=right}

# {{ title}}

!!! note "Objectives"
    - Differentiate between text files and binary files.
    - Define text files as composed of plain, human-readable text with specific character encoding.
    - Identify the line-based structure of text files, including the role of newline characters.
    - Explain the process of opening a file using the `open()` function.
    - Understand file modes (`r`, `w`, `a`, `b`) and their purposes (reading, writing, appending, binary).
    - Recognize the association of file handles with resource management and the importance of closing files.
    - Use the `write()` method to write a string to a text file.
    - Append data to an existing file using the 'a' mode.

Thus far all the programs we have written have been working with data stored in main memory, once the program finishes all the data we have been using is lost.  Here we look into how we can read and write data to a storage device thus making it available for any subsequent runs of our program.

Files can either be **text** files, where the data is stored as plain text; or **binary**, where the data is encoded in binary.  

## Text files vs binary files

A text file is a type of computer file that contains plain, human-readable text. It is a simple and commonly used file format for storing textual data in a structured or unstructured manner. Text files are typically composed of characters from a specific character encoding, such as ASCII or UTF-8, which represent alphanumeric characters, symbols, and control characters (e.g., newline and tab).

Text files are:

* **Human-Readable:** they can be opened with a text editor.

* **Unformatted:** Text files usually do not contain any formatting information. They consist of plain text without styles, fonts, colors, or any other layout-related attributes. This simplicity makes them versatile for a wide range of applications.

* **Line-Based:** Text files are often organized into lines or rows of text, with each line terminated by a newline character (e.g., '\n' in Unix-based systems or '\r\n' in Windows). Lines in text files are often used to separate records or pieces of information.

* **Character Encoding:** Text files use a specific character encoding scheme to represent characters. Common character encodings include ASCII, UTF-8, and ISO-8859-1. The choice of encoding determines which characters can be represented in the file.

In contrast to text files, binary files store data in a non-human-readable format, often in a way that is optimized for efficient storage and processing by a computer. Binary files can contain a wide range of data, including images, audio, video, executable programs, and more. Text files are primarily used for storing textual information and are easier for humans to work with and understand.

We'll mainly focus on how to handle text files.

## Example 14

```python hl_lines="1 5 9 12"
file = open("example.txt", "w")
file.write("Hello, World!")
file.close()

file = open("example.txt", "a")
file.write("\nThis is a new line.")
file.close()

file = open("example.txt", "r")
content = file.read()
print(content)
file.close()
```

Review the example and predict what will happen when:

- What do you think the `open()` function does in this code, line 1?
- Why are there different characters inside the quotes, such as `"w"`, `"a"`, and `"r"`, lines 1, 5, 9?
- What might happen when we write to a file and then append more text to it?
- Why is it important to close the file, line 12?

Copy and paste the code into a Python environment, run the code and check the results against your predictions.


## Further tasks

- Modify the file name in the code and see what happens when you try to read from a file that doesn’t exist.
- Experiment with different file modes, such as `"b"` for binary files, and discuss how this would change the data handling.
- Test what happens if you forget to close the file. Discuss how this can affect file integrity and resource management.

## Key Concepts and Explanations

1. **Text Files vs. Binary Files:**
   - **Text Files:** Contain plain, human-readable text with specific character encoding (e.g., UTF-8).
   - **Binary Files:** Consist of data in binary format, typically not human-readable, such as images or executables.

2. **File Modes in Python:**
   - `"r"`: Read mode (default). Opens the file for reading.
   - `"w"`: Write mode. Creates a new file or truncates an existing one.
   - `"a"`: Append mode. Opens the file for writing and appends data to the end.
   - `"b"`: Binary mode. Used with `"r"`, `"w"`, or `"a"` to handle binary files.

3. **File Handles and Resource Management:**
   - Opening a file returns a file handle, a reference to the file.
   - It's crucial to close files after operations to release system resources and avoid data corruption.

4. **Writing to a File:**
   - The `write()` method allows writing strings to a file. When in `"w"` mode, it overwrites existing content; in `"a"` mode, it appends new content.

5. **Appending Data:**
   - Using `"a"` mode, you can add new content to the end of the file without erasing the existing content.

## Files are line-based

Structurally a text file consists of a number of lines.  To break the file into lines we need the end of line character, sometimes called the newline character.  We've seen how we can force a string to go across two lines by using  `\n` in the string:

```py
>>> print('Hello\nWorld')
Hello
World
>>> my_string = 'a\nc'
>>> print(my_string)
a
c
>>> len(my_string)          # the new line character counts towards the count
3
```

When we look at the lines in a text file we have to remember there will be a new line character at the end of each line.

## Opening a File

Before you can read from or write to a file, you need to open it using the `open()` function. The `open()` function takes two arguments: the file name and the **mode** in which you want to open the file.

* r: Read (default mode) - Opens the file for reading.
* w: Write - Opens the file for writing. If the file already exists, it will be truncated; if not, a new file will be created.
* a: Append - Opens the file for writing, but appends data to the end of the file. If the file does not exist, it will be created.
* b: Binary mode - Used in conjunction with other modes to indicate that the file should be treated as binary.

When we are opening a file Python has to interact with the operating system.  It's the operating system that 'knows' where the data for the requested file is stored.  We're asking the operating system to find the file (using the name of the file) and to make sure the file exists in that location.

If the request to open the file is successful the operating system will return a **file handle**.  It's not the actual data in the file but a pointer to where that data is stored.

!!! note 

    File handles, like pointers, are associated with resource management. When you open a file, the operating system allocates resources to maintain the file's state, and the file handle is responsible for managing those resources. This includes closing the file handle when you're done to release those resources.


If the request is not successful an exception will be raised: `FileNotFoundError`.  It is always good practice to wrap any calls to open a file within a `try ... except` block (though my be omitted to save space in examples here).

## Reading from Text Files

To read from a text file, you can use various methods, but the most common one is `read()`.

```python
# Opening a text file for reading
file = open('example.txt', 'r')
# Reading the entire file
content = file.read()           # it's now one big string
# Closing the file
file.close()                    # Do not forget to close the file
# Printing the content
print(content)
```

We can iterate over each line of the file:

```python
# Opening a text file for reading
file = open('example.txt', 'r')
line_count = 0
for line in file:
    print(line)
    line_count += 1
file.close()                    # Do not forget to close the file
# Printing the content
print(f'{line_count} lines)
```

!!! note 

    To remove the new line character from the end of each line use `rstrip()`, where the 'r' here stands for 'right'.  Any trailing or preceding whitespace can also be stripped off using `strip()`

In the examples above the filename has been hardcoded but it's more usual to ask the user for the name of the file to use.  Of course this is better but also fraught as the user might make a typo, or misremember the name of the file and an exception error, `FileNotFoundError` will be returned.    In such cases we must wrap this request in a `try ... except` block.  It is best to *always* assume the request to `open()` the file will fail.  E.g.

```python
# Opening a text file for reading
filename = input('Enter filename: ')
try:
    file = open(filename, 'r')
except:
    print(f'File, {filename}, cannot be opened')
    exit()                      # quits the program
line_count = 0
for line in file:
    print(line)
    line_count += 1
file.close()                    # Do not forget to close the file
# Printing the content
print(f'{line_count} lines)
```

## Reading a file using `with open()`

In the previous examples we explicitly closed the file we had opened using the `close()` method on that file.  This is good practice and recommended but we can take a shortcut as it's so easy to forget to close the file:

```python
filename = input("Enter filename: ")
with open(filename, 'r') as file:
    contents = file.read()
print(contents)
```

When using the `with` statement the file will be automatically closed when it is no longer needed.  This assumes the file with that filename exists and can be found so it is good rpacticec to also wrap this statement in a `try ...except` block as before:

```python
try:
    # Open the file in a 'with' statement for automatic closing
    with open('filename.txt', 'r') as file:
        # Perform operations on the file
        content = file.read()
        # ... other file operations ...

except IOError as e:
    # Handle IOErrors, such as file not found or permission issues
    print(f"An IOError occurred: {e}")
    # Additional error handling code can be added here
```

!!! note 
    
    It is worth getting familiar with these constructs and always using `try...except` and `with open(...)` for all file handling operations.


## Writing to Text Files

To write to a text file, you can use the `write()` method and the `w` mode as the second parameter.

```python
# Opening a text file for writing
file = open('example.txt', 'w')
# Writing data to the file
file.write('Hello, World!')
# Closing the file
file.close()
```

!!! note 

    The `write()` function returns the number of characters that have been written.  In the example above this return value is not being assigned.

If the file already exists any existing data will be overwritten - so take care!  If the file has not been closed and subsequent calls to `write()` are made the new data will be appended to that file.

!!! hint

    When writing a line of text to a file make sure to include the newline character, `\n`.

## Reading and Writing Binary Files

For binary files, use the 'b' mode and methods like `read()`, `write()`, and `readinto()` for reading and writing binary data.

```python
# Reading binary data
with open('binary_data.bin', 'rb') as file:
    data = file.read()

# Writing binary data
with open('binary_data.bin', 'wb') as file:
    file.write(b'\x48\x65\x6c\x6c\x6f\x2c\x20\x57\x6f\x72\x6c\x64')
```

## Summary of reading/writing methods

In Python 3, there are several methods and techniques for reading and writing data to a text file. Here are some commonly used methods:

### Reading Data from a Text File:

1. **`read()` Method:**
   - The `read()` method reads the entire content of the file as a single string.
   - Example:
     ```python
     with open('example.txt', 'r') as file:
         content = file.read()
     ```

2. **`readline()` Method:**
   - The `readline()` method reads one line at a time from the file.
   - Example:
     ```python
     with open('example.txt', 'r') as file:
         line = file.readline()
         while line:
             # Process the line
             line = file.readline()
     ```

3. **`readlines()` Method:**
   - The `readlines()` method reads all lines from the file and returns them as a list of strings.
   - Example:
     ```python
     with open('example.txt', 'r') as file:
         lines = file.readlines()
     ```

4. **Iterating Through File Object:**
   - You can iterate directly through the file object itself to read lines one by one.
   - Example:
     ```python
     with open('example.txt', 'r') as file:
         for line in file:
             # Process the line
     ```

### Writing Data to a Text File:

1. **`write()` Method:**
   - The `write()` method is used to write a string to the file.
   - Example:
     ```python
     with open('output.txt', 'w') as file:
         file.write("Hello, World!")
     ```

2. **`writelines()` Method:**
   - The `writelines()` method writes a list of strings to the file, typically after joining them together.
   - Example:
     ```python
     lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
     with open('output.txt', 'w') as file:
         file.writelines(lines)
     ```

3. **Using the `print()` Function:**
   - You can use the `print()` function to write text to a file by specifying the `file` parameter.
   - Example:
     ```python
     with open('output.txt', 'w') as file:
         print("Hello, World!", file=file)
     ```

4. **Appending Data:**
   - To append data to an existing file, open it in 'a' (append) mode instead of 'w' (write) mode.
   - Example:
     ```python
     with open('existing.txt', 'a') as file:
         file.write("Appending data to the file.")
     ```

## Climate Quest Project

![](../../assets/images/climate-quest.png){align=left width="200"}

Throughout this topic we'll be working on a large scale project: **Climate Quest**.  In this project a player embarks on a journey to combat the effects of climate change by making decisions that impact the environment. Each choice affects the outcome of the game, emphasizing the importance of individual actions in addressing climate change.

[Go to task 11 - File Handling](./climate_quest/task_11.md){:class=md-button}

## Summary

[Cheat sheet for exceptions (and files)](../../files/beginners_python_cheat_sheet_pcc_files_exceptions.pdf){:class=md-button}[^source]

[^source]: [https://ehmatthes.github.io/pcc_3e/cheat_sheets/(https://ehmatthes.github.io/pcc_3e/cheat_sheets/)]

## Questions

{{ show_questions(page.title, page.meta.filename) }}

## Programming Tasks

{{ get_programming_tasks(page.title)}}