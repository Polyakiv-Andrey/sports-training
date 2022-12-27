from django.urls import path

from gym.views import *

urlpatterns = [
    path("", index, name="index"),
    path("athletes/", AthleteListView.as_view(), name="athletes-list"),
    path("athletes/<int:pk>/", AthleteDetailView.as_view(), name="athletes-detail"),
    path("exercise/", ExerciseListView.as_view(), name="exercise-list"),
    path("exercise/<int:pk>/", ExerciseDetailView.as_view(), name="exercise-detail"),
    path("exercise/create/", ExerciseCreateView.as_view(), name="exercise-create"),
    path("exercise/<int:pk>/update/", ExerciseUpdateView.as_view(), name="exercise-update"),
    path("exercise/<int:pk>/delete/", ExerciseDeleteView.as_view(), name="exercise-delete"),
    path("training/", TrainingListView.as_view(), name="training-list"),
    path("training/<int:pk>/", TrainingDetailView.as_view(), name="training-detail"),
    path("training/create/", TrainingCreateView.as_view(), name="training-create"),
]


app_name = "gym"
