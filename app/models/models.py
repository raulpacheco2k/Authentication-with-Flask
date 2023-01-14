from datetime import datetime

from app import db, login_manager


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String, unique=False, nullable=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, unique=False, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    def __int__(self, fullname, username, email, password):
        self.fullname = fullname
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return f"<User {self.username}>"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=False, nullable=False)
    content = db.Column(db.Text, unique=False, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    author = db.relationship('User', foreign_keys=author_id)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __int__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __repr__(self):
        return f"<Post {self.title}>"


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, unique=False, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    author = db.relationship('User', foreign_keys=author_id)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    post = db.relationship('Post', foreign_keys=post_id)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __int__(self, content, author, post):
        self.content = content
        self.author = author
        self.post = post

    def __repr__(self):
        return f"<Comment {self.content}>"


class Follow(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    follower_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    follower = db.relationship('User', foreign_keys=follower_id)
    followed_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    followed = db.relationship('User', foreign_keys=followed_id)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __init__(self, follower, followed):
        self.follower = follower
        self.followed = followed

    def __repr__(self):
        return f"<Follow {self.follower} -> {self.followed}>"
