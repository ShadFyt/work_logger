from django.db.models import fields
from django.forms import ModelForm

from .models import TimeSheet



class TimeSheetQuote(ModelForm):
    class Meta:
        model = TimeSheet
        fields = ['day_in_week', 'start_time', 'end_time', 'location']