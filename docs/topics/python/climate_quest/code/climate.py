def introduction():
    print("Welcome to Climate Quest!")
    print("The Earth is in peril as climate change accelerates, leading to devastating environmental consequences.")
    print("Your mission is to travel across different locations, make crucial decisions, and combat the effects of climate change.")
    print("Collect resources along the way to help you in your quest to save the planet.\n")

def make_choice(choices):
    print("\nYour choices:")
    for i, choice in enumerate(choices, 1):
        print(f"{i}. {choice}")
    
    while True:
        try:
            choice = int(input("\nEnter the number of your choice: "))
            if 1 <= choice <= len(choices):
                return choice
            else:
                print("Please enter a valid number.")
        except ValueError:
            print("Please enter a number.")

def evaluate_consequence(score, positive, neutral, negative):
    if score == 1:
        print(positive)
        return 1
    elif score == 2:
        print(neutral)
        return 0
    elif score == 3:
        print(negative)
        return -1

def collect_item(inventory, item):
    print(f"\nYou have collected a {item}!")
    inventory.append(item)

def location_forest(inventory):
    print("\n--- Location: Forest ---")
    print("You witness large-scale logging operations threatening to clear vast areas of trees.")
    choices = [
        "Confront the loggers and demand they stop.",
        "Start a tree-planting initiative with the local community.",
        "Ignore the situation and move on."
    ]
    choice = make_choice(choices)
    
    if choice == 1:
        collect_item(inventory, "Recycling Bin")
        return evaluate_consequence(1, "The loggers refuse to stop, but your protest raises awareness, leading to stricter logging regulations in the future.", "", "")
    elif choice == 2:
        return evaluate_consequence(2, "Your tree-planting initiative is a success, restoring parts of the forest.", "", "")
    elif choice == 3:
        return evaluate_consequence(3, "The deforestation continues, resulting in habitat loss and increased carbon emissions.", "", "")

def location_ocean(inventory):
    print("\n--- Location: Ocean ---")
    print("You arrive at a coral reef, now turning pale due to rising ocean temperatures and pollution.")
    choices = [
        "Launch a clean-up campaign to remove pollutants from the water.",
        "Advocate for stricter regulations on carbon emissions.",
        "Harvest the remaining coral for commercial purposes."
    ]
    choice = make_choice(choices)
    
    if choice == 1:
        collect_item(inventory, "Reusable Water Bottle")
        return evaluate_consequence(1, "The clean-up helps restore water quality, allowing some corals to recover.", "", "")
    elif choice == 2:
        return evaluate_consequence(2, "Your advocacy leads to international agreements to reduce carbon emissions.", "", "")
    elif choice == 3:
        return evaluate_consequence(3, "The coral is harvested, leading to the complete destruction of the reef.", "", "")

def location_city(inventory):
    print("\n--- Location: City ---")
    print("In a bustling city, smog fills the air, and trash litters the streets.")
    choices = [
        "Implement a city-wide recycling program.",
        "Promote the use of public transportation and electric vehicles.",
        "Do nothing and let the city continue on its current path."
    ]
    choice = make_choice(choices)
    
    if choice == 1:
        collect_item(inventory, "Electric Vehicle")
        return evaluate_consequence(1, "The recycling program reduces waste and pollution, making the city cleaner.", "", "")
    elif choice == 2:
        return evaluate_consequence(2, "Encouraging public transportation and electric vehicles reduces the city's carbon footprint.", "", "")
    elif choice == 3:
        return evaluate_consequence(3, "Pollution worsens, leading to health problems for the city's residents.", "", "")

def location_arctic(inventory):
    print("\n--- Location: Arctic ---")
    print("You travel to the Arctic, where glaciers are melting at an alarming rate.")
    choices = [
        "Invest in renewable energy projects to reduce global warming.",
        "Support indigenous communities in their efforts to protect the land.",
        "Ignore the melting glaciers and continue with business as usual."
    ]
    choice = make_choice(choices)
    
    if choice == 1:
        collect_item(inventory, "Solar Panels")
        return evaluate_consequence(1, "Renewable energy projects help slow down global warming, reducing the rate of glacier melting.", "", "")
    elif choice == 2:
        return evaluate_consequence(2, "Supporting indigenous communities leads to sustainable land management.", "", "")
    elif choice == 3:
        return evaluate_consequence(3, "The glaciers continue to melt, leading to severe sea level rise.", "", "")

def location_desert(inventory):
    print("\n--- Location: Desert ---")
    print("In a once fertile desert region, prolonged drought has dried up rivers and made farming nearly impossible.")
    choices = [
        "Implement water conservation techniques and build reservoirs.",
        "Introduce drought-resistant crops to the area.",
        "Abandon the region and relocate the population."
    ]
    choice = make_choice(choices)
    
    if choice == 1:
        collect_item(inventory, "Water Purifier")
        return evaluate_consequence(1, "Water conservation efforts help sustain the community.", "", "")
    elif choice == 2:
        return evaluate_consequence(2, "Drought-resistant crops thrive, providing food and income for the local population.", "", "")
    elif choice == 3:
        return evaluate_consequence(3, "The region is abandoned, and the desertification spreads.", "", "")

def final_challenge(inventory):
    print("\n--- Final Challenge: Global Environmental Crisis ---")
    print("A massive hurricane is approaching a heavily populated coastal city.")
    
    if "Solar Panels" in inventory:
        print("\nYou have solar panels in your inventory! Would you like to use them to power emergency shelters?")
        choices = [
            "Use the solar panels to power emergency shelters.",
            "Coordinate a massive evacuation and disaster response effort.",
            "Focus on long-term solutions by pushing for global climate policies and renewable energy initiatives.",
            "Accept the situation as inevitable and do nothing."
        ]
    else:
        choices = [
            "Coordinate a massive evacuation and disaster response effort.",
            "Focus on long-term solutions by pushing for global climate policies and renewable energy initiatives.",
            "Accept the situation as inevitable and do nothing."
        ]
    
    choice = make_choice(choices)
    
    if choice == 1 and "Solar Panels" in inventory:
        return evaluate_consequence(1, "The solar panels help power emergency shelters, saving countless lives.", "", "")
    elif choice == 1:
        return evaluate_consequence(1, "The evacuation saves thousands of lives, but similar disasters continue.", "", "")
    elif choice == 2:
        return evaluate_consequence(2, "Your push for global climate policies leads to a united effort to combat climate change.", "", "")
    elif choice == 3:
        return evaluate_consequence(3, "The hurricane devastates the city, and without any action, similar crises become more frequent.", "", "")

def game_ending(score):
    print("\n--- Game Over ---")
    if score >= 5:
        print("Best Ending: Through wise decisions, you have significantly mitigated the effects of climate change. The planet is on a path to recovery.")
    elif 3 <= score < 5:
        print("Moderate Ending: Some of your actions had positive effects, but others worsened the situation. The environment is in a precarious state.")
    else:
        print("Worst Ending: Your decisions accelerated environmental degradation. The planet is in crisis, with widespread disasters and little hope for recovery.")

def play_game():
    inventory = []
    introduction()
    score = 0
    score += location_forest(inventory)
    score += location_ocean(inventory)
    score += location_city(inventory)
    score += location_arctic(inventory)
    score += location_desert(inventory)
    score += final_challenge(inventory)
    game_ending(score)

play_game()