from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Rose Admin 1275'}
    return render_template('index.html', title='Home', user=user)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/prediction')
def prediction():
    return render_template('temp.html', title='Prediction')

@app.route('/revision')
def revision():
    return render_template('temp.html', title='Revision')

@app.route('/outcome')
def outcome():
    return render_template('temp.html', title='Outcome')