from flask import render_template, Blueprint, request
from flask_login import login_required
from app.forms import ScheduleForm

from app.models import Schedule
from app.logger import log

main_blueprint = Blueprint("main", __name__)


@main_blueprint.route("/", methods=["GET", "POST"])
@login_required
def program():
    form = ScheduleForm()
    schedule = Schedule.query.all()[0]
    db_launch_time = schedule.launch_time
    if request.method == "GET":
        if db_launch_time:
            form.launch_time.data = db_launch_time
    if form.validate_on_submit():
        launch_time = form.launch_time.data
        db_launch_time = launch_time
        schedule.save()
        return render_template("program.html", form=form)
    return render_template("program.html", form=form)
