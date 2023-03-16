"""Blogly application."""

import os

from flask import Flask, request, redirect, render_template
from models import db, connect_db, User
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", 'postgresql:///blogly')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

app.config['SECRET_KEY'] = "secret-password"
debug = DebugToolbarExtension(app)

@app.get("/")
def load_users_homepage():
    return redirect ("/users")

@app.get("/users")
def load_users():
    #access db to pull all users
    users = db.session.query(User).all()

    #add users to html list

    return render_template("users.html", users=users)

@app.get("/users/new")
def show_new_user_form():
    return render_template("new-user-form.html")

@app.post('/users/new')
def handle_new_user_form():
    first_name = request.form["first-name"]
    last_name = request.form["last-name"]
    img_url = request.form["image-url"]

    new_user = User(first_name=first_name, last_name=last_name, img_url=img_url)
    db.session.add(new_user)
    db.session.commit()

    return redirect("/users")