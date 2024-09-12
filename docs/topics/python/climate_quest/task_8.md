---
title: Climate Quest - Task 9
---

![](../../../assets/images/climate-quest.png){align=right width="100"}

# {{ title }}

!!! note  "Objectives"

    - Define what a list is in Python and explain its usefulness in storing and managing collections of data.
    - Maintain a list of visited locations for the game
    - Add a simple inventory system to the game
    
## Task Overview:

In this homework, you will enhance the "Climate Quest" project by incorporating lists to manage collections of data such as locations visited and resources collected during the game.

### Instructions:

1. **Create Lists to Store Data:**

    - Use lists to store player choices, environmental health changes, and resources collected.

2. **Retrieve Elements from Lists:**
   
    - Retrieve elements from the lists using positive and negative indices.

3. **Iterate Over Lists:**
   
    - Use `for` loops to iterate over the elements of the lists and perform actions based on the elements.

4. **List Operations:**
   
    - Use list operations like `append()`, `insert()`, `remove()`, and `clear()` to manage the lists.

5. **Check for Item Presence:**
   
    - Use the `in` keyword to check if an item is present in a list.

6. **Get Item Index:**
    
    - Use the `index()` method to get the position of an item in a list.

## Detailed Steps

Using the following code, with highlighted questions, complete the code as required by the question.

```python hl_lines="9-10 30-31 34-35 39-45 48-49 52-53"
def main():
    # Initialize Game
    display_message("Welcome to Climate Quest!")
    player_name = get_user_input("Enter your name: ")
    display_message(f"Hello, {player_name}! Your name has {len(player_name)} characters.")
    environment_health = initialize_health(100)
    display_message(f"Initial environmental health: {environment_health}")
    
    # Create lists to store data
    # Q1: Initialise lists to hold the visited_locations, and resources_collected
    # Answer:

    # Gameplay Loop
    while environment_health > 0:
        for _ in range(3):  # Example loop for 3 challenges
            location = choose_location()
            visited_locations.append(location)  # Store player choice
            if location == 1:
                environment_health = ocean_challenge(inventory)
            elif location == 2:
                environment_health = forest_challenge(inventory)
            elif location == 3:
                environment_health = city_challenge(inventory)
            display_message(f"Updated environmental health: {environment_health}")

    # End Game
    display_message("Environmental health has dropped to zero. Game over!")
    display_message("Thank you for playing Climate Quest!")
    
    # Retrieve elements from lists
    # Q2: For each of the lists, print the whole list and the first and last items in these lists
    # Answer:
    
    # 3. Iterate over lists
    # Q3: For each of the lists, write a for loop to iterate over the list and display each element?
    # Answer:

    
    # 4. List operations
    # Q4: For the locations list:
    # - remove the last choice and display the list
    # - clear all choices from the list and display the list
    # For the resources collected list:
    # - add a new resource to the list and display the list
    #
    # Answer:
    
    # 5. Check for item presence
    # Q5: How can we check if "forest" is in player_choices and if they have collected solar panels for their inventory?
    # Answer:
    
    # 6. Get item index
    # Q6: How can we find the position of "forest" in player_choices and solar panels in the inventory?
    # Answer:
```    

## Additional Challenge 1

The user visits a number of locations, and these are presented 'long-hand' to the user in a menu that has a number of `print` statements:

```python
def display_menu():
    """
    Display the main menu for user to select their location
    """
    print("1. Forest Challenge")
    print("2. Ocean Challenge")
    print("3. City Challenge")
    print("4. Arctic Challenge")
    print("5. Desert Challenge")
    print("6. Quit")
```

Using iteration, a list of locations and the `in` operator, modify this function to present the menu of locations using the locations defined in the list. 

## Additional Challenge 2

At the moment the user can visit a location more than once.  Using the list of `visited_locations` how can we ensure the user only visits the location once and once only?

There will be a number of possible solutions here, e.g.

- Following on from the previous challenge, the menu ONLY displays those locations that have not been visited by the user
- The menu choice functionality checks against the list of `visited_locations` and only proceeds when the user selects a location that has not yet been visited.