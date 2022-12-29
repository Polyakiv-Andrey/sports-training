from django.urls import path

from gym.views import *

urlpatterns = [
    path("login/", LoginUser.as_view(), name="login"),
    path("logout/", logout_user, name="logout"),
    path("", index, name="index"),
    path("athletes/", AthleteListView.as_view(), name="athletes-list"),
    path("athletes/<int:pk>/", AthleteDetailView.as_view(), name="athletes-detail"),
    path("athletes/create/", AthleteCreateView.as_view(), name="athletes-create"),
    path("athletes/<int:pk>/update/", AthleteUpdateView.as_view(), name="athletes-update"),
    path("athletes/<int:pk>/delete/", AthleteDeleteView.as_view(), name="athletes-delete"),
    path("exercise/", ExerciseListView.as_view(), name="exercise-list"),
    path("exercise/<int:pk>/", ExerciseDetailView.as_view(), name="exercise-detail"),
    path("exercise/create/", ExerciseCreateView.as_view(), name="exercise-create"),
    path("exercise/<int:pk>/update/", ExerciseUpdateView.as_view(), name="exercise-update"),
    path("exercise/<int:pk>/delete/", ExerciseDeleteView.as_view(), name="exercise-delete"),
    path("training/", TrainingListView.as_view(), name="training-list"),
    path("training/<int:pk>/", TrainingDetailView.as_view(), name="training-detail"),
    path("training/create/", TrainingCreateView.as_view(), name="training-create"),
    path("training/<int:pk>/update/", TrainingUpdateView.as_view(), name="training-update"),
    path("training/<int:pk>/delete/", TrainingDeleteView.as_view(), name="training-delete"),
]


app_name = "gym"
