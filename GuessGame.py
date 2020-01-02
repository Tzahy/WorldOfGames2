# Include necessary modules and functions
import random
from Score import add_score


# Get game level from the player and generate a random number between 1 to the user choice ane return it
# for comparison with the player guess.
def generate_number(difficulty):
    secret_generated = random.randint(1, difficulty)
    return secret_generated


# Ask the player to guess a number between 1 to the game level he chose and return it for comparison.
# The player must enter a valid entries as requested
def get_guess_from_user(difficulty):
    difficulty = str(difficulty)
    guessed_number = int(input("please guess a number between 1 to " + difficulty + " "))
    return guessed_number


# Compare the random number of the computer and the number the player choose.
# If the player was right then he WON and the score will be added to his score list.
# If the player was wrong he will get a second chance (only).
# If the player was right in the second chance then,
# his score will be added to his score list (like in the first attempt).
# If the player was wrong in the second phase the game will be finished without any points.
# The player must enter a valid entries as requested
def compare_results(generated, guessed):
    tries = 1
    while generated != guessed:
        if tries == 2:
            print("\nGame Over! The number was:", generated)
            exit()

        guessed_number = int(input("Try Again (last chance): "))
        guessed = guessed_number
        tries += 1
    else:
        return generated


# Run the all the functions necessary for the game and if the player won, add his points to his total points.
def play(difficulty):
    guessed_from_user = get_guess_from_user(difficulty)
    generated_number = generate_number(difficulty)
    points_to_add = compare_results(generated_number, guessed_from_user)
    # Run the player score function with the points to add.
    add_score(int(points_to_add))

