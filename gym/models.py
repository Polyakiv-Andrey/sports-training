from django.contrib.auth.models import AbstractUser
from django.db import models


class Athlete(AbstractUser):
    photo = models.ImageField(upload_to="photos", blank=True, null=True)
    experience = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ["username"]

    def __str__(self):
        if self.first_name:
            return f"{self.first_name} {self.last_name}"
        else:
            return f"{self.username}"


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
    training_description = models.TextField(default="It is the best training in the world")
    exercises = models.ManyToManyField(Exercise)

    def __str__(self):
        return f"{self.training_name}"

