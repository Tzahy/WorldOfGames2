# Include necessary modules and functions.
from Utils import scores_file_name
from Utils import score_print, is_file_exists


# Get the player score and add it to a text file ("Scores.txt").
# If the file not exists print a message, create the file, and add the score.
# Each game the score will be added to the previous score.
# The score will printed to the screen and to the browser by the flask server:
# I configured the server to run at: http://127.0.0.1:8080/ URL (in MainScores.py file).
def add_score(points):
    try:
        score_file = open(scores_file_name, 'r')
        score = score_file.read()
        current_score = points + int(score)
        score_file = open(scores_file_name, 'w')
        score_file.write(str(current_score))
        print(score_print, str(current_score))
        score_file.close()
    except FileNotFoundError:
        print(is_file_exists)
        score_file = open(scores_file_name, 'w')
        score_file.write(str(points))
        print(score_print, str(points))
        score_file.close()
