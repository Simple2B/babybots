import datetime
from flask_wtf import FlaskForm
from wtforms import SubmitField, TimeField, FloatField, BooleanField


class NullableDateField(TimeField):
    """Native WTForms DateField throws error for empty dates.
    Let's fix this so that we could have DateField nullable."""

    def process_formdata(self, valuelist):
        if valuelist:
            date_str = " ".join(valuelist).strip()
            if date_str == "":
                self.data = None
                return
            try:
                self.data = datetime.datetime.strptime(date_str, self.format).time()
            except ValueError:
                self.data = None
                raise ValueError(self.gettext("Not a valid date value"))


class ScheduleForm(FlaskForm):

    launch_time = NullableDateField("Launch Time")
    value1 = FloatField("DeadStock")
    value2 = FloatField("Special DeadStock")
    value3 = FloatField("Lightly Worm")
    value4 = FloatField("Moderate Ware")
    value5 = FloatField("Heavy Ware")
    value6 = FloatField("Replacement Box")
    value7 = FloatField("B Grade")
    value8 = FloatField("Special Lightly Worm")
    value9 = FloatField("Special Moderately Worn")
    value10 = FloatField("Special Heavily Worm")
    checkbox1 = BooleanField()
    checkbox2 = BooleanField()
    checkbox3 = BooleanField()
    checkbox4 = BooleanField()
    checkbox5 = BooleanField()
    checkbox6 = BooleanField()
    checkbox7 = BooleanField()
    checkbox8 = BooleanField()
    checkbox9 = BooleanField()
    checkbox10 = BooleanField()
    submit = SubmitField("Start timer")
    submit_manual = SubmitField("Manual start")
    submit_reset = SubmitField("Reset timer")
