---
title: File Handling
image: programming.jpg
filename: '_data/data_questions.json'
---

![](../../assets/images/topics/{{image}}){width="100"; align=right}

# {{ title}}

Reading and writing data to and from a file is an important process for most programs - where it is required.  For GCSE we only need to concern ourselves with **text files**, that is files that contain raw ASCII data.  Many programs will also save and read files in different formats loosely termed **binary files**.  These will not be considered here.

The process is not that complicated:

- obtain a **handle** to the file
- process the file by **reading** its contents into a variable, or **writing** the contents of a variable to the file
- close the file

A text file consists of a sequence of lines of text in the file e.g.

```
// file1.txt
radar
rotor
madam
```

Or, it might be a series of **records**.

### Records

The record has fallen out of favour in preference for other ways of organising data e.g. lists, or tuples but it does appear in the AQA syllabus.  So for completeness, a **record** is a data structure that contains a number fields, each field can be a different data type.

**Example**

```
type student = record
    studentId : integer
    first_name : string[15]         // 15 characters available for this field
    last_name : string[25]
    year_born : integer
end;
```

To clarify, Python does not have the concept of a **record**.  It does not need one as other data structures such as dictionary that work just as well if not better:

```python
student = {
    'studentId': 123,
    'first_name': 'Harry',
    'last_name': 'Jones',
    'year_born': 2007
}
```

The `collections` library also has a `namedtuple` data structure:

```python
from collection import namedtuple

Student = namedTuple('Student', ['studentId', 'first_name', 'last_name', 'year_born'])

student = Student(123, 'Harry', 'Jones', 1990)
```

We could (though it's not recommended) store the same data as a list:

```python
student = [123, 'Harry', 'Jones', 2007]
```
However, this is not as readable or maintainable as the other two examples.

## Reading from a text file

Assume we have a file of students, `students.txt`:

```
123, Harry, Jones, 2007
129, Ben, Davies, 2008
130, Mai Ling, Li, 2007
```

Each line in the file is a **record**, typically several fields separated by commas.  Each row represents one student.  This structure is also known as a **comma separated value** file, or **CSV**.

**Obtain a handle to the file**

```
my_file = openRead('student.txt')
```

Typically, when we open a file we will be opening to perform **one** type of action, or **mode**:

- **write**: allows writing to the file, usually overwriting any existing content
- **append**: adds data to the end of the file
- **read**: allows reading from the file

When we open the file we get back a **file handle**, essentially we're asking the operating system to grant us access to that file.  The OS returns a unique identifier, commonly known as the file handle.  It's a special key that allows us to interact with the file.  But, it is not the file itself!

**Process the file contents**

We want to read the contents of the file, the contents need to be put somewhere, i.e. assigned to a variable.  We might want all the lines in the file, or we might want to process each line one at a time.

Example:

```
student_file = open('students.txt')     // get a "handle" for the file
while not student_EOF()                 // EOF = End Of File
    line = student_file.readLine()      // read one line of the file
    print(line)
endwhile
student_file.close()                    // close the file handle
```

## Writing to a text file

The following should be straightforward:

```
student_file = open('students.txt')
id = int(input("Enter student id: "))
first_name = input("Enter student first name: ")
last_name = input("Enter student last name: ")
year_of_birth = int(input("Enter student year of birth: "))
student_file.writeLine(id + ", " + first_name + ", " + last_name + ", " + year_of_birth + "\n")
student_file.close()
```

**Take particular note of the `\n` at the end of the string in line 6.  This is the new line character and ensures any subsequent record is written to the next line of the file.**

## Closing the file

In the previous examples we used `student_file.close()`.  It is important to close any file when it is no longer needed:

- Frees up memory
- File cannot be processed when it is closed


**AQA Pseudocode**

There are no file handling functions in the AQA pseudocode.

**OCR Pseudocode**

The following functions are specified as part of the OCR pseudocode:


| Function | Description | Example |
|----------|-------------|---------|
| `openRead(file)` | Open a file to read | `file = openRead('students.txt')` |
| `readLine()` | Read a line from the file | `line = file.readLine()` |
| `endOfFile()` | Determines when the end of the file has been reached | `while not file.endOfFile()` |
| `openWrite(file)` | Open a file for writing | `file = openWrite('students.txt')` |
| `writeLine()` | Write a line to the file | `file.writeLine(line)` |
| `close()` | Close the file | `file.close()` |