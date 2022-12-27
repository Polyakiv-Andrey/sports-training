from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from gym.models import Athlete, Exercise, Training


@login_required
def index(request):

    num_athletes = Athlete.objects.count()
    num_exercises = Exercise.objects.count()
    num_trainings = Training.objects.count()

    context = {
        "num_athletes": num_athletes,
        "num_exercises": num_exercises,
        "num_trainings": num_trainings
    }
    return render(request, "gym/index.html", context=context)


class AthleteListView(LoginRequiredMixin, generic.ListView):
    model = Athlete
    paginate_by = 5


class AthleteDetailView(LoginRequiredMixin, generic.DetailView):
    model = Athlete


class ExerciseListView(LoginRequiredMixin, generic.ListView):
    model = Exercise
    queryset = Exercise.objects.all().select_related("exercise_creator")
    paginate_by = 5


class ExerciseDetailView(LoginRequiredMixin, generic.DetailView):
    model = Exercise


class ExerciseCreateView(LoginRequiredMixin, generic.CreateView):
    model = Exercise
    fields = "__all__"
    success_url = reverse_lazy("gym:athletes-list")


class TrainingListView(LoginRequiredMixin, generic.ListView):
    model = Training
    queryset = Training.objects.all().select_related("training_creator")
    paginate_by = 5


class TrainingDetailView(LoginRequiredMixin, generic.DetailView):
    model = Training
