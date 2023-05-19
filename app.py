from flask import Flask, render_template
from helpers import login_required

# Configure application
app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
@login_required
def index():
    """index of the game"""
    return render_template("index.html")


if __name__ == ("__main__"):
    app.run(debug=True)
    """_summary_"""
