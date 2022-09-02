from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from models.models import User, db

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False

        user = User.query.filter_by(login=email).first()
        if not user or not check_password_hash(user.password, password):
            flash('Email ou senha inválidos')
            return redirect(url_for('auth.login'))
        login_user(user, remember=remember)
        return redirect(url_for('login.index'))
    else:
        return render_template('login.html')


@auth.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        agency = request.form.get('agency')
        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')

        user = User.query.filter_by(login=email).first()
        if user:
            flash('Email já cadastrado')
            return redirect(url_for('auth.signup'))
        new_user = User(agency=agency, login=email, name=name,
                        password=generate_password_hash(password, method='sha256'), admin=False)

        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('auth.login'))
    else:
        return render_template('signup.html')


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login.index'))
