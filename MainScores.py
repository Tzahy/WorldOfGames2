# Import flask to be able to send info to a browser using a local server.
# I modified only the server details and the paragraph output.
from flask import Flask

app = Flask(__name__)


@app.route('/')
def score_server():
    try:
        score = open("Scores.txt", "r")  # score file
    except BaseException as e:
        return """<html>
        <head>
            <title>Scores Game</title>
        </head>
        <body>
        <body>
            <h1><div id="score" style="color:red">""" + Utils.BAD_RETURN_CODE + str(e) + """</div></h1>
        </body>
        </html>
        """
    return """
    <html>
        <head>
            <title>Scores Game</title>
        </head>
        <body>
            <h1><div id="score"> Your score is """ + str(score.readline()) + """ Points... Nice :)</div></h1>
        </body>
    </html>"""


if __name__ == '__main__':
    # Setting the server details
    app.run(host='0.0.0.0', debug=True, threaded=True, port=8080)
