"""Main script, uses other modules to generate sentences."""
from flask import Flask

app = Flask(__name__)

# TODO: Initialize your histogram, hash table, or markov chain here.
# Any code placed here will run only once, when the server starts.
from histogram import histogram
from stochastic_sampling import weighted_random_word

@app.route("/")
def home():
    """Route that returns a web page containing the generated text."""
    word = weighted_random_word(histogram('one fish, two fish, red fish, blue fish'))
    return f"<p>{word}</p>"


if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)
