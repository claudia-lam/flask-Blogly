"""Seed file to make sample datat for users db."""

from models import User, Post, db
from app import app

#create all tables
db.drop_all()
db.create_all()

#add users

madelyn = User(first_name="Madelyn", last_name="Romberg", img_url="")
claudia = User(first_name="Claudia", last_name="Lam", img_url="")



#add user objects to session

db.session.add_all([madelyn, claudia])

#commit to session
db.session.commit()
