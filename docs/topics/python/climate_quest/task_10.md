---
title: Climate Quest - Task 11
---

![](../../../assets/images/climate-quest.png){align=right width="100"}

# {{ title }}

!!! note "Objectives"

    Your task is to refactor a simple text-based game to improve its data handling by replacing a 2D list with a dictionary. The game, "Climate Quest," presents the player with various environmental challenges at different locations. Each location offers a scenario with multiple choices, and the player's decisions impact the outcome.

    - Understand the benefits of using dictionaries over 2D lists for organizing related data.
    - Practice accessing and manipulating nested data structures in Python.
    - Enhance code readability, maintainability, and scalability.

    
## Instructions:

The changes to be made to the program are mainly **refactoring**.  This means taking some of the original code and making amendments to improve structure, readability and maintainability.  It's a common feature of programming.  Often the first version of code that you write can be improved.  You can choose to refactor the code written for the 2D List challenge or start with a new file.

### **Step 1: Review the Existing Code**

The existing code uses a 2D list to store location data (name, scenario, and options). This can be unwieldy, especially as the game grows. Here's an example of how the data is currently structured:

```python
game_map = [
    ["Forest", "You encounter loggers in a forest. What will you do?", ["Confront the loggers", "Start a tree-planting initiative", "Ignore the situation"]],
    ["Ocean", "You see plastic waste polluting the ocean. What will you do?", ["Organize a beach cleanup", "Campaign against plastic use", "Do nothing"]],
    ["City", "The city is facing severe air pollution. What will you do?", ["Advocate for clean energy", "Promote public transportation", "Ignore the pollution"]],
    ["Arctic", "The Arctic ice is melting rapidly. What will you do?", ["Support renewable energy", "Research ice preservation methods", "Do nothing"]],
    ["Desert", "Desertification is threatening the region. What will you do?", ["Plant drought-resistant crops", "Build water reservoirs", "Do nothing"]]
]
```

1. **Refactor the `game_map`:** 
   - Instead of using a 2D list, reorganize the game map into a dictionary where each key is a location name (e.g., `"Forest"`, `"Ocean"`).
   - The value for each key should be another dictionary that contains:
     - An `"opening_statement"` key with a string value for the scenario.
     - An `"options"` key with a list of possible choices.

2. **Modify the `display_challenge` Function:**
   - Update the function to retrieve the scenario and options from your newly created dictionary.
   - The function should dynamically display the scenario and options based on the selected location.

3. **Update the `main` Function:**
   - Replace references to the old 2D list with the appropriate dictionary keys.
   - Ensure that the menu selection correctly maps to the dictionary.

## **Hints and Tips**

- **Why Use a Dictionary?**

    - **Readability:** Dictionaries allow you to use meaningful keys, making the data more intuitive to access and modify.
    - **Scalability:** Adding new locations or modifying existing ones becomes easier and less error-prone with a dictionary structure.
    - **Maintainability:** With a dictionary, you avoid the confusion of managing nested lists and indices, making your code easier to maintain.

- **Dictionary Structure Example:**
  Here's a simplified example of how you might structure the data for one location in a dictionary:

  ```python
  forest_data = {
      "opening_statement": "You encounter loggers in a forest. What will you do?",
      "options": ["Confront the loggers", "Start a tree-planting initiative", "Ignore the situation"]
  }
  ```

  You can expand this concept to the entire game map, using the location names as keys in your main dictionary.

- **Accessing Dictionary Data:**
    - Use the location name to access the scenario and options. For example:

    ```python
    print(game_map["Forest"]["opening_statement"])
    print(game_map["Forest"]["options"])
    ```

    - To iterate through options, you can use a loop:

    ```python
    for i, option in enumerate(game_map["Forest"]["options"], 1):
        print(f"{i}. {option}")
    ```

- **Think About Edge Cases:**
  
    - Consider what happens if a player inputs an invalid choice. How will your code handle it? Make sure your refactoring doesn't introduce new bugs.

- **Test Your Code:**
  
    - After refactoring, thoroughly test your code. Ensure that each location displays the correct scenario and options, and that the game logic works as expected.

---

### **Extra Credit:**

If you're up for a challenge, add a new location to the game. Use your dictionary structure to seamlessly integrate it into the existing code. Describe why it was easier to do this with a dictionary compared to the original
