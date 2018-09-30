from flask_wtf import FlaskForm
from wtforms import SubmitField, TextField, PasswordField
from wtforms.validators import DataRequired, EqualTo, Length, Email, ValidationError
from wtforms.fields.html5 import EmailField


def nospace(form, field):
    print(list(field.data))
    if ' ' in list(field.data):
        raise ValidationError('That is an invalid username')


class SignUpForm(FlaskForm):
    username = TextField('Username',
                         validators=[DataRequired(message='Username length between 3 and 20 characters.'), Length(min=3, max=20), nospace])

    password = PasswordField('Password',
                             validators=[DataRequired(), Length(min=6, max=16)])

    verifyPassword = PasswordField('Verify Password',
                                   validators=[DataRequired(),
                                               EqualTo('password')])

    email = EmailField('Email (optional)',
                       validators=[Email(message=None)])

    submit = SubmitField('Register!')
