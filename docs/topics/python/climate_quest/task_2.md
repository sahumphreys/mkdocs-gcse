---
title: Climate Quest - Task 2
---

![](../../../assets/images/climate-quest.png){align=right width="100"}
# {{ title}}


## Objective"

The objective of this task is to introduce you to various types of **operators** in Python, including assignment, mathematical, logical, and comparison operators. You will extend the "Climate Quest" game to incorporate these concepts.

!!! note "Learning Outcomes"

    By the end of this task, you should be able to:

    1. Understand the use and application of the assignment operator.
    2. Use mathematical operators for simple calculations.
    3. Utilize augmented assignment operators.
    4. Construct expressions while applying operator precedence.
    5. Use logical operators in Python.
    6. Understand and use comparison operators.
    7. Build expressions combining logical and comparison operators.
    8. Apply parentheses to modify the evaluation order of logical expressions.

## Task Description:

You will enhance the "Climate Quest" game by adding functionality to calculate and display initial environmental health, perform some basic calculations, and make simple decisions using logical and comparison operators.

## Steps to Complete the Task:

1. **Environmental Health Initialization**:

      - Use an assignment operator to set an initial environmental health value.
      - Use a mathematical operator to perform a calculation and update the environmental health.

2. **Augmented Assignment Operators**:

      - Use augmented assignment operators to update the environmental health based on user input.

3. **Logical and Comparison Operators**:

      - Use logical and comparison operators to make a decision in the game.

## Skeleton code

1. **Start a New Python File**:

      - Open your Python editor or an online Python compiler.
      - Create a new file and save it as `climate_quest_task2.py`.
  
Copy the code below into that file and answer all questions in the code to make a working Python program.  There are 4 questions.  Do not make any other changes to the given code.

```python
# Welcome Message
print("Welcome to Climate Quest!")
print("The environment is facing serious challenges due to climate change.")
print("Your mission:
print("Make decisions that help mitigate these effects and protect the planet.")

# Get User Input
player_name = input("What is your name? ")
print(f"Hello, {player_name}! Your mission is to protect the planet.")

# Environmental Health Initialization
# ----------------------------------------------------------------
# Question 1: assign a variable named "environment_health" to an 
# initial value of 100
                                        # complete this line
# ----------------------------------------------------------------
print(f"Initial environmental health: {environment_health}")

# ----------------------------------------------------------------
# Question 2: The environmental health inspectors have conducted an 
# initial investigation and have reduced the environment_health 
# score by 10%.
# Make the change to the environment_health score here:
environment_health =                    # complete this line
# ----------------------------------------------------------------
print(f"Environmental health after initial assessment: {environment_health}")

# ----------------------------------------------------------------
# Question 3: Following an internal discussion it was decided to 
# increase the environment_health score by 5 points. Use an 
# augmented assignment operator to update environmental health

environment_health                      # Complete this line
# ----------------------------------------------------------------
print(f"Environmental health after small improvement: {environment_health}")

# Logical and Comparison Operators
print("\nAssessing environmental conditions...")
tree_planting = int(input("Enter the number of trees you plan to plant: "))
pollution_level = int(input("Enter the current pollution level (0-100): "))

# Decision making using logical and comparison operators
# ----------------------------------------------------------------
# Question 4: Complete the expression below to check if 
# tree_planting is greater than 50 and pollution_level is less than 50
if (          ) and (          ):       # Complete this line
    environment_health += 10
    print("Great job! Your efforts are making a positive impact on the environment.")
else:
    environment_health -= 10
    print("Unfortunately, more effort is needed to improve environmental conditions.")

print(f"Final environmental health: {environment_health}")
```

## Questions for Reflection:

1. What is the purpose of using assignment and augmented assignment operators?
2. How do logical and comparison operators help in decision-making within a program?
3. Why is it important to understand operator precedence?

## Extension Activity (Optional):

- Add more decision points in the game using logical and comparison operators.
- Try creating more complex expressions and see how parentheses change the evaluation order.
