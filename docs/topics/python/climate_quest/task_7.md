---
title: Climate Quest - Task 7
---

![](../../../assets/images/climate-quest.png){align=right width="100"}

# {{ title }}


!!! note "Objectives"

    - Define iteration in programming and its importance.
    - Recognize the concept of loops as a fundamental element of iteration.
    - Differentiate between `for` and `while` loops in Python.
    - Explain when to use a `for` loop and when to use a `while` loop.
    - Describe the purpose of the `range()` function in `for` loops.
    - Illustrate the use of `for` loops to iterate over sequences like lists, tuples, and strings.
    - Explain the concept of nested `for` loops and demonstrate their use with examples.
    - Understand the structure of a `while` loop in Python.
    - Compare and contrast `for` loops and `while` loops.

## Task Overview:

In this homework, you will enhance the "Climate Quest" project by incorporating iteration. You will use `for` and `while` loops to handle repeated tasks and processes within the game. This will make the code more efficient and introduce the concept of looping through sequences and repeating actions.

## Instructions:

1. **Use `for` Loops to Iterate Over Sequences:**

    - Implement `for` loops to handle repeated actions in the game, such as iterating over challenges.

2. **Use `while` Loops for Repeated Actions:**
   
    - Implement `while` loops for conditions where the repetition depends on a condition, such as continuing the game until a certain condition is met.

3. **Nested `for` Loops:**
   
    - Use nested `for` loops where appropriate, for example, when dealing with multiple elements within a challenge.

### Detailed Steps:

Experiment with two different approaches to the game:

- The user visits a predetermined number of locations, say 3, as part of the game
- The user has to visit all of the locations before being presented with a final challenge

In both instances the main menu will have to be returned to and presented to the user, either for a set number of times, or until all locations have been visited

1. **Use `for` Loops to Iterate Over Sequences:**

    Update the main gameplay loop to use a `for` loop to iterate over a predefined number of challenges provided by the `range()` function:

    ```python
    def main():
        
        # Gameplay Loop
        for _ in range(3):  # Example loop for 3 challenges
            display_menu()
            location = get_valid_input("Choose a challenge (1-6): ")
            if location == 1:
                environment_health = ocean_challenge(environment_health)
            elif location == 2:
                environment_health = forest_challenge(environment_health)
            elif location == 3:
                environment_health = city_challenge(environment_health)
            # etc..
            display_message(f"Updated environmental health: {environment_health}")

        # End Game
        display_message("Thank you for playing Climate Quest!")
    ```

2. **Use `while` Loops for Repeated Actions:**

    Repeat the previous exercise but this time using a `while` loop.  For this exercise there will be 2 conditions:

    - while score > 0 and visited_locations < 6:

    Adjust the `main()` function to display the menu while these two conditions are `True`.
    

## Example Homework Questions:

1. **Use `for` Loops to Iterate Over Sequences:**
   
    - Refactor your main gameplay loop to use a `for` loop to iterate over a predefined number of challenges.

2. **Use `while` Loops for Repeated Actions:**
   
    - Modify your main gameplay loop to use a `while` loop to continue the game until the environmental health drops below a certain threshold.

