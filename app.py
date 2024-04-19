from flask import Flask, render_template, request, redirect, session
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)

# User database
users = {}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users:
            return "Username already exists. Please choose a different username."

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        users[username] = hashed_password

        return redirect('/login')

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username not in users:
            return "Username does not exist. Please register."

        hashed_password = users[username]

        if bcrypt.check_password_hash(hashed_password, password):
            session['username'] = username
            return redirect('/dashboard')
        else:
            return "Incorrect password. Please try again."

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return render_template('dashboard.html', username=session['username'])
    else:
        return "You must be logged in to access this page."

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')

if __name__ == '__main__':
    app.secret_key = 'secret_key'
    app.run(debug=True)