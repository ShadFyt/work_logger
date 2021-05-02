from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from datetime import datetime
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
            email = self.normalize_email(email),
            username = username,
            first_name = first_name
        )

        user.set_password(password)
        user.save(using = self._db)
        return user
    
    def create_superuser(self, email, username, first_name, password=None):
        user = self.create_user(
            email,
            username = username,
            first_name= first_name,
            password = password,
        )

        user.is_admin = True
        user.save(using = self._db)
        return user

class Profile(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=100, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
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


class TimeSheet(models.Model):
    class DayInWeek(models.TextChoices):
        MONDAY = "MON", ("Monday")
        TUESDAY = "TUE", ("Tuesday")
        WEDNESDAY = "WED", ("Wednesday")
        THURSDAY = "THU", ("Thursday")
        FRIDAY = "FRI", ("Friday")
        SATURDAY = "SAT", ("Saturday")
        SUNDAY = "SUN", ("Sunday")

    day_in_week = models.CharField(max_length=3, choices=DayInWeek.choices)

    date = models.DateField(default=datetime.now())
    start_time = models.TimeField(blank=True)
    end_time = models.TimeField(blank=True)
    location = models.CharField(max_length=100)

    @property
    def day_label(self):
        for day in self.DayInWeek:
            if self.day_in_week == day:
                return day.label

    def __str__(self) -> str:
        return f'{self.date} at {self.location}'

    def __repr__(self) -> str:
        return f'{__class__.__name__}: date: {self.date}, location: {self.location}'

    class Meta:
        ordering = ['-date']
