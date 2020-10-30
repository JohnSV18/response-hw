
# TODO: Follow the assignment instructions to complete the required routes!
# (And make sure to delete this TODO message when you're done!)

from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    """Shows a greeting to the user. """
    return 'Are you there, world? It\'s me , Ducky!'


@app.route('/penguins')
def animal():
    """Shows animal to the user."""
    return "Penguins are cute!"


@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """Display a message to the user that changes based on their favorite animal."""
    return f'Wow, {users_animal} is my favorite animal, too!'


@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert):
    """Displays a question asking how they new they're favorite snack"""
    return f'How did you know I liked {users_dessert}?'


@app.route('/madlibs/<adjective>/<noun>')
def story(adjective, noun):
    """Displays short story with two stringst that the user puts on url"""
    return f'The {adjective} {noun} was the most comforting thing for us'
    

@app.route('/multiply/<number1>/<number2>')
def multiply(number1, number2):

    """Displays 2 numbers that will be multiplied and then the total"""

    number1 = int(number1)
    number2 = int(number2)

    total = number1 * number2
    final = str(total)

    return f'{number1} times {number2} equals {final}'


if __name__ == '__main__':
    app.run(debug=True)
