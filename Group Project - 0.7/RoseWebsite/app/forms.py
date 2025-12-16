from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateTimeField, DateField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, NumberRange

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=20)])
    submit = SubmitField('Sign In')

class PredictionForm(FlaskForm):
    EventName = StringField('Event Name', validators=[DataRequired(), Length(min=5, max=70)])
    EventLocation = StringField('Location of Event', validators=[DataRequired(), Length(min=2, max=70)])
    EventDate = DateField('Date of Event')
    EventType = SelectField(u'Event Type', choices=['Community Drive', 'Wellness Screening'], validators=[DataRequired()])
    EventBudget = IntegerField('Budget for Event (RM)', validators=[DataRequired(), NumberRange(min=100, max=1000000)])
    AttendanceGoal = IntegerField('Attendance Goal', validators=[DataRequired(), NumberRange(min=10, max=100000)])
    MarketingTypes = SelectField(u'Marketing Type', choices=['Email','Social Media','Community Outreach','Physical Distribution'], validators=[DataRequired()])
    submit = SubmitField('Run Prediction')

