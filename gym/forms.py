from django.contrib.auth.forms import UserCreationForm
from django import forms

from gym.models import Athlete, Training, Exercise


class AthleteCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Athlete
        fields = ("username", "password1", "password2")


class TrainingForm(forms.ModelForm):
    exercises = forms.ModelMultipleChoiceField(
        queryset=Exercise.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Training
        fields = "__all__"


class ExerciseSearchForm(forms.Form):
    exercise_name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by exercise name..."})
    )
