#app.py file
from flask import Flask, render_template, request, redirect, url_for, session
from pymongo import MongoClient
import datetime
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'default_secret_key')

# MongoDB connection
client = MongoClient('mongodb://localhost:27017')
db = client['3fastcoders_database']
users_collection = db['usersCollection']


@app.route('/')
def root():
    return redirect(url_for('login'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Check if the username already exists
        if users_collection.find_one({'username': username}):
            return "Username already exists. Please choose a different username."
        user_data = {
            'username': username,
            'password': password,
            'signup_time': datetime.datetime.now()
        }
        users_collection.insert_one(user_data)
        session['username'] = username
        return redirect(url_for('welcome'))
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = users_collection.find_one({'username': username, 'password': password})
        if user:
            session['username'] = username
            return redirect(url_for('welcome'))
        else:
            return "Invalid username or password. Please try again."
    return render_template('login.html')

# show rows of users
@app.route('/welcome')
def welcome():
    if 'username' in session:
        username = session['username']
        userRows = [doc for doc in users_collection.find()]
        return render_template('landing.html', username=username, rows=userRows)
    
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
