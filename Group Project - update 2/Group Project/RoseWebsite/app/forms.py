from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateTimeField, DateField, IntegerField, TextAreaField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class Prediction(FlaskForm):
    EventName = StringField('Event Name', validators=[DataRequired()])
    EventDate = DateField('Date of Event', format="%d-%m-%Y", validators=[DataRequired()])
    EventLocation = StringField('Location of Event', validators=[DataRequired()])
    EventBudget = IntegerField('Budget for Event (RM)', validators=[DataRequired()])
    NumParticipents = IntegerField('Expected Number of Participents', validators=[DataRequired()])
    EventDescription = TextAreaField('Event Description / Notes', validators=[DataRequired()])
    submit = SubmitField('Run Prediction')