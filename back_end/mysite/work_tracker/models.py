from typing import List
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from datetime import datetime
from django.urls import reverse
from django.utils import timezone
from django.core.mail import send_mail


# Create your models here.


class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, first_name, password=None):
        if not email:
            raise ValueError("Must have valid email address")
        if not username:
            raise ValueError("Users must have a username")
        if not first_name:
            raise ValueError("Users must have a first name")

        user = self.model(
            email=self.normalize_email(email), username=username, first_name=first_name
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, first_name, password=None):
        user = self.create_user(
            email,
            username=username,
            first_name=first_name,
            password=password,
        )

        user.is_admin = True
        user.save(using=self._db)
        return user


class Profile(AbstractBaseUser):
    # Custom User model
    email = models.EmailField(verbose_name="email", max_length=100, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyAccountManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name"]

    def __str__(self):
        return f"Email: {self.email}, Username: {self.username}"

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.is_admin

    # return full name ex.. John Doe
    @property
    def full_name(self):
        return f"{self.first_name.title()} {self.last_name.title()}"

    def email_user(self, *args, **kwargs):
        # adds email_user method to my custom user model

        send_mail(
            "{}".format(args[0]),
            "{}".format(args[1]),
            "{}".format(args[2]),
            [self.email],
            fail_silently=False,
        )


class Job(models.Model):

    name = models.CharField(max_length=50, unique=True)
    job_type = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    sqft = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return f"Name: {self.name.title()}, Location: {self.location}"


class TimeEntry(models.Model):
    """
    A model used to represent an employee time punch clock

    ATTR
    {
        day_in_week: 'MON',
        date: '2021-05-22',
        start_time: '7:00',
        end_time: '15:00',
        job: Job
    }

    """

    class DayInWeek(models.TextChoices):
        MONDAY = "MON", ("Monday")
        TUESDAY = "TUE", ("Tuesday")
        WEDNESDAY = "WED", ("Wednesday")
        THURSDAY = "THU", ("Thursday")
        FRIDAY = "FRI", ("Friday")
        SATURDAY = "SAT", ("Saturday")
        SUNDAY = "SUN", ("Sunday")

    day_in_week = models.CharField(max_length=3, choices=DayInWeek.choices)
    date = models.DateField(default=datetime.now)
    start_time = models.CharField(max_length=10)
    end_time = models.CharField(max_length=10)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="time_entry")
    employee = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="employee"
    )

    @property
    def get_total_hours(self):
        # Convert string: "9:00" into float: 9.0 then
        # Get the difference of the two numbers
        total = abs(
            float(self.start_time.replace(":", "."))
            - float(self.end_time.replace(":", "."))
        )
        return round(total, 2)

    @property
    def day_label(self):
        # returns the label for DayInWeek(TextChoices)
        # example TimeEntry.DayInWeek('MON').label 'Monday'
        for day in self.DayInWeek:
            if self.day_in_week == day:
                return day.label

    def __str__(self) -> str:
        return f"{self.day_in_week}, start {self.start_time}, end {self.end_time}"

    def __repr__(self) -> str:
        return f"{__class__.__name__}: date: {self.date}"

    class Meta:
        ordering = ["-date"]


# TODO: Make expense model
class Expense(models.Model):

    item_name = models.CharField(max_length=50)
    store = models.CharField(max_length=50)
    price = models.FloatField(default=0.00)
    date = models.DateField(default=datetime.now)
    description = models.TextField(max_length=500, blank=True, null=True)
    paid = models.BooleanField(default=True)
    job = models.ForeignKey(Job, verbose_name="job", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "expense"
        verbose_name_plural = verbose_name + "s"

    def __str__(self):
        return (
            f"{self.item_name} was purchased at {self.store.title()} for ${self.price}"
        )

    def get_absolute_url(self):
        return reverse("expense_detail", kwargs={"pk": self.pk})

    @property
    def price_plus_tax(self):
        GST = 0.013
        return self.price * GST


class WeekTimeEntries:
    def __init__(self, date_one: datetime, date_two: datetime, pay_rate: int) -> None:
        self.date_one = date_one
        self.date_two = date_two
        self.pay_rate = pay_rate
        self.sheet = TimeEntry.objects.filter(
            date__gte=self.date_one, date__lte=self.date_two
        )

    @property
    def display_time_sheet(self):
        ordered_sheet = self.sheet.order_by("date")
        for i in ordered_sheet:
            print(
                f"{i.day_label}: {i.date}, Start time: {i.start_time}, End time: {i.end_time}, Location: Temp, Hours: {i.get_total_hours}"
            )

    @property
    def total_week_hours(self):
        hours: List = []
        for i in self.sheet:
            hours.append(i.get_total_hours)

        return f"Total hours worked for the week is: {sum(hours)}"
