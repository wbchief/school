from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('请输入用户名:', validators=[DataRequired()])
    password = PasswordField('请输入密码:', validators=[DataRequired()])
    submit = SubmitField('确认')