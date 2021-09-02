from flask import Blueprint, render_template, url_for, redirect, flash, request
from flask_login import login_user, logout_user, login_required
from datetime import datetime


from app.models import User
from app.forms import LoginForm, RegistrationForm
from app.logger import log

auth_blueprint = Blueprint("auth", __name__)


@auth_blueprint.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm(request.form)
    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data,
        )
        user.save()
        login_user(user)
        flash("Registration successful. You are logged in.", "success")
        return redirect(url_for("main.program"))
    elif form.is_submitted():
        flash("The given data was invalid.", "danger")
    return render_template("auth/register.html", form=form)


@auth_blueprint.route("/login", methods=["GET", "POST"])
def login():
    log(log.INFO, "login")
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user: User = User.authenticate(form.user_id.data, form.password.data)
        if user is not None:
            user.delta_time_hours = int(form.current_time.data) - int(datetime.now().time().hour)
            user.save()
            login_user(user)
            flash("Login successful.", "success")
            return redirect(url_for("main.program"))

        log(log.WARNING, "Wrong user ID or password")
        flash("Wrong user ID or password.", "danger")
    elif form.is_submitted():
        flash("Validation not pass")
        log(log.ERROR, "%s", form.errors)

    return render_template("auth/login.html", form=form)


@auth_blueprint.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You were logged out.", "info")
    return redirect(url_for("main.program"))
