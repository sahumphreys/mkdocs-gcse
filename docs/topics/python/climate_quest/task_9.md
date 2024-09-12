---
title: Climate Quest - Task 9
---

![](../../../assets/images/climate-quest.png){align=right width="100"}

# {{ title }}

!!! note "Objectives"
    
    - Understand the concept of 2D lists in Python and their usefulness in storing and managing more complex collections of data.
    - Learn how to create, access, and modify 2D lists.
    - Practice iterating over 2D lists using nested loops.
    - Apply these concepts to enhance the Climate Quest game.

Incorporating 2D lists into the Climate Quest text adventure game can add complexity and depth to the game's data structures. For example, we can use 2D lists to manage multiple attributes for various game locations, challenges, or resources.

Changing the way in which the data is being held means we can also simplify the challenge functions by removing the functions for each location i.e. `forest_challenge()`, `city_challenge()` etc into just one function and use the location as a parameter to that function!

!!! warning

    This challenge will involve a restructuring of the way the game data has been handled before.  It may be best to start a new game file for your Python code

Here are some ways to incorporate 2D lists into the game:

1. **Game Map:** Use a 2D list to represent a map of the game world, with different locations having various attributes (e.g., name, environmental health impact).
2. **Challenge Outcomes:** Store possible outcomes of challenges in a 2D list where each row represents a different challenge and each column represents possible outcomes.
3. **Resource Management:** Use a 2D list to keep track of resources, where each resource has multiple attributes (e.g., type, quantity, impact).

## Instructions

1. **Create a 2D List to Represent the Game Map:**

    - Each sublist represents a location with attributes like name, description, and environmental health impact.

    - Create a 2D list where each inner list represents a location. The inner list will contain the following elements:

        - **Location Name**: A string representing the name of the location.
        - **Opening Statement**: A string that describes the scenario at the location.
        - **Options**: A further list of possible actions the player can take.


    ```python
    game_map = [
    ["Forest", 
     "You encounter loggers in a forest. What will you do?",
     ["Confront the loggers", "Start a tree-planting initiative", "Ignore the situation"]],
    
    ["Ocean", 
     "You see plastic waste polluting the ocean. What will you do?",
     ["Organize a beach cleanup", "Campaign against plastic use", "Do nothing"]],
     # etc - add for the remaining locations
    ```

    Our top-level list is called `game_map`.  The `game_map` is a list of locations.

2. **Refactor the challenge functions**

    - Instead of having separate functions for each challenge, we can create a generic function that processes any location using the data from the game_map.

    ```python
    def display_challenge(location_data):
        """
        Display the challenge for the given location.
        
        Args:
            location_data (list): A list containing location name, opening statement, and options.
        """
        print(f"\n{location_data[0]} Challenge")
        print(f"{player_name}: {location_data[1]}")
        for i, option in enumerate(location_data[2], 1):
            print(f"{i}. {option}")

        choice = get_valid_input("Choose an action (1-3): ")
        # code will continue here
    ```

      - The parameter to this function, `location_data`, will be one of the items in the `game_data` list.
      - Line 8: pulls out the first item in that list, the title of the location
      - Line 9: pulls out the second item in that list, the location description
      - Line 10: A new loop function `enumerate()`.  As the title suggests this loop function also provides a number for each of the items in the list it is looping over and this is stored in the `i` variable.  Really useful!
      - Complete the code for this function by processing the choice and displaying the relevant outcome message to the screen from the `location_data`

3. **Update the main function**

    - When processing the user choice for the location we now only need to call the `display_challenge()` function and pass in the correct location data from the `game_map` list:

    ```python
    def main():
        while True:
            display_menu()
            choice = get_valid_input("Choose a challenge (1-6): ")

            if 1 <= choice <= 5:
                display_challenge(game_map[choice - 1])
            elif choice == 6:
                print("Thank you for playing Climate Quest!")
                break
            else:
                print("Invalid choice. Please choose again.")
    ```

    - Line 6: A more concise way of saying `if choice >= 1 and choice <= 5:`
     
5. **Other opportunities**

      - This approach can be developed further by keeping a list of the resources gathered by the user in each location, where each resource (if/when) used can have an impact on the `environmental_health` score.

!!! note

    Notice how, by changing how our data is being stored, we can simplify the algorithm and code needed to process that data.