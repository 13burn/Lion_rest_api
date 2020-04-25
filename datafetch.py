from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class userName(db.Model):
    """
    Model users
    >Renovar datos por renovacion de instalacion<
    """

    __tablename__ = "usuarios"
    """Nombres en base a los nombres de las tablas de la base"""
    ID=db.Column(db.Integer, primary_key = True)#numero de ID
    UID = db.Column(db.String(25), unique=True, nullable = False)#nombre de usuarios
    Passkey = db.Column(db.String(), nullable = False)#contraseña
