from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from gym.models import *

EXERCISE_LIST_URL = reverse("gym:exercise-list")
TRAINING_URL = reverse("gym:training-list")
ATHLETE_URL = reverse("gym:athletes-list")


class PublicExerciseTests(TestCase):

    def test_login_required_for_exercise_list(self):
        res = self.client.get(EXERCISE_LIST_URL)

        self.assertNotEqual(res.status_code, 200)


class PrivateExerciseTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="User123",
            password="qwer1234"
        )
        Exercise.objects.create(exercise_creator=self.user, exercise_name="Test1")
        Exercise.objects.create(exercise_creator=self.user, exercise_name="Test2")
        self.client.force_login(self.user)

    def test_retrieve_exercises(self):

        response = self.client.get(EXERCISE_LIST_URL)
        exercises = Exercise.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["exercise_list"]), list(exercises))
        self.assertTemplateUsed(response, "gym/exercise_list.html")

    def test_search_exercise_form(self):
        url = EXERCISE_LIST_URL + "?exercise_name=Test1"
        res = self.client.get(url)

        self.assertContains(res, "Test1")
        self.assertNotContains(res, "Test2")


class PublicTrainingTests(TestCase):

    def test_login_required(self):
        res = self.client.get(TRAINING_URL)

        self.assertNotEqual(res.status_code, 200)


class PrivateManufacturerTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="User123",
            password="qwer1234"
        )
        Training.objects.create(training_name="Test1", training_creator=self.user)
        Training.objects.create(training_name="Test2", training_creator=self.user)

        self.client.force_login(self.user)

    def test_retrieve_training(self):

        response = self.client.get(TRAINING_URL)
        manufacturers = Training.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["training_list"]),
            list(manufacturers)
        )
        self.assertTemplateUsed(response, "gym/training_list.html")

    def test_search_training_form(self):
        url = TRAINING_URL + "?training_name=Test1"
        res = self.client.get(url)

        self.assertContains(res, "Test1")
        self.assertNotContains(res, "Test2")


class PublicAthleteTest(TestCase):
    def test_login_required(self):
        res = self.client.get(ATHLETE_URL)

        self.assertNotEqual(res.status_code, 200)

    def test_create_athlete(self):
        form_data = {
            "username": "TestUser",
            "password1": "qwer1234!",
            "password2": "qwer1234!",
        }
        response = self.client.post(reverse("login"), data=form_data)
        self.assertContains(response, "TestUser")


class PrivateAthleteTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="User123",
            password="qwer1234"
        )
        self.client.force_login(self.user)

    def test_search_athlete_form(self):
        get_user_model().objects.create_user(
            username="test1",
            password="test1234",
        )
        get_user_model().objects.create_user(
            username="test2",
            password="test1234",
        )
        url = ATHLETE_URL + "?username=test1"
        res = self.client.get(url)

        self.assertContains(res, "test1")
        self.assertNotContains(res, "test2")
