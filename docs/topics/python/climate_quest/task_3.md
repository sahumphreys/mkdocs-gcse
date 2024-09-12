---
title: Climate Quest - Task 3
---

![](../../../assets/images/climate-quest.png){align=right width="100"}

# {{ title }}

The objective of this task is to introduce you to **strings** in Python. You will learn how to create, manipulate, and format strings, as well as use common string methods. You will extend the "Climate Quest" game to incorporate these string concepts.

!!! note "Learning Outcomes"

      By the end of this task, you should be able to:

      1. Understand the nature and importance of strings as a fundamental data type in Python.
      2. Create, manipulate, and format strings using various techniques.
      3. Use common string methods and their applications.
      4. Index, slice, and find the length of strings.
      5. Understand the concept of string immutability.
      6. Gain practical experience through programming tasks related to strings.

## Task Description:

You will enhance the "Climate Quest" game by adding functionality that involves string manipulation and formatting. You will also learn about string methods and slicing to improve the game's interaction with the player.

## Steps to Complete the Task:

1. **String Creation and Concatenation**:

      - Create strings and concatenate them to form messages.

2. **String Methods**:

      - Use common string methods to manipulate and format strings.

3. **Indexing and Slicing**:

      - Use indexing and slicing to extract specific parts of strings.

4. **String Formatting**:  

      - Format strings to display dynamic information.

5. **String Immutability**:
   
      - Understand and demonstrate the immutability of strings in Python.

## Skeleton Code:

Below is a skeleton of the code with questions embedded. Follow the steps to complete your own version.

```python
# Welcome Message
print("Welcome to Climate Quest!")
print("The environment is facing serious challenges due to climate change.")
print("Your mission is to make decisions that help mitigate these effects and protect the planet.")

# Get User Input
# ----------------------------------------------------------------
# Q1: Write code to ask the user for their name
                                    # complete this line

# Q2: Write code to greet the user with the message:
# "Hello, Emma!  Your mission is to protect the planet"
# (Replacing the name entered for question 1 and not "Emma"!)                                    
print(f"Hello, {player_name}! Your mission is to protect the planet.")
# ----------------------------------------------------------------

# Environmental Health Initialization
environment_health = 100
print(f"Initial environmental health: {environment_health}")

# String Creation and Concatenation
# ----------------------------------------------------------------
# Q3: Create a message that includes the player name using concatenation
welcome_message =                    # Complete this line
print(welcome_message)


# String Methods
# ----------------------------------------------------------------
# Convert the player's name to uppercase and display it
# Q4: Convert the player's name to uppercase and display it. 
# What method will you use to convert a string to uppercase?
uppercase_name =                    # Complete this line
print(f"The name of the player in uppercase: {uppercase_name}")

# Replace a word in the welcome_message
# ----------------------------------------------------------------
# Q5: Using a string method, replace "Welcome" with 
# "Greetings" in the welcome_message
welcome_message =                   # Complete this line
print(welcome_message)

# Indexing and Slicing
# ----------------------------------------------------------------
# Q6: Display the first and last character of the player's name
first_char =                        # Complete this line
last_char =                         # Complete this line
print(f"The first character of your name: {first_char}")
print(f"The last character of your name: {last_char}")

# Display the first three characters of the city name
# ----------------------------------------------------------------
# Q7: Use slicing to get the first three characters of player's name
first_three_chars =                 # Complete this line
print(f"The first three characters of your name: {first_three_chars}")

# String Formatting
# ----------------------------------------------------------------
# Create a formatted string that includes the player's name and environmental health
# Q8: Use an f-string to include the player's name and environmental health in a message
formatted_message =                 # Complete this line
print(formatted_message)

# String Immutability
# Demonstrate that strings are immutable
# Try to change the first character of the player's name (this should result in an error)
# Uncomment the next line to see the error
# player_name[0] = 'X'  # This line should raise a TypeError

# Explain why the above operation is not allowed in Python
# Q9: Why can't we change a single character in a string directly?

# Final Environmental Health Message
final_message = "Thank you for playing Climate Quest!"
print(final_message)
```

## Exercises

1. **Start a New Python File**:
  
      - Open your Python editor or an online Python compiler.
      - Create a new file and save it as `climate_quest_task3.py`.

2. **Write the Code**:
   
      - Follow the skeleton code provided above to write your own code.
      - Answer the embedded questions and complete the lines of code where indicated.
      - Make sure to test your code after each step to ensure it works correctly.

3. **Experiment with String Methods**:
   
      - Try different string methods such as `.lower()`, `.title()`, and `.find()`.
      - Explore how these methods can be used to manipulate strings in the game.

4. **Understand String Immutability**:
   
      - Try to modify a string directly and observe the resulting error.
      - Understand why strings are immutable in Python.

5. **Test Your Program**:
   
      - Run your program to ensure that it correctly performs string manipulations and displays the desired output.

## Questions for Reflection:

1. What are some common string methods you used in this task?
2. How does string indexing and slicing work in Python?
3. Why are strings immutable, and what are the implications of this immutability?

## Extension Activity (Optional):
- Add more interactive elements to the game using string manipulations.
- Try creating multi-line strings and formatting them in different ways.
