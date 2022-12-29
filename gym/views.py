from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from gym.forms import *
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

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(AthleteListView, self).get_context_data(**kwargs)
        username = self.request.GET.get("username", "")
        context["search_field"] = AthleteSearchForm(initial={
            "username": username
        }
        )
        return context

    def get_queryset(self):
        queryset = Athlete.objects.all()
        form = AthleteSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(
                username__icontains=form.cleaned_data["username"]
            )
        return queryset


class AthleteDetailView(LoginRequiredMixin, generic.DetailView):
    model = Athlete


class AthleteCreateView(generic.CreateView):
    form_class = AthleteCreationForm
    success_url = reverse_lazy("gym:index")
    template_name = "gym/athlete_form.html"


class AthleteUpdateView(generic.UpdateView):
    model = Athlete
    fields = ["first_name", "last_name", "email", "photo", "experience"]
    success_url = reverse_lazy("gym:athletes-list")
    template_name = "gym/athlete_form.html"


class AthleteDeleteView(generic.DeleteView):
    model = Athlete
    success_url = reverse_lazy("login")
    template_name = "gym/athlete_delete_confirm.html"


class ExerciseListView(LoginRequiredMixin, generic.ListView):
    model = Exercise
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ExerciseListView, self).get_context_data(**kwargs)
        exercise_name = self.request.GET.get("exercise_name", "")
        context["search_field"] = ExerciseSearchForm(initial={
            "exercise_name": exercise_name
        }
        )
        return context

    def get_queryset(self):
        queryset = Exercise.objects.all().select_related("exercise_creator")
        form = ExerciseSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(
                exercise_name__icontains=form.cleaned_data["exercise_name"]
            )
        return queryset


class ExerciseDetailView(LoginRequiredMixin, generic.DetailView):
    model = Exercise


class ExerciseCreateView(LoginRequiredMixin, generic.CreateView):
    model = Exercise
    fields = "__all__"
    success_url = reverse_lazy("gym:exercise-list")


class ExerciseUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Exercise
    fields = "__all__"
    success_url = reverse_lazy("gym:exercise-list")


class ExerciseDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Exercise
    template_name = "gym/exercise_delete_confirm.html"
    success_url = reverse_lazy("gym:exercise-list")


class TrainingListView(LoginRequiredMixin, generic.ListView):
    model = Training
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TrainingListView, self).get_context_data(**kwargs)
        training_name = self.request.GET.get("training_name", "")
        context["search_field"] = TrainingSearchForm(initial={
            "training_name": training_name
        }
        )
        return context

    def get_queryset(self):
        queryset = Training.objects.all().select_related("training_creator")
        form = TrainingSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(
                training_name__icontains=form.cleaned_data["training_name"]
            )
        return queryset


class TrainingDetailView(LoginRequiredMixin, generic.DetailView):
    model = Training


class TrainingCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = TrainingForm
    success_url = reverse_lazy("gym:training-list")
    template_name = "gym/training_form.html"


class TrainingUpdateView(LoginRequiredMixin, generic.UpdateView):
    form_class = TrainingForm
    model = Training
    success_url = reverse_lazy("gym:training-list")
    template_name = "gym/training_form.html"


class TrainingDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Training
    template_name = "gym/training_delete_confirm.html"
    success_url = reverse_lazy("gym:training-list")
