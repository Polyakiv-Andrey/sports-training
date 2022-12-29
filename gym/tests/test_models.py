from django.contrib.auth import get_user_model
from django.test import TestCase

from gym.models import *


class ModelsTest(TestCase):

    def test_exercise_str(self):
        athlete = get_user_model().objects.create_user(
            username="test",
            password="test1234",
        )
        exercise = Exercise.objects.create(
            exercise_creator=athlete,
            exercise_name="test_exercise",
            description="Wow",
        )

        self.assertEqual(
            str(exercise), f"{exercise.exercise_name}"
        )

    def test_athlete_without_first_name_and_last_name_str(self):
        athlete = get_user_model().objects.create_user(
            username="test",
            password="test1234",
        )

        self.assertEqual(str(athlete), "test")

    def test_athlete_with_first_name_and_last_name_str(self):
        athlete = get_user_model().objects.create_user(
            username="test",
            password="test1234",
            first_name="test first",
            last_name="test last"
            )
        self.assertEqual(str(athlete), "test first test last")

    def test_training_str(self):
        athlete = get_user_model().objects.create_user(
            username="test",
            password="test1234",
        )
        training = Training.objects.create(
            training_creator=athlete,
            training_name="test_training",
        )

        self.assertEqual(str(training), "test_training")

    def test_create_athlete_with_experience(self):
        username = "test user"
        password = "test password"
        experience = "test experience"
        athlete = get_user_model().objects.create_user(
            username=username,
            password=password,
            experience=experience
        )
        self.assertEqual(athlete.username, username)
        self.assertTrue(athlete.check_password(password))
        self.assertEqual(athlete.experience, experience)
