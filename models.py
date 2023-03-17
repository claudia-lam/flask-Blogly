"""Models for Blogly."""
import datetime

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

def connect_db(app):
    """Connect to database."""

    app.app_context().push()
    db.app = app
    db.init_app(app)


class User(db.Model):
    """User for blogly"""
    __tablename__ = "users"
    #backref to post: 'posts'
    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True)

    first_name = db.Column(
        db.String(50),
        nullable=False)

    last_name = db.Column(
        db.String(50),
        nullable=False)

    #TODO: add default image
    img_url = db.Column(
        db.String(),
        nullable=False)

    posts = db.relationship(
        "Post",
        backref="user")

class Post(db.Model):
    """Post for user's blog"""
    __tablename__ = "posts"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True)
    post_title = db.Column(
        db.String(100),
        nullable=False
    )
    post_content = db.Column(
        db.String(),
        nullable=False
    )
    created_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.datetime.now()
    )
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id'),
        nullable=False
    )


