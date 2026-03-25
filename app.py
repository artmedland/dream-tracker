from flask import Flask
from flask import render_template, request, redirect, session

from werkzeug.security import generate_password_hash, check_password_hash

import sqlite3
import config
import db

app = Flask(__name__)
app.secret_key = config.get_session_key()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/create", methods=["POST"])
def create():
    username = request.form["username"]
    password1 = request.form["password1"]
    password2 = request.form["password2"]
    
    if password1 != password2:
        return "ERR: Lösenord olika"
    password_hash = generate_password_hash(password1)

    try:
        sql = """INSERT INTO Users (username, password_hash)
                 VALUES (?, ?)"""
        db.execute(sql, [username, password_hash])
    except sqlite3.IntegrityError:
        return "ERR: Användarnamn upptaget"

    session["username"] = username
    return "Användarkonto skapat"

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    username = request.form["username"]
    password = request.form["password"]

    sql = "SELECT password_hash FROM Users WHERE username = ?"
    password_hash = db.query(sql, [username])[0][0]

    if check_password_hash(password_hash, password):
        session["username"] = username
        return redirect("/")
    else:
        return "ERR: Fel användarnamn eller lösenord"

@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")