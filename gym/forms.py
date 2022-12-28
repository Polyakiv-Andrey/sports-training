from django.contrib.auth.forms import UserCreationForm

from gym.models import Athlete


class AthleteCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Athlete
        fields = ("username", "password1", "password2")
