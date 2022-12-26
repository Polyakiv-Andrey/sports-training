from django.urls import path

from gym.views import *

urlpatterns = [
    path("", index, name="index"),
]


app_name = "gym"
