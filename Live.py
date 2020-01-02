# Include necessary modules and functions
import GuessGame, MemoryGame
from Utils import error_messages


# This function gets the user name from MainGame file and welcome the player.
# Player name is mandatory.
# If the player enter more then one word i parse only the first word (or number) and
# make the first letter uppercase. I use .title() function because we can use it
# as first uppercase letter for multiple words if we would like to change it later.
def welcome(user):
    user_name = user.partition(' ')[0]  # Parse the first word from the user name.
    while user_name == "":  # If the player don't enter user name keep asking for it.
        user_name = input("Please enter your name: ")
    else:
        welcome_message = """\nHello {user_name} and welcome to the World of Games (WoG).
Here you can find many cool games to play.\n""".format(user_name=user_name.title())  # make first letter uppercase

    return welcome_message


# This function asks the player which game he wants to play and the difficulty level.
# Each choice the player makes calls the corresponding function.
# The player must enter valid entries for his choices.
# Error messages are returned from Utils file.
def load_game():
    try:
        game_chosen = int(input("""Please choose a game to play: \n\t1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back
        2. Guess Game - guess a number and see if you chose like the computer\n"""))

        # Check that the user input 1 or 2 and not anything else (e.g. int or string)
        if 0 < game_chosen < 3:
            try:
                difficulty = int(input("\nPlease choose game difficulty from 1 to 5: "))
                if difficulty in range(1, 6):
                    if game_chosen == 1:
                        print("\nSTARTING TO PLAY MEMORY GAME")
                        print("------------------------------\n")
                        # Start the Memory game and sends the difficulty level as a parameter for points
                        MemoryGame.play(difficulty)
                    elif game_chosen == 2:
                        print("\nSTARTING TO PLAY GUESS GAME")
                        print("-----------------------------\n")
                        # Start the Guess game and sends the difficulty level as a parameter for points
                        GuessGame.play(difficulty)
                else:
                    error_messages('1')  # Get error message from Utils
                    exit()
            except ValueError:
                error_messages('2')  # Get error message from Utils
                exit()

            pass
        else:
            error_messages('3')  # Get error message from Utils
            exit()
    except ValueError:
        error_messages('4')  # Get error message from Utils
        exit()
