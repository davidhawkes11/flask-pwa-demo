from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from .models import User
from . import db, login_manager

bp = Blueprint("main", __name__)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@bp.route("/")
def index():
    return "Flask PWA secure demo"

@bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for("main.index"))
        flash("Invalid credentials", "error")
    return render_template("login.html")

@bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))

@bp.route("/protected")
@login_required
def protected():
    return f"Hello {current_user.email}"
