from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# List of players to vote for
PLAYERS = [
    "Younis Mahmoud",
    "Ali Adnan",
    "Hussein Ali",
    "Justin Meram",
    "Ahmed Radhi"
]

# In-memory vote tally
votes = {player: 0 for player in PLAYERS}

@app.route('/')
def index():
    return render_template('index.html', players=PLAYERS)

@app.route('/vote', methods=['POST'])
def vote():
    player = request.form.get('player')
    if player in votes:
        votes[player] += 1
    return redirect(url_for('results'))

@app.route('/results')
def results():
    return render_template('results.html', votes=votes)

if __name__ == '__main__':
    app.run(debug=True)
