import sqlite3
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import login_required, apology

# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
con = sqlite3.connect("wechat.db", check_same_thread=False)
db = con.cursor()


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["POST", "GET"])
@login_required
def index():
    """index of the game"""
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("email"):
            return apology("must provide email", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = list(db.execute("SELECT * FROM users WHERE username = ?",
                          (request.form.get("email"),)))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[4], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/register", methods=["POST", "GET"])
def register():
    """login fucntion"""
    if request.method == "POST":

        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        # Ensure email was submitted
        if not first_name:
            return apology("must provide first name", 403)

        # Ensure email was submitted
        if not last_name:
            return apology("must provide last name", 403)

        # Ensure email was submitted
        if not username:
            return apology("must provide usernaname", 403)

        # Ensure email was submitted
        if not email:
            return apology("must provide email", 403)

        # Ensure email was submitted
        if not password:
            return apology("must provide password", 403)

        hash = generate_password_hash(password)

        # Query database for username
        try:
            db.execute("INSERT INTO users (first_name, last_name, email, hash, username) VALUES(?,?,?,?,?)", (first_name, last_name, email, hash, username,))
        except ValueError:
            return apology("choose a different username", 400)
        # Remember which user has logged in
        rows = list(db.execute("SELECT * FROM users WHERE username = ?",(request.form.get("username"),)))

        session["user_id"] = rows[0]

        return redirect("/")
    else:
        return render_template("register.html")


if __name__ == ("__main__"):
    app.run(debug=True)
    """_summary_"""
