from django.contrib import admin

from management.models import Team, Person


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    ordering = ["name", "created_at"]


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    ordering = ["first_name", "last_name"]
