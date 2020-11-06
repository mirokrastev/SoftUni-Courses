from django.db import models


class Pet(models.Model):
    type = models.CharField(max_length=6)
    name = models.CharField(max_length=6)
    age = models.SmallIntegerField()
    description = models.TextField()
    image_field = models.ImageField(upload_to='images')


class Like(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
