---
title: Climate Quest - Task 6
---

![](../../../assets/images/climate-quest.png){align=right width="100"}

# {{ title }}


!!! note "Objectives"

    - Understand selection in algorithms and code.
    - Define the purpose of selection (conditional statements) in programming.
    - Learn the syntax of `if`, `elif`, and `else` statements in Python.
    - List and explain the relational operators used in conditions (e.g., `==`, `!=`, `>`, `<`, `>=`, `<=`).
    - Review examples of conditional statements.
    - Define the role of the `elif` statement in handling multiple conditions.
    - Differentiate the use of `elif` from `if` and `else`.

## Task Overview:

In this homework, you will enhance the "Climate Quest" project by incorporating selection statements (`if`, `elif`, and `else`) to make decisions within the game. These decisions will impact the gameplay based on the player's choices and environmental conditions.

There are two main occasions when a selection is required:

- User is presented with the menu of locations and is asked to select one to visit
- In that location, user is presented with up to 3 actions and to choose one of those actions

## Instructions:

1. **Process the location selection from the menu**

    - Get the location choice from the user
    - Select the correct location challenge function based on that choice
 
2. **Add Selection Statements in Challenges:**
  
      - In each location challenge the user is presented with 3 options to choose from
      - Add functionality to process this choice

3. **Role of `elif`:**
   
      - Demonstrate the role of `elif` in handling multiple conditions.

## Detailed Steps:

1. **Add Selection statements for the main menu**

    Having displayed the main manu of locations, get the user choice and branch to the selected location:

    ```python
    def main():
        display_menu()
        choice = get_valid_input("Choose a challenge (1-6): ")

        if choice == 1:
            forest_challenge()
        elif choice == 2:
            ocean_challenge()
        # etc..
    ```

2. **Add selection statements for each of the challenges**

    Each challenge contains three options.  Add these options and get the choice made by the user.

    ```python
    def forest_challenge():
    print("\nForest Challenge")
    print(f"{player_name}: You encounter loggers in a forest. What will you do?")
    print("1. Confront the loggers")
    print("2. Start a tree-planting initiative")
    print("3. Ignore the situation")

    choice = get_valid_input("Choose an action (1-3): ")

    # add the selection statements here. For each choice print a suitable response about the impact that choice will have on climate change:

    ```

3. **Selection Statements for the final comment**

    - To practice working with relational operators, when the game is complete there will be a final score representing the impact the choices have had on climate change.  
    - Assuming the score starts at 0, this will be added to as the game progresses.  
    - Positive impacts will increase the score, negative impacts will decrease the score.  
    - When the game is complete the final score should be presented to the user and a comment selected based on that final score.  
    - For example, if the score is greater than, say, 10 the comment might be "Great job!  There has been a major improvement in the state of the climate".  
    - Write a function `display_final_score(score)` that displays a different comment based on the final score
    ```

4. **Define Relational Operators:**

    Explain the relational operators used in the conditions within the function. For example:
    - `>`: Greater than
    - `>=`: Greater than or equal to
    - `<`: Less than
    - `<=`: Less than or equal to
    - `==`: Equal to
    - `!=`: Not equal to

5. **Role of `elif`:**

    The `elif` statement allows you to check multiple conditions. It stands for "else if" and is used when you need to handle more than two conditions.

6. **Add the score variable**

    As each challenge is completed, and each choice made in a location a `score` variable will need to be updated.  Add this variable to the challenge functions.

### Homework Questions:

1. **Add Selection Statements:**
  
      - Enhance the `ocean_challenge()` and `forest_challenge()` functions to use `if`, `elif`, and `else` statements for different scenarios based on user input.

2. **Define Relational Operators:**
   
      - Identify and explain the relational operators used in your conditions for the final comment.

3. **Role of `elif`:**
   
      - Describe the role of the `elif` statement in handling multiple conditions. How is it different from `if` and `else`?

4. **Keeping score**

    - Maintain a score representing the environmental health of the planet that is updated each time the user visits a location and takes a decision
