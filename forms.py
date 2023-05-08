from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField
from wtforms.validators import InputRequired, Email, Optional

units = ["Unit 1", "Unit 2", "Unit 3", "Unit 4", "Unit 5", "Unit 6", "Unit 7",
         "Unit 8", "Unit 9", "Unit 10", "Unit 11",
         "Unit 12", "Unit 13", "Unit 14", "Unit 15", "Unit 16", "Unit 17",
         "Unit 18", "Unit 19", "Unit 20", "Unit 21",
         "Unit 22", "Unit 23", "Unit 24", "Unit 25", "Unit 26", "Unit 27",
         "Unit 28", "Unit 29", "Unit 30", "Unit 31",
         "Unit 32", "Unit 33", "Unit 34", "Unit 35", "Unit 36", "Unit 37",
         "Unit 38", "Unit 39", "Unit 40", "Unit 41",
         "Unit 42", "Unit 43", "Unit 44", "Unit 45", "Unit 46", "Unit 47",
         "Unit 48", "Unit 49", "Unit 50", "Complete"]


class RegisterForm(FlaskForm):
    username = StringField("cal.com username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])
    email = StringField("Email", validators=[InputRequired(), Email()])
    first_name = StringField("First Name",  validators=[InputRequired()])
    last_name = StringField("Last Name",  validators=[InputRequired()])
    course_progress = SelectField(
        'Course Progress', choices=[(unit, unit) for unit in units],
        validators=[Optional()])


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])
