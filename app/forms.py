from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired, Optional

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    login = StringField('Имя', validators=[Optional()])
    second_name = StringField('Фамилия', validators=[Optional()])
    third_name = StringField('Отчество', validators=[Optional()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_confirm = PasswordField('Повторите пароль', validators=[Optional()])
    email = StringField('Email', validators=[DataRequired()])
    phone_number = IntegerField('Номер телефона', validators=[Optional()])
    is_entity = BooleanField('Юр. лицо?', validators=[Optional()])
    entity_name = StringField('Наименование организации', validators=[Optional()])
    iin = IntegerField('ИИН', validators=[Optional()])
    ogrn = IntegerField('ОГРН', validators=[Optional()])
    ref_code = StringField('Реферальный код', validators=[Optional()])


    submit = SubmitField('Sign In')

class ProcessPayment(FlaskForm):
    is_entity = BooleanField('Списать бонусные рубли?', validators=[Optional()])

    submit = SubmitField('Оплатить')