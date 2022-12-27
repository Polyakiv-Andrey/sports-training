from django.urls import path

from gym.views import *

urlpatterns = [
    path("", index, name="index"),
    path("athletes/", AthleteListView.as_view(), name="athletes-list")
]


app_name = "gym"
