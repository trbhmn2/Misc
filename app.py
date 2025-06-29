from flask import Flask, render_template, request
import random

app = Flask(__name__)

class Player:
    def __init__(self, name, height, morale):
        self.name = name
        self.height = height
        self.morale = morale
        self.feeling = random.randint(1, 5)
        self.score = 0

    def offensive_power(self):
        base = (
            random.randint(50 + self.feeling, 100 + self.feeling) +
            random.randint(50 + self.feeling, 100 + self.feeling + self.height) +
            random.randint(50 - self.height + self.feeling, 100 + self.feeling)
        )
        return base * self.morale if self.score > 10 else base

    def defensive_power(self):
        base = (
            random.randint(50 + self.feeling, 100 + self.feeling) +
            random.randint(50 + (self.height * 3), 100 + (self.height * 3)) +
            random.randint(50 - self.height, 100 - self.height)
        )
        return base * self.morale if self.score > 10 else base

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        p1_name = request.form["p1_name"]
        p2_name = request.form["p2_name"]
        try:
            p1_height = int(request.form["p1_height"])
            p2_height = int(request.form["p2_height"])
            p1_morale = int(request.form["p1_morale"])
            p2_morale = int(request.form["p2_morale"])
            target_score = int(request.form["target_score"])
        except ValueError:
            return render_template("index.html", error="Please enter valid numeric values.")

        player1 = Player(p1_name, p1_height, p1_morale)
        player2 = Player(p2_name, p2_height, p2_morale)

        log = []
        while player1.score < target_score and player2.score < target_score:
            if player2.offensive_power() > player1.defensive_power():
                player2.score += 1
                log.append(f"🏀 {player2.name} scored! Score: {player1.name} {player1.score} - {player2.name} {player2.score}")
            if player1.offensive_power() > player2.defensive_power():
                player1.score += 1
                log.append(f"🔥 {player1.name} scored! Score: {player1.name} {player1.score} - {player2.name} {player2.score}")

        winner = player1 if player1.score > player2.score else player2
        log.append(f"🏆 {winner.name} WINS! Final Score: {player1.name} {player1.score} - {player2.name} {player2.score}")

        return render_template("index.html", log=log)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
