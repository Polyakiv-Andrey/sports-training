from django.urls import path

from gym.views import *

urlpatterns = [
    path("", index, name="index"),
    path("athletes/", AthleteListView.as_view(), name="athletes-list"),
    path("athletes/<int:pk>/", AthleteDetailView.as_view(), name="athletes-detail"),
    path("exercise/", ExerciseListView.as_view(), name="exercise-list"),
    path("exercise/<int:pk>/", ExerciseDetailView.as_view(), name="exercise-detail"),
    path("training/", TrainingListView.as_view(), name="training-list"),
]


app_name = "gym"
