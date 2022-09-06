from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.


# class User(AbstractUser):
#     """user model"""
#     email = models.EmailField(max_length=255, unique=True)
#     username = models.CharField(max_length=20, unique=True)
#     password = models.CharField(max_length=50)

#     def __str__(self):
#         return self.email


class Schedule(models.Model):
    """schedule model"""
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='schedules')
    schedule_name = models.CharField(max_length=50)

    def __str__(self):
        return self.schedule_name


class Day(models.Model):
    """day model"""
    schedule = models.ForeignKey(
        Schedule, on_delete=models.CASCADE, related_name='days')
    week_name = models.CharField(max_length=50)
    day_of_week = models.DateField(max_length=50)

    def __str__(self):
        return self.week_name


class Exercise(models.Model):
    """exercise model"""
    day = models.ForeignKey(
        Day, on_delete=models.CASCADE, related_name='exercises')
    exercise_name = models.CharField(max_length=50)
    weight = models.IntegerField()
    set = models.IntegerField()
    reps = models.IntegerField()

    def __str__(self):
        return self.exercise_name
