import email_validator
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('Usuario',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Correo',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    confirm_password = PasswordField('Confirme Contraseña',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Registrarse')


class LoginForm(FlaskForm):
    email = StringField('Correo',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    remember = BooleanField('Recuerdame')
    submit = SubmitField('Iniciar Sesion')