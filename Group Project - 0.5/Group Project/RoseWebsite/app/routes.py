from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm, PredictionForm, RevisionForm
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Rose Admin 1275'}
    return render_template('index.html', title='Home', user=user)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}'.format(
            form.username.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    form = PredictionForm()
    if form.validate_on_submit():
        flash("Prediction '{}' is generating".format(
            form.EventName.data))
        return redirect(url_for('revision'))
    return render_template('prediction.html', title='Prediction', form=form)

@app.route('/input', methods=['GET', 'POST'])
def input():
    return render_template('input.html', title='Input')

@app.route('/outcome')
def outcome():
    return render_template('outcome.html', title='Outcome')