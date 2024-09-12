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

## Reading from a text file

**Obtain a handle to the file**

```
my_file = openRead('sample.txt')
```

