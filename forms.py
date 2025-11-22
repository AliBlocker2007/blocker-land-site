from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, SelectField
from wtforms.validators import DataRequired, Email, Length


class SignupForm(FlaskForm):
username = StringField('نام کاربری', validators=[DataRequired(), Length(min=3)])
email = StringField('ایمیل', validators=[DataRequired(), Email()])
password = PasswordField('رمز عبور', validators=[DataRequired(), Length(min=6)])
submit = SubmitField('ثبت‌نام')


class LoginForm(FlaskForm):
username = StringField('نام کاربری', validators=[DataRequired()])
password = PasswordField('رمز عبور', validators=[DataRequired()])
submit = SubmitField('ورود')


class BookForm(FlaskForm):
date = DateField('تاریخ', validators=[DataRequired()], format='%Y-%m-%d')
time = SelectField('ساعت', choices=[('09:00','09:00'),('10:00','10:00'),('11:00','11:00'),('14:00','14:00'),('15:00','15:00')])
submit = SubmitField('رزرو')
