from django.db import models
from django.utils import timezone

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)


class TimeSheet(models.Model):

    class DayInWeek(models.TextChoices):
        MONDAY = 'MON', _('Monday')
        TUESDAY = 'TUE', _('Tuesday')
        WEDNESDAY = 'WED', _('Wednesday')
        THURSDAY = 'THU', _('Thursday')
        FRIDAY = 'FRI', _('Friday')
        SATURDAY = 'SAT', _('Saturday')
        SUNDAY = 'SUN', _('Sunday')

    day_in_week = models.CharField(
        max_length= 3,
        choices=DayInWeek.choices
    )

    date = models.DateField(default=timezone.now)
    start_time = models.DateTimeField(default=8)
    end_time = models.DateTimeField(default=16)
