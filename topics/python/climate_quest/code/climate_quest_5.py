import json
score = 0
visited_locations = []

def display_menu():
    print("Welcome to Climate Quest!")
    print("The Earth is in peril as climate change accelerates. Your mission is to make crucial decisions to combat the effects of climate change.\n")
    print("1. Forest Challenge")
    print("2. Ocean Challenge")
    print("3. City Challenge")
    print("4. Arctic Challenge")
    print("5. Desert Challenge")
    print("6. Quit")


def load_challenges(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def challenge(location, data):
    global score, visited_locations
    if location in visited_locations:
        print(f"\nYou have already completed the {location.capitalize()} Challenge.")
        return

    visited_locations.append(location)
    print(f"\n{location.capitalize()} Challenge")
    print(data[location]['description'])

    for i, option in enumerate(data[location]['options'], 1):
        print(f"{i}. {option}")

    choice = int(input("Choose an action: ")) - 1

    if 0 <= choice < len(data[location]['outcomes']):
        print(data[location]['outcomes'][choice])
        score += data[location]['scores'][choice]
    else:
        print("Invalid choice.")
    
    print(f"Current Score: {score}")

def main():
    challenges = load_challenges('challenges.json')

    while True:
        display_menu()
        choice = input("Choose a challenge (1-6): ")

        if choice == '1':
            challenge('forest', challenges)
        elif choice == '2':
            challenge('ocean', challenges)
        elif choice == '3':
            challenge('city', challenges)
        elif choice == '4':
            challenge('arctic', challenges)
        elif choice == '5':
            challenge('desert', challenges)
        elif choice == '6':
            if len(visited_locations) == 5:
                final_challenge()
            else:
                print("Complete all challenges before facing the final challenge!")
        else:
            print("Invalid choice.")

# Run the game
main()
