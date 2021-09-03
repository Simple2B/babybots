from datetime import time
from flask import render_template, Blueprint, request, flash, jsonify
from flask_login import login_required, current_user

from app.forms import ScheduleForm
from app.models import Schedule, Input
from app.controllers import get_last_update
from app.logger import log


main_blueprint = Blueprint("main", __name__)


@main_blueprint.route("/", methods=["GET", "POST"])
@login_required
def program():
    form = ScheduleForm()
    schedule = Schedule.query.first()
    if not schedule:
        schedule = Schedule()
        schedule.save()
    db_launch_time = schedule.launch_time + current_user.delta_time_hours * 60
    status = schedule.is_run
    last_update = get_last_update()
    input1 = Input.query.filter(Input.name == "value1").first()
    input2 = Input.query.filter(Input.name == "value2").first()
    input3 = Input.query.filter(Input.name == "value3").first()
    input4 = Input.query.filter(Input.name == "value4").first()
    input5 = Input.query.filter(Input.name == "value5").first()
    input6 = Input.query.filter(Input.name == "value6").first()
    input7 = Input.query.filter(Input.name == "value7").first()
    input8 = Input.query.filter(Input.name == "value8").first()
    input9 = Input.query.filter(Input.name == "value9").first()
    input10 = Input.query.filter(Input.name == "value10").first()
    if request.method == "GET":
        if db_launch_time:
            form.launch_time.data = time(
                hour=(db_launch_time // 60) % 24, minute=db_launch_time % 60
            )
        form.value1.data = input1.value
        form.checkbox1.data = input1.is_locked
        form.value2.data = input2.value
        form.checkbox2.data = input2.is_locked
        form.value3.data = input3.value
        form.checkbox3.data = input3.is_locked
        form.value4.data = input4.value
        form.checkbox4.data = input4.is_locked
        form.value5.data = input5.value
        form.checkbox5.data = input5.is_locked
        form.value6.data = input6.value
        form.checkbox6.data = input6.is_locked
        form.value7.data = input7.value
        form.checkbox7.data = input7.is_locked
        form.value8.data = input8.value
        form.checkbox8.data = input8.is_locked
        form.value9.data = input9.value
        form.checkbox9.data = input9.is_locked
        form.value10.data = input10.value
        form.checkbox10.data = input10.is_locked
    if form.validate_on_submit():
        if form.submit_manual.data:
            manual_start(form)
        elif form.submit.data:
            timer_start(form)
        else:
            log(log.ERROR, "Wrong submit type")
    return render_template(
        "program.html", form=form, status=status, last_update=last_update
    )


def timer_start(form: ScheduleForm):
    schedule = Schedule.query.first()
    input1 = Input.query.filter(Input.name == "value1").first()
    input2 = Input.query.filter(Input.name == "value2").first()
    input3 = Input.query.filter(Input.name == "value3").first()
    input4 = Input.query.filter(Input.name == "value4").first()
    input5 = Input.query.filter(Input.name == "value5").first()
    input6 = Input.query.filter(Input.name == "value6").first()
    input7 = Input.query.filter(Input.name == "value7").first()
    input8 = Input.query.filter(Input.name == "value8").first()
    input9 = Input.query.filter(Input.name == "value9").first()
    input10 = Input.query.filter(Input.name == "value10").first()
    input1.value = form.value1.data
    input1.is_locked = form.checkbox1.data
    input2.value = form.value2.data
    input2.is_locked = form.checkbox2.data
    input3.value = form.value3.data
    input3.is_locked = form.checkbox3.data
    input4.value = form.value4.data
    input4.is_locked = form.checkbox4.data
    input5.value = form.value5.data
    input5.is_locked = form.checkbox5.data
    input6.value = form.value6.data
    input6.is_locked = form.checkbox6.data
    input7.value = form.value7.data
    input7.is_locked = form.checkbox7.data
    input8.value = form.value8.data
    input8.is_locked = form.checkbox8.data
    input9.value = form.value9.data
    input9.is_locked = form.checkbox9.data
    input10.value = form.value10.data
    input10.is_locked = form.checkbox10.data
    schedule.launch_time = (
        form.launch_time.data.minute + (form.launch_time.data.hour - current_user.delta_time_hours) * 60
    )
    schedule.save()
    input1.save()
    input2.save()
    input3.save()
    input4.save()
    input5.save()
    input6.save()
    input7.save()
    input8.save()
    input9.save()
    input10.save()
    flash("Timer has been set", "success")
    log(log.INFO, "Before launching script")


def manual_start(form: ScheduleForm):
    flash("Manual Start", "success")
    input1 = Input.query.filter(Input.name == "value1").first()
    input2 = Input.query.filter(Input.name == "value2").first()
    input3 = Input.query.filter(Input.name == "value3").first()
    input4 = Input.query.filter(Input.name == "value4").first()
    input5 = Input.query.filter(Input.name == "value5").first()
    input6 = Input.query.filter(Input.name == "value6").first()
    input7 = Input.query.filter(Input.name == "value7").first()
    input8 = Input.query.filter(Input.name == "value8").first()
    input9 = Input.query.filter(Input.name == "value9").first()
    input10 = Input.query.filter(Input.name == "value10").first()
    input1.value = form.value1.data
    input1.is_locked = form.checkbox1.data
    input2.value = form.value2.data
    input2.is_locked = form.checkbox2.data
    input3.value = form.value3.data
    input3.is_locked = form.checkbox3.data
    input4.value = form.value4.data
    input4.is_locked = form.checkbox4.data
    input5.value = form.value5.data
    input5.is_locked = form.checkbox5.data
    input6.value = form.value6.data
    input6.is_locked = form.checkbox6.data
    input7.value = form.value7.data
    input7.is_locked = form.checkbox7.data
    input8.value = form.value8.data
    input8.is_locked = form.checkbox8.data
    input9.value = form.value9.data
    input9.is_locked = form.checkbox9.data
    input10.value = form.value10.data
    input10.is_locked = form.checkbox10.data
    input1.save()
    input2.save()
    input3.save()
    input4.save()
    input5.save()
    input6.save()
    input7.save()
    input8.save()
    input9.save()
    input10.save()
    schedule = Schedule.query.first()
    schedule.is_run_now = True
    schedule.save()


@main_blueprint.route("/get_status", methods=["GET"])
@login_required
def get_status():
    schedule = Schedule.query.first()
    status = schedule.is_run
    return jsonify(status)
