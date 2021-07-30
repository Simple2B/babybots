import datetime
from flask_wtf import FlaskForm
from wtforms import DateTimeField, SubmitField, DateField


class NullableDateField(DateField):
    """Native WTForms DateField throws error for empty dates.
    Let's fix this so that we could have DateField nullable."""

    def process_formdata(self, valuelist):
        if valuelist:
            date_str = " ".join(valuelist).strip()
            if date_str == "":
                self.data = None
                return
            try:
                self.data = datetime.datetime.strptime(date_str, self.format).date()
            except ValueError:
                self.data = None
                raise ValueError(self.gettext("Not a valid date value"))


class ScheduleForm(FlaskForm):

    launch_time = NullableDateField("Launch Time")
    submit = SubmitField("Start timer")
