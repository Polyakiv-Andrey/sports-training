from django.shortcuts import render

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
