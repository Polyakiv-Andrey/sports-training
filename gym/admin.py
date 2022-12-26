from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from gym.models import Athlete, Exercise, Training


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ["exercise_name", "exercise_creator", "picture"]
    list_filter = ["exercise_creator"]
    search_fields = ["exercise_name"]


@admin.register(Athlete)
class AthleteAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (("Additional info", {"fields": ("photo", "experience")}),)
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info", {"fields": ("first_name", "last_name", "photo", "experience")}),
    )

admin.site.register(Training)
