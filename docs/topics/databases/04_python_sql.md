---
title: Python and SQL
image: 'databases.png'
---

![](../../assets/images/topics/{{image}}){width="100"; align=right}

# {{ title }}



!!! note "Objectives"

    - Set up and interact with an SQLite3 database using Python
    - Create tables (`Students` and `Classes`), insert data, and establish relationships.
    - Query the database to retrieve, update, and manage data.

## SQLite3 and Python Tutorial: Managing Students and Classes

## Prerequisites:

To follow along with this tutorial the following software and knowledge will be needed:

- Install Python (version 3 or higher) on your system.
- Ensure you have the `sqlite3` library (it comes pre-installed with Python).
- Basic knowledge of Python syntax.

## Part 1: Setting Up the Database

### Step 1: Importing SQLite3 in Python

```python
import sqlite3
```

- `import sqlite3` allows you to use the SQLite3 database engine in Python. SQLite3 is a lightweight, file-based database system, ideal for small projects.

### Step 2: Creating a Connection to SQLite Database

```python
# Connect to (or create) a new database
conn = sqlite3.connect('school.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()
```

- `sqlite3.connect('school.db')` creates or connects to a database file called school.db. If the file doesn't exist, it will be created in the current directory.
- `cursor = conn.cursor()` creates a cursor object, which is used to execute SQL commands and interact with the database.

## Part 2: Creating Tables for `Students` and `Classes`

### Step 3: Creating the `Students` Table

```python
# SQL command to create the Students table
create_students_table = '''
CREATE TABLE IF NOT EXISTS Student (
    StudentID INTEGER PRIMARY KEY,
    StudentName TEXT NOT NULL,
    Age INTEGER
);
'''

# Execute the SQL command
cursor.execute(create_students_table)

# Commit the changes
conn.commit()
```

- `CREATE TABLE IF NOT EXISTS Student` creates a table called `Student` if it doesn't already exist. The table contains three columns or fields: `StudentID` (unique identifier), `StudentName`, and `Age`.
- `PRIMARY KEY` defines `StudentID` as a unique identifier for each student.
- 
### Step 4: Creating the `Class` Table

```python
# SQL command to create the Classes table
create_class_table = '''
CREATE TABLE IF NOT EXISTS Class (
    ClassID TEXT PRIMARY KEY,
    ClassName TEXT NOT NULL,
    Teacher TEXT,
    RoomNumber TEXT
);
'''

# Execute the SQL command
cursor.execute(create_classes_table)

# Commit the changes
conn.commit()
```

- This step creates a `Class` table with four columns: `ClassID` (unique identifier for the class), `ClassName`, `Teacher`, and `RoomNumber`.

!!! warning

    The identifier for each field must be a whole word, no spaces.  Think of it like an identifier for a variable and follow the same rules.

### Step 5: Creating the `Enrollment` Table (Linking Table)

```python
# SQL command to create the Enrollment table (links Students and Classes)
create_enrollment_table = '''
CREATE TABLE IF NOT EXISTS Enrollment (
    StudentID INTEGER,
    ClassID TEXT,
    FOREIGN KEY (StudentID) REFERENCES Student(StudentID),
    FOREIGN KEY (ClassID) REFERENCES Class(ClassID)
);
'''

# Execute the SQL command
cursor.execute(create_enrollment_table)

# Commit the changes
conn.commit()
```

- This table links the Student and Class tables. 
- `FOREIGN KEY` is used to establish relationships between `StudentID` in the `Enrollment` table and `StudentID` in the `Student` table, and between `ClassID` in `Enrollment` and `ClassID` in the `Class` table. This allows us to relate students to their classes.

## Part 3: Inserting Data into the Tables

### Step 6: Inserting Data into the `Students` Table

```python
# Insert sample students into the Students table
students = [
    (1, 'John Doe', 16),
    (2, 'Jane Roe', 15),
    (3, 'Sam White', 16)
]

cursor.executemany('INSERT INTO Students (StudentID, StudentName, Age) VALUES (?, ?, ?)', students)
conn.commit()
```

- `cursor.executemany()` is used to insert multiple rows into the Student table. Each tuple in the students list contains values for `StudentID`, `StudentName`, and `Age`.

### Step 7: Inserting Data into the `Classes` Table

```python
# Insert sample classes into the Classes table
classes = [
    ('C001', 'Maths', 'Mr. Smith', '101'),
    ('C002', 'Science', 'Mrs. Johnson', '102'),
    ('C003', 'History', 'Mr. Brown', '201')
]

cursor.executemany('INSERT INTO Classes (ClassID, ClassName, Teacher, RoomNumber) VALUES (?, ?, ?, ?)', classes)
conn.commit()
```

- Similar to the previous step, `executemany()` inserts multiple rows into the `Class` table. Each tuple contains the class details (`ClassID`, `ClassName`, `Teacher`, and `RoomNumber`).

### Step 8: Inserting Data into the `Enrollment` Table (Linking Table)

```python
# Link students to their enrolled classes using the Enrollment table
enrollments = [
    (1, 'C001'),
    (1, 'C002'),
    (2, 'C001'),
    (2, 'C003'),
    (3, 'C002')
]

cursor.executemany('INSERT INTO Enrollment (StudentID, ClassID) VALUES (?, ?)', enrollments)
conn.commit()
```

- This step links students to the classes they are enrolled in. Each tuple contains a StudentID and a ClassID, establishing relationships between students and their classes.

## Part 4: Querying the Database

### Step 9: Retrieving Students and Their Enrolled Classes

To fetch data, we can use a `JOIN` query that links the `Students` and `Classes` tables via the `Enrollment` table.

```python
# SQL query to retrieve students and their classes
query = '''
SELECT Student.StudentName, Student.Age, Class.ClassName, Class.Teacher
FROM Enrollment
JOIN Student ON Enrollment.StudentID = Student.StudentID
JOIN Class ON Enrollment.ClassID = Class.ClassID;
'''

# Execute the query and fetch the results
cursor.execute(query)
results = cursor.fetchall()

# Display the results
for row in results:
    print(f"Student: {row[0]}, Age: {row[1]}, Class: {row[2]}, Teacher: {row[3]}")
```

- The `JOIN` query connects the `Enrollment`, `Student`, and `Class` tables to retrieve information about which students are enrolled in which classes.

### Expected Output:

```
Student: John Doe, Age: 16, Class: Maths, Teacher: Mr. Smith
Student: John Doe, Age: 16, Class: Science, Teacher: Mrs. Johnson
Student: Jane Roe, Age: 15, Class: Maths, Teacher: Mr. Smith
Student: Jane Roe, Age: 15, Class: History, Teacher: Mr. Brown
Student: Sam White, Age: 16, Class: Science, Teacher: Mrs. Johnson
```

### Step 10: Retrieving Students in a Specific Class

Let's fetch the list of students enrolled in a specific class (e.g., `Maths`).

```python
# SQL query to retrieve students enrolled in Maths
query = '''
SELECT Student.StudentName, Student.Age
FROM Enrollment
JOIN Student ON Enrollment.StudentID = Student.StudentID
WHERE Enrollment.ClassID = 'C001';
'''

# Execute the query and fetch the results
cursor.execute(query)
results = cursor.fetchall()

# Display the results
print("Students enrolled in Maths:")
for row in results:
    print(f"Student: {row[0]}, Age: {row[1]}")
```

- This query uses a `WHERE` clause to filter students who are enrolled in a particular class (e.g., C001 for Maths).

### Expected Output:

```
Students enrolled in Maths:
Student: John Doe, Age: 16
Student: Jane Roe, Age: 15
```

## Part 5: Updating and Deleting Data

### Step 11: Updating Student Information

```python
# Update the age of 'Jane Roe' to 16
cursor.execute('UPDATE Student SET Age = 16 WHERE StudentName = "Jane Roe"')
conn.commit()

# Verify the change
cursor.execute('SELECT * FROM Student WHERE StudentName = "Jane Roe"')
print(cursor.fetchone())
```

- `UPDATE` is used to change data in the `Student` table. Here, we update the age of a student named "Jane Roe."
- After executing the update query, we use `SELECT` to verify that the change has been applied.

### Step 12: Deleting a Student Record

```python
# Delete 'Sam White' from the Students table
cursor.execute('DELETE FROM Students WHERE StudentName = "Sam White"')
conn.commit()

# Verify the deletion
cursor.execute('SELECT * FROM Students')
print(cursor.fetchall())
```

- `DELETE` removes a record from the `Student` table. In this case, we delete "Sam White" by specifying their name in the `WHERE` clause.

## Part 6: Closing the Database Connection

```python
# Close the connection when you're done
conn.close()
```

- `conn.close()` closes the connection to the database. This is important to free up resources and ensure that no uncommitted changes are lost.

## Summary:
In this tutorial, you’ve learned to:

- Set up a relational database with SQLite3 using Python.
- Create and populate tables (`Students`, `Classes`, `Enrollment`).
- Use SQL queries to retrieve, update, and delete data.
- Understand how tables relate to each other using primary and foreign keys.

