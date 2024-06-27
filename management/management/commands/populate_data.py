import random

from django.core.management.base import BaseCommand

from management.models import Team, Person


class Command(BaseCommand):
    help = "Populates the database with initial data"

    def handle(self, *args, **kwargs):
        # Clear existing data
        Person.objects.all().delete()
        Team.objects.all().delete()

        # Create Teams
        teams_data = [
            {"name": "Team Alpha", "description": "Alpha team description"},
            {"name": "Team Beta", "description": "Beta team description"},
            {"name": "Team Gamma", "description": "Gamma team description"},
            {"name": "Team Delta", "description": "Delta team description"},
            {"name": "Team Epsilon", "description": "Epsilon team description"},
            {"name": "Team Zeta", "description": "Zeta team description"},
            {"name": "Team Eta", "description": "Eta team description"},
            {"name": "Team Theta", "description": "Theta team description"},
            {"name": "Team Iota", "description": "Iota team description"},
            {"name": "Team Kappa", "description": "Kappa team description"},
        ]

        teams = [Team(**data) for data in teams_data]
        Team.objects.bulk_create(teams)

        # Create People
        first_names = ["Alice", "Bob", "Charlie", "Diana", "Ethan", "Fiona", "George", "Hannah", "Irene", "Jack"]
        last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor"]

        people = []
        for i in range(50):  # Create 50 people
            first_name = random.choice(first_names)
            last_name = random.choice(last_names)
            email = f"{first_name.lower()}.{last_name.lower()}{i}@example.com"
            team = random.choice(teams)
            person = Person(first_name=first_name, last_name=last_name, email=email, team=team)
            people.append(person)

        Person.objects.bulk_create(people)

        self.stdout.write(self.style.SUCCESS("Successfully populated the database with initial data"))
