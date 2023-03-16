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
    """Homepage root, reroute to /users"""
    return redirect ("/users")

@app.get("/users")
def load_users():
    """Load users list"""
    #access db to pull all users
    users = db.session.query(User).all()

    #add users to html list

    return render_template("users.html", users=users)

@app.get("/users/new")
def show_new_user_form():
    """Show add new user form"""
    return render_template("new-user-form.html")

@app.post('/users/new')
def handle_new_user_form():
    """Handle add new user form submission"""
    first_name = request.form["first-name"]
    last_name = request.form["last-name"]
    img_url = request.form["img-url"]

    new_user = User(first_name=first_name, last_name=last_name, img_url=img_url)
    db.session.add(new_user)
    db.session.commit()

    return redirect("/users")

@app.get('/users/<id>')
def show_user_page(id):
    """show individual user page"""
    user = db.session.query(User).filter(User.id==id).one()

    return render_template("user-detail.html", user=user)

@app.get('/users/<id>/edit')
def show_edit_user_form(id):
    """Show edit user form"""
    user = db.session.query(User).filter(User.id==id).one()

    return render_template('edit-user-form.html', user=user)


@app.post('/users/<id>/edit')
def handle_edit_user_form(id):
    """Show edit user form"""
    user = db.session.query(User).filter(User.id==id)

    first_name = request.form["first-name"]
    last_name = request.form["last-name"]
    img_url = request.form["img-url"]

    user.first_name = first_name
    user.last_name = last_name
    user.img_url = img_url
    db.session.commit()

    return redirect('/users')


