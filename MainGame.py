# Include necessary modules and functions.
from Live import load_game, welcome
from Utils import screen_cleaner
from MainScores import score_server

# Clear the screen
screen_cleaner()
# Ask for player name (mandatory)
player_name = input("Please enter your name: ")

# Welcome message and games choice
print(welcome(player_name))
load_game()
score_server()

