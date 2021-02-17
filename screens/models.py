from django.db import models
import json

# Create your models here.


class Appointment(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    countries = models.CharField(max_length=500)
    company = models.CharField(max_length=50)
    objectives = models.CharField(max_length=50)
    description = models.CharField(max_length=200)

    def set_countries(self, countries):
        self.countries = json.dumps(countries)

    def get_countries(self):
        return json.loads(self.countries)

    def set_objectives(self, objectives):
        self.objectives = json.dumps(objectives)

    def get_objectives(self):
        return json.loads(self.objectives)


class Company(models.Model):
    name = models.CharField(max_length=50)
    countries = models.CharField(max_length=500)

    def as_dict(self, name, countries):
        return [name, countries]

    def set_countries(self, countries):
        self.countries = json.dumps(countries)

    def get_countries(self):
        return json.loads(self.countries)
