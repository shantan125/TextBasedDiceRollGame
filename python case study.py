import random

def roll_dice():
    min_value = 1
    max_value = 6
    dice_roll = random.randint(min_value, max_value)
    print(f"You rolled a {dice_roll}")

def start_game():
    while True:
        choice = input("Welcome to the Dice Roll Game! Do you want to start? (yes/no): ").lower()
        if choice == "yes" or choice == "y":
            roll_dice()
        elif choice == "no" or choice == "n":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")

# Start the game
start_game()
