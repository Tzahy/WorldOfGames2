# Include necessary modules and functions
import random, time
from Utils import screen_cleaner
from Score import add_score


# Generate n random numbers between 1 to 101 by the player level entry.
# The numbers will be shown for 0.7 seconds and then disappear (clean screen).
def generate_sequence(difficulty):
    random_numbers = [random.randrange(1, 101) for i in range(difficulty)]
    print(random_numbers)
    time.sleep(0.7)
    screen_cleaner()
    return random_numbers


# The player should remember the numbers he saw and enter them by their order.
# The player must enter valid entries for his choices.
def get_list_from_user(difficulty):
    print("After seeing the numbers enter the numbers you saw, each one separated with Enter")
    inputs = []
    for i in range(difficulty):
        inputs.append(input("Number: "))

    return inputs


# Check if the player guess is equal to the random numbers.
# If the player guesses wrong then the game is over and he can see the numbers he should have enter.
# The numbers are stored in lists and printed to the screen as string.
# If the player is right it returns the list length for the scoring function.
def is_list_equal(list_a, list_b):
    if list_a == list_b:
        score = len(list_a)
        return score
    else:
        print("\nGame Over! The numbers were", str(list_a))
        exit()
        return False


# Run the game functions
def play(difficulty):
    # Generate random list
    random_list = generate_sequence(difficulty)
    # Receive player input
    user_list = get_list_from_user(len(random_list))
    # Compare Player input with the random list and continue if player succeed to guess
    is_succeed = is_list_equal(random_list, list(map(int, user_list)))
    # Run the player score function with the points to add.
    add_score(int(is_succeed))
