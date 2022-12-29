from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
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


class TrainingSearchForm(forms.Form):
    training_name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by training name..."})
    )


class AthleteSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by username..."})
    )


