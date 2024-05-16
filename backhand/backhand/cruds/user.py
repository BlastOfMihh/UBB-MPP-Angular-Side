from backhand import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__='users'
    id_ = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    # from tutorial:
    # cart = db.Column(JSON, nullable=True, default=list)  # Make cart nullable

    # # Define the relationship between User and CartProducts
    # cart_products = relationship('CartProducts', backref="user", lazy="dynamic")
    # # Define the relationship between User and Wishlists
    # wishlists = db.relationship('Wishlists', backref='user', lazy=True)

    def __repr__(self):
        return f'<User {self.username}>'