from django.forms import ModelForm
from django_registration.forms import RegistrationForm

from .models import TimeEntry, Profile


class TimeEntryForm(ModelForm):
    def clean_data(self):
        return self.changed_data["day_in_week", "date", "start_time", "end_time", "job"]

    class Meta:
        model = TimeEntry
        fields = ["day_in_week", "date", "start_time", "end_time", "job"]


class MyCustomUserForm(RegistrationForm):
    class Meta(RegistrationForm.Meta):
        model = Profile
        fields = ["email", "username", "password1", "password2"]

#TODO: Add ProfileForm to edit user profile