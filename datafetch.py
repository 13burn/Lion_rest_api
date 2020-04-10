from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class userName(db.Model):
    """Model users"""
    __tablename__ = "users"
    id=db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(25), unique=True, nullable = False)
    password = db.Column(db.String(), nullable = False)
