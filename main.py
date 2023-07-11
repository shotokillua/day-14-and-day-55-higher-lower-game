from flask import Flask
import random

app = Flask(__name__)

print(__name__)

random_num = random.randint(0, 9)
# high_num = []
# low_num = []
#
# for num in range(0, 9):
#     if num > random_num:
#         high_num.append(num)
#     elif num < random_num:
#         low_num.append(num)

@app.route('/')
def home():
    return '<h1><b>Guess a number between 0 and 9</b></h1>' \
    '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'



@app.route(f'/<int:guess>')
def guess(guess):
    if guess == random_num:
        return '<h1 style="color:green">You found me!</h1>' \
        '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'

    elif guess > random_num:
        return '<h1 style="color:purple">Too high, try again!</h1>' \
        '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'

    elif guess < random_num:
        return '<h1 style="color:red">Too low, try again!</h1>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'


if __name__ == "__main__":
    app.run(debug=True)

