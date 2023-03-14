from flask import Flask, render_template, request
from Creatures_Desk import Creature, Ability

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/den")
def den():
    all_creature = Creature.objects()
    return render_template("den.html", all_creature=all_creature)

@app.route("/creature")
def creature():
    name = request.args.get("name")
    return render_template("creatutre.html", name=name)

if __name__ == '__main__':
    app.run(debug=True)
