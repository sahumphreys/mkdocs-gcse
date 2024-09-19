---
title: Relational Databases
image: 'databases.png'
filename: '_data/networking_questions.json'
---

![](../../assets/images/topics/{{image}}){width="100"; align=right}

# {{ title }}

!!! note "Objectives"

    - Explain the concept of a database.
    - Explain the concept of a relational database.
    - Understand key database concepts: tables, records, fields, data types, primary keys, and foreign keys.
    - Understand how relational databases help eliminate data inconsistency and data redundancy.


## What is a Database?
   
> A database is an organized collection of data that allows for easy access, management, and updating of information. It can be thought of as a digital filing system where data is stored and can be retrieved when needed.

For example: 

- A school system might use a database to store student information (names, grades, contact details, etc.).
- Online stores like Amazon use databases to track product information, customer orders, and inventory.

The key idea behind a database is they allow data to be stored systematically, making it easier to find specific information and perform tasks like searching, sorting, and filtering data.

## What is a Relational Database?
 
A relational database is a type of database that stores data in tables, where the data can be linked or related across different tables through common fields.


**Key Features:**

- **Tables:** The main structure that holds data in rows (records) and columns (fields).
- **Relationships:** Tables are connected (related) using keys (Primary Key and Foreign Key).
  
By analogy, imagine different folders (tables) in a filing cabinet, where each folder contains related information. A relational database lets you link these folders through a common identifier (like a student ID number). This way, you don’t have to store duplicate information in each folder.

For example:

- A school database could have one table for `Students` and another for `Classes`. The `Students` table would contain student details, and the `Classes` table would hold information about the subjects each student is enrolled in. The student ID could be used to link the two tables, creating a relationship between students and their classes.

## Key Database Concepts

a) **Table**

- **Definition:**  
  A table is a collection of data organized in rows and columns within a relational database.
  
- **Example:**  
  A table named `Students` might have columns like StudentID, Name, Age, and Address. Each row in the table represents one student.

b) **Record (Row)**

- **Definition:**  
  A record is a single, complete set of information in a table. Each row in the table is a record.
  
- **Example:**  
  In the `Students` table, a record would contain the details of one student, such as "John Doe, Age 16, Address: 123 Street."

c) **Field (Column)**

- **Definition:**  
  A field is a single piece of data, represented by a column in a table. It describes a specific attribute or characteristic of the data.
  
- **Example:**  
  In the `Students` table, fields might include Name, Age, and Address. Each of these is a field that holds specific data about the student.

d) **Data Type**

- **Definition:**  
  Data types specify the kind of data that can be stored in a field. Different fields might store text, numbers, dates, etc.
  
- **Common Data Types:**
  - **Text:** Used for names, addresses, etc.
  - **Integer:** Whole numbers, like age.
  - **Float/Decimal:** Numbers with decimal points, such as a price or percentage.
  - **Date/Time:** Used for storing dates and times.
  
- **Example:**  
  The `Age` field would likely use the Integer data type, while the `Name` field would use the Text data type.

e) **Primary Key**

- **Definition:**  
  A primary key is a unique identifier for each record in a table. It ensures that no two records are the same.
  
- **Key Feature:**  
  Every table must have one primary key to uniquely identify each record.
  
- **Example:**  
  In a `Students` table, the `StudentID` might be the primary key. Each student would have a unique StudentID.

f) **Foreign Key**

- **Definition:**  
  A foreign key is a field in one table that links to the primary key in another table, creating a relationship between the two tables.
  
- **Example:**  
  In the `Classes` table, the `StudentID` could be a foreign key, linking it to the `Students` table so that we know which students are enrolled in each class.

## Eliminating Data Inconsistency and Data Redundancy in Relational Databases

a) **Data Redundancy**

- **Definition:**  
  Data redundancy occurs when the same piece of data is stored in multiple places. This can lead to wasted storage space and make data harder to manage.

- **Example of Redundancy:**
  Imagine storing a student’s contact information in both the `Students` and `Classes` tables. If the contact details change, you’d have to update them in multiple places, which could cause errors.

b) **Data Inconsistency**
- **Definition:**  
  Data inconsistency arises when different copies of the same data do not match. This often happens as a result of data redundancy.

- **Example of Inconsistency:**
  If a student’s address changes but is updated in only one of the tables, the database will have conflicting information.

c) **How Relational Databases Eliminate Redundancy and Inconsistency**

- **By storing data in related tables, each piece of information is only stored once, reducing redundancy.**
- **Example:**  
  Instead of storing a student’s address in both the `Students` table and the `Classes` table, it’s stored only in the `Students` table. The `Classes` table only needs to store a foreign key (`StudentID`) to link the data.

- **This makes updates easier and helps prevent inconsistencies.**  
  If the student’s address changes, you only need to update it in one place (the `Students` table), and the change is reflected wherever that student’s data is used.

## Summary

- **Databases** store data in an organized way to make it easy to manage.
- **Relational databases** store data in tables that can be linked through relationships.
- Important concepts like **tables, records, fields, primary keys**, and **foreign keys** form the building blocks of relational databases.
- Relational databases **eliminate redundancy** (duplicate data) and **prevent inconsistency** (conflicting data).

## Questions

{{ show_questions(page.title, page.meta.filename) }}
