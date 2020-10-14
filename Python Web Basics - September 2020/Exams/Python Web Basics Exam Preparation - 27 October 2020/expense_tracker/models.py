from django.db import models


class Profile(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    budget = models.IntegerField()


class Expense(models.Model):
    title = models.CharField(max_length=50)
    image_url = models.URLField(max_length=200)
    description = models.TextField()
    price = models.FloatField()
