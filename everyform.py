from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField
from wtforms.validators import Length, InputRequired, EqualTo

class registerform(FlaskForm):
    username = StringField("Nombre se Ususario:",
        validators=[Length(min=5, max=12, message="Nombre de usuario debe ser entre 4 y 12 caracteres"),
        InputRequired(message="Nombre de usuario necesario") ])
    password = PasswordField("Contraseña",
        validators=[Length(min=5, max=12, message="contraseña debe ser entre 8 y 20 caracteres"),
        InputRequired(message="Contraseña necesaria") ])
    confirm_pass = PasswordField("Confirmar",
        validators=[ EqualTo("password", message="las contraseñas deben coincidir"),
        InputRequired(message="campo necesario")])
    submit = SubmitField("Crear")
