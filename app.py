from cs50 import SQL
from flask import Flask, render_template

app = Flask(__name__) 

# Linking to DB
db = SQL("sqlite:///health.db")

@app.route('/')
def index():
    users = db.execute("SELECT * FROM users")
    return render_template('index.html', users=users)