---
title: Climate Quest - Task 1
---

![](../../../assets/images/climate-quest.png){align=right width="100"}
# {{ title}}


## Objective

The objective of this task is to introduce you to the basic concepts of programming in Python, including **variables**, output to the screen using `print()`, and input from the keyboard using `input()`. You will create the initial part of the "Climate Quest" game, where the game starts with an introduction and displays a simple menu.

!!! note "Learning Outcomes"

    By the end of this task, you should be able to:

    1. Declare and use variables.
    2. Use the `print()` function to output text to the screen.
    3. Use the `input()` function to get user input from the keyboard.

## Task Description

You will write a Python program that:

1. Welcomes the player to the "Climate Quest" game.
2. Asks the player for their name.
3. Stores the player's input in a variable.
4. Displays a welcome message including the name of the player.

## Steps to Complete the Task

1. **Welcome Message**:  

    - Use the `print()` function to display the title of the game
    - Use the `print()` function to display a welcome message for the game.

2. **Get User Input**:
    
    - Use the `input()` function to ask the player for their name.
    - Store the player's input in a variable.

3. **Display Welcome Message with City Name**:
   
    - Use the `print()` function to display a welcome message that includes the name of the player entered by the player.

??? hint "Only open this section if _really_ stuck"

    ```python
    # Step 1: Welcome Message
    print("Welcome to Climate Quest!")

    # Step 2: Get User Input
    player_name = input("What is your name? ")

    # Step 3: Display Welcome Message with City Name
    print(f"Hello, {player_name}! Your mission is to protect the planet.")
    ```

## Exercise

1. **Start a New Python File**:
 
      - Open your Python editor or an online Python compiler.
      - Create a new file and save it as `climate_quest.py`.

2. **Write the Code**:
   
      - Write the code to meet the specification
      - Make sure to test your code after each step to ensure it works correctly.

3. **Enhance the Welcome Message**:
   
      - Modify the welcome message to include more details about the game. For example:
     
        ```python
        print("Welcome to Climate Quest!")
        print("The environment is facing serious challenges due to climate change.")
        print("Your mission is to make decisions that help mitigate these effects and protect the planet.")
        ```

4. **Test Your Program**:
   
      - Run your program to ensure that it correctly asks for the name of the player and displays the welcome message with the player's name.

## Questions for Reflection

1. What is the purpose of using variables in a program?
2. How does the `input()` function work in Python?
3. Why is it important to test your code after writing each part?

## Extension Activity (Optional)

- Experiment with different welcome messages and inputs.
- Try using different variable names and see how it affects your program.
