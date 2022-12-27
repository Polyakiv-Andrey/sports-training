from django.urls import path

from gym.views import *

urlpatterns = [
    path("", index, name="index"),
    path("athletes/", AthleteListView.as_view(), name="athletes-list"),
    path("exercise/", ExerciseListView.as_view(), name="exercise-list"),
    path("training/", TrainingListView.as_view(), name="training-list"),
]


app_name = "gym"
