---
title: SQL
image: 'databases.png'
---

![](../../assets/images/topics/{{image}}){width="100"; align=right}

# {{ title }}

!!! note "Objectives"

    - learn how to use `SELECT`, `FROM`, and `WHERE` to retrieve and filter data from a relational database.
    - apply the `ORDER BY` clause to sort results in ascending (`ASC`) or descending (`DESC`) order based on specified columns.
    - gain an understanding of how to use SQL to query data from more than one table using joins or table references.
    - use the `INSERT INTO` command to add new data into specific tables of a relational database.
    - use the `UPDATE` and `DELETE` commands to modify or remove records based on specified conditions within the database.

**SQL (Structured Query Language)** is a programming language used to manage and interact with relational databases. You will primarily use it to **retrieve**, **insert**, **update**, and **delete** data. Here’s a breakdown of key SQL commands that you need to know:


## The SELECT Statement

The `SELECT` statement is used to retrieve data from a database.

**Basic Syntax:**
```sql
SELECT column1, column2, ... 
FROM table_name;
```

- **SELECT**: Specifies the columns you want to retrieve.
- **FROM**: Indicates the table from which to fetch the data.

**Example:**
```sql
SELECT StudentName, Age 
FROM Students;
```
This retrieves the `StudentName` and `Age` columns from the `Students` table.

## Using WHERE to Filter Data

The `WHERE` clause is used to filter records based on a condition.

**Basic Syntax:**
```sql
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```

- **WHERE**: Specifies the condition that must be met for a record to be included in the results.

**Example:**
```sql
SELECT StudentName, Age 
FROM Students
WHERE Age > 15;
```
This retrieves the `StudentName` and `Age` of students who are older than 15.

## Sorting Results with ORDER BY

The `ORDER BY` clause is used to sort the result set in ascending or descending order.

**Basic Syntax:**
```sql
SELECT column1, column2, ...
FROM table_name
ORDER BY column1 [ASC | DESC];
```

- **ASC**: Sorts the data in ascending order (default).
- **DESC**: Sorts the data in descending order.

**Example:**
```sql
SELECT StudentName, Age 
FROM Students
ORDER BY Age DESC;
```
This retrieves the `StudentName` and `Age`, and sorts the result by `Age` in descending order (from oldest to youngest).

## Using SQL with Two Tables

You can extract data from more than one table by using `JOIN` or simply referencing multiple tables.

**Example with Two Tables:**
```sql
SELECT Students.StudentName, Classes.ClassName 
FROM Students, Enrollment, Classes
WHERE Students.StudentID = Enrollment.StudentID 
AND Classes.ClassID = Enrollment.ClassID;
```
This retrieves the `StudentName` and `ClassName` by combining the `Students`, `Enrollment`, and `Classes` tables using relationships between the tables.

## Inserting Data into a Relational Database

You can add new records to a table using the `INSERT INTO` statement.

**Basic Syntax:**
```sql
INSERT INTO table_name (column1, column2, ...)
VALUES (value1, value2, ...);
```

- **INSERT INTO**: Specifies the table into which the data will be inserted.
- **VALUES**: Provides the actual data for the columns.

**Example:**
```sql
INSERT INTO Students (StudentID, StudentName, Age)
VALUES (4, 'Emily Green', 17);
```
This inserts a new student record with ID `4`, name `Emily Green`, and age `17` into the `Students` table.

## Editing and Deleting Data in a Database

You can modify or delete existing records in a database using the `UPDATE` and `DELETE` commands.

### **Updating Data with the UPDATE Statement**

The `UPDATE` statement is used to change existing data in a table.

**Basic Syntax:**
```sql
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```

- **SET**: Specifies the columns and their new values.
- **WHERE**: Defines the condition to specify which rows should be updated.

**Example:**
```sql
UPDATE Students
SET Age = 18
WHERE StudentName = 'John Doe';
```
This updates the `Age` of the student named 'John Doe' to `18`.

## **Deleting Data with the DELETE Statement**

The `DELETE` statement is used to remove records from a table.

**Basic Syntax:**
```sql
DELETE FROM table_name
WHERE condition;
```

- **DELETE FROM**: Specifies the table from which to delete records.
- **WHERE**: Sets the condition that defines which rows to delete.

**Example:**
```sql
DELETE FROM Students
WHERE StudentID = 4;
```
This deletes the student with `StudentID` of `4` from the `Students` table.

## Summary of SQL Commands

| **Command** | **Purpose** | **Example** |
|-------------|-------------|-------------|
| `SELECT`    | Retrieve data from a table. | `SELECT StudentName FROM Students;` |
| `FROM`      | Specifies the table from which data is retrieved. | `SELECT * FROM Students;` |
| `WHERE`     | Filters records based on a condition. | `SELECT * FROM Students WHERE Age = 16;` |
| `ORDER BY`  | Sorts data in ascending or descending order. | `SELECT * FROM Students ORDER BY Age DESC;` |
| `INSERT INTO` | Inserts new data into a table. | `INSERT INTO Students (StudentID, StudentName, Age) VALUES (1, 'John Doe', 16);` |
| `UPDATE`    | Updates existing data in a table. | `UPDATE Students SET Age = 17 WHERE StudentID = 1;` |
| `DELETE`    | Deletes data from a table. | `DELETE FROM Students WHERE StudentID = 1;` |

These commands allow you to manage and interact with a relational database effectively, handling everything from simple data retrieval to complex data manipulation.