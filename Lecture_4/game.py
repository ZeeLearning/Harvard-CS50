import random

def get_positive_integer(prompt):
    # Prompt the user until they enter a positive integer
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                pass
        except ValueError:
            print("Invalid input.")

def main():
    # Prompt the user for the level
    level = get_positive_integer("Level: ")

    # Randomly generate an integer between 1 and the level, inclusive
    target_number = random.randint(1, level)

    while True:
        # Prompt the user to guess the number
        guess = get_positive_integer("Guess: ")

        if guess > target_number:
            print("Too large!")
        elif guess < target_number:
            print("Too small!")
        else:
            print("Just right!")
            break  # Exit the loop

if __name__ == "__main__":
    main()