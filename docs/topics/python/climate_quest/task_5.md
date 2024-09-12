---
title: Climate Quest - Task 5
---

![](../../../assets/images/climate-quest.png){align=right width="100"}

# {{ title }}


!!! note "Objectives"

    - Understand the role of a `main()` function
    - Understand the concept of built-in functions in Python.
    - Learn how to use some commonly used built-in functions for math, strings, and basic input/output.
    - Explore the purpose and usage of functions like `print()`, `len()`, `input()`, and more.


## The `main()` function

In many programming languages, there is a designated starting point where the program begins execution. In Python, this convention is followed using a special function often called `main()`, along with a specific conditional statement to ensure that this function runs when the script is executed directly.

The `main()` function serves as the entry point for the program. It organizes the code and provides a clear structure, making the program easier to understand and maintain. 

For example:

```python
def main():
    # Your main program logic here
    print("Hello, World!")

main()
```

!!! tip

    For this task, and any future tasks, do not forget to include this entry point in your code.


## Task Overview:

In this homework, you will further develop the "Climate Quest" adventure game by incorporating several built-in functions, organizing the code with a `main()` function and writing a function to validate input from the user.


## Questions

1. **Create the `main()` Function:**
   
      - Refactor your existing code to include a `main()` function. Move the game initialization and the main gameplay loop into this function.

2. **Enhanced Welcome Message:**
   
      - Modify the `main()` function to display a message that includes the length of the player's name entered by the user using the `len()` function.

3. **Enhanced Environmental Health Check:**
   
      - Update the `ocean_challenge()` and `forest_challenge()` functions to display the absolute value of changes in environmental health using the `abs()` function.

4. **Validate User Input:**
   
      - Create a `get_valid_input()` function that uses `str.isdigit()` to ensure that numeric inputs are valid. This is used when the user is selecting the location from the menu, and the options presented by each of the challenges.


??? note "If you're stuck, take a look here"

    ## Instructions:

    1. **Create the `main()` Function:**
        
        - Introduce the `main()` function as the entry point for the program.
        - Move the game initialisation and the main gameplay loop into the `main()` function.

    2. **Enhanced Welcome Message:**
    
        - Use the `len()` function to display the length of the player's name entered by the user.

    3. **Enhanced Environmental Health Check:**
    
        - Use the `abs()` function to display the absolute value of changes in environmental health.

    4. **Validate User Input:**
    
        - Use the `str.isdigit()` function to ensure that numeric inputs are valid numbers.

??? note "If you're **really** stuck ..."

    ## Detailed Steps:

    1. **Create the `main()` Function:**

        Refactor the existing code to include a `main()` function. The `main()` function should initialize the game and handle the main gameplay loop.

        ```python
        def main():
            # Initialize Game
            display_message("Welcome to Climate Quest!")
            player_name = get_user_input("Enter your name: ")
            display_message(f"Hello, {player_name}! Your name has {len(player_name)} characters.")
            environment_health = initialize_health(100)
            display_message(f"Initial environmental health: {environment_health}")

            # Gameplay Loop
            for _ in range(3):  # Example loop for 3 challenges
                location = choose_location()
                environment_health = handle_challenge(location, environment_health)
                display_message(f"Updated environmental health: {environment_health}")

            # End Game
            display_message("Thank you for playing Climate Quest!")

        # Run the game
        display_welcome_message()
        player_name = get_player_name()
        main()
        ```

        This code will need the following functions, if not already present in your code.

        ```python
        def display_message(message):
            print(message)

        def get_user_input(prompt):
            return input(prompt)

        def initialize_health(initial_value):
            return initial_value
        ```

    2. **Enhanced Environmental Health Check:**

        Update the challenge functions to use the `abs()` function when displaying the changes in environmental health.

        ```python
        def ocean_challenge(environment_health):
            display_message("You are addressing ocean pollution.")
            cleanup_amount = get_valid_input("Enter the amount of pollution cleaned (0-100): ")
            change = -cleanup_amount
            display_message(f"Change in environmental health: {abs(change)}")
            return update_health(environment_health, change)

        def forest_challenge(environment_health):
            display_message("You are tackling deforestation.")
            trees_planted = get_valid_input("Enter the number of trees planted: ")
            change = 20 if trees_planted > 50 else -10
            display_message(f"Change in environmental health: {abs(change)}")
            return update_health(environment_health, change)

        # Repeat this pattern in all challenge functions that require numeric input...
        ```

    4. **Validate User Input:**

        Create a helper function `get_valid_input()` to ensure numeric inputs are valid. Use this function in the challenge functions.

        ```python
        def get_valid_input(prompt):
            while True:
                user_input = get_user_input(prompt)
                if user_input.isdigit():
                    return int(user_input)
                else:
                    display_message("Invalid input. Please enter a number.")
        ```

