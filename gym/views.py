from django.shortcuts import render
from django.views import generic

from gym.models import Athlete, Exercise, Training


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


class AthleteListView(generic.ListView):
    model = Athlete


class AthleteDetailView(generic.DetailView):
    model = Athlete


class ExerciseListView(generic.ListView):
    model = Exercise
    queryset = Exercise.objects.all().select_related("exercise_creator")


class TrainingListView(generic.ListView):
    model = Training
    queryset = Training.objects.all().select_related("training_creator")
