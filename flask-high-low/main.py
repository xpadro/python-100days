from flask import Flask
import random

app = Flask(__name__)

solution = -1


@app.route("/")
def home():
    global solution
    solution = random.randrange(0, 9)
    return "<h1>Guess a number between 0 and 9</h1>"


@app.route("/<int:num>")
def hello2(num: int):
    if num == solution:
        return win()
    elif num < solution:
        return lower()
    else:
        return higher()


def win():
    return "<p style='color=red'>You got me!</p>" \
           "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"


def lower():
    return "<p style='color=blue'>Too low. Try again!</p>" \
           "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"


def higher():
    return "<p style='color=green'>Too high. Try again!</p>" \
           "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"


if __name__ == '__main__':
    # Debug mode enables hot reloading and debugging
    app.run(debug=True)
