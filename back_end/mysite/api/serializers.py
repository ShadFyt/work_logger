from django.db.models import fields
from rest_framework import serializers

from work_tracker.models import TimeEntry, Job


class TimeEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeEntry
        fields = ("day_in_week", "date", "start_time", "end_time", "job", "employee")


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ("name", "job_type", "location", "sqft", "description")
