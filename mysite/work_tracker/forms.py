from django.forms import ModelForm

from .models import TimeEntry


class TimeEntryForm(ModelForm):
    def clean_data(self):
        return self.changed_data["day_in_week", "date", "start_time", "end_time", "job"]

    class Meta:
        model = TimeEntry
        fields = ["day_in_week", "date", "start_time", "end_time", "job"]
