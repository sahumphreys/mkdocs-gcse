# climate_quest_1.py
# --------------------------------------------------------------------------
# First stage of the climate quest program.  Includes (most) of tasks 1-4
# --------------------------------------------------------------------------

def display_welcome_message():
    """
    Display a welcome message to the game
    """
    print("Welcome to Climate Quest!")
    print("The Earth is in peril as climate change accelerates. Your mission is to make crucial decisions to combat the effects of climate change.\n")


def get_player_name():
    """
    Return the name of the player
    """
    return input("What is your name? : ")


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


def forest_challenge():
    """
    The forest challenge
    """
    print("\nForest Challenge")
    print(f"{player_name}: You witness large-scale logging operations threatening to clear vast areas of trees. What will you do?")
    print("1. Confront the loggers and demand they stop.")
    print("2. Start a tree-planting initiative with the local community.")
    print("3. Ignore the situation and move on.")


def ocean_challenge():
    """
    The ocean challenge
    """
    print("\nOcean Challenge")
    print(f"{player_name}: You arrive at a coral reef, now turning pale due to rising ocean temperatures and pollution. What will you do?")
    print("1. Launch a clean-up campaign to remove pollutants from the water.")
    print("2. Advocate for stricter regulations on carbon emissions.")
    print("3. Harvest the remaining coral for commercial purposes.")


def city_challenge():
    """
    The city challenge
    """
    print("\nCity Challenge")
    print(f"{player_name}: In a bustling city, smog fills the air, and trash litters the streets. What will you do?")
    print("1. Implement a city-wide recycling program")
    print("2. Promote the use of public transportation and electric vehicles.")
    print("3. Do nothing and let the city continue on its current path.")


def arctic_challenge():
    """
    The arctic challenge
    """
    print("\nArctic Challenge")
    print(f"{player_name}: You travel to the Arctic, where glaciers are melting at an alarming rate. What will you do?")
    print("1. Invest in renewable energy projects to reduce global warming.")
    print("2. Support indigenous communities in their efforts to protect the land.")
    print("3. Ignore the melting glaciers and continue with business as usual.")


def desert_challenge():
    """
    The desert challenge
    """
    print("\nDesert Challenge")
    print(f"{player_name}: In a once fertile desert region, prolonged drought has dried up rivers and made farming nearly impossible. What will you do?")
    print("1. Implement water conservation techniques and build reservoirs.")
    print("2. Introduce drought-resistant crops to the area.")
    print("3. Abandon the region and relocate the population.")


def main():
    """
    Main game loop
    """
    while True:
        display_menu()
        choice = input("Choose a challenge (1-6): ")

        if choice == '1':
            forest_challenge() 
        elif choice == '2':
            ocean_challenge()
        elif choice == '3':
            city_challenge()
        elif choice == '4':
            arctic_challenge()
        elif choice == '5':
            desert_challenge()
        elif choice == '6':
            print("Thank you for playing Climate Quest")
            break
        else:
            print("Invalid choice") 

# Run the game
display_welcome_message()
player_name = get_player_name()
main()