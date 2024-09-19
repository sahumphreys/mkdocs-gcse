---
title: Worked Example
image: 'databases.png'
filename: '_data/database_questions.json'
---

![](../../assets/images/topics/{{image}}){width="100"; align=right}

# {{ title }}

!!! note "Objectives"

    - To develop understanding of a relational database
    - Work through an example of creating a database from a flat-file representation

In this worked example, we will take data currently stored in a flat-file system i.e. a spreadsheet and convert it into a relational database. The example will involve two tables: `Students` and `Classes`.


## Understanding Flat-File Systems (Spreadsheet Example)

A flat-file system stores all data in a single table, such as a spreadsheet. All information is kept in rows and columns without relationships between separate pieces of data. Flat-file systems can lead to redundancy (duplicate data) and inconsistency (conflicting data).

**Example Scenario:**  

Consider a simple school system stored in a spreadsheet where data about students and their enrolled classes are stored in one large table.

**Flat-file Spreadsheet Example:**

| StudentID | Student Name | Age | ClassID | Class Name | Teacher | Room Number |
|-----------|--------------|-----|---------|------------|---------|-------------|
| 1         | John Doe     | 16  | C001    | Maths      | Mr. Smith | 101         |
| 1         | John Doe     | 16  | C002    | Science    | Mrs. Johnson | 102         |
| 2         | Jane Roe     | 15  | C001    | Maths      | Mr. Smith | 101         |
| 2         | Jane Roe     | 15  | C003    | History    | Mr. Brown  | 201         |
| 3         | Sam White    | 16  | C002    | Science    | Mrs. Johnson | 102         |


## Problems with Flat-File Systems

In the above example, student details like `Student Name` and `Age` are repeated for every class a student is enrolled in.

Information about the class, such as `Teacher` and `Room Number`, is also repeated for each student in the class.

Thus, there is **redundant data**:

- John Doe's information (Name: "John Doe", Age: 16) is duplicated in both the Maths and Science classes.
- The details about the Maths class (`Class Name: Maths, Teacher: Mr. Smith, Room: 101`) are repeated for each student taking that class.

This redundancy can lead to problems:

- If John Doe’s age changes or if a teacher is reassigned, it must be updated in every occurrence in the spreadsheet. Missing updates may lead to conflicting or incorrect data.

- If John Doe’s age is updated in one row but not in the others, the system will have conflicting records of his age.

When you have this problem is is known as **data inconsistency**, you don;t know which version of the data is actually correct and can be relied upon.

**Limited Scalability and Poor Data Management:**  

Also, as the number of students and classes grows, managing the spreadsheet becomes more difficult and error-prone.  The errors can become compounded until it is just to difficult to work with.

## Converting the Flat-File into a Relational Database

To solve these problems, we can split the single flat-file into **two related tables**:  

1. **Students**: Contains information about the students.
2. **Classes**: Contains information about the classes.

We extract just the Student data first and create a students table pulling across the columns for:

- StudentID
- Student Name
- Age

** `Student` table

| **StudentID (Primary Key)** | **Student Name** | **Age** |
|-----------------------------|------------------|---------|
| 1                           | John Doe         | 16      |
| 2                           | Jane Roe         | 15      |
| 3                           | Sam White        | 16      |

We only need one **record**, or row, for each student in the system.  There are three columns, we call the columns **attributes** or **fields**.

The **StudentId** field uniquely identifies each student.  Wwe may have another student also called "Sam White".  If so, that student would need their own own in our table and be given a *different* student id to distinguish them from the other Sam White. No two students can have the same primary key.

This attribute is really important in relational databases, and is known as the **primary key**.

We do the same thing for the teachers and classes data as well pulling across the columns for:

- ClassID
- Class Name
- Teacher
- Room Number

**`Class` Table:**

| **ClassID (Primary Key)** | **Class Name** | **Teacher**      | **Room Number** |
|---------------------------|----------------|------------------|-----------------|
| C001                      | Maths          | Mr. Smith        | 101             |
| C002                      | Science        | Mrs. Johnson     | 102             |
| C003                      | History        | Mr. Brown        | 201             |

Again, each class is given a unique identifier for each row in the table, the **primary key** which is the ClassId in this example.

!!! note 

    The tables are named in their singular form i.e. `Student` and `Class` rather than `Students` and `Classes`.  This is good practice.


## Creating the relationship

However, we have now lost the connection between these two items of data.  We no longer know which student is in which class!  This needs to be corrected and is one of the most challenging aspects of designing the relational database structure.

### Degrees of relationship

Firstly, there are three **degrees of relationship**:

- One-to-One
- One-to-Many
- Many-to-Many

To work out the degree of relationship between these two tables we need to ask ourselves **two** questions, each from the perspective of each table.  Each question begins with the word "*One*".  The answer to the question will either be "*One*" or "*Many*".

Thus:

- One student is enrolled in how many classes?
- One class has how many students enrolled?

From our flat file system we can see the answer in both cases will be "*Many*".  Therefore, we have a Many-to-Many relationship.

To represent the Many-to-Many relationship between students and the classes they are enrolled in, we need an additional table called a **linking table** (or junction table). This will record which students are enrolled in which classes.

**`Enrollment` Table (Linking Table):**

| **StudentID (Foreign Key)** | **ClassID (Foreign Key)** |
|-----------------------------|---------------------------|
| 1                           | C001                      |
| 1                           | C002                      |
| 2                           | C001                      |
| 2                           | C003                      |
| 3                           | C002                      |

Thus, from our initial flat file system we have ended up with 3 tables:

- Student
- Class
- Enrollment

**Foreign Keys:**  

The `StudentID` and `ClassID` fields in the enrollment table are known as **foreign keys**. They refer to the primary keys in the `Students` and `Classes` tables, respectively, establishing a relationship between the tables.

## Other relationships

We could develop our system further and look at the relationship between a teacher and a subject.  It may be a requirement of the system that one teacher only teachers one subject.  The questions we would ask, therefore, would be:

- One teacher teaches how many subjects?
- One subject is taught by how many teachers?

Here are answers would be "*One*" and "*Many*".  Therefore, we would establish a One-to-Many relationship between the teacher and the subject.

Thus, we would create a table for **Subject**

| **SubjectId** | **Subject** |
|:-------------:|-------------|
| 1             | Maths       |
| 2             | Science     |
| 3             | History     |

To maintain the relationship between the teacher and the subject, e would import the primary key from the Subject table as a foreign key in the teacher table:

| **TeacherID** | **Name**    | **SubjectID** |
|:-------------:|-------------|:-------------:|
| 1             | Mr Smith    | 1             |
| 2             | Mrs Johnson | 2             |
| 3             | Mr Brown    | 3             |

!!! note

    One-to-one relationships do occur, though they are rare, and when they happen they are usually included as an attribute in the main table

## Data types

Each item of data will be a given data type.  This should be familiar room the programming topic though unlike Python the database management system being used to hold the database will require the data type to be defined.

In our example:

- The StudentId will be a positive whole number, i.e. an integer
- The Teacher Name will be characters, i.e. a string
- etc..

## How the Relational Database Solves Problems

a) **Elimination of Data Redundancy**

- By separating the student and class data into two tables, information about students and classes is stored only **once**.
- **Example:** John Doe’s details are only stored once in the `Student` table, and the `Maths` class details are only stored once in the `Class` table. There is no need for repetition.

b) **Prevention of Data Inconsistency**

- Updating data is easier and more reliable. If John Doe’s age changes, you only need to update his record in the `Student` table. This change will automatically apply to every class he is enrolled in through the `Enrollment` table.
- Similarly, if a teacher is reassigned or a class room number changes, the update only needs to be made in the `Class` table.

c) **Scalability and Efficient Data Management**

- Adding new students or classes is straightforward. You can simply add new records to the `Student` or `Class` tables and link them in the `Enrollment` table.
- Searching, filtering, and updating data across a relational database is much easier compared to a flat-file system, especially when handling large amounts of data.

## Database Terminology

A summary table of some of these key terms:

| Term | Definition |
|------|------------|
|Table | A collection of records, each with the same structure (a collection of columns) |
|Record| A group of related fields, representing one data entry (a row) |
|Field | A single item of data in a record, also known as an attribute (a column) |
|Data type | The type of data being held ina field e.g. string, integer etc |
|Primary Key | A unique identifier for each record/row in the table |
|Foreign Key | A field in a table that references a primary key in another table.  Used to link tables together and create a relationship between those tables |

## Summary

1. **Data Redundancy is Reduced:**  
   Information is only stored once in its appropriate table. Relationships between the tables link data together.

2. **Data Inconsistency is Prevented:**  
   Data updates are made in one place, ensuring there are no conflicting versions of the same data.

3. **Efficient Data Management and Scalability:**  
   Relational databases are easy to scale. Adding, removing, or updating data does not create excessive duplication or management issues.


## Questions

{{ show_questions(page.title, page.meta.filename) }}
