from django.contrib.auth import get_user_model
from django.test import TestCase


from gym.forms import AthleteCreationForm, TrainingForm
from gym.models import Exercise


class FormsTest(TestCase):

    def test_athlete_creation_form_with_first_name_last_name(self):

        form_data = {
            "username": "TestUser",
            "password1": "qwer1234!",
            "password2": "qwer1234!",
        }
        form = AthleteCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)

    def test_training_form(self):

        athlete = get_user_model().objects.create_user(
            username="test",
            password="test1234",
        )
        exercise = Exercise.objects.create(
            exercise_creator=athlete,
            exercise_name="test_exercise",
            description="Wow",
        )

        form_data = {
            "training_creator": athlete,
            "training_name": "qwer1234!",
            "training_description": "qwer1234!",
            "exercises": [exercise]
        }
        form = TrainingForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(list(form.cleaned_data), list(form_data))
