from django.db import models


class Team(models.Model):
    name = models.CharField("Team Name", max_length=100, unique=True)
    description = models.TextField("Description", blank=True, null=True)
    created_at = models.DateTimeField("Created Date", auto_now_add=True)

    def __str__(self):
        return self.name


class Person(models.Model):
    first_name = models.CharField("First name", max_length=50)
    last_name = models.CharField("Last name", max_length=50)
    email = models.EmailField("Email", unique=True)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True, related_name="members")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
