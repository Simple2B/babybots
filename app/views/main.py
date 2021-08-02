from flask import render_template, Blueprint, request, flash
from flask_login import login_required

from app.forms import ScheduleForm
from app.models import Schedule, Input
from app.controllers import get_last_update


main_blueprint = Blueprint("main", __name__)


@main_blueprint.route("/", methods=["GET", "POST"])
@login_required
def program():
    form = ScheduleForm()
    schedule = Schedule.query.all()[0]
    db_launch_time = schedule.launch_time
    status = schedule.launch_status
    last_update = get_last_update()
    input1 = Input.query.filter(Input.input_name == "value1").first()
    input2 = Input.query.filter(Input.input_name == "value2").first()
    input3 = Input.query.filter(Input.input_name == "value3").first()
    input4 = Input.query.filter(Input.input_name == "value4").first()
    input5 = Input.query.filter(Input.input_name == "value5").first()
    input6 = Input.query.filter(Input.input_name == "value6").first()
    input7 = Input.query.filter(Input.input_name == "value7").first()
    input8 = Input.query.filter(Input.input_name == "value8").first()
    if request.method == "GET":
        if db_launch_time:
            form.launch_time.data = db_launch_time
        form.value1.data = input1.input_value
        form.checkbox1.data = input1.is_locked
        form.value2.data = input2.input_value
        form.checkbox2.data = input2.is_locked
        form.value3.data = input3.input_value
        form.checkbox3.data = input3.is_locked
        form.value4.data = input4.input_value
        form.checkbox4.data = input4.is_locked
        form.value5.data = input5.input_value
        form.checkbox5.data = input5.is_locked
        form.value6.data = input6.input_value
        form.checkbox6.data = input6.is_locked
        form.value7.data = input7.input_value
        form.checkbox7.data = input7.is_locked
        form.value8.data = input8.input_value
        form.checkbox8.data = input8.is_locked
    if form.validate_on_submit():
        input1.input_value = form.value1.data
        input1.is_locked = form.checkbox1.data
        input2.input_value = form.value2.data
        input2.is_locked = form.checkbox2.data
        input3.input_value = form.value3.data
        input3.is_locked = form.checkbox3.data
        input4.input_value = form.value4.data
        input4.is_locked = form.checkbox4.data
        input5.input_value = form.value5.data
        input5.is_locked = form.checkbox5.data
        input6.input_value = form.value6.data
        input6.is_locked = form.checkbox6.data
        input7.input_value = form.value7.data
        input7.is_locked = form.checkbox7.data
        input8.input_value = form.value8.data
        input8.is_locked = form.checkbox8.data
        schedule.launch_time = form.launch_time.data
        schedule.save()
        input1.save()
        input2.save()
        input3.save()
        input4.save()
        input5.save()
        input6.save()
        input7.save()
        input8.save()
        flash("Timer has been set", "success")
        return render_template(
            "program.html", form=form, status=status, last_update=last_update
        )
    return render_template(
        "program.html", form=form, status=status, last_update=last_update
    )
