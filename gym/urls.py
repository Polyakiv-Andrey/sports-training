from django.urls import path

from gym.views import *

urlpatterns = [
    path("", index, name="index"),
    path("athletes/", AthleteListView.as_view(), name="athletes-list"),
    path("athletes/<int:pk>/", AthleteDetailView.as_view(), name="athletes-detail"),
    path("exercise/", ExerciseListView.as_view(), name="exercise-list"),
    path("exercise/<int:pk>/", ExerciseDetailView.as_view(), name="exercise-detail"),
    path("exercise/create/", ExerciseCreateView.as_view(), name="exercise-create"),
    path("training/", TrainingListView.as_view(), name="training-list"),
    path("training/<int:pk>/", TrainingDetailView.as_view(), name="training-detail"),
]


app_name = "gym"
