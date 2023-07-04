from flask import Blueprint, render_template, redirect, url_for, request, flash
from app.db import db
from app.models import User
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    print(email)
    password = request.form.get('password')
    print(password)
    remember = True if request.form.get('remember') else False
    print(remember)
    user = User.query.filter_by(email=email).first()
    print(user)
    if not user or not check_password_hash(user.password, password):
        return render_template('login_error.html')

    login_user(user, remember=remember)
    return redirect(url_for('bp.get_list_of_employees'))


@auth.route('/signup')
def signup():
    return render_template('signup.html')


@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()

    if user:
        flash('Email address already exists')
        return render_template('auth.signup')

    new_user = User(email=email, password=generate_password_hash(password, method='sha256'), name=name,)
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('bp.index'))
