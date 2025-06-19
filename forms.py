from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, Optional

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class StudyGoalForm(FlaskForm):
    subject = StringField('Subject', validators=[DataRequired()])
    hours_spent = IntegerField('Hours Spent', validators=[DataRequired()])
    submit = SubmitField('Add Goal')

class NoteForm(FlaskForm):
    note_content = TextAreaField('Note', validators=[Optional()])
    submit = SubmitField('Save Note')