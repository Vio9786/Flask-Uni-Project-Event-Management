from flask import render_template, flash, redirect, url_for, session
from app import app
from app.forms import LoginForm, PredictionForm
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    UserLogins = {'Admin1':'12345123451234512345','Employee1':'12345123451234512345'}
    if form.validate_on_submit():
        if form.username.data in ['Admin1','Employee1']: 
            if UserLogins[form.username.data] == form.password.data:
                session['username'] = form.username.data
                return redirect(url_for('Import'))
        else:
            return redirect(url_for('login'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    form = PredictionForm()
    if session.get('username') not in ['Admin1','Employee1']:
        return redirect(url_for('login'))
    elif session.get('username') == 'Employee1':
        return redirect(url_for('Import'))
    else:    
        UserPerms = session.get('username')
    if form.validate_on_submit():
        return redirect(url_for('outcome'))
    return render_template('prediction.html', title='Prediction', form=form, Perms = UserPerms)

@app.route('/import', methods=['GET', 'POST'])
def Import():
    if session.get('username') not in ['Admin1','Employee1']:
        return redirect(url_for('login'))
    else:
        UserPerms = session.get('username')
    return render_template('import.html', title='Import', Perms = UserPerms)

@app.route('/outcome')
def outcome():
    if session.get('username') not in ['Admin1','Employee1']:
        return redirect(url_for('login'))
    else:
        UserPerms = session.get('username')
    return render_template('outcome.html', title='Outcome', Perms = UserPerms)

@app.route('/logout')
def logout():
    session['username'] = ''
    return redirect(url_for('login'))