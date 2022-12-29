from django.test import TestCase


from gym.forms import AthleteCreationForm


class FormsTest(TestCase):

    def test_athlete_creation_form_with_first_name_last_name_licence(self):
        form_data = {
            "username": "TestUser",
            "password1": "qwer1234!",
            "password2": "qwer1234!",
        }
        form = AthleteCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)
