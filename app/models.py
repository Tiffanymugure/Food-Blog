# importing db
from . import db
# security model providing haching functionality
from werkzeug.security import generate_password_hash, check_password_hash

# import login manager
from . import login_manager

from datetime import datetime

# import class UserMixin
from flask_login import UserMixin


class User(UserMixin, db.Model):
    """
    creating class writer for creating blog writer and connecting it to database via db.Model
    """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), index=True)
    email = db.Column(db.String(255), unique=True, index=True)
    post = db.relationship('Post', backref='users', lazy='dynamic')
    comment = db.relationship('Comments', backref='users', lazy='dynamic')
    pass_secure = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())

    # call  back function retrieving writer id
    @login_manager.user_loader
    def load_writer(user_id):
        return User.query.get(int(user_id))

    def set_password(self, password):
        """
        method to set passwords
        """
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        """
        method to verify password
        """
        return check_password_hash(self.pass_secure, password)

    def __repr__(self):
        return f'Writer {self.username}'


class Post(db.Model):
    """
    creating class for creating blog posts
    """
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(255))
    header = db.Column(db.String(1000))
    post = db.Column(db.String(1000000))
    time = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comment = db.relationship('Comments', backref='post', lazy='dynamic')

    def save_post(self):
        """
        method to save blog posts
        """
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_post(cls, category):
        """
        method to return posts
        """
        post = Post.query.filter_by(category=category).all()
        return post

    def delete_post(self):
        """
        method to delete comments
        """
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f'User {self.category}'


class Comments(db.Model):
    """
    class Comments to create table for comments
    """
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    comment = db.Column(db.String(267))
    time = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    post_id =db.Column(db.Integer, db.ForeignKey('post.id'))

    def save_comments(self):
        """
        method to save comments
        """
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls, id):
        """
        method to return comments
        """
        comments = Comments.query.filter_by(comment=id).all()
        return comments

    def delete_comments(self):
        """
        method to delete comments
        """
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f'User {self.comment}'


class Subscriber(db.Model):
    """
    class subscriber to subscriber users
    """
    __tablename__ = 'subscribers'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), index=True)
    email = db.Column(db.String(255), unique=True, index=True)

    def save_subscriber(self):
        """
        method to save subscriber
        """
        db.session.add(self)
        db.session.commit()

    def get_subscriber(self, username):
        """
        method to get subscriber
        """
        email = Subscriber.query.filter_by(email=username).all()
        return email