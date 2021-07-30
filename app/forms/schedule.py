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
    value1 = FloatField('Value')
    value2 = FloatField('Value')
    value3 = FloatField('Value')
    value4 = FloatField('Value')
    value5 = FloatField('Value')
    value6 = FloatField('Value')
    value7 = FloatField('Value')
    value8 = FloatField('Value')
    checkbox1 = BooleanField()
    checkbox2 = BooleanField()
    checkbox3 = BooleanField()
    checkbox4 = BooleanField()
    checkbox5 = BooleanField()
    checkbox6 = BooleanField()
    checkbox7 = BooleanField()
    checkbox8 = BooleanField()
    submit = SubmitField("Start timer")
