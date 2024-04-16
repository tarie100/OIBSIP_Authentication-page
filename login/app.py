import bcrypt
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "your_secret_key"

# Dictionary to store user information (username and hashed password)
users = {}

@app.route("/")
def home():
    if "username" in session:
        return redirect("/secured")
    else:
        return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        if username in users:
            return "Username already exists. Please try again."

        password = request.form["password"]
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

        users[username] = hashed_password
        return "Registration successful. <a href='/'>Login</a>"
    else:
        return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username not in users:
            return "Invalid username."

        hashed_password = users[username]
        if bcrypt.checkpw(password.encode(), hashed_password):
            session["username"] = username
            return redirect("/secured")
        else:
            return "Incorrect password."
    else:
        return render_template("login.html")

@app.route("/secured")
def secured_page():
    if "username" in session:
        return "Welcome to the secured page!"
    else:
        return redirect("/")

@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect("/")

if __name__ == "__main__":
    app.run()