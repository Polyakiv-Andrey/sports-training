from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


class AdminSiteTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="admin1234"
        )
        self.client.force_login(self.admin_user)
        self.athlete = get_user_model().objects.create_user(
            username="userTom",
            password="pass1234",
        )

    def test_athlete_detailed_photo_listed(self):
        url = reverse("admin:gym_athlete_change", args=[self.athlete.id])
        res = self.client.get(url)

        self.assertContains(res, "photo")
        self.assertContains(res, "experience")

    def test_athlete_detailed_add_fieldsets_listed(self):
        url = reverse("admin:gym_athlete_add")
        res = self.client.get(url)

        self.assertContains(res, "first_name")
        self.assertContains(res, "last_name")
        self.assertContains(res, "photo")
        self.assertContains(res, "experience")
