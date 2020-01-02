# Include necessary modules and functions.
# variables and functions to serve the other files.
import os
scores_file_name = "Scores.txt"
is_file_exists = "File is not exists, creating new file and adding your score..."
score_print = "You're right!!! Your score is"


def screen_cleaner():
    os.system('cls')


# Used in Live.py
def error_messages(error):
    if error == '1':
        print("No valid option was chosen. Exiting...")
    elif error == '2':
        print("Not a number, try again a valid option, exiting...")
    elif error == '3':
        print("Please choose '1' or '2' next time. Exiting...")
    elif error == '4':
        print("Not a number, exiting...")
