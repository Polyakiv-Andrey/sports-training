from django.contrib.auth.models import AbstractUser
from django.db import models


class Athlete(AbstractUser):
    photo = models.ImageField(upload_to="photos")
    experience = models.TextField()

    class Meta:
        ordering = ["username"]

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"


class Exercise(models.Model):
    exercise_creator = models.ForeignKey(Athlete, on_delete=models.CASCADE)
    exercise_name = models.CharField(max_length=255)
    description = models.TextField()
    picture = models.ImageField(upload_to="photos")

    class Meta:
        ordering = ["exercise_name"]

    def __str__(self):
        return f"{self.exercise_name}"


class Training(models.Model):
    training_creator = models.ForeignKey(Athlete, on_delete=models.CASCADE)
    training_name = models.CharField(max_length=255)
    exercises = models.ManyToManyField(Exercise)

    def __str__(self):
        return f"{self.training_name}"

