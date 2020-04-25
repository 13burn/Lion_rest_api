from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField
from wtforms.validators import Length, InputRequired, EqualTo, ValidationError

from datafetch import userName

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
    submit = SubmitField("Crear Cuenta")

    def validate_username(self, username):
        user_object = userName.query.filter_by( UID=username.data).first()#usando el nombre de usuario como se marca en la tabla
        if user_object:
            raise ValidationError("Nombre de usuario ya existe, use otro nombre.")

class loginform(FlaskForm):
    """ formulario login """
    username = StringField("Username_lab", validators=[InputRequired(message="Nombre de usuario necesario.")])
    password = PasswordField("password_lab", validators=[InputRequired(message="Contraseña necesaria.")])
    submit = SubmitField("Iniciar Sesion")


    """analizar la fincion para encontrar errores
    >>>>
    def input_validation(self, username):
        username_in = username.data
        pass_in = loginform.password.data
        print(3)
        user_obj = username.query.filter_by( UID=username_in.data).first()
        if user_obj is None:
            print(1)
            raise ValidationError("Nombre de usuario o contraseña erroneos")
        elif pass_in != user_obj.password:
            print(2)
            raise ValidationError("Nombre de usuario o contraseña erroneos")
    >>>>
    """
