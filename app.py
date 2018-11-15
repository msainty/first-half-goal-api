"""
first-half-goals service app
"""
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=['http://localhost:3000'])

@app.route('/')
def handler():
    """
    Return a list of fixtures
    """
    return jsonify([
        {
            'uuid': '1',
            'kickOff': '2018-01-27T10:00:00',
            'country': 'England',
            'league': 'PL',
            'status': 0.6,
            'homeTeam': 'Manchester United',
            'awayTeam': 'Brighton',
            'played': 15,
            'noOfNoScoreFirstHalf': 0,
            'percentageOfAFirstGoalHome': 0.66,
            'percentageOfAFirstGoalAway': 0.55,
            'probability': 0.85,
            'price': 1.35,
            'matched': 344,
            'rating': 5,
        },
        {
            'uuid': '2',
            'kickOff': '2018-02-27T10:00:00',
            'country': 'Scotland',
            'league': 'C',
            'status': 0.7,
            'homeTeam': 'Celtic',
            'awayTeam': 'Dundee United',
            'played': 18,
            'noOfNoScoreFirstHalf': 0,
            'percentageOfAFirstGoalHome': 0.5,
            'percentageOfAFirstGoalAway': 0.5,
            'probability': 0.5,
            'price': 1.35,
            'matched': 200,
            'rating': 4,
        }
    ])

if __name__ == '__main__':
    app.run()
