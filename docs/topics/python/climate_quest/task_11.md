---
title: Climate Quest - Task 11
---

![](../../../assets/images/climate-quest.png){align=right width="100"}

# {{ title }}

In this final task we'll add file handling to the Climate Quest Adventure Game.

!!! note "Objectives"

    - Understand the basics of file handling in Python.
    - Learn how to open, read, write, and close files.
    - Apply file handling to save game progress, load game settings, or store player statistics.
    - Implement exception handling when working with files to manage potential errors (e.g., file not found).

In this challenge, you will take the refactored game from the previous task and further enhance it by storing the game data in a JSON file. This will teach you how to separate your code from the data it operates on, making your program more flexible and easier to maintain.

## **Background:**

So far, you've stored the game's locations, opening statements, and options directly in a Python dictionary. While this works, hard-coding data within your code can make it difficult to update or expand the game. Instead, by storing this data in a JSON file, you can easily modify the game's content without touching the code itself.

## **What is JSON?**

- **JSON** (JavaScript Object Notation) is a lightweight data-interchange format that is easy for humans to read and write, and easy for machines to parse and generate.
- **Advantages:**
  - **Separation of Concerns:** Keeps your game data separate from the logic, making the code cleaner.
  - **Flexibility:** You can update or add new game data without modifying the code.
  - **Portability:** JSON is widely used, so your data can be easily shared or reused in other programs.

## **Your Task**

1. **Create a JSON File**
   
       - Move the game data (locations, opening statements, options) from your Python dictionary to a JSON file.
   - **Example Structure:**
     ```json
     {
         "Forest": {
             "opening_statement": "You encounter loggers in a forest. What will you do?",
             "options": ["Confront the loggers", "Start a tree-planting initiative", "Ignore the situation"]
         },
         "Ocean": {
             "opening_statement": "You see plastic waste polluting the ocean. What will you do?",
             "options": ["Organize a beach cleanup", "Campaign against plastic use", "Do nothing"]
         }
         // Add more locations...
     }
     ```
   - !!! tip 
         - Save this JSON data in a file named `game_data.json`.

2. **Read the JSON File in Python**
  
      - Use Python’s built-in `json` module to read the data from your JSON file and load it into a dictionary.
   - **Sample Code:**
     ```python
     import json

     with open('game_data.json', 'r') as file:
         game_map = json.load(file)
     ```
   - !!! tip
         -  Place this code at the start of your game logic to load the data before the game begins.

3. **Modify Your Existing Functions**
   
      - Ensure that your game functions (e.g., `display_challenge`) work with the data loaded from the JSON file.
   
      - !!! tip
        - If your previous code was correctly using a dictionary, minimal changes should be required.

4. **Test Your Game**
   
      - Run your game to ensure it works with the data loaded from the JSON file.
      - Try adding new locations or updating existing ones in the JSON file to see how the game reacts.

### **Hints & Tips**

- **Validating JSON:** 
  
    - Make sure your JSON file is properly formatted. Use an online JSON validator to check for errors.
  
- **Working with JSON in Python:**
  
    - Use `json.load()` to read from a file and `json.dump()` if you ever need to write back to a JSON file.
  
- **Error Handling:**
  
    - Consider what should happen if the JSON file is missing or corrupted. You might want to add error handling to manage these cases gracefully.

## **Expected Outcome**

  - By the end of this challenge, your game should load its data from a JSON file. This will allow you or anyone else to modify the game’s content without changing the Python code.

## **Benefits of Using JSON for Game Data**

- **Maintainability:** Game data is separated from the logic, making it easier to update or expand.
- **Reusability:** The JSON file can be reused in other programs or shared easily.
- **Ease of Updates:** Non-programmers can edit the game content directly in the JSON file without needing to understand the Python code.

## **Challenge Yourself**
- **Dynamic Loading:** Try dynamically loading different JSON files based on user input, allowing for different game scenarios or levels.
- **Save Progress:** Use JSON to save and load the player’s progress, making the game more interactive.

